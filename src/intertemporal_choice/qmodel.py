"""The q model chapter's figures and sliders, kept out of its notebook.

The notebook, content/investment/qModel/qModel.ipynb, shows the economics: the chapter's first
order condition, envelope condition and accumulation equation, the steady state, and the locus
where the marginal value of capital is constant (with the chapter's approximation, which sets aside
the effect of capital on the costs of adjustment), all in `q_model`, which returns them for given
values of the interest rate and the depreciation rate. It passes that model here. This module
solves the stacked equations of a perfect-foresight path by Newton's method, which is numerics
rather than economics, and draws.

An experiment is a change announced at date 0 that takes effect at date n: from n on, productivity,
the share of revenue left after the corporate tax, or the after-ITC price of capital takes its new
value. An unexpected change that takes effect at once has n = 0. The chapter's timing puts investment made at t into the capital of t+1 and has it paid for at
t+1's price, so an ITC that takes effect at n applies first to the investment made at n-1.

Capital is drawn relative to the steady state before the change, k/k̄, so that pictures with
different parameters share axes. Every slider panel redraws on fixed axes, the largest any
combination of its sliders' values needs (Chris, 2026-10-26), found by solving every combination of
the ends of the sliders' ranges when the panel opens.

`python -m intertemporal_choice --self-test` runs `self_test`.
"""

import itertools
from types import SimpleNamespace

import numpy as np

from intertemporal_choice import slider_check

READOUT = dict(facecolor="white", edgecolor="none", alpha=0.85)  # a readout stays legible over a line
SHOWN = 30  # periods after the announcement in the pictures by period
BEFORE = 3  # and before it
PERIODS = 100  # periods solved: the economy is back in a steady state long before the last
OLD, NEW, PATH = "0.55", "C3", "C0"  # colors: the economy before the change, after it, and its path

# The sliders, by panel: name -> (first value, lowest, highest, step, label, readout format).
PHASE = {
    "omega": (2.0, 0.5, 6.0, 0.25, "adjustment cost ω", ".2f"),
    "rate": (0.04, 0.02, 0.08, 0.005, "interest rate r", ".3f"),
    "delta": (0.10, 0.05, 0.15, 0.01, "depreciation rate δ", ".2f"),
}
PRODUCTIVITY = {
    "size": (1.10, 1.02, 1.20, 0.01, "productivity, new over old", ".2f"),
    "lead": (5, 0, 10, 1, "periods until it takes effect, n", ""),
    "omega": (2.0, 0.5, 6.0, 0.25, "adjustment cost ω", ".2f"),
}
CORPORATE_TAX = {
    "size": (0.20, 0.10, 0.28, 0.01, "new corporate tax rate (old 0.30)", ".2f"),
    "lead": (5, 0, 10, 1, "periods until it takes effect, n", ""),
    "omega": (2.0, 0.5, 6.0, 0.25, "adjustment cost ω", ".2f"),
}
ITC = {
    "size": (0.10, 0.02, 0.20, 0.01, "new investment tax credit (old 0)", ".2f"),
    "lead": (5, 0, 10, 1, "periods until it takes effect, n", ""),
    "omega": (2.0, 0.5, 6.0, 0.25, "adjustment cost ω", ".2f"),
}

# While a picture is being drawn, "drawing" and a dot a second appear above it, after half a second,
# as in the OLG chapter's panels.
_DOTS = "".join(f"{10 * i}%{{content:'{'.' * i}'}}" for i in range(10))
BUSY = ("<style>.ic-busy{opacity:0;animation:ic-show 0s .5s forwards}"
        ".ic-busy::after{content:'';animation:ic-dots 10s step-end .5s infinite}"
        f"@keyframes ic-show{{to{{opacity:1}}}}@keyframes ic-dots{{{_DOTS}}}</style>"
        "<span class='ic-busy'>drawing</span>")


def newton(residuals, guess, tol=1e-11, max_iter=60):
    """Solve residuals(x) = 0 from `guess` by Newton's method, with a Jacobian by forward
    differences and a step halved until it reduces the residuals. Raises if it does not converge."""
    x = np.asarray(guess, float).copy()
    r = residuals(x)
    for _ in range(max_iter):
        size = np.max(np.abs(r))
        if size < tol:
            return x
        h = 1e-7 * np.maximum(1.0, np.abs(x))
        jacobian = np.empty((r.size, x.size))
        for j in range(x.size):
            step = x.copy()
            step[j] += h[j]
            jacobian[:, j] = (residuals(step) - r) / h[j]
        move = np.linalg.solve(jacobian, -r)
        shrink = 1.0
        while True:
            trial = x + shrink * move
            with np.errstate(invalid="ignore", divide="ignore"):
                r_trial = residuals(trial)
            if (np.all(np.isfinite(r_trial)) and np.max(np.abs(r_trial)) < size) or shrink < 1e-4:
                break
            shrink /= 2
        x, r = trial, r_trial
    raise RuntimeError(f"Newton's method did not converge: largest residual {np.max(np.abs(r)):.2e}")


def _paths(before, after, lead, length):
    """Productivity, the after-tax share and the after-ITC price, period by period from the
    announcement: each at its old value before `lead` and at its new one from then on."""
    t = np.arange(length)
    return {name: np.where(t >= lead, after[name], before[name]) for name in before}


def solve(model, before, after, lead, omega):
    """The perfect-foresight path after a change announced at 0 and effective from `lead`, starting
    in the steady state before the change. Returns t, and by period capital relative to the old
    steady state, lambda, q and iota, with BEFORE periods of the old steady state first (t < 0)."""
    lead = int(round(lead))
    k0, lam0 = model.steady_state(before["tax_free"], before["P"], before["A"])
    k1, lam1 = model.steady_state(after["tax_free"], after["P"], after["A"])
    paths = _paths(before, after, lead, PERIODS + 1)
    equations = lambda x: model.residuals(x, k0, paths["tax_free"], paths["P"], paths["A"], omega)
    guess = np.concatenate([np.linspace(lam0, lam1, PERIODS + 1), np.linspace(k0, k1, PERIODS + 1)[1:]])
    x = newton(equations, guess)
    lam, k = x[:PERIODS + 1], np.concatenate([[k0], x[PERIODS + 1:]])
    iota = np.append(model.iota(lam[1:], paths["P"][1:], omega), 0.0)
    old = np.ones(BEFORE)
    return {"t": np.arange(-BEFORE, PERIODS + 1), "k": np.concatenate([old, k / k0]), "k0": k0,
            "lambda": np.concatenate([lam0 * old, lam]), "q": np.concatenate([old * lam0 / before["P"], lam / paths["P"]]),
            "iota": np.concatenate([0 * old, iota]), "lead": lead}


def saddle_path(model, values, omega, low=0.5, high=1.6):
    """Points (k, lambda) on the saddle path with the parameters `values`: the solved paths from
    capital `low` and `high` times the steady state, which lie on it."""
    kbar, lam = model.steady_state(values["tax_free"], values["P"], values["A"])
    paths = _paths(values, values, 0, PERIODS + 1)
    ks, ls = [], []
    for start in (low, high):
        equations = lambda x, k0=start * kbar: model.residuals(x, k0, paths["tax_free"], paths["P"], paths["A"], omega)
        guess = np.concatenate([np.full(PERIODS + 1, lam), np.linspace(start * kbar, kbar, PERIODS + 1)[1:]])
        x = newton(equations, guess)
        ks.append(np.concatenate([[start * kbar], x[PERIODS + 1:]]))
        ls.append(x[:PERIODS + 1])
    k, lam = np.concatenate(ks), np.concatenate(ls)
    order = np.argsort(k)
    return k[order], lam[order]


def _motion(ax, model, values, omega, unit, kbar, frame):
    """Arrows of motion, one pair in each of the four regions the loci divide the frame into: above
    the line where capital is constant it grows, and above the locus where lambda is constant
    lambda rises."""
    (k_lo, k_hi), (y_lo, y_hi) = frame
    level = model.steady_state(values["tax_free"], values["P"], values["A"])[1] / unit
    dx, dy = 0.06 * (k_hi - k_lo), 0.06 * (y_hi - y_lo)
    for side in (-1, 1):
        x = 1 + 0.55 * side * (k_hi - 1 if side > 0 else 1 - k_lo)
        locus = float(model.stationary(np.array([x * kbar]), values["tax_free"], values["P"], values["A"], omega)[0]) / unit
        between = (locus + level) / 2  # between the two loci
        outside = (y_hi - 0.12 * (y_hi - y_lo)) if side > 0 else (y_lo + 0.12 * (y_hi - y_lo))  # beyond both
        for y in (between, outside):
            grows = y > level
            rises = y > locus
            for ddx, ddy in ((dx if grows else -dx, 0), (0, dy if rises else -dy)):
                ax.annotate("", xy=(x + ddx, y + ddy), xytext=(x, y), arrowprops=dict(arrowstyle="->", lw=0.8, color="0.35"))


def draw_phase(ax, model, values, omega, scale="lambda", frame=None):
    """The phase diagram in (k, lambda), or with scale="q" in (k, q): the locus where the marginal
    value of capital is constant, the line where capital is (lambda at the price of capital, q at
    one), the saddle path and arrows of motion. k is relative to the steady state; `frame`, from the
    sliders, fixes the axes."""
    kbar, lam_bar = model.steady_state(values["tax_free"], values["P"], values["A"])
    unit = values["P"] if scale == "q" else 1.0
    ks, ls = saddle_path(model, values, omega)
    if frame is None:
        frame = ((0.5, 1.6), (0.75 * lam_bar / unit, 1.4 * lam_bar / unit))
    (k_lo, k_hi), (y_lo, y_hi) = frame
    k = np.linspace(k_lo, k_hi, 400) * kbar
    with np.errstate(invalid="ignore"):
        locus = model.stationary(k, values["tax_free"], values["P"], values["A"], omega) / unit
    name = "q" if scale == "q" else r"\lambda"
    ax.plot(k / kbar, locus, color="black", lw=1.6)
    ax.axhline(lam_bar / unit, color="black", lw=1.0, linestyle="--")
    ax.plot(ks / kbar, ls / unit, color=NEW, lw=1.8)
    ax.plot([1], [lam_bar / unit], "o", color="black", ms=4)
    _motion(ax, model, values, omega, unit, kbar, frame)
    x = k_lo + 0.22 * (k_hi - k_lo)  # upper left, where the locus is above the saddle path
    y = float(model.stationary(np.array([x * kbar]), values["tax_free"], values["P"], values["A"], omega)[0]) / unit
    ax.annotate(rf"$\Delta {name} = 0$", (x, min(y, y_hi)), xytext=(8, 0), textcoords="offset points", fontsize=9)
    ax.annotate(r"$\Delta k = 0$", (k_hi, lam_bar / unit), xytext=(-40, 4), textcoords="offset points", fontsize=9)
    x = k_lo + 0.8 * (k_hi - k_lo)  # lower right, where the saddle path is above the locus
    ax.annotate("saddle path", (x, float(np.interp(x * kbar, ks, ls)) / unit), xytext=(0, 8),
                textcoords="offset points", fontsize=9, color=NEW)
    ax.set_xlim(k_lo, k_hi)
    ax.set_ylim(y_lo, y_hi)
    ax.set_xlabel(r"$k/\bar{k}$", loc="right")
    ax.set_ylabel(rf"${name}$", loc="top", rotation=0)


def draw_experiment(axes, model, before, after, lead, omega, frames=None):
    """An experiment, in four panels: the phase diagram in (k, lambda), with the loci (light gray
    before the change, black after it) and the saddle paths (gray and dashed before, red after), and
    the path the economy takes (dots, one a period); and by period, the net investment rate, lambda
    and q, and capital. `frames`, from the sliders, fixes all four; without it the phase diagram
    frames the two steady states and the path between them."""
    phase, inv, values, capital = axes
    path = solve(model, before, after, lead, omega)
    k0 = path["k0"]
    k_new = model.steady_state(after["tax_free"], after["P"], after["A"])[0] / k0
    k = np.linspace(0.5, 1.8, 400) * k0
    for v, old in ((before, True), (after, False)):
        lam_bar = model.steady_state(v["tax_free"], v["P"], v["A"])[1]
        color = "0.75" if old else "black"
        phase.plot(k / k0, model.stationary(k, v["tax_free"], v["P"], v["A"], omega), color=color, lw=1.0)
        phase.axhline(lam_bar, color=color, lw=0.9, linestyle="--")
        ks, ls = saddle_path(model, v, omega)
        phase.plot(ks / k0, ls, color=OLD if old else NEW, lw=1.6, linestyle="--" if old else "-")
    shown = (path["t"] >= 0) & (path["t"] <= SHOWN)
    phase.plot(path["k"][shown], path["lambda"][shown], ".", color=PATH, ms=4)
    phase.plot([1], [path["lambda"][0]], "o", color="black", ms=4)
    phase.annotate("before", (1, path["lambda"][0]), xytext=(4, 4), textcoords="offset points", fontsize=8)
    phase.set_xlabel(r"$k/\bar{k}$", loc="right")
    phase.set_ylabel(r"$\lambda$", loc="top", rotation=0)
    window = path["t"] <= SHOWN
    t = path["t"][window]
    inv.axhline(0, color=OLD, lw=0.8)
    inv.plot(t, path["iota"][window], ".-", color=PATH, lw=1.2, ms=4)
    inv.set_ylabel(r"$\iota_{t}$", loc="top", rotation=0)
    values.plot(t, path["lambda"][window], ".-", color=PATH, lw=1.2, ms=4, label=r"$\lambda_{t}$")
    values.plot(t, path["q"][window], color="C1", lw=1.2, linestyle="--", label=r"$q_{t}$")
    values.legend(loc="best", fontsize=8)
    capital.plot(t, path["k"][window], ".-", color=PATH, lw=1.2, ms=4)
    capital.set_ylabel(r"$k_{t}/\bar{k}$", loc="top", rotation=0)
    for ax in (inv, values, capital):
        ax.axvline(0, color=OLD, lw=0.6, linestyle=":")
        if path["lead"] > 0:
            ax.axvline(path["lead"], color=OLD, lw=0.6, linestyle=":")
        ax.set_xlabel(r"$t$", loc="right")
        ax.set_xlim(-BEFORE, SHOWN)
    if frames is None:  # around the old and new steady states and the path between them
        left, right = 0.8, max(1.3, 1.12 * k_new)
        near = path["lambda"][(path["k"] >= left) & (path["k"] <= right)]
        lam_new = model.steady_state(after["tax_free"], after["P"], after["A"])[1]
        frames = [((left, right), _pad(min(np.min(near), lam_new, 1.0), max(np.max(near), lam_new, 1.0), 0.6))]
        phase.set_xlim(*frames[0][0])
        phase.set_ylim(*frames[0][1])
    else:
        phase.set_xlim(*frames[0][0])
        phase.set_ylim(*frames[0][1])
        for ax, (low, high) in zip((inv, values, capital), frames[1:]):
            ax.set_ylim(low, high)
    return path


def _corners(table):
    names = list(table)
    return [dict(zip(names, values)) for values in itertools.product(*(table[name][1:3] for name in names))]


def _pad(low, high, share=0.08):
    spare = share * (high - low) or 0.01
    return low - spare, high + spare


def experiment_frames(model, before, change, table):
    """Frames that hold every combination of the ends of a panel's sliders: for the phase diagram,
    (capital, lambda); for the three pictures by period, (lowest, highest)."""
    k_hi, lams, lows, highs = 1.0, [], [np.inf] * 3, [-np.inf] * 3
    for corner in _corners(table):
        after = change(before, corner["size"])
        path = solve(model, before, after, corner["lead"], corner["omega"])
        window = path["t"] <= SHOWN
        for i, series in enumerate((path["iota"][window], np.concatenate([path["lambda"][window], path["q"][window]]),
                                    path["k"][window])):
            lows[i], highs[i] = min(lows[i], float(np.min(series))), max(highs[i], float(np.max(series)))
        k_hi = max(k_hi, float(np.max(path["k"])))
        lams += [float(np.min(path["lambda"])), float(np.max(path["lambda"]))]
    phase = ((0.8, max(1.3, 1.08 * k_hi)), _pad(min(lams), max(lams), 0.4))
    return [phase] + [_pad(lo, hi) for lo, hi in zip(lows, highs)]


def phase_frame(model_with, values, table=PHASE):
    """The (k, q) frame that holds the saddle path of every combination of the ends of the sliders."""
    low, high = np.inf, -np.inf
    for corner in _corners(table):
        model = model_with(corner["rate"], corner["delta"])
        ks, ls = saddle_path(model, values, corner["omega"])
        low, high = min(low, float(np.min(ls)) / values["P"]), max(high, float(np.max(ls)) / values["P"])
    return (0.5, 1.6), _pad(low, high)


def _look(widgets, labels):
    """One label width for all of a panel's sliders, set by its longest label, and a track beside it."""
    label = 0.55 * max(len(text) for text in labels) + 1
    return {"style": {"description_width": f"{label:.1f}em"}, "layout": widgets.Layout(width=f"{label + 25:.1f}em")}


def _controls(widgets, table):
    """The panel's sliders; n, the number of periods, moves in whole periods."""
    look = _look(widgets, [row[4] for row in table.values()])
    controls = {}
    for name, (value, low, high, step, label, fmt) in table.items():
        if name == "lead":
            controls[name] = widgets.IntSlider(value=value, min=low, max=high, step=step, description=label, **look)
        else:
            controls[name] = widgets.FloatSlider(value=value, min=low, max=high, step=step, description=label,
                                                 readout_format=fmt, **look)
    return controls


def _panel(widgets, explore, controls):
    """Show the sliders, the note that appears while a picture takes long to draw, and the picture.
    The note's line has a fixed height, so it does not move the picture."""
    from IPython.display import display

    status = widgets.HTML(layout=widgets.Layout(height="1.5em"))

    def draw(**values):
        status.value = BUSY
        try:
            explore(**values)
        finally:
            status.value = ""

    display(widgets.VBox([*controls.values(), status, widgets.interactive_output(draw, controls)]))


def sliders_phase(model_with, values, table=PHASE):
    """Sliders for the cost of adjustment, the interest rate and the depreciation rate: the phase
    diagram in (k, q), with its saddle path. `model_with(rate, delta)` is the notebook's model."""
    import ipywidgets as widgets
    import matplotlib.pyplot as plt

    frame = phase_frame(model_with, values, table)

    def explore(omega, rate, delta):
        fig, ax = plt.subplots(figsize=(6.4, 4.6))
        draw_phase(ax, model_with(rate, delta), values, omega, scale="q", frame=frame)
        ax.text(0.03, 0.97, f"ω = {omega:.2f}, r = {rate:.3f}, δ = {delta:.2f}", transform=ax.transAxes,
                va="top", fontsize=9, bbox=READOUT)
        plt.show()

    _panel(widgets, explore, _controls(widgets, table))


def sliders_experiment(model, before, change, table, what):
    """Sliders for the size of a change, how many periods after its announcement it takes effect,
    and the cost of adjustment: the experiment's four panels, on frames that hold every combination.
    `change(before, size)` is the parameters after the change."""
    import ipywidgets as widgets
    import matplotlib.pyplot as plt

    frames = experiment_frames(model, before, change, table)

    def explore(size, lead, omega):
        fig, axes = plt.subplots(2, 2, figsize=(7.2, 6.0))
        path = draw_experiment(axes.ravel(), model, before, change(before, size), lead, omega, frames)
        n = path["lead"]
        later = f" and {path['iota'][BEFORE + n - 1]:+.3f} at {n - 1}" if n > 1 else ""
        fig.suptitle(f"{what}, announced at 0 and in effect from {n}: the net investment rate ι is "
                     f"{path['iota'][BEFORE]:+.3f} at 0{later}", fontsize=9)
        fig.tight_layout()
        plt.show()

    _panel(widgets, explore, _controls(widgets, table))


def self_test() -> list[str]:
    import matplotlib.pyplot as plt

    failures = []

    def model_with(rate=0.04, delta=0.10, alpha=0.30):
        """The chapter's model, as the notebook writes it."""
        beta = 1 / (1 + rate)

        def iota(lam_next, P_next, omega):
            return (lam_next / P_next - 1) / omega

        def steady_state(tax_free, P, A):
            return (P * (1 - beta * (1 - delta)) / (tax_free * A * alpha)) ** (1 / (alpha - 1)), P

        def residuals(x, k0, tax_free, P, A, omega):
            T = len(P) - 1
            lam, k = x[:T + 1], np.concatenate([[k0], x[T + 1:]])
            i = iota(lam[1:], P[1:], omega)
            accumulation = k[1:] - (1 + i) * k[:-1]
            envelope = lam[:-1] - (tax_free[:-1] * A[:-1] * alpha * k[:-1] ** (alpha - 1)
                                   + omega * (i**2 / 2 + i * delta) * P[1:] * beta + beta * (1 - delta) * lam[1:])
            return np.concatenate([accumulation, envelope, [lam[-1] - steady_state(tax_free[-1], P[-1], A[-1])[1]]])

        def stationary(k, tax_free, P, A, omega):
            return tax_free * A * alpha * k ** (alpha - 1) / (1 - beta * (1 - delta))

        return SimpleNamespace(iota=iota, steady_state=steady_state, residuals=residuals, stationary=stationary)

    model = model_with()
    before = {"tax_free": 0.7, "P": 1.0, "A": 1.0}
    # the review's table (2026-10-31): an ITC from 0 to 10 percent, effective at t = 5
    path = solve(model, before, {**before, "P": 0.9}, 5, 2.0)
    iota = path["iota"][BEFORE:BEFORE + 6]
    expected = [-0.0072, -0.0079, -0.0090, -0.0106, +0.0352, +0.0284]
    if not np.allclose(iota, expected, atol=2e-4):
        failures.append(f"qmodel: the future ITC's investment rates are {np.round(iota, 4)}, not {expected}")
    if not abs(path["lambda"][BEFORE] - 0.9861) < 2e-4:
        failures.append(f"qmodel: lambda at the ITC's announcement is {path['lambda'][BEFORE]:.4f}, not 0.9861")
    path = solve(model, before, {**before, "A": 1.1}, 5, 2.0)
    if not (np.all(np.diff(path["iota"][BEFORE:BEFORE + 5]) > 0) and path["lambda"][BEFORE] > 1):
        failures.append("qmodel: a future productivity increase does not raise lambda and investment until it arrives")
    ks, ls = saddle_path(model, before, 2.0)
    kbar, lam_bar = model.steady_state(0.7, 1.0, 1.0)
    if not (abs(np.interp(kbar, ks, ls) - lam_bar) < 1e-3 and np.all(np.diff(ls) < 1e-9)):  # down, up to rounding at the steady state
        failures.append("qmodel: the saddle path does not slope down through the steady state")
    if not abs(model.stationary(np.array([kbar]), 0.7, 1.0, 1.0, 2.0)[0] - lam_bar) < 1e-10:
        failures.append("qmodel: the locus where lambda is constant misses the steady state")
    fig, axes = plt.subplots(2, 2)
    try:
        draw_experiment(axes.ravel(), model, before, {**before, "P": 0.9}, 5, 2.0)
    except Exception as e:  # noqa: BLE001
        failures.append(f"qmodel: draw_experiment failed: {e!r}")
    fig2, ax = plt.subplots()
    try:
        draw_phase(ax, model, before, 2.0, scale="q")
    except Exception as e:  # noqa: BLE001
        failures.append(f"qmodel: draw_phase failed: {e!r}")
    plt.close("all")
    import ipywidgets as widgets

    if _controls(widgets, ITC)["lead"].step != 1:
        failures.append("qmodel: the lead slider does not move in whole periods")
    failures += slider_check.check("qmodel ITC", sliders_experiment, model, before,
                                   lambda b, size: {**b, "P": 1 - size}, ITC, "an ITC")
    failures += slider_check.check("qmodel productivity", sliders_experiment, model, before,
                                   lambda b, size: {**b, "A": size}, PRODUCTIVITY, "productivity")
    failures += slider_check.check("qmodel corporate tax", sliders_experiment, model, before,
                                   lambda b, size: {**b, "tax_free": 1 - size}, CORPORATE_TAX, "a tax cut")
    failures += slider_check.check("qmodel phase", sliders_phase, model_with, before)
    return failures
