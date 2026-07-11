# Blind re-derivation: human–AI opportunity-capture model

*Independent derivation from the problem statement only. Continuous-time Poisson race
model with free human entry and accumulating AI capability.*

## 0. Setup, notation, and modeling assumptions

Opportunities arrive at Poisson rate $g$, each worth $v$ to the first detector, and each
uncaptured opportunity expires at rate $\theta$. Human participants each pay flow cost
$c_h$ and detect a *given* live opportunity at rate $\mu_h$; with $n_h$ identical
participants the aggregate human detection intensity is $\Lambda_h = n_h\mu_h$. The AI has
aggregate detection intensity $\Lambda_a\ge 0$. All detection and expiry clocks are
independent exponentials.

**Assumptions I make explicit (needed for a well-posed model):**

- **(A1) No congestion / unbounded concurrency.** Each agent races each live opportunity
  independently at rate $\mu_h$; there is no per-agent capacity limit and no diminishing
  returns to holding many live opportunities at once. This makes captures — and hence
  income — *linear* in $\Lambda_h$. (The phrase "detects any given live opportunity at rate
  $\mu_h$, independent across opportunities and agents" strongly implies this.)
- **(A2) Free entry pins net rent to zero.** Humans enter while expected net flow income is
  $>0$ and exit while $<0$; entry/exit is infinitely fast (quasi-static), so participation
  always sits at its zero-net-rent level (or at the $\Lambda_h=0$ corner).
- **(A3) Outside option $0$; risk neutrality; steady state.** Income is expected flow value.

### The single-opportunity race

A live opportunity faces three competing exponential hazards: total human detection
$\Lambda_h$, AI detection $\Lambda_a$, and expiry $\theta$. The first event wins, so

$$
\Pr(\text{human}) = \frac{\Lambda_h}{\Lambda_h+\Lambda_a+\theta},\quad
\Pr(\text{AI}) = \frac{\Lambda_a}{\Lambda_h+\Lambda_a+\theta},\quad
\Pr(\text{expire}) = \frac{\theta}{\Lambda_h+\Lambda_a+\theta}.
$$

Opportunities arrive at rate $g$ and resolve independently, so the **gross income flows** are

$$
\boxed{\;\kappa_h = \frac{g\,v\,\Lambda_h}{\Lambda_h+\Lambda_a+\theta},\qquad
\kappa_a = \frac{g\,v\,\Lambda_a}{\Lambda_h+\Lambda_a+\theta}. \;}
$$

A single tagged agent (hazard $\mu_h$) captures at rate $g\mu_h/(\Lambda_h+\Lambda_a+\theta)$,
so **per-participant gross income** is
$g v \mu_h/(\Lambda_h+\Lambda_a+\theta)$ — note it is independent of the stock of live
opportunities, because arrival scaling and race-share scaling cancel.

---

## Q1. Free-entry human level, income flows, and human share

### Free-entry condition

Per-participant net flow is $\dfrac{g v \mu_h}{\Lambda_h+\Lambda_a+\theta} - c_h$. Interior
free entry (A2) sets it to zero:

$$
\frac{g v \mu_h}{\Lambda_h+\Lambda_a+\theta} = c_h
\;\;\Longrightarrow\;\;
\Lambda_h+\Lambda_a+\theta = \frac{g v \mu_h}{c_h}\equiv S.
$$

**Key structural fact:** free entry *pins the total hazard* $\Lambda_h+\Lambda_a+\theta$ to
the constant $S \equiv gv\mu_h/c_h$, regardless of $\Lambda_a$. Hence

$$
\boxed{\;\Lambda_h^\*(\Lambda_a) = S - \theta - \Lambda_a
= \frac{gv\mu_h}{c_h} - \theta - \Lambda_a,\;}
$$

valid while positive. Define the **critical AI intensity**

$$
\boxed{\;\Lambda_a^{\mathrm{crit}} = S - \theta = \frac{gv\mu_h}{c_h} - \theta.\;}
$$

- **Regime A (coexistence), $0\le \Lambda_a < \Lambda_a^{\mathrm{crit}}$:** $\Lambda_h^\*>0$,
  crowding out is **one-for-one** ($d\Lambda_h^\*/d\Lambda_a=-1$).
- **Regime B (exclusion), $\Lambda_a\ge \Lambda_a^{\mathrm{crit}}$:** $\Lambda_h^\*=0$. Even a
  lone entrant earns $gv\mu_h/(\Lambda_a+\theta)\le c_h$, so nobody enters.

*(Precondition: $S>\theta$, i.e. $gv\mu_h/c_h>\theta$, else humans never participate even at
$\Lambda_a=0$ — the market is simply unprofitable, not "excluded"; flagged.)*

### Income flows

In **Regime A** the denominator is the constant $S$, so using $gv/S = c_h/\mu_h$:

$$
\kappa_h = \frac{gv\,\Lambda_h^\*}{S} = gv - (\theta+\Lambda_a)\frac{c_h}{\mu_h},
\qquad
\kappa_a = \frac{gv\,\Lambda_a}{S} = \Lambda_a\,\frac{c_h}{\mu_h}.
$$

- $\kappa_h$ **falls linearly** in $\Lambda_a$ (slope $-c_h/\mu_h$), hitting $0$ exactly at
  $\Lambda_a^{\mathrm{crit}}$.
- $\kappa_a$ **rises linearly** in $\Lambda_a$ (slope $+c_h/\mu_h$).
- Total earned income $\kappa_h+\kappa_a = gv(S-\theta)/S = gv - \theta c_h/\mu_h$ is
  **constant** in Regime A: the expired fraction $\theta/S$ is fixed, so AI gains exactly
  what humans lose.
- Note $\kappa_h = n_h c_h$ identically: **human net rent is zero throughout Regime A**;
  $\kappa_h$ is gross income entirely absorbed by costs. (Important for interpretation of
  $\pi$ below.)

In **Regime B** ($\Lambda_h=0$):
$\kappa_h=0$, $\;\kappa_a = \dfrac{gv\Lambda_a}{\Lambda_a+\theta}$ (concave, saturating at
$gv$ as $\Lambda_a\to\infty$).

**Continuity:** at $\Lambda_a=\Lambda_a^{\mathrm{crit}}$ both formulas give
$\kappa_a = gv(S-\theta)/S$ and $\kappa_h=0$; the functions are continuous with a **kink**
(the "regime change" is a loss of smoothness / crowd-out slope change, not a jump).

### Human share of earned income

$$
\pi(\Lambda_a)=\frac{\kappa_h}{\kappa_h+\kappa_a}
=\begin{cases}
\displaystyle 1-\frac{\Lambda_a}{S-\theta}=1-\frac{\Lambda_a}{\Lambda_a^{\mathrm{crit}}},
& 0\le\Lambda_a<\Lambda_a^{\mathrm{crit}},\\[2mm]
0, & \Lambda_a\ge \Lambda_a^{\mathrm{crit}}.
\end{cases}
$$

$\pi$ **declines linearly from $1$ to $0$** across $[0,\Lambda_a^{\mathrm{crit}}]$, then stays
$0$. (Caveat: $\pi$ is the share of *gross earned* income; human *net surplus* is zero
throughout Regime A, so $\pi$ overstates human welfare.)

---

## Q2. AI capability dynamics $\dot\Lambda_a = \eta\kappa_a - \delta\Lambda_a$

With humans always at their fast free-entry response, substitute the Regime-A income
$\kappa_a=\Lambda_a c_h/\mu_h$:

$$
\dot\Lambda_a = \eta\,\Lambda_a\frac{c_h}{\mu_h} - \delta\Lambda_a
= \Lambda_a\underbrace{\left(\frac{\eta c_h}{\mu_h}-\delta\right)}_{\displaystyle r}.
$$

This is **linear** (AK / endogenous-growth form): per-capita growth $r$ is **independent of
$\Lambda_a$**, because in Regime A the AI's income per unit intensity is the constant
$c_h/\mu_h$. $\Lambda_a=0$ is always a fixed point.

**Growth vs decay condition (Regime A):**

$$
\boxed{\;\dot\Lambda_a>0 \iff \frac{\eta c_h}{\mu_h}>\delta \iff \eta c_h>\delta\mu_h
\;\;(r>0).\;}
$$

### Case $r<0$ ($\eta c_h<\delta\mu_h$): AI dies out
$\Lambda_a\to 0$ from any start (in Regime B the bracket
$\eta gv/(\Lambda_a+\theta)-\delta$ is $\le r<0$ for all $\Lambda_a\ge\Lambda_a^{\mathrm{crit}}$,
so it decays back through the threshold in finite time and on to $0$).
**Global attractor:** $\Lambda_a=0$, full participation $\Lambda_h^\*=S-\theta$, $\pi=1$.

### Case $r>0$ ($\eta c_h>\delta\mu_h$): runaway exclusion
$\Lambda_a=0$ is **unstable**; any $\Lambda_a(0)>0$ grows exponentially,
$\Lambda_a(t)=\Lambda_a(0)e^{rt}$, and reaches $\Lambda_a^{\mathrm{crit}}$ in **finite time**

$$
\boxed{\;t^\* = \frac{1}{r}\,\ln\!\frac{\Lambda_a^{\mathrm{crit}}}{\Lambda_a(0)}
= \frac{\ln\big[(gv\mu_h/c_h-\theta)/\Lambda_a(0)\big]}{\eta c_h/\mu_h-\delta}.\;}
$$

At $t^\*$ **human participation collapses to zero** (finite-time exclusion). Thereafter, in
Regime B, $\dot\Lambda_a=\Lambda_a\big(\eta gv/(\Lambda_a+\theta)-\delta\big)$ has the stable
fixed point

$$
\boxed{\;\Lambda_a^{\infty}=\frac{\eta g v}{\delta}-\theta,\;}
$$

approached **asymptotically (infinite time)**. One checks
$\Lambda_a^{\infty}\ge\Lambda_a^{\mathrm{crit}} \iff \eta/\delta\ge\mu_h/c_h \iff r\ge0$:
**the very same condition** $r>0$ both (i) makes AI grow through the threshold and (ii) places
the saturation point above the threshold. So the Q1 critical value $\Lambda_a^{\mathrm{crit}}$
is crossed **iff** $r>0$.

**Summary of attractors:**

| condition | attractor | humans |
|---|---|---|
| $r<0$ | $\Lambda_a=0$ | full participation, $\pi=1$ |
| $r=0$ | line of neutral fixed points in Regime A (degenerate) | marginal |
| $r>0$ | $\Lambda_a^\infty=\eta gv/\delta-\theta$ | excluded in finite time $t^\*$, $\pi=0$ |

The knife-edge is $\eta c_h = \delta\mu_h$. When $r>0$ the outcome is a **tipping point**: an
arbitrarily small seed AI intensity triggers full human exclusion.

---

## Q3. Endogenous value $v$: hysteresis and irreversibility

Let $v=v_{hi}$ while humans participate and $v=\beta v_{hi}$ ($0<\beta<1$) once humans are
fully excluded. Define $S(v)=gv\mu_h/c_h$, so thresholds scale with $v$:
$\Lambda_a^{\mathrm{crit}}(v)=S(v)-\theta$. Ramp $\Lambda_a$ up quasi-statically, then down.

**Upward ramp.** Humans participate ($v=v_{hi}$) and remain so until

$$
\Lambda_{\mathrm{up}} = S(v_{hi})-\theta = \frac{g v_{hi}\mu_h}{c_h}-\theta.
$$

At $\Lambda_a=\Lambda_{\mathrm{up}}$ humans are excluded and value drops to $\beta v_{hi}$.

**Downward ramp.** Now $v=\beta v_{hi}$; a would-be re-entrant earns
$g\beta v_{hi}\mu_h/(\Lambda_a+\theta)$, which exceeds $c_h$ only once

$$
\Lambda_{\mathrm{down}} = S(\beta v_{hi})-\theta = \frac{\beta g v_{hi}\mu_h}{c_h}-\theta.
$$

Since $\beta<1$, $\;\Lambda_{\mathrm{down}}<\Lambda_{\mathrm{up}}$: the system is **not
reversible**. For $\Lambda_a\in(\Lambda_{\mathrm{down}},\Lambda_{\mathrm{up}})$ the state is
**bistable** (humans-in-at-$v_{hi}$ or humans-out-at-$\beta v_{hi}$), selected by history — a
hysteresis loop / fold catastrophe.

**Size of the irreversibility effect (hysteresis width):**

$$
\boxed{\;\Delta\Lambda = \Lambda_{\mathrm{up}}-\Lambda_{\mathrm{down}}
=(1-\beta)\,\frac{g v_{hi}\mu_h}{c_h}=(1-\beta)\,S(v_{hi}).\;}
$$

Width is **proportional to $(1-\beta)$**: $\beta\to1$ recovers reversibility (no loop);
$\beta\to0$ gives maximal width $S(v_{hi})$.

**Permanent-exclusion threshold.** $\Lambda_{\mathrm{down}}\ge0$ requires
$\beta\ge \theta c_h/(gv_{hi}\mu_h)=\theta/S(v_{hi})\equiv\beta_{\mathrm{crit}}$. If

$$
\boxed{\;\beta<\beta_{\mathrm{crit}}=\frac{\theta c_h}{g v_{hi}\mu_h},\;}
$$

then $\Lambda_{\mathrm{down}}<0$: once humans are excluded they **never return, even at
$\Lambda_a=0$** — the value collapse alone renders participation unprofitable. Irreversibility
is then total.

---

## Q4. Sanity checks

**(a) $\Lambda_a=0$.** $\Lambda_h^\*=S-\theta=gv\mu_h/c_h-\theta>0$ (given $S>\theta$),
$\pi=1$. Humans capture all non-expired opportunities; nobody is excluded. (If $S\le\theta$
nobody participates, but that is an unprofitable market, not competitive exclusion — flagged.)

**(b) $\Lambda_a$ frozen $>0$, $\eta=0$.** No dynamics. If $\Lambda_a<\Lambda_a^{\mathrm{crit}}$:
**stable coexistence**, $\Lambda_h^\*=S-\theta-\Lambda_a>0$, $\pi\in(0,1)$. Only if the frozen
$\Lambda_a\ge\Lambda_a^{\mathrm{crit}}$ (exogenously large) are humans excluded. **Without the
growth feedback there is no runaway**: a moderate AI coexists indefinitely with humans.

**(c) AI replaced by a second identical free-entry human population.** Both obey the same
zero-profit condition; the common free-entry equation pins only the **sum**:
$\Lambda_1+\Lambda_2+\theta=S=gv\mu_h/c_h$, i.e. $\Lambda_1+\Lambda_2=S-\theta$, with the
split **indeterminate** (a continuum of equilibria; symmetric one $\Lambda_1=\Lambda_2=(S-\theta)/2$).
**Neither population is excluded** — they share. A free-entry population *cannot* grow without
bound because entry stops when net rent hits zero; it has no retained earnings to convert into
durable capability.

**The asymmetry that drives exclusion (Q2) is not that AI is "better" — $\mu$ and cost play
symmetric roles.** It is that **free entry holds humans at zero net rent** (nothing to
reinvest, no accumulation), whereas the AI converts its **gross** earnings $\kappa_a$ into
durable, accumulating intensity via $\eta$, with only depreciation $\delta$ as a brake and
**no zero-profit condition disciplining its growth**. Remove that accumulation channel (η=0,
case b) or impose free entry on the competitor (case c), and exclusion disappears.

---

## Flags: ambiguities / ill-posedness in the setup

1. **Congestion/capacity unspecified (A1).** Linearity of income in $\Lambda_h$ hinges on
   unbounded concurrency. Any per-agent capacity limit would make $\kappa_h$ concave and
   change the crowd-out geometry. The stated rate structure supports linearity, but it should
   be made explicit.
2. **Gross vs net asymmetry.** $\kappa_a$ enters the AI ODE as *gross* income reinvested,
   while humans are charged $c_h$ and driven to zero net rent. This gross/net asymmetry is the
   entire engine of the result and should be justified (why doesn't the AI face an analogous
   opportunity cost, or a competitive zero-profit brake?).
3. **"Human income share $\pi$" vs welfare.** $\pi$ is a share of *gross earned* income; human
   *net* surplus is identically zero in Regime A. $\pi>0$ therefore does not mean humans are
   better off — only that they are still transacting.
4. **Precondition $S>\theta$.** Needed for any human participation; otherwise "no
   participation" is a market-viability issue, not exclusion. Similarly $\beta_{\mathrm{crit}}$
   in Q3 marks where re-entry becomes impossible for all $\Lambda_a\ge0$.
5. **$r=0$ knife-edge** yields a non-generic continuum of fixed points; the model's prediction
   is discontinuous there.

---

## Compact result list

- Free-entry pins total hazard: $\Lambda_h+\Lambda_a+\theta = S\equiv gv\mu_h/c_h$.
- $\Lambda_h^\*=S-\theta-\Lambda_a$ (one-for-one crowd-out); $\;\Lambda_a^{\mathrm{crit}}=S-\theta$.
- Regime A: $\kappa_h=gv-(\theta+\Lambda_a)c_h/\mu_h$, $\;\kappa_a=\Lambda_a c_h/\mu_h$,
  $\;\pi=1-\Lambda_a/(S-\theta)$; total earned $=gv-\theta c_h/\mu_h$ constant.
- Regime B: $\kappa_h=0$, $\;\kappa_a=gv\Lambda_a/(\Lambda_a+\theta)$, $\;\pi=0$ (continuous, kinked).
- Growth condition: $\dot\Lambda_a>0\iff \eta c_h>\delta\mu_h$ ($r=\eta c_h/\mu_h-\delta>0$);
  Regime A is linear, growth rate $r$ constant in $\Lambda_a$.
- Finite-time exclusion: $t^\*=\tfrac1r\ln(\Lambda_a^{\mathrm{crit}}/\Lambda_a(0))$; then
  saturate asymptotically at $\Lambda_a^\infty=\eta gv/\delta-\theta$.
- Attractors: $r<0\Rightarrow\Lambda_a=0$ (π=1); $r>0\Rightarrow\Lambda_a^\infty$ (π=0).
  $\Lambda_a^\infty\ge\Lambda_a^{\mathrm{crit}}\iff r\ge0$.
- Q3 hysteresis: $\Lambda_{\mathrm{up}}=S(v_{hi})-\theta$,
  $\Lambda_{\mathrm{down}}=\beta S(v_{hi})-\theta$; width $\Delta\Lambda=(1-\beta)gv_{hi}\mu_h/c_h$.
  Permanent exclusion if $\beta<\beta_{\mathrm{crit}}=\theta c_h/(gv_{hi}\mu_h)$.
