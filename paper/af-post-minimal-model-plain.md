# A small, testable model of humans being priced out of the economy: please break it

> **How this was made.** I'm an electronics and embedded-systems engineer, not an economist. This post, the math, and the simulation code were produced with heavy AI assistance, under my direction, over a few nights. I say this up front because site policy asks for it and because it's the honest framing.
>
> What I'm asking you to judge is not the prose but the object behind it: a public repo with a formal model, closed-form results, four independent verification passes, and pre-registered predictions, one of which failed and is reported as a failure. Code and derivations: github.com/MatioRIGARD/gradient-exhaustion
>
> Why I decided to look into this topic: I've come to believe the alignment problem is at least as much an economic problem as a technical one. This is my attempt to make one piece of that belief precise enough to be wrong.

## What's missing in the existing arguments

Several careful essays argue that advanced AI could push humans out of the economy, not by harming anyone, just by making human participation unprofitable. "Gradual Disempowerment" (Kulveit et al. 2025) makes the general case: when economic and political systems stop needing human input, human influence over them fades, no catastrophe required. "The Intelligence Curse" (Drago & Laine 2025) adds an analogy from oil states: an actor that gets its wealth from intelligence-on-tap loses its incentive to invest in people. Earlier versions of the structural argument are Critch (2021) and Christiano (2019).

These are all arguments in words. As far as I can tell, nobody has written the mechanism down as a formal model, something with equations, where you can point at an assumption and say "this one is false, so the conclusion fails." That's the gap this post tries to fill. The model is deliberately tiny. I'm not claiming it's realistic. I'm claiming it's small enough to check, and wrong in ways you can actually find.

## The model, in plain words

Picture the economy as a stream of short-lived profit opportunities. A mispriced asset, an unmet need, a client looking for a freelancer, a new niche. Call each one a **gradient**. Gradients appear at some rate, each is worth money to whoever grabs it first, and if nobody grabs it, it fades (the mispricing corrects itself, the client finds another way).

Two kinds of players race to grab them.

**Humans.** Participating costs a human something per unit of time: attention, effort, staying informed. In exchange they spot gradients at some fixed rate. And there's a crucial rule called **free entry**: as long as participating pays better than staying out, more humans join; when it stops paying, they leave. (This is the standard way economists model an open market. Think of how food-delivery apps filled up with couriers exactly until the pay stopped being attractive.)

**AI operators.** Exactly the same kind of player, with one difference, and this one difference drives the whole model: **their income makes them better at the game**. Money earned gets reinvested into more compute, better models, more detection capacity. Humans in this version get no such loop: their speed and cost stay flat.

That single asymmetry is assumption **A7**, and I want to flag it as the model's main empirical bet. It does *not* say humans can't improve. It says software capability compounds with reinvested income much faster than human capability does. That's a claim about the real world, and it could be false. If you switch it off, or give humans the same compounding, the model produces no exclusion at all. Nothing else in the setup treats humans and AI differently: they are two parameter settings of the same agent, not two rulebooks.

## Four results

A few symbols, so the formulas below are readable:

- $\mu_h$: how fast one human spots gradients; $c_h$: what participating costs them per unit of time
- $g$: how often gradients appear; $v$: what each is worth; $\theta$: how fast an ungrabbed one fades
- $\Lambda_a$: total AI detection capability (the AI side's "speed")

One derived quantity matters: $S = g v \mu_h / c_h$, the level of total competition at which one more human would exactly break even. Everything below is a consequence of free entry pushing the market to that level.

**(i) There is a finite cutoff, not a slow fade.** Humans participate if and only if AI capability is below a threshold

$$\bar\Lambda = \frac{g v \mu_h}{c_h} - \theta.$$

At that value, human participation hits exactly zero, not "approaches zero eventually." The threshold behaves sensibly: more opportunities or more efficient humans push it up (harder to exclude humans); faster-fading gradients pull it down.

**(ii) The decline is linear, and quiet.** Below the threshold, the human share of participation is a straight line:

$$\pi = 1 - \frac{\Lambda_a}{\bar\Lambda}.$$

Here's the part I find politically important. Because of free entry, humans in this market never earn more than their costs: competition among humans has already eaten the surplus, with or without AI. So as AI capability grows, no participant ever sees their *profits* fall; what shrinks is the *number of humans for whom showing up still makes sense*. The decline is invisible in anyone's margins and visible only in headcount. That's one structural reason a process like this could stay quiet until late.

The flip side, stated honestly: since net surplus is zero throughout, this model cannot by itself say anything about *welfare*, about people getting hurt. $\pi$ measures presence in the economic loop, not well-being. Connecting the two would need a subsistence assumption the model doesn't contain.

**(iii) One number decides the outcome, and no one has to want it.** Now let AI capability grow by reinvestment. In the regime where humans still participate, everything collapses into one comparison:

$$\gamma = \frac{\eta c_h}{\mu_h} - \delta,$$

where $\eta$ is how efficiently reinvested income becomes new capability and $\delta$ is how fast capability depreciates (models go stale, hardware ages). In words: **can the AI side turn its earnings into new capability faster than the old capability rots?**

- If no ($\gamma < 0$): AI capability shrinks and humans end up dominant. Interestingly, human free entry is what starves it: the crowded field caps what AI earns per unit of capability.
- If yes ($\gamma > 0$): AI capability grows exponentially and crosses the threshold at a **finite, computable date** $t^* = \gamma^{-1}\ln(\bar\Lambda/\Lambda_a(0))$. Human participation falls slowly at first, then fast. Gradual, then sudden.

No strategy, no coordination, no intent appears anywhere in this; it's a formal instance of what Critch calls an agent-agnostic process. But I want the fine print in the main text: "competition plus compounding" only produces this because of two more structural assumptions. Humans, under free entry, keep zero surplus, so they have nothing to reinvest. The AI side, by assumption **A9**, reinvests its *gross* income and faces no such competitive discipline. If competition *between* AI operators burned away their margins the way competition between humans does, the effective $\eta$ would drop and a coexistence region would open up. Whether real AI competition works that way is an open question, not something the model settles.

**(iv) A possible point of no return, but only if you buy one more assumption.** So far the value of gradients was fixed. Now add assumption **A8**: gradient value depends on demand, and human income is what feeds most of that demand. Concretely: a fraction $\beta$ of demand is autonomous (doesn't care about human income), the rest is human spending. While humans participate, value is high; once they're fully excluded, their spending is gone and value drops to $\beta$ times its old level.

Lower value means a lower threshold. So the model now has *two* thresholds: the one where humans exit, and a lower one below which AI capability would have to fall for re-entry to pay. Between the two is a trap (the economics name is **hysteresis**): the door humans exit through is higher than the door they'd need to come back in through. Even if AI capability later declines below the exit point, humans don't come back, because the demand their own incomes used to provide is gone. The width of the trap is $(1-\beta)\,S$.

I want to be precise about what this result is, because a hostile review of the model rightly pressed on it. It is **not** a discovery; it follows in one line of algebra from assuming the value drop. All the work is done by A8's asymmetry: human income feeds final demand, AI income mostly doesn't (operators buy compute and inputs, not groceries). That's an empirical claim and it may be false: if AI income does flow back into final demand at scale, $\beta$ is high and the trap shrinks or vanishes. (At $\beta = 1$ there's no trap at all, but then the economy no longer needs human demand either, which is its own unsettling limit, cf. Korinek's realization crisis.) So result (iv) is strictly *conditional on A8*, and it carries less weight than (i) to (iii).

## Where the model corrected me

Before running the simulation, I wrote down predictions. One of them failed, and I think that failure is the most credible thing in this post.

The two-state version of A8 above (value high, then suddenly low) is a hard on/off switch. A test run replaced it with the smoothest possible alternative, where value simply tracks human income, proportionally. Under that version, **the trap disappeared entirely.** Exclusion still happened, and actually happened *earlier*, but it was reversible: value follows income back up just as it followed it down. Checked by hand, the feedback in the smooth version is just too weak to create two stable states.

So the honest summary became: **exclusion is the robust result; irreversibility is not.**

Then the first production sweep refuted my *next* guess too. I had predicted the trap would come back if the demand response was steep enough (an S-curve instead of a straight line). Wrong: steepness alone did nothing, and even made exclusion earlier. What actually restores the trap is **lateness**: when demand holds up until human income is nearly gone, and only then gives way, a clean hysteresis loop reappears. And "demand that holds and then gives way" is exactly what savings, consumer credit, habits, and income support produce.

Because I found this only after my registered prediction failed, I treated it as exploratory: I re-registered it quantitatively and ran a confirmation on ten fresh seeds at half the ramp speed. Loop width $+0.64 \pm 0.13$ under late demand versus $-0.14 \pm 0.08$ under smooth demand (the confidence intervals don't overlap, and all three registered confirmation predictions passed). A static fixed-point analysis of the same demand equations, done independently of the simulation, agrees. (One precision note: a steep mid-range response does open a narrow trap zone at low AI capability in the static analysis, which the noisy finite-population simulation escapes; the sharp claim is about the trap near the exclusion boundary.)

The economic reading is uncomfortable and testable: *smooth consumption adjustment gives an earlier but reversible collapse; consumption that holds and then breaks (which is what savings, credit, and transfer programs produce) gives a later but irreversible one.*

## How it was checked

The point of building a small object is that it can actually be verified, so here is the list:

1. **Nineteen numeric checks**: Monte-Carlo for the capture probabilities and threshold, numerical integration for the exclusion date and the post-exclusion resting point, and the trap widths.
2. **A blind re-derivation**: a fresh agent, given only the setup, re-derived every formula independently and matched them symbol for symbol (it also raised three substantive issues, now folded into the audit).
3. **An agent-based reproduction**: a simulation of individual agents with only local information recovered the linear decline, the threshold location, and the exclusion-date formula (six of six anchor tests within tolerance).
4. **A hostile adversarial review**: seven required corrections, all applied, including declaring the A8 asymmetry openly, downgrading the trap result from "novel," and adding the welfare caveat in result (ii).

The first production runs then tested the pre-registered predictions. The boundary between "AI grows" and "AI shrinks" lands exactly on the predicted line $\delta = \eta c_h/\mu_h$ across the whole parameter grid.

![f2_phase_diagram](https://raw.githubusercontent.com/MatioRIGARD/gradient-exhaustion/refs/heads/master/paper/figures/f2_phase_diagram.png)

When capability growth saturates early, the predicted coexistence region is there and tracks the analytic formula point by point.

![f2b_coexistence](https://raw.githubusercontent.com/MatioRIGARD/gradient-exhaustion/refs/heads/master/paper/figures/f2b_coexistence.png)

Collapse dynamics behave as derived.

![f1_pi_dynamics](https://raw.githubusercontent.com/MatioRIGARD/gradient-exhaustion/refs/heads/master/paper/figures/f1_pi_dynamics.png)

Splitting the same total AI capability across 1 to 20 operators leaves the exclusion date exactly unchanged, confirming that *without* margin-destroying competition, "many AIs instead of one" protects no one.

![f4_operators](https://raw.githubusercontent.com/MatioRIGARD/gradient-exhaustion/refs/heads/master/paper/figures/f4_operators.png)

Two further registered rounds tested the obvious policy levers, with sobering results. **Redistribution** (taxing AI income and transferring it to humans) prevents exclusion only above a near-confiscatory rate, about 92% at baseline parameters, because the tax has to beat exponential compounding. Below that, transfers buy time and buy survival, but not participation: after exclusion, the human share of income equals the tax rate exactly. Kept alive, out of the loop, and now a measurable regime. (Also: this is a single-jurisdiction result. In the real world, unilateral taxation invites capability to migrate to whoever taxes least, so the lever requires coordination, which is the disempowerment problem again, one level up.) **Competition between operators** protects humans only if it destroys about 97% of their margins; with collusion, the unprotected outcome returns exactly. A first attempt at early-warning signals (statistical tremors before the collapse) came up negative with a naive estimator, and is reported as negative, not spun.

One registered prediction was refuted and is reported as refuted. The verdict summary lives next to the code.

## What would prove this wrong

The model itself names the conditions under which no exclusion happens, each one an empirical question:

- **$\gamma \le 0$.** If turning AI income into capability loses to depreciation, AI never bootstraps. The whole result hangs on one inequality.
- **Early saturation.** If reinvestment hits diminishing returns and AI capability plateaus *below* the threshold, humans and AI coexist indefinitely. Exclusion is not universal even inside the model.
- **Human compounding.** If humans can compound like AI (tools, augmentation), exclusion vanishes; the story becomes "augmented vs. un-augmented humans," a different (and more tractable) problem.
- **AI-vs-AI competition.** If operators compete their margins away, effective reinvestment falls and coexistence grows. The simulation established the null half: merely having many operators changes nothing. Everything rides on whether real competition destroys margins. Note the uncomfortable real-world data point that current AI companies reinvest *at a loss*, funded by capital markets on expected future income, which would bypass margin discipline entirely.

And the two objections I consider strongest:

- **No general equilibrium.** The stream of opportunities is fixed from outside the model. The economy that *generates* opportunities isn't modeled, and there's no Schumpeterian regeneration, no mechanism by which AI-driven abundance opens new niches faster. An economist would attack here first, and rightly. Everything above is a partial statement about one market, not the whole economy.
- **"Participation" is a choice of definition.** $\pi$ counts *earned* participation. A human who owns AI capacity but doesn't operate anything is, by this definition, out of the loop; their income is tracked in a separate series, never folded into the headline number. I think that's defensible (owning is not participating), but it is a choice, and reasonable people will disagree. The current model also doesn't let a human *buy into* the compounding channel; if they can, "human exclusion" becomes partly a question of distribution among humans.

## The ask

Next steps are the full agent-based program (the coexistence/exclusion phase diagram, the demand-lateness mapping, operator competition), plus empirical anchoring on the cleanest data I can find: freelance-platform earnings before and after capable models, and early agentic-economy data as it appears.

But the ask here is specific. The three assumptions doing the real work are:

- **A7**: AI capability compounds with income much faster than human capability;
- **A8**: human income feeds final demand, AI income mostly does not;
- **A9**: AI reinvests gross income, undisciplined by competition.

If any of these is wrong in a way I haven't accounted for, the corresponding result falls, and I'd rather learn it here than on arXiv. The model is small, checked, and public. Please break it.
