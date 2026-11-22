"""A Tractable Model of Buffer Stock Saving: the notebook's figures, kept out of its notebook.

The notebook, content/consumption/TractableBufferStock/TractableBufferStock.ipynb, shows the economics:
the parameters, the solution by reverse shooting, the loci, growth rates and paths each figure plots, and
the checks on the solution. It computes them with its own functions and passes them here. This module
only draws: axes, labels, arrows and annotations.

`python -m intertemporal_choice --self-test` runs `self_test`. Besides the drawing, it checks the
notebook's solver, `models.tractable_buffer_stock`, against HARK's TractableConsumerType when HARK is
installed, as it is in the book's own environment.
"""

import numpy as np

M_TARG = r"\hat{m}"
M_LABEL = r"$m^{\mathrm{e}}_{t}$"
C_LABEL = r"$c^{\mathrm{e}}_{t}$"
THORN_LABEL = r"$\varrho^{-1}(\mathsf{r}-\vartheta) \approx \mathrm{þ}$"
UNLINED = dict(facecolor="white", edgecolor="none", pad=1)  # hides the line behind a label


def _arrow(width=1.5):
    return dict(arrowstyle="-|>", color="black", linewidth=width, mutation_scale=14)


def _growth_axes(ax):
    ax.tick_params(length=0)
    ax.set_xlabel(M_LABEL, loc="right")
    ax.set_ylabel("Growth", loc="top", rotation=0)


def draw_phase_diagram(ax, m_targ, c_targ, c, c_locus, m_locus):
    """The c and m loci, the stable arm c and arrows of motion, for m up to 1.5 times its target."""
    m_max, c_max = 1.5 * m_targ, 1.7 * c_targ
    m = np.linspace(0, m_max, 400)
    ax.plot(m, c_locus(m), color="black", linewidth=1.2)
    ax.plot(m, m_locus(m), color="black", linewidth=1.2)
    ax.plot(m, c(m), color="black", linewidth=1.2, linestyle="--")

    m_label = 1.25 * m_targ
    ax.text(m_label, c_locus(m_label), r"$\Delta c^{\mathrm{e}}_{t+1} = 0$ →  ", ha="right", va="center")
    m_label = m_targ / 3
    ax.text(m_label, m_locus(m_label), r"$\Delta m^{\mathrm{e}}_{t+1} = 0$ ↘", ha="right", va="bottom")
    m_label = m_targ / 2
    ax.text(m_label, c(m_label), r"$c^{\mathrm{e}}(m)$ = Stable Arm →  ", ha="right", va="center")
    ax.text(m_targ, c_targ, "SS ↘ ", ha="right", va="bottom")

    arrow = _arrow(1.2)
    for (x, y), (dx, dy) in [
        ((m_targ, c_targ / 2), (m_targ / 10, 0)),
        ((m_targ, c_targ / 2), (0, -c_targ / 5)),
        ((m_targ, 1.5 * c_targ), (-m_targ / 10, 0)),
        ((m_targ, 1.5 * c_targ), (0, c_targ / 5)),
    ]:
        ax.annotate("", xy=(x + dx, y + dy), xytext=(x, y), arrowprops=arrow)

    ax.set_xlim(0, m_max)
    ax.set_ylim(0, c_max)
    ax.set_xticks([])
    ax.set_yticks([])
    ax.set_xlabel(M_LABEL, loc="right")
    ax.set_ylabel(C_LABEL, loc="top", rotation=0)


def draw_consumption_function(ax, m_targ, c, c_perfect_foresight):
    """c, the perfect foresight consumption function and the 45 degree line, for m up to 15 times its target."""
    m_max = 15 * m_targ
    m = np.linspace(0, m_max, 600)
    c_pf = c_perfect_foresight(m)
    diagonal = np.linspace(0, c(m_max), 100)
    ax.plot(m, c(m), color="black")
    ax.plot(m, c_pf, color="black", linestyle="--", linewidth=1.2)
    ax.plot(diagonal, diagonal, color="black", linestyle="--", linewidth=1.2)

    top = c(m_max)
    ax.text(0.8 * top, 0.8 * top, "  ← 45 Degree Line", ha="left", va="center")
    m_label = m_targ / 3
    label = r"  ← Consumption Function $\mathrm{c}(m^{\mathrm{e}}_{t})$"
    ax.text(m_label, c(m_label), label, ha="left", va="center")
    m_label = 0.85 * m_max
    ax.text(
        m_label,
        c_perfect_foresight(m_label),
        r"Perf Foresight $\bar{\mathrm{c}}(m^{\mathrm{e}}_{t})$ →  ",
        ha="right",
        va="bottom",
    )

    ax.set_xlim(0, m_max)
    ax.set_ylim(0, 1.05 * c_pf[-1])
    ax.set_xticks([])
    ax.set_yticks([])
    ax.set_xlabel(M_LABEL, loc="right")
    ax.set_ylabel(C_LABEL, loc="top", rotation=0)


def draw_growth(ax, m_targ, growth, gamma, thorn):
    """Consumption growth for a consumer who stays employed, with income growth gamma and the perfect
    foresight growth rate thorn, and the precautionary increment between them."""
    m = np.linspace(0.5 * m_targ, 2.5 * m_targ, 400)
    g = growth(m)
    y_min, y_max = thorn - 0.01, g[0]

    ax.plot(m, g, color="black")
    ax.hlines([gamma, thorn], 0, 2.5 * m_targ, color="black", linewidth=1.2)
    ax.vlines(m_targ, y_min, y_max, color="black", linewidth=0.8)

    m_label = 2 * m_targ / 3
    ax.text(
        m_label + 0.25,
        growth(m_label),
        r"← $\Delta\,\log\,\boldsymbol{c}^{\mathrm{e}}_{t+1} \approx \mathrm{þ} + \mho(1+\mathfrak{p}\nabla_{t+1})\nabla_{t+1}$",
        ha="left",
        va="center",
        bbox=UNLINED,
    )
    m_label = 2 * m_targ
    ax.annotate(
        "",
        xy=(m_label, growth(m_label)),
        xytext=(m_label, thorn),
        arrowprops=dict(arrowstyle="<->", color="black", linewidth=1),
    )
    ax.text(
        m_label - 0.25,
        (growth(m_label) + thorn) / 2,
        r"Precautionary Increment: $\mho(1+\mathfrak{p}\nabla_{t+1})\nabla_{t+1}$",
        ha="right",
        va="center",
        bbox=UNLINED,
    )

    ax.set_xlim(0, 2.5 * m_targ)
    ax.set_ylim(y_min, y_max)
    ax.set_xticks([m_targ], [rf"${M_TARG}$"])
    ax.set_yticks([gamma, thorn], [r"$\mathring{\mathrm{g}}$", THORN_LABEL])
    _growth_axes(ax)


def draw_growth_higher_r(ax, m_old, m_new, growth_old, growth_new, gamma, thorn_old, thorn_new):
    """Consumption growth before and after a rise in the interest rate, with the shift it causes."""
    m = np.linspace(0.5 * m_old, 2.5 * m_old, 400)
    y_min, y_max = thorn_old - 0.01, growth_new(0.5 * m_new)

    ax.plot(m, growth_old(m), color="black")
    ax.plot(m, growth_new(m), color="black", linestyle="--")
    ax.hlines([gamma, thorn_old], 0, 2.5 * m_old, color="black", linewidth=1.2)
    ax.hlines(thorn_new, 0, 2.5 * m_old, color="black", linewidth=1.2, linestyle="--")
    ax.vlines(m_old, y_min, y_max, color="black", linewidth=0.8)
    ax.vlines(m_new, y_min, y_max, color="black", linewidth=0.8, linestyle=":")

    # The rise in r lifts the perfect foresight growth rate, and with it the whole locus.
    arrow = _arrow()
    m_arrow = 1.25 * m_new
    ax.annotate("", xy=(m_arrow, thorn_new), xytext=(m_arrow, thorn_old), arrowprops=arrow)
    ax.annotate("", xy=(m_arrow, growth_new(m_arrow)), xytext=(m_arrow, growth_old(m_arrow)), arrowprops=arrow)

    m_label = 5 * m_old / 6
    ax.text(m_label, growth_old(m_label), r"$\Delta\,\log\,\boldsymbol{c}^{\mathrm{e}}_{t+1}$ →  ", ha="right", va="bottom")
    m_label = 13 * m_old / 8
    ax.text(
        m_label,
        growth_new(m_label),
        r"  ← $\Delta\,\log\,\grave{\boldsymbol{c}}^{\mathrm{e}}_{t+1}$",
        ha="left",
        va="bottom",
    )

    ax.set_xlim(0, 1.8 * m_new)
    ax.set_ylim(y_min, y_max)
    ax.set_xticks([m_old, m_new], [rf"${M_TARG}$", rf"$\grave{{{M_TARG}}}$"])
    ax.set_yticks(
        [gamma, thorn_new, thorn_old],
        [
            r"$\mathring{\mathrm{g}}$",
            r"$\varrho^{-1}(\grave{\mathsf{r}}-\vartheta) \approx \grave{\mathrm{þ}}$",
            THORN_LABEL,
        ],
    )
    _growth_axes(ax)


def draw_growth_higher_mho(ax, m_old, m_new, growth_old, growth_new, gamma_old, gamma_new, thorn):
    """Consumption growth before and after a rise in unemployment risk, with both targets."""
    m_max = 1.8 * m_new
    m = np.linspace(0.5 * m_old, m_max, 400)
    y_min, y_max = thorn - 0.01, growth_new(0.45 * m_new)

    ax.plot(m, growth_old(m), color="black")
    ax.plot(m, growth_new(m), color="black", linestyle="--")
    ax.hlines([gamma_old, thorn], 0, m_max, color="black", linewidth=1.2)
    ax.hlines(gamma_new, 0, m_max, color="black", linewidth=1.2, linestyle="--")
    ax.vlines([m_old, m_new], y_min, y_max, color="black", linewidth=0.8)
    ax.plot([m_old, m_new], [gamma_old, gamma_new], "o", color="black", markersize=6)
    ax.text(m_old, gamma_old, "Old Target ↗ ", ha="right", va="top")
    ax.text(m_new, gamma_new, " ↙ New Target", ha="left", va="bottom")

    arrow = _arrow()
    ax.annotate("", xy=(0.1 * m_old, gamma_new), xytext=(0.1 * m_old, gamma_old), arrowprops=arrow)
    ax.annotate("", xy=(m_old, growth_new(m_old)), xytext=(m_old, gamma_old), arrowprops=arrow)

    m_label = 7.5 * m_old / 12
    ax.text(
        m_label,
        growth_new(m_label),
        r"$\Delta\,\log\,\grave{\boldsymbol{c}}^{\mathrm{e}}_{t+1}$ →  ",
        ha="right",
        va="top",
    )

    ax.set_xlim(0, m_max)
    ax.set_ylim(y_min, y_max)
    ax.set_xticks([m_old, m_new], [rf"${M_TARG}$", rf"$\grave{{{M_TARG}}}$"])
    ax.set_yticks(
        [gamma_new, gamma_old, thorn],
        [r"New $\mathring{\mathrm{g}}$", r"Old $\mathring{\mathrm{g}}$", THORN_LABEL],
    )
    _growth_axes(ax)


def draw_new_target(ax, old, new, c_old, c_new, m_locus, m_path, c_path):
    """The old and new consumption functions, the m locus, and the path from the old target (old, new: (m, c))."""
    (m_old, c_old_targ), (m_new, c_new_targ) = old, new
    m = np.linspace(0, m_new + 2, 400)
    ax.plot(m, c_old(m), color="black", linewidth=1.2)
    ax.plot(m, c_new(m), color="black")
    ax.plot(m, m_locus(m), color="black", linewidth=1.2, linestyle="--")
    ax.plot(np.r_[m_old, m_path], np.r_[c_old_targ, c_path], ".", color="black", markersize=4)

    ax.text(m_old, 1.02 * c_old_targ, "Orig Target ↘", ha="right", va="bottom")
    ax.text(m_new, 0.98 * c_new_targ, " ↖ New Target", ha="left", va="top")
    ax.text(0.45 * m_old, 0.67 * c_old_targ, r"Orig $\mathrm{c}(m^{\mathrm{e}}_{t})$ →  ", ha="right", va="center")
    ax.text(0.9 * m_old, c_new(0.9 * m_old), r"  ← New $\mathrm{c}(m^{\mathrm{e}}_{t})$", ha="left", va="top")

    ax.spines["left"].set_position(("data", 0))
    ax.set_xlim(-1, m_new + 2)
    ax.set_ylim(0, 1.3 * c_new_targ)
    ax.set_xticks([])
    ax.set_yticks([])
    ax.set_xlabel(M_LABEL, loc="right")
    ax.set_ylabel(C_LABEL, loc="top", rotation=0)


def draw_path(ax, periods, series, ylabel, xticks=(0, 25, 50, 75)):
    """A time path: dots, time ticks, no ticks on the value axis."""
    ax.plot(periods[: len(series)], series, ".", color="black", markersize=6)
    ax.set_xlim(periods[0] - 2, periods[-1] + 2)
    ax.set_ylim(0, 1.05 * np.max(series))
    ax.set_xticks(list(xticks))
    ax.set_yticks([])
    ax.set_xlabel("Time", loc="right")
    ax.set_ylabel(ylabel, loc="top", rotation=0)


def draw_level(ax, periods, level, label):
    """A dashed horizontal line across a path figure, labeled from below at its middle."""
    ax.hlines(level, periods[0], periods[-1], color="black", linewidth=1.2, linestyle="--")
    middle = (periods[0] + periods[-1]) / 2
    ax.text(middle, level, f"↑\n{label}", ha="center", va="top")


def _check_against_hark() -> list[str]:
    """The notebook's solver against HARK's TractableConsumerType, run here: every comparison value comes from
    HARK. The calibrations stay away from the edge of growth impatience, where HARK's solve stops at its cap of
    5,000 iterations before its stable arm covers the range."""
    try:
        import HARK.ConsumptionSaving.TractableBufferStockModel as tbs
    except ImportError:
        return []  # the core installs without HARK; the book's own environment, and CI, have it
    from intertemporal_choice.models import tractable_buffer_stock as model

    class Hark(tbs.TractableConsumerType):
        def pre_solve(self):
            super().pre_solve()
            self.assign_parameters(mUpperBnd=16 * self.mTarg)

    failures = []
    for changes in ({}, {"R": 1.07}, {"mho": 0.015}, {"beta": 1 / 1.08}, {"mho": 0.0005, "rho": 1.0}):
        e = model.Consumer(**changes)
        s = model.solve(e)
        h = Hark(UnempPrb=e.mho, DiscFac=e.beta, Rfree=e.R, PermGroFac=e.G, CRRA=e.rho, verbose=0)
        h.solve()
        ours = [s.m_targ, s.c_targ, s.mpc_targ, s.mpc_targ_1, s.mpc_targ_2, s.mpc_0, e.kappa]
        theirs = [h.mTarg, h.cTarg, h.MPCtarg, h.MMPCtarg, h.MMMPCtarg, h.MPCmax, h.PFMPC]
        if not np.allclose(ours, theirs, rtol=1e-10, atol=0):
            failures.append(f"tractable: the target, its MPC and its derivatives, or the MPC at 0, differ from HARK's at {changes}")
        m = np.linspace(0, 15 * s.m_targ, 2001)
        cfunc = h.solution[0].cFunc
        if not (np.allclose(s.c(m), cfunc(m), rtol=0, atol=1e-10) and np.allclose(s.mpc(m), cfunc.derivative(m), rtol=0, atol=1e-10)):
            failures.append(f"tractable: the consumption function or its MPC differs from HARK's at {changes}")
    return failures


def self_test() -> list[str]:
    import matplotlib.pyplot as plt

    failures = []
    c = lambda m: np.minimum(m, 0.9 + 0.05 * m)  # a stand-in consumption function: concave, below the 45 degree line
    c_locus, m_locus = (lambda m: 0.2 * m), (lambda m: 0.97 + 0.03 * m)

    fig, ax = plt.subplots()
    draw_phase_diagram(ax, 5.0, 1.1, c, c_locus, m_locus)
    if len(ax.get_lines()) != 3 or len([t for t in ax.texts if getattr(t, "arrow_patch", None) is not None]) != 4:
        failures.append("tractable: draw_phase_diagram does not draw two loci, the stable arm and four arrows")
    plt.close(fig)

    fig, ax = plt.subplots()
    draw_consumption_function(ax, 5.0, c, lambda m: 0.06 * (m - 1 + 34))
    if len(ax.get_lines()) != 3 or ax.get_xlim() != (0.0, 75.0):
        failures.append("tractable: draw_consumption_function does not draw c, perfect foresight and the 45 degree line to 15 times target")
    plt.close(fig)

    growth = lambda m: 0.05 / m - 0.06
    fig, ax = plt.subplots()
    draw_growth(ax, 5.0, growth, -0.005, -0.033)
    if [t.get_text() for t in ax.get_xticklabels()] != [rf"${M_TARG}$"]:
        failures.append("tractable: draw_growth does not mark the target on the m axis")
    plt.close(fig)

    for draw in (draw_growth_higher_r, draw_growth_higher_mho):
        fig, ax = plt.subplots()
        draw(ax, 5.0, 6.5, growth, lambda m: growth(m) + 0.02, -0.005, 0.0, -0.033)
        if len(ax.get_xticks()) != 2:
            failures.append(f"tractable: {draw.__name__} does not mark the old and new targets")
        plt.close(fig)

    fig, ax = plt.subplots()
    draw_new_target(ax, (5.0, 1.1), (7.0, 1.15), c, lambda m: 0.95 * c(m), m_locus, np.linspace(5, 7, 10), np.linspace(1.0, 1.15, 10))
    if len(ax.get_lines()) != 4:
        failures.append("tractable: draw_new_target does not draw two consumption functions, the m locus and the path")
    plt.close(fig)

    fig, ax = plt.subplots()
    periods = np.arange(-4, 75)
    draw_path(ax, periods, np.linspace(1.0, 2.0, 79), r"$\kappa_{t}$")
    draw_level(ax, periods, 0.06, "Perfect Foresight MPC")
    if len(ax.collections) != 1 or "Perfect Foresight MPC" not in ax.texts[0].get_text():
        failures.append("tractable: draw_level does not draw and label its line")
    plt.close(fig)

    return failures + _check_against_hark()
