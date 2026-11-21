"""The book's notation, spelled out: its macros expanded into the LaTeX they print.

The book writes every economic object with its macro (`\\CRRA`, `\\kap`, `\\ptyGroRte`), and the
registry and the course block decide what each one prints. The website reads those
definitions; matplotlib and a notebook opened in Colab do not. `tex` spells the macros out, so
a figure label written `tex(r"$\\ptyGroRte$ low")` prints whatever the book prints for
productivity growth, and follows a change of notation without an edit.

The definitions are in `_notation_macros.py`, which code/notebook_math.py writes from the
registry (@resources/notation/econark-math.yml) and the course block
(notation/course-local-math.yml); the course block wins where both define a name, as in the
book's myst.yml.

`python -m intertemporal_choice --self-test` runs `self_test`.
"""

import re

from intertemporal_choice._notation_macros import MACROS

CONTROL_WORD = re.compile(r"\\[A-Za-z]+")
PARAMETER = re.compile(r"#([1-9])")
ENDS_IN_CONTROL_WORD = re.compile(r"\\[A-Za-z]+$")


def arity(body: str) -> int:
    """How many arguments a definition takes: its highest #n."""
    return max((int(n) for n in PARAMETER.findall(body)), default=0)


def _argument(tex: str, i: int) -> tuple[str, int]:
    """The argument that starts at tex[i], spaces skipped: a braced group's content, a control
    word or symbol, or one character; and the index just past it."""
    while i < len(tex) and tex[i] == " ":
        i += 1
    if i >= len(tex):
        raise ValueError("a macro is missing an argument")
    if tex[i] == "{":
        depth, j = 0, i
        while j < len(tex):
            if tex[j] == "\\":
                j += 2
                continue
            depth += {"{": 1, "}": -1}.get(tex[j], 0)
            if depth == 0:
                return tex[i + 1 : j], j + 1
            j += 1
        raise ValueError("an argument's braces do not close")
    if tex[i] == "\\":
        m = CONTROL_WORD.match(tex, i)
        return (m.group(0), m.end()) if m else (tex[i : i + 2], i + 2)
    return tex[i], i + 1


def expand(tex: str, macros: dict[str, str] = MACROS, _depth: int = 0) -> str:
    """tex with every macro in `macros` replaced, recursively, by what it prints. Other control
    words (\\frac, \\alpha) are left as they are."""
    if _depth > 30:
        raise ValueError("macros that expand into each other without end")
    out: list[str] = []
    i = 0
    while i < len(tex):
        if tex[i] != "\\":
            out.append(tex[i])
            i += 1
            continue
        m = CONTROL_WORD.match(tex, i)
        if not m:  # a control symbol: \, \{ \\ ...
            out.append(tex[i : i + 2])
            i += 2
            continue
        if m.group(0) not in macros:
            out.append(m.group(0))
            i = m.end()
            continue
        body, i = macros[m.group(0)], m.end()
        for n in range(1, arity(body) + 1):
            argument, i = _argument(tex, i)
            body = body.replace(f"#{n}", argument)
        text = expand(body, macros, _depth + 1)
        # A control word must not run into the letters around it: \alpha\kap is \alpha k, not \alphak.
        if text[:1].isalpha() and out and ENDS_IN_CONTROL_WORD.search(out[-1]):
            text = " " + text
        if ENDS_IN_CONTROL_WORD.search(text) and tex[i : i + 1].isalpha():
            text += " "
        out.append(text)
    return "".join(out)


def tex(text: str) -> str:
    """A label written with the book's macros, as matplotlib can print it: tex(r"$\\kap$") is "$k$"."""
    return expand(text)


def self_test() -> list[str]:
    failures = []
    macros = {"\\a": "\\alpha", "\\b": "\\a", "\\bb": "\\bar{\\bar{#1}}", "\\k": "k", "\\pair": "(#1,#2)"}
    cases = [
        (r"\b + \k", r"\alpha + k", "a macro defined by another"),
        (r"\bb{\k}", r"\bar{\bar{k}}", "a macro with an argument"),
        (r"\bb\k", r"\bar{\bar{k}}", "an argument given without braces"),
        (r"\pair{x}{\k}", r"(x,k)", "two arguments"),
        (r"\frac{\k}{2}\,\{", r"\frac{k}{2}\,\{", "control words and symbols it does not define"),
        (r"\alpha\k", r"\alpha k", "a control word running into a letter"),
        (r"\k x", r"k x", "a space after a macro"),
        (r"\bb{\{a\}}", r"\bar{\bar{\{a\}}}", "escaped braces inside an argument"),
    ]
    for given, want, what in cases:
        got = expand(given, macros)
        if got != want:
            failures.append(f"notation: {what}: {given!r} gave {got!r}, not {want!r}")
    for given, what in [(r"\pair{x}", "a missing argument"), (r"\bb{x", "an unclosed argument")]:
        try:
            expand(given, macros)
            failures.append(f"notation: {what} was not refused")
        except ValueError:
            pass
    try:
        expand(r"\loop", {"\\loop": "\\loop"})
        failures.append("notation: a macro defined by itself was not refused")
    except ValueError:
        pass
    if "\\CRRA" not in MACROS or tex(r"$\kap$") != "$k$":
        failures.append("notation: the book's definitions are missing, or \\kap does not print k")
    return failures
