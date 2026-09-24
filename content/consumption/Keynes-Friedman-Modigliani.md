(sec:Keynes-Friedman-Modigliani)=
# Keynes, Friedman, Modigliani

:::{tip} Run it yourself
This chapter summarizes the Econ-ARK notebook [Keynes, Friedman, Modigliani](https://econ-ark.org/materials/keynesfriedmanmodigliani/). That page launches the notebook on Binder, a free service that runs it on a remote server and shows it in your browser, with nothing to install. It can take a minute or two to start. You can then rerun every estimate and simulation below and change the parameters. The figure links in this chapter go to the notebook's rendered copy on [DemARK](https://econ-ark.github.io/DemARK/keynesfriedmanmodigliani/).
:::

<!-- Figure links point at the notebook's cell anchors on the DemARK site (#kfm-<label>-outputs
shows the figure itself). The labels are set with `#| label:` lines in DemARK's
notebooks/KeynesFriedmanModigliani.ipynb; the figures are also saved as files in
notebooks/KeynesFriedmanModigliani/. Numbers quoted below are that notebook's outputs,
from FRED quarterly data for 1990-2020 and simulations seeded with 0. -->

The modern theory of consumption began as an argument about a single empirical relationship: how much of an extra dollar of income a household spends. This chapter follows that argument from Keynes's consumption function, through the evidence that did not fit it, to Friedman's resolution.

## Keynes's Consumption Function

{cite:t}`keynesGeneralTheory` held that the amount of aggregate consumption depends mainly on the amount of aggregate income, and called it a "fundamental psychological law" that when income rises, consumption rises by less than the increase in income. The simplest formalization is

```{math}
:label: eq:KFM-KeynesianC

\begin{aligned}
\cRat_{t} & = \alpha_{0} + \alpha_{1} \yRat_{t} \\
\Delta \cRat_{t} & = \alpha_{1} \Delta \yRat_{t}
\end{aligned}
```

with {math}`\alpha_{0} > 0` and {math}`\alpha_{1} < 1`, so that the saving rate rises with income.

This linear rule is not at odds with optimizing behavior. The notebook solves a perfect foresight consumer's problem in Econ-ARK's HARK toolkit and, with suitable parameter values, obtains a consumption function of exactly this form, with {math}`\alpha_{0} = 1.66` and {math}`\alpha_{1} = 0.78` ([figure](https://econ-ark.github.io/DemARK/keynesfriedmanmodigliani/#kfm-keynesian-cfunc-plot-outputs)).

## The Evidence Does Not Settle on One Slope

Estimates of {math}`\alpha_{1}` depend on the data used to measure it.

- **Levels.** Regressing real consumption on real disposable income in quarterly U.S. data gives {math}`\alpha_{1} = 0.92` ([figure](https://econ-ark.github.io/DemARK/keynesfriedmanmodigliani/#kfm-fred-levels-regression-outputs)). This matches Kuznets's finding that the saving rate shows no trend over long periods, which contradicts Keynes's rising saving rate.
- **But both series trend.** Consumption grows steadily over the sample ([figure](https://econ-ark.github.io/DemARK/keynesfriedmanmodigliani/#kfm-fred-consumption-series-outputs)), and so does income, so the levels regression largely measures their common trend.
- **Quarterly changes.** Regressing the change in consumption on the change in income, the second line of {eq}`eq:KFM-KeynesianC`, gives {math}`\alpha_{1} = 0.09` ([figure](https://econ-ark.github.io/DemARK/keynesfriedmanmodigliani/#kfm-fred-quarterly-diff-regression-outputs)).
- **Households.** Cross sections of households show a large intercept and a slope of perhaps 0.5, with low-income households spending two or three times their income and high-income households saving a great deal.

The disagreement between the levels and the first-difference estimates is the most important result in this section. If {eq}`eq:KFM-KeynesianC` described how consumption is actually determined, its two lines would be the same model, and estimating {math}`\alpha_{1}` from levels or from first differences should give the same answer, up to sampling error. Getting 0.92 one way and 0.09 the other is a powerful signal that the model is wrong in some profound way, or, in the more polite technical term, that it is *misspecified*. Refining the estimate of {math}`\alpha_{1}` cannot fix this; the model itself has to change. Friedman's permanent income hypothesis, below, is one such change, and it predicts exactly this pattern.

## Duesenberry: Habits and Relative Income

{cite:t}`duesenberryIncome` proposed that past consumption shapes current consumption through habits, and that households judge their consumption relative to that of their peers. In the aggregate data, lagged consumption does dominate: regressing consumption on income and on last quarter's consumption gives a coefficient of 0.98 on lagged consumption (t-statistic 31) and 0.02 on income, statistically indistinguishable from zero ([regression](https://econ-ark.github.io/DemARK/keynesfriedmanmodigliani/#kfm-habit-regression-outputs)). Because both series are non-stationary, this regression should not be taken at face value. The deeper problems are theoretical: Duesenberry's framework has no budget constraint and no serious treatment of the intertemporal nature of saving.

## Friedman's Permanent Income Hypothesis

{cite:t}`friedmanATheory` split income into a permanent component {math}`p` and a transitory component {math}`\theta`, and held that consumption depends on permanent income alone:

```{math}
\begin{aligned}
\yRat_{i} & = p_{i} + \theta_{i} \\
\cRat_{i} & = p_{i} + u_{i}
\end{aligned}
```

where {math}`u` is transitory consumption, unrelated to income. The notebook builds this consumer as a special case of the model in the [perfect foresight CRRA](#sec:PerfForesightCRRA) section: whatever its current income, a consumer with a permanent income of 1 consumes 1 ([figure](https://econ-ark.github.io/DemARK/keynesfriedmanmodigliani/#kfm-pih-cfunc-plot-outputs)).

If Friedman is right, a regression of consumption on measured income across households does not recover a true marginal propensity to consume. The estimated slope instead measures how much of the variation in income is permanent:

```{math}
:label: eq:KFM-attenuation

\alpha_{1} = \frac{\sigma^{2}_{p}}{\sigma^{2}_{p} + \sigma^{2}_{\theta}}
```

The notebook confirms this by simulating 200 households:

- When permanent and transitory income are equally variable, {eq}`eq:KFM-attenuation` predicts a slope of 0.5, and the simulation gives 0.54 ([figure](https://econ-ark.github.io/DemARK/keynesfriedmanmodigliani/#kfm-pih-sim-low-perm-variance-outputs)).
- When permanent income is five times as variable (in standard deviation), the prediction is 0.96, and the simulation gives 0.95 ([figure](https://econ-ark.github.io/DemARK/keynesfriedmanmodigliani/#kfm-pih-sim-high-perm-variance-outputs)).

The same logic explains the aggregate evidence. Over one quarter, most changes in income are transitory, and the slope is 0.09 ([figure](https://econ-ark.github.io/DemARK/keynesfriedmanmodigliani/#kfm-fred-quarterly-diff-pih-outputs)). Over twenty quarters, changes in permanent income dominate, and the slope rises to 0.89 ([figure](https://econ-ark.github.io/DemARK/keynesfriedmanmodigliani/#kfm-fred-20-quarter-diff-regression-outputs)). The two estimates do not contradict each other. They measure the same behavior over horizons at which permanent income matters very differently.

## Modigliani and What Follows

{cite:t}`modiglianiBrumberg` reached a closely related conclusion from a different starting point: households plan consumption over the whole life cycle, so consumption tracks lifetime resources rather than current income. The chapters that follow build that idea from the ground up, starting with the [Fisher two-period problem](#sec:2PeriodLCModel), and the [consumption function](#sec:ConsumptionFunction) section returns to Friedman's distinction between permanent and transitory shocks with an explicit model of optimal behavior.
