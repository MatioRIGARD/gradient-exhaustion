"""The capture race: detection and allocation of opportunity value.

Per step of length dt, each live opportunity runs one memoryless race between
total eligible human intensity, total eligible AI intensity, and expiry (rate
theta). Sampling the race outcome exactly (P(no event) = exp(-total*dt), winner
proportional to rates) keeps the discretization unbiased, which is what makes the
V1 analytic anchor achievable at finite dt. The degenerate two-population case is
the Grossman-Stiglitz transposition of model-notes.md §2.
"""

from __future__ import annotations

from dataclasses import dataclass, field

import numpy as np

from sim.core.agents import AIPopulation, HumanPopulation
from sim.core.opportunities import OpportunityPool

HUMAN, AI, EXPIRE = 0, 1, 2


@dataclass
class RaceOutcome:
    """Aggregate result of one step's races."""

    human_income: float = 0.0
    ai_income: float = 0.0
    ai_income_per_operator: np.ndarray = field(default_factory=lambda: np.zeros(0))
    gone: np.ndarray = field(default_factory=lambda: np.zeros(0, dtype=bool))
    n_human_captures: int = 0
    n_ai_captures: int = 0


def run_races(
    opps: OpportunityPool,
    humans: HumanPopulation,
    ais: AIPopulation,
    theta: float,
    dt: float,
    rng: np.random.Generator,
) -> RaceOutcome:
    out = RaceOutcome(
        ai_income_per_operator=np.zeros(ais.lam.size),
        gone=np.zeros(opps.n, dtype=bool),
    )
    if opps.n == 0:
        return out

    lam_h = humans.intensity_for(opps.difficulty)
    lam_a = ais.intensity_for(opps.difficulty)
    total = lam_h + lam_a + theta

    u_event = rng.random(opps.n)
    happened = u_event < 1.0 - np.exp(-total * dt)
    if not happened.any():
        return out

    idx = np.flatnonzero(happened)
    probs = np.column_stack([lam_h[idx], lam_a[idx], np.full(idx.size, theta)])
    probs /= probs.sum(axis=1, keepdims=True)
    cum = np.cumsum(probs, axis=1)
    kind = (rng.random(idx.size)[:, None] < cum).argmax(axis=1)

    out.gone[idx] = True
    for i, k in zip(idx, kind, strict=True):
        v, diff = float(opps.value[i]), float(opps.difficulty[i])
        if k == HUMAN:
            humans.credit(humans.pick_winner(diff, rng), v)
            out.human_income += v
            out.n_human_captures += 1
        elif k == AI:
            out.ai_income_per_operator[ais.pick_winner(diff, rng)] += v
            out.ai_income += v
            out.n_ai_captures += 1
    return out
