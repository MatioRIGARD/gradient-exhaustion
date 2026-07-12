"""Agent populations held as numpy arrays (no per-agent objects).

Two economic species differing ONLY by parameter values, never by special rules
(anti-tautology rule #1). Both populations expose the same interface: a detection
intensity brought to each opportunity's race (possibly zero when the opportunity's
difficulty exceeds an agent's capability ceiling) and an income account. What
differs is parameter structure: humans have fixed (mu, cost, ceiling) and decide
participation by entry/exit; AI operators compound intensity through reinvestment
(eta, delta) — the load-bearing asymmetry A7 of model-notes.md, expressed as
parameters, not rules.
"""

from __future__ import annotations

from dataclasses import dataclass, field

import numpy as np


@dataclass
class HumanPopulation:
    """Potential human participants; `active` marks current entrants.

    Entry/exit is a local rule (A5 relaxed to finite rates). Each participant
    keeps its own account: it enters with a grubstake (patience * cost), pays
    its participation cost continuously, credits its own captures, and exits
    when its account is exhausted (bankruptcy). Capture income arrives in rare
    lumps, so exits must be patient rather than signal-triggered — otherwise
    noise rectification empties the market even at profitable parameters.
    Entry combines signal-independent exploration (which keeps re-entry
    possible from an empty market: an absorbing zero-participation state would
    be a construction artefact) with imitation proportional to the observed
    excess income of incumbents. No agent ever consults the analytic solution.
    """

    mu: np.ndarray  # per-agent detection intensity
    cost: np.ndarray  # per-agent participation cost flow
    ceiling: np.ndarray  # max difficulty the agent can exploit
    active: np.ndarray  # bool
    wealth: np.ndarray  # per-agent account while active
    patience: float = 8.0  # grubstake in units of (cost * time)
    income_ema: float = 0.0  # smoothed per-capita earned income of incumbents
    ema_rate: float = 1.0  # EMA rate per unit time
    entry_rate: float = 50.0  # imitation entries per unit time at 100% excess income
    explore_rate: float = 5.0  # signal-independent probing entries per unit time

    @classmethod
    def homogeneous(cls, n_pool: int, mu: float, cost: float, ceiling: float = np.inf):
        return cls(
            mu=np.full(n_pool, mu),
            cost=np.full(n_pool, cost),
            ceiling=np.full(n_pool, ceiling),
            active=np.zeros(n_pool, dtype=bool),
            wealth=np.zeros(n_pool),
        )

    @property
    def n_active(self) -> int:
        return int(self.active.sum())

    def intensity_for(self, difficulty: np.ndarray) -> np.ndarray:
        """Total active human intensity eligible for each opportunity."""
        act_mu = self.mu[self.active]
        act_ceil = self.ceiling[self.active]
        if act_mu.size == 0:
            return np.zeros_like(difficulty)
        order = np.argsort(act_ceil)
        sorted_ceil = act_ceil[order]
        csum = np.concatenate([[0.0], np.cumsum(act_mu[order])])
        first_ok = np.searchsorted(sorted_ceil, difficulty, side="left")
        return csum[-1] - csum[first_ok]

    def pick_winner(self, difficulty: float, rng: np.random.Generator) -> int:
        """Sample the capturing agent among eligible actives, proportional to mu."""
        idx = np.flatnonzero(self.active & (self.ceiling >= difficulty))
        w = self.mu[idx]
        return int(rng.choice(idx, p=w / w.sum()))

    def credit(self, agent_idx: int, value: float) -> None:
        """Add capture income, capped at the grubstake: agents maintain a
        working buffer and consume the surplus (otherwise past luck banks
        into unbounded exit lags and the free-entry equilibrium blurs)."""
        cap = self.patience * self.cost[agent_idx]
        self.wealth[agent_idx] = min(self.wealth[agent_idx] + value, cap)

    def update_signal(self, expected_flow: float, dt: float) -> None:
        """Entry signal = a prospective entrant's expected capture flow.

        Races are memoryless, so an agent with intensity mu expects to capture
        value at rate mu * (total value of currently open opportunities) —
        market thickness, a public and slowly-varying statistic. Competition
        enters through pool depletion, not through observing rivals' incomes;
        this keeps the signal finite and stampede-free at any headcount. No
        analytic solution is consulted: the free-entry correspondence is
        emergent."""
        a = min(1.0, self.ema_rate * dt)
        self.income_ema += a * (expected_flow - self.income_ema)

    def activate(self, idx: np.ndarray) -> None:
        self.active[idx] = True
        self.wealth[idx] = self.patience * self.cost[idx]

    def tick(self, dt: float) -> None:
        """Shared mechanics under every decision rule: participation-cost
        drain and the bankruptcy backstop. Voluntary entry/exit lives in the
        pluggable decision rules (sim/strategies/)."""
        self.wealth[self.active] -= self.cost[self.active] * dt
        self.active &= self.wealth > 0.0


@dataclass
class AIPopulation:
    """AI operators: intensity compounds with reinvested income (A7).

    lam_max is the optional capability saturation of audit row A7' (rising
    marginal cost of capability): with lam_max below the human viability
    threshold, the model predicts a stable coexistence region.
    """

    lam: np.ndarray  # per-operator detection intensity
    eta: np.ndarray  # income -> capability conversion rate
    delta: np.ndarray  # capability depreciation rate
    ceiling: np.ndarray = field(default_factory=lambda: np.empty(0))
    lam_max: np.ndarray = field(default_factory=lambda: np.empty(0))

    @classmethod
    def create(
        cls,
        n_operators: int,
        lam0_total: float,
        eta: float,
        delta: float,
        ceiling: float = np.inf,
        lam_max: float = np.inf,
    ):
        n = max(1, n_operators)
        return cls(
            lam=np.full(n, lam0_total / n),
            eta=np.full(n, eta),
            delta=np.full(n, delta),
            ceiling=np.full(n, ceiling),
            lam_max=np.full(n, lam_max),
        )

    @classmethod
    def single(cls, lam0: float, eta: float, delta: float, ceiling: float = np.inf):
        return cls.create(1, lam0, eta, delta, ceiling)

    def intensity_for(self, difficulty: np.ndarray) -> np.ndarray:
        order = np.argsort(self.ceiling)
        csum = np.concatenate([[0.0], np.cumsum(self.lam[order])])
        first_ok = np.searchsorted(self.ceiling[order], difficulty, side="left")
        return csum[-1] - csum[first_ok]

    def pick_winner(self, difficulty: float, rng: np.random.Generator) -> int:
        idx = np.flatnonzero(self.ceiling >= difficulty)
        w = self.lam[idx]
        return int(rng.choice(idx, p=w / w.sum()))

    def reinvest(self, income_per_operator: np.ndarray, dt: float) -> None:
        self.lam += dt * (self.eta * income_per_operator - self.delta * self.lam)
        np.clip(self.lam, 0.0, self.lam_max, out=self.lam)
