"""The Investment Notes chapter's figures and sliders, kept out of its notebook.

The notebook, content/investment/InvestmentNotes/InvestmentNotes.ipynb, shows the economics:
Samuelson's multiplier-accelerator model, the conditions under which its output cycles and
converges, and the growth of real GDP, consumption and investment in the national accounts. It
passes those here, and this module only draws.

The slider panel redraws on fixed axes: the map of the four regimes is the whole (v, c) plane the
sliders cover, and output is drawn relative to the long-run effect of the change, on a frame that
paths which explode leave.

`python -m intertemporal_choice --self-test` runs `self_test`.
"""

import numpy as np

from intertemporal_choice import slider_check

READOUT = dict(facecolor="white", edgecolor="none", alpha=0.85)  # a readout stays legible over a line
V_MAX = 4.0  # the accelerator v on the regime map
FRAME = (-2.0, 4.0)  # output relative to the long-run effect of the change

# The sliders: name -> (first value, lowest, highest, step, label, readout format).
SAMUELSON = {
    "c": (0.6, 0.2, 0.95, 0.01, "marginal propensity to consume c", ".2f"),
    "v": (1.0, 0.0, 4.0, 0.05, "accelerator v", ".2f"),
}

_DOTS = "".join(f"{10 * i}%{{content:'{'.' * i}'}}" for i in range(10))
BUSY = ("<style>.ic-busy{opacity:0;animation:ic-show 0s .5s forwards}"
        ".ic-busy::after{content:'';animation:ic-dots 10s step-end .5s infinite}"
        f"@keyframes ic-show{{to{{opacity:1}}}}@keyframes ic-dots{{{_DOTS}}}</style>"
        "<span class='ic-busy'>drawing</span>")


def draw_regimes(ax, cycles, stable, point=None, examples=()):
    """The (v, c) plane divided by the two conditions: output cycles below the curve
    c(1+v)^2 = 4v and converges below cv = 1, the four regimes shaded: blues converge and oranges
    explode, and of each pair the one below the solid curve cycles. `examples`, (c, v) pairs, are marked and numbered, one in each regime;
    `point`, from the sliders, is marked alone."""
    v = np.linspace(0, V_MAX, 600)[1:]
    c = np.linspace(0, 1, 400)
    V, C = np.meshgrid(v, c)
    regime = np.where(stable(C, V), np.where(cycles(C, V), 1, 0), np.where(cycles(C, V), 2, 3))
    ax.contourf(V, C, regime, levels=[-0.5, 0.5, 1.5, 2.5, 3.5], colors=["#e8f1fa", "#cfe3f3", "#f9dccc", "#f3c1a8"])
    ax.plot(v, np.minimum(4 * v / (1 + v) ** 2, 1), color="black", lw=1.0)
    ax.plot(v, np.minimum(1 / v, 1), color="black", lw=1.0, linestyle="--")
    for i, (ce, ve) in enumerate(examples, 1):
        ax.plot([ve], [ce], "o", color="black", ms=4)
        ax.annotate(str(i), (ve, ce), xytext=(4, 3), textcoords="offset points", fontsize=8)
    if point is not None:
        ax.plot([point[1]], [point[0]], "o", color="C3", ms=6)
    ax.set_xlim(0, V_MAX)
    ax.set_ylim(0, 1)
    ax.set_xlabel("accelerator $v$", loc="right")
    ax.set_ylabel("$c$", loc="top", rotation=0)
    ax.text(0.97, 0.03, "solid: $c(1+v)^2 = 4v$\ndashed: $cv = 1$", transform=ax.transAxes, ha="right", fontsize=8, bbox=READOUT)


def draw_path(ax, t, relative, label=None, frame=FRAME):
    """Output relative to the long-run effect of the change: 0 before it, 1 in the new steady
    state. A path that explodes leaves the frame."""
    ax.axhline(0, color="0.6", lw=0.8)
    ax.axhline(1, color="0.6", lw=0.8, linestyle="--")
    ax.plot(t, np.clip(relative, frame[0] - 1, frame[1] + 1), ".-", color="C0", lw=1.2, ms=3)
    ax.set_ylim(*frame)
    ax.set_xlim(t[0], t[-1])
    if label:
        ax.set_title(label, fontsize=9)
    ax.set_xlabel("$t$", loc="right")


def draw_volatility(ax, growth, recessions):
    """Four-quarter growth rates, in percent, with recessions shaded. `growth` maps a name to a
    series indexed by quarter; `recessions` is a 0/1 series by quarter."""
    first = max(series.dropna().index[0] for series in growth.values())
    shown = recessions[recessions.index >= first]
    starts = shown.index[(shown == 1) & (shown.shift(1, fill_value=0) == 0)]
    ends = shown.index[(shown == 1) & (shown.shift(-1, fill_value=0) == 0)]
    for a, b in zip(starts, ends):
        ax.axvspan(a, b, color="0.88", lw=0)
    styles = {0: dict(color="C3", lw=1.2), 1: dict(color="black", lw=1.4), 2: dict(color="C0", lw=1.0, linestyle="--")}
    for i, (name, series) in enumerate(growth.items()):
        ax.plot(series.index, series.values, label=name, **styles[i % 3])
    ax.axhline(0, color="0.5", lw=0.6)
    ax.set_xlim(first, max(series.index[-1] for series in growth.values()))
    ax.set_ylabel("percent", loc="top", rotation=0)
    ax.legend(loc="upper right", fontsize=8, ncol=len(growth))


def _look(widgets, labels):
    label = 0.55 * max(len(text) for text in labels) + 1
    return {"style": {"description_width": f"{label:.1f}em"}, "layout": widgets.Layout(width=f"{label + 25:.1f}em")}


def sliders_samuelson(path, cycles, stable, table=SAMUELSON):
    """Sliders for the marginal propensity to consume and the accelerator: where they sit on the map
    of regimes, and the path of output after government spending rises."""
    import ipywidgets as widgets
    import matplotlib.pyplot as plt
    from IPython.display import display

    look = _look(widgets, [row[4] for row in table.values()])
    controls = {name: widgets.FloatSlider(value=value, min=low, max=high, step=step, description=label,
                                          readout_format=fmt, **look)
                for name, (value, low, high, step, label, fmt) in table.items()}
    status = widgets.HTML(layout=widgets.Layout(height="1.5em"))

    def explore(c, v):
        status.value = BUSY
        try:
            fig, (left, right) = plt.subplots(1, 2, figsize=(9.0, 3.8))
            draw_regimes(left, cycles, stable, point=(c, v))
            t, relative = path(c, v)
            draw_path(right, t, relative)
            kind = ("cycles" if cycles(c, v) else "no cycles") + (", converges" if stable(c, v) else ", explodes")
            right.text(0.97, 0.97, f"c = {c:.2f}, v = {v:.2f}: {kind}\ncv = {c * v:.2f}", transform=right.transAxes,
                       ha="right", va="top", fontsize=9, bbox=READOUT)
            fig.tight_layout()
            plt.show()
        finally:
            status.value = ""

    display(widgets.VBox([*controls.values(), status, widgets.interactive_output(explore, controls)]))


def self_test() -> list[str]:
    import matplotlib.pyplot as plt

    failures = []
    cycles = lambda c, v: c * (1 + v) ** 2 < 4 * v
    stable = lambda c, v: c * v < 1

    def path(c, v, periods=30, change=0.1):
        Y = np.full(periods + 2, 1 / (1 - c))
        for t in range(2, periods + 2):
            Y[t] = 1 + change + c * (1 + v) * Y[t - 1] - c * v * Y[t - 2]
        old, new = 1 / (1 - c), (1 + change) / (1 - c)
        return np.arange(-1, periods), (Y[1:] - old) / (new - old)

    # each example lands in its regime
    for (c, v), want in {(0.5, 0.1): (False, True), (0.5, 1.5): (True, True), (0.8, 2.0): (True, False), (0.9, 4.0): (False, False)}.items():
        if (bool(cycles(c, v)), bool(stable(c, v))) != want:
            failures.append(f"accelerator: ({c}, {v}) is not in its regime")
    t, r = path(0.5, 0.1)
    if not abs(r[-1] - 1) < 1e-6:
        failures.append("accelerator: a stable path does not reach the new steady state")
    fig, (a, b) = plt.subplots(1, 2)
    try:
        draw_regimes(a, cycles, stable, examples=[(0.5, 0.1)])
        draw_path(b, t, r)
    except Exception as e:  # noqa: BLE001
        failures.append(f"accelerator: drawing failed: {e!r}")
    plt.close("all")
    failures += slider_check.check("accelerator", sliders_samuelson, path, cycles, stable)
    return failures
