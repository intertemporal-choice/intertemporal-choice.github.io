"""The Fisher two-period chapter's figure and sliders: the drawing, kept out of the notebook.

The chapter's notebook, content/consumption/Fisher2Period/Fisher2Period.ipynb, shows the economics:
the consumption function and the four points A, D, B and C of the decomposition, computed by its
own `effects` function, which it passes here. This module only draws what that function returns,
so the notebook carries no plotting code (Chris, 2026-10-26: "def draw should not be visible in
the notebook -- it's distracting"; collapsing the cell does not hide it in every viewer).

The sliders redraw the panel on fixed axes, the largest any combination of their values needs (Chris,
2026-10-26: "calculate the maximum coordinates/results for any combination of parameter values and
fix the axes to correspond to those values, so that rescaling does not hide meaningful changes").

`python -m intertemporal_choice --self-test` runs `self_test`.
"""

import itertools

import numpy as np

from intertemporal_choice import slider_check

# The sliders: name -> (first value, lowest, highest, step, label). The first values draw the
# chapter's lower panel. The ranges are narrow enough that, on axes holding every combination, that
# first picture still fills a third of the width and a quarter of the height.
SLIDERS = {
    "b1": (0.0, 0.0, 0.5, 0.05, "b₁"),
    "y1": (0.0, 0.0, 1.0, 0.05, "y₁"),
    "y2": (1.0, 0.0, 1.0, 0.05, "y₂"),
    "R_old": (1.0, 0.75, 2.0, 0.05, "R before"),
    "R_new": (2.0, 0.75, 2.0, 0.05, "R after"),
    "beta": (0.96, 0.5, 1.0, 0.01, "β"),
    "rho": (2.0, 0.5, 5.0, 0.1, "ρ"),
}


def _u(c, rho):
    """CRRA utility, logarithmic when rho is one."""
    return np.log(c) if abs(rho - 1) < 1e-9 else c ** (1 - rho) / (1 - rho)


def _u_inverse(v, rho):
    """The consumption that gives utility v."""
    return np.exp(v) if abs(rho - 1) < 1e-9 else ((1 - rho) * v) ** (1 / (1 - rho))


def extent(effects, b1, y1, y2, R_old, R_new, beta, rho):
    """The largest c1 and c2 a panel draws: the ends of its budget lines and its four points."""
    points = effects(b1, y1, y2, R_old, R_new, beta, rho).values()
    c1 = [b1 + y1 + y2 / R for R in (R_old, R_new)] + [P[0] for P in points]
    c2 = [(b1 + y1) * R + y2 for R in (R_old, R_new)] + [P[1] for P in points]
    return max(c1), max(c2)


def axis_limits(effects, sliders=SLIDERS):
    """Axes holding every panel the sliders can draw: a tenth beyond the largest extent at the
    corners of their ranges, where it is largest (the notebook checks a random sample)."""
    names = list(sliders)
    extents = []
    for corner in itertools.product(*(sliders[name][1:3] for name in names)):
        values = dict(zip(names, corner))
        if values["b1"] + values["y1"] + values["y2"] > 0:  # with no resources there is nothing to draw
            extents.append(extent(effects, **values))
    return 1.1 * max(e[0] for e in extents), 1.1 * max(e[1] for e in extents)


def draw(ax, effects, b1, y1, y2, R_old, R_new, beta, rho, limits=None):
    """One panel of the chapter's figure: the budget constraints at the old and the new interest
    factor, the indifference curves through the points, the lines at the old factor through D and
    B, and the size of each effect on c1, for the points `effects(...)` returns. `limits`, the
    sliders' (width, height), fixes the axes; without it they fit this panel."""
    points = effects(b1, y1, y2, R_old, R_new, beta, rho)
    A, D, B, C = (points[k] for k in "ADBC")
    value = lambda P: _u(P[0], rho) + beta * _u(P[1], rho)
    own_width = 1.1 * max(b1 + y1 + y2 / R_old, b1 + y1 + y2 / R_new)  # what this panel alone needs
    own_height = 1.1 * max((b1 + y1) * R + y2 for R in (R_old, R_new))
    width, height = (own_width, own_height) if limits is None else limits
    # the indifference curves stop where the chapter's figure would cut them, not at the sliders' top
    cap = 2 * height if limits is None else own_height
    for R, wealth, line in ((R_old, b1 + y1 + y2 / R_old, "-"), (R_new, b1 + y1 + y2 / R_new, "--")):
        ax.plot([0, wealth], [R * wealth, 0], "k" + line, lw=1.1, label=f"R = {R:.2f}")
    for P in (D, B):  # at the old factor, through D and B
        wealth = P[0] + P[1] / R_old
        ax.plot([0, wealth], [R_old * wealth, 0], ":", color="0.45", lw=1.0)
    same = np.allclose(D, A)  # all income in the first period: no human wealth effect
    for P in (A, C) if same else (A, D, C):  # indifference curves, near each point
        c1 = np.linspace(0.45 * P[0], min(2.2 * P[0], width), 200)
        with np.errstate(all="ignore"):
            c2 = _u_inverse((value(P) - _u(c1, rho)) / beta, rho)
        c2 = np.where(np.isfinite(c2) & (c2 > 0) & (c2 < cap), c2, np.nan)  # the curve's visible branch
        ax.plot(c1, c2, color="C0", lw=1.0)
    if not same:  # the fall in human wealth, on the horizontal axis
        ends = sorted(b1 + y1 + y2 / R for R in (R_old, R_new))
        ax.annotate("", xy=(ends[0], 0.03 * height), xytext=(ends[1], 0.03 * height),
                    arrowprops=dict(arrowstyle="<->", lw=0.9))
        ax.text(sum(ends) / 2, 0.05 * height, "$\\Delta h$", ha="center", va="bottom")
    for name, P in points.items():
        if name == "D" and same:
            continue
        ax.plot(*P, "o", color="black", ms=4)
        ax.annotate(name, P, xytext=(5, 5), textcoords="offset points")
    rows = [("human wealth", "A", "D"), ("income", "D", "B"), ("substitution", "B", "C"), ("total", "A", "C")]
    if same:
        rows = [("income", "A", "B")] + rows[2:]
    text = "\n".join(f"{what} effect {a}{b}: {points[b][0] - points[a][0]:+.3f}" for what, a, b in rows)
    ax.text(0.97, 0.97, f"$(y_1, y_2) = ({y1:g}, {y2:g})$\neffects on $c_1$:\n" + text,
            transform=ax.transAxes, ha="right", va="top", fontsize=9)
    ax.set_xlim(0, width)
    ax.set_ylim(0, height)
    ax.set_xlabel("$c_1$", loc="right")
    ax.set_ylabel("$c_2$", loc="top", rotation=0)
    # on the sliders' fixed axes the diagram sits at the lower left, so the legend goes right
    ax.legend(loc="lower left" if limits is None else "center right", fontsize=9)


def sliders(effects):
    """Sliders for b1, y1, y2, the interest factor before and after, beta and rho, each redrawing the
    panel on the same axes."""
    import ipywidgets as widgets  # only the sliders need it
    import matplotlib.pyplot as plt

    limits = axis_limits(effects)

    def explore(b1, y1, y2, R_old, R_new, beta, rho):
        fig, ax = plt.subplots(figsize=(6.4, 5.0))
        draw(ax, effects, b1, y1, y2, R_old, R_new, beta, rho, limits=limits)
        plt.show()

    widgets.interact(explore, **{
        name: widgets.FloatSlider(value=value, min=low, max=high, step=step, description=label,
                                  continuous_update=False)
        for name, (value, low, high, step, label) in SLIDERS.items()})


def self_test() -> list[str]:
    import matplotlib.pyplot as plt

    failures = []

    def effects(b1, y1, y2, R_old, R_new, beta, rho):  # fixed points, the shapes the notebook returns
        A = np.array([0.5, 0.5])
        D = A.copy() if y2 == 0 else np.array([0.25, 0.25])
        return dict(A=A, D=D, B=np.array([0.35, 0.34]), C=np.array([0.30, 0.41]))

    for y1, y2, letters in ((1, 0, "ABC"), (0, 1, "ABCD")):
        fig, ax = plt.subplots()
        try:
            draw(ax, effects, b1=0, y1=y1, y2=y2, R_old=1.0, R_new=2.0, beta=0.96, rho=2)
        except Exception as e:  # noqa: BLE001
            failures.append(f"fisher: draw failed for income ({y1}, {y2}): {e!r}")
            plt.close(fig)
            continue
        labels = {t.get_text() for t in ax.texts}
        if not set(letters) <= labels or ("D" in labels) != ("D" in letters):
            failures.append(f"fisher: income ({y1}, {y2}) labels {sorted(labels & set('ABCD'))}, expected {letters}")
        if len(ax.lines) < 5:
            failures.append(f"fisher: income ({y1}, {y2}) drew only {len(ax.lines)} lines")
        plt.close(fig)

    def choice(wealth, R, beta, rho):  # the CRRA consumption rule: enough to move every point
        growth = (R * beta) ** (1 / rho)
        c1 = wealth / (1 + growth / R)
        return np.array([c1, growth * c1])

    def moving(b1, y1, y2, R_old, R_new, beta, rho):
        wealth = lambda R: b1 + y1 + y2 / R
        return dict(A=choice(wealth(R_old), R_old, beta, rho), D=choice(wealth(R_new), R_old, beta, rho),
                    B=choice((wealth(R_old) + wealth(R_new)) / 2, R_old, beta, rho),
                    C=choice(wealth(R_new), R_new, beta, rho))

    failures += slider_check.check("fisher", sliders, moving)
    return failures
