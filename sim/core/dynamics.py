"""Main loop: reinvestment and endogenous entry/exit.

The feedback loop of the model: capture -> revenue -> reinvestment -> better
capture. Humans enter and exit on a local income signal (their market exit is
the observed variable and must never be forced); AI operators compound intensity
through reinvestment; opportunity values respond to circulating human income
through the demand pool. Every parameter comes from SimConfig — no magic numbers.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any

import numpy as np

from sim.core.agents import AIPopulation, HumanPopulation
from sim.core.capture import run_races
from sim.core.opportunities import DemandPool, OpportunityPool
from sim.strategies.base import make_rule


@dataclass
class SimConfig:
    # opportunities
    g: float  # arrival rate
    v: float  # base opportunity value
    theta: float  # expiry rate
    difficulty_lo: float = 0.0
    difficulty_hi: float = 0.0
    # humans
    n_pool: int = 2000
    mu_h: float = 0.05
    c_h: float = 0.5
    human_ceiling: float = float("inf")
    entry_rate: float = 50.0
    explore_rate: float = 5.0
    patience: float = 8.0
    income_ema_rate: float = 1.0
    n_active_init: int = 0
    # AI
    ai_lam0: float = 0.0
    ai_eta: float = 0.0
    ai_delta: float = 0.0
    ai_ceiling: float = float("inf")
    ai_lam_max: float = float("inf")
    ai_n_operators: int = 1
    ai_rent_dissipation: float = 0.0  # share of capture value burned by operator competition
    ai_collude: bool = False  # colluding operators dissipate nothing
    redistribution_rate: float = 0.0  # tax on AI effective income, transferred to humans
    # demand
    human_decision: str = "replicator"  # replicator | best_response | learning
    decision_params: dict[str, float] = field(default_factory=dict)
    # demand (part 2)
    beta: float = 1.0  # autonomous share; 1.0 = exogenous values
    demand_smoothing: float = 2.0
    demand_hill_n: float = 0.0  # <=0: linear response (legacy)
    demand_hill_k: float = 0.5
    # integration
    dt: float = 0.01
    seed: int = 0

    @classmethod
    def from_dict(cls, d: dict[str, Any]) -> SimConfig:
        return cls(**d)

    @property
    def s_intensity(self) -> float:
        """Analytic saturation intensity S = g v mu_h / c_h (reporting only)."""
        return self.g * self.v * self.mu_h / self.c_h


@dataclass
class History:
    t: list[float] = field(default_factory=list)
    lam_h: list[float] = field(default_factory=list)
    lam_a: list[float] = field(default_factory=list)
    n_active: list[int] = field(default_factory=list)
    kappa_h: list[float] = field(default_factory=list)  # smoothed flow
    kappa_a: list[float] = field(default_factory=list)  # smoothed flow
    t_h: list[float] = field(default_factory=list)  # smoothed transfer flow
    value_multiplier: list[float] = field(default_factory=list)

    def as_arrays(self) -> dict[str, np.ndarray]:
        return {k: np.asarray(v) for k, v in self.__dict__.items()}


class Simulation:
    def __init__(self, cfg: SimConfig):
        self.cfg = cfg
        self.rng = np.random.default_rng(cfg.seed)
        self.opps = OpportunityPool()
        self.humans = HumanPopulation.homogeneous(cfg.n_pool, cfg.mu_h, cfg.c_h, cfg.human_ceiling)
        self.humans.entry_rate = cfg.entry_rate
        self.humans.explore_rate = cfg.explore_rate
        self.humans.patience = cfg.patience
        self.humans.ema_rate = cfg.income_ema_rate
        self.humans.income_ema = cfg.c_h  # start at break-even belief
        if cfg.n_active_init > 0:
            self.humans.activate(np.arange(cfg.n_active_init))
        self.ais = AIPopulation.create(
            cfg.ai_n_operators, cfg.ai_lam0, cfg.ai_eta, cfg.ai_delta, cfg.ai_ceiling,
            cfg.ai_lam_max,
        )
        # warm-start the pool at its stationary count for the initial intensities,
        # so the income signal is unbiased from t=0 (no cold-start starvation)
        lam0 = cfg.mu_h * cfg.n_active_init + cfg.ai_lam0
        n_warm = int(round(cfg.g / (lam0 + cfg.theta)))
        self.opps = OpportunityPool()
        self.opps.spawn(self.rng, n_warm, cfg.v, 1.0, (cfg.difficulty_lo, cfg.difficulty_hi))
        # reference human income = analytic full-participation flow at beta=1
        ref = max(cfg.g * cfg.v - (cfg.c_h / cfg.mu_h) * cfg.theta, 1e-12)
        self.demand = DemandPool(
            cfg.beta, ref_income=ref, smoothing=cfg.demand_smoothing,
            hill_n=cfg.demand_hill_n, hill_k=cfg.demand_hill_k,
        )
        self.rule = make_rule(cfg.human_decision, cfg.n_pool, cfg.decision_params)
        self.t = 0.0
        self.kappa_h_flow = 0.0  # EMA of human capture income flow
        self.kappa_a_flow = 0.0
        self.t_flow = 0.0  # EMA of transfer flow to humans (redistribution)
        self.flow_ema_rate = cfg.income_ema_rate

    def step(self) -> None:
        cfg, dt, rng = self.cfg, self.cfg.dt, self.rng
        self.opps.spawn(
            rng,
            rng.poisson(cfg.g * dt),
            cfg.v,
            self.demand.multiplier,
            (cfg.difficulty_lo, cfg.difficulty_hi),
        )
        out = run_races(self.opps, self.humans, self.ais, cfg.theta, dt, rng)
        self.opps.remove(out.gone)

        # operator competition dissipates a share of captured value unless they
        # collude (E4.2); dissipated value is burned — reported, not recirculated
        n_ops = self.ais.lam.size
        dissip = 0.0 if cfg.ai_collude else cfg.ai_rent_dissipation * (1.0 - 1.0 / n_ops)
        ai_income_eff = out.ai_income * (1.0 - dissip)
        ai_per_op_eff = out.ai_income_per_operator * (1.0 - dissip)
        # redistribution: tax on AI effective income, transferred to humans (T channel)
        t_transfer = cfg.redistribution_rate * ai_income_eff
        ai_income_net = ai_income_eff - t_transfer
        ai_per_op_net = ai_per_op_eff * (1.0 - cfg.redistribution_rate)

        a = min(1.0, self.flow_ema_rate * dt)
        self.kappa_h_flow += a * (out.human_income / dt - self.kappa_h_flow)
        self.kappa_a_flow += a * (ai_income_net / dt - self.kappa_a_flow)
        self.t_flow += a * (t_transfer / dt - self.t_flow)

        expected_flow = float(self.humans.mu.mean()) * float(self.opps.value.sum())
        self.humans.update_signal(expected_flow, dt)
        self.humans.tick(dt)
        self.rule.apply(self.humans, rng, dt)
        self.ais.reinvest(ai_per_op_net / dt, dt)
        # DEC-002: demand is fed by TOTAL human disposable income (capture + transfers)
        self.demand.update(self.kappa_h_flow + self.t_flow, dt)
        self.t += dt

    def run(self, t_end: float, record_every: int = 10) -> History:
        hist = History()
        n_steps = int(round(t_end / self.cfg.dt))
        for i in range(n_steps):
            self.step()
            if i % record_every == 0:
                hist.t.append(self.t)
                hist.lam_h.append(float(self.humans.mu[self.humans.active].sum()))
                hist.lam_a.append(float(self.ais.lam.sum()))
                hist.n_active.append(self.humans.n_active)
                hist.kappa_h.append(self.kappa_h_flow)
                hist.kappa_a.append(self.kappa_a_flow)
                hist.t_h.append(self.t_flow)
                hist.value_multiplier.append(self.demand.multiplier)
        return hist
