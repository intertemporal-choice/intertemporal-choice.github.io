(sec:RamseyCassKoopmans)=
# The Ramsey/Cass-Koopmans (RCK) Model

{cite:t}`ramseySave`, followed much later by {cite:t}`cass:growth` and {cite:t}`koopmans:growth`, formulated the canonical model of optimal growth for an economy with exogenous 'labor-augmenting' technological progress. This chapter follows the textbook treatment in {cite:t}`blanchard&fischer:text`, chapter 2; {cite:t}`barro&salaimartin:book`, chapter 2, is another. For the facts the model is meant to explain, and the Solow model it builds on, see the undergraduate textbook of {cite:t}`ashrafWeilGrowth`.

## The Budget Constraint

The economy has a perfectly competitive production sector that uses a Cobb-Douglas aggregate production function

```{math}
\begin{gathered}\begin{aligned}
                   \YLvl & =  \FFunc(\KLvl,\Labor) = \KLvl^{\kapShare}(\PtyLab \Labor)^{1-\kapShare}
\end{aligned}\end{gathered}
```

to produce output using capital and labor. Labor hours (the same as population) increase exogenously at a constant rate

:::{margin}
States and controls are a function of time, but putting time subscripts on everything would add clutter; we do it only where necessary for clarity.
:::

```{math}
\begin{gathered}\begin{aligned}
  \dot{\Labor}/\Labor & =  \PopnGroRte
\end{aligned}\end{gathered}
```

and {math}`\PtyLab` is an index of labor productivity that grows at rate

```{math}
\begin{gathered}\begin{aligned}
  \dot{\PtyLab }/\PtyLab  & =  \PtyGroRte. 
\end{aligned}\end{gathered}
```

Thus, technological progress allows each worker to
produce perpetually more as time goes by with the same amount of
physical capital.

:::{margin}
This is the definition of 'labor-augmenting' (Harrod-neutral) productivity growth. Progress can also augment capital, {math}`\FFunc(\PtyLab \KLvl,\Labor)` ('Solow-neutral'), or output, {math}`\PtyLab \FFunc(\KLvl,\Labor)` ('Hicks-neutral'). With any production function other than Cobb-Douglas, a steady state with constant growth rates requires progress to be labor-augmenting {cite:p}`uzawaNeutral`.
:::

The quantity {math}`\PtyLab \Labor` is known as the number of 'efficiency units' of labor in the economy.

Aggregate capital accumulates according to

```{math}
:label: eq:Kdotlevel

\begin{gathered}\begin{aligned}
  \dot{\KLvl} & =  \YLvl - \CLvl - \deprRte \KLvl .
\end{aligned}\end{gathered}
```

Lower case variables are the upper case version divided by efficiency units, so {math}`\yNrm = \YLvl/(\PtyLab \Labor) = (\KLvl/\PtyLab \Labor)^{\kapShare} = \kap^{\kapShare}`. Since {math}`\kap = \KLvl/(\PtyLab \Labor)`,

:::{margin}
NOT per-capita; this is required for '[balanced growth](#sec:RCK-SteadyState)'.
:::

```{math}
\dot{\kap}/\kap = \dot{\KLvl}/\KLvl - \dot{\PtyLab}/\PtyLab - \dot{\Labor}/\Labor = \dot{\KLvl}/\KLvl - (\PtyGroRte +\PopnGroRte),
```

so dividing {eq}`eq:Kdotlevel` by {math}`\PtyLab \Labor` and using it gives

```{math}
:label: eq:RCK-kdot

\dot{\kap} = \fFunc(\kap) - \cNrm - (\PtyGroRte +\PopnGroRte+\deprRte) \kap .
```

A steady state is a point where {math}`\dot{\kap} = 0`, so that {math}`\cNrm = \fFunc(\kap) - (\PtyGroRte +\PopnGroRte+\deprRte) \kap`. A first candidate for the best steady state is the one with the highest {math}`\cNrm`. Setting the derivative with respect to {math}`\kap` to zero gives the "golden rule" of {cite:t}`phelps:golden`, an article well worth reading:

```{math}
:label: eq:RCK-goldenRule

\fFunc^{\prime}(\GoldRule{\kap}) = \PtyGroRte +\PopnGroRte+\deprRte .
```

## The Social Planner's Problem

Now suppose that there is a social planner whose goal is to maximize the discounted
sum of CRRA utility from per-capita consumption:

:::{margin}
This objective counts each date's per capita utility once, as {cite:t}`blanchard&fischer:text` do. {cite:t}`romer:text` weights it by the size of the population, which replaces {math}`\discRte` with {math}`\discRte-\PopnGroRte` below, and takes {math}`\PopnGroRte` out of the steady-state condition.
:::

```{math}
:label: eq:RCK-maxprob

\max \int_{0}^{\infty} \left(\frac{(\CLvl/\Labor)^{1-\CRRA}}{1-\CRRA}\right) e^{-\discRte  t}\,dt .
```

But {math}`\CLvl/\Labor = \PtyLab (\CLvl/\PtyLab \Labor)= \PtyLab \cNrm`. Recall that for a variable growing at rate {math}`\PtyGroRte`,

```{math}
\begin{gathered}\begin{aligned}
  \PtyLab _{t} & =  \PtyLab _{0}e^{\PtyGroRte t}
\end{aligned}\end{gathered}
```

so if the economy started off in period 0 with productivity {math}`\PtyLab_{0}`, by date {math}`t` we can rewrite

```{math}
:label: eq:cRat

\begin{gathered}\begin{aligned}
  \CLvl/\Labor & =  \cNrm\PtyLab   \\
               & =  \cNrm\PtyLab _{0}e^{\PtyGroRte t}. 
\end{aligned}\end{gathered}
```

Using {eq}`eq:cRat` and the other results above, we can rewrite the social planner's objective function as

```{math}
:label: eq:maxprobmod

\begin{gathered}\begin{aligned}
  \int_{0}^{\infty} \left(\frac{(\PtyLab \cNrm)^{1-\CRRA}}{1-\CRRA}\right) e^{-\discRte  t}\,dt & =  
                                                                                               \PtyLab _{0}^{1-\CRRA}\int_{0}^{\infty} \left(\frac{\cNrm^{1-\CRRA}}{1-\CRRA}\right) e^{-\discRte  t}e^{(1-\CRRA)\PtyGroRte  t}\,dt 
  \\ & =  \PtyLab _{0}^{1-\CRRA}\int_{0}^{\infty} \uFunc(\cNrm) e^{\left((1-\CRRA)\PtyGroRte -\discRte \right) t}\,dt
           .
\end{aligned}\end{gathered}
```

Thus, assuming {math}`\discRte > (1-\CRRA) \PtyGroRte`, so that the objective is finite (that is, imposing the [growth impatience condition](#eq:PatWGroCond)), and normalizing the initial
level of productivity to {math}`\PtyLab _{0}=1`, the complete optimization problem
can be formulated as

```{math}
\max \int_{0}^{\infty} \uFunc(\cNrm) e^{-(\discRte - (1-\CRRA)\PtyGroRte) t}\,dt
```

subject to

```{math}
\dot{\kap} = \kap^{\kapShare}-\cNrm-(\PopnGroRte+\PtyGroRte+\deprRte)\kap,
```

which has a current-value Hamiltonian representation

:::{margin}
If the Hamiltonian is new to you, Peter Thompson's [lecture notes on optimal control](https://www.andrew.cmu.edu/course/88-737/optimal_control/optimal_control.pdf) derive the method from the economics of a firm's capital problem, and later work through this model. Wikipedia's worked example of this model, linked from the two optimization conditions, uses the present-value Hamiltonian instead, whose costate is this one discounted to date zero.
:::

```{math}
\Ham(\kap,\cNrm,\vk) = \uFunc(\cNrm) + (\kap^{\kapShare} - \cNrm - (\PopnGroRte+\PtyGroRte+\deprRte)\kap)\vk.
```

The first [current-value Hamiltonian optimization condition](https://en.wikipedia.org/wiki/Hamiltonian_\(control_theory\)#Example:_Ramsey%E2%80%93Cass%E2%80%93Koopmans_model) requires {math}`\partial 
 \Ham/\partial \cNrm = 0`:

```{math}
:label: eq:RCK-H1A

\begin{gathered}\begin{aligned}
  \cNrm^{-\CRRA} & =  \vk   \\
  -\CRRA \cNrm^{-\CRRA-1}\dot{\cNrm} & =  \dot{\vk} 
                                       .
\end{aligned}\end{gathered}
```

The second [current-value Hamiltonian optimization condition](https://en.wikipedia.org/wiki/Hamiltonian_\(control_theory\)#Example:_Ramsey%E2%80%93Cass%E2%80%93Koopmans_model) requires:

```{math}
\begin{gathered}\begin{aligned}
  \dot{\vk} & =  (\discRte-(1-\CRRA)\PtyGroRte)\vk - \partial \Ham/\partial \kap  \\
                & =  (\discRte-(1-\CRRA)\PtyGroRte)\vk - \vk (\fFunc^{\prime}(\kap) - (\PopnGroRte+\PtyGroRte+\deprRte))  \\
  \dot{\vk}/{\vk} & =  \discRte+\PopnGroRte+\deprRte+\CRRA \PtyGroRte-\fFunc^{\prime}(\kap) .
\end{aligned}\end{gathered}
```

Since {eq}`eq:RCK-H1A` gives {math}`\dot{\vk}/\vk = -\CRRA\dot{\cNrm}/\cNrm`, this is

```{math}
:label: eq:cdotOc

\dot{\cNrm}/\cNrm = \CRRA^{-1}(\fFunc^{\prime}(\kap)-(\PopnGroRte+\deprRte)-\discRte - \CRRA \PtyGroRte),
```

or, with {math}`\rfree \equiv \fFunc^{\prime}(\kap) - \deprRte` the interest rate, {math}`\dot{\cNrm}/\cNrm = \CRRA^{-1}(\rfree - \discRte - \PopnGroRte) - \PtyGroRte`.

This Euler equation is called the "Keynes-Ramsey rule," because it was originally derived by
Ramsey with an explanation attributed to Keynes.
It is just like [the Euler equation in the perfect foresight CRRA model](#eq:PFCRRA-cgrow), except that now the relevant interest rate can vary over
time as {math}`\fFunc^{\prime}(\kap)` varies.

Since per capita consumption is {math}`\CLvl/\Labor = \cNrm \PtyLab`, it grows at {math}`\dot{\cNrm}/\cNrm + \PtyGroRte = \CRRA^{-1}(\fFunc^{\prime}(\kap)-(\PopnGroRte+\deprRte)-\discRte)`: the same formula, as a function of {math}`\kap`, as in the model with no productivity growth, the [Euler equation](#eq:cdotOc) with {math}`\PtyGroRte=0`. Productivity growth matters only through {math}`\kap`.

(sec:RCK-SteadyState)=
## The Steady State

The assumption of labor augmenting technological progress was made
because it implies that in steady-state, per-capita consumption, income,
and capital all grow at rate {math}`\PtyGroRte`.

:::{margin}
See {cite:t}`ghosDespiteUzawa` for a discussion of the realism of this requirement.
:::

{math}`\dot{\cNrm}/\cNrm = 0` implies that at the steady-state value of {math}`\Steady{\kap}`,

```{math}
:label: eq:RCK-modGoldenRule

\begin{gathered}\begin{aligned}
  \fFunc^{\prime}(\Steady{\kap}) & =  \discRte +\PopnGroRte+\deprRte+\CRRA \PtyGroRte  \\
  \kapShare \Steady{\kap}^{\kapShare-1} & =  \discRte +\PopnGroRte+\deprRte+\CRRA \PtyGroRte  \\
  \Steady{\kap} & =  \left(\frac{\kapShare}{\discRte +\PopnGroRte+\deprRte+\CRRA \PtyGroRte}\right)^{\frac{1}{1-\kapShare}}   
\end{aligned}\end{gathered}
```

This is the "modified golden rule" of {cite:t}`blanchard&fischer:text`, chapter 2. Comparing it with the [golden rule](#eq:RCK-goldenRule), {math}`\fFunc^{\prime}(\Steady{\kap}) - \fFunc^{\prime}(\GoldRule{\kap}) = \discRte - (1-\CRRA)\PtyGroRte`, so {math}`\Steady{\kap} < \GoldRule{\kap}` exactly when {math}`\discRte > (1-\CRRA)\PtyGroRte`: the assumption that keeps the planner's objective finite also rules out accumulating more capital than the golden rule.

Thus, the steady-state {math}`\kap` will be higher if capital
is more productive ({math}`\kapShare` is higher), and will be lower if
consumers are more impatient, population growth is faster,
depreciation is greater, or technological progress occurs more rapidly.

## A Phase Diagram

While the RCK model has an analytical solution for its steady-state,
it does not in general have an analytical solution for the transition to the
steady-state. The usual method for analyzing
models of this kind is a [phase diagram](https://en.wikipedia.org/wiki/Phase_diagram) in {math}`\cNrm` and {math}`\kap`.

:::{margin}
The exception is the case in which the coefficient of relative risk aversion equals the capital share, {math}`\CRRA = \kapShare` {cite:p}`smithClosedForm`. The saddle path is then the ray {math}`\cNrm = \left((\discRte + (1-\kapShare)(\PopnGroRte+\deprRte))/\kapShare\right)\kap` through the steady state; along it, {math}`\dot{\kap} = \kap^{\kapShare} - \left((\discRte+\PopnGroRte+\deprRte)/\kapShare + \PtyGroRte\right)\kap` is a Bernoulli equation, so the transition has a closed form.
:::

The first step in constructing the phase diagram is to take the differential
equations that describe the system and find the points where they are
zero. Thus, from {eq}`eq:RCK-kdot` we have that {math}`\dot{\kap}=0` implies

```{math}
:label: eq:RCK-kdotEq0

\begin{gathered}\begin{aligned}
  \cNrm & =  \fFunc(\kap) - (\PtyGroRte +\PopnGroRte+\deprRte) \kap 
\end{aligned}\end{gathered}
```

and we have already solved for the (constant) {math}`\Steady{\kap}` that characterizes
the {math}`\dot{\cNrm}/\cNrm=0` locus. These can be combined to generate the borders between
the phases in the phase diagram, as illustrated in {numref}`fig:RamseySSPlot`.

:::{figure} figures/RamseySSPlot.png
:name: fig:RamseySSPlot

{math}`\dot{\cNrm}/\cNrm =0` and {math}`\dot{\kap}=0` Loci

Note: With {math}`\CRRA=2`, {math}`\kapShare=0.3`, {math}`\discRte=0.02`, {math}`\PopnGroRte=0.01` and {math}`\deprRte=0.08`, and productivity growth {math}`\PtyGroRte` of 0.03 (low) or 0.06 (high); the dotted line marks the golden rule when {math}`\PtyGroRte` is low. Drawn by the [notebook](RamseyCassKoopmans.ipynb); run it in your browser with nothing to install, in [JupyterLite](https://intertemporal-choice.github.io/lite/notebooks/index.html?path=RamseyCassKoopmans.ipynb), or open it in [Colab](https://colab.research.google.com/github/intertemporal-choice/intertemporal-choice.github.io/blob/main/content/growth/RamseyCassKoopmans/RamseyCassKoopmans.ipynb) or [Binder](https://mybinder.org/v2/gh/intertemporal-choice/intertemporal-choice.github.io/main?labpath=content/growth/RamseyCassKoopmans/RamseyCassKoopmans.ipynb).
:::

## Transition

The two differential equations and {math}`\kap_{0}` don't pin down {math}`\cNrm_{0}`: every starting {math}`\cNrm_{0}` traces a path. The transversality condition, the counterpart of the intertemporal budget constraint, picks one:

```{math}
:label: eq:tvc

\begin{gathered}\begin{aligned}
  \lim_{t \rightarrow \infty} e^{-\int_{0}^{t} (\rfree_{\tau} -\PopnGroRte -\PtyGroRte)\,d\tau }\kap_{t} & =  0.
\end{aligned}\end{gathered}
```

The intuitive purpose of this unintuitive equation is basically to prevent
the capital stock from becoming negative or infinite as time goes by.

Obviously a capital stock that was negative for the entire future could not
satisfy the equation. And a capital stock that is too large has an interest rate below {math}`\PopnGroRte+\PtyGroRte`, so the discount term grows without bound, and so does the left side of the transversality condition.

{numref}`fig:RamseySaddlePlot` shows three paths for {math}`\cNrm` and {math}`\kap`
that satisfy {eq}`eq:cdotOc` and {eq}`eq:RCK-kdot`. The topmost path,
however, is clearly on a trajectory toward zero then negative
{math}`\kap`, while the bottommost path accumulates capital past the golden rule, toward the point where the
{math}`\dot{\kap}=0` locus meets the {math}`\kap` axis, with consumption falling toward zero. Only the middle path, labeled the "saddle path," satisfies
both {eq}`eq:cdotOc` and {eq}`eq:RCK-kdot` as well as the TVC
{eq}`eq:tvc`.

:::{figure} figures/RamseySaddlePlot.png
:name: fig:RamseySaddlePlot

Transition to the Steady State

Note: The same economy, with {math}`\PtyGroRte=0.03`. From {math}`\kap=0.5`, consumption 10 percent above the saddle path runs the capital stock down to zero, and consumption 10 percent below it accumulates capital past the golden rule, marked by the dotted line. Drawn by the [notebook](RamseyCassKoopmans.ipynb); run it in your browser with nothing to install, in [JupyterLite](https://intertemporal-choice.github.io/lite/notebooks/index.html?path=RamseyCassKoopmans.ipynb), or open it in [Colab](https://colab.research.google.com/github/intertemporal-choice/intertemporal-choice.github.io/blob/main/content/growth/RamseyCassKoopmans/RamseyCassKoopmans.ipynb) or [Binder](https://mybinder.org/v2/gh/intertemporal-choice/intertemporal-choice.github.io/main?labpath=content/growth/RamseyCassKoopmans/RamseyCassKoopmans.ipynb).
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
'time elimination' method {cite:p}`Mulligan&sm:transdynam`. It starts from the fact that

```{math}
\begin{gathered}\begin{aligned}
    \left(\frac{d\cNrm/dt}{d\kap/dt}\right) &=  d\cNrm/d\kap.
  \end{aligned}\end{gathered}
```

Note from {eq}`eq:cdotOc` that we can write

```{math}
:label: eq:cdot

\begin{gathered}\begin{aligned}
    \dot{\cNrm} & =   \CRRA^{-1}(\fFunc^{\prime}(\kap)-\discRte -(\PopnGroRte+\deprRte)-\CRRA \PtyGroRte)\cNrm ,
  \end{aligned}\end{gathered}
```

so we can obtain

```{math}
\begin{gathered}\begin{aligned}
    d\cNrm/d\kap & =  \left(\frac{(\kapShare \kap^{\kapShare-1}-\discRte -(\PopnGroRte+\deprRte)-\CRRA \PtyGroRte)\cNrm}
                       {\CRRA(\kap^{\kapShare} - \cNrm - (\PtyGroRte +\PopnGroRte+\deprRte) \kap)}\right)
  \end{aligned}\end{gathered}
```

which is a differential equation with, in general, no analytical solution. Many numerical math packages can solve differential equations numerically, yielding a numerical version of the {math}`\cFunc(\kap)` function.

There is one problem, however, which is that at the steady-state values of {math}`\cNrm` and {math}`\kap` both numerator and denominator of this equation are zero. The alternative is to solve the differential equation twice: Once for a domain extending from {math}`\kap=0` to {math}`\Steady{\kap}-\epsilon`, yielding {math}`\cFunc_{-}(\kap)`, and once for a domain from {math}`\Steady{\kap}+\epsilon` to some large value of {math}`\kap`, yielding {math}`\cFunc_{+}(\kap)`. The true consumption policy function can then be approximated by interpolating between the upper endpoint of {math}`\cFunc_{-}(\kap)` and the lower endpoint of {math}`\cFunc_{+}(\kap)`.

{cite:t}`judd:book` covers numerical methods for saddle paths more generally. The [notebook](RamseyCassKoopmans.ipynb) solves the model this way and draws both figures; run it in your browser with nothing to install, in [JupyterLite](https://intertemporal-choice.github.io/lite/notebooks/index.html?path=RamseyCassKoopmans.ipynb), or open it in [Colab](https://colab.research.google.com/github/intertemporal-choice/intertemporal-choice.github.io/blob/main/content/growth/RamseyCassKoopmans/RamseyCassKoopmans.ipynb) or [Binder](https://mybinder.org/v2/gh/intertemporal-choice/intertemporal-choice.github.io/main?labpath=content/growth/RamseyCassKoopmans/RamseyCassKoopmans.ipynb).
