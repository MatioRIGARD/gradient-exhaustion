"""V3 - invariances.

The stationary equilibrium must be stable under seed permutation (with a
confidence interval covering the analytic level within V1 tolerance), under
doubling of the potential-agent reservoir, and under halving of the time step.
See docs/simulation-architecture.md §3.1. (CI uses 10 seeds to stay fast; the
30-seed protocol applies to production experiments, cf. PLAN.md phase 4.)
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
    n_active_init=0,
    ai_lam0=1.5,
    beta=1.0,
    dt=0.01,
)
EXPECTED = 1.5  # lambda_bar - lam_a


def stationary_lam_h(overrides: dict, t_end: float = 60.0) -> float:
    cfg = SimConfig.from_dict(BASE | overrides)
    hist = Simulation(cfg).run(t_end).as_arrays()
    return float(hist["lam_h"][hist["t"] > t_end / 2].mean())


def test_seed_invariance() -> None:
    vals = np.array([stationary_lam_h({"seed": s}) for s in range(10)])
    ci_half = 1.96 * vals.std(ddof=1) / np.sqrt(vals.size)
    assert ci_half < 0.25, f"seed spread too wide: ±{ci_half:.3f}"
    assert abs(vals.mean() - EXPECTED) < 0.15 * 3.0, f"mean={vals.mean():.3f} vs {EXPECTED}"


def test_reservoir_invariance() -> None:
    small = stationary_lam_h({"seed": 21})
    big = stationary_lam_h({"seed": 21, "n_pool": 2000})
    assert abs(big - small) < 0.3, f"reservoir doubling shifted equilibrium: {small:.2f}->{big:.2f}"


def test_timestep_invariance() -> None:
    coarse = stationary_lam_h({"seed": 22})
    fine = stationary_lam_h({"seed": 22, "dt": 0.005})
    assert abs(fine - coarse) < 0.3, f"dt halving shifted equilibrium: {coarse:.2f}->{fine:.2f}"
