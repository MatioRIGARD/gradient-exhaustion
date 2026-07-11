# Priced Out by Machines: A Multi-Agent Model of Human Economic Disempowerment

> Working draft — Markdown master, LaTeX conversion at phase 5 (T5.4).
> Alternative titles: "Asymmetric Gradient Exhaustion: How AI Optimizers Price Humans Out of the Economic Loop" / "The Economics of Gradual Disempowerment: A Formal Model".
> Author: Mathieu R. — Status: skeleton; sections filled as phases complete (see PLAN.md).

## Abstract (draft v0 — rewrite after results)

Recent qualitative work argues that incremental AI deployment may gradually disempower humans by eroding the economic relevance on which societal alignment implicitly relies (Kulveit et al. 2025; Drago & Laine 2025). We provide, to our knowledge, the first formal multi-agent treatment of this hypothesis. We model the economy as a stream of profit opportunities ("gradients") captured competitively by two populations — human agents with fixed detection costs and latency, and AI-operated agents whose costs decline with reinvested income. In a minimal analytic model we derive conditions under which human gradient income collapses even though total system profit remains positive. An agent-based simulation generalizes the result under heterogeneous opportunities, richer strategy spaces (collusion, exit, redistribution) and three interchangeable learning rules. We find [PLACEHOLDER: threshold / hysteresis / competition-necessity results — F2, F3, F4]. We propose an operational index of human economic participation (π), derive early-warning signatures observable before the critical region, and state falsifiable predictions on the emerging agentic economy (2025–2028). [~180 words max]

## 1. Introduction

- Hook: the gradual disempowerment thesis — existential risk without takeover — currently rests on qualitative argument.
- Gap: no formal model, no simulation, no characterization of critical thresholds (cite the explicit research-project lists calling for this).
- Contribution (3 bullets): (i) minimal analytic model of asymmetric gradient capture (a two-species extension of Grossman-Stiglitz); (ii) ABM with complete strategy space and anti-tautology validation protocol; (iii) phase diagram, hysteresis analysis, early-warning indicators, and pre-registered predictions.
- Non-claims (important, early): we do not claim inevitability; results are conditional on measured parameters; competition intensity is a parameter, not an assumption.

## 2. Related work

- Gradual disempowerment & post-AGI economics: Kulveit et al. 2025; Drago & Laine 2025; Christiano 2019; Critch 2021; Korinek (realization crisis).
- Multi-agent risks & algorithmic collusion: Hammond et al. 2025 (CAIF); Calvano et al. 2020; steganographic collusion.
- Economic traditions the model draws on: Grossman-Stiglitz 1980 (self-defeating efficiency); Schumpeterian rent regeneration; markup/superstar-firm empirics (De Loecker & Eeckhout); secular stagnation. One paragraph each, ending with what none of them does (the unified formal treatment).
- [Source: docs/fiches-lecture.md after T0.2 — verify every reference against docs/biblio-verification.md]

## 3. A minimal model of gradient capture

[From paper/model-notes.md after T2.1-T2.4]
- 3.1 Setup: opportunity stream (g, v, k, ℓ, d); two populations; capture race; income flows.
- 3.2 Static case: closed-form incomes; comparative statics.
- 3.3 Dynamic case: AI reinvestment loop; conditions for human income collapse; threshold existence.
- 3.4 Assumptions audit (A1-An) and which results depend on which.

## 4. Agent-based model

[From docs/simulation-architecture.md as built in phase 3]
- 4.1 Architecture: vectorized populations, demand loop, entry/exit.
- 4.2 Strategy space: collusion, exit, investment/distribution; three learning rules (replicator / best response / Q-learning).
- 4.3 The participation index π (from docs/pi-definition.md): π_market vs π_total.
- 4.4 Validation protocol: analytic correspondence (V1), non-tautology tests (V2), invariance (V3). — This subsection is itself a methodological contribution; keep it.

## 5. Results

- 5.1 (F1) Dynamics of π under increasing AI progress rates.
- 5.2 (F2) Phase diagram: AI speed × niche regeneration; the critical frontier.
- 5.3 (F3) Hysteresis: the point of no return.
- 5.4 (F4) Is competition necessary? Monopoly vs N operators.
- 5.5 (F5) Ablations: which conclusions survive collusion / exit / redistribution.
- 5.6 (F6) Early-warning signatures ahead of the transition.

## 6. Empirical signatures and predictions

- Embryonic evidence: freelance-platform displacement studies; arbitrage spread compression; markup concentration. [verify sources — T0.1]
- Pre-registered predictions on the agentic economy (from paper/predictions.md, committed before production runs — cite commit hash).

## 7. Limitations and objections

Write this section as our own hostile referee (T5.2). Minimum content: stylized opportunity process; π definition choices; learning-rule dependence (report all three); no general-equilibrium price feedback in v1; the self-fulfilling-prophecy concern and why conditional modeling mitigates it; what K1-K4 style evidence would falsify the diagnosis.

## 8. Conclusion

Conditional statement of findings; the three parameters that matter; what to measure now.

## References

[Only entries validated in docs/biblio-verification.md]

---

## Figure checklist

| Fig | Source experiment | Status |
|---|---|---|
| F1 | E1 (T4.1) | ☐ |
| F2 | E2 (T4.2) | ☐ |
| F3 | E3 (T4.3) | ☐ |
| F4 | E4 (T4.4) | ☐ |
| F5 | E5 (T4.5) | ☐ |
| F6 | E6 (T4.6) | ☐ |
