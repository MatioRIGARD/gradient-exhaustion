"""Common decision interface for the three interchangeable rationality levels.

A decision rule governs *voluntary* human entry/exit each step; the shared
mechanics (participation-cost drain and bankruptcy backstop) live in
HumanPopulation.tick and apply identically under every rule. Selectable by
config (`human_decision`) so every headline figure can be checked against all
three levels (robustness). See docs/simulation-architecture.md §2.6.
"""

from __future__ import annotations

from typing import Protocol

import numpy as np

from sim.core.agents import HumanPopulation


class DecisionRule(Protocol):
    def apply(self, humans: HumanPopulation, rng: np.random.Generator, dt: float) -> None:
        """Perform voluntary entries/exits for this step."""
        ...


def make_rule(name: str, n_pool: int, params: dict) -> DecisionRule:
    from sim.strategies.best_response import BestResponseRule
    from sim.strategies.learning import LearningRule
    from sim.strategies.replicator import ReplicatorRule

    rules = {
        "replicator": lambda: ReplicatorRule(),
        "best_response": lambda: BestResponseRule(deadband=params.get("deadband", 0.05)),
        "learning": lambda: LearningRule(
            n_pool=n_pool,
            review_rate=params.get("review_rate", 0.05),
            probe_rate=params.get("probe_rate", 0.02),
        ),
    }
    if name not in rules:
        raise ValueError(f"unknown decision rule: {name!r}")
    return rules[name]()
