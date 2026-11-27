---
math:
  # Everything else this chapter writes comes from the shared notation (econ-ark-tools, @resources/notation).
  # Kept here: two symbols that wait on Chris (Pi's face, the check), and the two loci's labels, which have
  # no registry row.
  '\GPRteAdj': '\check{\APRte}_{\WGroRtehFix}'
  '\dcEqZero': '\Delta\cNrmE=0'
  '\dmEqZero': '\Delta\mNrmE=0'
  '\straight': '\Pi'
---
(sec:TractableBufferStock)=
# A Tractable Model of Buffer Stock Saving

## Introduction

This chapter illustrates the logic of precautionary saving by assuming that individuals face only a single, simple kind of uncertainty: A small risk of becoming permanently unemployed. More realistic assumptions yield similar conclusions (after much more work).

:::{margin}
The model simplifies many of the key results in {cite:t}`carroll:brookings` and {cite:t}`BufferStockTheory` using a discrete-time version of the elegant continuous-time model of {cite:t}`toche:urisk`. For a brief summary of the precautionary saving literature, see {cite:t}`CarrollKimballPSPW`; for a more rigorous treatment of the theoretical issues, see {cite:t}`BufferStockTheory`.
:::

Two assumptions make the model tractable. Unemployment is permanent, so an unemployed consumer has a perfect foresight problem whose solution is linear in resources. And the income of a consumer who stays employed grows just fast enough that a change in the risk of unemployment leaves expected human wealth unchanged, so the change is a pure change in uncertainty.

We show that a consumer who is sufficiently impatient has a target ratio of wealth to income, at which impatience, pulling wealth down, is balanced by prudence, which grows stronger as wealth falls; and that the consumption function is concave. The model then shows why estimates of the consumption Euler equation can mislead and, for [a small open economy](#sec:TractableBufferStockMacro), how a transfer to each newborn generation (a "stake") lets a representative agent describe the behavior of many households. The [appendix](#sec:TractableBufferStock-Appendix) derives the results and describes how the model is solved numerically.

A companion notebook in the Econ-ARK DemARK collection, [Tractable Buffer Stock (interactive)](https://econ-ark.org/materials/tractablebufferstock-interactive), lets you vary the model's parameters and watch the consumption function and target wealth respond. HARK solves the model as its [`TractableConsumerType`](https://github.com/econ-ark/HARK/blob/main/examples/TractableBufferStockModel/TractableConsumerType.ipynb). This chapter's figures are drawn by its [figure notebook](TractableBufferStock.ipynb), which solves the model itself; its results have been checked against HARK's. Run it in your browser, with nothing to install, in [JupyterLite](https://intertemporal-choice.github.io/lite/notebooks/index.html?path=TractableBufferStock.ipynb), or open it in [Colab](https://colab.research.google.com/github/intertemporal-choice/intertemporal-choice.github.io/blob/main/content/consumption/TractableBufferStock/TractableBufferStock.ipynb) or [Binder](https://mybinder.org/v2/gh/intertemporal-choice/intertemporal-choice.github.io/main?labpath=content/consumption/TractableBufferStock/TractableBufferStock.ipynb).

## The Microeconomic Consumer's Problem

The aggregate wage {math}`\Wage_{t}` grows by a constant factor {math}`\WGroFac` every period, reflecting exogenous labor productivity improvements:

```{math}
\Wage_{t+1} = \WGroFac \Wage_{t}.
```

The consumer lives in a small open economy, so there is a constant interest factor {math}`\Rfree`. Defining {math}`\mLvl` as **m**arket resources (net worth plus current income), {math}`\aLvl` as end-of-period **a**ssets **a**fter **a**ll **a**ctions **a**re **a**ccomplished (specifically, after the consumption decision), and {math}`\bLvl` as **b**ank **b**alances **b**efore receipt of labor income, the dynamic budget constraint can be decomposed into the following elements:

```{math}
:label: eq:TBS-DBC

\begin{aligned}
    \aLvl_{t} & =  \mLvl_{t}-\cLvl_{t}
\\  \bLvl_{t+1} & =  \Rfree \aLvl_{t}
\\  \mLvl_{t+1} & =  \bLvl_{t+1}+\labor_{t+1}\Wage_{t+1}\tranShkAll_{t+1}
\end{aligned}
```

where {math}`\labor` measures the consumer's labor productivity ("endowment") and {math}`\tranShkAll` is a dummy variable indicating the consumer's employment state: Everyone is either employed (state "e"), in which case {math}`\tranShkAll = 1`, or unemployed (state "u"), in which case {math}`\tranShkAll=0`, so that for unemployed individuals labor income is zero.

:::{margin}
We could allow for unemployment insurance by modifying the values of {math}`\tranShkAll` associated with the two states. The key conclusions would not change.
:::

(sec:TBS-Fred)=
### The Unemployed Consumer's Problem

Once a person becomes unemployed, that person can never become employed again (i.e. if {math}`\tranShkAll_{t}=0` then {math}`\tranShkAll_{t+1}=0`). Consumers have a CRRA felicity function {math}`\uFunc(\bullet)= \bullet^{1-\CRRA}/(1-\CRRA)`, and discount future felicity geometrically by {math}`\DiscFac` per period.

:::{margin}
"Felicity" refers explicitly to a one-period, or in a continuous-time model, an instantaneous utility function.
:::

The solution to the unemployed consumer's optimization problem is

:::{margin}
See [perfect foresight CRRA](#sec:PerfForesightCRRA) for a derivation, noting that human wealth is zero for the unemployed consumer.
:::

```{math}
:label: eq:TBS-cpfinfhorunemp

\cLvl^{\UnempLbl}_{t} = \underbrace{\left(1-\overbrace{\Rfree ^{-1}(\Rfree{\DiscFac})^{1/\CRRA}}^{\equiv \RPFac}\right)}_{\equiv \MPC} \bLvl_{t} ,
```

where the {math}`\UnempLbl` superscript signifies the consumer's (un)employment status; {math}`\MPC` is the marginal propensity to consume for the perfect foresight consumer, which is strictly below the MPC for the problem with uncertainty {cite:p}`carroll&kimball:concavity`; and {math}`\RPFac` is what {cite:t}`BufferStockTheory` calls the "return patience factor."

:::{margin}
The Old English letter {math}`\APFac = (\Rfree \DiscFac)^{1/\CRRA}`, which looks like a combination of {math}`\Rfree, \DiscFac,` and {math}`\CRRA`, designates the "absolute patience factor," which determines whether consumption rises ({math}`\APFac > 1`), stays the same ({math}`\APFac = 1`), or falls ({math}`\APFac < 1`) in the perfect foresight problem (see [perfect foresight CRRA](#sec:PerfForesightCRRA)). Terms like this are defined in {cite:t}`BufferStockTheory`, which we henceforth do not cite each time a new term is introduced; see it for further definition and discussion.
:::

We now impose the "return impatience condition" (RIC),

```{math}
:label: eq:TBS-RIC

\underbrace{\left(\frac{(\Rfree \DiscFac)^{1/\CRRA}}{\Rfree}\right)}_{= \RPFac} < 1
```

which deserves its name because it is the condition that guarantees that {math}`\MPC > 0`: the consumer must not be *so* patient that, given the interest rate, a boost to resources fails to boost spending. An alternative (equally correct) interpretation is that the condition guarantees that the present discounted value of consumption for the unemployed consumer is not infinity.

:::{margin}
"Pathologically patient" consumers who do not satisfy this condition can be thought of as people who would hoard any incremental resources in order to enable even more extra spending in the distant future.
:::

:::{margin}
For a perfect foresight consumer, [perfect foresight CRRA](#sec:PerfForesightCRRA) shows that consumption grows by the factor {math}`\APFac = (\Rfree\DiscFac)^{1/\CRRA}`, so if we do not impose the RIC, consumption would "want" to grow by a factor greater than the factor {math}`\Rfree` by which it is being discounted.
:::

For many purposes (not least, the calibration of the model), it turns out to be useful to alternatively express impatience conditions like {eq}`eq:TBS-RIC` in terms of the upper bound of the range of time preference factors {math}`\bar{\DiscFac}` that satisfy the condition; solving {eq}`eq:TBS-RIC` for {math}`\DiscFac`, we designate this object

```{math}
\DiscFacMaxRIC = \Rfree^{\CRRA-1}
```

and write the alternative version of the constraint as

```{math}
:label: eq:TBS-DiscountMaxRIC

\DiscFac < \DiscFacMaxRIC .
```

{math}`\RPFac` is the "return patience factor" because it defines the patience factor {math}`\APFac` relative to the return factor {math}`\Rfree`; correspondingly, we define the "return patience rate" as lower-case

```{math}
:label: eq:TBS-patr

\begin{aligned}
   \RPRte & \equiv   \log \RPFac
\\ & \approx \RPFac - 1
\\ & =  -\MPC
\end{aligned}
```

and we say that a consumer is "return impatient" if the RIC {eq}`eq:TBS-RIC` holds (equivalent conditions are {math}`\RPRte < 0` and {math}`\MPC > 0`).

:::{margin}
Throughout, we will casually treat logs of factors like {math}`\RPFac` as equivalent to the level minus 1; that is, we will treat expressions like those in {eq}`eq:TBS-patr` as interchangeable, which is an appropriate approximation so long as the factor is "close" to 1.
:::

### The Employed Consumer's Problem

(sec:TBS-uMPS)=
#### Unemployment Risk as a Mean Preserving Spread in Human Wealth

If a person who is employed in period {math}`t` ({math}`\tranShkAll_{t}=1`) is still employed next period ({math}`\tranShkAll_{t+1}=1`), market resources will be

```{math}
:label: eq:TBS-MLevtp1

\mLvl^{\EmpLbl}_{t+1} = (\mLvl^{\EmpLbl}_{t}-\cLvl^{\EmpLbl}_{t})\Rfree+\Wage_{t+1}\labor_{t+1}.
```

But employed consumers face a constant risk {math}`\urate` of becoming unemployed. It will be convenient to define {math}`\erate\equiv 1-\urate` as the probability that a consumer does *not* become unemployed. Whether the consumer is employed or not, their labor productivity {math}`\labor` is well-defined: For convenience, {math}`\labor` is assumed to grow by a factor {math}`\erate^{-1}` every period,

:::{margin}
"Labor productivity" is purely hypothetical for a consumer who is unemployed; but defining it even for unemployed consumers simplifies notation and some later analysis.
:::

```{math}
:label: eq:TBS-meanPreserve

\labor_{t+1} =    \labor_{t}/\erate ,
```

which means that for a consumer who remains employed, labor income will grow by factor

```{math}
\WGroFachFix = \WGroFac/\erate
```

so that the *expected* labor income growth factor for employed consumers is the same {math}`\WGroFac` as in the perfect foresight case:

```{math}
\begin{aligned}
  \Ex_{t}[\Wage_{t+1}\labor_{t+1}\tranShkAll_{t+1}] & =   \left(\frac{\labor_{t} \WGroFac \Wage_{t}}{\erate}\right)\left(\urate \times 0 + \erate \times 1 \right)
\\ \left(\frac{\Ex_{t}[\Wage_{t+1}\labor_{t+1}\tranShkAll_{t+1}]}{\Wage_{t} \labor_{t}}\right) &  =  \WGroFac
,
\end{aligned}
```

which is the reason for {eq}`eq:TBS-meanPreserve`'s assumption about the growth of individual labor productivity: An increase in {math}`\urate` is a pure increase in uncertainty with no effect on the present discounted value of expected labor income ("human wealth"); an increase in {math}`\urate` therefore constitutes a "mean-preserving spread" in human wealth.

:::{margin}
In a model with more realistic shocks – like a lognormal distribution of permanent shocks – a mean-preserving increase in uncertainty might constitute, say, a spread in the distribution of permanent shocks.
:::

#### First Order Optimality Condition

The same solution methods used in [perfect foresight CRRA](#sec:PerfForesightCRRA) can be applied here too (take the first order condition with respect to {math}`\cLvl`, use the [Envelope theorem](#sec:Envelope)); the only difference is the need to keep the expectations operator in place. Using {math}`\bullet` as a placeholder for "e" or "u," the usual steps lead to the standard consumption Euler equation:

```{math}
:label: eq:TBS-ctp1Oct

\begin{aligned}
        \uFunc^{\prime}(\cLvl^{\EmpLbl}_{t}) & =  \Rfree\DiscFac \Ex_{t}\left[\uFunc^{\prime}(\cLvl^{\bullet}_{t+1}) \right]
\\  1         & =  \Rfree\DiscFac \Ex_{t}\left[\left(\frac{\cLvl^{\bullet}_{t+1}}{\cLvl^{\EmpLbl}_{t}}\right)^{-\CRRA} \right]
.
\end{aligned}
```

Defining nonbold variables as the bold equivalent divided by the level of permanent labor income for an employed consumer, e.g. {math}`{\cNrm}^{\EmpLbl}_{t}=\cLvl^{\EmpLbl}_{t}/(\Wage_{t}\labor_{t})`, we can rewrite the consumption Euler equation as

```{math}
:label: eq:TBS-Explicit

\begin{aligned}
  1         & =  \Rfree\DiscFac \Ex_{t}\left[\left(\frac{{\cNrm}^{\bullet}_{t+1} \Wage_{t+1}\labor_{t+1}}{{\cNrm}^{\EmpLbl}_{t} \Wage_{t}\labor_{t}}\right)^{-\CRRA} \right]
\\          & =  \Rfree\DiscFac \Ex_{t}\left[\left(\frac{{\cNrm}^{\bullet}_{t+1}}{{\cNrm}^{\EmpLbl}_{t}}\WGroFachFix\right)^{-\CRRA} \right]
\\          & =  \WGroFachFix^{-\CRRA}\Rfree\DiscFac \Ex_{t}\left[\left(\frac{{\cNrm}^{\bullet}_{t+1}}{{\cNrm}^{\EmpLbl}_{t}}\right)^{-\CRRA} \right]
\\          & =  \WGroFachFix^{-\CRRA}\Rfree\DiscFac \left\{(1-\urate)\left(\frac{{\cNrm}^{\EmpLbl}_{t+1}}{{\cNrm}^{\EmpLbl}_{t}}\right)^{-\CRRA}+\urate \left(\frac{\cNrmU_{t+1}}{{\cNrm}^{\EmpLbl}_{t}}\right)^{-\CRRA}\right\}
\end{aligned}
```

#### Analysis and Intuition of Consumption Growth

It will be useful now to define a "growth patience factor" (terminology justified below):

```{math}
:label: eq:TBS-GPFacRaw

\GPFachFix = \left(\frac{(\Rfree\DiscFac)^{1/\CRRA}}{\WGroFachFix}\right),
```

which is the factor by which {math}`{\cNrm}^{\EmpLbl}` would grow in the perfect foresight version of the model with permanent income growth factor {math}`\WGroFachFix` (again see [perfect foresight CRRA](#sec:PerfForesightCRRA)). Using this, {eq}`eq:TBS-Explicit` can be written as

```{math}
:label: eq:TBS-BeforePFStep

\begin{aligned}
        1  & = \GPFachFix^{\CRRA} \left(\frac{{\cNrm}^{\EmpLbl}_{t+1}}{{\cNrm}^{\EmpLbl}_{t}}\right)^{-\CRRA} \left\{(1-\urate)+\urate\left[\left(\frac{\cNrmU_{t+1}}{{\cNrm}^{\EmpLbl}_{t}}\right)\left(\frac{{\cNrm}^{\EmpLbl}_{t}}{{\cNrm}^{\EmpLbl}_{t+1}}\right)\right]^{-\CRRA}\right\}
\\       & = \GPFachFix^{\CRRA} \left(\frac{{\cNrm}^{\EmpLbl}_{t+1}}{{\cNrm}^{\EmpLbl}_{t}}\right)^{-\CRRA} \left\{1+\urate\left[\left(\frac{\cNrmU_{t+1}}{{\cNrm}^{\EmpLbl}_{t+1}}\right)^{-\CRRA}-1\right]\right\}
\\       \left(\frac{{\cNrm}^{\EmpLbl}_{t+1}}{{\cNrm}^{\EmpLbl}_{t}}\right)^{\CRRA} & = \GPFachFix^{\CRRA} \left\{1+\urate\left[\left(\frac{{\cNrm}^{\EmpLbl}_{t+1}}{\cNrmU_{t+1}}\right)^{\CRRA}-1\right]\right\}
\\       \left(\frac{{\cNrm}^{\EmpLbl}_{t+1}}{{\cNrm}^{\EmpLbl}_{t}}\right) & = {\GPFachFix} \left\{1+\urate\left[\left(\frac{{\cNrm}^{\EmpLbl}_{t+1}}{\cNrmU_{t+1}}\right)^{\CRRA}-1\right]\right\}^{1/\CRRA}.
\end{aligned}
```

(This is where the perfect foresight assumption is important; without it {eq}`eq:TBS-BeforePFStep` would be

```{math}
:label: eq:TBS-BeforePFStepWithEx

1 = \GPFachFix^{\CRRA} \Ex_{t}\left[\left(\frac{{\cNrm}^{\EmpLbl}_{t+1}}{{\cNrm}^{\EmpLbl}_{t}}\right)^{-\CRRA} \left\{1+\urate\left[\left(\frac{\cNrmU_{t+1}}{{\cNrm}^{\EmpLbl}_{t+1}}\right)^{-\CRRA}-1\right]\right\}\right]
```

and we would be unable to proceed.)

Now define {math}`\cGap _{t+1} \equiv \left(\frac{{\cNrm}^{\EmpLbl}_{t+1}-\cNrmU_{t+1}}{\cNrmU_{t+1}}\right)` (which is the proportion by which consumption would be greater next period for an employed than for an unemployed person), and define an "excess prudence" factor

:::{margin}
Mnemonic: {math}`\cGap` is like {math}`\Delta`, a change, but it points down, because it measures the fall in consumption if unemployment strikes.
:::

```{math}
\prudEx = \left(\frac{\CRRA-1}{2}\right).
```

The [appendix on approximate consumption growth](#sec:TBS-CGroApprox) shows that, with some approximations, we can rewrite {eq}`eq:TBS-BeforePFStep` as

```{math}
:label: eq:TBS-cedelapprox

\left(\frac{{\cNrm}^{\EmpLbl}_{t+1}}{{\cNrm}^{\EmpLbl}_{t}}\right) \approx \left(1+ \urate (1+\prudEx\cGap _{t+1})\cGap _{t+1}\right) {\GPFachFix}
```

which can be simplified in the logarithmic utility case (where {math}`\prudEx = 0`) to

```{math}
:label: eq:TBS-cedelapproxLog

\left(\frac{{\cNrm}^{\EmpLbl}_{t+1}}{{\cNrm}^{\EmpLbl}_{t}}\right) \approx \left(1+ \urate \cGap _{t+1}\right) {\GPFachFix} .
```

Now since consumption if employed {math}`{\cNrm}^{\EmpLbl}_{t+1}` is surely greater than consumption if unemployed {math}`\cNrmU_{t+1}`, {math}`\cGap _{t+1}` is certainly a positive number. But since {math}`{\GPFachFix}` is the value that {math}`{\cNrm}^{\EmpLbl}_{t+1}/{\cNrm}^{\EmpLbl}_{t}` would exhibit in a perfect foresight model, this equation tells us that uncertainty boosts the growth of consumption for a consumer who stays employed; in the logarithmic case, that growth is augmented by an amount proportional to the probability of becoming unemployed {math}`\urate` multiplied by the size of the "consumption risk" (the amount by which consumption would fall if unemployment occurs).

We noted above that for any given {math}`\mNrmE_{t}`, an increase in uncertainty constitutes a mean-preserving spread in human wealth; thus the "human wealth effect" of an increase in {math}`\urate` would be zero for a consumer without a precautionary motive. In this small-open-economy model a change in {math}`\urate` also has no effect on the interest rate {math}`\rfree`, and so none of the conventional determinants of consumption in the perfect foresight model (the income, substitution, and human wealth effects) is affected by a change in uncertainty. Not all of the increase in the growth of {math}`{\cNrm}^{\EmpLbl}` in {eq}`eq:TBS-cedelapprox` or {eq}`eq:TBS-cedelapproxLog` is precautionary, though. {math}`{\cNrm}^{\EmpLbl}_{t+1}` is consumption in the event that the consumer stays employed, which exceeds expected consumption even for a consumer with no precautionary motive: with quadratic utility and {math}`\Rfree\DiscFac=1`, consumption is a martingale, {math}`\cLvl^{\EmpLbl}_{t} = \Ex_{t}[\cLvl^{\bullet}_{t+1}]`, so {math}`\cLvl^{\EmpLbl}_{t+1}/\cLvl^{\EmpLbl}_{t} = 1/(1-\urate\cGap_{t+1}/(1+\cGap_{t+1})) \approx 1+\urate\cGap_{t+1}`. The precautionary motive shows up in *expected* consumption growth. Since {math}`\cLvl^{\UnempLbl}_{t+1} = \cLvl^{\EmpLbl}_{t+1}/(1+\cGap_{t+1})`, multiplying {eq}`eq:TBS-cedelapprox` by {math}`\WGroFachFix` and dropping terms of order {math}`\urate^{2}` or {math}`\cGap^{3}` gives

```{math}
\begin{aligned}
\Ex_{t}[\cLvl^{\bullet}_{t+1}]/\cLvl^{\EmpLbl}_{t} & = \left(\cLvl^{\EmpLbl}_{t+1}/\cLvl^{\EmpLbl}_{t}\right)\left(1-\urate\cGap_{t+1}/(1+\cGap_{t+1})\right)
\\ & \approx \APFac\left(1+\urate(1+\prudEx)\cGap_{t+1}^{2}\right) = \APFac\left(1+(\urate/2)(\CRRA+1)\cGap_{t+1}^{2}\right) .
\end{aligned}
```

Expected consumption grows faster than in the perfect foresight model by an amount proportional to {math}`\CRRA+1`, the coefficient of relative prudence of CRRA utility, and to {math}`\urate\cGap_{t+1}^{2}`, approximately the variance of the proportional change in consumption. Furthermore, because a profile with faster expected consumption *growth* can only exhibit the *same expected present discounted value* if that faster growth *starts* from a lower initial consumption *level*, we know that for any given initial value of {math}`\mNrmE`, the introduction of a risk of becoming unemployed {math}`\urate` induces a (precautionary) decline in consumption (and corresponding increase in saving).

Furthermore, under the (compelling) assumption that {math}`\CRRA > 1`, {eq}`eq:TBS-cedelapprox` implies that a consumer with a higher degree of prudence (larger {math}`\CRRA` and therefore larger {math}`\prudEx`) will anticipate a greater increment to consumption growth as a consequence of the introduction of uncertainty. This reflects the greater precautionary saving motive induced by a higher degree of prudence.

#### Finding the Target

The target level of {math}`\mNrm^{\EmpLbl}` (if one exists) will be the point of intersection between the {math}`\dcEqZero` and {math}`\dmEqZero` loci. Here and below, a variable without a time subscript denotes its value on a locus along which it does not change from one period to the next; the target itself is marked with a hat, as in {math}`\mTrgNrm^{\EmpLbl}`.

The {math}`\dcEqZero` locus can be characterized by substituting {math}`{\cNrm}^{\EmpLbl}_{t+1}={\cNrm}^{\EmpLbl}_{t} \equiv {\cNrm}^{\EmpLbl}`:

```{math}
:label: eq:TBS-straightDef

\begin{aligned}
         1 & = \left\{1+\urate\left[\left(\frac{{\cNrm}^{\EmpLbl}_{t+1}}{\cNrm_{t+1}^{\UnempLbl}}\right)^{\CRRA}-1\right]\right\} \GPFachFix^{\CRRA}
\\ \GPFachFix^{-\CRRA} & =  (1-\urate)+\urate\left(\frac{{\cNrm}^{\EmpLbl}}{\cNrm_{t+1}^{\UnempLbl} }\right)^{\CRRA}
\\ \underbrace{\left(\frac{\GPFachFix^{-\CRRA}-1+\urate}{\urate}\right)^{1/\CRRA}}_{\equiv \straight} & =   \left(\frac{{\cNrm}^{\EmpLbl}}{\cNrmU_{t+1}}\right)
  \\ \underbrace{\left(1+\urate^{-1}(\GPFachFix^{-\CRRA}-1)\right)^{1/\CRRA}}_{=\straight} & =   \left(\frac{{\cNrm}^{\EmpLbl}}{\cNrmU_{t+1}}\right)
\end{aligned}
```

which boils down to

```{math}
:label: eq:TBS-cRatEtfmcRatUtp1

{\cNrm}^{\EmpLbl} = \cNrm^{\UnempLbl}_{t+1} \straight .
```

The importance of the linearity of the consumption function of the unemployed consumer now becomes evident: It means that the right-hand side of {eq}`eq:TBS-cRatEtfmcRatUtp1` is linear in {math}`\cNrm^{\EmpLbl}_{t}`:

```{math}
:label: eq:TBS-PSTerm

\cNrm^{\EmpLbl}_{t} = \overbrace{(\mNrm^{\EmpLbl}_{t}-{\cNrm}^{\EmpLbl}_{t})\RNrmByG \MPC}^{\cNrm^{\UnempLbl}_{t+1}} \straight .
```

We know that {math}`\mNrmE_{t}-{\cNrm}^{\EmpLbl}_{t} > 0` because a consumer in these circumstances (facing possible perpetual unemployment) will never borrow (see [consumption function](#fig:TBS-cFunc)). Since the RIC imposes {math}`\MPC>0`, {eq}`eq:TBS-PSTerm` tells us that steady-state consumption (if it exists) is a positive finite number so long as {math}`\straight > 0`. That holds if and only if the numerator on the left-hand side of {eq}`eq:TBS-straightDef` is a positive finite number, which requires

:::{margin}
Under some parameter values, the model has solutions under which the consumer always spends less than the amount that would leave {math}`\mNrmE` constant, and so accumulates forever.
:::

```{math}
:label: eq:TBS-GICExistsSoln

\begin{aligned}
        \WGroFachFix^{\CRRA}(\Rfree\DiscFac)^{-1}-(1-\urate) & >  0  \\
       \WGroFachFix^{\CRRA} & >  (\Rfree \DiscFac (1-\urate))
\\     1 & >  \left(\frac{(\Rfree \DiscFac (1-\urate))^{1/\CRRA}}{\WGroFachFix}\right) = \GPFachFix (1-\urate)^{1/\CRRA}
.\end{aligned}
```

#### Upper Bounds for {math}`\DiscFac`, Given Other Parameters

As with the RIC, it may be useful to rewrite this as defining an upper bound to the time preference factors that satisfy it:

```{math}
:label: eq:TBS-DiscountMaxGICTBS

\DiscFac < \DiscFacMaxGICTBS = \left(\frac{\WGroFachFix^{\CRRA}}{\Rfree(1-\urate)}\right) .
```

In the limit as {math}`\urate` approaches zero, {eq}`eq:TBS-GICExistsSoln` reduces to a requirement that the growth patience factor is less than one,

```{math}
:label: eq:TBS-GICPGro

\GPFachFix < 1 ,
```

which, as in [perfect foresight CRRA](#sec:PerfForesightCRRA), we call a "growth impatience condition" (GIC) by analogy to the "return impatience condition" {eq}`eq:TBS-RIC` imposed earlier. [Perfect foresight CRRA](#sec:PerfForesightCRRA) shows that the limit of {eq}`eq:TBS-GICExistsSoln` as {math}`\urate \downarrow 0`, {math}`\WGroFac > \APFac`, ensures that a consumer facing no uncertainty is sufficiently impatient that their wealth-to-permanent-income ratio will fall over time. We label the weaker condition {eq}`eq:TBS-GICExistsSoln` the "GIC-TBS" (the version of the GIC required for the {math}`\dcEqZero` locus to exist and slope upward in the Tractable Buffer Stock model). It will always hold if the plain-vanilla {math}`\GICWGro` holds because {math}`\urate \geq 0`. A target level of wealth requires more: the {math}`\GIChFix`, {math}`\GPFachFix < 1`, which is stronger than the GIC-TBS but weaker than the {math}`\GICWGro`, because {math}`\WGroFachFix \geq \WGroFac`. Thus, a consumer who, in the absence of uncertainty, would satisfy both the RIC and the {math}`\GICWGro`, will have a positive finite target level of wealth when uncertainty is introduced.

:::{margin}
See the [appendix on conditions for a target](#sec:TBS-mTargExists) for a proof that, given the RIC, the {math}`\GIChFix` condition is both necessary and sufficient for the existence of a target level of wealth.
:::

When it is useful to distinguish the version of the GIC that applies in the model with income growth of {math}`\WGroFac` from the corresponding condition when growth is {math}`\WGroFachFix` we will label the two conditions {math}`\GIChFix` and {math}`\GICWGro`, and the corresponding bounds on {math}`\DiscFac` are

```{math}
\begin{aligned}
   \DiscFac < \DiscFacMaxGIChFix & =  \left(\frac{\WGroFachFix^{\CRRA}}{\Rfree}\right)
\\ \DiscFac < \DiscFacMaxGICWGro & =  \left(\frac{\WGroFac^{\CRRA}}{\Rfree}\right)
\end{aligned}
```

Using {math}`\WGroRtehFix \equiv \log \WGroFachFix`, we similarly define the corresponding "growth patience rate":

```{math}
\GPRtehFix \equiv \log \GPFachFix \approx \CRRA^{-1}(\rfree-\discRte) - \WGroRtehFix
```

so that the growth impatience condition {eq}`eq:TBS-GICExistsSoln` (the GIC-TBS) can also be written (approximately) as

```{math}
:label: eq:TBS-GICrateUsingpGro

\GPRtehFix - \CRRA^{-1}\urate < 0
```

or, since {math}`\WGroRtehFix \approx \WGroRte+\urate`,

```{math}
:label: eq:TBS-GICrateUsingwGro

\CRRA^{-1}(\rfree-\discRte-\urate)-(\WGroRte+\urate) < 0 .
```

(sec:TBS-URiskGrowthImpatience)=
#### Why Increased Unemployment Risk Increases Effective Growth Impatience

Equation {eq}`eq:TBS-GICrateUsingwGro` becomes easier to satisfy (in the sense of requiring a lower {math}`\discRte`) as {math}`\urate` increases, since in both places where {math}`\urate` appears on the left-hand side it is with a negative coefficient.

The reason the two appearances of {math}`\urate` have not been combined in {eq}`eq:TBS-GICrateUsingwGro` is that the separate terms reflect two logically distinct effects. The first appearance, where {math}`\urate` is premultiplied by {math}`-\CRRA^{-1}`, can be interpreted as capturing the sense in which an increase in {math}`\urate` is like an increase in the discounting of the future (the coefficient on {math}`\urate` is the same as that on {math}`\discRte`). This downweighting of the future occurs precisely because that future might not occur (if the consumer becomes unemployed). The effect is much like the increase in discounting that occurs when a positive probability of death is introduced in consumption problems, cf. {cite:t}`blanchardFinite`.

:::{margin}
A different future (with the consumer unemployed) does occur; but here we are effectively analyzing the behavior of a consumer *contingent on that consumer remaining employed*.
:::

The second, separate, reason {math}`\urate` strengthens growth impatience (that is, weakens the GIC: the GIC-TBS holds in more circumstances than the {math}`\GICWGro`) is that we adjust labor productivity growth so that {math}`\WGroRtehFix\approx\WGroRte+\urate` in order to maintain constant human wealth for different values of {math}`\urate` (eq. {eq}`eq:TBS-meanPreserve`). For higher {math}`\urate`, permanent income growth is greater *conditional on remaining employed*; the continuously-employed consumer is effectively more "impatient" in the relevant sense of desiring consumption growth slower than income growth.

This is essentially a mechanical result, which reflects our model's design for the purpose of examining thought experiments that manipulate the degree of uncertainty while leaving the perfect-foresight level of human wealth constant.

Note that although {math}`\urate` is our measure of uncertainty, neither of these effects of {math}`\urate` is in any meaningful sense directly a "precautionary" effect; instead, they both reflect effects of {math}`\urate` on the relevant degree of growth impatience in the GIC-TBS condition.

#### The Target Level of {math}`\mNrmE`

The [appendix on conditions for a target](#sec:TBS-mTargExists) demonstrates that, given the RIC, the {math}`\GIChFix` is necessary and sufficient for the existence of a target value of market resources {math}`\mTrgNrm^{\EmpLbl}`; the weaker GIC-TBS guarantees only that the {math}`\dcEqZero` locus exists and slopes upward, while for {math}`\CRRA > 1`, the consumption function exists whether or not the GIC-TBS holds. The [appendix on the exact target formula](#sec:TBS-mTargExact) solves for an explicit formula for that target.

Briefly, this is accomplished as follows. We can obtain the {math}`\dcEqZero` locus by substituting {math}`{\cNrm}^{\EmpLbl}_{\prdt+1}={\cNrm}^{\EmpLbl}_{\prdt}={\cNrm}^{\EmpLbl}` into equation {eq}`eq:TBS-PSTerm`:

```{math}
:label: eq:TBS-cDelEqZero

\begin{aligned}
  {\cNrm}^{\EmpLbl} & =  \mNrmE \RNrmByG\MPC\straight - {\cNrm}^{\EmpLbl} \RNrmByG\MPC\straight
\\  {\cNrm}^{\EmpLbl} & =  \left(\frac{\RNrmByG\MPC\straight}{1+\RNrmByG\MPC\straight}\right)\mNrmE.
\end{aligned}
```

Now we need to use a normalized version of the dynamic budget constraint (equation {eq}`eq:TBS-MLevtp1`),

```{math}
:label: eq:TBS-metp1

\mNrmE_{t+1} = (\mNrmE_{t}-{\cNrm}^{\EmpLbl}_{t})\RNrmByG+1
```

to derive the {math}`\mNrmE_{t+1}=\mNrmE_{t}=\mNrmE` locus (also referred to as the {math}`\dmEqZero` locus):

```{math}
:label: eq:TBS-mDelEqZero

\begin{aligned}
      \RNrmByG^{-1}(\mNrmE-1) & =  \mNrmE-{\cNrm}^{\EmpLbl}
\\      {\cNrm}^{\EmpLbl} & =  \mNrmE-\RNrmByG^{-1}(\mNrmE-1)
\\       & =  (1-\RNrmByG^{-1})\mNrmE+\RNrmByG^{-1}.
\end{aligned}
```

The steady-state levels of {math}`\mNrmE` and {math}`{\cNrm}^{\EmpLbl}` are the values of these two variables at which both {eq}`eq:TBS-mDelEqZero` and {eq}`eq:TBS-cDelEqZero` hold. This is just a set of two linear equations and two unknowns, and with a bit of algebra can be solved explicitly.

#### Finite Human Wealth and the Existence of a Target

Interestingly, the limit of the buffer stock model as {math}`\urate \downarrow 0` is *not* the perfect foresight solution obtained when {math}`\urate` is exactly equal to zero.

[Perfect foresight CRRA](#sec:PerfForesightCRRA) shows that in the perfect foresight context, it is necessary to impose the Finite Human Wealth Condition {math}`\Rfree > \WGroFac` (henceforth, {math}`\FHWCWGro`) to obtain a sensible solution. But if the {math}`\FHWCWGro` holds, the {math}`\GICWGro` is strictly stronger than the RIC, because the combination {math}`\APFac/\WGroFac < 1` and {math}`\Rfree > \WGroFac` obviously implies {math}`\APFac/\Rfree < 1`. If we substitute {math}`\WGroFachFix` for {math}`\WGroFac`, we can define the corresponding version of the condition in the case where growth is {math}`\WGroFachFix`: the {math}`\FHWChFix`.

:::{margin}
The [appendix to perfect foresight CRRA](#sec:PFwhenFHWfails) shows that if the {math}`\FHWCWGro` fails, the limit of the perfect foresight model is {math}`\cFunc(\mNrm)=\infty \forall \mNrm`, which is not a useful or plausible solution.
:::

It turns out that in the buffer stock model, we can relax the requirement that human wealth is finite.

The [GIC-TBS](#eq:TBS-GICExistsSoln), which is necessary for the existence of a steady-state level of consumption, reduces to the {math}`\GIChFix` in the case being considered here, the limit as {math}`\urate \downarrow 0`. The interesting question is therefore what happens when the {math}`\FHWCWGro` does not hold (that is {math}`\WGroFac > \Rfree`).

Given that the {math}`\GICWGro` holds, if the {math}`\FHWCWGro` does not hold the RIC may or may not hold: {math}`\WGroFac > \Rfree` implies that {math}`\APFac/\Rfree > \APFac/\WGroFac` but {math}`1 > \APFac/\WGroFac` could be consistent with {math}`\APFac/\Rfree` being greater or less than one. But recall that our assumption is that the unemployed consumer is assumed to behave according to the perfect foresight model with human wealth equal to zero. We must therefore impose the RIC in order to obtain a nondegenerate solution.

For any finite horizon, human wealth is finite, and there is a positive probability that income will be zero over the remainder of the horizon. This puts a strict bound on the extent to which consumers are willing to rely for current consumption upon future income that is unbounded in expectation (as the horizon extends) but potentially bounded in practice. In effect, the precautionary motive introduces a self-imposed borrowing constraint that prevents the (arbitrarily large) amount of future income from being something the consumer is willing to borrow against.

The consequence is that, given the RIC, the limiting model (as {math}`\urate \downarrow 0`) exhibits, for {math}`\CRRA > 1`, a solution with a unique finite target {math}`\mNrmE` so long as the {math}`\GIChFix` holds, *even if human wealth is infinite*; in this case the {math}`\dmEqZero` locus is downward sloping (because {math}`\Rfree < \WGroFachFix` means {math}`\RNrmByG < 1`, so its slope {math}`1-\RNrmByG^{-1}` in [the locus's equation](#eq:TBS-mDelEqZero) is negative) while the {math}`\dcEqZero` locus is upward sloping (as guaranteed by the [GIC-TBS](#eq:TBS-GICExistsSoln), which the {math}`\GIChFix` implies). Thus, a target {math}`\mNrmE` will exist. (The {math}`\GIChFix` holds automatically here: {math}`\RNrmByG < 1` and the RIC give {math}`\GPFachFix = \RNrmByG\RPFac < \RPFac < 1`.)

The conditions used in this chapter, and what each guarantees, are summarized below. They nest: the {math}`\GICWGro` implies the {math}`\GIChFix`, which implies the GIC-TBS.

| Condition | Inequality | Bound on {math}`\DiscFac` | In rates (approximately) | Guarantees |
|---|---|---|---|---|
| RIC | {math}`\RPFac < 1` | {math}`\DiscFac < \Rfree^{\CRRA-1}` | {math}`\CRRA^{-1}(\rfree-\discRte) < \rfree` | {math}`\MPC > 0`: the unemployed consumer's problem has a solution |
| {math}`\FHWCWGro` | {math}`\WGroFac < \Rfree` | | {math}`\WGroRte < \rfree` | human wealth {math}`\hNrm` is finite, so the perfect foresight {math}`\bar{\cFunc}` exists |
| {math}`\FHWChFix` | {math}`\WGroFachFix < \Rfree` | | {math}`\WGroRtehFix < \rfree` | the {math}`\dmEqZero` locus slopes upward |
| {math}`\GICWGro` | {math}`\APFac < \WGroFac` | {math}`\DiscFac < \WGroFac^{\CRRA}/\Rfree` | {math}`\CRRA^{-1}(\rfree-\discRte) < \WGroRte` | a perfect foresight consumer's wealth ratio falls |
| {math}`\GIChFix` | {math}`\GPFachFix < 1` | {math}`\DiscFac < \WGroFachFix^{\CRRA}/\Rfree` | {math}`\CRRA^{-1}(\rfree-\discRte) < \WGroRtehFix` | with the RIC, a target {math}`\mTrgNrm^{\EmpLbl}` exists (necessary and sufficient) |
| GIC-TBS | {math}`\GPFachFix(1-\urate)^{1/\CRRA} < 1` | {math}`\DiscFac < \WGroFachFix^{\CRRA}/(\Rfree(1-\urate))` | {math}`\CRRA^{-1}(\rfree-\discRte-\urate) < \WGroRte+\urate` | {math}`\straight > 0`: the {math}`\dcEqZero` locus exists and, with the RIC, slopes upward |

#### Approximations to the Target

In the special case of logarithmic utility ({math}`\CRRA = 1`), the [approximation appendix](#sec:TBS-mTargApprox) shows that (under some strong assumptions) an approximation to target market resources will be given by

```{math}
:label: eq:TBS-mTargetLogCase

\mTrgNrm^{\EmpLbl} \approx 1 + \left(\frac{1}{(\WGroRtehFix-\rfree)+\discRte(1+(\WGroRtehFix+\discRte-\rfree)/\urate)}\right)
```

and that the RIC and the {math}`\GIChFix` guarantee that the denominator of the fraction is a positive number.

This expression encapsulates several of the key intuitions of the model. The "human wealth effect" of growth, which {cite:t}`summersCapTax` emphasized, is captured by the first {math}`\WGroRtehFix` term in the denominator; clearly, for any calibration for which the denominator is a positive number, increasing {math}`\WGroRtehFix` will increase the size of the denominator and therefore reduce the target level of wealth. The human wealth effect of interest rates is correspondingly captured by the {math}`-\rfree` term. An increase in the future discounting rate, {math}`\discRte`, will also increase the size of the denominator and therefore reduce target wealth. Finally, holding {math}`\WGroRtehFix` fixed, a reduction in unemployment risk will boost {math}`(\WGroRtehFix+\discRte-\rfree)/\urate` and therefore reduce target wealth. Under the model's design, though, {math}`\WGroRtehFix \approx \WGroRte+\urate` moves with {math}`\urate` to keep human wealth fixed; substituting it, the derivative of the denominator with respect to {math}`\urate` is {math}`1-\discRte(\WGroRte+\discRte-\rfree)/\urate^{2}`, so a reduction in unemployment risk reduces target wealth only if {math}`\discRte(\WGroRte+\discRte-\rfree) > \urate^{2}`, as it does at the benchmark values of these parameters.

:::{margin}
Under {math}`\log` utility ({math}`\CRRA=1`), {math}`(\WGroRtehFix+\discRte-\rfree) > 0` is (approximately) the {math}`\GIChFix`, {math}`\WGroRtehFix > \CRRA^{-1}(\rfree-\discRte)`; the weaker GIC-TBS {eq}`eq:TBS-GICrateUsingwGro` does not guarantee it.
:::

The assumption of log utility is restrictive, and probably does not capture sufficient aversion to consumption fluctuations. Fortunately, another special case helps to illuminate the effect of higher levels of prudence. The [approximation appendix](#sec:TBS-mTargApprox) shows that, in the special case where {math}`\discRte=\rfree`, the target level of wealth will be approximable by

```{math}
:label: eq:TBS-mTargetrEqdelta

\mTrgNrm^{\EmpLbl} \approx 1 + \left(\frac{1}{(\WGroRtehFix-\rfree)+\discRte(1+(\WGroRtehFix/\urate)(1-(\WGroRtehFix/\urate)\prudEx))}\right)
```

which is like {eq}`eq:TBS-mTargetLogCase` (with {math}`\discRte-\rfree=0`) but with the addition of the final term involving {math}`\prudEx` which measures the amount by which prudence exceeds the logarithmic benchmark. An increase in {math}`\prudEx` reduces the denominator of {eq}`eq:TBS-mTargetrEqdelta` and thereby boosts the target level of wealth: Exactly what would be expected from an increase in the intensity of the precautionary motive.

Note that the different effects *interact* with each other, in the sense that the strength of, say, the human wealth effect will vary depending on the values of the other parameters. The ways in which these interactions make intuitive sense will repay deep reflection. (Hint: how much a consumer cares about the future governs the power that future events have in determining the target; use the formula to think about why.)

#### The Phase Diagram

The figures use a benchmark calibration chosen to show the model's features clearly rather than for realism: {math}`\urate = 0.005`, {math}`\discRte = 0.10` (so {math}`\DiscFac = 1/1.10`), {math}`\Rfree = 1.03`, {math}`\WGroFac = 1` and {math}`\CRRA = 2` (and, for the small open economy, {math}`\PopnGroFac = 1.01`). It implies {math}`\RPFac \approx 0.939`, so {math}`\MPC \approx 0.061`; {math}`\GPFachFix \approx 0.963`, so the {math}`\GIChFix` holds; and a target {math}`\mTrgNrm^{\EmpLbl} \approx 5.48`, with {math}`\cTrgNrm^{\EmpLbl} \approx 1.11`.

{numref}`fig:TBS-PhaseDiag` presents the phase diagram.

:::{figure} figures/PhaseDiag.png
:name: fig:TBS-PhaseDiag
:class: note-under

Phase Diagram

Note: The {math}`\dcEqZero` and {math}`\dmEqZero` loci cross at the target; the stable arm through it is the consumption function, and the arrows show the direction of motion in each region.
:::

The {math}`\Delta \mNrmE = 0` locus, given in {eq}`eq:TBS-mDelEqZero`, indicates, for a given level of {math}`\mNrmE`, how much consumption {math}`{\cNrm}^{\EmpLbl}` would be exactly the right amount to leave {math}`\mNrmE` unchanged. Call this the "permanently sustainable consumption locus," or for short "sustainable consumption." For any given {math}`\mNrmE`, consuming an amount less than the "sustainable" level will cause wealth to rise (and conversely for points above {math}`\Delta \mNrmE =0`). This provides the logic for the horizontal arrows of motion in the diagram: Above the sustainable consumption locus they point left, and below they point right.

:::{margin}
Some authors refer to {math}`\Delta \mNrmE = 0` as giving the level of "permanent income," but this definition differs from {cite:t}`friedmanATheory`'s and is problematic because it could be confused with "permanent labor income" {math}`\Wage_{t} \labor_{t}`.
:::

The intuition for the {math}`\Delta {\cNrm}^{\EmpLbl}=0` locus (which comes from {eq}`eq:TBS-cDelEqZero`) is a bit subtler, because it reflects preferences: it comes from the Euler equation, not from the budget constraint, which gives the {math}`\Delta \mNrmE = 0` locus. Take a point on the {math}`\Delta {\cNrm}^{\EmpLbl}=0` locus, and consider how things would change if {math}`\mNrmE` were a bit higher at the same {math}`\cNrmE`. Recall that the growth rate of consumption consistent with the Euler equation {eq}`eq:TBS-ctp1Oct` depends on the amount by which consumption will fall if the bad state is realized, {math}`\cGap_{t+1} = \cNrmE_{t+1}/\cNrmU_{t+1}-1`. But {math}`\cNrmU_{t+1} = \MPC \RNrmByG (\mNrmE_{t} - \cNrmE_{t})` so at the same {math}`\cNrmE_{t}` but a greater {math}`\mNrmE_{t}`, {math}`\cNrmU_{t+1}` will be larger. If {math}`\cNrmE_{t+1}` were to remain unchanged, then with the larger {math}`\cNrmU_{t+1}` the ratio {math}`\cGap_{t+1} = \cNrmE_{t+1}/\cNrmU_{t+1}-1` would be smaller.

The consequences of this are easiest to see in the logarithmic case whose consumption growth equation is derived in {eq}`eq:TBS-cedelapproxLog`, which tells us that {math}`{\cNrm}^{\EmpLbl}_{t+1} \approx {\cNrm}^{\EmpLbl}_{t}\left(1+ \urate \cGap _{t+1}\right) {\GPFachFix}`, which directly implies that the lower {math}`\cGap_{t+1}` will yield a lower {math}`\cNrmE_{t+1}`. That is, for any point to the right of the {math}`\Delta \cNrmE_{t+1}=0` locus, the growth rate of consumption will be lower than at the corresponding point on the locus. Since on the locus, growth was zero, this means that to the right of the locus, {math}`\cNrmE` is declining (hence the down arrow in the phase diagram). Reciprocally, for any point to the left of {math}`\Delta \cNrmE_{t+1}=0`, the Euler equation implies that consumption will rise.

#### The Consumption Function

{numref}`fig:TBS-cFunc` shows the optimal consumption function {math}`\cFunc(\mNrm)` for an employed consumer (dropping the {math}`\EmpLbl` superscript to reduce clutter). This is actually just the stable arm in the phase diagram. (Think about why). Also plotted are the 45 degree line along which {math}`\cNrm = \mNrm` as well as the function

```{math}
\bar{\cFunc}(\mNrm) = (\mNrm-1+\hNrm)\MPC
```

where

```{math}
\hNrm = \left(\frac{1}{1-\WGroFac/\Rfree}\right)
```

is the level of (normalized) human wealth. {math}`\bar{\cFunc}(\mNrm)` is the solution to a perfect foresight problem in which income grows by the factor {math}`\WGroFac`; it is depicted in order to introduce a final fact: As wealth approaches infinity, the solution to the problem with uncertain labor income approaches arbitrarily close to the perfect foresight solution, as the [appendix on the consumption function as wealth grows large](#sec:TBS-PGroGEQRfree) shows.

:::{margin}
This limiting result requires that we impose the {math}`\FHWCWGro` ({math}`\WGroFac < \Rfree`), because the perfect foresight consumption function is not defined if {math}`\WGroFac \geq \Rfree`. Informally, the proof is as follows. Define {math}`\underline{\cFunc}(\mNrm) \equiv \MPC\mNrm=\cFunc^{\UnempLbl}(\mNrm)` as the consumption function for the unemployed consumer who will receive no future labor income. Then {math}`\underline{\cFunc}(\mNrm) < \cFunc(\mNrm) \leq \bar{\cFunc}(\mNrm)`, and so {math}`1 < \cFunc(\mNrm)/\underline{\cFunc}(\mNrm)<\bar{\cFunc}(\mNrm)/\underline{\cFunc}(\mNrm)`. In the limit as {math}`\mNrm \uparrow \infty`, however, human wealth accounts for an arbitrarily small proportion {math}`\MPC \hNrm/\MPC (\hNrm+\mNrm-1)` of consumption, so {math}`\lim_{\mNrm \uparrow \infty} \cFunc^{\EmpLbl}(\mNrm)/\cFunc^{\UnempLbl}(\mNrm) = 1` so the precautionary motive captured by {math}`\cGap` vanishes.
:::

:::{figure} figures/cFunc.png
:name: fig:TBS-cFunc
:class: note-under

The Consumption Function

Note: The consumption function lies below the 45 degree line and below the perfect foresight consumption function {math}`\bar{\cFunc}`, which it approaches as {math}`\mNrmE` grows.
:::

Note that {math}`\cFunc(\mNrm)` is *concave*. That is, the marginal propensity to consume {math}`\MPCFunc(\mNrm) \equiv d \cFunc(\mNrm)/d \mNrm` is higher at low levels of {math}`\mNrm`. This is because of the increase in the intensity of the precautionary motive as resources {math}`\mNrm` decline; the consequences of becoming unemployed with little wealth are very painful. The MPC is high at low levels of {math}`\mNrm` because at low levels of {math}`\mNrm` the *relaxation* in the intensity of the precautionary motive with each extra bit of {math}`\mNrm` is quite large {cite:p}`kimball:smallandlarge`. This diminution in the precautionary motive translates into an increase in consumption; for {math}`\mNrm`-poor consumers even a modest increase in {math}`\mNrm` can give a substantial boost to {math}`\cNrm`.

:::{margin}
{cite:t}`carroll&kimball:concavity` prove that the consumption function must be concave for almost all commonly-used assumptions about risk and utility functions.
:::

This point is clearest as {math}`\mNrm` approaches zero. Note that the consumption function always remains below the 45 degree line. This is because if the consumer were to spend all of their resources in period {math}`t`, {math}`\cNrm_{t}=\mNrm_{t}`, then on becoming unemployed next period they would have {math}`\mNrmU_{t+1}=(\mNrm_{t}-\cNrm_{t})\RNrmByG=0` which would induce {math}`\cNrmU_{t+1}= \MPC \mNrmU_{t+1}=0`, yielding negative infinite utility. Thus the consumer will never spend all of their resources, and will always leave at least a little bit for next period in case of disaster (unemployment).

:::{margin}
This is an implication not just of the CRRA utility function used here but of the general class of continuously differentiable utility functions that satisfy the usual *Inada condition* {math}`\uFunc^{\prime}(0) = \infty`.
:::

#### Consumption Growth for a Consumer Who Stays Employed Is Downward Sloping in {math}`\mNrmE`

{numref}`fig:TBS-GrowthA` ("the growth diagram") illustrates some of the same points in a different way. It depicts the growth rate of consumption as a function of {math}`\mNrmE_{t}`. Since {math}`\urate \geq 0`, the {math}`\GICWGro` implies:

```{math}
\WGroRtehFix > \CRRA^{-1}(\rfree-\discRte) ,
```

a condition that can be visually verified for our benchmark calibration in {numref}`fig:TBS-GrowthA`. Now multiply both sides of {eq}`eq:TBS-BeforePFStep` by {math}`\WGroFachFix`, obtaining

```{math}
:label: eq:TBS-cLevGro

\begin{aligned}
        \left(\frac{\cLvl^{\EmpLbl}_{t+1}}{\cLvl^{\EmpLbl}_{t}}\right) & =  (\Rfree\DiscFac)^{1/\CRRA} \left\{1+\urate\left[\left(\frac{{\cNrm}^{\EmpLbl}_{t+1}}{\cNrmU_{t+1}}\right)^{\CRRA}-1\right]\right\}^{1/\CRRA}
\\       \Delta \log \cLvl^{\EmpLbl}_{t+1} & \approx  \CRRA^{-1}(\rfree-\discRte) +  \urate \cGap _{t+1},
\end{aligned}
```

where the last line uses the same (dubious) approximations used to obtain {eq}`eq:TBS-cedelapprox`.

:::{margin}
We have also assumed that {math}`(\cGap _{t+1})^{2}` is "small."
:::

Thus consumption growth is equal to what it would be in the absence of uncertainty, plus a precautionary term. Furthermore, the precautionary contribution will become arbitrarily large as {math}`\mNrm_{t} \downarrow 0` because {math}`\cNrmU_{t+1} = \mNrmU_{t+1}\MPC = (\mNrm_{t}-\cFunc(\mNrm_{t}))\RNrmByG\MPC` approaches zero as {math}`\mNrm_{t} \downarrow 0`. Sure enough, {numref}`fig:TBS-GrowthA` shows that as {math}`\mNrmE_{t}` gets low, the growth of consumption for a consumer who stays employed gets very large.

:::{figure} figures/GrowthA.png
:name: fig:TBS-GrowthA
:class: note-under

Income and Consumption Growth

Note: The growth of consumption for a consumer who stays employed falls as {math}`\mNrmE` rises and equals income growth {math}`\WGroRtehFix` at the target; its excess over the perfect foresight rate is the precautionary increment.
:::

Next, note that the point where the consumption growth locus meets the income growth line is labeled {math}`\mTrgNrm`. This is because the place where consumption growth is equal to income growth is at the target value of {math}`\mNrmE`.

#### Summing Up the Intuition

We are finally in position to get an intuitive understanding of how the model works, and why there is a target wealth ratio. On the one hand, consumers are growth-impatient. This prevents their wealth-to-income ratio from heading off to infinity. On the other hand, consumers have a precautionary motive that intensifies more and more as the level of wealth gets lower and lower. At some point the precautionary motive gets strong enough to counterbalance impatience. The point where impatience matches prudence defines the target wealth-to-income ratio.

#### Comparative Statics

Now consider the results of increasing the interest rate to {math}`\grave{\rfree}>\rfree`, depicted in {numref}`fig:TBS-GrowthB`. Obviously the perfect foresight consumption growth locus will shift up, to {math}`\CRRA^{-1}(\grave{\rfree}-\discRte)`, inducing a corresponding increase in the consumption growth locus for a consumer who stays employed. But we have not changed the expected growth rate of income. It is clear from the figure, therefore, that the new target level of cash-on-hand {math}`\grave{\mTrgNrm}^{\EmpLbl}` will be greater than the original target. That is, an increase in the interest rate increases the target level of wealth, as would be expected on intuitive grounds: in the benchmark calibration, raising {math}`\rfree` by 0.04 raises {math}`\mTrgNrm^{\EmpLbl}` from 5.48 to 6.89.

:::{figure} figures/GrowthB.png
:name: fig:TBS-GrowthB
:class: note-under

Effect of An Increase In {math}`\rfree`

Note: A higher interest rate raises the perfect foresight growth rate and shifts the consumption growth curve up, so the target rises.
:::

The next exercise, shown in {numref}`fig:TBS-cGroIncreaseMhoPlot`, is an increase in the risk of unemployment {math}`\urate`. The principal effect we are interested in is the upward shift in the consumption growth locus (for a consumer who stays employed) to {math}`\Delta \grave{\cLvl}_{t+1}`. If the household starts at the original target level of resources {math}`\mTrgNrm`, the size of the upward shift at that point is captured by the arrow originating at {math}`\{\mTrgNrm,\WGroRtehFix\}`.

In the absence of other consequences of the rise in {math}`\urate`, the effect on the target level of {math}`\mNrm` would be unambiguously positive. However, recall our adjustment to the growth rate conditional upon employment, {eq}`eq:TBS-meanPreserve`; this induces the shift in the income growth locus to {math}`\grave{\WGroRtehFix}` which has an offsetting effect on the target {math}`\mNrm` ratio. Under our benchmark parameter values, the target value of {math}`\mNrm` is higher than before the increase in risk even after accounting for the effect of higher {math}`\WGroRtehFix` (tripling {math}`\urate` raises {math}`\mTrgNrm^{\EmpLbl}` from 5.48 to 7.50), but in principle it is possible for the {math}`\WGroRtehFix` effect to dominate the direct effect. Note, however, that even if the target value of {math}`\mNrm` is lower, it is possible that the *saving rate* will be higher; this is possible because the faster rate of {math}`\WGroRtehFix` makes a given saving rate translate into a lower ratio of wealth to income. In any case, the most useful calibrations of the model are those for which an increase in uncertainty results in either an increase in the saving rate or an increase in the target ratio of resources to permanent income. This is partly because our intent is to use the model to illustrate the general features of precautionary behavior, including the qualitative effects of an increase in the magnitude of transitory shocks, which a prudent consumer meets with more precautionary saving {cite:p}`kimball:smallandlarge`.

:::{figure} figures/cGroIncreaseMhoPlot.png
:name: fig:TBS-cGroIncreaseMhoPlot
:class: note-under

Effect of an Increase in {math}`\urate`

Note: Higher unemployment risk shifts the consumption growth curve up and raises income growth {math}`\WGroRtehFix` for consumers who stay employed; at the benchmark calibration the target rises.
:::

#### Death to the Log-Linearized Consumption Euler Equation!

{numref}`fig:TBS-GrowthA` and {numref}`fig:TBS-GrowthB` show that, so long as consumers are impatient, the steady state growth rate of consumption will be equal to the steady-state growth rate of income,

```{math}
:label: eq:TBS-ceqg

\Delta \log \cLvl^{\EmpLbl}_{t+1} = \WGroRtehFix.
```

Yet the approximate Euler equation for consumption growth, {eq}`eq:TBS-cLevGro`, does not contain any term explicitly involving income growth; in the logarithmic utility case, for example, the expression is

```{math}
:label: eq:TBS-cdelapprox2

\Delta \log \cLvl^{\EmpLbl}_{t+1} \approx \CRRA^{-1}(\rfree-\discRte) + \urate \cGap _{t+1}.
```

How can we reconcile these two expressions for consumption growth? Only by realizing that the size of the precautionary term {math}`\urate \cGap_{t+1}` is *endogenous*: It depends on {math}`\WGroRtehFix`. Indeed, we can solve {eq}`eq:TBS-ceqg` and {eq}`eq:TBS-cdelapprox2` to determine that in steady-state we must have

```{math}
:label: eq:TBS-prectermSS

\urate \TargetNrm{\cGap} \approx \WGroRtehFix - \CRRA^{-1}(\rfree-\discRte).
```

We can use this equation to understand the relationship between parameters and steady-state levels of wealth, by noting that {math}`\cGap_{t+1}(\mNrmE_{t})` is a downward-sloping function of {math}`\mNrmE_{t}` (see {numref}`fig:TBS-GrowthA` again). This is because at low levels of current wealth, much of the spending of employed consumers is financed by their current income. If they lose that income, they will have no choice but to cut consumption drastically; this is reflected in a large value of {math}`\cGap_{t+1}`.

For example, an increase in the growth rate of income implies that the right-hand side of equation {eq}`eq:TBS-prectermSS` increases. The new target level of {math}`\mTrgNrm` must be lower, because lower wealth induces greater consumption risk and a corresponding increase in the left-hand side of {eq}`eq:TBS-prectermSS`. This is how the human wealth effect works in this framework: Consumers who anticipate faster income growth will hold less market wealth.

The fact that consumption growth equals income growth in the steady-state poses major problems for empirical attempts to estimate the Euler equation. To see why, suppose we had a collection of countries indexed by {math}`i`, identical in all respects except that they have different interest rates {math}`\rfree_{i}`. Then in the spirit of {cite:t}`hallSubstitution`, one might be tempted to estimate an equation:

```{math}
\Delta \log \cLvl_{i} = \eta_{0} + \eta_{1} \rfree_{i}+\epsilon_{i},
```

and to interpret the coefficient estimate on {math}`\rfree_{i}` as an indication of the value of {math}`\CRRA^{-1}`.

But suppose that all of these countries contained impatient consumers and were in their steady-states where {math}`\Delta \log \cLvl_{i} = \WGroRtehFix_{i}`. Suppose further that all countries had *the same* steady-state income growth rate and unemployment rate. Then the regression equation would return the estimates

:::{margin}
The key point holds even if countries have different growth rates, but is easiest to understand if growth rates are identical.
:::

```{math}
\begin{aligned}
        \eta_{0} & =  \WGroRtehFix  \\
        \eta_{1} & =  0.
\end{aligned}
```

The econometric problem here is that there is an *omitted variable* from the regression specification, the {math}`\urate \cGap` term, which is (perfectly) correlated with the included variable {math}`\rfree_{i}`. Thus, Euler equation estimation cannot be expected to return an unbiased estimate of {math}`\CRRA^{-1}`. For much more on this problem, see {cite:t}`carroll:death`. For empirical evidence that the problem is important in macroeconomic practice, see {cite:t}`ParkerPrestonPrecaution`.

(sec:TBS-FinalExperiment)=
#### A Final Experiment

We now consider a final experiment: A decrease in the time preference rate. To reduce clutter, we drop the {math}`\Delta \cNrmE_{t+1}=0` locus from the phase diagram from {numref}`fig:TBS-PhaseDiag`, and everywhere drop the {math}`\EmpLbl` superscripts.

{numref}`fig:TBS-DecreaseTheta` depicts the effect on the employed consumer's spending by showing each successive point in time as a dot. Starting at time 0 from the steady-state level of consumption, the decrease in the future discounting rate (an increase in patience) causes an instantaneous drop in the level of consumption. Starting from this diminished base, consumption growth is subsequently faster than before the drop in {math}`\discRte`.

:::{margin}
We could also analyze the effects on growth, but the results would be essentially the same as in {numref}`fig:TBS-GrowthB`, which analyzes the effect of an increase in the interest rate.
:::

:::{figure} figures/DecreaseTheta.png
:name: fig:TBS-DecreaseTheta
:class: note-under

Effect of Lower {math}`\discRte` On Consumption Function

Note: The new consumption function lies below the original; from the original target, consumption drops, and the consumer then moves along the new function to the higher new target.
:::

Eventually consumption approaches its new, higher equilibrium ratio to permanent income at a new, higher level of equilibrium {math}`\mNrmE` (in the benchmark calibration, lowering {math}`\discRte` from 0.10 to 0.08 raises {math}`\mTrgNrm^{\EmpLbl}` from 5.48 to 7.19 and {math}`\cTrgNrm^{\EmpLbl}` from 1.11 to 1.15). This higher level of consumption is financed in the long run by the higher interest income earned on the higher level of wealth.

Note again, however, that equilibrium steady-state consumption growth is still equal to the growth rate of income (this follows from the fact that there is a steady-state *level* for the *ratio* of consumption to income, {math}`\cNrm`). This means that the higher level of wealth in equilibrium ends up being precisely enough to reduce the precautionary term by an amount that exactly offsets the fact that the {math}`-\CRRA^{-1}\discRte` term in the Euler equation is now smaller in absolute value.

{numref}`fig:TBS-cPathAfterThetaDrop`, {numref}`fig:TBS-mPathAfterThetaDrop` and {numref}`fig:TBS-MPCPathAfterThetaDrop` depict the time paths of consumption, market wealth, and the marginal propensity to consume {math}`\MPCFunc(\mNrm)` following the decline in {math}`\discRte`. These are implicit in the phase diagram analysis, but the dots in these three diagrams are spread out evenly over time to give a sense of the time scale over which the model adjusts toward the steady state.

:::{figure} figures/cPathAfterThetaDrop.png
:name: fig:TBS-cPathAfterThetaDrop
:class: note-under

Path of {math}`{\cNrm}^{\EmpLbl}` Before and After {math}`\discRte` Decline

Note: Consumption drops when {math}`\discRte` falls, then rises to a higher steady-state ratio.
:::

:::{figure} figures/mPathAfterThetaDrop.png
:name: fig:TBS-mPathAfterThetaDrop
:class: note-under

Path of {math}`\mNrmE` Before and After {math}`\discRte` Decline

Note: Market resources rise gradually to the higher new target.
:::

:::{figure} figures/MPCPathAfterThetaDrop.png
:name: fig:TBS-MPCPathAfterThetaDrop
:class: note-under

Marginal Propensity to Consume {math}`\MPCFunc(\mNrm_{t})` Before and After {math}`\discRte` Decline

Note: The MPC drops when {math}`\discRte` falls and keeps falling as wealth accumulates, staying above the perfect foresight MPC {math}`\MPC`.
:::

## A Macroeconomic Interpretation

Loosely following {cite:t}`cjSOE`, the model can be read as a small open economy of overlapping generations, in which newly unemployed households leave the country and each generation is larger than the one before by the factor {math}`\PopnGroFac`. If a wage tax finances a "stake" that gives each newborn the target ratio of bank balances, every employed household in the steady state is at the same ratios, so a representative employed consumer describes the economy. After a rise in patience, aggregate consumption then responds much as the individual's does ({numref}`fig:TBS-SOEStakescPathAfterThetaDropPlot`), apart from a small effect of the higher tax that finances the larger stakes. Without stakes, aggregate consumption has to be simulated. [A Macroeconomic Interpretation of the Tractable Buffer Stock Model](#sec:TractableBufferStockMacro) works out both cases.

:::{figure} figures/SOEStakescPathAfterThetaDropPlot.png
:name: fig:TBS-SOEStakescPathAfterThetaDropPlot
:class: note-under

Aggregate {math}`\CNrm` in a Small Open Economy Before and After {math}`\discRte` Decline

Note: With stakes, aggregate consumption behaves like an individual's: it drops, then rises to a higher ratio.
:::

(sec:TractableBufferStock-AppendixResults)=
## Results in the Appendix

The [appendix](#sec:TractableBufferStock-Appendix) derives nine further results, which are stated here without their derivations. The [notebook](TractableBufferStock.ipynb) uses those on the MPC to solve the model.

- *[Approximate consumption growth](#sec:TBS-CGroApprox).* Taylor approximations turn the employed consumer's Euler equation into {math}`{\cNrm}^{\EmpLbl}_{t+1}/{\cNrm}^{\EmpLbl}_{t} \approx \GPFachFix\left(1+\urate(1+\prudEx\cGap_{t+1})\cGap_{t+1}\right)`, the approximation this chapter uses, where {math}`\prudEx = (\CRRA-1)/2`.
- *[A target exists if and only if the {math}`\GIChFix` holds](#sec:TBS-mTargExists).* Given the RIC, the employed consumer has a target {math}`\mTrgNrm^{\EmpLbl}` if and only if {math}`\GPFachFix < 1`, that is, {math}`\DiscFac < \WGroFachFix^{\CRRA}/\Rfree`. When the {math}`\FHWChFix` fails ({math}`\WGroFachFix \geq \Rfree`), the RIC implies the {math}`\GIChFix`, so a target always exists.
- *[The {math}`\dcEqZero` locus exists under a weaker condition](#sec:TractableBufferStock-cLocusExists).* Given the RIC, the {math}`\dcEqZero` locus exists, and slopes upward, if and only if the GIC-TBS, {math}`\GPFachFix(1-\urate)^{1/\CRRA} < 1`, holds, while for {math}`\CRRA > 1`, the employed consumer's consumption function exists whether or not the GIC-TBS holds. The GIC-TBS can hold even when the perfect foresight {math}`\GICWGro` fails. When the GIC-TBS holds but the {math}`\GIChFix` fails, there is no target, and the ratio of wealth to income grows forever.
- *[The exact target](#sec:TBS-mTargExact).* The target is {math}`\mTrgNrm^{\EmpLbl} = 1 + \Rfree/(\WGroFachFix+\Rfree\MPC\straight-\Rfree)`, whose denominator the RIC and the {math}`\GIChFix` make positive. As the unemployment risk vanishes, the target approaches 1 if the perfect foresight {math}`\GICWGro` holds, and a finite value above 1 if {math}`\APFac_{\WGroFac} = 1`.
- *[Approximate formulas for the target](#sec:TBS-mTargApprox).* Taylor approximations give simple formulas for the target, such as {math}`\mTrgNrm^{\EmpLbl} \approx 1 + 1/\left((\WGroRtehFix-\rfree)+\discRte(1+(\WGroRtehFix+\discRte-\rfree)/\urate)\right)` under logarithmic utility. Under logarithmic utility they are close; otherwise they are reliable only when the consumer is barely growth-impatient relative to the unemployment risk: rough when {math}`\discRte=\rfree`, and useless at the benchmark calibration.
- *[The MPC at the target and as {math}`\mNrm` approaches zero](#sec:TractableBufferStock-MPC).* The MPC at the target is the root in (0, 1) of a quadratic, which has a closed form. As {math}`\mNrm` approaches zero, the MPC approaches {math}`\MPC/(\MPC+\RPFac\urate^{1/\CRRA})`, which lies between the perfect foresight {math}`\MPC` and 1.
- *[The MPC's derivatives at the target](#sec:TractableBufferStock-MPCDerivatives).* Each derivative of the MPC at the target has an explicit formula in terms of the lower ones. With the [reverse-shooting equations](#sec:TractableBufferStock-ReverseShooting), these let the notebook trace the consumption function out from the target.
- *[The value function](#sec:TractableBufferStock-ValueFunction).* For {math}`\CRRA \neq 1`, the unemployed consumer's value is current utility times {math}`1/\MPC`, as in the perfect foresight model. The employed consumer's value at the target has a closed form, finite when {math}`\DiscFac\WGroFachFix^{1-\CRRA}(1-\urate) < 1`, which the RIC and the {math}`\GIChFix` imply when {math}`\CRRA \geq 1`.
- *[The consumption function as wealth grows large](#sec:TBS-PGroGEQRfree).* When human wealth is finite ({math}`\WGroFac < \Rfree`), the consumption function approaches the perfect foresight function {math}`\MPC(\mNrm-1+\hNrm)` as {math}`\mNrm` grows, even when the {math}`\FHWChFix` fails. When {math}`\WGroFac \geq \Rfree`, it approaches {math}`\MPC\mNrm` only in ratio.
