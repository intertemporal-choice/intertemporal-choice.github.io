# Consumption Theory

Fisher's two-period problem opens the chapter. It exposes the logic of intertemporal
choice in the simplest setting that contains anything interesting, one in which a budget
constraint trades current against future consumption and a first-order condition equates
the marginal rate of substitution between them to the interest factor.

Extending that problem in one direction gives the Diamond overlapping generations
model, which lets us ask how public pensions and government debt shift resources across
cohorts. Extending Fisher's problem in the other direction,
toward many periods and uncertain income, gives the perfect foresight CRRA consumption
function and then the random walk result. Admitting a precautionary motive yields buffer
stock behavior, which reconciles the theory with observed age profiles of consumption
and income (the hump the perfect foresight model cannot produce).

The chapter closes with the leading departures from that benchmark: habit formation,
durable goods, time inconsistent discounting, and expectations that respond only
sluggishly to news.

<!-- PDF-only setup, ignored by every other export. This is the first article of the
export, so it runs before any equation or symbol below depends on it. It must sit BELOW
the heading above: anything above a page's first heading stops MyST rendering that
heading as \chapter.

\counterwithin numbers equations within the section (2.7.1) rather than the chapter
(2.304), which is what a book class does by default once its chapters are real.

\cancel and \mathscr stand in for the cancel and mathrsfs packages, which cannot be
reached from here. MyST only ever injects 14 hardcoded packages, has no configuration
key for others, and \usepackage is already an error stub by the time a body block runs,
so only the template preamble could load them. Left undefined, LaTeX drops the wrapper
and prints the bare symbol, which would make Carroll's bliss point \cancel{\cRat}
identical to ordinary consumption and \kPriceAfterITC identical to the ordinary price.
KaTeX supports both natively, so the website is unaffected and these fallbacks stay out
of its way. Replace them with the real packages if the template is ever vendored. -->


```{raw:latex}
\counterwithin{equation}{section}
\providecommand{\cancel}[1]{{\not{#1}}}
\providecommand{\mathscr}[1]{\mathcal{#1}}
```
