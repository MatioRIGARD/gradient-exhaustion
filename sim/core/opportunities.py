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
    """Endogenous value multiplier: m = beta + (1 - beta) * h(D).

    D tracks human disposable income (EMA; in the v1 core the only human
    income channel is capture — DEC-002 binds later channels), normalized by
    its reference level `ref_income` (the full-participation flow). beta is
    the autonomous share of demand; beta = 1 switches the feedback off.

    Response shape h: linear h(D) = D when hill_n <= 0 (legacy, no
    bistability per the preliminary E3 finding), else a normalized Hill
    sigmoid h(D) = D^n (1 + K^n) / (D^n + K^n) with h(0)=0, h(1)=1 — the
    steepness n is the "demand stickiness/nonlinearity" the ratchet requires.
    """

    beta: float
    ref_income: float
    smoothing: float  # EMA rate per unit time
    level: float = 1.0  # normalized D, starts at full participation
    hill_n: float = 0.0  # <= 0: linear response
    hill_k: float = 0.5  # half-response point of the sigmoid

    def update(self, human_income_flow: float, dt: float) -> None:
        target = 0.0 if self.ref_income <= 0 else human_income_flow / self.ref_income
        a = min(1.0, self.smoothing * dt)
        self.level += a * (min(target, 1.0) - self.level)

    @property
    def multiplier(self) -> float:
        d = max(self.level, 0.0)
        if self.hill_n <= 0:
            h = d
        else:
            dn, kn = d**self.hill_n, self.hill_k**self.hill_n
            h = dn * (1.0 + kn) / (dn + kn)
        return self.beta + (1.0 - self.beta) * h
