"""The capital-market imperfections chapter's figure, kept out of its notebook.

The notebook, content/investment/DynanImperfCapMkts/DynanImperfCapMkts.ipynb, reads Moody's yields
on seasoned Baa and Aaa corporate bonds and the NBER's recession dates, and computes the spread
between the two yields, a measure of the premium the market charges riskier borrowers. This module
only draws.

`python -m intertemporal_choice --self-test` runs `self_test`.
"""

import numpy as np


def draw_spread(ax, spread, recessions, marks=()):
    """The spread, in percentage points, by month, with recessions shaded; `marks`, dates, are
    labeled with the spread's value then."""
    shown = recessions[recessions.index >= spread.index[0]]
    starts = shown.index[(shown == 1) & (shown.shift(1, fill_value=0) == 0)]
    ends = shown.index[(shown == 1) & (shown.shift(-1, fill_value=0) == 0)]
    for a, b in zip(starts, ends):
        ax.axvspan(a, b, color="0.88", lw=0)
    ax.plot(spread.index, spread.values, color="black", lw=0.9)
    for date in marks:
        value = float(spread.loc[date])
        ax.annotate(f"{date:%b %Y}: {value:.1f}", (date, value), xytext=(6, 2), textcoords="offset points", fontsize=8)
    ax.set_xlim(spread.index[0], spread.index[-1])
    ax.set_ylim(0, 1.08 * float(np.max(spread.values)))
    ax.set_ylabel("Baa − Aaa", loc="top", rotation=0)


def self_test() -> list[str]:
    import matplotlib.pyplot as plt
    import pandas as pd

    failures = []
    months = pd.date_range("1990-01-01", periods=60, freq="MS")
    spread = pd.Series(np.linspace(1, 3, 60), index=months)
    recessions = pd.Series((np.arange(60) % 20 < 5).astype(int), index=months)
    fig, ax = plt.subplots()
    try:
        draw_spread(ax, spread, recessions, marks=[months[30]])
        if len(ax.patches) != 3:
            failures.append(f"spreads: {len(ax.patches)} recessions shaded, not 3")
    except Exception as e:  # noqa: BLE001
        failures.append(f"spreads: draw_spread failed: {e!r}")
    plt.close(fig)
    return failures
