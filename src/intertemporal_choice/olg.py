"""The Diamond OLG chapter's figures and sliders, kept out of its notebook.

The notebook, content/consumption/OLGModel/OLGModel.ipynb, shows the economics: the chapter's
equations for the accumulation of capital, the steady state, the golden rule and the planner's
steady state, and the Social Security chapter's curve, both with that chapter's fixed interest
factor and exactly. It passes those functions here, and this module only draws, as `fisher` and
`portfolio` do for their chapters.

A period is a generation. The sliders take a discount factor and a population growth rate per
year and turn them into a generation's: beta = beta_year^years and Xi = (1 + n)^years.

Every slider panel redraws on fixed axes, the largest any combination of its sliders' values needs
(Chris, 2026-10-26: "calculate the maximum coordinates/results for any combination of parameter
values and fix the axes to correspond to those values, so that rescaling does not hide meaningful
changes"). Each quantity drawn is monotone in each parameter, so the largest values are found at
the corners of the sliders' ranges.

`python -m intertemporal_choice --self-test` runs `self_test`.
"""

import itertools

import numpy as np

from intertemporal_choice import slider_check

YEARS = 30  # a generation
BEFORE = {"alpha": 1 / 3, "beta_year": 0.96, "growth_year": 0.01}  # the chapter's calibration
READOUT = dict(facecolor="white", edgecolor="none", alpha=0.85)  # a readout stays legible over a line

# The sliders, by panel: name -> (first value, lowest, highest, step, label, readout format). The
# first values are the chapter's calibration, except the transition's, which raise patience. The
# ranges are narrow enough that, on axes holding every combination, each first picture's steady
# state is about 60 percent of the way across its frame (a 30-year generation compounds every
# annual parameter; Chris, 2026-10-27: the ranges were "too wide, with the result that the figures
# often occupy too little of the available space"). The output panel keeps wide ranges, so that
# the economy can become dynamically inefficient, and draws capital on a log scale instead.
DYNAMICS = {
    "alpha": (1 / 3, 0.31, 0.36, 0.01, "capital share α", ".2f"),
    "beta_year": (0.96, 0.957, 0.963, 0.001, "β per year", ".3f"),
    "growth_year": (0.01, 0.007, 0.013, 0.001, "population growth per year", ".3f"),
}
OUTPUT = {
    "alpha": (1 / 3, 0.20, 0.40, 0.01, "capital share α", ".2f"),
    "beta_year": (0.96, 0.94, 0.999, 0.001, "β per year", ".3f"),
    "growth_year": (0.01, 0.01, 0.04, 0.001, "population growth per year", ".3f"),
    "beth_year": (0.98, 0.94, 0.999, 0.001, "planner's ℶ per year", ".3f"),
}
TRANSITION = {
    "alpha": (1 / 3, 0.31, 0.36, 0.01, "capital share α from now on", ".2f"),
    "beta_year": (0.97, 0.955, 0.972, 0.001, "β per year from now on", ".3f"),
    "growth_year": (0.01, 0.007, 0.013, 0.001, "population growth from now on", ".3f"),
    "jump": (0.0, 0.0, 0.5, 0.05, "one-time rise in the number of young", ".2f"),
}
SOCIAL_SECURITY = {
    "contribution": (0.10, 0.0, 0.30, 0.01, "contribution, share of the old wage", ".2f"),
    "alpha": (1 / 3, 0.31, 0.36, 0.01, "capital share α", ".2f"),
    "beta_year": (0.96, 0.957, 0.963, 0.001, "β per year", ".3f"),
}
MARGIN = 1.15  # a frame runs this far beyond the largest steady state any combination reaches

# A staircase's arrow heads shrink with the arrows, which shrink geometrically toward the steady
# state, and the staircase stops once an arrow would be too short to read: drawn at full size,
# the last heads piled up there (Chris, 2026-10-27). Lengths are shares of the frame.
FULL_ARROW = 0.08  # an arrow at least this long has a full-size head
SHORTEST_ARROW = 0.02  # the staircase stops before an arrow this short

# While a picture is being drawn, "drawing" and a dot a second appear above it, but only after
# half a second, so a quick redraw does not flicker (Chris, 2026-10-27: "some indicator that
# calculations are ongoing ... a series of periods/dots that adds one dot per second").
_DOTS = "".join(f"{10 * i}%{{content:'{'.' * i}'}}" for i in range(10))
BUSY = ("<style>.ic-busy{opacity:0;animation:ic-show 0s .5s forwards}"
        ".ic-busy::after{content:'';animation:ic-dots 10s step-end .5s infinite}"
        f"@keyframes ic-show{{to{{opacity:1}}}}@keyframes ic-dots{{{_DOTS}}}</style>"
        "<span class='ic-busy'>drawing</span>")


def _per_generation(beta_year, growth_year, years=YEARS):
    return beta_year**years, (1 + growth_year) ** years


def _corners(table):
    """Every combination of the lowest and highest values of a panel's sliders."""
    names = list(table)
    return [dict(zip(names, values)) for values in itertools.product(*(table[name][1:3] for name in names))]


def _look(widgets, labels):
    """One label width for all of a panel's sliders, set by its longest label, and a track about 20 em
    long beside it. A slider is 300 px wide in all unless told otherwise, so a long label left its
    track a few pixels, or none."""
    label = 0.55 * max(len(text) for text in labels) + 1  # em: a character is about half an em wide
    return {"style": {"description_width": f"{label:.1f}em"}, "layout": widgets.Layout(width=f"{label + 25:.1f}em")}


def _controls(widgets, table, look=None):
    """The panel's sliders. They redraw while they move: ipywidgets sends only the latest value
    while a picture is being drawn, so the picture keeps up instead of waiting for the release."""
    look = look or _look(widgets, [row[4] for row in table.values()])
    return {name: widgets.FloatSlider(value=value, min=low, max=high, step=step, description=label,
                                      readout_format=fmt, **look)
            for name, (value, low, high, step, label, fmt) in table.items()}


def _panel(widgets, explore, controls):
    """Show the sliders, the note that appears while a picture takes long to draw, and the picture."""
    from IPython.display import display

    status = widgets.HTML()

    def draw(**values):
        status.value = BUSY
        try:
            explore(**values)
        finally:
            status.value = ""

    display(widgets.VBox([*controls.values(), status, widgets.interactive_output(draw, controls)]))


def _staircase(ax, k_next, k0, steps, span, base=0.0):
    """Arrows from (k0, base) up to the accumulation curve, across to the 45-degree line, and so
    on, for at most `steps` generations: each head in proportion to its arrow, until an arrow would
    be shorter than SHORTEST_ARROW of `span`, the frame's width. Returns where the arrows stop."""
    kt = k0
    for _ in range(steps):
        k1 = float(k_next(kt))
        for start, end in (((kt, base), (kt, k1)), ((kt, k1), (k1, k1))):
            length = abs(end[1] - start[1] + end[0] - start[0]) / span  # each arrow is level or upright
            if length < SHORTEST_ARROW:
                return kt
            ax.annotate("", xy=end, xytext=start, arrowprops=dict(
                arrowstyle="->", lw=0.9, mutation_scale=10 * min(1.0, length / FULL_ARROW)))
        kt, base = k1, k1
    return kt


def draw_dynamics(ax, k_next, k0, kbar, steps=8, kmax=None):
    """The chapter's first figure: capital per worker converging to the steady state. `kmax`, from
    the sliders, fixes the axes; without it they fit this economy."""
    kmax = 1.35 * max(kbar, k0) if kmax is None else kmax
    k = np.linspace(0, kmax, 400)
    ax.plot(k, k_next(k), color="black", lw=1.8)
    ax.plot(k, k, color="C0", lw=1.0, linestyle="--")
    ax.axvline(kbar, color="black", lw=0.8, linestyle="--")
    _staircase(ax, k_next, k0, steps, kmax)
    # beyond the steady state, below the curve: clear of the staircase, which ends at the steady state
    ax.annotate(r"$k_{t+1}(k_t)$", (0.85 * kmax, float(k_next(0.85 * kmax))), xytext=(-20, -20),
                textcoords="offset points")
    ax.annotate("45° line", (0.95 * kmax, 0.95 * kmax), xytext=(-55, 4), textcoords="offset points")
    ax.annotate(r"$k_1$", (k0, float(k_next(k0))), xytext=(-18, 2), textcoords="offset points")
    ax.set_xlim(0, kmax)
    ax.set_ylim(0, kmax)
    ax.set_xticks([k0, kbar], [r"$k_0$", r"$\bar{k}$"])
    ax.set_yticks([])
    ax.set_xlabel(r"$k_t$", loc="right")
    ax.set_ylabel(r"$k_{t+1}$", loc="top", rotation=0)


def draw_output(top, bottom, alpha, xi, kgold, kbar=None, limits=None, kplanner=None):
    """The chapter's second figure: gross output f(k) and xi k (top), and their difference,
    steady-state consumption per worker, which is highest at the golden rule (bottom). Without
    `limits` the panels run, on a linear scale, to where consumption would be zero. `limits`, from
    the sliders, is (the smallest and the largest k, the top panel's top, the bottom panel's top),
    and k is then on a log scale, which gives the economy's steady state, the planner's and the
    golden rule room: at the chapter's calibration the economy has a twenty-fifth of the golden
    rule's capital, and on a linear scale it sat against the left edge (Chris, 2026-10-27)."""
    kzero = xi ** (1 / (alpha - 1))  # where f(k) = xi k and consumption would be zero
    if limits is None:
        left, right = 0.0, 1.05 * kzero
        k = np.linspace(left, right, 500)
        across = lambda share: share * kzero  # a point some share of the way across
    else:
        left, right = limits[0], limits[1]
        k = np.geomspace(left, right, 500)
        across = lambda share: left * (right / left) ** share
    f = k**alpha
    top.plot(k, f, color="black", lw=1.8)
    top.plot(k, xi * k, color="C0", lw=1.0, linestyle="--")
    if limits is None:
        x = across(0.6)
        top.annotate(r"$\mathrm{f}(k)$", (x, x**alpha), xytext=(0, 8), textcoords="offset points")
        top.annotate(r"$\xi k$", (x, xi * x), xytext=(8, -14), textcoords="offset points")
    else:  # inside the fixed frame
        x, y = across(0.85), min(across(0.97), 0.6 * limits[2] / xi)  # xi k rises late on a log scale
        top.annotate(r"$\mathrm{f}(k)$", (x, x**alpha), xytext=(-12, 8), textcoords="offset points")
        top.annotate(r"$\xi k$", (y, xi * y), xytext=(-24, 0), textcoords="offset points")
    bottom.plot(k, f - xi * k, color="black", lw=1.8)
    bottom.axvline(kgold, color="0.45", lw=0.8, linestyle=":", label=r"$k^{**}$, the golden rule")
    ticks, names = [kgold], [r"$k^{**}$"]
    if kbar is not None:
        bottom.axvline(kbar, color="C1", lw=0.8, linestyle="--", label=r"$\bar{k}$, the economy's")
        ticks, names = ticks + [kbar], names + [r"$\bar{k}$"]
    if kplanner is not None:
        bottom.axvline(kplanner, color="C2", lw=0.8, linestyle="-.", label=r"$k^{*}$, the planner's")
        ticks, names = ticks + [kplanner], names + [r"$k^{*}$"]
    x = across(0.75) if limits is None else across(0.08)
    bottom.annotate(r"$\mathrm{f}(k)-\xi k$", (x, x**alpha - xi * x), xytext=(6, 6) if limits is None else (0, 14),
                    textcoords="offset points")
    for ax, height in ((top, None if limits is None else limits[2]), (bottom, None if limits is None else limits[3])):
        if limits is not None:
            ax.set_xscale("log")
        ax.set_xlim(left, right)
        ax.set_ylim(0, height)
        ax.set_yticks([])
        ax.set_xlabel(r"$k$" if limits is None else r"$k$, on a log scale", loc="right")
    top.set_xticks([])
    if limits is None:  # the chapter's figure
        bottom.set_xticks(ticks, names)
    else:  # the three can sit close together, so a legend names them
        for ax in (top, bottom):
            ax.set_xticks([])
            ax.set_xticks([], minor=True)
        bottom.legend(loc="lower right", fontsize=8)


def dynamics_limits(k_bar, table=DYNAMICS):
    """The largest capital the dynamics panel draws: MARGIN beyond the highest steady state."""
    return MARGIN * max(k_bar(c["alpha"], *_per_generation(c["beta_year"], c["growth_year"])) for c in _corners(table))


def sliders_dynamics(k_next, k_bar, table=DYNAMICS):
    """Sliders for the capital share, patience, population growth and the capital the economy starts
    with, on axes holding the steady state of every combination."""
    import ipywidgets as widgets  # only the sliders need it
    import matplotlib.pyplot as plt

    kmax = dynamics_limits(k_bar, table)
    first = {name: row[0] for name, row in table.items()}
    kbar_first = k_bar(first["alpha"], *_per_generation(first["beta_year"], first["growth_year"]))

    def explore(alpha, beta_year, growth_year, k0):
        beta, Xi = _per_generation(beta_year, growth_year)
        kbar = k_bar(alpha, beta, Xi)
        fig, ax = plt.subplots(figsize=(6.4, 5.0))
        draw_dynamics(ax, lambda k: k_next(k, alpha, beta, Xi), k0, kbar, kmax=kmax)
        ax.text(0.03, 0.97, f"$\\bar{{k}}$ = {kbar:.4f}\neach generation closes {1 - alpha:.0%}\n"
                f"of the log gap to $\\bar{{k}}$", transform=ax.transAxes, va="top", fontsize=9, bbox=READOUT)
        plt.show()

    start = "capital to start with, k₀"
    look = _look(widgets, [row[4] for row in table.values()] + [start])
    controls = _controls(widgets, table, look)
    # rounded down: a tick beyond the axis would make matplotlib widen it
    controls["k0"] = widgets.FloatSlider(value=round(kbar_first / 4, 3), min=0.002, max=np.floor(kmax * 1000) / 1000, step=0.001,
                                         description=start, readout_format=".3f", **look)
    _panel(widgets, explore, controls)


def output_limits(k_bar, k_golden, k_planner, table=OUTPUT):
    """The output panel's (smallest k, largest k, top panel's top, bottom panel's top): on its log
    scale, from a third below the smallest to half again beyond the largest of the three steady
    states any combination reaches, and the highest output and consumption in between."""
    small, large = np.inf, 0.0
    for c in _corners(table):
        beta, Xi = _per_generation(c["beta_year"], c["growth_year"])
        points = (k_bar(c["alpha"], beta, Xi), k_golden(c["alpha"], Xi - 1),
                  k_planner(c["alpha"], Xi, c["beth_year"] ** YEARS))
        small, large = min(small, *points), max(large, *points)
    left, right = small / 1.5, 1.5 * large
    k = np.geomspace(left, right, 400)
    top, bottom = 0.0, 0.0
    for c in _corners(table):
        xi = _per_generation(c["beta_year"], c["growth_year"])[1] - 1
        top = max(top, 1.05 * float(np.max(k ** c["alpha"])))
        bottom = max(bottom, 1.05 * float(np.max(k ** c["alpha"] - xi * k)))
    return left, right, top, bottom


def sliders_output(k_bar, k_golden, k_planner, interest_factor, table=OUTPUT):
    """Sliders for the capital share, patience, population growth and the planner's discount factor:
    output, the economy's steady state, the planner's and the golden rule, and whether the economy
    is dynamically efficient, judged by its interest rate against population growth."""
    import ipywidgets as widgets  # only the sliders need it
    import matplotlib.pyplot as plt

    limits = output_limits(k_bar, k_golden, k_planner, table)

    def explore(alpha, beta_year, growth_year, beth_year):
        beta, Xi = _per_generation(beta_year, growth_year)
        kbar, kgold = k_bar(alpha, beta, Xi), k_golden(alpha, Xi - 1)
        kstar = k_planner(alpha, Xi, beth_year**YEARS)
        rate = interest_factor(kbar, alpha) ** (1 / YEARS) - 1
        fig, (top, bottom) = plt.subplots(2, 1, figsize=(6.4, 7.0))
        draw_output(top, bottom, alpha, Xi - 1, kgold, kbar, limits=limits, kplanner=kstar)
        verdict = "dynamically inefficient" if kbar > kgold else "dynamically efficient"
        fig.suptitle(f"interest rate {rate:.1%} a year, population growth {growth_year:.1%}: {verdict}\n"
                     f"$\\bar{{k}}$ = {kbar:.3f}, $k^{{*}}$ = {kstar:.3f}, $k^{{**}}$ = {kgold:.3f}", fontsize=9)
        plt.show()

    _panel(widgets, explore, _controls(widgets, table))


def _transition_path(k_next, k_bar, wage, interest_factor, change, generations):
    """Capital, the wage and the interest rate by generation, relative to the old steady state: one
    generation before the change, then from the change on, under the new values."""
    before = _per_generation(BEFORE["beta_year"], BEFORE["growth_year"])
    kbar0 = k_bar(BEFORE["alpha"], *before)
    beta, Xi = _per_generation(change["beta_year"], change["growth_year"])
    k = [kbar0, kbar0 / (1 + change["jump"])]  # more young share the same capital
    for _ in range(generations):
        k.append(float(k_next(k[-1], change["alpha"], beta, Xi)))
    k = np.array(k)
    alphas = np.array([BEFORE["alpha"]] + [change["alpha"]] * (len(k) - 1))
    w0, r0 = wage(kbar0, BEFORE["alpha"]), interest_factor(kbar0, BEFORE["alpha"]) - 1
    return k, {"capital": k / kbar0, "wage": wage(k, alphas) / w0, "interest rate": (interest_factor(k, alphas) - 1) / r0}


def transition_limits(k_next, k_bar, wage, interest_factor, table=TRANSITION, generations=8):
    """The transition panel's largest capital, and the lowest and highest ratio its paths reach."""
    before = k_bar(BEFORE["alpha"], *_per_generation(BEFORE["beta_year"], BEFORE["growth_year"]))
    kmax, low, high = before, 1.0, 1.0
    for c in _corners(table):
        kmax = max(kmax, k_bar(c["alpha"], *_per_generation(c["beta_year"], c["growth_year"])))
        _, paths = _transition_path(k_next, k_bar, wage, interest_factor, c, generations)
        low = min([low] + [float(np.min(p)) for p in paths.values()])
        high = max([high] + [float(np.max(p)) for p in paths.values()])
    spare = 0.05 * (high - low)
    return MARGIN * kmax, (low - spare, high + spare)


def sliders_transition(k_next, k_bar, wage, interest_factor, table=TRANSITION, generations=8):
    """Sliders for what changes now, in the old steady state (the chapter's calibration): the capital
    share, patience and population growth from now on, and a one-time rise in the number of young.
    Left, the old and new accumulation curves and the path between them; right, capital, the wage and
    the interest rate by generation, relative to the old steady state."""
    import ipywidgets as widgets  # only the sliders need it
    import matplotlib.pyplot as plt

    kmax, (low, high) = transition_limits(k_next, k_bar, wage, interest_factor, table, generations)
    beta0, Xi0 = _per_generation(BEFORE["beta_year"], BEFORE["growth_year"])
    kbar0 = k_bar(BEFORE["alpha"], beta0, Xi0)

    def explore(alpha, beta_year, growth_year, jump):
        change = {"alpha": alpha, "beta_year": beta_year, "growth_year": growth_year, "jump": jump}
        beta, Xi = _per_generation(beta_year, growth_year)
        kbar = k_bar(alpha, beta, Xi)
        k, paths = _transition_path(k_next, k_bar, wage, interest_factor, change, generations)
        fig, (left, right) = plt.subplots(1, 2, figsize=(11.0, 4.6))
        grid = np.linspace(0, kmax, 400)
        left.plot(grid, k_next(grid, BEFORE["alpha"], beta0, Xi0), color="0.6", lw=1.4, label="before")
        left.plot(grid, k_next(grid, alpha, beta, Xi), color="black", lw=1.8, label="from now on")
        left.plot(grid, grid, color="C0", lw=1.0, linestyle="--")
        _staircase(left, lambda x: k_next(x, alpha, beta, Xi), k[1], generations, kmax)
        left.axvline(kbar0, color="0.6", lw=0.8, linestyle="--")
        left.axvline(kbar, color="black", lw=0.8, linestyle="--")
        left.set_xlim(0, kmax)
        left.set_ylim(0, kmax)
        left.set_xticks([])
        if np.isclose(kbar, kbar0, rtol=1e-3):
            marks = [(kbar0, r"$\bar{k}$, before and after", "left", "black")]
        else:  # the left one's label to its left, the right one's to its right
            (x0, l0, c0), (x1, l1, c1) = sorted(((kbar0, r"$\bar{k}$ before", "0.45"), (kbar, r"$\bar{k}$ after", "black")))
            marks = [(x0, l0, "right", c0), (x1, l1, "left", c1)]
        for x, label, align, color in marks:
            left.annotate(label, (x, 0.97 * kmax), xytext=(4 if align == "left" else -4, 0),
                          textcoords="offset points", ha=align, va="top", color=color, fontsize=9)
        left.set_yticks([])
        left.set_xlabel(r"$k_t$", loc="right")
        left.set_ylabel(r"$k_{t+1}$", loc="top", rotation=0)
        left.legend(loc="lower right", fontsize=9)
        t = np.arange(-1, len(k) - 1)
        for (name, path), color in zip(paths.items(), ("black", "C0", "C1")):
            right.plot(t, path, color=color, marker="o", ms=3, lw=1.4, label=name)
        right.axhline(1, color="0.6", lw=0.6)
        right.axvline(-0.5, color="0.6", lw=0.6, linestyle=":")
        right.set_xlim(-1.5, len(k) - 1.5)
        right.set_ylim(low, high)
        right.set_xlabel("generation (the change comes at 0)", loc="right")
        right.set_ylabel("relative to before", loc="top")
        right.legend(loc="upper right", fontsize=9)
        right.text(0.03, 0.04, f"capital in the new steady state: {kbar / kbar0:.2f} times the old",
                   transform=right.transAxes, fontsize=9, bbox=READOUT)
        fig.tight_layout()
        plt.show()

    _panel(widgets, explore, _controls(widgets, table))


def payg_limits(k_bar, table=SOCIAL_SECURITY):
    """The largest capital the Social Security panel draws: MARGIN beyond the highest steady
    state without it (contributions only lower the curve)."""
    return MARGIN * max(k_bar(c["alpha"], c["beta_year"] ** YEARS, 1.0) for c in _corners(table))


def sliders_payg(k_next, k_bar, wage, k_next_payg, k_bar_payg, k_next_payg_exact, k_bar_payg_exact,
                 table=SOCIAL_SECURITY):
    """Sliders for the size of a pay-as-you-go system, the capital share and patience: the path from
    the old steady state to the new one, with no population growth, as in the Social Security
    chapter. The contribution is a fixed amount, a share of the wage in the old steady state. The
    exact curve lets the interest factor move with capital; the chapter's holds it at its old value."""
    import ipywidgets as widgets  # only the sliders need it
    import matplotlib.pyplot as plt

    kmax = payg_limits(k_bar, table)

    def explore(contribution, alpha, beta_year):
        beta = beta_year**YEARS
        kbar = k_bar(alpha, beta, 1.0)
        z = contribution * wage(kbar, alpha)
        exact, shortcut = k_bar_payg_exact(alpha, beta, z), k_bar_payg(alpha, beta, z)
        k = np.linspace(1e-9, kmax, 400)
        fig, ax = plt.subplots(figsize=(6.4, 5.0))
        ax.plot(k, k_next(k, alpha, beta, 1.0), color="black", lw=1.8, label="before")
        ax.plot(k, k_next_payg(k, alpha, beta, z), color="0.55", lw=1.4, linestyle="--",
                label="with it, R held at its old value (the chapter's figure)")
        ax.plot(k, k_next_payg_exact(k, alpha, beta, z), color="C1", lw=1.8, label="with it, exactly")
        ax.plot(k, k, color="C0", lw=1.0, linestyle="--")
        ticks, names = [kbar], [r"$\bar{k}$"]
        if exact is not None:  # from the old steady state toward the new one, on the exact curve
            _staircase(ax, lambda x: k_next_payg_exact(x, alpha, beta, z), kbar, 8, kmax, base=kbar)
            ticks, names = [exact] + ticks, [r"$\bar{\bar{k}}$"] + names
            fallen = f"capital falls {1 - exact / kbar:.0%}"
            held = ("no steady state" if shortcut is None else f"{1 - shortcut / kbar:.0%}")
            text = f"{fallen}; with R held at its old value, {held}"
        else:
            text = "Contributions this large leave no steady state: capital runs out."
        ax.set_xlim(0, kmax)
        ax.set_ylim(0, kmax)
        ax.set_xticks(ticks, names)
        ax.set_yticks([])
        ax.set_xlabel(r"$k_t$", loc="right")
        ax.set_ylabel(r"$k_{t+1}$", loc="top", rotation=0)
        ax.legend(loc="lower right", fontsize=8)
        ax.text(0.03, 0.97, text, transform=ax.transAxes, va="top", fontsize=9, bbox=READOUT)
        plt.show()

    _panel(widgets, explore, _controls(widgets, table))


def self_test() -> list[str]:
    import matplotlib.pyplot as plt

    failures = []
    # the chapter's economics in closed form, enough to drive every panel
    wage = lambda k, alpha: (1 - alpha) * np.asarray(k, float) ** alpha
    interest_factor = lambda k, alpha: 1 + alpha * np.asarray(k, float) ** (alpha - 1)
    Q = lambda alpha, beta, Xi: (1 - alpha) * beta / (Xi * (1 + beta))
    k_next = lambda k, alpha, beta, Xi: Q(alpha, beta, Xi) * np.asarray(k, float) ** alpha
    k_bar = lambda alpha, beta, Xi: Q(alpha, beta, Xi) ** (1 / (1 - alpha))
    k_golden = lambda alpha, xi: (xi / alpha) ** (1 / (alpha - 1))
    k_planner = lambda alpha, Xi, beth: ((Xi / beth - 1) / alpha) ** (1 / (alpha - 1))
    shift = lambda alpha, beta, z: z * (1 + interest_factor(k_bar(alpha, beta, 1.0), alpha) * beta) / (
        interest_factor(k_bar(alpha, beta, 1.0), alpha) * (1 + beta))
    payg = lambda k, alpha, beta, z: k_next(k, alpha, beta, 1.0) - shift(alpha, beta, z)
    steady = lambda alpha, beta, z: 0.8 * k_bar(alpha, beta, 1.0) if z < 0.02 else None

    alpha, beta, Xi = 1 / 3, 0.96**YEARS, 1.01**YEARS
    kbar = k_bar(alpha, beta, Xi)
    fig, ax = plt.subplots()
    try:
        draw_dynamics(ax, lambda k: k_next(k, alpha, beta, Xi), kbar / 4, kbar)
        if len(ax.lines) < 3:
            failures.append(f"olg: draw_dynamics drew {len(ax.lines)} lines")
    except Exception as e:  # noqa: BLE001
        failures.append(f"olg: draw_dynamics failed: {e!r}")
    plt.close(fig)
    # the staircase stops within its shortest arrow of the steady state, its heads never growing
    span = 1.5 * kbar
    _, ax = plt.subplots()
    end = _staircase(ax, lambda k: k_next(k, alpha, beta, Xi), kbar / 4, 60, span)
    heads = [a.arrow_patch.get_mutation_scale() for a in ax.texts]
    if abs(end - kbar) > 2 * SHORTEST_ARROW * span or len(heads) < 4:
        failures.append(f"olg: the staircase stops at {end:.4f}, not near the steady state {kbar:.4f}, after {len(heads)} arrows")
    if any(later > earlier for earlier, later in zip(heads, heads[1:])) or heads[-1] >= heads[0]:
        failures.append(f"olg: the staircase's heads do not shrink toward the steady state: {heads}")
    plt.close("all")
    fig, (top, bottom) = plt.subplots(2, 1)
    try:
        draw_output(top, bottom, alpha, Xi - 1, k_golden(alpha, Xi - 1), kbar)
    except Exception as e:  # noqa: BLE001
        failures.append(f"olg: draw_output failed: {e!r}")
    plt.close(fig)

    # the fixed axes hold a random sample of each panel's combinations
    rng = np.random.default_rng(0)
    sample = lambda table: {name: rng.uniform(low, high) for name, (_, low, high, *_) in table.items()}
    kmax = dynamics_limits(k_bar)
    left, right, _, _ = output_limits(k_bar, k_golden, k_planner)
    for _ in range(200):
        c = sample(DYNAMICS)
        if k_bar(c["alpha"], *_per_generation(c["beta_year"], c["growth_year"])) > kmax:
            failures.append(f"olg: the dynamics panel's axes miss {c}")
        c = sample(OUTPUT)
        beta, Xi = _per_generation(c["beta_year"], c["growth_year"])
        points = (k_bar(c["alpha"], beta, Xi), k_golden(c["alpha"], Xi - 1), k_planner(c["alpha"], Xi, c["beth_year"] ** YEARS))
        if min(points) < left or max(points) > right:
            failures.append(f"olg: the output panel's axes miss {c}")
    failures += slider_check.check("olg dynamics", sliders_dynamics, k_next, k_bar)
    failures += slider_check.check("olg output", sliders_output, k_bar, k_golden, k_planner, interest_factor)
    failures += slider_check.check("olg transition", sliders_transition, k_next, k_bar, wage, interest_factor)
    failures += slider_check.check("olg Social Security", sliders_payg, k_next, k_bar, wage, payg, steady, payg, steady)
    return failures
