"""The RCK model with government: the notebook's figures, kept out of its notebook.

The notebook, content/growth/RCKWithGov/RCKWithGov.ipynb, computes the economics: the loci where
consumption and capital stop changing with low and with high government spending, the original
saddle path, and the paths after a permanent and after a temporary increase in spending. It passes
the numbers here. This module only draws, in the letters the book prints: k and c per person, the
steady state k̄, government spending X, the interest rate r.

`python -m intertemporal_choice --self-test` runs `self_test`.
"""

import numpy as np

from intertemporal_choice.notation import tex

# The two experiments: the permanent increase purple, the temporary one brown, as the RCK figures color the
# paths off the saddle path (not red and green, which color-blind readers confuse).
PERMANENT, TEMPORARY = "C4", "C5"


def _arrow(ax, x, y, color, at):
    """An arrowhead on the path (x, y), pointing along it at index `at`."""
    ax.annotate("", (x[at], y[at]), xytext=(x[at - 3], y[at - 3]),
                arrowprops={"arrowstyle": "-|>", "color": color, "lw": 1.8, "mutation_scale": 14})


def _point(ax, x, y, label, offset):
    ax.plot(x, y, "o", color="black", markersize=4, zorder=5)
    ax.annotate(label, (x, y), xytext=offset, textcoords="offset points", fontsize=12)


def draw_phase(ax, k, kdot0_low, kdot0_high, steady, saddle, temporary, returning, c_range):
    """The phase diagram of both experiments, zoomed on the steady state.

    k: a grid of capital; kdot0_low and kdot0_high: consumption on the kdot = 0 locus at each k with
    low and with high spending; steady: (k̄, c̄ with low spending, c̄ with high spending); saddle: the
    original saddle path (k, c); temporary: the path (k, c) while spending is high, from its start A
    to its end B; returning: the path (k, c) from B back toward the steady state E along the original
    saddle path; c_range: the vertical axis limits.

    The permanent increase drops consumption from E to E' with capital unchanged (purple). The
    temporary increase drops it from E to A, then capital runs down to B while spending is high, and
    the economy returns along the saddle path (brown). Each is labeled with its experiment's name."""
    k_bar, c_low, c_high = steady
    spending = tex(r"$\GovSpend$")
    ax.plot(k, kdot0_low, color="C0")
    ax.plot(k, kdot0_high, color="C0", linestyle="--")
    for c, words, va, dy in ((kdot0_low, "low", "bottom", 5), (kdot0_high, "high", "top", -6)):
        ax.annotate(tex(r"$\dot{\kap}=0$") + f", {spending} {words}", (k[0], c[0]), xytext=(4, dy),
                    textcoords="offset points", ha="left", va=va, color="C0")
    ax.axvline(k_bar, color="C1")
    ax.annotate(tex(r"$\dot{\cNrm}=0$"), (k_bar, 0.97), xycoords=("data", "axes fraction"), xytext=(4, 0),
                textcoords="offset points", ha="left", va="top", color="C1")
    ax.plot(*saddle, color="black", linewidth=2.2)
    ax.annotate("saddle path", (saddle[0][-1], saddle[1][-1]), xytext=(-4, 8), textcoords="offset points",
                ha="right", va="bottom")
    # The permanent increase: straight down from E to E'.
    ax.annotate("", (k_bar, c_high), xytext=(k_bar, c_low),
                arrowprops={"arrowstyle": "-|>", "color": PERMANENT, "lw": 1.8, "mutation_scale": 14,
                            "shrinkA": 0, "shrinkB": 2})
    # The temporary increase: E to A (a jump), A to B (capital runs down), B back to E along the saddle path.
    k_t, c_t = temporary
    k_r, c_r = returning
    ax.plot([k_bar, k_bar], [c_low, c_t[0]], color=TEMPORARY, linestyle=":", linewidth=1.6)
    ax.plot(k_t, c_t, color=TEMPORARY, linewidth=1.6)
    _arrow(ax, k_t, c_t, TEMPORARY, at=len(k_t) // 2)
    ax.plot(k_r, c_r, color=TEMPORARY, linewidth=1.6)
    _arrow(ax, k_r, c_r, TEMPORARY, at=len(k_r) // 3)
    # Which path is which (Chris, in class, 2026-11-17).
    ax.annotate("permanent", (k_bar, (c_low + c_t[0]) / 2), xytext=(6, 0), textcoords="offset points",
                ha="left", va="center", color=PERMANENT)
    mid = len(k_t) // 2
    ax.annotate("temporary", (k_t[mid], c_t[mid]), xytext=(0, -8), textcoords="offset points",
                ha="center", va="top", color=TEMPORARY)
    _point(ax, k_bar, c_low, "E", (-14, 6))
    _point(ax, k_bar, c_high, "E′", (6, -12))
    _point(ax, k_t[0], c_t[0], "A", (6, -6))
    _point(ax, k_t[-1], c_t[-1], "B", (-14, 2))
    ax.set_xlim(k[0], k[-1])
    ax.set_ylim(*c_range)
    ax.set_xticks([])
    ax.set_yticks([])
    ax.set_xlabel(tex(r"$\kap$"), loc="right")
    ax.set_ylabel(tex(r"$\cNrm$"), loc="top", rotation=0)


def draw_paths(axes, t, temporary, permanent, t_end):
    """Consumption, capital and the interest rate over time, in three panels from top to bottom.

    t: dates; temporary and permanent: dicts with the series "c", "k" and "r" at those dates (r in
    percent); t_end: the date the temporary increase ends. The temporary increase is drawn solid
    brown and the permanent one dashed purple; the shaded band marks the dates spending is high in
    the temporary experiment."""
    rows = (("c", tex(r"$\cNrm$")), ("k", tex(r"$\kap$")), ("r", tex(r"$\rfree$") + " (percent)"))
    for ax, (key, label) in zip(axes, rows):
        ax.axvspan(0, t_end, color="0.92", zorder=0)
        ax.plot(t, permanent[key], color=PERMANENT, linestyle="--", linewidth=1.6)
        ax.plot(t, temporary[key], color=TEMPORARY, linewidth=1.8)
        ax.set_ylabel(label, loc="top", rotation=0)
    axes[0].annotate("temporary", (t[-1], temporary["c"][-1]), xytext=(-4, -6), textcoords="offset points",
                     ha="right", va="top", color=TEMPORARY)
    axes[0].annotate("permanent", (t[-1], permanent["c"][-1]), xytext=(-4, 5), textcoords="offset points",
                     ha="right", va="bottom", color=PERMANENT)
    axes[-1].set_xlim(t[0], t[-1])
    axes[-1].set_xlabel("years after the increase", loc="right")


def self_test() -> list[str]:
    import matplotlib.pyplot as plt

    failures = []
    k = np.linspace(3.8, 5.4, 60)
    low, high = k**0.3 - 0.08 * k - 0.32, k**0.3 - 0.08 * k - 0.40
    saddle = (k, 0.2 * k)
    fig, ax = plt.subplots()
    draw_phase(ax, k, low, high, (4.8, 0.90, 0.82), saddle, (np.linspace(4.8, 4.4, 20), np.linspace(0.86, 0.88, 20)),
               (np.linspace(4.4, 4.7, 20), np.linspace(0.88, 0.895, 20)), (0.7, 1.0))
    # the two loci, the cdot = 0 line, the saddle path, the dotted jump to A, the two path pieces, four points
    if len(ax.get_lines()) != 11:
        failures.append("fiscal: draw_phase does not draw both loci, the saddle path, both paths and the four points")
    if {line.get_color() for line in ax.get_lines()} & {"C2", "C3", "tab:green", "tab:red"}:
        failures.append("fiscal: draw_phase draws in red or green")
    plt.close(fig)

    fig, axes = plt.subplots(3, 1, sharex=True)
    t = np.linspace(-5, 30, 50)
    series = {"c": np.ones_like(t), "k": np.ones_like(t), "r": 2 * np.ones_like(t)}
    draw_paths(axes, t, series, series, 10)
    if any(len(ax.get_lines()) != 2 for ax in axes):
        failures.append("fiscal: draw_paths does not draw both experiments in each panel")
    plt.close(fig)
    return failures
