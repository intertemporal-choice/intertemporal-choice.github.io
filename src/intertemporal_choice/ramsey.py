"""The Ramsey/Cass-Koopmans model: the notebook's figures, kept out of its notebook.

The notebook, content/growth/RamseyCassKoopmans/RamseyCassKoopmans.ipynb, shows the economics:
the loci where consumption and capital per efficiency unit stop changing, the saddle path found
by time elimination, and the paths that start off it. It computes them with its own functions and
passes the numbers here. This module only draws, in the letters the book prints: k and c per
efficiency unit, the steady state k̄, the golden rule k̿, productivity growth g.

`python -m intertemporal_choice --self-test` runs `self_test`.
"""

import numpy as np

from intertemporal_choice.notation import tex

# Labels are written with the book's macros and spelled out by notation.tex, so the figures print
# whatever the book prints: the steady state is the registry's \Steady, a bar. The golden rule stays
# Unicode, in italic text, as the figures have printed it.
STEADY = tex(r"$\Steady{\kNrm}$")   # k̄
GOLDEN = "k\u033f"                 # k̿, k with a double bar


def _axes(ax, k_max, c_max):
    ax.set_xlim(0, k_max)
    ax.set_ylim(0, c_max)
    ax.set_xticks([])
    ax.set_yticks([])
    ax.set_xlabel(tex(r"$\kNrm$"), loc="right")
    ax.set_ylabel(tex(r"$\cNrm$"), loc="top", rotation=0)


def _tick(ax, k, label):
    """A label under the horizontal axis at k, where a number would be."""
    ax.annotate(label, (k, 0), xytext=(0, -4), textcoords="offset points", ha="center", va="top",
                xycoords=("data", "axes fraction"), fontsize=12, fontstyle="italic")


def draw_loci(ax, k, loci, golden=None, c_max=None):
    """The kdot = 0 curve and the cdot/c = 0 line of each economy in `loci`, a dict from its label
    (such as tex(r"$\\ptyGroRte$ low")) to (c on the kdot = 0 curve at each k, its steady state k̄). The first
    economy is drawn solid and labeled to the right of its lines, the others dashed and labeled to
    the left, so that no label crosses a line. The first economy's steady state is marked k̄ on the
    axis; `golden`, if given, is its golden rule k̿, marked on the axis with a dotted line up to the
    top of its curve."""
    k_max = k[-1]
    c_max = c_max or 1.25 * max(np.max(c) for c, _ in loci.values())
    for index, (label, (c, steady)) in enumerate(loci.items()):
        first = index == 0
        style = "-" if first else "--"
        ax.plot(k, c, color="C0", linestyle=style)
        ax.annotate(tex(r"$\dot{\kNrm}=0$") + f", {label}", (k_max, c[-1]), xytext=(-4, 5 if first else -6),
                    textcoords="offset points", ha="right", va="bottom" if first else "top", color="C0")
        ax.axvline(steady, color="C1", linestyle=style)
        ax.annotate(tex(r"$\dot{\cNrm}/\cNrm=0$") + f", {label}", (steady, 0.08), xycoords=("data", "axes fraction"),
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


# The arrows of motion: light, so the paths stay readable.
MOTION = {"color": "0.55", "lw": 1.0, "mutation_scale": 9}


def _motion(ax, k, c_kdot0, steady, saddle, k_max, c_max):
    """The direction of motion in each of the four regions the loci make, as a pair of arrows from a point
    in the region: one horizontal (kdot's sign: right below the kdot = 0 curve, left above it) and one
    vertical (cdot's sign: up left of the steady state, down right of it). Above the curve, a point lies
    between the curve and the saddle path where the path is above the curve, so as to clear both. Each arrow
    is tagged "motion"."""
    k_bar = steady[0]
    dk, dc = 0.06 * k_max, 0.06 * c_max
    for k_at, up in ((0.5 * k_bar, True), (k_bar + 0.75 * (k_max - k_bar), False)):
        locus = np.interp(k_at, k, c_kdot0)
        on_saddle = np.interp(k_at, *saddle)
        above = (locus + on_saddle) / 2 if on_saddle - locus > 3 * dc else locus + 0.6 * (c_max - locus)
        for c_at, right in ((0.3 * locus, True), (above, False)):
            for to in ((k_at + (dk if right else -dk), c_at), (k_at, c_at + (dc if up else -dc))):
                ax.annotate("", to, xytext=(k_at, c_at), gid="motion",
                            arrowprops={"arrowstyle": "-|>", "shrinkA": 0, "shrinkB": 0, **MOTION})


# The paths off the saddle path: purple and brown, not red and green, which color-blind readers
# confuse, and neither close to the blue kdot = 0 curve or the orange cdot/c = 0 line.
PATH_COLORS = ("C4", "C5")


def draw_saddle(ax, k, c_kdot0, steady, saddle, paths, golden=None, c_max=None, motion=False):
    """The phase diagram: the kdot = 0 curve (c_kdot0 at each k), the cdot/c = 0 line at the steady
    state, the saddle path `saddle` = (k, c) with arrows toward the steady state, and `paths`, each
    a path (k, c) in time order, with an arrow at its end. `golden`, if given, is the golden rule
    k̿, marked on the axis with a dotted line up to the top of the kdot = 0 curve. `motion` adds the
    direction of motion in each of the four regions, as light pairs of arrows."""
    k_max = k[-1]
    c_max = c_max or 1.6 * np.max(c_kdot0)
    if motion:
        _motion(ax, k, c_kdot0, steady, saddle, k_max, c_max)
    ax.plot(k, c_kdot0, color="C0")
    ax.annotate(tex(r"$\dot{\kNrm}=0$"), (k_max, c_kdot0[-1]), xytext=(-4, -6), textcoords="offset points",
                ha="right", va="top", color="C0")
    ax.axvline(steady[0], color="C1")
    ax.annotate(tex(r"$\dot{\cNrm}/\cNrm=0$"), (steady[0], 0.97), xycoords=("data", "axes fraction"), xytext=(4, 0),
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
    if len(paths) > len(PATH_COLORS):
        raise ValueError(f"draw_saddle draws at most {len(PATH_COLORS)} paths off the saddle path, not {len(paths)}")
    for (k_p, c_p), color in zip(paths, PATH_COLORS):
        ax.plot(k_p, c_p, color=color, linewidth=1.4)
        _arrow(ax, k_p, c_p, color)
    _tick(ax, steady[0], STEADY)
    if golden is not None:
        ax.plot([golden, golden], [0, np.interp(golden, k, c_kdot0)], color="0.4", linestyle=":", linewidth=1.2)
        _tick(ax, golden, GOLDEN)
    _axes(ax, k_max, c_max)


def draw_time_pref_fall(ax, k, c_kdot0, old, new, saddle, golden=None, c_range=None):
    """A fall in the time preference rate, around the steady states: the kdot = 0 curve (c_kdot0 at each k; it does
    not involve the time preference rate, so it does not move), the old cdot/c = 0 line at the old steady state
    `old` = (k̄, c̄) dashed, the new one at `new` solid, the new saddle path `saddle` = (k, c) with an arrow on each
    branch toward the new steady state, and the jump: with k fixed, consumption falls from the old steady state onto
    the new saddle path. `golden`, if given, is the golden rule k̿. `c_range` is (c_min, c_max) for the view; the
    saddle path is drawn where it is in view. Returns consumption just after the jump."""
    k_min, k_max = k[0], k[-1]
    c_min, c_max = c_range or (0, 1.6 * np.max(c_kdot0))
    ax.plot(k, c_kdot0, color="C0")
    ax.annotate(tex(r"$\dot{\kNrm}=0$"), (k_max, c_kdot0[-1]), xytext=(-4, -6), textcoords="offset points",
                ha="right", va="top", color="C0")
    ax.axvline(old[0], color="C1", linestyle="--")
    ax.annotate(tex(r"$\dot{\cNrm}/\cNrm=0$") + ", old", (old[0], 0.97), xycoords=("data", "axes fraction"),
                xytext=(-4, 0), textcoords="offset points", ha="right", va="top", color="C1")
    ax.axvline(new[0], color="C1")
    ax.annotate(tex(r"$\dot{\cNrm}/\cNrm=0$") + ", new", (new[0], 0.04), xycoords=("data", "axes fraction"),
                xytext=(4, 0), textcoords="offset points", ha="left", va="bottom", color="C1")
    k_s, c_s = saddle
    inside = (c_s >= c_min) & (c_s <= c_max)  # the part of the saddle path in view
    k_s, c_s = k_s[inside], c_s[inside]
    ax.plot(k_s, c_s, color="black", linewidth=2.2)
    ax.annotate("new saddle path", (k_s[-1], c_s[-1]), xytext=(6, -2), textcoords="offset points", ha="left",
                va="top")
    for side in (k_s < new[0], k_s > new[0]):  # an arrow on each branch, pointing at the new steady state
        kb, cb = k_s[side], c_s[side]
        order = np.argsort(np.abs(kb - new[0]))[::-1]  # far to near
        _arrow(ax, kb[order], cb[order], "black", at=len(order) // 3)
    c_jump = np.interp(old[0], k_s, c_s)
    ax.annotate("", (old[0], c_jump), xytext=old,
                arrowprops={"arrowstyle": "-|>", "color": PATH_COLORS[0], "lw": 1.8, "mutation_scale": 14,
                            "shrinkA": 4, "shrinkB": 0})
    ax.plot(*old, "o", markerfacecolor="white", markeredgecolor="black", markersize=6)
    ax.plot(*new, "o", color="black", markersize=5)
    for k_at, word, side in ((old[0], "old ", "right"), (new[0], "new ", "left")):  # apart, so they don't collide
        # upright, so the word doesn't read as variables; k̄ is math, italic on its own
        ax.annotate(word + STEADY, (k_at, 0), xytext=(0, -4), textcoords="offset points", ha=side, va="top",
                    xycoords=("data", "axes fraction"), fontsize=12)
    if golden is not None:
        ax.plot([golden, golden], [c_min, np.interp(golden, k, c_kdot0)], color="0.4", linestyle=":", linewidth=1.2)
        _tick(ax, golden, GOLDEN)
    _axes(ax, k_max, c_max)
    ax.set_xlim(k_min, k_max)
    ax.set_ylim(c_min, c_max)
    return c_jump


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
    draw_saddle(ax, k, curve(0.03), (2.25, 1.0), (k_s, 0.45 * k_s**0.5), paths, golden=3.7)
    # the kdot = 0 curve, the cdot = 0 line, the saddle path, its point, two paths, the golden rule
    if len(ax.get_lines()) != 7:
        failures.append("ramsey: draw_saddle does not draw the loci, the saddle path, each path and the golden rule")
    if {line.get_color() for line in ax.get_lines()[4:6]} & {"C2", "C3", "tab:green", "tab:red", "#2ca02c", "#d62728"}:
        failures.append("ramsey: draw_saddle draws the paths in red and green")
    arrows = [a for a in ax.texts if a.arrow_patch is not None]
    if len(arrows) != 4:
        failures.append("ramsey: draw_saddle does not put an arrow on each branch of the saddle path and each path")
    plt.close(fig)

    fig, ax = plt.subplots()
    draw_saddle(ax, k, curve(0.03), (2.25, 1.0), (k_s, 0.45 * k_s**0.5), paths, golden=3.7, motion=True)
    motion = [a for a in ax.texts if a.get_gid() == "motion"]
    if len(motion) != 8 or len([a for a in ax.texts if a.arrow_patch is not None]) != 12:
        failures.append("ramsey: draw_saddle(motion=True) does not add a pair of arrows in each of the four regions")
    for a in motion:  # each arrow points the way the loci say: right below kdot = 0, up left of the steady state
        (k0, c0), (k1, c1) = a.xyann, a.xy
        locus = np.interp(k0, k, curve(0.03))
        if k1 != k0 and (k1 > k0) != (c0 < locus):
            failures.append("ramsey: a horizontal arrow of motion points against kdot's sign")
        if c1 != c0 and (c1 > c0) != (k0 < 2.25):
            failures.append("ramsey: a vertical arrow of motion points against cdot's sign")
    plt.close(fig)

    fig, ax = plt.subplots()
    kk = np.linspace(1.6, 4.0, 60)
    k_s = np.linspace(1.6, 4.0, 40)
    c_jump = draw_time_pref_fall(ax, kk, kk**0.3 - 0.12 * kk, (2.25, 1.0), (2.45, 1.01), (k_s, 0.6 + 0.17 * k_s),
                                 golden=3.7, c_range=(0.85, 1.1))
    # the kdot = 0 curve, two cdot = 0 lines, the saddle path, the two steady states, the golden rule
    if len(ax.get_lines()) != 7:
        failures.append("ramsey: draw_time_pref_fall does not draw both loci, the saddle path, both steady states and the golden rule")
    jumps = [a for a in ax.texts if a.arrow_patch is not None and a.xy[0] == a.xyann[0] == 2.25]
    if len(jumps) != 1 or not jumps[0].xy[1] < jumps[0].xyann[1] or not np.isclose(c_jump, 0.6 + 0.17 * 2.25):
        failures.append("ramsey: draw_time_pref_fall does not draw consumption jumping straight down onto the new saddle path")
    if ax.get_xlim() != (1.6, 4.0) or ax.get_ylim() != (0.85, 1.1):
        failures.append("ramsey: draw_time_pref_fall does not show the view it is given")
    plt.close(fig)
    return failures
