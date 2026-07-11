# Gradient Exhaustion

**A multi-agent model of human economic disempowerment.**

Recent work ("Gradual Disempowerment", Kulveit et al. 2025; "The Intelligence Curse", Drago & Laine 2025) argues qualitatively that incremental AI deployment may push humans out of the economic loop — not through takeover, but because the systems society relies on stop depending on human participation. This project builds the missing formal layer: a minimal analytic model and an agent-based simulation of **asymmetric gradient exhaustion** — the hypothesis that AI optimizers capture every profit opportunity ("gradient") faster than humans can, driving human market income toward zero even while total system profit persists.

We study the dynamics of a **human economic participation index (π)** and look for:
- **critical thresholds** (does π collapse abruptly past a level of AI penetration?),
- **hysteresis** (is there a point of no return?),
- **the role of competition** (is a single benevolent operator enough to produce exclusion?),
- **early-warning signatures** observable before the critical region,
- **falsifiable predictions** on the emerging agentic economy.

## Status

Early stage — research program and architecture defined, model formalization in progress. See `PLAN.md` (roadmap, in French), `docs/` (research program, simulation architecture, background), `paper/paper.md` (article skeleton).

## Principles

- **No baked-in conclusion**: human and AI agents differ only by parameter values, never by special rules; non-tautology checks live in the test suite.
- **Validation before production**: the simulator must reproduce the analytic solution in degenerate cases before any experiment counts.
- **Full reproducibility**: every reported number regenerates from a single documented command; experiment configs are versioned.

## Setup

Tooling is driven by [uv](https://docs.astral.sh/uv/) (no system `pip` needed); it
provisions Python 3.12 and all dependencies on a clean machine.

```bash
make setup    # uv sync: create .venv, install deps + the sim package (writes uv.lock)
make test     # pytest (sim/tests) -- passes with zero tests during scaffolding
make lint     # ruff check
make format   # ruff format
make ci       # local gate: lint + test (run before committing)
make clean    # remove .venv and caches
```

## Layout

```
sim/core/        opportunities, agent populations, capture race, main dynamics
sim/strategies/  three interchangeable rationality levels + richer strategies
sim/metrics/     pi (market/total), Gini, niche lifetimes, early-warning indicators
sim/experiments/ configs (one YAML per experiment) + multi-seed runner
sim/analysis/    phase-boundary / hysteresis detection, publication figures
sim/tests/       V1 analytic, V2 sanity (non-tautology), V3 invariance
```

See `docs/simulation-architecture.md` for the rationale behind each module.

## License

MIT.
