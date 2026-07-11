.PHONY: setup test lint format ci clean

# Tooling is driven by uv (https://docs.astral.sh/uv/): no system pip required.
# `uv sync` creates .venv, installs deps + the sim package, and writes uv.lock.
# `uv run` executes a command inside that environment (auto-syncing if needed).

setup:
	uv sync --extra dev

# pytest exits 5 when it collects zero tests; treat that as success while the
# suite is still being scaffolded (V1-V3 land in T3.4-T3.6).
test:
	@uv run pytest; code=$$?; if [ $$code -eq 5 ]; then echo "No tests collected (scaffolding stage)."; exit 0; fi; exit $$code

lint:
	uv run ruff check .

format:
	uv run ruff format .

# Local CI gate: run this before committing.
ci: lint test

clean:
	rm -rf .venv .pytest_cache .ruff_cache
	find . -type d -name __pycache__ -prune -exec rm -rf {} +
