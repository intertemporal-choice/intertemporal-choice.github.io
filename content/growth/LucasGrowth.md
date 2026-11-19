(sec:LucasGrowth)=
# The Lucas (1988) Model

{cite:t}`lucasGrowth` presents a growth model in which output is generated via a production function of the form

```{math}
:label: eq:aggY

\YLvl = \PtyAgg \KLvl^{\kapShare} (\labor \hCap \LLvl)^{1-\kapShare}
```

where {math}`\YLvl`, {math}`\PtyAgg`, {math}`\KLvl` and {math}`\LLvl` are as usually defined, {math}`0 < \kapShare < 1`, {math}`\labor` is the proportion of total labor time
spent working, and {math}`\hCap` is what Lucas calls the stock of 'human
capital.'

The production function can be rewritten in per-capita terms as

```{math}
:label: eq:pcy

\yNrm = \PtyAgg \kNrm^\kapShare (\labor \hCap)^{1-\kapShare}
```

which is a constant returns to scale production function in
{math}`\kNrm` and {math}`\labor \hCap`.

Capital accumulation proceeds via the usual differential equation,

```{math}
:label: eq:Lucas-kdot

\dot{\kNrm} = \yNrm - \cNrm - (\PopnGroRte+\deprRte) \kNrm,
```

:::{margin}
The population growth rate is written {math}`\PopnGroRte`: {math}`\PopnGroFac` is the population's growth factor and {math}`\lnat` is the natural log, so {math}`\PopnGroRte = \log \PopnGroFac`.
:::

while {math}`\hCap` accumulates according to

```{math}
:label: eq:hdot

\begin{gathered}\begin{aligned}
  \dot{\hCap} & =  \hCapProd \hCap (1-\labor)
\\ \dot{\hCap}/\hCap & =  \hCapProd (1-\labor).
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

Recall {cite:t}`rebelo:long`'s [key insight](#sec:Endogenous) about endogenous growth models: In order
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
be about human capital because {math}`\hCap` can be accumulated without bound,
and without diminishing returns, neither of which makes sense for an
individual. It can't be about generalized knowledge, because the
optimization problem reflects the return for an individual, while only
a trivial proportion of total knowledge (in Mankiw's sense) is
contributed by any single individual.

Given these considerations, it probably makes more sense to think of the
model as a tool for normative than for positive analysis.

## The Solow Version

We analyze first the 'Solow' version of the model, in which
the saving rate is exogenously fixed at {math}`\savRte`. Thus the
capital accumulation equation becomes

```{math}
:label: eq:kdots

\begin{gathered}\begin{aligned}
  \dot{\kNrm} & =  \savRte \yNrm - (\PopnGroRte+\deprRte) \kNrm
\\ \dot{\kNrm}/\kNrm & =  \savRte (\yNrm/\kNrm) - (\PopnGroRte+\deprRte)
\\ & =  \savRte \PtyAgg \kNrm^{\kapShare - 1} (\labor \hCap)^{1-\kapShare}-(\PopnGroRte+\deprRte)
\\ & =  \savRte \PtyAgg (\kNrm/\hCap)^{\kapShare-1} \labor^{1-\kapShare} -(\PopnGroRte+\deprRte).
\end{aligned}\end{gathered}
```

This equation tells us that the steady-state growth
rate in this model (if one exists) requires a constant
ratio of {math}`\kNrm` to {math}`\hCap`. Thus, {math}`\kNrm` and {math}`\hCap` must be growing
at the same rate in equilibrium.

Further insight can be obtained by rewriting the per-capita production function as

```{math}
:label: eq:CRSprodfunc

\begin{gathered}\begin{aligned}
  \yNrm & =  (\PtyAgg \labor^{1-\kapShare}) \kNrm^{\kapShare} \hCap^{1-\kapShare}.
\end{aligned}\end{gathered}
```

If we define a measure of 'broad capital' as the combination
of physical capital and human capital,

```{math}
:label: eq:Lucas-broadCap

\kNrm^\kapShare \hCap^{1-\kapShare},
```

the model becomes

```{math}
:label: eq:ak

\yNrm = (\PtyAgg \labor^{1-\kapShare}) (\kNrm^\kapShare \hCap^{1-\kapShare}).
```

So if {math}`\labor` is constant and if {math}`\kNrm` and {math}`\hCap` are growing at the same rate,
then the exponent on 'broad capital' is 1, and we are effectively back
at the usual [Rebelo {math}`\PtyAgg \KLvl` model](#sec:RebeloAK).

The key assumption that permits this to work is the accumulation
equation for human capital, which is itself like an {math}`\PtyAgg \KLvl` model, in the
sense that the exponent on human capital in the accumulation equation
for human capital is one. Human capital can be accumulated without
bound and without diminishing returns.

## The Ramsey/Cass-Koopmans Version

Lucas does not examine the Solow version of the model with a constant
saving rate, but instead the version in which a social planner solves
for the optimal perfect foresight paths of the two state variables {math}`\kNrm`
and {math}`\hCap`. It's not worth going through the math here; I'll just
present the conclusion, which is that the steady-state growth rate is

```{math}
:label: eq:Lucas-ssg

\dot{\cNrm}/\cNrm = \CRRA^{-1}(\hCapProd - \discRte).
```

:::{margin}
The planner maximizes the discounted sum of CRRA utility from per capita consumption, with time preference rate {math}`\discRte`, counting each date's per capita utility once, as [the RCK model's planner](#eq:RCK-maxprob) does. Lucas weights utility by the size of the population, which replaces {math}`\discRte` with {math}`\discRte-\PopnGroRte` here and in the decentralized growth rate below.
:::

:::{margin}
Human capital grows at the same rate as consumption, so by {eq}`eq:hdot` the time spent working is {math}`\labor = 1-\CRRA^{-1}(\hCapProd-\discRte)/\hCapProd`. It is positive, and utility finite, only if growth is below the return, {math}`\CRRA^{-1}(\hCapProd-\discRte) < \hCapProd`: the condition of the [Rebelo model](#sec:RebeloAK), with {math}`\hCapProd` in place of {math}`\PtyAgg`.
:::

Note that this confirms the crucial role of the CRS accumulation
equation for human capital: The key parameter that corresponds to
the interest rate is {math}`\hCapProd`, the parameter that determines the efficiency
of human capital accumulation in equation {eq}`eq:hdot`. So {eq}`eq:Lucas-ssg` is the RCK model's [Keynes-Ramsey rule](#eq:cdotOc), consumption growth equal to {math}`\CRRA^{-1}` times the excess of a return over the time preference rate, with the return {math}`\hCapProd` on time spent building human capital.

Lucas also solves a version of the model in which there is an
externality to human capital. The idea here is that each person
is more productive if they are surrounded by other people with high
levels of human capital. Specifically, in this version of the model
the individual's production function is

```{math}
:label: eq:pcyext

\yNrm_i = \PtyAgg \kNrm_{i}^{\kapShare} (\labor _{i}\hCap_{i})^{1-\kapShare} \hCapAvg^{\extElas}
```

where {math}`\hCapAvg` is average human capital in the population (and the
other variables reflect the values for the individual), and {math}`\extElas` is the elasticity of the individual's output with respect to {math}`\hCapAvg`, as {math}`\extElas` is with respect to knowledge in [Romer's model](#sec:Romer86).

Working through the decentralized solution, Lucas shows that the
steady-state growth rate of human capital for an individual consumer
will be

```{math}
:label: eq:indgrow

\begin{gathered}\begin{aligned}
  \dot{\hCap}/\hCap &  =  \left(\frac{\CRRA^{-1}(\hCapProd-\discRte)}{1+\extElas(1-1/\CRRA)/(1-\kapShare)}\right) .
\end{aligned}\end{gathered}
```

Since every individual is assumed to be identical, the growth rate
of average human capital is the same as
the rate for this individual.

It is easy to see that if there is no externality to human capital
accumulation (that is, if {math}`\extElas = 0`), this solution is identical to
{eq}`eq:Lucas-ssg`. If there is an externality, its effect on the growth of human capital depends on
whether {math}`1/\CRRA` is greater than, equal to, or less than 1. This is
because the effect depends on whether the externality causes
saving, here the time spent studying, to rise or to fall (since in endogenous growth models,
saving is the source of all growth). The {math}`\hCapAvg` externality is like an
increase in the interest rate, and thus its effect will be determined
by the balance between the income and substitution effects. We know
that for {math}`\CRRA=1` the income and substitution effects exactly offset
each other, leaving the marginal propensity to consume out of
wealth unchanged in response to an increase in the interest
rate, which is why {eq}`eq:indgrow`
collapses to {eq}`eq:Lucas-ssg` for {math}`\CRRA=1`. If consumers are very
willing to cut current consumption in exchange for higher future
consumption (that is, if the intertemporal elasticity of substitution
{math}`(1/\CRRA)` is greater than 1), then the externality boosts saving
and therefore growth. If consumers have an intertemporal elasticity
of less than one, the income effect outweighs the substitution effect,
saving falls, and human capital grows more slowly. In every case, physical capital, output and consumption per capita grow faster than they would without the externality.

:::{margin}
The externality is the first of the failures of the welfare theorem's assumptions listed in [Decentralizing the Ramsey/Cass-Koopmans Model](#sec:DecRCK-Failures): the private return to human capital falls short of its social return, the same kind of wedge that a [tax on capital income](#sec:RCKGov-CapitalTax) drives between the private and the social return to saving in the RCK model with government.
:::

Lucas also shows that this decentralized solution is suboptimal,
because individual consumers do not obtain the full benefits to
society of increasing their own human capital. Devoting more
time to {math}`\hCap_i` accumulation they increase {math}`\hCapAvg`, which benefits all
others in the economy in addition to themselves. Lucas shows,
unsurprisingly, that the socially optimal solution requires greater
investment in human capital accumulation than is obtained in the
decentralized model. He also derives an optimal subsidy to human
capital accumulation that corrects the externality and induces
households to invest the socially optimal amount in human capital.
