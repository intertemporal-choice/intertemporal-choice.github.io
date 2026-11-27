(sec:TractableBufferStockMacro)=
# A Macroeconomic Interpretation of the Tractable Buffer Stock Model

Loosely following {cite:t}`cjSOE` (with some simplifications), this note extends the model of [A Tractable Model of Buffer Stock Saving](#sec:TractableBufferStock) to analyze macroeconomic dynamics in a small open economy with a large number of individuals, where the population statistics reflect the fulfillment of individual consumers' *ex ante* expectations; for example, exactly proportion {math}`\urate` of households who are employed in period {math}`t` become "unemployed" before {math}`t+1`, so that the aggregate labor supply of the "active" (still employed) members of a generation evolves according to

```{math}
\PopnLvl_{t+1,t} = \erate \PopnLvl_{t,t} ,
```

where the first subscript denotes the date being examined and the second denotes the period of birth of the generation being examined.

We make strong assumptions that permit straightforward aggregation. The first such assumption is that newly unemployed households immediately migrate out of the country (think of British retirees moving to southern Spain). This means that macroeconomic variables will reflect only the circumstances of employed consumers, rather than a blend of the employed and the unemployed.

:::{margin}
The qualitative story is not changed if the unemployed stay at home and live off their savings; since they have a simple linear decision rule (they spend a constant proportion of their resources), accounting for their behavior is straightforward but complicates the exposition without adding much substance. See {cite:t}`cjSOE` for a model that incorporates a stay-at-home unemployed population.
:::

Each person is part of a single "generation" of households born at the same time, and every new generation is larger by the factor {math}`\PopnGroFac` than the newborn generation in the previous period:

```{math}
\PopnLvl_{t+1,t+1} = \PopnGroFac \PopnLvl_{t,t} .
```

We assume that total production by the (surviving) members of a generation grows by the factor {math}`\WGroFac` every period. If total production is to grow despite a shrinking number of surviving members of the generation, production *per active capita* must grow by {math}`\WGroFac/\erate`, as the chapter's [growth of individual labor productivity](#eq:TBS-meanPreserve) provides.

Consider the economy in some period 0 in which the size of the newborn population and the wage rate have been normalized to {math}`\PopnLvl_{0,0} = \Wage_{0} = 1`, and index each generation by its age {math}`\age`, the number of periods since its birth. If the economy was created {math}`\bar{\age}` periods before period 0, so that its oldest generation has age {math}`\bar{\age}`, the ratio of the total population to the population of newborns will be

```{math}
1 + (\erate/\PopnGroFac)+ (\erate/\PopnGroFac)^{2}+ ... +(\erate/\PopnGroFac)^{\bar{\age}} = \left(\frac{1-(\erate/\PopnGroFac)^{\bar{\age}+1}}{1-(\erate/\PopnGroFac)}\right)
```

whose limit as {math}`\bar{\age} \rightarrow \infty` is a finite number so long as {math}`\erate/\PopnGroFac < 1`. We assume that the population grows, {math}`\PopnGroFac > 1`; since {math}`\erate < 1`, that ensures both this and, below, a finite total labor income.

Relative to the labor income of period 0's newborn cohort ({math}`\PopnLvl_{0,0} \Wage_{0} = 1`), the total labor income in period 0 of the generation born in period {math}`-1` is {math}`\PopnGroFac^{-1}`; the sum of the incomes of all of the two-period-old individuals is {math}`\PopnGroFac^{-2}`, and so on; total labor income for all generations in the economy in period 0 is

```{math}
:label: eq:TBS-LabIncTot

1 + \PopnGroFac^{-1}+ \PopnGroFac^{-2}+ ...+\PopnGroFac^{-\bar{\age}} = \left(\frac{1-(\PopnGroFac^{-1})^{\bar{\age}+1}}{1-\PopnGroFac^{-1}}\right) ,
```

which is finite because {math}`\PopnGroFac>1`. The *proportion* of aggregate income accounted for by a generation born at any specific moment declines toward zero as time passes (old generations never die, they just fade away).

In the balanced growth equilibrium, the growth factor for aggregate population will therefore be {math}`\PopnGroFac` and output per capita will increase by {math}`\WGroFac` per period. Total labor income therefore grows by {math}`\PopnGroFac \WGroFac.`

## Stakes

We now examine this model under two assumptions about the initial "stake" of newborns in the economy. (We use "stake" to designate a transfer received by newborns). This is explicitly *not* an inheritance, as we have assumed that individuals have no bequest motive and newborns are unrelated to anyone in the existing population. Our motivation is to make the model more tractable, rather than to represent an important feature of the real world; the model without a "stake" can only be solved by simulation, and {numref}`fig:TBS-SOENoStakescPath` shows how its aggregate consumption evolves when households start with no wealth.

### A "Stake" That Yields a Representative Agent

We first consider a version of the model in which an exogenous redistribution program guarantees that the behavior of employed households can be understood by analyzing the actions of a "representative employed agent."

If a benevolent source outside the economy were to provide every newborn with an initial transfer upon birth of size {math}`\bTrgNrm`, then the newborn's total monetary resources would be

```{math}
\begin{aligned}
  \mNrmE_{t,t} & =  \bTrgNrm + 1
\\ & =  \mTrgNrm
.
\end{aligned}
```

Thus, per-capita market resources for members of the newborn generation would be exactly equal to the target level of market resources for a person anticipating the future path of labor income that the members of the newborn generation actually anticipate (which is the same as the future path anticipated by all other generations as well).

If such a transfer policy had been in place forever, the economy at every point in time would consist of employed households whose consumption had been equal to its steady-state value {math}`{\cNrm}^{\EmpLbl}` for their whole lives. That is, every individual agent in this economy would be identical in their *ratio* of consumption, market resources, etc. to permanent labor income. The behavior of any individual would therefore be fully captured by the behavior of a representative employed agent.

:::{margin}
The *level* of permanent labor income will differ for different households, depending on their age and accumulated wage seniority; the circumstances of individuals are identical only after their problem has been normalized by their varying levels of permanent labor income.
:::

The foregoing scenario assumed that the "stake" is provided by a mysterious "benevolent source outside the economy." Fortunately, there is an easy way to eliminate this problematic assumption: Assume that the stakes are financed by a wage tax.

The size of the required tax rate is calculated as follows. The total size of the resources transferred to the newborn generation must be

```{math}
\check{\BLvl}^{\EmpLbl}_{t,t} = \check{\bNrm} \PopnLvl_{t,t} \check{\Wage}_{t}
```

where

```{math}
\check{\Wage}_{t} = \left(1-\TaxRte\right)\Wage_{t}
```

is the after-tax wage rate for the economy as a whole (and {math}`\check{\bNrm}` is the steady state target ratio of bank balances to after-tax wages).

From {eq}`eq:TBS-LabIncTot`, the ratio of total aggregate labor income to the labor income of the newborn generation is

```{math}
\left(\frac{1}{1-\PopnGroFac^{-1}}\right)
```

so, since the stake is {math}`\check{\bNrm}` times the after-tax wage, the aggregate wage tax rate required to finance a "stake" of size {math}`\check{\bNrm}` for newborns is given by

```{math}
\begin{aligned}
  \check{\bNrm}(1-\TaxRte) & =    \left(\frac{\TaxRte}{1-\PopnGroFac^{-1}}\right)
\\ \TaxRte & =  \left(\frac{(1-\PopnGroFac^{-1})\check{\bNrm}}{1+(1-\PopnGroFac^{-1})\check{\bNrm}}\right)
.
\end{aligned}
```

Note, however, that in an economy where this tax has existed forever, the consequence of the tax is effectively just a permanent reduction in after-tax labor income by proportion {math}`\TaxRte`, compared to its value in the absence of the tax. Given the homotheticity of the model, a permanent rescaling by a constant factor leaves the scaled version of the individual's problem (and its solution) unchanged. Thus we can conclude not only that a representative agent exists in this economy, but that the steady-state characteristics of the representative agent's problem are identical (in ratio form) to the characteristics of the unrescaled individual's problem; that is, {math}`\check{\cFunc}(\mNrm) = \cFunc^{\EmpLbl}(\mNrm)`, {math}`\check{\bNrm} = \bTrgNrm`, and so on.

Matters are not much more complicated outside the balanced growth steady state, so long as we assume that the government always transfers the amount {math}`\check{\bNrm}` to newborn households, financed by the tax {math}`\TaxRte` derived above. Consider, for example, an economy that was in steady-state equilibrium leading up to period {math}`\prdt`, and at the beginning of {math}`\prdt` there is a sudden realization that future growth rates will be higher than those anticipated and experienced in the past: {math}`\Alt{\WGroFac} > \WGroFac` after {math}`\prdt`. Since expected growth rates affect {math}`\bTrgNrm`, the tax rate must be immediately and permanently changed so that the generations born after {math}`\prdt-1` receive a "stake" of the proper new size. This change in {math}`\TaxRte` has two consequences for the generations that survive from periods prior to {math}`\prdt`. Under the old tax rate, they would have experienced {math}`\bNrmE_{t} = \bLvl_{t}/((1-\TaxRte)\Wage_{t}) = \bTrgNrm`; the change in expectations has no effect on {math}`\bLvl_{t}` or {math}`\Wage_{t}` but changes the tax rate to {math}`\Alt{\TaxRte}`. Thus these households will have an actual resource ratio that differs from its new target value, {math}`\bNrmE_{t} \neq \Alt{\bTrgNrm}`, both because the after-tax income scaling factor has changed and because the target ratio has changed from {math}`\bTrgNrm` to {math}`\Alt{\bTrgNrm}`.

However, if we started out in steady-state, the *ratio* problem of every member of the continuing-employed population is identical to that of every other such household (though, again, their masses differ depending on age, etc); as a result, the dynamics of the economy are fully captured by keeping track of the relative weights in the economy of the (gradually diminishing) "representative shocked agent" and the (gradually increasing) "representative new agent" whose behavior is locked at its steady-state value.

:::{margin}
If the economy has experienced multiple shocks, it will be necessary to retain a complete history of the shocks in order to compute the properly population-weighted dynamics. This is not too hard to do, if we start with the assumption that the economy started at its balanced growth equilibrium before the shocks began to arrive.
:::

{numref}`fig:TractableBufferStockMacro-SOEStakescPath` illustrates the dynamics in this economy using an experiment identical to the chapter's [final experiment](#sec:TBS-FinalExperiment) for the individual's problem: In period 0 there is a one-off decline in the future discounting rate (assuming the economy was in steady state before period 0). In that experiment, each individual consumer's consumption function shifted down, and consumption experienced a discrete jump downward, because the agent became more patient. Here, there is a modest further effect: With more-patient consumers, the tax rate that the government sets to finance a transfer of {math}`\bTrgNrm` to the newborns must be larger (so that the ratio of initial assets to after-tax income is larger). The higher tax also lowers the after-tax income of the households alive at the change, so they start from {math}`1+\bTrgNrm(1-\TaxRte)/(1-\Alt{\TaxRte})`, a little above the old target, as the figure shows. Qualitatively, the dynamics are indistinguishable from the individual consumer's dynamics obtainable without working through the extra complication involved in accounting for the "stakes."

:::{figure} /content/consumption/TractableBufferStock/figures/SOEStakescPathAfterThetaDropPlot.png
:name: fig:TractableBufferStockMacro-SOEStakescPath

Aggregate {math}`\CNrm` in a Small Open Economy Before and After {math}`\discRte` Decline. With stakes, aggregate consumption behaves like an individual's: it drops, then rises to a higher ratio. Drawn by the chapter's [notebook](../consumption/TractableBufferStock/TractableBufferStock.ipynb); run it in your browser, with nothing to install, in [JupyterLite](https://intertemporal-choice.github.io/lite/notebooks/index.html?path=TractableBufferStock.ipynb), or open it in [Colab](https://colab.research.google.com/github/intertemporal-choice/intertemporal-choice.github.io/blob/main/content/consumption/TractableBufferStock/TractableBufferStock.ipynb) or [Binder](https://mybinder.org/v2/gh/intertemporal-choice/intertemporal-choice.github.io/main?labpath=content/consumption/TractableBufferStock/TractableBufferStock.ipynb).
:::

### No Stake

The polar alternative to assuming that newborns get a "stake" is to assume that newborns enter the economy with zero assets. Analysis of this version of the model must be performed using simulation methods, because households of different ages will have different levels of assets. (Because the consumption function is concave and has no closed form, aggregation cannot be done analytically.)

Our simulation procedure assumes that at date 0 the economy has existed forever (so that the age distribution of relative populations and productivities are at their steady-state values), but saving has been impossible prior to period 0. With everyone's {math}`\bNrmE_{t}=0`, the ratio of market resources to permanent labor income is the same for all individuals, whatever their age {math}`\age`:

:::{margin}
In periods before 0, unemployment presumably would have meant immediate death by starvation; we think of this more as a starting point for the simulations than as a realistic description of a plausible economy.
:::

```{math}
\mNrmE_{0,-\age} = 1 .
```

The consumption ratio in period 0 is therefore {math}`\cFunc(1)` for every household (regardless of age), while the level of per-capita labor income for a generation of age {math}`\age` is {math}`\erate^{-\age}`. The population of such workers is {math}`(\erate/\PopnGroFac)^{\age}`, so aggregate consumption will be given by the per-capita consumption ratio, multiplied by the per-capita level of permanent income, multiplied by the population of workers still alive:

:::{margin}
The absolute level of wages will have grown by {math}`\WGroFac/\erate` per period for these households since their birth, but we have normalized by the level of wages for period-0 newborns, which cancels the {math}`\WGroFac` from the expression.
:::

```{math}
\begin{aligned}
  \CLvl_{0} & =  \sum_{\age=0}^{\infty} \cFunc(1) \erate^{-\age} (\erate/\PopnGroFac)^{\age}
\\ & =  \cFunc(1) \sum_{\age=0}^{\infty}  \PopnGroFac^{-\age}
\\ & =  \cFunc(1) \left(\frac{1}{1-\PopnGroFac^{-1}}\right)
.
\end{aligned}
```

The longer a generation lives, the more time it will have had to save toward its target level of wealth; but newborns always begin life with no assets. After period 0, therefore, age-heterogeneity in assets and consumption ratios creeps into the population.

The foregoing discussion contains (in some cases implicitly) all the assumptions necessary to conduct a simulation of this economy. {numref}`fig:TBS-SOENoStakescPath` shows the path of {math}`\CNrm_{t}`, aggregate consumption as a ratio to aggregate labor income, starting from period 0 for an economy under the benchmark parameterization of [A Tractable Model of Buffer Stock Saving](#sec:TractableBufferStock). The only extra parameter required beyond the chapter's is {math}`\PopnGroFac`; we choose {math}`\PopnGroFac=1.01` corresponding roughly to the postwar population growth rate in the United States.

:::{figure} /content/consumption/TractableBufferStock/figures/SOENoStakescPath.png
:name: fig:TBS-SOENoStakescPath

Path of Aggregate {math}`\CNrm` in a Small Open Economy Without Stakes From Date 0. Starting with no wealth, aggregate consumption rises quickly toward its steady-state ratio as households build their buffer stocks. Drawn by the chapter's [notebook](../consumption/TractableBufferStock/TractableBufferStock.ipynb); run it in your browser, with nothing to install, in [JupyterLite](https://intertemporal-choice.github.io/lite/notebooks/index.html?path=TractableBufferStock.ipynb), or open it in [Colab](https://colab.research.google.com/github/intertemporal-choice/intertemporal-choice.github.io/blob/main/content/consumption/TractableBufferStock/TractableBufferStock.ipynb) or [Binder](https://mybinder.org/v2/gh/intertemporal-choice/intertemporal-choice.github.io/main?labpath=content/consumption/TractableBufferStock/TractableBufferStock.ipynb).
:::

