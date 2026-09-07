(sec:LucasGrowth)=
# The Lucas Growth Model

{cite:t}`lucasGrowth` presents a growth model in which output is generated via a production function of the form

```{math}
:label: eq:aggY

\YLev = \PtyLev \Kap^{\kapShare} (\labor \hLucas \Labor)^{1-\kapShare}
```

where {math}`\YLev, \PtyLev,` and {math}`\KLev` are as usually defined and {math}`0 < \kapShare < 1`, where {math}`\labor` is defined as the proportion of total labor time
spent working, and {math}`\hLucas` is what Lucas calls the stock of 'human
capital.'

The production function can be rewritten in per-capita terms as

```{math}
:label: eq:pcy

\yRat = \PtyLev \kRat^\kapShare (\labor \hLucas)^{1-\kapShare}
```

which is a constant returns to scale production function in
{math}`\kap` and {math}`\labor \hLucas`.

Capital accumulation proceeds via the usual differential equation,

```{math}
:label: eq:Lucas-kdot

\dot{k} = \yRat - \cRat - (\popGro+\depr) \kap,
```

while {math}`\hLucas` accumulates according to

```{math}
:label: eq:hdot

\begin{gathered}\begin{aligned}
  \dot{\hLucas} & =  \phi \hLucas (1-\labor)
\\ \dot{\hLucas}/h & =  \phi (1-\labor).
\end{aligned}\end{gathered}
```

## Discussion

Before analyzing the model, an aside. {cite:t}`mankiw:growth` has persuasively
argued for defining 'knowledge' as the sum
total of technological and scientific discoveries (what is
written in textbooks, scholarly journals, websites, and the like),
and defining 'human capital' as the stock of knowledge
that has been transmitted from those sources into human brains via
studying.

Recall {cite:t}`rebelo:long`'s key insight about endogenous growth models: In order
to produce perpetual growth, there must be a factor or a combination
of factors that can be accumulated indefinitely without diminishing
returns. Mankiw points out that since lifetimes are finite, there is a
maximum limit to the amount of human capital that an individual can accumulate.

Thus, while increasing human capital (with more years of schooling,
for example) may be able to extend the length of the transition period
in a growth model, human capital accumulation cannot be the source of
perpetual growth. It is more plausible to think that scientific knowledge can be
accumulated indefinitely (though presumably there is some limit even
to the accumulation of knowledge). These considerations
suggest that models of endogenous growth should focus more on
understanding the process of fundamental research and technological
development than on human capital accumulation as Mankiw defines it.

With this distinction in mind, there are (at least) two
interpretations of the Lucas model. One is at the aggregate level.

Here we can think of {math}`\labor` as the fraction of the population
engaged in useful work to produce goods and services, while proportion
{math}`1-\labor` is not working in conventional boring jobs that require
asking customers questions like "Would you like
fries with that?" but instead is producing 'knowledge' by
conducting scientific and technological research.

The other interpretation is at the level of an individual agent. Such
an agent can be thought of as operating his or her own production
function of the form in {eq}`eq:pcy`, where {math}`(1-\labor)` is now interpreted as the proportion of the time this individual spends studying and {math}`\labor` is the time spent working.

From the point of view of
Mankiw's distinction, it is hard to interpret Lucas's model as being
either about human capital accumulation or about knowledge. It can't
be about human capital because {math}`\hLucas` can be accumulated without bound,
and without diminishing returns, neither of which makes sense for an
individual. It can't be about generalized knowledge, because the
optimization problem reflects the return for an individual, while only
a trivial proportion of total knowledge (in Mankiw's sense) is
contributed by any single individual.

Given these considerations, it probably makes more sense to think of the
model as a tool for normative than for positive analysis.

## The Solow Version

We analyze first the 'Solow' version of the model, in which
the saving rate is exogenously fixed at {math}`s`. Thus the
capital accumulation equation becomes

```{math}
:label: eq:kdots

\begin{gathered}\begin{aligned}
  \dot{\kap} & =  \save \yRat - (\popGro+\depr) \kap
\\ \dot{\kap}/\kap & =  \save (\yRat/\kap) - (\popGro+\depr)
\\ & =  \save \PtyLev \kRat^{\kapShare - 1} (\labor \hLucas)^{1-\kapShare}-(\popGro+\depr)
\\ & =  \save \PtyLev (\kap/\hLucas)^{\kapShare-1} \labor^{1-\kapShare} -(\popGro+\depr).
\end{aligned}\end{gathered}
```

This equation tells us that the steady-state growth
rate in this model (if one exists) requires a constant
ratio of {math}`\kap` to {math}`\hLucas`. Thus, {math}`\kap` and {math}`\hLucas` must be growing
at the same rate in equilibrium.

Further insight can be obtained by defining {math}`\hat{A} = \PtyLev \labor^{1-\kapShare}`
and rewriting the per-capita production function as

```{math}
:label: eq:CRSprodfunc

\begin{gathered}\begin{aligned}
  \yRat & =  \hat{\PtyLev} \kRat^{\kapShare} \hLucas^{1-\kapShare}.
\end{aligned}\end{gathered}
```

If we define a measure of 'broad capital' as the combination
of physical capital and human capital,

```{math}
:label: eq:kappa

\kappa \equiv \kRat^\kapShare \hLucas^{1-\kapShare},
```

the model becomes

```{math}
:label: eq:ak

\yRat = \hat{\PtyLev} \kappa.
```

So if {math}`\labor` is constant and if {math}`\kap` and {math}`\hLucas` are growing at the same rate,
then the exponent on 'broad capital' is 1, and we are effectively back
at the usual Rebelo {math}`\PtyLev \Kap` model.

The key assumption that permits this to work is the accumulation
equation for human capital, which is itself like an {math}`\PtyLev \Kap` model, in the
sense that the exponent on human capital in the accumulation equation
for human capital is one. Human capital can be accumulated without
bound and without diminishing returns.

## The Ramsey/Cass-Koopmans Version

Lucas does not examine the Solow version of the model with a constant
saving rate, but instead the version in which a social planner solves
for the optimal perfect foresight paths of the two state variables {math}`\kap`
and {math}`\hLucas`. It's not worth going through the math here; I'll just
present the conclusion, which is that the steady-state growth rate is

```{math}
:label: eq:Lucas-ssg

\dot{c}/c = \CRRA^{-1}(\phi - \theta).
```

Note that this confirms the crucial role of the CRS accumulation
equation for human capital: The key parameter that corresponds to
the interest rate is {math}`\phi`, the parameter that determines the efficiency
of human capital accumulation in equation {eq}`eq:hdot`.

Lucas also solves a version of the model in which there is an
externality to human capital. The idea here is that each person
is more productive if they are surrounded by other people with high
levels of human capital. Specifically, in this version of the model
the individual's production function is

```{math}
:label: eq:pcyext

\yRat_i = \PtyLev \kap_{i}^{\kapShare} (\labor _{i}\hLucas_{i})^{1-\kapShare} \bar{\hLucas}^{\psi}
```

where {math}`\bar{\hLucas}` is average human wealth in the population (and the
other variables reflect the values for the individual).

Working through the decentralized solution, Lucas shows that the
steady-state growth rate of human capital for an individual consumer
will be

```{math}
:label: eq:indgrow

\begin{gathered}\begin{aligned}
  \gamma_\hLucas &  =  \left(\frac{\CRRA^{-1}(\phi-\theta)}{1+\psi(1-1/\CRRA)/(1-\kapShare)}\right) .
\end{aligned}\end{gathered}
```

Since every individual is assumed to be identical, the growth rate
of aggregate human capital (and everything else) is the same as
the rate for this individual.

It is easy to see that if there is no externality to human capital
accumulation (that is, if {math}`\psi = 0`), this solution is identical to
{eq}`eq:Lucas-ssg`. If there is an externality, its effect depends on
whether {math}`1/\CRRA` is greater than, equal to, or less than 1. This is
because the effect depends on whether the externality causes the
saving rate to rise or to fall (since in endogenous growth models,
saving is the source of all growth). The {math}`\bar{\hLucas}` externality is like an
increase in the interest rate, and thus its effect will be determined
by the balance between the income and substitution effects. We know
that for {math}`\CRRA=1` the income and substitution effects exactly offset
each other, leaving consumption unchanged in response to an
increase in the interest rate, which is why {eq}`eq:indgrow`
collapses to {eq}`eq:Lucas-ssg` for {math}`\CRRA=1`. If consumers are very
willing to cut current consumption in exchange for higher future
consumption (that is, if the intertemporal elasticity of substitution
{math}`(1/\CRRA)` is greater than 1), then the externality boosts saving
and therefore growth. If consumers have an intertemporal elasticity
of less than one, the income effect outweighs the substitution effect,
saving falls, and growth is slower.

Lucas also shows that this decentralized solution is suboptimal,
because individual consumers do not obtain the full benefits to
society of increasing their own stock of knowledge. Devoting more
time to {math}`\hLucas_i` accumulation they increase {math}`\bar{\hLucas}`, which benefits all
others in the economy in addition to themselves. Lucas shows,
unsurprisingly, that the socially optimal solution requires greater
investment in human capital accumulation than is obtained in the
decentralized model. He also derives an optimal subsidy to human
capital accumulation that corrects the externality and induces
households to invest the socially optimal amount in human capital.
