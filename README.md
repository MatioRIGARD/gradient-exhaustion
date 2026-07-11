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

```bash
make setup   # venv + dependencies
make test    # pytest
make lint    # ruff
```

## License

MIT.
