# A minimal, falsifiable model of economic disempowerment — please break it

*Independent developer. This is a working post; the object it describes is small on purpose. I would rather it be attacked than admired.*

## The gap

The thesis that advanced AI could push humans out of the economic loop — not by killing us, but by making our participation unprofitable — is now stated carefully and at length. "Gradual Disempowerment" (Kulveit et al. 2025) argues that as economic, political, and cultural systems stop depending on human participation, human influence over them erodes even without any discrete catastrophe. "The Intelligence Curse" (Drago & Laine 2025) sharpens the economic half with the rentier-state analogy: an actor whose wealth comes from intelligence-on-tap loses its incentive to invest in people. Both build on earlier structural arguments — Critch's robust agent-agnostic processes (2021) and Christiano's "What Failure Looks Like" (2019).

These are qualitative arguments. As far as I can find, no one has written down a formal model that makes the mechanism precise enough to be wrong. That is the gap I am trying to fill, and this post presents a deliberately minimal first object: closed-form where possible, verified several ways, and honest about the assumptions doing the work. I am not claiming the model is realistic. I am claiming it is small, checkable, and falsifiable, and I want help finding where it breaks.

## The model in plain language

Think of the economy as a stream of profit opportunities — call them **gradients**: an arbitrage, an unmet need, a mispricing, a new idea. Gradients arrive at some rate, each is worth something to whoever captures it first, and an uncaptured gradient decays as conditions drift and the knowledge diffuses. Two populations race to capture them.

**Humans** are a fixed detection technology. A participating human pays a flow cost (time, attention, the cost of acquiring information — the participation cost of Grossman & Stiglitz 1980) and detects live gradients at some fixed rate. Crucially, there is **free entry**: humans join while participation pays and leave when it does not, with an outside option normalized to zero.

**AI operators** are the same kind of detector with one difference that carries the whole model: their capability **compounds with income**. Reinvested capture income buys more detection capability, net of depreciation. Humans get no such compounding in this version — their detection rate and cost are constant.

That single asymmetry — assumption **A7**, that software detection capability compounds with reinvested income much faster than human capability does — is the load-bearing empirical claim, and I state it as such. It is not "humans cannot improve." It is a claim about relative rates, and it is exactly the kind of claim that could be false. If you switch A7 off, or hand the same compounding to humans, the model produces no exclusion at all (I return to this). Nothing else in the setup singles out humans; "human" and "AI" are two parameter vectors, not two rulebooks.

## Four results, each with its conditions

Write the human detection rate as $\mu_h$, human flow cost as $c_h$, gradient arrival rate $g$, gradient value $v$, decay rate $\theta$, and total AI detection intensity $\Lambda_a$. Define the **saturation intensity** $S = g v \mu_h / c_h$: the total race intensity at which a marginal human exactly breaks even.

**(i) A finite exclusion threshold.** Free entry drives human net income to zero while any human participates, which pins the total race intensity at $S$. Solving for where human participation hits zero gives a threshold in AI capability,

$$\bar\Lambda = \frac{g v \mu_h}{c_h} - \theta,$$

and humans participate if and only if $\Lambda_a < \bar\Lambda$, reaching **exactly zero at the finite value $\bar\Lambda$** — not asymptotically. The threshold reads sensibly: it rises with the opportunity flow $gv$ and with human efficiency $\mu_h/c_h$, and falls with faster gradient decay $\theta$. (We assume $S > \theta$, else humans are never viable.)

**(ii) Linear, quiet decline of participation.** In the interior regime, total earned flow is constant, so the human participation share is exactly linear:

$$\pi = 1 - \frac{\Lambda_a}{\bar\Lambda}, \qquad 0 \le \Lambda_a \le \bar\Lambda.$$

Here is the politically important part, and I want to state it without drama because the model itself is undramatic here: because of free entry with a zero outside option, **human net rents are zero throughout the interior regime**. Participants earn back their costs and no more, from the first gradient to the last. Human earned income shrinks linearly toward zero, but nobody on the margin is ever visibly losing rents. The decline shows up in *participation flow*, not in *profits* — which is one structural reason a process like this could stay quiet. I flag the flip side immediately: because net surplus is already zero, this model cannot by itself represent the *welfare* harm the qualitative literature is worried about. $\pi$ measures presence in the loop, not well-being. Any normative weight requires a subsistence assumption the model does not contain.

**(iii) An exclusion criterion with no malice in it.** Let AI capability evolve by reinvestment. In the interior regime the dynamics collapse to a single dimensionless comparison. Define

$$\gamma = \frac{\eta c_h}{\mu_h} - \delta,$$

where $\eta$ converts reinvested income into capability and $\delta$ is depreciation. Then:

- If $\gamma \le 0$, AI capability decays and the system converges to human dominance. AI cannot bootstrap, because human free entry keeps the field congested and caps AI's return per unit of capability at the human break-even rate.
- If $\gamma > 0$, AI capability grows exponentially and crosses $\bar\Lambda$ at a **finite exclusion time** $t^* = \gamma^{-1}\ln(\bar\Lambda/\Lambda_a(0))$. The participation share falls slowly at first, then accelerates: gradual, then sudden.

No strategy, no coordination, no intent appears anywhere — this is a formal instance of Critch's agent-agnostic process. But "competition plus compounding" is sufficient *only jointly* with the model's other structural asymmetries, and I want those on the table as part of the claim, not as fine print: human free entry retains zero rent (so humans have nothing to reinvest), while the AI side reinvests **gross** income with no zero-profit discipline (assumption **A9**). If competition *among* AI operators dissipated their rents the way free entry dissipates human rents, the effective $\eta$ would fall and a coexistence region would open. That is an open question, not a settled result.

**(iv) A demand-side ratchet — as a consequence of an assumption, not a discovery.** Let gradient value depend on circulating demand, in the simplest two-state form (assumption **A8**): a fraction $\beta$ of demand is autonomous (independent of human income), the rest is fed by human earned income; value is $v_{\text{hi}}$ when humans participate and collapses to $v_{\text{lo}} = \beta v_{\text{hi}}$ once they are fully excluded. Each state has its own threshold, and they differ, producing **hysteresis**: once humans have exited and demand has collapsed, they do not re-enter when AI capability falls back below the exit threshold. The width of the trap is

$$\bar\Lambda_{\text{exit}} - \bar\Lambda_{\text{re}} = (1-\beta)\,S.$$

I want to be exact about the epistemic status here, because a hostile review of this model (applied in full; see below) was right to press on it. This is **not** an independent discovery. It follows algebraically from writing $v_{\text{lo}} = \beta v_{\text{hi}}$. What A8 encodes is a labeled asymmetry — human income feeds demand, AI income does not except through the fixed share $\beta$ — and *that* asymmetry, not competition and not compounding, is the entire engine of this section. It is an empirical claim (displaced humans stop buying; AI operators reinvest in inputs rather than final consumption) and it may simply be false. If AI income recirculates into final demand at scale, $\beta$ is effectively high and the ratchet weakens or vanishes. At $\beta \to 1$ there is no hysteresis at all — but then the economy no longer needs humans for demand either, which is Korinek's realization-crisis limit reached from the other side. So Result (iv) is stated strictly as *conditional on A8*, and it carries less evidentiary weight than (i)–(iii).

## The model self-correcting

I pre-registered predictions about the demand-side dynamics before running the simulation, and one of them was infirmed — which I think is the most credible thing in this post.

The two-state form of A8 is a step function: a hard nonlinearity. A de-risking run (not the production run) instead used a *continuous linear* coupling, where value tracks smoothed human income proportionally. Under that coupling the **hysteresis loop width collapsed to zero**. Exclusion still happened — in fact it arrived *earlier*, at the lower threshold $\beta S - \theta$ instead of $S - \theta$ — but it was **reversible**: value follows income symmetrically in both directions, so there is no trap. Worked out by hand, the loop gain of the linear coupling is below one, so no bistability, exactly the failure mode the adversarial review had flagged before the run.

The honest reading, which is now how I present §4, is: **exclusion is the robust part; its irreversibility is not.** And a first production sweep sharpened this once more, refuting my own registered guess in the process: I had predicted the loop would return with the *steepness* of a sigmoidal demand response. It did not — steepness alone at a mid-range threshold still gave no loop (and made exclusion *earlier*, because a steep response collapses demand sooner once income dips below its midpoint). What restores the trap is the response's **lateness**: when demand holds up until human income is nearly gone (half-response point pushed low — think savings, credit, consumption habits, or income support), a clean hysteresis loop appears (width $0.95 \pm 0.03$ at the lowest lateness tested, against a two-state limit of $2$, monotone in lateness). Status: exploratory, found after the registered prediction failed, to be confirmed on fresh seeds with a quantitative pre-registration. The economic reading is uncomfortable and testable: *smooth consumption adjustment gives an earlier but reversible collapse; consumption that holds and then gives way — which is what savings, credit, and transfer programs produce — gives a later but irreversible one.*

## How it was verified

Verification is the point of this object, so I will be concrete. The model was checked five ways: (1) a **closed-form solution** of statics and dynamics; (2) a suite of **nineteen numeric checks** — Monte-Carlo for the capture shares and threshold, ODE integration for the exclusion time and post-exclusion fixed point, and the hysteresis widths; (3) a **blind independent re-derivation** by a fresh agent given only the setup, which matched every formula symbol for symbol and raised three substantive flags now folded into the audit; (4) an **agent-based reproduction** with local-information agents that recovered the linear decline, the threshold location, and the exclusion-time formula (six of six anchor tests, within stated tolerances); and (5) a **hostile adversarial review**, whose seven required corrections are all applied in the current revision — including declaring the A8 demand asymmetry, downgrading the ratchet from "novel," stating the welfare-neutrality point, and recomputing the post-exclusion fixed point under collapsed demand (where $\beta$ cancels and the absorbing condition stays $\gamma > 0$).

A first production pass of the simulation then tested the pre-registered predictions: the **phase boundary sits exactly on the predicted line** $\delta = \eta c_h/\mu_h$ across the whole grid [Figure: f2_phase_diagram.png]; the **coexistence region under capability saturation is real** and tracks the analytic line $1 - \Lambda_{\max}/\bar\Lambda$ point by point [Figure: f2b_coexistence.png]; the collapse dynamics behave as derived [Figure: f1_pi_dynamics.png]; splitting the same aggregate capability across 1–20 operators leaves the exclusion time **exactly invariant** — confirming that without rent dissipation, competition among AIs protects no one [Figure: f4_operators.png]; and the demand-response experiment is the one described above [Figure: f3_hysteresis.png]. One registered prediction was refuted and is reported as such; the summary of verdicts lives next to the code.

## What would falsify this, and what I am unsure of

The model *fails* to produce exclusion — by design — in several regimes, and each is an empirical question the eventual paper must target:

- **$\gamma \le 0$**: reinvestment loses to depreciation, AI decays, humans persist. The whole result hangs on one inequality.
- **Early capability saturation.** If reinvestment has diminishing returns and AI capability rests *below* $\bar\Lambda$, there is a genuine coexistence region. Exclusion is not universal even inside the model.
- **Symmetric human compounding.** If humans compound like AI, the exclusion vanishes and the story becomes "the un-augmented" versus "the augmented," not "humans" versus "AI."
- **Operator competition (E4).** If AI operators compete their rents away, the effective reinvestment rate falls and coexistence grows — the analogue of free entry, applied to the AI side. The first pass established the null half of this: merely *splitting* capability across many operators changes nothing (exact invariance); everything therefore rides on whether real AI-vs-AI competition dissipates rents — noting the uncomfortable real-world observation that current AI actors reinvest at a loss, funded by capital markets on expected future income, which would bypass rent discipline entirely.

Two deeper objections I take as the strongest:

- **No general equilibrium (assumption A10).** Arrival rate $g$ and value $v$ are exogenous. The economy that *generates* gradients is not modeled, and there is no Schumpeterian regeneration — abundance does not open new niches faster. A Korinek-style critic would attack this first, and rightly: endogenizing $g$, or letting AI income recirculate as demand, could reverse both the exclusion and the ratchet. Everything here is a partial-equilibrium statement.
- **Participation is a value-laden choice.** $\pi$ counts *earned participation*, not ownership. A human who owns AI capacity but does not operate is, by this definition, out of the loop — their income is reported in a separate series, never folded into the headline. That is a defensible choice (owning is not participating) but it is a choice, and the two-channel accounting behind it — demand source-agnostic, participation self-enforcing-only — is exactly the kind of thing reasonable people will disagree about. The current dynamics also do not let a human *buy* the compounding channel; if they can, "human exclusion" partly becomes a distribution question among humans.

## What's next, and the ask

The analytic model is a skeleton. Next is the full agent-based program: the phase diagram of coexistence versus exclusion, the hysteresis mapping under nonlinear demand, and operator competition against the single-operator criterion — plus empirical anchoring on the cleanest laboratory I can find, gig-level freelance-platform earnings before and after capable models, and early agentic-economy data as it appears.

The ask is specific. I would most value criticism of the **assumptions audit**, and above all of the three assumptions doing the real work: **A7** (that AI capability compounds with income far faster than human capability), **A8** (that human income feeds final demand and AI income largely does not), and **A9** (that AI reinvests gross income with no zero-profit discipline). If any of those three is wrong in a way I have not accounted for, the corresponding result should fall — and I would rather learn that here than later. Here is a small, verified, falsifiable object. Please break it.
