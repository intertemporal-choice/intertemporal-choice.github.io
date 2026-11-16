"""Checks for the slider panels, run by the modules' self-tests: the axes stay fixed, and moving
each slider changes the picture.

Chris, 2026-10-26: "no visible change occurs in the figure for some of the changes of parameters
... fix the axes ... so that rescaling does not hide meaningful changes." A panel drawn relative to
its own values redraws the same picture with new numbers in its readouts and on its axes, so the
check compares pixels with readouts, legends and ticks hidden, not the plotted data.
"""

import warnings

import numpy as np


def capture(sliders, *args):
    """Run `sliders(*args)` with ipywidgets.interact and interactive_output, and IPython's display,
    replaced, and return the redraw function and the sliders it was given, so a test can draw any
    combination of values without a browser."""
    import IPython.display
    import ipywidgets as widgets

    captured = {}

    def output(f, controls):
        captured.update(redraw=f, controls=controls)
        return widgets.Output()

    saved = widgets.interact, widgets.interactive_output, IPython.display.display
    widgets.interact = lambda f, **controls: captured.update(redraw=f, controls=controls)
    widgets.interactive_output = output
    IPython.display.display = lambda *objects, **kwargs: None
    try:
        sliders(*args)
    finally:
        widgets.interact, widgets.interactive_output, IPython.display.display = saved
    return captured["redraw"], captured["controls"]


def picture(redraw, values):
    """Draw one combination and return its axes' limits and its pixels without readouts, legends or
    ticks, which a rescaled axis redraws with new numbers (the staircases' arrows are annotations
    with no text, and stay)."""
    import matplotlib.pyplot as plt

    with warnings.catch_warnings():  # plt.show() warns on a backend with no display
        warnings.simplefilter("ignore", UserWarning)
        redraw(**values)
    fig = plt.gcf()
    for ax in fig.axes:
        for text in ax.texts:
            if text.get_text():
                text.set_visible(False)
        if ax.get_legend():
            ax.get_legend().set_visible(False)
        ax.tick_params(which="both", bottom=False, left=False, labelbottom=False, labelleft=False)
    fig.canvas.draw()
    limits = [(ax.get_xlim(), ax.get_ylim()) for ax in fig.axes]
    pixels = np.asarray(fig.canvas.buffer_rgba()).astype(int)
    plt.close("all")
    return limits, pixels


def changed(a, b):
    """The share of pixels that differ visibly: by more than an eighth of a channel's range."""
    return float(np.mean(np.any(np.abs(a - b) > 32, axis=-1)))


def check(name, sliders, *args, skip=()):
    """Failures, as strings. Each slider, the others at their first values, is drawn at the ends of its
    range and a quarter of the way in from each end. The two inner pictures must differ in at least one
    pixel in ten thousand (a pure rescaling differs in none; the ends can be degenerate, such as no
    income at all), and every picture must have the first one's axes."""
    redraw, controls = capture(sliders, *args)
    first = {key: control.value for key, control in controls.items()}
    limits, _ = picture(redraw, first)
    failures = []
    for key, control in controls.items():
        if key in skip:
            continue
        points = [control.min + share * (control.max - control.min) for share in (0, 0.25, 0.75, 1)]
        pictures = [picture(redraw, {**first, key: point}) for point in points]
        if changed(pictures[1][1], pictures[2][1]) < 1e-4:
            failures.append(f"{name}: moving {key} from {points[1]:.4g} to {points[2]:.4g} leaves the picture unchanged")
        if any(axes != limits for axes, _ in pictures):
            failures.append(f"{name}: moving {key} changes the axes")
    return failures
