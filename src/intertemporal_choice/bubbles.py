"""The bubbles chapter's figures and sliders, kept out of its notebook.

The notebook, content/asset_pricing/Bubbles/Bubbles.ipynb, shows the economics: Blanchard's rule
for a bubble that bursts at random, the simulation of many such bubbles, and, for Tirole's bubble in
an overlapping generations economy, the OLG chapter's accumulation of capital with and without a
bubble and the golden rule. It passes those here, and this module only draws.

Every slider panel redraws on fixed axes, the largest any combination of its sliders' values needs
(Chris, 2026-10-26), found at the ends of the sliders' ranges, since each quantity drawn is monotone
in each parameter. The simulated bubbles use a fixed seed, so a redraw with the same values draws
the same bubbles.

`python -m intertemporal_choice --self-test` runs `self_test`.
"""

import itertools

import numpy as np

from intertemporal_choice import slider_check

READOUT = dict(facecolor="white", edgecolor="none", alpha=0.85)  # a readout stays legible over a line
YEARS = 36  # a generation, as in the OLG chapter
PERIODS = 40  # periods of the sample paths
LONGEST = 120  # the lifetimes drawn, in periods

# The sliders, by panel: name -> (first value, lowest, highest, step, label, readout format).
BURSTING = {
    "D": (0.05, 0.02, 0.10, 0.005, "probability of bursting each period", ".3f"),
    "R": (1.04, 1.02, 1.06, 0.005, "interest factor R", ".3f"),
}
TIROLE = {
    "alpha": (0.20, 0.15, 0.30, 0.01, "capital share α", ".2f"),
    "beta_year": (0.999, 0.98, 0.999, 0.001, "β per year", ".3f"),
    "growth_year": (0.04, 0.02, 0.04, 0.001, "population growth per year", ".3f"),
}

_DOTS = "".join(f"{10 * i}%{{content:'{'.' * i}'}}" for i in range(10))
BUSY = ("<style>.ic-busy{opacity:0;animation:ic-show 0s .5s forwards}"
        ".ic-busy::after{content:'';animation:ic-dots 10s step-end .5s infinite}"
        f"@keyframes ic-show{{to{{opacity:1}}}}@keyframes ic-dots{{{_DOTS}}}</style>"
        "<span class='ic-busy'>drawing</span>")


def draw_paths(ax, paths, expected, top=None):
    """Sample bubbles relative to their starting size, on a log scale. While they last they all grow
    alike, by R/(1-D) a period, so they share one line; an x marks the last period a bubble was
    alive (with a count when several burst together), after which it is zero, off a log scale. The expected value (dashed) grows by R."""
    t = np.arange(paths.shape[0])
    alive = paths > 0
    longest = int(alive.all(axis=0).any()) * len(t) or int(np.max(np.argmin(alive, axis=0)))
    growth = paths[1, 0] / paths[0, 0] if paths[1, 0] > 0 else None
    ax.plot(t, np.max(paths, axis=1) if longest == len(t) else np.where(t < longest, np.max(paths, axis=1), np.nan),
            color="C0", lw=1.6, label="while it lasts")
    ends = [int(np.argmin(alive[:, j])) - 1 for j in range(paths.shape[1]) if not alive[:, j].all()]  # last period alive
    for end in sorted(set(ends)):
        value = float(np.max(paths[end]))
        ax.plot([end, end], [value, 0.8], color="C3", lw=0.6, linestyle=":")
        ax.plot([end], [value], "x", color="C3", ms=6, mew=1.4)
        if ends.count(end) > 1:  # several burst together
            ax.annotate(f"{ends.count(end)}", (end, value), xytext=(-4, 6), textcoords="offset points", fontsize=8, color="C3")
    burst = len(ends)
    ax.plot(t, expected, color="black", lw=1.6, linestyle="--", label="expected value")
    ax.set_yscale("log")
    ax.set_ylim(0.8, top if top is not None else 1.5 * float(np.max(paths)))
    ax.set_xlim(0, t[-1])
    ax.text(0.97, 0.05, f"{burst} of {paths.shape[1]} bubbles burst (x) by period {t[-1]}", transform=ax.transAxes,
            ha="right", fontsize=9, bbox=READOUT)
    ax.set_xlabel(r"$t$", loc="right")
    ax.set_ylabel(r"$B_{t}/B_{0}$", loc="top", rotation=0)
    ax.legend(loc="upper left", fontsize=8)


def draw_lifetimes(ax, lifetimes, D, top=None):
    """The share of bubbles that burst in each period, against the geometric distribution, with the
    expected lifetime and the half-life of survival marked."""
    counts = np.bincount(np.minimum(lifetimes, LONGEST + 1), minlength=LONGEST + 2)[1:LONGEST + 1] / len(lifetimes)
    s = np.arange(1, LONGEST + 1)
    ax.bar(s, counts, width=1.0, color="C0", alpha=0.45, label="simulated")
    ax.plot(s, D * (1 - D) ** (s - 1), color="black", lw=1.2, label="geometric")
    mean, half = 1 / D, np.log(2) / -np.log(1 - D)
    ax.axvline(half, color="C1", lw=1.0, linestyle="--", label=f"half-life {half:.1f}")
    ax.axvline(mean, color="C3", lw=1.0, linestyle=":", label=f"expected lifetime {mean:.1f}")
    ax.set_xlim(0, LONGEST)
    if top is not None:
        ax.set_ylim(0, top)
    ax.set_xlabel("periods until it bursts", loc="right")
    ax.set_ylabel("share", loc="top", rotation=0)
    ax.legend(loc="upper right", fontsize=8)


def draw_tirole(ax, k_next, k_bar, k_golden, alpha, beta, Xi, kmax=None):
    """Tirole's bubble in the OLG chapter's economy: the accumulation curve and the 45-degree line,
    the steady state with no bubble, k̄, and the golden rule, k**, where the interest factor equals
    the growth factor of the population. When k̄ exceeds k**, the economy is dynamically inefficient
    and a bubble can last: in its steady state capital is at the golden rule, and the bubble takes
    the savings that would have been capital beyond it (the gap, scaled by the growth factor)."""
    kbar, kgold = k_bar(alpha, beta, Xi), k_golden(alpha, Xi - 1)
    kmax = 1.3 * max(kbar, kgold) if kmax is None else kmax
    k = np.linspace(0, kmax, 400)
    ax.plot(k, k_next(k, alpha, beta, Xi), color="black", lw=1.8)
    ax.plot(k, k, color="C0", lw=1.0, linestyle="--")
    ax.axvline(kbar, color="black", lw=0.8, linestyle="--")
    ax.axvline(kgold, color="0.45", lw=0.8, linestyle=":")
    ticks, names = [kbar, kgold], [r"$\bar{k}$", r"$k^{**}$"]
    if kgold < kbar:
        top = float(k_next(kgold, alpha, beta, Xi))
        ax.annotate("", xy=(kgold, kgold), xytext=(kgold, top), arrowprops=dict(arrowstyle="<->", lw=1.0, color="C3"))
        ax.annotate("the bubble", (kgold, (kgold + top) / 2), xytext=(6, 0), textcoords="offset points", fontsize=9, color="C3")
        ax.plot([kgold], [kgold], "o", color="C3", ms=4)
    ax.set_xlim(0, kmax)
    ax.set_ylim(0, kmax)
    if abs(kbar - kgold) < 0.04 * kmax:  # one tick would cover the other
        ticks, names = [min(kbar, kgold)], [r"$\bar{k} \approx k^{**}$"]
    ax.set_xticks(ticks, names)
    ax.set_yticks([])
    ax.set_xlabel(r"$k_t$", loc="right")
    ax.set_ylabel(r"$k_{t+1}$", loc="top", rotation=0)


def _per_generation(beta_year, growth_year):
    return beta_year**YEARS, (1 + growth_year) ** YEARS


def _corners(table):
    names = list(table)
    return [dict(zip(names, values)) for values in itertools.product(*(table[name][1:3] for name in names))]


def _look(widgets, labels):
    label = 0.55 * max(len(text) for text in labels) + 1
    return {"style": {"description_width": f"{label:.1f}em"}, "layout": widgets.Layout(width=f"{label + 25:.1f}em")}


def _controls(widgets, table):
    look = _look(widgets, [row[4] for row in table.values()])
    return {name: widgets.FloatSlider(value=value, min=low, max=high, step=step, description=label,
                                      readout_format=fmt, **look)
            for name, (value, low, high, step, label, fmt) in table.items()}


def _panel(widgets, explore, controls):
    from IPython.display import display

    status = widgets.HTML(layout=widgets.Layout(height="1.5em"))

    def draw(**values):
        status.value = BUSY
        try:
            explore(**values)
        finally:
            status.value = ""

    display(widgets.VBox([*controls.values(), status, widgets.interactive_output(draw, controls)]))


def sliders_bursting(simulate, expected, lifetimes, table=BURSTING):
    """Sliders for the probability of bursting and the interest factor: sample paths of the bubble
    and its expected value (left), and the distribution of lifetimes (right)."""
    import ipywidgets as widgets
    import matplotlib.pyplot as plt

    D_low, D_high = table["D"][1:3]
    R_high = table["R"][2]
    top_paths = 1.5 * (R_high / (1 - D_high)) ** PERIODS
    top_share = 1.15 * D_high

    def explore(D, R):
        fig, (left, right) = plt.subplots(1, 2, figsize=(9.0, 3.8))
        draw_paths(left, simulate(R, D, PERIODS), expected(R, PERIODS), top=top_paths)
        draw_lifetimes(right, lifetimes(D), D, top=top_share)
        fig.tight_layout()
        plt.show()

    _panel(widgets, explore, _controls(widgets, table))


def tirole_limits(k_bar, k_golden, table=TIROLE):
    return 1.15 * max(max(k_bar(c["alpha"], *_per_generation(c["beta_year"], c["growth_year"])),
                          k_golden(c["alpha"], _per_generation(c["beta_year"], c["growth_year"])[1] - 1))
                      for c in _corners(table))


def sliders_tirole(k_next, k_bar, k_golden, interest_factor, table=TIROLE):
    """Sliders for the capital share, patience and population growth, a generation being YEARS
    years: whether a bubble can last, and how large it is."""
    import ipywidgets as widgets
    import matplotlib.pyplot as plt

    kmax = tirole_limits(k_bar, k_golden, table)

    def explore(alpha, beta_year, growth_year):
        beta, Xi = _per_generation(beta_year, growth_year)
        fig, ax = plt.subplots(figsize=(6.4, 5.0))
        draw_tirole(ax, k_next, k_bar, k_golden, alpha, beta, Xi, kmax=kmax)
        rate = float(interest_factor(k_bar(alpha, beta, Xi), alpha)) ** (1 / YEARS) - 1
        verdict = ("dynamically inefficient: a bubble can last" if rate < growth_year
                   else "dynamically efficient: no bubble can last")
        ax.text(0.03, 0.97, f"with no bubble, interest rate {rate:.2%} a year\nagainst population growth {growth_year:.1%}: {verdict}",
                transform=ax.transAxes, va="top", fontsize=9, bbox=READOUT)
        plt.show()

    _panel(widgets, explore, _controls(widgets, table))


def self_test() -> list[str]:
    import matplotlib.pyplot as plt

    failures = []

    def simulate(R, D, periods, bubbles=12, seed=0):
        rng = np.random.default_rng(seed)
        B = np.ones((periods + 1, bubbles))
        for t in range(periods):
            B[t + 1] = np.where(rng.random(bubbles) >= D, B[t] * R / (1 - D), 0.0)
        return B

    expected = lambda R, periods: R ** np.arange(periods + 1)
    lifetimes = lambda D: np.random.default_rng(1).geometric(D, size=20000)
    Q = lambda alpha, beta, Xi: (1 - alpha) * beta / (Xi * (1 + beta))
    k_next = lambda k, alpha, beta, Xi: Q(alpha, beta, Xi) * np.asarray(k, float) ** alpha
    k_bar = lambda alpha, beta, Xi: Q(alpha, beta, Xi) ** (1 / (1 - alpha))
    k_golden = lambda alpha, xi: (xi / alpha) ** (1 / (alpha - 1))
    interest_factor = lambda k, alpha: 1 + alpha * np.asarray(k, float) ** (alpha - 1)

    paths = simulate(1.04, 0.05, 2000, bubbles=4000, seed=2)
    if not abs(np.mean(paths[50]) / 1.04**50 - 1) < 0.25:
        failures.append("bubbles: the simulated bubble's mean does not grow at the interest factor")
    life = lifetimes(0.05)
    if not (abs(np.mean(life) - 20) < 0.6 and abs(np.median(life) - 14) <= 1):
        failures.append(f"bubbles: lifetimes have mean {np.mean(life):.1f} and median {np.median(life)}, not about 20 and 14")
    fig, (a, b, c) = plt.subplots(1, 3)
    try:
        draw_paths(a, simulate(1.04, 0.05, PERIODS), expected(1.04, PERIODS))
        draw_lifetimes(b, life, 0.05)
        beta, Xi = _per_generation(0.999, 0.04)
        draw_tirole(c, k_next, k_bar, k_golden, 0.20, beta, Xi)
        if k_golden(0.20, Xi - 1) >= k_bar(0.20, beta, Xi):
            failures.append("bubbles: the first Tirole picture is not dynamically inefficient")
    except Exception as e:  # noqa: BLE001
        failures.append(f"bubbles: drawing failed: {e!r}")
    plt.close("all")
    failures += slider_check.check("bubbles bursting", sliders_bursting, simulate, expected, lifetimes)
    failures += slider_check.check("bubbles Tirole", sliders_tirole, k_next, k_bar, k_golden, interest_factor)
    return failures
