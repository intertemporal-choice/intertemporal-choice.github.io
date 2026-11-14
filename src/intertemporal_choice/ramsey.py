"""The Ramsey/Cass-Koopmans model: the notebook's figures, kept out of its notebook.

The notebook, content/growth/RamseyCassKoopmans/RamseyCassKoopmans.ipynb, shows the economics:
the loci where consumption and capital per efficiency unit stop changing, the saddle path found
by time elimination, and the paths that start off it. It computes them with its own functions and
passes the numbers here. This module only draws, in the letters the book prints: k and c per
efficiency unit, the steady state ǩ, the golden rule k̿, productivity growth φ.

`python -m intertemporal_choice --self-test` runs `self_test`.
"""

import numpy as np

# Italic text, not mathtext: mathtext sets the check of \check{k} beside the k, not above it.
STEADY = "\u01e9"        # ǩ
GOLDEN = "k\u033f"       # k̿, k with a double bar


def _axes(ax, k_max, c_max):
    ax.set_xlim(0, k_max)
    ax.set_ylim(0, c_max)
    ax.set_xticks([])
    ax.set_yticks([])
    ax.set_xlabel(r"$k$", loc="right")
    ax.set_ylabel(r"$c$", loc="top", rotation=0)


def _tick(ax, k, label):
    """A label under the horizontal axis at k, where a number would be."""
    ax.annotate(label, (k, 0), xytext=(0, -4), textcoords="offset points", ha="center", va="top",
                xycoords=("data", "axes fraction"), fontsize=12, fontstyle="italic")


def draw_loci(ax, k, loci, golden=None, c_max=None):
    """The kdot = 0 curve and the cdot/c = 0 line of each economy in `loci`, a dict from its label
    (such as r"$\\phi$ low") to (c on the kdot = 0 curve at each k, its steady state ǩ). The first
    economy is drawn solid and labeled to the right of its lines, the others dashed and labeled to
    the left, so that no label crosses a line. The first economy's steady state is marked ǩ on the
    axis; `golden`, if given, is its golden rule k̿, marked on the axis with a dotted line up to the
    top of its curve."""
    k_max = k[-1]
    c_max = c_max or 1.25 * max(np.max(c) for c, _ in loci.values())
    for index, (label, (c, steady)) in enumerate(loci.items()):
        first = index == 0
        style = "-" if first else "--"
        ax.plot(k, c, color="C0", linestyle=style)
        ax.annotate(rf"$\dot{{k}}=0$, {label}", (k_max, c[-1]), xytext=(-4, 5 if first else -6),
                    textcoords="offset points", ha="right", va="bottom" if first else "top", color="C0")
        ax.axvline(steady, color="C1", linestyle=style)
        ax.annotate(rf"$\dot{{c}}/c=0$, {label}", (steady, 0.08), xycoords=("data", "axes fraction"),
                    xytext=(4 if first else -4, 0), textcoords="offset points", ha="left" if first else "right",
                    color="C1")
    first_c, first_steady = next(iter(loci.values()))
    _tick(ax, first_steady, STEADY)
    if golden is not None:
        top = np.interp(golden, k, first_c)
        ax.plot([golden, golden], [0, top], color="0.4", linestyle=":", linewidth=1.2)
        _tick(ax, golden, GOLDEN)
    _axes(ax, k_max, c_max)


def _arrow(ax, k, c, color, at=-1):
    """An arrowhead on the path (k, c), pointing along it at index `at`."""
    ax.annotate("", (k[at], c[at]), xytext=(k[at - 3], c[at - 3]),
                arrowprops={"arrowstyle": "-|>", "color": color, "lw": 1.8, "mutation_scale": 14})


def draw_saddle(ax, k, c_kdot0, steady, saddle, paths, c_max=None):
    """The phase diagram: the kdot = 0 curve (c_kdot0 at each k), the cdot/c = 0 line at the steady
    state, the saddle path `saddle` = (k, c) with arrows toward the steady state, and `paths`, each
    a path (k, c) in time order, with an arrow at its end."""
    k_max = k[-1]
    c_max = c_max or 1.6 * np.max(c_kdot0)
    ax.plot(k, c_kdot0, color="C0")
    ax.annotate(r"$\dot{k}=0$", (k_max, c_kdot0[-1]), xytext=(-4, -6), textcoords="offset points",
                ha="right", va="top", color="C0")
    ax.axvline(steady[0], color="C1")
    ax.annotate(r"$\dot{c}/c=0$", (steady[0], 0.97), xycoords=("data", "axes fraction"), xytext=(4, 0),
                textcoords="offset points", ha="left", va="top", color="C1")
    k_s, c_s = saddle
    ax.plot(k_s, c_s, color="black", linewidth=2.2)
    ax.annotate("saddle path", (k_s[-1], c_s[-1]), xytext=(-4, 4), textcoords="offset points", ha="right",
                va="bottom")
    for side in (k_s < steady[0], k_s > steady[0]):  # an arrow on each branch, pointing at the steady state
        kb, cb = k_s[side], c_s[side]
        order = np.argsort(np.abs(kb - steady[0]))[::-1]  # far to near
        middle = len(order) // 2
        _arrow(ax, kb[order], cb[order], "black", at=middle)
    ax.plot(*steady, "o", color="black", markersize=5)
    for index, (k_p, c_p) in enumerate(paths):
        color = f"C{index + 2}"
        ax.plot(k_p, c_p, color=color, linewidth=1.4)
        _arrow(ax, k_p, c_p, color)
    _tick(ax, steady[0], STEADY)
    _axes(ax, k_max, c_max)


def self_test() -> list[str]:
    import matplotlib.pyplot as plt

    failures = []
    k = np.linspace(0.01, 6, 50)
    curve = lambda g: k**0.3 - (0.09 + g) * k
    fig, ax = plt.subplots()
    draw_loci(ax, k, {"low": (curve(0.03), 2.25), "high": (curve(0.06), 1.46)}, golden=3.7)
    if len(ax.get_lines()) != 5 or ax.get_xlim() != (0.0, 6.0):  # two curves, two lines, the golden rule
        failures.append("ramsey: draw_loci does not draw each economy's two loci and the golden rule")
    plt.close(fig)

    fig, ax = plt.subplots()
    k_s = np.linspace(0.05, 5, 40)
    paths = [(np.linspace(0.5, 0.05, 20), np.linspace(0.6, 1.2, 20)), (np.linspace(0.5, 5, 20), np.linspace(0.4, 0.8, 20))]
    draw_saddle(ax, k, curve(0.03), (2.25, 1.0), (k_s, 0.45 * k_s**0.5), paths)
    if len(ax.get_lines()) != 6:  # the kdot = 0 curve, the cdot = 0 line, the saddle path, its point, two paths
        failures.append("ramsey: draw_saddle does not draw the loci, the saddle path and each path")
    arrows = [a for a in ax.texts if a.arrow_patch is not None]
    if len(arrows) != 4:
        failures.append("ramsey: draw_saddle does not put an arrow on each branch of the saddle path and each path")
    plt.close(fig)
    return failures
