"""Opportunity generation, ageing, and the demand pool.

Opportunities are the "gradients": each carries a value and a difficulty.
Lifetimes are memoryless (expiry rate theta), so ageing needs no per-opportunity
clock: expiry competes as one more exponential in each step's race (capture.py).
The demand pool makes opportunity values endogenous to circulating human income
(model-notes.md §4, assumption A8 in continuous form).
"""

from __future__ import annotations

from dataclasses import dataclass, field

import numpy as np


@dataclass
class OpportunityPool:
    """Active opportunities as parallel arrays."""

    value: np.ndarray = field(default_factory=lambda: np.empty(0))
    difficulty: np.ndarray = field(default_factory=lambda: np.empty(0))

    @property
    def n(self) -> int:
        return self.value.size

    def spawn(
        self,
        rng: np.random.Generator,
        count: int,
        base_value: float,
        value_multiplier: float,
        difficulty_dist: tuple[float, float],
    ) -> None:
        """Add `count` new opportunities.

        Values are base_value * value_multiplier (the demand-side scaling);
        difficulties are uniform over [lo, hi] (degenerate when lo == hi).
        """
        if count <= 0:
            return
        lo, hi = difficulty_dist
        new_v = np.full(count, base_value * value_multiplier)
        new_k = rng.uniform(lo, hi, count) if hi > lo else np.full(count, lo)
        self.value = np.concatenate([self.value, new_v])
        self.difficulty = np.concatenate([self.difficulty, new_k])

    def remove(self, gone: np.ndarray) -> None:
        """Drop opportunities flagged in the boolean mask `gone`."""
        keep = ~gone
        self.value = self.value[keep]
        self.difficulty = self.difficulty[keep]


@dataclass
class DemandPool:
    """Endogenous value multiplier: m = beta + (1 - beta) * D.

    D tracks human earned income (EMA), normalized by its reference level
    `ref_income` (the full-participation flow). beta is the autonomous share
    of demand; beta = 1 switches the feedback off entirely.
    """

    beta: float
    ref_income: float
    smoothing: float  # EMA rate per unit time
    level: float = 1.0  # normalized D, starts at full participation

    def update(self, human_income_flow: float, dt: float) -> None:
        target = 0.0 if self.ref_income <= 0 else human_income_flow / self.ref_income
        a = min(1.0, self.smoothing * dt)
        self.level += a * (min(target, 1.0) - self.level)

    @property
    def multiplier(self) -> float:
        return self.beta + (1.0 - self.beta) * self.level
