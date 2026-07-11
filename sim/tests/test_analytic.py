"""V1 - analytic agreement.

The simulator must reproduce the closed-form solution of the degenerate case
(homogeneous opportunities, frozen or compounding AI) within stated tolerances:
free-entry participation level, linear pi decline, exclusion beyond the
threshold, and the finite exclusion time under reinvestment (model-notes.md
§2-§3, verified by sim/analysis/analytic_check.py). Until V1 passes, no
experiment counts. See docs/simulation-architecture.md §3.1.
"""

from __future__ import annotations

import numpy as np
import pytest

from sim.core.dynamics import SimConfig, Simulation

# Baseline mirrors sim/analysis/analytic_check.py: S = 5.0, lambda_bar = 3.0.
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
    beta=1.0,
    dt=0.01,
)
LAMBDA_BAR = 3.0


def stationary(lam_a: float, seed: int, t_end: float = 60.0) -> tuple[float, float, float]:
    """Run with frozen AI; time-averaged (lam_h, kappa_h, kappa_a) over the second half."""
    cfg = SimConfig.from_dict(BASE | {"ai_lam0": lam_a, "seed": seed})
    hist = Simulation(cfg).run(t_end).as_arrays()
    half = hist["t"] > t_end / 2  # discard build-up
    return (
        float(hist["lam_h"][half].mean()),
        float(hist["kappa_h"][half].mean()),
        float(hist["kappa_a"][half].mean()),
    )


@pytest.mark.parametrize("lam_a", [0.0, 1.0, 2.0])
def test_free_entry_level(lam_a: float) -> None:
    lam_h, _, _ = stationary(lam_a, seed=1)
    expected = LAMBDA_BAR - lam_a
    assert abs(lam_h - expected) < 0.15 * LAMBDA_BAR, f"lam_h={lam_h:.3f} vs {expected:.3f}"


def test_exclusion_beyond_threshold() -> None:
    lam_h, _, _ = stationary(4.0, seed=2)
    assert lam_h < 0.15 * LAMBDA_BAR, f"lam_h={lam_h:.3f} should be ~0 beyond the threshold"


def test_pi_linear_decline() -> None:
    for lam_a, tol in [(1.0, 0.08), (2.0, 0.08)]:
        _, kappa_h, kappa_a = stationary(lam_a, seed=3)
        pi = kappa_h / (kappa_h + kappa_a)
        expected = 1.0 - lam_a / LAMBDA_BAR
        assert abs(pi - expected) < tol, f"pi={pi:.3f} vs {expected:.3f} at lam_a={lam_a}"


def test_exclusion_time_under_reinvestment() -> None:
    # gamma = eta*c_h/mu_h - delta = 0.06*10 - 0.05 = 0.55; t* = ln(3/0.3)/0.55 ~= 4.19
    # humans exit with a lag ~ patience*c_h/deficit after the threshold, hence the long horizon
    eta, delta, lam0 = 0.06, 0.05, 0.3
    gamma = eta * BASE["c_h"] / BASE["mu_h"] - delta
    t_star = np.log(LAMBDA_BAR / lam0) / gamma
    cfg = SimConfig.from_dict(BASE | {"ai_lam0": lam0, "ai_eta": eta, "ai_delta": delta, "seed": 4})
    hist = Simulation(cfg).run(6.0 * t_star).as_arrays()
    crossed = np.nonzero(hist["lam_a"] >= LAMBDA_BAR)[0]
    assert crossed.size > 0, "AI never crossed the threshold despite gamma > 0"
    t_cross = float(hist["t"][crossed[0]])
    assert abs(t_cross - t_star) < 0.35 * t_star, f"t_cross={t_cross:.2f} vs t*={t_star:.2f}"
    late = hist["t"] > 5.0 * t_star
    assert float(hist["lam_h"][late].mean()) < 0.15 * LAMBDA_BAR, "humans not excluded after t*"
