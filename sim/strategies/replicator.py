"""Replicator-style rule: flow rates proportional to the signed payoff gap.

This is the v1 default (the rule the V1 analytic anchor was validated with):
entries at explore + entry_rate * gap when the market-thickness signal exceeds
the participation cost, voluntary exits at the same rate on the downside —
the symmetric response that avoids noise-rectification bias.
"""

from __future__ import annotations

import numpy as np

from sim.core.agents import HumanPopulation


class ReplicatorRule:
    def apply(self, humans: HumanPopulation, rng: np.random.Generator, dt: float) -> None:
        mean_cost = float(humans.cost.mean())
        gap = (humans.income_ema - mean_cost) / mean_cost
        if gap < 0.0:
            incumbents = np.flatnonzero(humans.active)
            n_out = min(incumbents.size, rng.poisson(humans.entry_rate * min(1.0, -gap) * dt))
            if n_out > 0:
                humans.active[rng.choice(incumbents, n_out, replace=False)] = False
        rate_in = humans.explore_rate + humans.entry_rate * min(1.0, max(0.0, gap))
        candidates = np.flatnonzero(~humans.active)
        n_in = min(candidates.size, rng.poisson(rate_in * dt))
        if n_in > 0:
            humans.activate(rng.choice(candidates, n_in, replace=False))
