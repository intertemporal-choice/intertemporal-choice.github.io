"""Portfolio Choice with CRRA Utility: the chapter's figures and sliders, kept out of its notebook.

The notebook, content/asset_pricing/Portfolio-CRRA/Portfolio-CRRA.ipynb, shows the economics: the
approximate risky share and the exactly optimal one, computed by its own `share_approx` and
`share_exact`, which it passes here. This module only draws, as `fisher` does for the Fisher
two-period chapter.

`python -m intertemporal_choice --self-test` runs `self_test`.
"""

import numpy as np


def draw_share(ax, rho, share):
    """The chapter's first figure: the risky share at each degree of relative risk aversion."""
    ax.plot(rho, share, color="C0")
    ax.set_xlim(rho[0], rho[-1])
    ax.set_xlabel(r"$\rho$", loc="right")
    ax.set_ylabel(r"$\varsigma$", loc="top", rotation=0)


def draw_error(ax, rho, error):
    """The chapter's second figure: the exactly optimal share minus the approximation."""
    ax.plot(rho, error, color="C0")
    ax.axhline(0, color="black", linewidth=0.6)
    ax.set_xlim(rho[0], rho[-1])
    ax.set_xlabel(r"$\rho$", loc="right")
    ax.set_ylabel("exact minus approximate share", loc="top")


def sliders(share_approx, share_exact, rho=np.linspace(1.0, 5.0, 81)):
    """Sliders for the premium and the volatility, each redrawing the two shares and their difference."""
    import ipywidgets as widgets  # only the sliders need it
    import matplotlib.pyplot as plt

    def explore(phi, sigma):
        approx = share_approx(rho, phi, sigma)
        exact = np.array([share_exact(x, phi, sigma) for x in rho])
        fig, (left, right) = plt.subplots(1, 2, figsize=(10.0, 4.0))
        left.plot(rho, approx, color="C0", label="approximation")
        left.plot(rho, exact, color="C1", linestyle="--", label="exact")
        left.axhline(1, color="0.6", linewidth=0.6)
        left.set_ylim(0, max(1.1, min(float(approx.max()) * 1.05, 3.0)))
        left.set_xlim(rho[0], rho[-1])
        left.set_xlabel(r"$\rho$", loc="right")
        left.set_ylabel(r"$\varsigma$", loc="top", rotation=0)
        left.legend(loc="upper right", fontsize=9)
        left.text(0.97, 0.70, f"Sharpe ratio $\\varphi/\\sigma$ = {phi / sigma:.2f}\n"
                  f"at $\\rho$ = 2: {share_approx(2.0, phi, sigma):.3f} approximate, "
                  f"{share_exact(2.0, phi, sigma):.3f} exact",
                  transform=left.transAxes, ha="right", va="top", fontsize=9)
        draw_error(right, rho, exact - approx)
        fig.tight_layout()
        plt.show()

    def slider(value, low, high, step, label):
        return widgets.FloatSlider(value=value, min=low, max=high, step=step, description=label,
                                   continuous_update=False, readout_format=".3f")

    widgets.interact(
        explore,
        phi=slider(0.03, 0.0, 0.10, 0.005, "premium φ"),
        sigma=slider(0.20, 0.05, 0.40, 0.01, "σ"),
    )


def self_test() -> list[str]:
    import matplotlib.pyplot as plt

    failures = []
    rho = np.linspace(1.0, 5.0, 9)
    for draw, values in ((draw_share, 0.03 / (rho * 0.04)), (draw_error, np.zeros_like(rho))):
        fig, ax = plt.subplots()
        try:
            draw(ax, rho, values)
            if not ax.lines or ax.get_xlim() != (rho[0], rho[-1]):
                failures.append(f"portfolio: {draw.__name__} drew no line or the wrong range")
        except Exception as e:  # noqa: BLE001
            failures.append(f"portfolio: {draw.__name__} failed: {e!r}")
        plt.close(fig)
    return failures
