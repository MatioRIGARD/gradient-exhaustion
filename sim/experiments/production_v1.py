"""Production experiments E1-E4 (first pass; seeds to be densified by a later task).

Usage:  uv run python sim/experiments/production_v1.py --exp e1|e2|e2b|e3|e3conf|e4|e5|e4b|e6
Data:   results/<exp>.npz (config embedded; gitignored)
Figures: paper/figures/f*.png (committed)
Verdicts vs paper/predictions.md are written by the analysis notes, not here.
"""

from __future__ import annotations

import argparse
import json
from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

from sim.core.dynamics import SimConfig, Simulation

ROOT = Path(__file__).resolve().parents[2]
RESULTS = ROOT / "results"
FIGURES = ROOT / "paper" / "figures"

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

# Validated palette (dataviz reference instance, light mode).
SEQ = ["#9ec5f4", "#6da7ec", "#3987e5", "#256abf", "#184f95", "#0d366b"]  # light->dark
CAT = ["#2a78d6", "#1baf7a", "#eda100", "#008300"]  # fixed slot order

plt.rcParams.update(
    {
        "figure.facecolor": "white",
        "axes.spines.top": False,
        "axes.spines.right": False,
        "axes.grid": True,
        "grid.alpha": 0.25,
        "grid.linewidth": 0.6,
        "lines.linewidth": 1.8,
        "font.size": 10,
        "axes.titlesize": 11,
        "figure.dpi": 200,
    }
)


def run_once(overrides: dict, t_end: float) -> dict[str, np.ndarray]:
    cfg = SimConfig.from_dict(BASE | overrides)
    return Simulation(cfg).run(t_end).as_arrays()


def pi_series(hist: dict[str, np.ndarray]) -> np.ndarray:
    tot = hist["kappa_h"] + hist["kappa_a"]
    return np.where(tot > 0, hist["kappa_h"] / np.maximum(tot, 1e-12), np.nan)


def save(exp: str, **arrays) -> None:
    RESULTS.mkdir(exist_ok=True)
    FIGURES.mkdir(exist_ok=True)
    np.savez_compressed(RESULTS / f"{exp}.npz", **arrays)


# ── E1: pi(t) vs AI progress rate ───────────────────────────────────────────


def e1(seeds: int = 30) -> None:
    etas = [0.003, 0.01, 0.02, 0.04, 0.08]
    t_end, delta, lam0 = 60.0, 0.05, 0.3
    curves = {}
    for eta in etas:
        pis = []
        for s in range(seeds):
            h = run_once({"ai_lam0": lam0, "ai_eta": eta, "ai_delta": delta, "seed": s}, t_end)
            pis.append(pi_series(h))
        t = h["t"]
        arr = np.vstack(pis)
        curves[eta] = (arr.mean(axis=0), arr.std(axis=0) / np.sqrt(seeds))
    save("e1", t=t, etas=np.array(etas), config=np.array(json.dumps(BASE)), **{
        f"pi_{eta}": np.vstack(curves[eta]) for eta in etas
    })

    fig, ax = plt.subplots(figsize=(6.4, 4.0))
    for eta, color in zip(etas, SEQ[1:], strict=False):
        mean, se = curves[eta]
        gamma = eta * 10 - delta
        ax.plot(t, mean, color=color, label=f"η={eta} (γ={gamma:+.2f})")
        ax.fill_between(t, mean - 1.96 * se, mean + 1.96 * se, color=color, alpha=0.18, lw=0)
    ax.set(xlabel="time", ylabel="π (human share of earned flow)", ylim=(-0.02, 1.05),
           title="F1 — Human participation vs AI reinvestment efficiency η")
    ax.legend(frameon=False, fontsize=8)
    fig.tight_layout()
    fig.savefig(FIGURES / "f1_pi_dynamics.png")
    print("E1 done")


# ── E2: phase diagram eta x delta ───────────────────────────────────────────


def e2(seeds: int = 10) -> None:
    etas = np.linspace(0.002, 0.05, 9)
    deltas = np.linspace(0.02, 0.5, 9)
    t_end = 100.0
    grid = np.zeros((len(deltas), len(etas)))
    for i, delta in enumerate(deltas):
        for j, eta in enumerate(etas):
            vals = []
            for s in range(seeds):
                h = run_once(
                    {"ai_lam0": 0.3, "ai_eta": float(eta), "ai_delta": float(delta), "seed": s},
                    t_end,
                )
                pi = pi_series(h)
                late = h["t"] > 0.8 * t_end
                vals.append(np.nanmean(pi[late]))
            grid[i, j] = float(np.mean(vals))
        print(f"E2 row {i + 1}/{len(deltas)} done")
    save("e2", etas=etas, deltas=deltas, grid=grid)

    fig, ax = plt.subplots(figsize=(5.6, 4.4))
    cmap = matplotlib.colors.LinearSegmentedColormap.from_list("seq", ["#0d366b", "#cde2fb"])
    im = ax.imshow(grid, origin="lower", aspect="auto", cmap=cmap, vmin=0, vmax=1,
                   extent=(etas[0], etas[-1], deltas[0], deltas[-1]))
    ax.plot(etas, 10 * etas, color="#e34948", lw=1.8, label="predicted boundary δ = 10η (γ=0)")
    ax.set(xlabel="η (reinvestment efficiency)", ylabel="δ (capability depreciation)",
           ylim=(deltas[0], deltas[-1]),
           title="F2 — Phase diagram: final π (dark = humans excluded)")
    fig.colorbar(im, ax=ax, label="final π")
    ax.legend(frameon=False, fontsize=8, loc="upper left")
    fig.tight_layout()
    fig.savefig(FIGURES / "f2_phase_diagram.png")
    print("E2 done")


# ── E2b: coexistence under capability saturation (A7') ─────────────────────


def e2b(seeds: int = 10) -> None:
    caps = np.linspace(0.5, 6.0, 8)
    t_end = 80.0
    means, ses = [], []
    for cap in caps:
        vals = []
        for s in range(seeds):
            h = run_once(
                {"ai_lam0": 0.3, "ai_eta": 0.06, "ai_delta": 0.05,
                 "ai_lam_max": float(cap), "seed": s},
                t_end,
            )
            late = h["t"] > 0.75 * t_end
            vals.append(np.nanmean(pi_series(h)[late]))
        means.append(np.mean(vals))
        ses.append(np.std(vals) / np.sqrt(seeds))
    save("e2b", caps=caps, means=np.array(means), ses=np.array(ses))

    fig, ax = plt.subplots(figsize=(5.6, 3.8))
    xs = np.linspace(0.4, 6.0, 100)
    ax.plot(xs, np.clip(1 - xs / LAMBDA_BAR, 0, 1), color="#52514e", ls="--", lw=1.2,
            label="analytic 1 − Λmax/Λ̄")
    ax.errorbar(caps, means, yerr=1.96 * np.array(ses), fmt="o", color=CAT[0], ms=5,
                capsize=3, lw=1.2, label="simulation")
    ax.set(xlabel="AI capability ceiling Λmax", ylabel="final π",
           title="F2b — Coexistence region under capability saturation (A7′)")
    ax.legend(frameon=False, fontsize=8)
    fig.tight_layout()
    fig.savefig(FIGURES / "f2b_coexistence.png")
    print("E2b done")


# ── E3: hysteresis vs demand steepness ──────────────────────────────────────


def ramp(hill_n: float, beta: float, seed: int, lam_max: float = 4.5, t_leg: float = 300.0,
         hill_k: float = 0.5):
    cfg = SimConfig.from_dict(
        BASE
        | {"beta": beta, "seed": seed, "n_active_init": 300,
           "demand_hill_n": hill_n, "demand_hill_k": hill_k, "ai_lam0": 0.0}
    )
    sim = Simulation(cfg)
    n_steps = int(t_leg / cfg.dt)
    rec: dict[str, list] = {"lam": [], "lam_h": [], "leg": []}
    for leg, sign in ((0, +1), (1, -1)):
        for i in range(n_steps):
            frac = i / n_steps
            sim.ais.lam[0] = lam_max * (frac if sign > 0 else 1 - frac)
            sim.step()
            if i % 100 == 0:
                rec["lam"].append(sim.ais.lam[0])
                rec["lam_h"].append(BASE["mu_h"] * sim.humans.n_active)
                rec["leg"].append(leg)
    return {k: np.asarray(v) for k, v in rec.items()}


def loop_area(r: dict[str, np.ndarray]) -> float:
    up, dn = r["leg"] == 0, r["leg"] == 1
    grid = np.linspace(0.05, 4.45, 200)
    f_up = np.interp(grid, r["lam"][up], r["lam_h"][up])
    f_dn = np.interp(grid, r["lam"][dn][::-1], r["lam_h"][dn][::-1])
    return float(np.trapezoid(f_up - f_dn, grid))


def crossing_gap(r: dict[str, np.ndarray], thresh: float = 0.5) -> float:
    """Exit-minus-re-entry control value (positive = hysteresis)."""
    up, dn = r["leg"] == 0, r["leg"] == 1
    lh_u = np.convolve(r["lam_h"][up], np.ones(9) / 9, "same")
    lh_d = np.convolve(r["lam_h"][dn], np.ones(9) / 9, "same")
    if not (lh_u < thresh).any() or not (lh_d > thresh).any():
        return float("nan")
    return float(r["lam"][up][np.argmax(lh_u < thresh)] - r["lam"][dn][np.argmax(lh_d > thresh)])


def e3(seeds: int = 3) -> None:
    """Hysteresis requires a LATE demand response: sweep the half-response point K
    at fixed steepness n=8, plus the linear legacy; sample curves for the panels."""
    beta = 0.6
    ks = [0.5, 0.15, 0.05]
    gaps, ses, sample = [], [], {}
    r_lin = ramp(0.0, beta, seed=0)
    sample["linear"] = r_lin
    gap_lin = [crossing_gap(ramp(0.0, beta, seed=s)) for s in range(seeds)]
    for k in ks:
        vals = []
        for s in range(seeds):
            r = ramp(8.0, beta, seed=s, hill_k=k)
            vals.append(crossing_gap(r))
            if s == 0 and k == 0.05:
                sample["sigmoid"] = r
        gaps.append(np.nanmean(vals))
        ses.append(np.nanstd(vals) / np.sqrt(seeds))
        print(f"E3 K={k}: gap={gaps[-1]:.2f}±{ses[-1]:.2f}")
    save("e3", ks=np.array(ks), gaps=np.array(gaps), ses=np.array(ses),
         gap_linear=np.array(gap_lin))

    fig, axes = plt.subplots(1, 3, figsize=(11, 3.8))
    fig.suptitle("F3 — Irreversibility requires a late demand response (β = 0.6)", y=0.99)
    win = np.ones(15) / 15
    titles = ("linear response: no trap", "late response (K=0.05): trap")
    for ax, key, title in zip(axes[:2], ("linear", "sigmoid"), titles, strict=False):
        r = sample[key]
        up, dn = r["leg"] == 0, r["leg"] == 1
        ax.plot(r["lam"][up], np.convolve(r["lam_h"][up], win, "same"),
                color=CAT[0], label="Λa ramping up")
        ax.plot(r["lam"][dn], np.convolve(r["lam_h"][dn], win, "same"),
                color=CAT[2], label="Λa ramping down")
        ax.set(xlabel="AI capability Λa (controlled)", ylabel="human intensity Λh",
               title=title)
        ax.legend(frameon=False, fontsize=8)
    ax = axes[2]
    ax.errorbar(ks, gaps, yerr=1.96 * np.array(ses), fmt="o-", color=CAT[0], ms=5, capsize=3)
    ax.errorbar([0.75], [np.nanmean(gap_lin)],
                yerr=[1.96 * np.nanstd(gap_lin) / np.sqrt(seeds)],
                fmt="s", color="#52514e", ms=6, capsize=3, label="linear")
    ax.axhline(0, color="#52514e", lw=0.8, ls=":")
    ax.axhline(2.0, color=CAT[2], lw=1.0, ls="--", label="two-state limit (1−β)S")
    ax.invert_xaxis()
    ax.set(xlabel="demand half-response point K (lower = later)",
           ylabel="hysteresis width (exit − re-entry)",
           title="trap width vs response lateness")
    ax.legend(frameon=False, fontsize=8)
    fig.tight_layout(rect=(0, 0, 1, 0.94))
    fig.savefig(FIGURES / "f3_hysteresis.png")
    print("E3 done")


# ── E3conf: pre-registered K-confirmation (E3.9-E3.11) ──────────────────────


def e3conf(seeds: int = 10) -> None:
    """Confirmation protocol of notes-production-v1.md (ADDENDUM 2026-07-13b):
    FRESH seeds 100-109, ramp legs t_leg=600 (half the exploratory ramp speed),
    beta=0.6, late response (n=8, K=0.05) vs linear legacy. Verdicts against
    predictions E3.9-E3.11. This is the code path for the headline hysteresis
    number (gap under late demand vs linear); added by the 2026-07-13 audit —
    the original confirmation run was executed with uncommitted code."""
    beta, t_leg = 0.6, 600.0
    gaps = {"late": [], "linear": []}
    for s in range(100, 100 + seeds):
        gaps["late"].append(crossing_gap(ramp(8.0, beta, seed=s, t_leg=t_leg, hill_k=0.05)))
        gaps["linear"].append(crossing_gap(ramp(0.0, beta, seed=s, t_leg=t_leg)))
        print(f"E3conf seed {s}: gap_late={gaps['late'][-1]:+.2f}  "
              f"gap_linear={gaps['linear'][-1]:+.2f}")
    out = {}
    for key, vals in gaps.items():
        arr = np.asarray(vals)
        mean, se = float(np.nanmean(arr)), float(np.nanstd(arr) / np.sqrt(seeds))
        out[key] = (mean, se)
        print(f"E3conf {key}: gap = {mean:+.2f} ± {se:.2f} (SE), "
              f"95% CI [{mean - 1.96 * se:+.2f}, {mean + 1.96 * se:+.2f}]")
    (ml, sl), (mn, sn) = out["late"], out["linear"]
    ci_disjoint = (ml - 1.96 * sl) > (mn + 1.96 * sn)
    print(f"E3.9  gap(K=0.05) in [0.6, 1.4] and >0 at 95%: "
          f"{'PASS' if 0.6 <= ml <= 1.4 and ml - 1.96 * sl > 0 else 'FAIL'}")
    print(f"E3.10 gap(linear) in [-0.3, +0.3]: {'PASS' if -0.3 <= mn <= 0.3 else 'FAIL'}")
    print(f"E3.11 difference {ml - mn:.2f} > 0.4 with disjoint 95% CIs: "
          f"{'PASS' if ml - mn > 0.4 and ci_disjoint else 'FAIL'}")
    save("e3_confirmation", gap_late=np.asarray(gaps["late"]),
         gap_linear=np.asarray(gaps["linear"]),
         seeds=np.arange(100, 100 + seeds), t_leg=np.array([t_leg]))
    print("E3conf done")


# ── E4: number of operators ─────────────────────────────────────────────────


def e4(seeds: int = 30) -> None:
    ns = [1, 2, 5, 20]
    t_end = 30.0
    t_cross = {n: [] for n in ns}
    for n in ns:
        for s in range(seeds):
            h = run_once(
                {"ai_lam0": 0.3, "ai_eta": 0.06, "ai_delta": 0.05,
                 "ai_n_operators": n, "seed": s},
                t_end,
            )
            idx = np.nonzero(h["lam_a"] >= LAMBDA_BAR)[0]
            t_cross[n].append(h["t"][idx[0]] if idx.size else np.nan)
    save("e4", ns=np.array(ns), **{f"tc_{n}": np.array(t_cross[n]) for n in ns})

    fig, ax = plt.subplots(figsize=(5.2, 3.8))
    for i, n in enumerate(ns):
        vals = np.array(t_cross[n])
        ax.scatter(np.full(vals.size, i) + np.random.default_rng(0).uniform(-0.08, 0.08, vals.size),
                   vals, s=18, color=CAT[0], alpha=0.7)
        ax.scatter([i], [np.nanmean(vals)], s=70, color="#0d366b", zorder=3, marker="_")
    gamma = 0.06 * 10 - 0.05
    ax.axhline(np.log(LAMBDA_BAR / 0.3) / gamma, color="#52514e", ls="--", lw=1.2,
               label="analytic t* (single aggregate)")
    ax.set(xticks=range(len(ns)), xticklabels=[str(n) for n in ns],
           xlabel="number of AI operators (same aggregate capability)",
           ylabel="exclusion time t*",
           title="F4 — Operator count: invariant without rent dissipation")
    ax.legend(frameon=False, fontsize=8)
    fig.tight_layout()
    fig.savefig(FIGURES / "f4_operators.png")
    print("E4 done")



# ── E5: redistribution as an endogenous brake ───────────────────────────────


def crossing_time(h: dict[str, np.ndarray]) -> float:
    idx = np.nonzero(h["lam_a"] >= LAMBDA_BAR)[0]
    return float(h["t"][idx[0]]) if idx.size else float("nan")


def e5(seeds: int = 6) -> None:
    taus = [0.0, 0.5, 0.8, 0.95]
    t_end = 120.0
    rows = []
    for tau in taus:
        tcs, pis_m, pis_t = [], [], []
        for s in range(seeds):
            h = run_once(
                {"ai_lam0": 0.3, "ai_eta": 0.06, "ai_delta": 0.05,
                 "redistribution_rate": tau, "seed": s},
                t_end,
            )
            tcs.append(crossing_time(h))
            late = h["t"] > 0.85 * t_end
            k_h, k_a, t_h = (h["kappa_h"][late].mean(), h["kappa_a"][late].mean(),
                             h["t_h"][late].mean())
            pis_m.append(k_h / max(k_h + k_a, 1e-9))
            pis_t.append((k_h + t_h) / max(k_h + k_a + t_h, 1e-9))
        rows.append((tau, np.nanmean(tcs), np.mean(pis_m), np.mean(pis_t)))
        print(f"E5 τ={tau}: t*={np.nanmean(tcs):.1f}  π_market={np.mean(pis_m):.2f}  "
              f"π_total={np.mean(pis_t):.2f}")
    arr = np.array(rows)
    save("e5", taus=arr[:, 0], t_star=arr[:, 1], pi_market=arr[:, 2], pi_total=arr[:, 3])

    fig, axes = plt.subplots(1, 2, figsize=(9, 3.8))
    ts_th = [np.log(LAMBDA_BAR / 0.3) / (0.06 * (1 - t) * 10 - 0.05)
             if 0.06 * (1 - t) * 10 > 0.05 else np.nan for t in taus]
    axes[0].plot(taus[:3], ts_th[:3], ls="--", color="#52514e", label="analytic t*(τ)")
    axes[0].plot(arr[:3, 0], arr[:3, 1], "o", color=CAT[0], label="simulation")
    axes[0].set(xlabel="redistribution rate τ", ylabel="exclusion time t*",
                title="delay below τ* ≈ 0.917")
    axes[0].legend(frameon=False, fontsize=8)
    axes[1].plot(arr[:, 0], arr[:, 2], "o-", color=CAT[0], label="π_market")
    axes[1].plot(arr[:, 0], arr[:, 3], "s-", color=CAT[2], label="π_total")
    axes[1].axvline(1 - 0.05 / 0.6, ls=":", color="#52514e", lw=1.0)
    axes[1].annotate("τ*", (1 - 0.05 / 0.6, 0.05), fontsize=9, color="#52514e")
    axes[1].set(xlabel="redistribution rate τ", ylabel="stationary share",
                title="kept alive (π_total) vs in the loop (π_market)")
    axes[1].legend(frameon=False, fontsize=8)
    fig.suptitle("F5 — Redistribution: brake and perfusion", y=1.0)
    fig.tight_layout(rect=(0, 0, 1, 0.95))
    fig.savefig(FIGURES / "f5_redistribution.png")
    print("E5 done")


# ── E4b: rent dissipation and collusion ─────────────────────────────────────


def e4b(seeds: int = 6) -> None:
    rhos = [0.0, 0.5, 0.9, 1.0]
    t_end = 120.0
    rows, collusion_row = [], None
    for rho in rhos:
        tcs = []
        for s in range(seeds):
            h = run_once(
                {"ai_lam0": 0.3, "ai_eta": 0.06, "ai_delta": 0.05,
                 "ai_n_operators": 20, "ai_rent_dissipation": rho, "seed": s},
                t_end,
            )
            tcs.append(crossing_time(h))
        rows.append((rho, np.nanmean(tcs), float(np.mean(np.isnan(tcs)))))
        if np.all(np.isnan(tcs)):
            print(f"E4b ρ_d={rho}: NO exclusion ({seeds} seeds)")
        else:
            n_exc = seeds - int(np.isnan(tcs).sum())
            print(f"E4b ρ_d={rho}: t*={np.nanmean(tcs):.1f}  (excluded in {n_exc}/{seeds})")
    tcs = []
    for s in range(seeds):
        h = run_once(
            {"ai_lam0": 0.3, "ai_eta": 0.06, "ai_delta": 0.05, "ai_n_operators": 20,
             "ai_rent_dissipation": 1.0, "ai_collude": True, "seed": s},
            t_end,
        )
        tcs.append(crossing_time(h))
    collusion_row = np.nanmean(tcs)
    print(f"E4b collusion (ρ_d=1.0, collude=True): t*={collusion_row:.1f}")
    arr = np.array(rows)
    save("e4b", rhos=arr[:, 0], t_star=arr[:, 1], frac_no_excl=arr[:, 2],
         t_star_collusion=np.array([collusion_row]))

    fig, ax = plt.subplots(figsize=(5.6, 3.8))
    ax.plot(arr[:, 0], arr[:, 1], "o-", color=CAT[0], label="20 competing operators")
    ax.scatter([1.0], [collusion_row], marker="D", s=45, color=CAT[2], zorder=3,
               label="20 colluding operators (ρ_d=1)")
    ax.axvline(0.965, ls=":", color="#52514e", lw=1.0)
    ax.annotate("ρ* ≈ 0.965", (0.965, ax.get_ylim()[0]), fontsize=8, color="#52514e",
                rotation=90, va="bottom", ha="right")
    ax.set(xlabel="rent dissipation share ρ_d", ylabel="exclusion time t* (NaN = prevented)",
           title="F4b — Competition protects only at near-total dissipation;\n"
                 "collusion switches it off")
    ax.legend(frameon=False, fontsize=8)
    fig.tight_layout()
    fig.savefig(FIGURES / "f4b_dissipation.png")
    print("E4b done")



# ── E6: early-warning signals ───────────────────────────────────────────────


def e6(seeds: int = 3) -> None:
    """Rolling lag-1 autocorrelation of participation on the up-leg, before each
    run's own exit point: predicted to ramp up in the demand-trap regime
    (K=0.05) and to stay flat-ish in the linear regime (E6.1-E6.3)."""
    from sim.metrics.indices import rolling_lag1_autocorr

    window = 60  # recorded points (~6 time units at record stride 1.0)
    curves = {}
    for label, (n, k) in {"linear": (0.0, 0.5), "trap (K=0.05)": (8.0, 0.05)}.items():
        acs = []
        for s in range(seeds):
            r = ramp(n, 0.6, seed=100 + s, t_leg=600.0, hill_k=k)
            up = r["leg"] == 0
            lam_h = r["lam_h"][up]
            exit_idx = np.argmax(np.convolve(lam_h, np.ones(9) / 9, "same") < 0.3)
            pre = lam_h[: max(exit_idx, window + 10)]
            ac = rolling_lag1_autocorr(pre, window)
            acs.append(ac[-200:])  # the 200 points leading into the exit
        min_len = min(a.size for a in acs)
        curves[label] = np.vstack([a[-min_len:] for a in acs])
        mean_late = np.nanmean(curves[label][:, -40:])
        mean_early = np.nanmean(curves[label][:, :40])
        print(f"E6 {label}: lag-1 autocorr early={mean_early:.2f} -> late={mean_late:.2f}")
    save("e6", **{k.replace(" ", "_").replace("(", "").replace(")", "").replace("=", "")
                  .replace(".", ""): v for k, v in curves.items()})

    fig, ax = plt.subplots(figsize=(6.4, 3.8))
    for (label, arr), color in zip(curves.items(), (CAT[0], CAT[2]), strict=False):
        x = np.arange(-arr.shape[1], 0)
        ax.plot(x, np.nanmean(arr, axis=0), color=color, label=label)
        lo, hi = np.nanpercentile(arr, 10, axis=0), np.nanpercentile(arr, 90, axis=0)
        ax.fill_between(x, lo, hi, color=color, alpha=0.15, lw=0)
    ax.set(xlabel="recorded steps before own exit point",
           ylabel="rolling lag-1 autocorrelation of Λh",
           title="F6 — Early warning before the exit: trap regime vs linear")
    ax.legend(frameon=False, fontsize=8)
    fig.tight_layout()
    fig.savefig(FIGURES / "f6_early_warnings.png")
    print("E6 done")


if __name__ == "__main__":
    p = argparse.ArgumentParser()
    choices = ["e1", "e2", "e2b", "e3", "e3conf", "e4", "e5", "e4b", "e6"]
    p.add_argument("--exp", required=True, choices=choices)
    args = p.parse_args()
    {"e1": e1, "e2": e2, "e2b": e2b, "e3": e3, "e3conf": e3conf, "e4": e4,
     "e5": e5, "e4b": e4b, "e6": e6}[args.exp]()
