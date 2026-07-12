"""Myopic best response: bang-bang reaction to the market-thickness signal.

Each step, agents act on the *sign* of the expected-profit gap (with a small
deadband against chatter): full-rate entry while participation looks profitable,
full-rate voluntary exit while it does not. The saturated limit of the
replicator rule — same information, cruder reaction.
"""

from __future__ import annotations

import numpy as np

from sim.core.agents import HumanPopulation


class BestResponseRule:
    def __init__(self, deadband: float = 0.05):
        self.deadband = deadband

    def apply(self, humans: HumanPopulation, rng: np.random.Generator, dt: float) -> None:
        mean_cost = float(humans.cost.mean())
        gap = (humans.income_ema - mean_cost) / mean_cost
        if gap < -self.deadband:
            incumbents = np.flatnonzero(humans.active)
            n_out = min(incumbents.size, rng.poisson(humans.entry_rate * dt))
            if n_out > 0:
                humans.active[rng.choice(incumbents, n_out, replace=False)] = False
        rate_in = humans.explore_rate + (humans.entry_rate if gap > self.deadband else 0.0)
        candidates = np.flatnonzero(~humans.active)
        n_in = min(candidates.size, rng.poisson(rate_in * dt))
        if n_in > 0:
            humans.activate(rng.choice(candidates, n_in, replace=False))
