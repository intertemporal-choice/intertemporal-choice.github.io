"""The Lucas Asset Pricing Model: the notebook's figures, kept out of its notebook.

The notebook, content/asset_pricing/LucasAssetPrice/LucasAssetPrice.ipynb, shows the economics: the
exact series for the price-dividend ratio, the numerical solution of the pricing equation, the
riskless rate, and a small tree whose dividends move partly with the economy's. It computes the
numbers with its own functions and passes them here. This module only draws.

`python -m intertemporal_choice --self-test` runs `self_test`.
"""

import numpy as np

# The persistence figure's horizontal axis: tau = 1 - 10**(-k), so k = 0, 1, 2, 3 are tau = 0, 0.9,
# 0.99 and 0.999, the climb the chapter describes.
TAU_TICKS = {0: "0", 1: "0.9", 2: "0.99", 3: "0.999"}


def tau_from_k(k):
    """The persistence tau at each point of the persistence figure's horizontal axis."""
    return 1 - 10.0 ** (-np.asarray(k, float))


def draw_persistence(ax, k, ratios, random_walk):
    """Price-dividend ratio against persistence, one line per dividend level, with the random
    walk's ratio, the limit as tau goes to one, as a dashed line.

    `ratios` maps a label (such as "d = 1") to the ratios at tau_from_k(k)."""
    for label, ratio in ratios.items():
        ax.plot(k, ratio, label=label)
    ax.axhline(random_walk, color="black", linestyle="--", linewidth=0.8, label="random walk")
    ax.set_xticks(list(TAU_TICKS), list(TAU_TICKS.values()))
    ax.set_xlim(k[0], k[-1])
    ax.set_xlabel(r"persistence $\tau$", loc="right")
    ax.set_ylabel(r"$\mathsf{P}/d$", loc="top", rotation=0)
    ax.legend(frameon=False)


def draw_against_rho(ax, rho, lines, ylabel=r"$\mathsf{P}/d$", log=False):
    """One line per economy or asset against relative risk aversion. `lines` maps a label to its
    values at `rho`."""
    for label, values in lines.items():
        ax.plot(rho, values, label=label)
    if log:
        from matplotlib.ticker import NullFormatter

        ax.set_yscale("log")
        low = min(min(v) for v in lines.values())
        high = max(max(v) for v in lines.values())
        ticks = [v for v in (2, 5, 10, 15, 25, 50, 100, 200, 500) if 0.95 * low <= v <= 1.05 * high]
        ax.set_yticks(ticks, [f"{v:g}" for v in ticks])  # 25, 50, 100, not 2.5 x 10^1
        ax.yaxis.set_minor_formatter(NullFormatter())
    ax.set_xlim(rho[0], rho[-1])
    ax.set_xlabel(r"$\rho$", loc="right")
    ax.set_ylabel(ylabel, loc="top", rotation=0)
    ax.legend(frameon=False)


def draw_small_tree(ax, risk, lines, xlabel, from_zero=True):
    """The small tree's price-dividend ratio as one kind of its risk grows. `risk` is the standard
    deviation of that risk; `lines` maps a label to the ratios at each value of it. The axis starts
    at zero unless `from_zero` is False, for a figure whose point is the gap between the lines."""
    for label, values in lines.items():
        ax.plot(risk, values, label=label)
    ax.set_xlim(risk[0], risk[-1])
    if from_zero:  # a few percent looks like a few percent
        ax.set_ylim(0, 1.1 * max(max(v) for v in lines.values()))
    ax.set_xlabel(xlabel, loc="right")
    ax.set_ylabel(r"$\mathsf{P}/d$", loc="top", rotation=0)
    ax.legend(frameon=False)


def self_test() -> list[str]:
    import matplotlib.pyplot as plt

    failures = []
    if not np.allclose(tau_from_k([0, 1, 2, 3]), [0, 0.9, 0.99, 0.999]):
        failures.append("lucas: the persistence axis does not put tau = 0, 0.9, 0.99, 0.999 at 0, 1, 2, 3")

    k = np.linspace(0, 3, 7)
    fig, ax = plt.subplots()
    draw_persistence(ax, k, {"d = 1": 25 + k, "d = 2": 100 - k}, 108)
    if len(ax.get_lines()) != 3 or ax.get_xlim() != (0.0, 3.0):
        failures.append("lucas: draw_persistence does not draw two ratios and the random walk on tau's axis")
    plt.close(fig)

    rho = np.linspace(1, 3, 5)
    fig, ax = plt.subplots()
    draw_against_rho(ax, rho, {"a": rho, "b": 2 * rho}, log=True)
    if len(ax.get_lines()) != 2 or ax.get_yscale() != "log":
        failures.append("lucas: draw_against_rho does not draw each line on a log scale when asked")
    plt.close(fig)

    fig, ax = plt.subplots()
    draw_small_tree(ax, np.linspace(0, 0.1, 3), {"own": [1, 1, 1], "systematic": [1, 0.9, 0.8]}, "risk")
    if len(ax.get_lines()) != 2 or ax.get_ylim()[0] != 0:
        failures.append("lucas: draw_small_tree does not draw one line per kind of risk, from zero")
    plt.close(fig)
    fig, ax = plt.subplots()
    draw_small_tree(ax, np.linspace(0, 0.1, 3), {"own": [12, 12, 12], "systematic": [12, 11.8, 11.6]}, "risk", from_zero=False)
    if ax.get_ylim()[0] <= 0:
        failures.append("lucas: draw_small_tree starts at zero when told not to")
    plt.close(fig)
    return failures
