"""Opportunity generation, ageing, and the demand pool.

Opportunities are the "gradients": each carries a value, a complexity, a required
detection latency, and a lifetime. A fraction is regenerated endogenously by the
agents themselves (Schumpeterian regeneration). See docs/simulation-architecture.md
§2.1 and §2.3. Implemented in T3.1.
"""
