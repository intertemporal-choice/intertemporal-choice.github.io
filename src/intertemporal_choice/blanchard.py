"""Blanchard's model of perpetual youth: the notebook's figures, kept out of its notebook.

The notebook, content/growth/BlanchardFiniteHorizon/BlanchardFiniteHorizon.ipynb, computes the
economics: the loci where aggregate consumption and capital stop changing, the steady states, the
saddle paths found by time elimination, and the path of consumption after the government issues
debt. It passes the numbers here. This module only draws, in the letters the book prints: capital K
and consumption C (aggregates, and also amounts per person, since the population is one), the steady
state K̄ and C̄, the RCK model's steady state K̄_RCK, the golden rule K̿, the steady state with debt
K̄_D and C̄_D, the interest rate r, the death rate d, the time preference rate ϑ and the growth of
income with age g. Every curve and point is labeled in the drawing, in words where a symbol would not
say which is which.

`python -m intertemporal_choice --self-test` runs `self_test`.
"""

import numpy as np
from matplotlib.ticker import MaxNLocator
from matplotlib.transforms import offset_copy

from intertemporal_choice.notation import tex

# The loci are colored as in the RCK figures: the Kdot = 0 locus blue, the Cdot = 0 locus orange, the
# saddle path black. The debt's path is purple, as the RCK figures color a path off the saddle path
# (not red and green, which color-blind readers confuse). The arrows of motion are gray.
KDOT, CDOT, SADDLE, DEBT, MOTION, NOTE = "C0", "C1", "black", "C4", "0.45", "0.3"

K_BAR = tex(r"$\Steady{\KNrm}$")                     # K̄
C_BAR = tex(r"$\Steady{\CNrm}$")                     # C̄
K_RCK = tex(r"$\Steady{\KNrm}_{\mathrm{RCK}}$")      # K̄_RCK
K_GOLD = tex(r"$\GoldRule{\KNrm}$")                  # K̿
K_BAR_D = tex(r"$\Steady{\KNrm}_{\Debt}$")           # K̄_D
C_BAR_D = tex(r"$\Steady{\CNrm}_{\Debt}$")           # C̄_D
KDOT_0 = tex(r"$\dot{\KNrm}=0$")
CDOT_0 = tex(r"$\dot{\CNrm}=0$")


def _xtick(ax, x, label):
    """A label under the horizontal axis at x, where a number would be, with a short tick."""
    ax.plot([x, x], [0, 0.015], color="black", linewidth=0.9, transform=ax.get_xaxis_transform(), clip_on=False)
    ax.annotate(label, (x, 0), xytext=(0, -4), textcoords="offset points", ha="center", va="top",
                xycoords=("data", "axes fraction"), fontsize=12)


def _ytick(ax, y, label):
    """A label left of the vertical axis at y, with a short tick."""
    ax.plot([0, 0.012], [y, y], color="black", linewidth=0.9, transform=ax.get_yaxis_transform(), clip_on=False)
    ax.annotate(label, (0, y), xytext=(-4, 0), textcoords="offset points", ha="right", va="center",
                xycoords=("axes fraction", "data"), fontsize=12)


def _guides(ax, x, y):
    """Light dotted lines from the point (x, y) down to the horizontal axis and across to the vertical one."""
    x0, y0 = ax.get_xlim()[0], ax.get_ylim()[0]
    ax.plot([x, x, x0], [y0, y, y], color="0.6", linestyle=":", linewidth=1.0, zorder=1)


def _point(ax, x, y, label, offset, color="black"):
    ax.plot(x, y, "o", color=color, markersize=5, zorder=6)
    ax.annotate(label, (x, y), xytext=offset, textcoords="offset points", fontsize=12, color=color, zorder=6)


def _arrow(ax, x, y, color, at, back=3, lw=1.8):
    """An arrowhead on the path (x, y), pointing along it at index `at`."""
    ax.annotate("", (x[at], y[at]), xytext=(x[at - back], y[at - back]),
                arrowprops={"arrowstyle": "-|>", "color": color, "lw": lw, "mutation_scale": 14,
                            "shrinkA": 0, "shrinkB": 0})


def _midway(ax, x, y, share):
    """The index of the point `share` of the way along the path (x, y), measured as it is drawn."""
    (x0, x1), (y0, y1) = ax.get_xlim(), ax.get_ylim()
    steps = np.hypot(np.diff(x) / (x1 - x0), np.diff(y) / (y1 - y0))
    along = np.concatenate([[0], np.cumsum(steps)])
    return int(np.searchsorted(along, share * along[-1]))


def _motion(ax, K, C, dK, dC, length=17):
    """Two short gray arrows from (K, C): left or right as capital falls or rises (the sign of Kdot, dK),
    down or up as consumption does (dC)."""
    for dx, dy in ((np.sign(dK), 0), (0, np.sign(dC))):
        head = offset_copy(ax.transData, fig=ax.figure, x=dx * length, y=dy * length, units="points")
        ax.annotate("", (K, C), xycoords=head, xytext=(K, C), textcoords="data",
                    arrowprops={"arrowstyle": "-|>", "color": MOTION, "lw": 1.2, "mutation_scale": 10,
                                "shrinkA": 0, "shrinkB": 0})


def _axes(ax, x_range, y_range):
    ax.set_xlim(*x_range)
    ax.set_ylim(*y_range)
    ax.set_xticks([])
    ax.set_yticks([])
    ax.set_xlabel(tex(r"$\KNrm$"), loc="right")
    ax.set_ylabel(tex(r"$\CNrm$"), loc="top", rotation=0)


def _exit_top(K, C, c_max):
    """The capital at which the rising curve C(K) leaves the top of the axes, c_max."""
    i = np.flatnonzero(np.nan_to_num(C, nan=np.inf) >= c_max)[0]
    return np.interp(c_max, C[i - 1 : i + 1], K[i - 1 : i + 1])


def draw_phase(ax, K, kdot0, cdot0, steady, saddle, line, golden, motion, c_max, marks=(), rate_signs=None,
               saddle_label_K=None, a_offset=(-13, 5)):
    """A phase diagram in capital K and consumption C, from the origin.

    K: a grid of capital; kdot0 and cdot0: consumption on the Kdot = 0 and on the Cdot = 0 locus at each K
    (cdot0 NaN where the locus does not reach); steady: the steady state A, (K̄, C̄); saddle: the saddle
    path (K, C), from low capital to high; line: (K, label) for the dashed vertical line that the Cdot = 0
    locus approaches as consumption rises, its label written at its top; golden: the golden rule K̿, at the
    top of the Kdot = 0 locus, marked by a dotted line; motion: (K, C, dK, dC) for each pair of gray arrows
    of motion, dK and dC the signs of Kdot and Cdot there; c_max: the top of the axes; marks: other
    (K, label) to write under the axis; rate_signs: if given, (left, right), written either side of the
    golden rule, where the interest rate is positive and where it is negative; saddle_label_K: the capital
    at which "saddle path" is written, under the path (by default, near its upper end); a_offset: where
    the label A goes, in points from the steady state.
    """
    K_bar, C_bar = steady
    k_max = K[-1]
    _axes(ax, (0, k_max), (0, c_max))
    ax.plot(K, kdot0, color=KDOT)
    ax.annotate(KDOT_0, (k_max, kdot0[-1]), xytext=(-4, -7), textcoords="offset points", ha="right", va="top",
                color=KDOT, fontsize=12)
    shown = np.isfinite(cdot0) & (cdot0 <= 1.05 * c_max)
    ax.plot(K[shown], cdot0[shown], color=CDOT)
    ax.annotate(CDOT_0, (_exit_top(K, cdot0, c_max), c_max), xytext=(-6, -2), textcoords="offset points",
                ha="right", va="top", color=CDOT, fontsize=12)
    k_line, line_label = line
    ax.axvline(k_line, color=CDOT, linestyle="--", linewidth=1.3)
    ax.annotate(line_label, (k_line, c_max), xytext=(5, -2), textcoords="offset points", ha="left", va="top",
                color=CDOT, fontsize=12)
    top = np.interp(golden, K, kdot0)
    ax.plot([golden, golden], [0, top], color="0.4", linestyle=":", linewidth=1.2)
    ax.annotate("golden rule", (golden, top), xytext=(0, 6), textcoords="offset points", ha="center",
                va="bottom", color=NOTE, fontsize=11)
    _xtick(ax, golden, K_GOLD)
    if rate_signs is not None:
        for text, dx, ha in zip(rate_signs, (-5, 5), ("right", "left")):
            ax.annotate(text, (golden, 0.025 * c_max), xytext=(dx, 0), textcoords="offset points", ha=ha,
                        va="bottom", color=NOTE, fontsize=11)
    K_s, C_s = saddle
    keep = C_s <= c_max
    K_s, C_s = K_s[keep], C_s[keep]
    ax.plot(K_s, C_s, color=SADDLE, linewidth=2.2, zorder=4)
    for side in (K_s < K_bar, K_s > K_bar):  # an arrowhead on each branch, pointing at the steady state
        kb, cb = K_s[side], C_s[side]
        order = np.argsort(np.abs(kb - K_bar))[::-1]  # far to near
        _arrow(ax, kb[order], cb[order], SADDLE, at=len(order) // 2)
    k_label = saddle_label_K if saddle_label_K is not None else K_s[int(0.8 * (len(K_s) - 1))]
    ax.annotate("saddle path", (k_label, np.interp(k_label, K_s, C_s)), xytext=(8, -6), textcoords="offset points",
                ha="left", va="top", fontsize=12)
    for point in motion:
        _motion(ax, *point)
    _guides(ax, K_bar, C_bar)
    _point(ax, K_bar, C_bar, "A", a_offset)
    _xtick(ax, K_bar, K_BAR)
    _ytick(ax, C_bar, C_BAR)
    for k, label in marks:
        _xtick(ax, k, label)


def draw_debt_phase(ax, K, kdot0, cdot0_before, cdot0_after, before, after, saddle, jump_to, path, window):
    """The phase diagram of the debt, zoomed on the two steady states.

    K: a grid of capital across the window; kdot0: consumption on the Kdot = 0 locus, which the debt does
    not move; cdot0_before and cdot0_after: consumption on the Cdot = 0 locus without and with the debt;
    before and after: the steady states A, (K̄, C̄), and A′, (K̄_D, C̄_D); saddle: the saddle path with
    the debt (K, C), labeled at its upper end, which should stop short of the window's right edge to
    leave the label room; jump_to: consumption just after date 0, on that saddle path at K̄; path: (K, C)
    from there toward A′, in time order; window: ((K low, K high), (C low, C high)).

    At date 0 capital cannot jump and consumption can: it jumps from A up onto the saddle path with the
    debt (dotted purple), and then capital and consumption fall along that path toward A′ (solid purple).
    """
    (k_lo, k_hi), (c_lo, c_hi) = window
    _axes(ax, (k_lo, k_hi), (c_lo, c_hi))
    ax.plot(K, kdot0, color=KDOT)
    ax.annotate(KDOT_0, (K[-1], kdot0[-1]), xytext=(-4, -7), textcoords="offset points", ha="right", va="top",
                color=KDOT, fontsize=12)
    # The locus with debt is labeled on its right, the one without on its left: between them, where nothing else is.
    for c, words, style, dx, ha in ((cdot0_before, "no debt", "-", -6, "right"),
                                    (cdot0_after, "with debt", "--", 6, "left")):
        ax.plot(K, c, color=CDOT, linestyle=style)
        ax.annotate(f"{CDOT_0},\n{words}", (_exit_top(K, c, c_hi), c_hi), xytext=(dx, -4), textcoords="offset points",
                    ha=ha, va="top", color=CDOT, fontsize=12, linespacing=1.3)
    K_s, C_s = saddle
    ax.plot(K_s, C_s, color=SADDLE, linewidth=2.2, zorder=3)
    ax.annotate("saddle path\nwith debt", (K_s[-1], C_s[-1]), xytext=(5, 0), textcoords="offset points",
                ha="left", va="center", fontsize=12, linespacing=1.3)
    (K_bar, C_bar), (K_bar_D, C_bar_D) = before, after
    ax.plot([K_bar, K_bar], [C_bar, jump_to], color=DEBT, linestyle=":", linewidth=2.0, zorder=4)
    ax.annotate("", (K_bar, jump_to), xytext=(K_bar, C_bar + 0.6 * (jump_to - C_bar)),
                arrowprops={"arrowstyle": "-|>", "color": DEBT, "lw": 1.8, "mutation_scale": 14, "shrinkA": 0,
                            "shrinkB": 0})
    ax.annotate("jump at\ndate 0", (K_bar, 0.5 * (C_bar + jump_to)), xytext=(16, 0), textcoords="offset points",
                ha="left", va="center", color=DEBT, fontsize=12, linespacing=1.3)
    K_p, C_p = path
    ax.plot(K_p, C_p, color=DEBT, linewidth=1.8, zorder=5)
    at = _midway(ax, K_p, C_p, 0.45)
    _arrow(ax, K_p, C_p, DEBT, at=at)
    ax.annotate("after date 0", (K_p[0], C_p[0]), xytext=(-8, 7), textcoords="offset points", ha="right",
                va="bottom", color=DEBT, fontsize=12)
    ax.plot(K_bar, jump_to, "o", color=DEBT, markersize=4, zorder=6)
    for k, c in ((K_bar, C_bar), (K_bar_D, C_bar_D)):
        _guides(ax, k, c)
    _point(ax, K_bar, C_bar, "A", (6, -15))
    _point(ax, K_bar_D, C_bar_D, "A′", (6, -16))
    _xtick(ax, K_bar, K_BAR)
    _xtick(ax, K_bar_D, K_BAR_D)
    _ytick(ax, C_bar, C_BAR)
    _ytick(ax, C_bar_D, C_BAR_D)


def draw_consumption(ax, t, C, before, after):
    """Aggregate consumption over time: t, years after the debt is issued; C, consumption then; before
    and after, the steady-state levels C̄ (at A) and C̄_D (at A′), drawn dashed."""
    span = np.max(C) - after
    ax.set_ylim(after - 0.2 * span, np.max(C) + 0.08 * span)
    ax.axvline(0, color="0.6", linestyle=":", linewidth=1.2)
    ax.annotate("debt issued", (0, 0), xycoords=("data", "axes fraction"), xytext=(-5, 4), textcoords="offset points",
                ha="right", va="bottom", color=NOTE, fontsize=11)
    for level, words, va, dy in ((before, f"{C_BAR}, before the debt", "bottom", 3),
                                 (after, f"{C_BAR_D}, with the debt", "top", -4)):
        ax.axhline(level, color="0.45", linestyle="--", linewidth=1.2)
        ax.annotate(words, (t[-1], level), xytext=(-2, dy), textcoords="offset points", ha="right", va=va,
                    color=NOTE, fontsize=11)
    ax.plot(t, C, color=DEBT, linewidth=2.0)
    i = np.searchsorted(t, 0.06 * (t[-1] - t[0]), side="right")  # a little after date 0, on the way down
    ax.annotate("consumption", (t[i], C[i]), xytext=(8, 2), textcoords="offset points", ha="left", va="bottom",
                color=DEBT, fontsize=11)
    ax.set_xlim(t[0], t[-1])
    ax.yaxis.set_major_locator(MaxNLocator(5))
    ax.set_xlabel("years after the debt is issued", loc="right")
    ax.set_ylabel(tex(r"$\CNrm$"), loc="top", rotation=0)


def self_test() -> list[str]:
    import matplotlib.pyplot as plt

    failures = []
    K = np.linspace(1e-3, 9, 200)
    kdot0 = K**0.3 - 0.08 * K
    r = 0.3 * K**-0.7 - 0.08
    cdot0 = np.where(r > 0.02, 0.0035 * K / np.where(r > 0.02, r - 0.02, 1), np.nan)
    K_s = np.linspace(1, 8, 50)
    fig, ax = plt.subplots()
    motion = [(1.0, 1.6, -1, 1), (2.0, 0.8, 1, 1), (6.0, 0.3, 1, -1), (7.5, 1.6, -1, -1)]
    draw_phase(ax, K, kdot0, cdot0, (4.09, 1.199), (K_s, 0.3 + 0.2 * K_s), (4.8, "line"), 6.6, motion, 1.9,
               marks=[(4.8, "x")], rate_signs=("+", "-"))
    # the two loci, the dashed line, the golden rule's dotted line, the saddle path, the guides, A, and four ticks
    if len(ax.get_lines()) != 11:
        failures.append(f"blanchard: draw_phase drew {len(ax.get_lines())} lines, not the loci, the saddle path, A "
                        "and the ticks")
    arrows = [a for a in ax.texts if a.arrow_patch is not None]
    if len(arrows) != 2 + 2 * len(motion):
        failures.append("blanchard: draw_phase does not put an arrowhead on each branch of the saddle path and on "
                        "each arrow of motion")
    if not {"saddle path", "golden rule", "A"} <= {t.get_text() for t in ax.texts}:
        failures.append("blanchard: draw_phase does not label the saddle path, the golden rule and A")
    if {line.get_color() for line in ax.get_lines()} & {"C2", "C3", "tab:green", "tab:red"}:
        failures.append("blanchard: draw_phase draws in red or green")
    plt.close(fig)

    fig, ax = plt.subplots()
    K = np.linspace(3.9, 4.2, 50)
    draw_debt_phase(ax, K, 1.17 + 0.03 * (K - 3.9), 1.19 + 2.2 * (K - 4.09), 1.19 + 2.2 * (K - 3.99),
                    (4.09, 1.199), (3.99, 1.195), (K, 1.195 + 0.17 * (K - 3.99)), 1.213,
                    (np.linspace(4.09, 4.0, 20), np.linspace(1.213, 1.197, 20)), ((3.9, 4.2), (1.18, 1.23)))
    texts = " ".join(t.get_text() for t in ax.texts)
    if not all(word in texts for word in ("no debt", "with debt", "jump", "after date 0", "A′")):
        failures.append("blanchard: draw_debt_phase does not say which locus, path and point is which")
    plt.close(fig)

    fig, ax = plt.subplots()
    t = np.linspace(-10, 60, 100)
    draw_consumption(ax, t, np.where(t < 0, 1.20, 1.195 + 0.018 * np.exp(-0.14 * np.maximum(t, 0))), 1.20, 1.195)
    if len(ax.get_lines()) != 4:
        failures.append("blanchard: draw_consumption does not draw the path, the two levels and date 0")
    plt.close(fig)
    return failures
