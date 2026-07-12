# Pre-registered predictions for experiments E1-E6 (T4.0)

> **Committed BEFORE any production run** (git history is the timestamp). Each
> experiment must return a verdict against these predictions: CONFIRMED /
> REFUTED / PARTIAL, written in the experiment's analysis note. A refuted
> prediction is a *result*, not a failure — the one forbidden move is silently
> adjusting the model until it fits. Derived from the analytic model
> (paper/model-notes.md), which is itself triple-verified; deviations therefore
> localize what the ABM's relaxations (finite adjustment, agent granularity,
> noise) change.

Baseline parameters (as in tests): g=50, v=1, θ=2, μ_h=0.01, c_h=0.1 ⇒ S=5, Λ̄=3.

## E1 — Dynamics of π vs AI progress rate (→ F1)

With η varying and δ=0.05 fixed, γ = 10η − δ:
1. γ ≤ 0 (η ≤ 0.005): Λ_a → 0, π → 1 (human dominance).
2. γ > 0: π(t) ≈ 1 − (Λ_a(0)/Λ̄)e^{γt} — slow-then-sudden decline; full exclusion (π < 0.05) shortly after t* = ln(Λ̄/Λ_a(0))/γ, with a lag of order the human adjustment time (patience/deficit), i.e. t_exclusion ∈ [t*, t* + ~20].
3. Doubling η (well inside γ>0) halves t* to first order: t*(2η)/t*(η) ≈ (η − δ/10)/(2η − δ/10) ≈ 1/2 for η ≫ δ/10.

## E2 — Phase diagram (→ F2)

Axes: η × δ (linear reinvestment), plus a second map η × Λ_max (capability cap, the A7′ relaxation).
1. η × δ plane: sharp boundary along the line **η = δ·μ_h/c_h = δ/10** (γ = 0). Above: exclusion (π_final ≈ 0); below: human dominance (π_final ≈ 1). No intermediate-π stationary band of nonzero width along a generic ray (the interior fixed point is non-generic, knife-edge γ=0 only).
2. η × Λ_max plane: **coexistence region appears** — for Λ_max < Λ̄, π_final ≈ 1 − Λ_max/Λ̄ ∈ (0,1) stable. This is the honest "exclusion is not universal" region; its boundary Λ_max = Λ̄ is where π_final hits 0.
3. Bimodality of π_final across seeds near boundaries; away from them, low variance.

## E3 — Hysteresis under demand feedback (→ F3)

Protocol: β < 1, slowly ramp a *controlled* Λ_a up past exclusion then back down (AI dynamics off; Λ_a as control parameter), demand endogenous.
1. Exit on the way up at Λ_a ≈ Λ̄_hi = S−θ = 3 (within the adjustment lag).
2. Re-entry on the way down only at Λ_a ≈ βS − θ (e.g. β=0.6: 1.0).
3. **Loop width ≈ (1−β)·S**, vanishing as β → 1 (no hysteresis at fully autonomous demand); for β ≤ θ/S = 0.4, no re-entry even at Λ_a = 0 (permanent trap).
4. With the continuous demand pool (smoothed, not two-state), the loop persists but its width may shrink by up to ~20% relative to (1−β)S (smooth fold vs hard switch); direction of the inequality is the prediction: width_continuous ≤ (1−β)S.

## E4 — Number of AI operators (→ F4)

N operators, aggregate initial capability fixed, each reinvesting its own income (current core: no price competition between operators).
1. Under the v1 mechanics, the aggregate dynamics is *invariant in N* (incomes sum; identical η, δ): same t*, same π trajectory — competition between operators changes nothing absent rent dissipation. This null result is itself informative.
2. **Conditional prediction** (requires the T3.8 price-competition/collusion strategy layer): if operators bid down capture margins (rent dissipation share ρ_d), effective η falls to η(1−ρ_d); exclusion is delayed and, for η(1−ρ_d) < δ/10, prevented. Collusion (ρ_d → 0) restores the single-operator outcome. I.e. **AI-vs-AI competition protects humans only if it dissipates AI rents; collusion removes the protection.**

## E6 — Early-warning signals (→ F6)

1. In β=1 runs (no demand feedback), the transition is a boundary crossing of a slow drift, NOT a fold bifurcation of the fast subsystem ⇒ **weak or absent** critical-slowing-down signatures in π (variance may rise mechanically as captures thin, but lag-1 autocorrelation should not show the classic pre-fold ramp).
2. In β<1 runs (fold present), rolling variance and lag-1 autocorrelation of π rise ahead of the collapse; the rise precedes t_exclusion by an interval growing with (1−β).
3. Sharp falsifiable statement: EWS discriminate the demand-coupled regime from the uncoupled one — if EWS appear equally in both, prediction REFUTED.

## ADDENDUM 2026-07-13 (pre-registered BEFORE the E3 production runs, AFTER the preliminary finding of notes-preliminary-e3.md)

The preliminary run refuted E3.4 for *linear* demand coupling. The production E3 adds a demand-response steepness parameter (normalized Hill sigmoid, exponent n; n≤0 = linear legacy, K=0.5). New predictions:

- **E3.5** — n linear: no hysteresis loop (replicates the preliminary finding); exclusion of participation completes near Λ_a ≈ βS−θ on the way up.
- **E3.6** — loop appears above a critical steepness n_c (existence claim; n_c not predicted quantitatively) and its width increases with n.
- **E3.7** — as n grows large the loop width approaches the two-state value (1−β)S from below.
- **E3.8** — permanent trap (no re-entry at Λ_a=0) for β < θ/S at high n, absent at n linear.

## ADDENDUM 2026-07-13b (pre-registered BEFORE the K-confirmation runs, AFTER the exploratory K finding of notes-production-v1.md)

The exploratory pass (seeds 0-2, ramp legs 300) found the hysteresis driver to be the demand response's half-response point K, not its steepness. Confirmation protocol: **fresh seeds 100-109 (10 seeds), ramp legs 600 (half the ramp speed), β=0.6, n=8**. Predictions:

- **E3.9** — gap(K=0.05) ∈ [0.6, 1.4] and strictly positive at 95% confidence.
- **E3.10** — gap(linear) ∈ [−0.3, +0.3] (compatible with zero).
- **E3.11** — gap(K=0.05) − gap(linear) > 0.4 with non-overlapping 95% CIs.

## ADDENDUM 2026-07-13c (pre-registered BEFORE the E5/E4b runs — redistribution and rent dissipation, T3.8)

**E5 — redistribution as an endogenous brake** (β=1 to isolate the reinvestment channel; tax rate τ on AI income, transferred to humans; η=0.06, δ=0.05, Λ_a(0)=0.3):
- **E5.1** — effective growth is γ(τ) = η(1−τ)c_h/μ_h − δ; exclusion is prevented iff τ > τ* = 1 − δμ_h/(ηc_h) ≈ **0.917**. Concretely: exclusion at τ ∈ {0, 0.5, 0.8}; no exclusion at τ = 0.95 (stationary π_market > 0.5).
- **E5.2** — below τ*, exclusion time scales as t*(τ) = t*(0)·γ(0)/γ(τ): with t*(0) ≈ 4.2, predict t*(0.5) ≈ 9.2 and t*(0.8) ≈ 33 (±35%).
- **E5.3** — post-exclusion, π_total ≈ τ exactly (transfers are the only human income), so the perfusion gap Δ = π_total − π_market ≈ τ: the "kept alive but out of the loop" regime, now measurable.
- Reading to test in words: **redistribution helps only via confiscatory rates at these parameters** — because the brake must beat exponential compounding, not linear growth.

**E4b — rent dissipation between operators** (N=20 operators, dissipation share ρ_d of captured value burned by competition, collusion flag restores ρ_d=0):
- **E4.4** — prevention iff η(1−ρ_d(1−1/N))c_h/μ_h < δ, i.e. ρ_d > ρ* ≈ **0.965** at baseline: exclusion at ρ_d ∈ {0, 0.5, 0.9}; no exclusion at ρ_d = 1.0.
- **E4.5** — with the collusion flag on, the single-operator outcome is restored at any ρ_d (t* back to ≈ 4.2 ± 35%).
- Reading: **AI-vs-AI competition protects humans only at near-total rent dissipation, and collusion switches the protection off entirely.**

## Out of scope of these predictions

Labor channel (λ), transfers (T), Goodhart on π, heterogeneous difficulties with human ceilings (the "front" prediction of A4 audit: exclusion proceeds skill-band by skill-band) — to be pre-registered when T3.8+ lands, before their experiments run.
