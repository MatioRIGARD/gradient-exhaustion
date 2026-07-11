"""Metrics: pi (market/total), Gini, niche lifetimes, early-warning indicators.

pi is the human economic participation index (capture + labour + transfers, with
transfers counted separately: pi_market vs pi_total). Early-warning indicators:
rolling variance, lag-1 autocorrelation, skewness. Implemented exactly as defined
in docs/pi-definition.md (T1.1). See §2.5. Implemented in T3.9.
"""
