# The Human Economic Participation Index (π): a working definition

> Early-stage working note, shared for feedback. This project builds the formal layer that the qualitative literature on gradual disempowerment (Kulveit et al. 2025) and the intelligence curse (Drago & Laine 2025) leaves open: a minimal analytic model and an agent-based simulation of **asymmetric gradient exhaustion** — the hypothesis that AI optimizers capture profit opportunities ("gradients") faster than humans can, driving human *market* income toward zero even while total system profit persists. Before writing the model, we need one operational definition of its central state variable: **the share of the economic loop that still runs through humans**, which we call π. The questions I would most value your reaction to are flagged in §3 and §7. English translation of an internal working note; comments welcome on the definitional choices, not the prose.

---

## 1. Design principles (three commitments)

π measures **the share of the economic *flow* that runs through humans as economic agents**. Three choices fix everything else:

1. **A flow, not a stock, not a headcount.** π is a share of *value circulating per unit time* (income), not a share of accumulated wealth and not a fraction of the population. The claim under scrutiny is about the economic *loop* (who captures opportunities, who decides, who works), not about who holds inherited wealth or how many humans are nominally "active".
2. **Attribution to the residual claimant, not to the tool.** Income is "human" if a **human agent** is its residual beneficiary and bears the participation cost — whatever tool (including an AI) it uses. A human who *rents* AI capacity is still human; what counts on the human side is the **net margin** they retain, while the fee paid to the operator counts on the AI side (see §4, "AI-assisted human").
3. **A ratio, robust to the fate of demand.** π is deliberately a *share* (numerator/denominator). It is therefore well-defined whether total flow Y collapses (Korinek's realization crisis) or persists through self-sustaining inter-AI demand. The fate of Y is a *model parameter* (the share of final demand originating from operators themselves), not an ingredient of π.

**Non-tautology guardrail.** In the model, "human" and "AI" denote only two **parameter vectors** (detection latency, information cost, capacity ceiling, learning speed), never special rules. Nothing in the definition of π forces the human share up or down: the parameters and the dynamics decide.

---

## 2. Value channels and formal definition

At each time step the model produces a flow of captured value. We split it by **beneficiary** (humans `h` / AI operators `a`) and by **channel**:

| Channel | Symbol (humans) | Description |
|---|---|---|
| **Capture** | κ_h | income from seizing "open" gradients (arbitrage, entrepreneurship, allocation decisions) |
| **Labour** | λ_h | capture of gradients tagged "requires human presence" — the non-automatable fraction, **endogenous and declining** (AI may eventually capture these too: λ_a ≥ 0, no ad hoc protection) |
| **Transfers** | T_h | political redistribution: UBI, tax→transfer |
| **Passive capital** | R_h | dividends/rents paid to humans who do not operate — reported as a **separate output series**, kept out of the headline indices (see §4, §7) |

Aggregates: **earned** (pre-transfer) human income `E_h = κ_h + λ_h`, AI `E_a = κ_a + λ_a`; total earned flow `E = E_h + E_a`. Transfers redistribute E without creating it (post-transfer total remains E).

**Market (earned) index:**
$$\pi_{\text{market}} = \frac{E_h}{E} = \frac{\kappa_h + \lambda_h}{\kappa_h + \lambda_h + \kappa_a + \lambda_a}$$
the human share of **earned** income. This is the primary index, whose dynamics and thresholds we study.

**Total (livelihood) index:**
$$\pi_{\text{total}} = \frac{E_h + T_h}{E}$$
the share of the flow that **sustains** humans once redistribution is counted.

**Perfusion gap:**
$$\Delta = \pi_{\text{total}} - \pi_{\text{market}} = \frac{T_h}{E}$$
**itself a result, not a by-product**: the share of human livelihood no longer *earned in the loop* but *paid from outside it* through redistribution. A regime "π_market → 0, π_total high, Δ large" is precisely the diagnostic's endgame: *humans living on perfusion*, outside the productive loop.

**Passive-capital series (separate):**
$$\rho = \frac{R_h}{E}$$
the share of the flow paid to humans who **own but do not operate** (AI capital rents). Reported **separately** in every experiment: it enters neither π_market nor Δ, keeping the **headline indices unchanged** while leaving the question "does owning AI capital protect humans?" analysable. An extended reading π_total⁺ = π_total + ρ is available if one wants to test it (never the default index).

All of these are **ratios of counters kept by the simulator** → unambiguously computable and reproducible.

---

## 3. The two hard questions

**Demand — is human demand load-bearing or decorative?**
- *Can inter-AI demand become self-sustaining?* Treated as a **model parameter** (the share of final demand originating from operators), not as part of the definition. Because π is a ratio, it stays interpretable in either regime: if inter-AI demand sustains Y despite null human income, then "π_market → 0" is a *stable, self-uncorrecting* state — which is exactly the point. The definition need not settle this; it only needs to be **robust** to it, which the ratio choice guarantees.
- *Is UBI "in the loop" or perfusion?* **Settled**: redistribution is channel T, counted in **π_total only**, never in π_market. We do not choose between the two readings — we **report both**, and the gap Δ measures the "perfusion" explicitly.

**Measurement — what counts as "human in the loop", and how is it measured?**
- *What counts*: **active participation** = capture (κ_h) + labour (λ_h). Holding wealth or receiving a transfer is not participating (→ channels T, ρ). Deciding / arbitraging / founding a business / working, yes (→ E_h).
- *How to measure*: as flow ratios in the model; as an index built from proxies in real data (§5).
- π_market **is** the central state variable. A secondary *decision* indicator (share of capture events initiated by human-operated agents) is kept as a complementary diagnostic but **not** as the headline π (reason in §6, rejected alternative #3).

---

## 4. Boundary cases, resolved

| Case | Ruling | Where it lands | Expected signature |
|---|---|---|---|
| **UBI / redistribution** | income not earned in the loop → channel T | π_total only (in Δ) | π_market↓ but π_total sustained, Δ↑ = perfusion economy |
| **AI-assisted human** ("centaur") | attributed to the human residual claimant. Modelled as a human agent renting capacity: their **net margin** (value − fee) is κ_h; the fee is κ_a | π_market (the margin) + AI's π_market (the fee) | when operators capture the whole surplus, the human margin → 0 *even though "a human is involved"* — the mechanism made measurable |
| **Passive shareholder** (human living off AI-firm dividends, not operating) | capital income **without participation** → out of π_market; **separate series ρ** (neither in π_market nor in Δ) | series ρ (headline indices unchanged) | "AI rentier class": π_market → 0 while ρ stays positive — the ρ series *shows* whether owning protects, instead of asserting it |

Unifying principle: **we count participation, not ownership and not perfusion.** A unit of value enters π_market only if it is *earned* by a human agent who captures a gradient or supplies labour.

---

## 5. Mapping to real-world data

No single source yields π directly; π_market is a **constructed index**. Correspondences:

- **λ_h (labour)** ≈ the **labour share** in national accounts (measured, declining — but confounded by globalisation and market power, cf. De Loecker & Eeckhout; hence the labour share alone is insufficient, §6-1).
- **κ_h (human capture / entrepreneurship)** ≈ self-employment income + value created by new firms founded and run *without frontier AI*; the **cleanest laboratory** is gig-by-gig earnings on freelance platforms before/after LLMs.
- **Δ (perfusion)** ≈ social-transfer share of household disposable income + household capital income not from own activity.
- **Decision proxy** ≈ share of transactions (e-commerce, finance) initiated by autonomous agents; `1 −` that share approximates human decision.

One sub-economy (a freelance platform) yields a sectoral π_market computable gig by gig — the cleanest empirical instantiation.

---

## 6. Three rejected alternatives

1. **Labour share alone** (π := labour income / national income). *Rejected*: (a) ignores human capture/entrepreneurship (κ_h), which is central to the mechanism — a world where humans earn no wages but still capture gradients as entrepreneurs is not disempowerment; (b) the labour share already declines for reasons unrelated to AI (market power), so it *confounds*. We keep it as an **empirical proxy for λ_h**, not as π.
2. **Employment rate / active-population share** (π := fraction of humans employed). *Rejected*: this is the "population" framing we deliberately drop. Humans can be "employed" in make-work while all allocative value flows to AI; conversely a handful of humans could capture a great deal. π must be a share of **value flow**, not a headcount.
3. **Decision-rights share** (π := fraction of allocation decisions made by humans). *Rejected as the primary definition*: conceptually purest, but **unmeasured and ill-defined** (what is "a decision"? how to weight it?) — not approximable in data and ambiguous in the model. We choose **computability**: it survives as a *secondary indicator* (share of captures initiated by humans), not as π.

*(A related candidate also set aside: the human **share of wealth** — a stock, not a flow; a rentier holds a stock while contributing nothing to the loop's flow. We measure the flow.)*

---

## 7. The one value-laden choice, stated explicitly

The **passive shareholder** is treated as "out of the loop": passive capital income is **kept out of π_market** and **reported as a separate series ρ** (not folded into Δ, headline indices unchanged). This is the choice consistent with a *participation* definition and with the rentier framing of the intelligence curse. It is a genuine value choice with a real stake: if one held that *owning* AI capital is itself a way of staying in the loop (control through ownership), a world where humans own the AI firms would score high π and the diagnostic would be weaker. We keep the "owning is not participating" choice — it makes the diagnostic more demanding — state it as an explicit assumption, and let the ρ series test the alternative reading empirically rather than settle it by definition. **This is the choice I would most value an outside opinion on.**

---

*Companion to the model specification (in preparation). The index is implemented as π_market, π_total, Δ and ρ, computed exactly as above, so that the definition and the code stay traceable to one another.*
