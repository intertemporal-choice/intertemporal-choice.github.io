(sec:RamseyCassKoopmans)=
# The Ramsey/Cass-Koopmans (RCK) Model

{cite:t}`ramseySave`, followed much later by {cite:t}`cass:growth` and {cite:t}`koopmans:growth`, formulated the canonical model of optimal growth for an economy with exogenous 'labor-augmenting' technological progress. This chapter follows the textbook treatment in {cite:t}`blanchard&fischer:text`, chapter 2; {cite:t}`barro&salaimartin:book`, chapter 2, is another.

## The Budget Constraint

The economy has a perfectly competitive production sector that uses a Cobb-Douglas aggregate production function

```{math}
\begin{gathered}\begin{aligned}
                   \Inc & =  \ProdFunc(\Kap,\Labor) = \Kap^{\kapShare}(\PtyLab \Labor)^{1-\kapShare}
\end{aligned}\end{gathered}
```

to produce output using capital and labor.[^DGoP2Gjmvh] Labor hours (the same as population) increase exogenously at a constant rate

[^DGoP2Gjmvh]: All Roman variables are functions of time, but putting time subscripts on everything would clutter the notation, so we do it only where necessary for clarity.

```{math}
\begin{gathered}\begin{aligned}
  \dot{\Labor}/\Labor & =  \popGro
\end{aligned}\end{gathered}
```

and {math}`\PtyLab` is an index of labor productivity that grows at rate

```{math}
\begin{gathered}\begin{aligned}
  \dot{\PtyLab }/\PtyLab  & =  \ptyGro. 
\end{aligned}\end{gathered}
```

Thus, technological progress allows each worker to
produce perpetually more as time goes by with the same amount of
physical capital.[^QeBMSQU4dN] The quantity {math}`\PtyLab \Labor` is known as the number of 'efficiency units' of labor in the economy.

:::{margin}
Writing progress in {math}`\PtyLab \Labor` form is a peculiar assumption; it seems more natural to imagine technology embodied in new {math}`\Kap`. Solow (1960) and Phelps (1962) showed that steady-state growth does not depend on how much of technical progress is embodied in new capital, though convergence is faster the more of it is embodied; so the simpler disembodied form delivers the same steady-state growth rate.
:::

[^QeBMSQU4dN]: This is the definition of 'labor-augmenting' (Harrod-neutral) productivity growth. Progress can also augment capital, {math}`\ProdFunc(\PtyLab \Kap,\Labor)` ('Solow-neutral'), or output, {math}`\PtyLab \ProdFunc(\Kap,\Labor)` ('Hicks-neutral'). With a Cobb-Douglas production function the three are the same thing at different rates. With any other production function, a steady state with constant growth rates requires progress to be labor-augmenting (Uzawa 1961; Jones and Scrimgeour 2008 give a short proof).

Aggregate capital accumulates according to

```{math}
:label: eq:Kdotlevel

\begin{gathered}\begin{aligned}
  \dot{\Kap} & =  \Inc - \Cons - \depr \Kap .
\end{aligned}\end{gathered}
```

Lower case variables are the upper case version divided by efficiency units, so {math}`\inc = \Inc/(\PtyLab \Labor) = (\Kap/\PtyLab \Labor)^{\kapShare} = \kap^{\kapShare}`. Since {math}`\kap = \Kap/(\PtyLab \Labor)`,

```{math}
\dot{\kap}/\kap = \dot{\Kap}/\Kap - \dot{\PtyLab}/\PtyLab - \dot{\Labor}/\Labor = \dot{\Kap}/\Kap - (\ptyGro +\popGro),
```

so dividing {eq}`eq:Kdotlevel` by {math}`\PtyLab \Labor` and using it gives

```{math}
:label: eq:RCK-kdot

\dot{\kap} = \prodFunc(\kap) - \cons - (\ptyGro +\popGro+\depr) \kap .
```

A steady state is a point where {math}`\dot{\kap} = 0`, so that {math}`\cons = \prodFunc(\kap) - (\ptyGro +\popGro+\depr) \kap`. A first candidate for the best steady state is the one with the highest {math}`\cons`. Setting the derivative with respect to {math}`\kap` to zero gives the "golden rule" of {cite:t}`phelps:golden`, an article well worth reading:

```{math}
:label: eq:RCK-goldenRule

\prodFunc^{\prime}(\GoldRule{\kap}) = \ptyGro +\popGro+\depr .
```

## The Social Planner's Problem

Now suppose that there is a social planner whose goal is to maximize the discounted
sum of CRRA utility from per-capita consumption:[^RCKpopWeight]

[^RCKpopWeight]: This objective counts each date's per capita utility once, as {cite:t}`blanchard&fischer:text` do. {cite:t}`romer:text` weights it by the size of the population, which replaces {math}`\timeRate` with {math}`\timeRate-\popGro` below, and takes {math}`\popGro` out of the steady-state condition.

```{math}
:label: eq:RCK-maxprob

\max \int_{0}^{\infty} \left(\frac{(\Cons/\Labor)^{1-\CRRA}}{1-\CRRA}\right) e^{-\timeRate  t}\,dt .
```

But {math}`\Cons/\Labor = \PtyLab (\Cons/\PtyLab \Labor)= \PtyLab c`. Recall that for a variable growing at rate {math}`\ptyGro`,

```{math}
\begin{gathered}\begin{aligned}
  \PtyLab _{t} & =  \PtyLab _{0}e^{\ptyGro t}
\end{aligned}\end{gathered}
```

so if the economy started off in period 0 with productivity {math}`\PtyLab_{0}`, by date {math}`t` we can rewrite

```{math}
:label: eq:cRat

\begin{gathered}\begin{aligned}
  \Cons/\Labor & =  c\PtyLab   \\
               & =  c\PtyLab _{0}e^{\ptyGro t}. 
\end{aligned}\end{gathered}
```

Using {eq}`eq:cRat` and the other results above, we can rewrite the social planner's objective function as

```{math}
:label: eq:maxprobmod

\begin{gathered}\begin{aligned}
  \int_{0}^{\infty} \left(\frac{(\PtyLab c)^{1-\CRRA}}{1-\CRRA}\right) e^{-\timeRate  t}\,dt & =  
                                                                                               \PtyLab _{0}^{1-\CRRA}\int_{0}^{\infty} \left(\frac{\cons^{1-\CRRA}}{1-\CRRA}\right) e^{-\timeRate  t}e^{(1-\CRRA)\ptyGro  t}\,dt 
  \\ & =  \PtyLab _{0}^{1-\CRRA}\int_{0}^{\infty} \util(c) e^{\left((1-\CRRA)\ptyGro -\timeRate \right) t}\,dt
           .
\end{aligned}\end{gathered}
```

Thus, defining {math}`\nu = \timeRate  - (1-\CRRA) \ptyGro`, which we assume is positive so that the objective is finite, and normalizing the initial
level of productivity to {math}`\PtyLab _{0}=1`, the complete optimization problem
can be formulated as

```{math}
\max \int_{0}^{\infty} \util(c) e^{-\nu  t}\,dt
```

subject to

```{math}
\dot{\kap} = \kap^{\kapShare}-\cons-(\popGro+\ptyGro+\depr)k,
```

which has a discounted Hamiltonian representation

```{math}
\Ham(\kap,c,\lambda) = \util(c) + (\kap^{\kapShare} - \cons - (\popGro+\ptyGro+\depr)\kap)\lambda.
```

The first [discounted Hamiltonian optimization condition](https://en.wikipedia.org/wiki/Hamiltonian_\(control_theory\)) requires {math}`\partial 
 \Ham/\partial \cons = 0`:

```{math}
:label: eq:RCK-H1A

\begin{gathered}\begin{aligned}
  c^{-\CRRA} & =  \lambda   \\
  -\CRRA c^{-\CRRA-1}\dot{\cons} & =  \dot{\lambda} 
                                       .
\end{aligned}\end{gathered}
```

The second discounted Hamiltonian optimization condition requires:

```{math}
\begin{gathered}\begin{aligned}
  \dot{\lambda} & =  \nu\lambda - \partial \Ham/\partial \kap  \\
                & =  \nu\lambda - \lambda (\prodFunc^{\prime}(\kap) - (\popGro+\ptyGro+\depr))  \\
  \dot{\lambda}/{\lambda} & =  (\nu+(\popGro+\ptyGro+\depr)-\prodFunc^{\prime}(\kap))
  \\  \left(\frac{-\CRRA c^{-\CRRA-1}\dot{\cons}}{\cons^{-\CRRA}}\right) & =  (\nu+(\popGro+\ptyGro+\depr)-\prodFunc^{\prime}(\kap))
  \\  \CRRA \dot{\cons}/\cons & =  (\prodFunc^{\prime}(\kap)-\nu-(\popGro+\ptyGro+\depr))
  \\  \dot{\cons}/\cons  & =  \CRRA^{-1}(\prodFunc^{\prime}(\kap)-(\popGro+\ptyGro+\depr)-\nu)
\end{aligned}\end{gathered}
```

where {math}`\rfree \equiv \prodFunc^{\prime}(\kap) - \depr` is the interest rate, so {math}`\prodFunc^{\prime}(\kap)-(\popGro+\ptyGro+\depr) = \rfree - \popGro - \ptyGro` is the interest rate net of depreciation and dilution.

This Euler equation is called the "Keynes-Ramsey rule," because it was originally derived by
Ramsey with an explanation attributed to Keynes.
It is just like [the Euler equation in the perfect foresight CRRA model](#eq:PFCRRA-cgrow), except that now the relevant interest rate can vary over
time as {math}`\prodFunc^{\prime}(\kap)` varies.

Substituting in the modified time preference rate gives

```{math}
:label: eq:cdotOc

\begin{gathered}\begin{aligned}
  \dot{\cons}/\cons  & =  \CRRA^{-1}(\prodFunc^{\prime}(\kap)-(\popGro+\depr+\ptyGro)-\timeRate  +(1- \CRRA) \ptyGro)
  \\   & =  \CRRA^{-1}(\prodFunc^{\prime}(\kap)-(\popGro+\depr)-\timeRate  - \CRRA \ptyGro). 
\end{aligned}\end{gathered}
```

Since per capita consumption is {math}`\Cons/\Labor = \cons \PtyLab`, it grows at {math}`\dot{\cons}/\cons + \ptyGro = \CRRA^{-1}(\prodFunc^{\prime}(\kap)-(\popGro+\depr)-\timeRate)`: the same formula, as a function of {math}`\kap`, as in the model with no productivity growth ({eq}`eq:cdotOc` with {math}`\ptyGro=0`). Productivity growth matters only through {math}`\kap`.

## The Steady State

The assumption of labor augmenting technological progress was made
because it implies that in steady-state, per-capita consumption, income,
and capital all grow at rate {math}`\ptyGro`.[^x66RuMjc3A]

[^x66RuMjc3A]: See {cite:t}`ghosDespiteUzawa` for a discussion of the realism of this requirement.

{math}`\dot{\cons}/\cons = 0` implies that at the steady-state value of {math}`\check{\kap}`,

```{math}
:label: eq:RCK-modGoldenRule

\begin{gathered}\begin{aligned}
  \prodFunc^{\prime}(\check{\kap}) & =  \timeRate +\popGro+\depr+\CRRA \ptyGro  \\
  \kapShare \check{\kap}^{\kapShare-1} & =  \timeRate +\popGro+\depr+\CRRA \ptyGro  \\
  \check{\kap} & =  \left(\frac{\kapShare}{\timeRate +\popGro+\depr+\CRRA \ptyGro}\right)^{\frac{1}{1-\kapShare}}   
\end{aligned}\end{gathered}
```

This is the "modified golden rule" of {cite:t}`blanchard&fischer:text`, chapter 2. Comparing it with the [golden rule](#eq:RCK-goldenRule), {math}`\prodFunc^{\prime}(\check{\kap}) = \prodFunc^{\prime}(\GoldRule{\kap}) + \nu`, so {math}`\check{\kap} < \GoldRule{\kap}` exactly when {math}`\nu > 0`: the assumption that keeps the planner's objective finite also rules out accumulating more capital than the golden rule.

Thus, the steady-state {math}`\kap` will be higher if capital
is more productive ({math}`\kapShare` is higher), and will be lower if
consumers are more impatient, population growth is faster,
depreciation is greater, or technological progress occurs more rapidly.

## A Phase Diagram

While the RCK model has an analytical solution for its steady-state,
it does not in general have an analytical solution for the transition to the
steady-state.[^RCKclosedForm] The usual method for analyzing
models of this kind is a [phase diagram](https://en.wikipedia.org/wiki/Phase_diagram) in {math}`\cons` and {math}`\kap`.

[^RCKclosedForm]: The exception is the case in which the coefficient of relative risk aversion equals the capital share, {math}`\CRRA = \kapShare` (Smith 2006). The saddle path is then the ray {math}`\cons = \left((\timeRate + (1-\kapShare)(\popGro+\depr))/\kapShare\right)\kap` through the steady state; along it, {math}`\dot{\kap} = \kap^{\kapShare} - \left((\timeRate+\popGro+\depr)/\kapShare + \ptyGro\right)\kap` is a Bernoulli equation, so the transition has a closed form.

The first step in constructing the phase diagram is to take the differential
equations that describe the system and find the points where they are
zero. Thus, from {eq}`eq:RCK-kdot` we have that {math}`\dot{\kap}=0` implies

```{math}
:label: eq:RCK-kdotEq0

\begin{gathered}\begin{aligned}
  \cons & =  \prodFunc(\kap) - (\ptyGro +\popGro+\depr) \kap 
\end{aligned}\end{gathered}
```

and we have already solved for the (constant) {math}`\check{\kap}` that characterizes
the {math}`\dot{\cons}/\cons=0` locus. These can be combined to generate the borders between
the phases in the phase diagram, as illustrated in {numref}`fig:RamseySSPlot`.

:::{margin}
The programs that generated these figures are not quite consistent with the equations above: they assume {math}`\util(\cons \Labor)/\Labor`, whereas here we assume {math}`\util(\cons)`.
:::

:::{figure} /content/figures/RamseyCassKoopmans/RamseySSPlot.png
:name: fig:RamseySSPlot

{math}`\dot{\cons}/\cons =0` and {math}`\dot{\kap}=0` Loci
:::

## Transition

The two differential equations and {math}`\kap_{0}` don't pin down {math}`\cons_{0}`: every starting {math}`\cons_{0}` traces a path. The transversality condition, the counterpart of the intertemporal budget constraint, picks one:

```{math}
:label: eq:tvc

\begin{gathered}\begin{aligned}
  \lim_{t \rightarrow \infty} e^{-\int_{0}^{t} (\rfree_{\tau} -\popGro -\ptyGro)\,d\tau }\kap_{t} & =  0.
\end{aligned}\end{gathered}
```

The intuitive purpose of this unintuitive equation is basically to prevent
the capital stock from becoming negative or infinite as time goes by.

Obviously a capital stock that was negative for the entire future could not
satisfy the equation. And a capital stock that is too large has an interest rate below {math}`\popGro+\ptyGro`, so the discount term grows without bound, and so does the left side of the transversality condition.

{numref}`fig:RamseySaddlePlot` shows three paths for {math}`\cons` and {math}`\kap`
that satisfy {eq}`eq:cdotOc` and {eq}`eq:RCK-kdot`. The topmost path,
however, is clearly on a trajectory toward zero then negative
{math}`\kap`, while the bottommost path accumulates capital past the golden rule, toward the point where the
{math}`\dot{\kap}=0` locus meets the {math}`\kap` axis, with consumption falling toward zero. Only the middle path, labeled the "saddle path," satisfies
both {eq}`eq:cdotOc` and {eq}`eq:RCK-kdot` as well as the TVC
{eq}`eq:tvc`.

:::{figure} /content/figures/RamseyCassKoopmans/RamseySaddlePlot.png
:name: fig:RamseySaddlePlot

Transition to the Steady State
:::

How much of observed growth can the transition explain? Little, {cite:t}`king&rebelo:trans` argue: with plausible parameters, an economy far enough below its steady state for the transition to account for much of its growth would have implausibly high interest rates early on.

## Appendix: Numerical Solution

The RCK model does not in general have an analytical solution, which means that
numerical methods must be used to find out the model's quantitative
implications for transition paths.

The method of solution of these kinds of models is not important for
the purposes of first year graduate macroeconomics; this appendix
has been written as a reference for more advanced students who might
be beginning their research on growth models.

The most straightforward method of numerical solution for perfect foresight
models of this kind is called the
'time elimination' method (Mulligan and Sala-i-Martin 1993). It starts from the fact that

```{math}
\begin{gathered}\begin{aligned}
    \left(\frac{d\cons/dt}{d\kap/dt}\right) &=  d\cons/d\kap.
  \end{aligned}\end{gathered}
```

Note from {eq}`eq:cdotOc` that we can write

```{math}
:label: eq:cdot

\begin{gathered}\begin{aligned}
    \dot{\cons} & =   \CRRA^{-1}(\prodFunc^{\prime}(\kap)-\timeRate -(\popGro+\depr)-\CRRA \ptyGro)\cons ,
  \end{aligned}\end{gathered}
```

so we can obtain

```{math}
\begin{gathered}\begin{aligned}
    d\cons/d\kap & =  \left(\frac{(\kapShare \kap^{\kapShare-1}-\timeRate -(\popGro+\depr)-\CRRA \ptyGro)\cons}
                       {\CRRA(\kap^{\kapShare} - \cons - (\ptyGro +\popGro+\depr) \kap)}\right)
  \end{aligned}\end{gathered}
```

which is a differential equation with, in general, no analytical solution. Many numerical math packages can solve differential equations numerically, yielding a numerical version of the {math}`\cFunc(\kap)` function.

There is one problem, however, which is that at the steady-state values of {math}`\cons` and {math}`\kap` both numerator and denominator of this equation are zero. The alternative is to solve the differential equation twice: Once for a domain extending from {math}`\kap=0` to {math}`\check{\kap}-\epsilon`, yielding {math}`\cFunc_{-}(\kap)`, and once for a domain from {math}`\check{\kap}+\epsilon` to some large value of {math}`\kap`, yielding {math}`\cFunc_{+}(\kap)`. The true consumption policy function can then be approximated by interpolating between the upper endpoint of {math}`\cFunc_{-}(\kap)` and the lower endpoint of {math}`\cFunc_{+}(\kap)`.

{cite:t}`judd:book` covers numerical methods for saddle paths more generally. The [RamseyCassKoopmans notebook](https://github.com/llorracc/Jupyter/blob/master/notebooks/RamseyCassKoopmans.ipynb) implements this method; in a clone of its repo, `ipython RamseyCassKoopmans.py` runs the corresponding Python program.
