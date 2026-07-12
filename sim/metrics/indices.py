"""Metrics: pi (market/total), early-warning indicators, stationary summaries.

pi is the human economic participation index of docs/pi-definition.md. In the
v1 core the only earned channel is capture (no labour channel, no transfers
yet — those arrive with strategies, T3.8), so pi_market = kappa_h / (kappa_h +
kappa_a) and pi_total = pi_market. Early-warning indicators (rolling variance,
lag-1 autocorrelation) feed experiment E6.
"""

from __future__ import annotations

import numpy as np


def pi_market(kappa_h: np.ndarray, kappa_a: np.ndarray) -> np.ndarray:
    """Human share of earned flow; NaN where nothing is earned."""
    total = kappa_h + kappa_a
    out = np.full_like(total, np.nan, dtype=float)
    np.divide(kappa_h, total, out=out, where=total > 0)
    return out


def pi_total(kappa_h: np.ndarray, kappa_a: np.ndarray, t_h: np.ndarray) -> np.ndarray:
    """Share of the pre-tax earned flow that sustains humans (earned + transfers).

    Denominator = kappa_h + kappa_a + t_h (AI income is recorded net of tax, so
    adding the transfer restores the pre-tax earned flow). pi_total - pi_market
    is the perfusion gap of docs/pi-definition.md."""
    total = kappa_h + kappa_a + t_h
    out = np.full_like(total, np.nan, dtype=float)
    np.divide(kappa_h + t_h, total, out=out, where=total > 0)
    return out


def stationary_mean(t: np.ndarray, series: np.ndarray, discard_frac: float = 0.5) -> float:
    """Mean of `series` after discarding the initial `discard_frac` of the run."""
    cut = t >= t[0] + discard_frac * (t[-1] - t[0])
    vals = series[cut]
    vals = vals[~np.isnan(vals)]
    return float(vals.mean()) if vals.size else float("nan")


def rolling_variance(series: np.ndarray, window: int) -> np.ndarray:
    """Rolling variance (same length; NaN-padded head)."""
    out = np.full(series.size, np.nan)
    for i in range(window, series.size + 1):
        out[i - 1] = np.var(series[i - window : i])
    return out


def rolling_lag1_autocorr(series: np.ndarray, window: int) -> np.ndarray:
    """Rolling lag-1 autocorrelation (same length; NaN-padded head)."""
    out = np.full(series.size, np.nan)
    for i in range(window, series.size + 1):
        w = series[i - window : i]
        a, b = w[:-1], w[1:]
        sa, sb = a.std(), b.std()
        out[i - 1] = float(np.corrcoef(a, b)[0, 1]) if sa > 0 and sb > 0 else np.nan
    return out
