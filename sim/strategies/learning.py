"""Experience-based learning: agents act on their OWN realized income only.

No agent reads the market-thickness signal. Inactive agents probe at a small
rate (optimistic exploration); active agents accumulate their personal net
income and, at Poisson review times, stay only if their own experience since
the last review was profitable. The individual-bandit level: noisier, uses
strictly less information than the other two rules — if the headline results
survive it, they do not depend on agents observing aggregate statistics.

KNOWN LIMITATION (2026-07-13): in the baseline regime income lumps (~v) are
large relative to per-review costs, so a single agent's review is nearly a
coin flip (P(net>0) ~ 0.49 in a losing market vs 0.59 in a break-even one);
the stationary population barely discriminates profitable from unprofitable
markets. Making individual-experience learning informative here requires much
slower personal timescales (and correspondingly long runs). Follow-up task;
robustness claims currently rest on replicator + best_response + the analytic
anchor. Do NOT use this rule for production experiments yet.
"""

from __future__ import annotations

import numpy as np

from sim.core.agents import HumanPopulation


class LearningRule:
    def __init__(self, n_pool: int, review_rate: float = 0.05, probe_rate: float = 0.02):
        self.review_rate = review_rate
        self.probe_rate = probe_rate
        self.net_acc = np.zeros(n_pool)
        self._prev_wealth = np.zeros(n_pool)

    def apply(self, humans: HumanPopulation, rng: np.random.Generator, dt: float) -> None:
        # accumulate each active agent's realized net income via its wealth delta
        # (wealth integrates capture income minus cost; the grubstake cap rarely
        # binds between reviews at these scales)
        delta = humans.wealth - self._prev_wealth
        self.net_acc[humans.active] += delta[humans.active]

        reviews = humans.active & (rng.random(humans.active.size) < self.review_rate * dt)
        quit_idx = np.flatnonzero(reviews & (self.net_acc < 0.0))
        if quit_idx.size > 0:
            humans.active[quit_idx] = False
        self.net_acc[reviews] = 0.0

        candidates = np.flatnonzero(~humans.active)
        n_in = min(candidates.size, rng.poisson(self.probe_rate * dt * max(1, candidates.size)))
        if n_in > 0:
            chosen = rng.choice(candidates, n_in, replace=False)
            humans.activate(chosen)
            self.net_acc[chosen] = 0.0
        self._prev_wealth = humans.wealth.copy()
