"""Preliminary E3 check: hysteresis under demand feedback (NOT the production run).

Protocol: AI capability as a *controlled* parameter, ramped slowly up then down;
demand endogenous (beta < 1) vs autonomous (beta = 1). Predictions (pre-registered
in paper/predictions.md, E3): exit near lambda_bar_hi = 3, re-entry near
beta*S - theta (1.0 at beta=0.6), no loop at beta=1.

Run: uv run python sim/analysis/preliminary_e3.py
"""

from __future__ import annotations

import numpy as np

from sim.core.dynamics import SimConfig, Simulation

BASE = dict(
    g=50.0,
    v=1.0,
    theta=2.0,
    mu_h=0.01,
    c_h=0.1,
    n_pool=1000,
    entry_rate=400.0,
    explore_rate=0.2,
    patience=10.0,
    income_ema_rate=1.0,
    n_active_init=300,
    ai_lam0=0.0,
    ai_eta=0.0,
    ai_delta=0.0,
    dt=0.01,
)


def ramp(beta: float, seed: int, lam_max: float = 4.5, t_leg: float = 300.0):
    cfg = SimConfig.from_dict(BASE | {"beta": beta, "seed": seed})
    sim = Simulation(cfg)
    n_steps = int(t_leg / cfg.dt)
    lam_up, lam_h_up, lam_dn, lam_h_dn = [], [], [], []
    for i in range(n_steps):  # up-leg
        sim.ais.lam[0] = lam_max * i / n_steps
        sim.step()
        if i % 100 == 0:
            lam_up.append(sim.ais.lam[0])
            lam_h_up.append(0.01 * sim.humans.n_active)
    for i in range(n_steps):  # down-leg
        sim.ais.lam[0] = lam_max * (1 - i / n_steps)
        sim.step()
        if i % 100 == 0:
            lam_dn.append(sim.ais.lam[0])
            lam_h_dn.append(0.01 * sim.humans.n_active)
    return map(np.asarray, (lam_up, lam_h_up, lam_dn, lam_h_dn))


def crossings(lam: np.ndarray, lam_h: np.ndarray, thresh: float = 0.3) -> float:
    """First control value where participation crosses `thresh` (smoothed)."""
    smooth = np.convolve(lam_h, np.ones(9) / 9, mode="same")
    below = smooth < thresh
    idx = np.flatnonzero(below[1:] != below[:-1])
    return float(lam[idx[0]]) if idx.size else float("nan")


if __name__ == "__main__":
    for beta in (0.6, 1.0):
        lam_up, lam_h_up, lam_dn, lam_h_dn = ramp(beta, seed=42)
        exit_at = crossings(lam_up, lam_h_up)
        reentry_at = crossings(lam_dn, lam_h_dn)
        width = exit_at - reentry_at
        pred_exit, pred_re = 3.0, (beta * 5.0 - 2.0)
        print(
            f"beta={beta}:  exit at Λ_a={exit_at:.2f} (pred ~{pred_exit:.1f})   "
            f"re-entry at Λ_a={reentry_at:.2f} (pred ~{pred_re:.1f})   "
            f"loop width={width:.2f} (pred ~{(1 - beta) * 5.0:.1f})"
        )
