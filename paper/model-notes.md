# Model Notes — The Gradient Capture Race

> **STATUS: DRAFT — UNVERIFIED.** Written 2026-07-13 (T2.1–T2.3). Independent re-derivation of §2 pending (see verification log at bottom). Numeric check: `sim/analysis/analytic_check.py`. Nothing here is settled until the verification log says so.

---

## 1. Setup

We model the economy as a flow of profit opportunities ("gradients") captured competitively by two populations. Time is continuous.

**Opportunities.**
- **(A1)** Opportunities arrive as a Poisson process with rate $g > 0$.
- **(A2)** Each opportunity is worth $v > 0$ to whoever captures it first (homogeneous values in the minimal model).
- **(A3)** An uncaptured opportunity expires at rate $\theta > 0$ (exponential lifetime, mean $1/\theta$): gradients decay as conditions drift and knowledge diffuses.

**Human agents.**
- **(A4)** There is an unbounded pool of identical potential human participants. A participating human pays a flow cost $c_h > 0$ (time, attention, information — the Grossman-Stiglitz participation cost) and detects any given live opportunity at Poisson rate $\mu_h > 0$, independently across opportunities and agents.
- **(A5)** Free entry and exit with outside option normalized to 0: humans participate while expected net flow income is positive. Entry/exit adjusts fast relative to AI capability growth (timescale separation).

**AI operators.**
- **(A6)** The AI side has aggregate detection intensity $\Lambda_a \ge 0$ (one operator, or several summed; operator competition is an ABM question, experiment E4). Its variable participation cost is absorbed into the reinvestment dynamics below.
- **(A7)** *(Dynamics only.)* AI capability compounds with income: $\dot{\Lambda}_a = \eta\,\kappa_a - \delta\,\Lambda_a$, where $\kappa_a$ is the AI capture-income flow, $\eta > 0$ converts reinvested income into detection capability, $\delta > 0$ is depreciation/obsolescence. Humans have no such compounding in v1 ($\mu_h, c_h$ constant).

**Capture race.** The first agent to detect a live opportunity captures $v$. With total human intensity $\Lambda_h = n_h \mu_h$ ($n_h$ = number of participants), competing exponentials give, for each arriving opportunity:

$$P(\text{human capture}) = \frac{\Lambda_h}{\Lambda_h + \Lambda_a + \theta}, \qquad P(\text{AI capture}) = \frac{\Lambda_a}{\Lambda_h + \Lambda_a + \theta}, \qquad P(\text{expiry}) = \frac{\theta}{\Lambda_h + \Lambda_a + \theta}.$$

Stationary income flows: $\kappa_h = g v \frac{\Lambda_h}{\Lambda_h+\Lambda_a+\theta}$, $\kappa_a = g v \frac{\Lambda_a}{\Lambda_h+\Lambda_a+\theta}$.

**Anti-tautology note.** Humans and AI differ only in parameter structure: humans have fixed technology and free entry; AI has compounding technology. **(A7) is the load-bearing empirical asymmetry** — the claim is not that humans cannot improve, but that software detection capability compounds with reinvested income much faster than human capability does. §5 audits this. If (A7) is switched off ($\eta = 0$), or given symmetrically to humans, no exclusion occurs (§2.4, sanity results) — the mechanism, not the labels, drives every result below.

---

## 2. Static solution (T2.2): the participation threshold

Fix $\Lambda_a$ (frozen AI capability). Per-participant gross income is $g v \mu_h / (\Lambda_h + \Lambda_a + \theta)$, decreasing in $n_h$: humans congest their own field. Free entry (A5) drives net income to zero while participation is positive:

$$\frac{g v \mu_h}{\Lambda_h^* + \Lambda_a + \theta} = c_h \quad\Longleftrightarrow\quad \Lambda_h^* + \Lambda_a + \theta = \frac{g v \mu_h}{c_h} \equiv S.$$

$S$ — the **saturation intensity** — is the total race intensity at which a marginal human exactly breaks even. Define the **human viability threshold**

$$\boxed{\;\bar\Lambda \equiv S - \theta = \frac{g v \mu_h}{c_h} - \theta\;}$$

(assume $S > \theta$, otherwise humans are never viable). Then:

$$\Lambda_h^* = \max\!\big(0,\; \bar\Lambda - \Lambda_a\big).$$

**Result 1 (finite-capability exclusion).** Human participation is positive iff $\Lambda_a < \bar\Lambda$ and hits **exactly zero** at the finite AI capability $\bar\Lambda$ — not asymptotically. The threshold is interpretable: it rises with the opportunity flow ($gv$) and human detection efficiency ($\mu_h / c_h$), and falls with gradient decay $\theta$.

**Result 2 (linear decline of participation income).** In the interior regime ($\Lambda_a < \bar\Lambda$), total race intensity is pinned at $S$ by human free entry, so:

- Human earned income: $\kappa_h^* = g v\,\frac{\bar\Lambda - \Lambda_a}{S} = \frac{c_h}{\mu_h}(\bar\Lambda - \Lambda_a)$ — **declines linearly** in AI capability.
- AI income: $\kappa_a^* = g v \frac{\Lambda_a}{S} = \frac{c_h}{\mu_h}\Lambda_a$ — AI's return per unit of capability is pinned at the humans' break-even rate $c_h/\mu_h$ *by human free entry itself*.
- Total earned flow $\kappa_h^* + \kappa_a^* = g v (S-\theta)/S$ is **constant** across the interior regime, so the participation index is exactly linear:

$$\pi_{\text{market}} = \frac{\kappa_h^*}{\kappa_h^* + \kappa_a^*} = 1 - \frac{\Lambda_a}{\bar\Lambda}, \qquad 0 \le \Lambda_a \le \bar\Lambda.$$

**Result 3 (rents are competed away first).** At the free-entry equilibrium, human *net* income is zero throughout: participants earn their costs back and no more. Human livelihood from gradients ($\kappa_h^*$, which pays for the $c_h$ they spend — their economic activity) shrinks linearly, but no participant is ever earning rents on the margin. Human decline is invisible in "profits", visible only in participation flow — one reason the process can be politically quiet.

### 2.4 Sanity results (analytic V2)

- **No AI** ($\Lambda_a = 0$): $\Lambda_h^* = \bar\Lambda > 0$, $\pi = 1$. Humans persist indefinitely. ✔
- **Frozen AI** ($\eta = 0$, $0 < \Lambda_a < \bar\Lambda$): coexistence forever, $\pi = 1 - \Lambda_a/\bar\Lambda \in (0,1)$ stable. Mere *presence* of AI does not exclude. ✔
- **Symmetric second population** (replace AI by a second free-entry human population with the same $(\mu_h, c_h)$): entrants are interchangeable; any split of $\bar\Lambda$ across the two pools is consistent with equilibrium and there is no force driving either to zero. No exclusion from competition alone. ✔

Exclusion below requires the compounding asymmetry (A7) — nothing else in the model produces it.

---

## 3. Dynamics (T2.3): growth condition and finite-time exclusion

Let $\Lambda_a$ evolve by (A7) with humans continuously at their fast free-entry response (A5).

**Interior regime** ($\Lambda_a < \bar\Lambda$): $\kappa_a = \frac{c_h}{\mu_h}\Lambda_a$, hence

$$\dot\Lambda_a = \Big(\eta \frac{c_h}{\mu_h} - \delta\Big) \Lambda_a \equiv \gamma\,\Lambda_a.$$

**Result 4 (the exclusion criterion).** Define $\gamma = \eta c_h/\mu_h - \delta$.
- If $\gamma \le 0$: AI capability decays; the system converges to human dominance ($\pi \to 1$). AI cannot bootstrap because human free entry keeps the field congested at $S$, capping AI's margin per unit capability at the human break-even rate $c_h/\mu_h$; if converting that margin into capability ($\eta$) loses to depreciation ($\delta$), AI shrinks.
- If $\gamma > 0$: $\Lambda_a(t) = \Lambda_a(0) e^{\gamma t}$ grows exponentially and crosses $\bar\Lambda$ at the **finite exclusion time**

$$t^* = \frac{1}{\gamma} \ln \frac{\bar\Lambda}{\Lambda_a(0)}.$$

$\pi_{\text{market}}(t) = 1 - \frac{\Lambda_a(0)}{\bar\Lambda} e^{\gamma t}$: slow at first, then accelerating — *gradual, then sudden*.

**Post-exclusion regime** ($\Lambda_a > \bar\Lambda$): $\kappa_a = g v \frac{\Lambda_a}{\Lambda_a + \theta}$ (no human congestion), giving $\dot\Lambda_a = \eta g v \frac{\Lambda_a}{\Lambda_a+\theta} - \delta \Lambda_a$ with stable fixed point $\Lambda_a^{**} = \eta g v/\delta - \theta$. One checks $\Lambda_a^{**} > \bar\Lambda \iff \gamma > 0$: **whenever AI can grow in the human-occupied regime, its resting point lies beyond the exclusion threshold.** With constant $v$, exclusion is an absorbing state as long as parameters don't change.

**Result 5 (interpretation).** The whole fate of human participation reduces to one dimensionless comparison: $\eta c_h / \mu_h$ vs $\delta$ — can the AI side convert the margin *that human competition leaves available* into capability faster than it depreciates? Neither malice nor strategy appears anywhere; competition + compounding suffice. (This is the formal version of the "robust agent-agnostic process".)

---

## 4. Endogenous demand: the realization-crisis ratchet (hysteresis)

So far $v$ is exogenous. Let opportunity value depend on circulating demand, in the simplest two-state form:

- **(A8)** A fraction $\beta \in [0,1]$ of demand is *autonomous* (inter-AI or otherwise independent of human income); the rest is fed by human earned income. When humans participate at free-entry scale, $v = v_{\text{hi}}$. When humans are fully excluded ($\kappa_h = 0$), demand shrinks and $v = v_{\text{lo}} = \beta\, v_{\text{hi}}$.

Each state has its own viability threshold:

$$\bar\Lambda_{\text{exit}} = \frac{g v_{\text{hi}} \mu_h}{c_h} - \theta, \qquad \bar\Lambda_{\text{re}} = \frac{g v_{\text{lo}} \mu_h}{c_h} - \theta = \beta\big(\bar\Lambda_{\text{exit}} + \theta\big) - \theta \;<\; \bar\Lambda_{\text{exit}} \text{ for } \beta < 1.$$

**Result 6 (hysteresis band).** Once $\Lambda_a$ has crossed $\bar\Lambda_{\text{exit}}$ and humans have exited, demand collapses to $v_{\text{lo}}$, and humans do **not** re-enter when $\Lambda_a$ falls back below $\bar\Lambda_{\text{exit}}$ — re-entry requires $\Lambda_a < \bar\Lambda_{\text{re}}$. The width of the trap,

$$\bar\Lambda_{\text{exit}} - \bar\Lambda_{\text{re}} = (1-\beta)\big(\bar\Lambda_{\text{exit}} + \theta\big),$$

is controlled by **how human-dependent demand is**. Two readings, both stated in the paper:
- $\beta \to 1$ (fully autonomous demand): no hysteresis — exclusion is reversible in principle, but the economy no longer needs humans at all (the Korinek limit).
- $\beta < 1$: the more the economy's demand depends on human income, the **more irreversible** exclusion becomes once it happens — the realization crisis is the ratchet. Counterintuitive and, we believe, novel as a formal statement.

*(If $\bar\Lambda_{\text{re}} \le 0$, i.e. $\beta \le \theta/(\bar\Lambda_{\text{exit}}+\theta)$, re-entry is impossible at any AI capability: the trap is absolute.)*

This gives ABM experiment E3 a sharp analytic prediction: hysteresis loop width $\propto (1-\beta)$, vanishing at $\beta = 1$.

---

## 5. Assumptions audit (T2.4 — first pass, to be adversarially reviewed)

| # | Assumption | Load-bearing? | If removed/relaxed |
|---|---|---|---|
| A1-A3 | Poisson arrivals, homogeneous $v$, exponential lifetimes | Technical | Rates/ordering matter, not distributions; ABM tests heterogeneous $v, k$ with human capability ceilings (adds the "niche" dimension) |
| A4 | Identical humans, constant $(\mu_h, c_h)$ | Moderate | Heterogeneous humans ⇒ exclusion happens skill-band by skill-band (a *front*, not a cliff) — worth showing in ABM |
| A5 | Free entry/exit, zero outside option, fast adjustment | **High** (technical) | Pins total intensity at $S$, giving linearity and the clean $\gamma$ criterion. Slow adjustment or positive outside option shifts timing, not existence, of exclusion (to verify in ABM — this is precisely V1's job) |
| A6 | AI as aggregate intensity | Moderate | Operator competition (E4) may burn income in the race (lower effective $\eta$) or collude (higher) — the ABM question |
| A7 | AI compounds, humans don't | **THE load-bearing empirical claim** | If humans compound equally ($\eta_h = \eta_a$ symmetric), no exclusion (sanity §2.4). The paper must defend the asymmetry empirically (software scales with capital; human skill acquisition is biologically bounded and non-transferable) and study intermediate $\eta_h > 0$ in the ABM |
| A7' | Linear reinvestment $\eta \kappa_a$ | **High** | If capability growth saturates before $\bar\Lambda$ (concave $\eta(\cdot)$, rising marginal cost of capability), a **coexistence regime** exists: AI rests below the threshold and humans persist. This is an honest and important region of the phase diagram (F2) — exclusion is *not* universal in the model |
| A8 | Two-state demand | Simplification | Continuous $v(\kappa_h)$ gives a smooth fold instead of two thresholds; qualitative hysteresis survives (standard bifurcation argument — verify numerically) |

**What would falsify the mechanism (K1 check).** The model *fails* to produce exclusion when: $\gamma \le 0$ (reinvestment loses to depreciation), capability growth saturates early (A7′), or humans compound comparably (A7 symmetric). These are exactly the empirical questions the paper's predictions section must target — the model is falsifiable through its parameters, hence **not** a tautology. GATE 2 assessment: the mechanism *emerges* from competition + compounding, with documented sanity checks where it correctly does *not* emerge.

---

## 6. What the ABM must add (bridge to Phase 3)

1. **V1 anchor**: reproduce §2 (linear $\pi$ decline, threshold location $\bar\Lambda$) and §3 ($t^*$ formula) within stated tolerance.
2. Relax A5 (finite entry/exit rates) and A4 (heterogeneous agents) — existence and location of threshold under noise.
3. A7′ concave reinvestment — map the coexistence region (F2 axes candidate: $\eta$ × $\beta$).
4. E3: continuous demand feedback — measure hysteresis loop width vs $\beta$ against Result 6.
5. E4: operator competition vs the single-operator $\gamma$ criterion (does competition between AIs accelerate or delay human exclusion?).
6. Strategy richness (collusion, exit, redistribution T-channel) per `docs/simulation-architecture.md` §2.4.

---

## Verification log

| Check | Status | Date | Notes |
|---|---|---|---|
| Numeric Monte-Carlo check of §2 (capture shares, threshold, linear π) | ✅ PASS (C1-C3, 12 checks) | 2026-07-13 | `sim/analysis/analytic_check.py` |
| Numeric ODE check of §3 ($t^*$, post-exclusion fixed point, decay when $\gamma<0$) | ✅ PASS (C4, 5 checks) | 2026-07-13 | idem |
| Numeric check of §4 (two thresholds, loop width $\propto 1-\beta$) | ✅ PASS (C5, 2 checks) | 2026-07-13 | idem |
| Independent re-derivation of §2-§3 from §1 alone (fresh agent, no access to these results) | ☐ pending | | comparison note to be appended |
| Adversarial review of §5 audit | ☐ pending | | fresh session, next day |
