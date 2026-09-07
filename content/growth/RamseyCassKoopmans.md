(sec:RamseyCassKoopmans)=
# The Ramsey/Cass-Koopmans (RCK) Model

{cite:t}`ramseySave`, followed much later by {cite:t}`cass:growth` and {cite:t}`koopmans:growth`, formulated the canonical model of optimal growth for an economy with exogenous 'labor-augmenting' technological progress.

## The Budget Constraint

The economy has a perfectly competitive production sector that uses a Cobb-Douglas aggregate production function

```{math}
\begin{gathered}\begin{aligned}
                   \Inc & =  \ProdFunc(\Kap,\Labor) = \Kap^{\kapShare}(\PtyLab \Labor)^{1-\kapShare}
\end{aligned}\end{gathered}
```

to produce output using capital and labor.[^DGoP2Gjmvh] Labor hours (the same as population) increases exogenously at a constant rate[^GMWPgcHLoc]

[^DGoP2Gjmvh]: All Roman variables are functions of time, but putting time subscripts on everything would clutter the notation, so we do it only where necessary for clarity.

[^GMWPgcHLoc]: The ancient Greek philosophers captured eternal truths; therefore, Greek letters represent constants whose value never changes.

```{math}
\begin{gathered}\begin{aligned}
  \dot{\Labor}/\Labor & =  \popGro
\end{aligned}\end{gathered}
```

and {math}`\PtyLab` is an index of labor productivity that grows at rate

:::{margin}
Solow and Phelps showed that steady-state growth is independent of the fraction of technical progress that is embodied in new capital, though the speed of convergence is faster the more progress is embodied.
:::

```{math}
\begin{gathered}\begin{aligned}
  \dot{\PtyLab }/\PtyLab  & =  \ptyGro. 
\end{aligned}\end{gathered}
```

Thus, technological progress allows each worker to
produce perpetually more as time goes by with the same amount of
physical capital.[^QeBMSQU4dN] The quantity {math}`\PtyLab \Labor` is known as the number of 'efficiency units' of labor in the economy.

:::{margin}
Writing progress in {math}`\PtyLab \Labor` form is a peculiar assumption; it seems more natural to imagine technology embodied in new {math}`K`. The disembodied form is used here because it is simpler and, as noted above, delivers the same steady state.
:::

[^QeBMSQU4dN]: This is the definition of 'labor-augmenting' (Harrod-neutral) productivity growth; with a Cobb-Douglas production function, it turns out to be essentially the same as 'capital-augmenting' productivity growth, also known as Hicks-neutral, as well as output-neutral ('Solow-neutral') progress.

Aggregate capital accumulates according to

```{math}
:label: eq:Kdotlevel

\begin{gathered}\begin{aligned}
  \dot{\Kap} & =  \Inc - \Cons - \depr K .
\end{aligned}\end{gathered}
```

Lower case variables are the upper case version divided by efficiency units, i.e.

```{math}
\begin{gathered}\begin{aligned}
  \inc & =  \Inc/(\PtyLab \Labor)  \\
       & =  \Kap^{\kapShare}(\PtyLab \Labor)^{1-\kapShare}/(\PtyLab \Labor)  \\
       & =  (\Kap/\PtyLab \Labor)^{\kapShare}
  \\   & =  \kap^{\kapShare}    .
\end{aligned}\end{gathered}
```

Note that

```{math}
\begin{gathered}\begin{aligned}
  \dot{\kap} \equiv       \left(\frac{d\kap}{dt}\right) & =  \left(\frac{\dot{\Kap}\PtyLab \Labor - K(\dot{\PtyLab }L + \PtyLab \dot{\Labor})}{(\PtyLab \Labor)^{2}}\right) 
  \\   & =  \dot{\Kap}/\PtyLab \Labor - k(\dot{\PtyLab }/{\PtyLab } + \dot{\Labor}/\Labor)
  \\          & =  \dot{\Kap}/\PtyLab \Labor - (\ptyGro +\popGro)k
\end{aligned}\end{gathered}
```

which means that {eq}`eq:Kdotlevel` can be divided by {math}`\PtyLab \Labor` and becomes

```{math}
:label: eq:RCK-kdot

\begin{gathered}\begin{aligned}
  \dot{\Kap}/\PtyLab \Labor & =  \inc - \cons - \depr \kap  \\
  \dot{\kap}+(\ptyGro +\popGro)k & =  \prodFunc(\kap) - \cons - \depr \kap  \\
  \dot{\kap} & =  \prodFunc(\kap) - \cons - (\ptyGro +\popGro+\depr) \kap .
\end{aligned}\end{gathered}
```

A steady-state will be a point where {math}`\dot{\kap} = 0`.

Equation {eq}`eq:RCK-kdot` yields a first candidate for an optimal
steady-state of the growth model: It seems reasonable to argue that the best
possible steady-state is the one that maximizes {math}`\cons`. This is the
"golden rule" optimality condition of
{cite:t}`phelps:golden`, an article well worth reading; this is
one of the chief contributions for which Phelps won the Nobel prize.

## The Social Planner's Problem

Now suppose that there is a social planner whose goal is to maximize the discounted
sum of CRRA utility from per-capita consumption:

```{math}
:label: eq:RCK-maxprob

\max \int_{0}^{\infty} \left(\frac{(\Cons/\Labor)^{1-\CRRA}}{1-\CRRA}\right) e^{-\timeRate  t} .
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
  \int_{0}^{\infty} \left(\frac{(\PtyLab c)^{1-\CRRA}}{1-\CRRA}\right) e^{-\timeRate  t} & =  
                                                                                               \PtyLab _{0}^{1-\CRRA}\int_{0}^{\infty} \left(\frac{\cons^{1-\CRRA}}{1-\CRRA}\right) e^{-\timeRate  t}e^{(1-\CRRA)\ptyGro  t} 
  \\ & =  \PtyLab _{0}^{1-\CRRA}\int_{0}^{\infty} \util(c) e^{\left((1-\CRRA)\ptyGro -\timeRate \right) t}
           .
\end{aligned}\end{gathered}
```

Thus, defining {math}`\nu = \timeRate  - (1-\CRRA) \ptyGro` and normalizing the initial
level of productivity to {math}`\PtyLab _{0}=1`, the complete optimization problem
can be formulated as

```{math}
\max \int_{0}^{\infty} \util(c) e^{-\nu  t}
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
  \\  \dot{\cons}/\cons  & =  \CRRA^{-1}(\underbrace{\prodFunc^{\prime}(\kap)-(\popGro+\ptyGro+\depr)}_{\mbox{$\equiv \acute{r}$}}-\nu)
\end{aligned}\end{gathered}
```

where the definition of {math}`\acute{r}` is motivated by thinking of
{math}`\prodFunc^{\prime}(\kap)-(\popGro+\ptyGro+\depr)` as the interest rate net of depreciation and
dilution.

This is called the "modified golden rule" (or sometimes the
"Keynes-Ramsey rule" because it was originally derived by
Ramsey with an explanation attributed to Keynes).

Thus, we end up with an Euler equation for consumption growth that is
just like [the Euler equation in the perfect foresight partial equilibrium consumption model](http://www.econ2.jhu.edu/people/ccarroll/public/LectureNotes/Consumption/PerfForesightCRRA/#EulerCGroFac), except that now the relevant interest rate can vary over
time as {math}`\prodFunc^{\prime}(\kap)` varies.

Substituting in the modified time preference rate gives

```{math}
:label: eq:cdotOc

\begin{gathered}\begin{aligned}
  \dot{\cons}/\cons  & =  \CRRA^{-1}(\prodFunc^{\prime}(\kap)-(\popGro+\depr+\ptyGro)-\timeRate  +(1- \CRRA) \ptyGro)
  \\   & =  \CRRA^{-1}(\prodFunc^{\prime}(\kap)-(\popGro+\depr)-\timeRate  - \CRRA \ptyGro), 
\end{aligned}\end{gathered}
```

and finally note that defining per capita consumption {math}`\chi = \Cons/\Labor`
so that {math}`\cons = \chi \PtyLab ^{-1}`,

```{math}
:label: eq:chiDotOchi

\begin{gathered}\begin{aligned}
  \dot{\cons} & =  \dot{\biggl(\chi \PtyLab ^{-1}\biggr)} =  \dot{\chi}\PtyLab ^{-1}-(\chi \PtyLab ^{-1})\dot{\PtyLab }/\PtyLab 
  \\ \dot{\cons}/\cons & =  \dot{\biggl(\chi \PtyLab ^{-1}\biggr)}/(\chi \PtyLab^{-1}) =  \dot{\chi}/\chi - \ptyGro 
\end{aligned}\end{gathered}
```

and since {eq}`eq:cdotOc` can be written

```{math}
\begin{gathered}\begin{aligned}
  \dot{\cons}/\cons  & =  \CRRA^{-1}(\prodFunc^{\prime}(\kap)-(\popGro+\depr)-\timeRate ) - \ptyGro,
\end{aligned}\end{gathered}
```

we have

```{math}
\begin{gathered}\begin{aligned}
  \dot{\chi}/\chi & =  \CRRA^{-1}(\prodFunc^{\prime}(\kap)-(\popGro+\depr)-\timeRate )
\end{aligned}\end{gathered}
```

so the formula for per capita consumption growth (as a function of
{math}`\kap`) is identical to the model with no growth (equation
{eq}`eq:cdotOc` with {math}`\ptyGro=0`). Any important differences between
the no-growth model and the model with growth therefore must come
through the channel of differences in {math}`\kap`.

## The Steady State

The assumption of labor augmenting technological progress was made
because it implies that in steady-state, per-capita consumption, income,
and capital all grow at rate {math}`\ptyGro`.[^x66RuMjc3A]

[^x66RuMjc3A]: See {cite:t}`ghosDespiteUzawa` for a discussion of the realism of this requirement.

{math}`\dot{\cons}/\cons = 0` implies that at the steady-state value of {math}`\check{\kap}`,

```{math}
\begin{gathered}\begin{aligned}
  \prodFunc^{\prime}(\check{\kap}) & =  \timeRate +\popGro+\depr+\CRRA \ptyGro  \\
  \kapShare \check{\kap}^{\kapShare-1} & =  \timeRate +\popGro+\depr+\CRRA \ptyGro  \\
  \check{\kap} & =  \left(\frac{\timeRate +\popGro+\depr+\CRRA \ptyGro}{\kapShare}\right)^{\frac{1}{\kapShare-1}}
  \\      \check{\kap} & =  \left(\frac{\kapShare}{\timeRate +\popGro+\depr+\CRRA \ptyGro}\right)^{\frac{1}{1-\kapShare}}   
\end{aligned}\end{gathered}
```

Thus, the steady-state {math}`\kap` will be higher if capital
is more productive ({math}`\kapShare` is higher), and will be lower if
consumers are more impatient, population growth is faster,
depreciation is greater, or technological progress occurs more rapidly.

## A Phase Diagram

While the RCK model has an analytical solution for its steady-state,
it does not have an analytical solution for the transition to the
steady-state. The usual method for analyzing
models of this kind is a [phase diagram](https://en.wikipedia.org/wiki/Phase_diagram) in {math}`\cons` and {math}`\kap`.

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

Actually, as stated so far, the solution to the problem is very simple: The
consumer should spend an infinite amount in every period. This solution is
not ruled out by anything we have yet assumed (except possibly the fact that
once {math}`\kap` becomes negative the production function is undefined).

Obviously, this is not the solution we are looking for. What is missing is
that we have not imposed anything corresponding to the intertemporal
budget constraint. In this context, the IBC takes the form of a "transversality
condition,"

```{math}
:label: eq:tvc

\begin{gathered}\begin{aligned}
  \lim_{t \rightarrow \infty} \lambda_{t} e^{(\ptyGro +\popGro) t - \int_{0}^{t} r_{\tau} d\tau }k_{t} & =  0.
\end{aligned}\end{gathered}
```

The intuitive purpose of this unintuitive equation is basically to prevent
the capital stock from becoming negative or infinity as time goes by.

Obviously a capital stock that was negative for the entire future could not
satisfy the equation. And a capital stock that is too large will have
an arbitrarily small interest rate, which will result in the LHS of the
TVC being a positive number, again failing to satisfy the TVC.

{numref}`fig:RamseySaddlePlot` shows three paths for {math}`\cons` and {math}`\kap`
that satisfy {eq}`eq:cdotOc` and {eq}`eq:RCK-kdot`. The topmost path,
however, is clearly on a trajectory toward zero then negative
{math}`\kap`, while the bottommost path is heading toward an infinite
{math}`\kap`. Only the middle path, labelled the "saddle path," satisfies
both {eq}`eq:cdotOc` and {eq}`eq:RCK-kdot` as well as the TVC
{eq}`eq:tvc`.

:::{figure} /content/figures/RamseyCassKoopmans/RamseySaddlePlot.png
:name: fig:RamseySaddlePlot

Transition to the Steady State
:::

## Interactive Notebooks

An explicit numerical solution to the Ramsey problem, with a description of a solution method and its
mathematical/computational underpinnings, is available [here](https://github.com/llorracc/Jupyter/blob/master/notebooks/RamseyCassKoopmans.ipynb).

## Appendix: Numerical Solution

The RCK model does not have an analytical solution, which means that
numerical methods must be used to find out the model's quantitative
implications for transition paths.

The method of solution of these kinds of models is not important for
the purposes of first year graduate macroeconomics; this appendix
has been written as a reference for more advanced students who might
be beginning their research on growth models.

The most straightforward method of numerical solution for perfect foresight
models of this kind is called the
'time elimination' method. It starts from the fact that

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

which is a differential equation with no analytical solution. Many numerical math packages can solve differential equations numerically, yielding a numerical version of the {math}`\cFunc(\kap)` function.

There is one problem, however, which is that at the steady-state values of {math}`\cons` and {math}`\kap` both numerator and denominator of this equation are zero. The alternative is to solve the differential equation twice: Once for a domain extending from {math}`\kap=0` to {math}`\check{\kap}-\epsilon`, yielding {math}`\cFunc_{-}(\kap)`, and once for a domain from {math}`\check{\kap}+\epsilon` to some large value of {math}`\kap`, yielding {math}`\cFunc_{+}(\kap)`. The true consumption policy function can then be approximated by interpolating between the upper endpoint of {math}`\cFunc_{-}(\kap)` and the lower endpoint of {math}`\cFunc_{+}(\kap)`.

For further details of the numerical solution of this model, see [this Jupyter notebook](https://github.com/llorracc/Jupyter/blob/master/notebooks/RamseyCassKoopmans.ipynb), or clone the repo and, in the cloned directory, run the corresponding python program: `ipython RamseyCassKoopmans.py`.
