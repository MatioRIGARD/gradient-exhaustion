"""Numeric verification of paper/model-notes.md (T2.2/T2.3).

Checks, against Monte-Carlo and ODE integration:
  C1  capture-share formulas (competing exponentials)          [notes §1]
  C2  free-entry equilibrium and viability threshold  Λ̄        [notes §2]
  C3  linearity of π_market in Λ_a over the interior regime    [notes §2]
  C4  exclusion time t* and post-exclusion fixed point Λ_a**   [notes §3]
  C5  hysteresis thresholds Λ̄_exit / Λ̄_re and band width      [notes §4]

Run:  uv run python sim/analysis/analytic_check.py
Exits non-zero on any FAIL.
"""

from __future__ import annotations

import sys

import numpy as np

RNG = np.random.default_rng(20260713)

# Baseline parameters (arbitrary but generic; C1-C5 sweep around them).
G = 50.0  # opportunity arrival rate
V = 1.0  # opportunity value
THETA = 2.0  # gradient decay rate
MU_H = 0.05  # per-human detection intensity
C_H = 0.5  # per-human participation cost flow

S = G * V * MU_H / C_H  # saturation intensity  (= 5.0 here)
LAMBDA_BAR = S - THETA  # viability threshold    (= 3.0 here)

FAILURES: list[str] = []


def check(name: str, ok: bool, detail: str) -> None:
    status = "PASS" if ok else "FAIL"
    print(f"[{status}] {name}: {detail}")
    if not ok:
        FAILURES.append(name)


# ── C1: capture-share formulas ──────────────────────────────────────────────


def mc_shares(lam_h: float, lam_a: float, theta: float, n: int = 400_000) -> tuple[float, float]:
    """Monte-Carlo estimate of (human, ai) capture probabilities for one opportunity.

    Detection times are exponential; the race winner is the earliest of
    human detection, AI detection, and expiry. Per-opportunity independence
    makes this equivalent to the full arrival-process simulation.
    """
    t_h = RNG.exponential(1.0 / lam_h, n) if lam_h > 0 else np.full(n, np.inf)
    t_a = RNG.exponential(1.0 / lam_a, n) if lam_a > 0 else np.full(n, np.inf)
    t_x = RNG.exponential(1.0 / theta, n)
    stacked = np.vstack([t_h, t_a, t_x])
    winner = np.argmin(stacked, axis=0)
    return float(np.mean(winner == 0)), float(np.mean(winner == 1))


def c1() -> None:
    for lam_h, lam_a in [(1.0, 0.5), (2.5, 2.5), (0.3, 4.0)]:
        tot = lam_h + lam_a + THETA
        p_h_mc, p_a_mc = mc_shares(lam_h, lam_a, THETA)
        p_h_th, p_a_th = lam_h / tot, lam_a / tot
        err = max(abs(p_h_mc - p_h_th), abs(p_a_mc - p_a_th))
        check(
            f"C1 shares (Λ_h={lam_h}, Λ_a={lam_a})",
            err < 3e-3,
            f"max|MC-theory|={err:.2e}",
        )


# ── C2: free-entry equilibrium ──────────────────────────────────────────────


def gross_per_capita(n_h: float, lam_a: float) -> float:
    lam_h = n_h * MU_H
    return G * V * MU_H / (lam_h + lam_a + THETA)


def free_entry_n(lam_a: float) -> float:
    """Largest participation level with non-negative net income (continuum)."""
    lo, hi = 0.0, 10 * S / MU_H
    if gross_per_capita(0.0, lam_a) <= C_H:
        return 0.0
    for _ in range(200):
        mid = (lo + hi) / 2
        lo, hi = (mid, hi) if gross_per_capita(mid, lam_a) > C_H else (lo, mid)
    return lo


def c2() -> None:
    for lam_a in [0.0, 1.0, 2.0, 2.9, 3.5, 6.0]:
        lam_h_num = free_entry_n(lam_a) * MU_H
        lam_h_th = max(0.0, LAMBDA_BAR - lam_a)
        err = abs(lam_h_num - lam_h_th)
        check(
            f"C2 free entry (Λ_a={lam_a})",
            err < 1e-6,
            f"Λ_h*={lam_h_num:.6f} vs theory {lam_h_th:.6f}",
        )
    lam_h_at_bar = free_entry_n(LAMBDA_BAR) * MU_H
    check("C2 threshold exact", lam_h_at_bar < 1e-6, f"Λ_h*(Λ̄)={lam_h_at_bar:.2e}")


# ── C3: linear π in the interior regime ─────────────────────────────────────


def c3() -> None:
    lam_as = np.linspace(0.0, LAMBDA_BAR, 13)[1:-1]
    pis = []
    for lam_a in lam_as:
        lam_h = max(0.0, LAMBDA_BAR - lam_a)
        tot = lam_h + lam_a + THETA
        k_h, k_a = G * V * lam_h / tot, G * V * lam_a / tot
        pis.append(k_h / (k_h + k_a))
    pis = np.array(pis)
    theory = 1.0 - lam_as / LAMBDA_BAR
    err = float(np.max(np.abs(pis - theory)))
    check("C3 π linearity", err < 1e-12, f"max|π - (1-Λ_a/Λ̄)|={err:.2e}")
    total_flow = []
    for lam_a in lam_as:
        lam_h = LAMBDA_BAR - lam_a
        total_flow.append(G * V * (lam_h + lam_a) / (lam_h + lam_a + THETA))
    spread = float(np.ptp(total_flow))
    check("C3 constant earned flow", spread < 1e-12, f"ptp={spread:.2e}")


# ── C4: dynamics — exclusion time and post-exclusion fixed point ────────────


def kappa_a(lam_a: float, v: float = V) -> float:
    """AI income with humans at instantaneous free-entry response (value v)."""
    s = G * v * MU_H / C_H
    lam_bar = s - THETA
    lam_h = max(0.0, lam_bar - lam_a)
    return G * v * lam_a / (lam_h + lam_a + THETA)


def integrate(lam0: float, eta: float, delta: float, t_end: float, dt: float = 1e-4):
    ts = np.arange(0.0, t_end, dt)
    lam = np.empty_like(ts)
    x = lam0
    for i, _ in enumerate(ts):
        lam[i] = x
        x += dt * (eta * kappa_a(x) - delta * x)
    return ts, lam


def c4() -> None:
    eta, delta = 1.2, 0.5
    gamma = eta * C_H / MU_H - delta  # = 11.5 with baseline params
    check("C4 γ sign", gamma > 0, f"γ={gamma:.3f} (growth regime)")
    lam0 = 0.05
    t_star_th = np.log(LAMBDA_BAR / lam0) / gamma
    ts, lam = integrate(lam0, eta, delta, t_end=2.0 * t_star_th)
    crossed = np.nonzero(lam >= LAMBDA_BAR)[0]
    t_star_num = ts[crossed[0]] if crossed.size else np.inf
    err = abs(t_star_num - t_star_th) / t_star_th
    check("C4 exclusion time t*", err < 0.02, f"num={t_star_num:.4f} vs th={t_star_th:.4f}")

    fp_th = eta * G * V / delta - THETA
    ts2, lam2 = integrate(LAMBDA_BAR * 1.01, eta, delta, t_end=40.0, dt=1e-3)
    err_fp = abs(lam2[-1] - fp_th) / fp_th
    check("C4 fixed point Λ_a**", err_fp < 0.01, f"num={lam2[-1]:.3f} vs th={fp_th:.3f}")
    check("C4 Λ_a** > Λ̄ (absorbing)", fp_th > LAMBDA_BAR, f"{fp_th:.2f} > {LAMBDA_BAR:.2f}")

    eta_low = 0.5 * delta * MU_H / C_H  # γ = -δ/2 = -0.25
    _, lam3 = integrate(0.5, eta_low, delta, t_end=40.0, dt=1e-3)
    check("C4 decay when γ<0", lam3[-1] < 0.01, f"Λ_a(end)={lam3[-1]:.2e}")


# ── C5: hysteresis under two-state demand ───────────────────────────────────


def c5() -> None:
    beta = 0.6
    v_hi, v_lo = V, beta * V
    bar_exit = G * v_hi * MU_H / C_H - THETA
    bar_re = G * v_lo * MU_H / C_H - THETA
    width_th = (1 - beta) * (bar_exit + THETA)

    lam_grid_up = np.linspace(0.0, 1.5 * bar_exit, 4001)
    humans_in = True
    exit_at = None
    for lam_a in lam_grid_up:  # quasi-static ramp up
        v = v_hi if humans_in else v_lo
        lam_bar = G * v * MU_H / C_H - THETA
        if humans_in and lam_a >= lam_bar:
            humans_in, exit_at = False, lam_a
    re_at = None
    for lam_a in lam_grid_up[::-1]:  # ramp down from excluded state
        v = v_hi if humans_in else v_lo
        lam_bar = G * v * MU_H / C_H - THETA
        if not humans_in and lam_a < lam_bar:
            humans_in, re_at = True, lam_a
    ok = (
        exit_at is not None
        and re_at is not None
        and abs(exit_at - bar_exit) < 0.01
        and abs(re_at - bar_re) < 0.01
    )
    check(
        "C5 hysteresis thresholds",
        ok,
        f"exit={exit_at:.3f} (th {bar_exit:.3f}), re-entry={re_at:.3f} (th {bar_re:.3f})",
    )
    check(
        "C5 band width ∝ (1-β)",
        abs((exit_at - re_at) - width_th) < 0.02,
        f"width={exit_at - re_at:.3f} vs th={width_th:.3f}",
    )


if __name__ == "__main__":
    print(f"Baseline: S={S:.2f}, Λ̄={LAMBDA_BAR:.2f}\n")
    c1()
    c2()
    c3()
    c4()
    c5()
    print(f"\n{'ALL CHECKS PASS' if not FAILURES else 'FAILURES: ' + ', '.join(FAILURES)}")
    sys.exit(1 if FAILURES else 0)
