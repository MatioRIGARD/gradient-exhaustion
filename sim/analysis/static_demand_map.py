"""Static fixed-point map of the demand coupling (audit follow-up, 2026-07-13).

Independent of the ABM: solves the self-consistent free-entry condition under
the endogenous demand multiplier of sim/core/opportunities.DemandPool,

    Lambda_h + Lambda_a + theta = S * m(D),   D = min(Lambda_h / Lambda_bar, 1),

where m(D) = beta + (1-beta) * h(D) and h is the linear or normalized-Hill
response (exact same formula as the core). The demand multiplier cancels in
per-capture income, so interior human income is kappa_h = (c_h/mu_h)*Lambda_h
and D = kappa_h / ref_income = Lambda_h / Lambda_bar exactly as in the ABM.

For each response shape it reports the band of controlled Lambda_a in which
the map is bistable (a stable interior branch coexists with the absorbing
Lambda_h = 0 state, itself absorbing iff Lambda_a > beta*S - theta, or two
stable interior branches). Purpose: locate where hysteresis is possible in
the *deterministic* map, against which the ABM's measured loop (crossing_gap,
threshold near exclusion) must be read — see notes-production-v1.md addendum.

Usage: uv run python sim/analysis/static_demand_map.py
"""

from __future__ import annotations

import numpy as np

G, V, THETA, MU_H, C_H = 50.0, 1.0, 2.0, 0.01, 0.1  # baseline (predictions.md)
S = G * V * MU_H / C_H  # 5.0
LAMBDA_BAR = S - THETA  # 3.0
BETA = 0.6


def h_response(d: np.ndarray, n: float, k: float) -> np.ndarray:
    if n <= 0:
        return d
    dn, kn = d**n, k**n
    return dn * (1.0 + kn) / (dn + kn)


def multiplier(lam_h: np.ndarray, n: float, k: float) -> np.ndarray:
    d = np.minimum(lam_h / LAMBDA_BAR, 1.0)
    return BETA + (1.0 - BETA) * h_response(d, n, k)


def stable_interior_roots(lam_a: float, n: float, k: float) -> list[float]:
    """Roots of F(x) = S*m(x) - theta - lam_a - x on (0, S], keeping F' < 0."""
    xs = np.linspace(1e-6, S, 20001)
    f = S * multiplier(xs, n, k) - THETA - lam_a - xs
    roots = []
    sign_change = np.nonzero(np.diff(np.sign(f)) != 0)[0]
    for i in sign_change:
        x0 = float(np.interp(0.0, [f[i + 1], f[i]], [xs[i + 1], xs[i]]))
        slope = (f[i + 1] - f[i]) / (xs[i + 1] - xs[i])
        if slope < 0:
            roots.append(x0)
    return roots


def bistable_band(n: float, k: float, grid: int = 1200) -> tuple[float, float] | None:
    lam_as = np.linspace(0.0, 4.5, grid)
    zero_absorbing = lam_as > BETA * S - THETA
    bistable = []
    for la, z_abs in zip(lam_as, zero_absorbing, strict=True):
        stable = stable_interior_roots(la, n, k)
        n_states = len(stable) + (1 if z_abs else 0)
        bistable.append(n_states >= 2)
    idx = np.nonzero(bistable)[0]
    if idx.size == 0:
        return None
    return float(lam_as[idx[0]]), float(lam_as[idx[-1]])


if __name__ == "__main__":
    print(f"Baseline: S={S}, Lambda_bar={LAMBDA_BAR}, beta={BETA}, "
          f"Lambda_h=0 absorbing for Lambda_a > {BETA * S - THETA:.2f}")
    cases = [("linear (n<=0)", 0.0, 0.5), ("steep mid-range (n=8, K=0.5)", 8.0, 0.5),
             ("steep late (n=8, K=0.05)", 8.0, 0.05)]
    for label, n, k in cases:
        band = bistable_band(n, k)
        if band is None:
            print(f"{label:32s} no bistable band (fully reversible map)")
        else:
            print(f"{label:32s} bistable for Lambda_a in [{band[0]:.2f}, {band[1]:.2f}] "
                  f"(width {band[1] - band[0]:.2f})")
    print(f"two-state reference width (1-beta)*S = {(1 - BETA) * S:.2f}")
