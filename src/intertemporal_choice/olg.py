"""The Diamond OLG chapter's figures and sliders, kept out of its notebook.

The notebook, content/consumption/OLGModel/OLGModel.ipynb, shows the economics: the chapter's
equations for the accumulation of capital, the steady state, the golden rule and the shift that a
pay-as-you-go Social Security system makes. It passes those functions here, and this module only
draws, as `fisher` and `portfolio` do for their chapters.

A period is a generation. The sliders take a discount factor and a population growth rate per
year and turn them into a generation's: beta = beta_year^years and Xi = (1 + n)^years.

`python -m intertemporal_choice --self-test` runs `self_test`.
"""

import numpy as np


def _staircase(ax, k_next, k0, steps):
    """Arrows from k0 up to the accumulation curve, across to the 45-degree line, and so on."""
    kt, base = k0, 0.0
    for _ in range(steps):
        k1 = float(k_next(kt))
        ax.annotate("", xy=(kt, k1), xytext=(kt, base), arrowprops=dict(arrowstyle="->", lw=0.9))
        ax.annotate("", xy=(k1, k1), xytext=(kt, k1), arrowprops=dict(arrowstyle="->", lw=0.9))
        kt, base = k1, k1
    return kt


def draw_dynamics(ax, k_next, k0, kbar, steps=4):
    """The chapter's first figure: capital per worker converging to the steady state."""
    kmax = 1.35 * max(kbar, k0)
    k = np.linspace(0, kmax, 400)
    ax.plot(k, k_next(k), color="black", lw=1.8)
    ax.plot(k, k, color="C0", lw=1.0, linestyle="--")
    ax.axvline(kbar, color="black", lw=0.8, linestyle="--")
    _staircase(ax, k_next, k0, steps)
    ax.annotate(r"$k_{t+1}(k_t)$", (0.55 * kmax, float(k_next(0.55 * kmax))), xytext=(-40, 12),
                textcoords="offset points")
    ax.annotate("45° line", (0.95 * kmax, 0.95 * kmax), xytext=(-55, 4), textcoords="offset points")
    ax.annotate(r"$k_1$", (k0, float(k_next(k0))), xytext=(-18, 2), textcoords="offset points")
    ax.set_xlim(0, kmax)
    ax.set_ylim(0, kmax)
    ax.set_xticks([k0, kbar], [r"$k_0$", r"$\bar{k}$"])
    ax.set_yticks([])
    ax.set_xlabel(r"$k_t$", loc="right")
    ax.set_ylabel(r"$k_{t+1}$", loc="top", rotation=0)


def draw_output(top, bottom, epsilon, xi, kgold, kbar=None):
    """The chapter's second figure: gross output f(k) and xi k (top), and their difference,
    steady-state consumption per worker, which is highest at the golden rule (bottom)."""
    kzero = xi ** (1 / (epsilon - 1))  # where f(k) = xi k and consumption would be zero
    k = np.linspace(0, 1.05 * kzero, 500)
    f = k**epsilon
    top.plot(k, f, color="black", lw=1.8)
    top.plot(k, xi * k, color="C0", lw=1.0, linestyle="--")
    top.annotate(r"$\mathrm{f}(k)$", (0.6 * kzero, (0.6 * kzero) ** epsilon), xytext=(0, 8), textcoords="offset points")
    top.annotate(r"$\xi k$", (0.6 * kzero, xi * 0.6 * kzero), xytext=(8, -14), textcoords="offset points")
    bottom.plot(k, f - xi * k, color="black", lw=1.8)
    bottom.axvline(kgold, color="0.45", lw=0.8, linestyle=":")
    ticks, names = [kgold], [r"$k^{**}$"]
    if kbar is not None:
        bottom.axvline(kbar, color="C1", lw=0.8, linestyle="--")
        ticks, names = ticks + [kbar], names + [r"$\bar{k}$"]
    bottom.annotate(r"$\mathrm{f}(k)-\xi k$", (0.75 * kzero, (0.75 * kzero) ** epsilon - xi * 0.75 * kzero),
                    xytext=(6, 6), textcoords="offset points")
    for ax in (top, bottom):
        ax.set_xlim(0, 1.05 * kzero)
        ax.set_ylim(0, None)
        ax.set_yticks([])
        ax.set_xlabel(r"$k$", loc="right")
    top.set_xticks([])
    bottom.set_xticks(ticks, names)


def _per_generation(beta_year, growth_year, years):
    return beta_year**years, (1 + growth_year) ** years


def _slider(widgets, value, low, high, step, label, fmt=".3f"):
    return widgets.FloatSlider(value=value, min=low, max=high, step=step, description=label,
                               continuous_update=False, readout_format=fmt,
                               style={"description_width": "initial"})


def sliders_dynamics(k_next, k_bar, years=30):
    """Sliders for the capital share, patience, population growth and the starting capital."""
    import ipywidgets as widgets
    import matplotlib.pyplot as plt

    def explore(epsilon, beta_year, growth_year, start):
        beta, Xi = _per_generation(beta_year, growth_year, years)
        step = lambda k: k_next(k, epsilon, beta, Xi)
        kbar = k_bar(epsilon, beta, Xi)
        fig, ax = plt.subplots(figsize=(6.4, 5.0))
        draw_dynamics(ax, step, start * kbar, kbar, steps=6)
        ax.text(0.03, 0.97, f"$\\bar{{k}}$ = {kbar:.4f}\neach generation closes {1 - epsilon:.0%}\n"
                f"of the log gap to $\\bar{{k}}$", transform=ax.transAxes, va="top", fontsize=9)
        plt.show()

    widgets.interact(
        explore,
        epsilon=_slider(widgets, 0.33, 0.20, 0.40, 0.01, "capital share ε", ".2f"),
        beta_year=_slider(widgets, 0.96, 0.94, 0.99, 0.001, "β per year"),
        growth_year=_slider(widgets, 0.01, -0.01, 0.04, 0.001, "population growth per year"),
        start=_slider(widgets, 0.25, 0.05, 2.0, 0.05, "k₀ / k̄", ".2f"),
    )


def sliders_output(k_bar, k_golden, years=30):
    """Sliders for the capital share, patience and population growth: output, and whether the
    economy's steady state lies beyond the golden rule."""
    import ipywidgets as widgets
    import matplotlib.pyplot as plt

    def explore(epsilon, beta_year, growth_year):
        beta, Xi = _per_generation(beta_year, growth_year, years)
        xi = Xi - 1
        if xi <= 0:
            print("With a shrinking or constant population, xi k never catches up with f(k); "
                  "raise population growth above zero.")
            return
        kbar, kgold = k_bar(epsilon, beta, Xi), k_golden(epsilon, xi)
        fig, (top, bottom) = plt.subplots(2, 1, figsize=(6.4, 7.0))
        draw_output(top, bottom, epsilon, xi, kgold, kbar)
        verdict = "dynamically inefficient" if kbar > kgold else "dynamically efficient"
        bottom.text(0.97, 0.95, f"$\\bar{{k}}$ = {kbar:.4f}, $k^{{**}}$ = {kgold:.4f}:\n{verdict}",
                    transform=bottom.transAxes, ha="right", va="top", fontsize=9)
        plt.show()

    widgets.interact(
        explore,
        epsilon=_slider(widgets, 0.33, 0.20, 0.40, 0.01, "capital share ε", ".2f"),
        beta_year=_slider(widgets, 0.96, 0.94, 0.999, 0.001, "β per year"),
        growth_year=_slider(widgets, 0.01, 0.001, 0.04, 0.001, "population growth per year"),
    )


def sliders_payg(k_next, k_next_payg, k_bar, interest_factor, wage, years=30):
    """Sliders for the size of a pay-as-you-go system, the capital share and patience: the path
    from the old steady state to the new one, with no population growth, as in the chapter."""
    import ipywidgets as widgets
    import matplotlib.pyplot as plt

    def explore(contribution, epsilon, beta_year):
        beta = beta_year**years
        kbar = k_bar(epsilon, beta, 1.0)
        R = interest_factor(kbar, epsilon)  # held at its old steady-state value, as in the chapter
        z = contribution * wage(kbar, epsilon)
        old = lambda k: k_next(k, epsilon, beta, 1.0)
        new = lambda k: k_next_payg(k, epsilon, beta, z, R)
        # the new steady state: the upper root of new(k) = k, between the curve's peak above the
        # 45-degree line and the old steady state
        peak = (old(1.0) * epsilon) ** (1 / (1 - epsilon))  # where Q eps k^(eps-1) = 1
        if new(peak) <= peak:
            print("Contributions this large leave no steady state: capital runs out.")
            return
        low, high = peak, kbar
        for _ in range(100):
            middle = (low + high) / 2
            low, high = (middle, high) if new(middle) > middle else (low, middle)
        kbarbar = (low + high) / 2
        kmax = 1.35 * kbar
        k = np.linspace(1e-9, kmax, 400)
        fig, ax = plt.subplots(figsize=(6.4, 5.0))
        ax.plot(k, old(k), color="black", lw=1.8)
        ax.plot(k, new(k), color="C1", lw=1.8)
        ax.plot(k, k, color="C0", lw=1.0, linestyle="--")
        kt = kbar
        for _ in range(8):  # from the old steady state toward the new one
            k1 = float(new(kt))
            ax.annotate("", xy=(kt, k1), xytext=(kt, kt), arrowprops=dict(arrowstyle="->", lw=0.9))
            ax.annotate("", xy=(k1, k1), xytext=(kt, k1), arrowprops=dict(arrowstyle="->", lw=0.9))
            kt = k1
        ax.set_xlim(0, kmax)
        ax.set_ylim(0, kmax)
        ax.set_xticks([kbarbar, kbar], [r"$\bar{\bar{k}}$", r"$\bar{k}$"])
        ax.set_yticks([])
        ax.set_xlabel(r"$k_t$", loc="right")
        ax.set_ylabel(r"$k_{t+1}$", loc="top", rotation=0)
        ax.text(0.03, 0.97, f"$\\bar{{k}}$ = {kbar:.4f} before, $\\bar{{\\bar{{k}}}}$ = {kbarbar:.4f} after:\n"
                f"capital falls {1 - kbarbar / kbar:.0%}", transform=ax.transAxes, va="top", fontsize=9)
        plt.show()

    widgets.interact(
        explore,
        contribution=_slider(widgets, 0.10, 0.0, 0.30, 0.01, "contribution, share of the wage", ".2f"),
        epsilon=_slider(widgets, 0.33, 0.20, 0.40, 0.01, "capital share ε", ".2f"),
        beta_year=_slider(widgets, 0.96, 0.94, 0.99, 0.001, "β per year"),
    )


def self_test() -> list[str]:
    import matplotlib.pyplot as plt

    failures = []
    eps, beta, Xi = 0.33, 0.96**30, 1.01**30
    Q = (1 - eps) * beta / (Xi * (1 + beta))
    k_next = lambda k: Q * np.asarray(k, float) ** eps
    kbar = Q ** (1 / (1 - eps))
    fig, ax = plt.subplots()
    try:
        draw_dynamics(ax, k_next, kbar / 4, kbar)
        if len(ax.lines) < 3:
            failures.append(f"olg: draw_dynamics drew {len(ax.lines)} lines")
    except Exception as e:  # noqa: BLE001
        failures.append(f"olg: draw_dynamics failed: {e!r}")
    plt.close(fig)
    if abs(_staircase(plt.subplots()[1], k_next, kbar / 4, 60) - kbar) > 1e-6 * kbar:
        failures.append("olg: the staircase does not reach the steady state")
    plt.close("all")
    xi = Xi - 1
    fig, (top, bottom) = plt.subplots(2, 1)
    try:
        draw_output(top, bottom, eps, xi, (xi / eps) ** (1 / (eps - 1)), kbar)
    except Exception as e:  # noqa: BLE001
        failures.append(f"olg: draw_output failed: {e!r}")
    plt.close(fig)
    return failures
