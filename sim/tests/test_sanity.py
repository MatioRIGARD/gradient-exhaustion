"""V2 - non-tautology (epistemic guardrail in CI).

Without AI the market must be stationary with pi = 1; with frozen-capacity AI
below the threshold, coexistence must be stable (pi bounded away from 0 and 1
indefinitely); with decaying AI (gamma < 0) the model must produce HUMAN
dominance. If exclusion occurs without the compounding advantage, the model is
tautological (criterion K1). If this test fails, fix the core -- never weaken
the test (CLAUDE.md rule #1). See docs/simulation-architecture.md §3.1.
"""

from __future__ import annotations

from sim.core.dynamics import SimConfig, Simulation
from sim.metrics.indices import pi_market, stationary_mean

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


def run(overrides: dict, t_end: float):
    cfg = SimConfig.from_dict(BASE | overrides)
    return Simulation(cfg).run(t_end).as_arrays()


def test_no_ai_stationary_and_full_pi() -> None:
    hist = run({"ai_lam0": 0.0, "seed": 11}, t_end=80.0)
    third = hist["t"].size // 3
    m1 = hist["lam_h"][third : 2 * third].mean()
    m2 = hist["lam_h"][2 * third :].mean()
    assert abs(m2 - m1) < 0.15 * LAMBDA_BAR, f"not stationary: {m1:.2f} -> {m2:.2f}"
    pi = stationary_mean(hist["t"], pi_market(hist["kappa_h"], hist["kappa_a"]))
    assert pi > 0.999, f"pi={pi} with no AI"


def test_frozen_ai_coexists_indefinitely() -> None:
    hist = run({"ai_lam0": 2.5, "seed": 12}, t_end=120.0)
    late = hist["t"] > 90.0
    lam_h_late = float(hist["lam_h"][late].mean())
    assert lam_h_late > 0.1, f"exclusion at frozen AI (lam_h={lam_h_late:.3f}): tautology"
    pi = stationary_mean(hist["t"], pi_market(hist["kappa_h"], hist["kappa_a"]), 0.75)
    assert 0.02 < pi < 0.6, f"pi={pi:.3f} out of coexistence range"


def test_decaying_ai_yields_human_dominance() -> None:
    # gamma = eta*c_h/mu_h - delta = 0.02*10 - 0.5 < 0: AI cannot sustain itself
    hist = run({"ai_lam0": 2.0, "ai_eta": 0.02, "ai_delta": 0.5, "seed": 13}, t_end=60.0)
    late = hist["t"] > 45.0
    assert float(hist["lam_a"][late].mean()) < 0.05, "AI did not decay despite gamma < 0"
    pi = stationary_mean(hist["t"], pi_market(hist["kappa_h"], hist["kappa_a"]), 0.75)
    assert pi > 0.95, f"humans did not dominate after AI decay (pi={pi:.3f})"
