"""T3.7 robustness: headline statics must hold under interchangeable decision rules.

Two validated levels (replicator = V1 anchor default, best_response = saturated
bang-bang). The individual-learning level is implemented but not yet calibrated
for this lumpy-income regime (see sim/strategies/learning.py docstring); it is
excluded here on purpose and tracked as a follow-up task.
"""

from __future__ import annotations

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
    beta=1.0,
    dt=0.01,
)


def stationary_lam_h(rule: str, lam_a: float, seed: int = 7, t_end: float = 60.0) -> float:
    cfg = SimConfig.from_dict(BASE | {"ai_lam0": lam_a, "seed": seed, "human_decision": rule})
    hist = Simulation(cfg).run(t_end).as_arrays()
    return float(hist["lam_h"][hist["t"] > t_end / 2].mean())


def test_best_response_coexistence_and_exclusion() -> None:
    mid = stationary_lam_h("best_response", 1.0)
    assert abs(mid - 2.0) < 0.8, f"best_response coexistence off: {mid:.2f} vs 2.0"
    out = stationary_lam_h("best_response", 4.0)
    assert out < 0.45, f"best_response exclusion failed: {out:.2f}"


def test_rules_agree_qualitatively() -> None:
    for rule in ("replicator", "best_response"):
        lo = stationary_lam_h(rule, 2.5)
        hi = stationary_lam_h(rule, 0.5)
        assert hi > lo + 0.8, f"{rule}: participation not decreasing in AI capability"
