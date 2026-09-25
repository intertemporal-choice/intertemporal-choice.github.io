(sec:TractableBufferStock)=
# A Tractable Model of Buffer Stock Saving

A companion notebook in the Econ-ARK DemARK collection, [Tractable Buffer Stock (interactive)](https://econ-ark.org/materials/tractablebufferstock-interactive), lets you vary the model's parameters and watch the consumption function and target wealth respond. HARK solves the model as its [`TractableConsumerType`](https://github.com/econ-ark/HARK/blob/main/examples/TractableBufferStockModel/TractableConsumerType.ipynb), and this chapter's figures are drawn with that class by its [figure notebook](../notebooks/TractableBufferStock.md).

## Introduction

This chapter illustrates the logic of precautionary saving by assuming that individuals face only a single, simple kind of uncertainty: A small risk of becoming permanently unemployed. More realistic assumptions yield similar conclusions (after much more work).[^tbs-model-simplifies-many]

[^tbs-model-simplifies-many]: The model simplifies many of the key results in {cite:t}`carroll:brookings` and {cite:t}`BufferStockTheory` using a discrete-time version of the elegant continuous-time model of {cite:t}`toche:urisk`. For a brief summary of the precautionary saving literature, see {cite:t}`CarrollKimballPSPW`; for a more rigorous treatment of the theoretical issues, see {cite:t}`BufferStockTheory`.

## The Microeconomic Consumer's Problem

The aggregate wage {math}`\Wage_{t}` grows by a constant factor {math}`\WGro` every period, reflecting exogenous labor productivity improvements:

```{math}
\Wage_{t+1} = \WGro \Wage_{t}.
```

The consumer lives in a small open economy, so there is a constant interest factor {math}`\Rfree`. Defining {math}`\mLevBF` as **m**arket resources (net worth plus current income), {math}`\aLevBF` as end-of-period **a**ssets **a**fter **a**ll **a**ctions **a**re **a**ccomplished (specifically, after the consumption decision), and {math}`\bLevBF` as **b**ank **b**alances **b**efore receipt of labor income, the dynamic budget constraint (DBC) can be decomposed into the following elements:

```{math}
:label: eq:TBS-DBC

\begin{aligned}
    \aLevBF_{t} & =  \mLevBF_{t}-\cLevBF_{t}
\\  \bLevBF_{t+1} & =  \Rfree \aLevBF_{t}
\\  \mLevBF_{t+1} & =  \bLevBF_{t+1}+\labor_{t+1}\Wage_{t+1}\empState_{t+1}
\end{aligned}
```

where {math}`\labor` measures the consumer's labor productivity ("endowment") and {math}`\empState` is a dummy variable indicating the consumer's employment state: Everyone is either employed (state "e"), in which case {math}`\empState = 1`, or unemployed (state "u"), in which case {math}`\empState=0`, so that for unemployed individuals labor income is zero.[^tbs-could-allow-unemployment]

[^tbs-could-allow-unemployment]: We could allow for unemployment insurance by modifying the values of {math}`\empState` associated with the two states. The key conclusions would not change.

(sec:TBS-Fred)=
### The Unemployed Consumer's Problem

Once a person becomes unemployed, that person can never become employed again (i.e. if {math}`\empState_{t}=0` then {math}`\empState_{t+1}=0`). Consumers have a CRRA felicity function[^tbs-felicity-refers-explicitly] {math}`\uFunc(\bullet)= \bullet^{1-\CRRA}/(1-\CRRA)`, and discount future felicity geometrically by {math}`\Discount` per period.

[^tbs-felicity-refers-explicitly]: "Felicity" refers explicitly to a one-period, or in a continuous-time model, an instantaneous utility function.

The solution to the unemployed consumer's optimization problem is[^tbs-perfforesightcrra-derivation-noting]

[^tbs-perfforesightcrra-derivation-noting]: See the [perfect foresight CRRA](#sec:PerfForesightCRRA) section for a derivation, noting that human wealth is zero for the unemployed consumer.

```{math}
:label: eq:TBS-cpfinfhorunemp

\cLevBF^{u}_{t} = \underbrace{\left(1-\overbrace{\Rfree ^{-1}(\Rfree{\Discount})^{1/\CRRA}}^{\equiv \PatR}\right)}_{\equiv \MPC} \bLevBF_{t} ,
```

where the {math}`u` superscript signifies the consumer's (un)employment status; {math}`\MPC` is the marginal propensity to consume for the perfect foresight consumer, which is strictly below the MPC for the problem with uncertainty ({cite:p}`carroll&kimball:concavity`); and {math}`\PatR` is what {cite:t}`BufferStockTheory` calls the "return patience factor."[^tbs-old-english-letter]

[^tbs-old-english-letter]: The Old English letter {math}`\Pat = (\Rfree \Discount)^{1/\CRRA}`, which conveniently looks something like a combination of {math}`\Rfree, \Discount,` and {math}`\CRRA`, is used to designate the "absolute patience factor" which determines whether consumption will rise ({math}`\Pat > 1`), stay the same ({math}`\Pat = 1`), or fall ({math}`\Pat < 1`) in the perfect foresight problem (see the [perfect foresight CRRA](#sec:PerfForesightCRRA) section). Terms like this are all defined in {cite:t}`BufferStockTheory` and citations to that paper will henceforth be omitted when new terms are introduced, on the understanding that the reader knows to see {cite:t}`BufferStockTheory` for further definition and discussion.

We now impose the "return impatience condition" (RIC),

```{math}
:label: eq:TBS-RIC

\underbrace{\left(\frac{(\Rfree \Discount)^{1/\CRRA}}{\Rfree}\right)}_{= \PatR} < 1
```

which deserves its name because it is the condition that guarantees that {math}`\MPC > 0`: the consumer must not be *so* patient that, given the interest rate, a boost to resources fails to boost spending.[^tbs-pathologically-patient-consumers] An alternative (equally correct) interpretation is that the condition guarantees that the PDV of consumption for the unemployed consumer is not infinity.[^tbs-perfect-foresight-consumer]

[^tbs-pathologically-patient-consumers]: "Pathologically patient" consumers who do not satisfy this condition can be thought of as people who would hoard any incremental resources in order to enable even more extra spending in the distant future.

[^tbs-perfect-foresight-consumer]: For a perfect foresight consumer, the [perfect foresight CRRA](#sec:PerfForesightCRRA) section shows that consumption grows by the factor {math}`\Pat = (\Rfree\Discount)^{1/\CRRA}`, so if we do not impose the RIC, consumption would "want" to grow by a factor greater than the factor {math}`\Rfree` by which it is being discounted.

For many purposes (not least, the calibration of the model), it turns out to be useful to alternatively express impatience conditions like {eq}`eq:TBS-RIC` in terms of the upper bound of the range of time preference factors {math}`\bar{\Discount}` that satisfy the condition; solving {eq}`eq:TBS-RIC` for {math}`\Discount`, we designate this object

```{math}
\DiscountMaxRIC = \Rfree^{\CRRA-1}
```

and write the alternative version of the constraint as

```{math}
:label: eq:TBS-DiscountMaxRIC

\Discount < \DiscountMaxRIC .
```

{math}`\PatR` is the "return patience factor" because it defines the patience factor {math}`\Pat` relative to the return factor {math}`\Rfree`; correspondingly, we define the "return patience rate" as lower-case

```{math}
:label: eq:TBS-patr

\begin{aligned}
   \patr & \equiv   \log \PatR
\\ & \approx \PatR - 1
\\ & =  -\MPC
\end{aligned}
```

and we say that a consumer is "return impatient" if the RIC {eq}`eq:TBS-RIC` holds (equivalent conditions are {math}`\patr < 0` and {math}`\MPC > 0`).[^tbs-throughout-will-casually]

[^tbs-throughout-will-casually]: Throughout, we will casually treat logs of factors like {math}`\PatR` as equivalent to the level minus 1; that is, we will treat expressions like those in {eq}`eq:TBS-patr` as interchangeable, which is an appropriate approximation so long as the factor is "close" to 1.

### The Employed Consumer's Problem

(sec:TBS-uMPS)=
#### Unemployment Risk as a Mean Preserving Spread in Human Wealth

If a person who is employed in period {math}`t` ({math}`\empState_{t}=1`) is still employed next period ({math}`\empState_{t+1}=1`), market resources will be

```{math}
:label: eq:TBS-MLevtp1

\mLevBF^{e}_{t+1} = (\mLevBF^{e}_{t}-\cLevBF^{e}_{t})\Rfree+\Wage_{t+1}\labor_{t+1}.
```

But employed consumers face a constant risk {math}`\urate` of becoming unemployed. It will be convenient to define {math}`\erate\equiv 1-\urate` as the probability that a consumer does *not* become unemployed. Whether the consumer is employed or not, the consumer's labor productivity {math}`\labor` is well-defined:[^tbs-labor-productivity-purely] For convenience, {math}`\labor` is assumed to grow by a factor {math}`\erate^{-1}` every period,

[^tbs-labor-productivity-purely]: "Labor productivity" is purely hypothetical for a consumer who is unemployed; but defining it even for unemployed consumers simplifies notation and some later analysis.

```{math}
:label: eq:TBS-meanPreserve

\labor_{t+1} =    \labor_{t}/\erate ,
```

which means that for a consumer who remains employed, labor income will grow by factor

```{math}
\PGro = \WGro/\erate
```

so that the *expected* labor income growth factor for employed consumers is the same {math}`\WGro` as in the perfect foresight case:

```{math}
\begin{aligned}
  \Ex_{t}[\Wage_{t+1}\labor_{t+1}\empState_{t+1}] & =   \left(\frac{\labor_{t} \WGro \Wage_{t}}{\erate}\right)\left(\urate \times 0 + \erate \times 1 \right)
\\ \left(\frac{\Ex_{t}[\Wage_{t+1}\labor_{t+1}\empState_{t+1}]}{\Wage_{t} \labor_{t}}\right) &  =  \WGro
,
\end{aligned}
```

which is the reason for {eq}`eq:TBS-meanPreserve`'s assumption about the growth of individual labor productivity: It implies that an increase in {math}`\urate` is a pure increase in uncertainty with no effect on the PDV of expected labor income ("human wealth"); an increase in {math}`\urate` therefore constitutes a "mean-preserving spread" in human wealth.

#### First Order Optimality Condition

The same solution methods used in the [perfect foresight CRRA](#sec:PerfForesightCRRA) section can be applied here too (take the first order condition with respect to {math}`\cLev`, use the [Envelope theorem](#sec:Envelope)); the only difference is the need to keep the expectations operator in place. Using {math}`\bullet` as a placeholder for "e" or "u," the usual steps lead to the standard consumption Euler equation:

```{math}
:label: eq:TBS-ctp1Oct

\begin{aligned}
        \uFunc^{\prime}(\cLevBF^{e}_{t}) & =  \Rfree\Discount \Ex_{t}\left[\uFunc^{\prime}(\cLevBF^{\bullet}_{t+1}) \right]
\\  1         & =  \Rfree\Discount \Ex_{t}\left[\left(\frac{\cLevBF^{\bullet}_{t+1}}{\cLevBF^{e}_{t}}\right)^{-\CRRA} \right]
.
\end{aligned}
```

Defining nonbold variables as the bold equivalent divided by the level of permanent labor income for an employed consumer, e.g. {math}`{\cRat}^{e}_{t}=\cLevBF^{e}_{t}/(\Wage_{t}\labor_{t})`, we can rewrite the consumption Euler equation as

```{math}
:label: eq:TBS-Explicit

\begin{aligned}
  1         & =  \Rfree\Discount \Ex_{t}\left[\left(\frac{{c}^{\bullet}_{t+1} \Wage_{t+1}\labor_{t+1}}{{\cRat}^{e}_{t} \Wage_{t}\labor_{t}}\right)^{-\CRRA} \right]
\\          & =  \Rfree\Discount \Ex_{t}\left[\left(\frac{{c}^{\bullet}_{t+1}}{{\cRat}^{e}_{t}}\PGro\right)^{-\CRRA} \right]
\\          & =  \PGro^{-\CRRA}\Rfree\Discount \Ex_{t}\left[\left(\frac{{c}^{\bullet}_{t+1}}{{\cRat}^{e}_{t}}\right)^{-\CRRA} \right]
\\          & =  \PGro^{-\CRRA}\Rfree\Discount \left\{(1-\urate)\left(\frac{{\cRat}^{e}_{t+1}}{{\cRat}^{e}_{t}}\right)^{-\CRRA}+\urate \left(\frac{\cU_{t+1}}{{\cRat}^{e}_{t}}\right)^{-\CRRA}\right\}
\end{aligned}
```

#### Analysis and Intuition of Consumption Growth

It will be useful now to define a "growth patience factor" (terminology justified below):

```{math}
:label: eq:TBS-GPFacRaw

\PatPGro = \left(\frac{(\Rfree\Discount)^{1/\CRRA}}{\PGro}\right),
```

which is the factor by which {math}`{\cRat}^{e}` would grow in the perfect foresight version of the model with permanent income growth factor {math}`\PGro` (again see the [perfect foresight CRRA](#sec:PerfForesightCRRA) section). Using this, {eq}`eq:TBS-Explicit` can be written as

```{math}
:label: eq:TBS-BeforePFStep

\begin{aligned}
        1  & = \PatPGro^{\CRRA} \left(\frac{{\cRat}^{e}_{t+1}}{{\cRat}^{e}_{t}}\right)^{-\CRRA} \left\{(1-\urate)+\urate\left[\left(\frac{\cU_{t+1}}{{\cRat}^{e}_{t}}\right)\left(\frac{{\cRat}^{e}_{t}}{{\cRat}^{e}_{t+1}}\right)\right]^{-\CRRA}\right\}
\\       & = \PatPGro^{\CRRA} \left(\frac{{\cRat}^{e}_{t+1}}{{\cRat}^{e}_{t}}\right)^{-\CRRA} \left\{1+\urate\left[\left(\frac{\cU_{t+1}}{{\cRat}^{e}_{t+1}}\right)^{-\CRRA}-1\right]\right\}
\\       \left(\frac{{\cRat}^{e}_{t+1}}{{\cRat}^{e}_{t}}\right)^{\CRRA} & = \PatPGro^{\CRRA} \left\{1+\urate\left[\left(\frac{{\cRat}^{e}_{t+1}}{\cU_{t+1}}\right)^{\CRRA}-1\right]\right\}
\\       \left(\frac{{\cRat}^{e}_{t+1}}{{\cRat}^{e}_{t}}\right) & = {\PatPGro} \left\{1+\urate\left[\left(\frac{{\cRat}^{e}_{t+1}}{\cU_{t+1}}\right)^{\CRRA}-1\right]\right\}^{1/\CRRA}.
\end{aligned}
```

(This is where the perfect foresight assumption is important; without it {eq}`eq:TBS-BeforePFStep` would be

```{math}
:label: eq:TBS-BeforePFStepWithEx

1 = \PatPGro^{\CRRA} \Ex_{t}\left[\left(\frac{{\cRat}^{e}_{t+1}}{{\cRat}^{e}_{t}}\right)^{-\CRRA} \left\{1+\urate\left[\left(\frac{\cU_{t+1}}{{\cRat}^{e}_{t+1}}\right)^{-\CRRA}-1\right]\right\}\right]
```

and we would be unable to proceed.)

Now define {math}`\nabla _{t+1} \equiv \left(\frac{{\cRat}^{e}_{t+1}-\cU_{t+1}}{\cU_{t+1}}\right)` (which is the proportion by which consumption would be greater next period for an employed than for an unemployed person),[^tbs-nabla-mnemonic] and define an "excess prudence" factor

[^tbs-nabla-mnemonic]: Mnemonic: {math}`\nabla` is like {math}`\Delta`, a change, but it points down, because it measures the fall in consumption if unemployment strikes.

```{math}
\prudEx = \left(\frac{\CRRA-1}{2}\right).
```

The [appendix on approximate consumption growth](#sec:TBS-CGroApprox) shows that, with some approximations, we can rewrite {eq}`eq:TBS-ctp1Oct` as

```{math}
:label: eq:TBS-cedelapprox

\left(\frac{{\cRat}^{e}_{t+1}}{{\cRat}^{e}_{t}}\right) \approx \left(1+ \urate (1+\prudEx\nabla _{t+1})\nabla _{t+1}\right) {\PatPGro}
```

which can be simplified in the logarithmic utility case (where {math}`\prudEx = 0`) to

```{math}
:label: eq:TBS-cedelapproxLog

\left(\frac{{\cRat}^{e}_{t+1}}{{\cRat}^{e}_{t}}\right) \approx \left(1+ \urate \nabla _{t+1}\right) {\PatPGro} .
```

Now since consumption if employed {math}`{\cRat}^{e}_{t+1}` is surely greater than consumption if unemployed {math}`\cU_{t+1}`, {math}`\nabla _{t+1}` is certainly a positive number. But since {math}`{\PatPGro}` is the value that {math}`{\cRat}^{e}_{t+1}/{\cRat}^{e}_{t}` would exhibit in a perfect foresight model, this equation tells us that uncertainty boosts consumption growth;[^tbs-least-continuing-employed] in the logarithmic case, consumption growth is augmented by an amount proportional to the probability of becoming unemployed {math}`\urate` multiplied by the size of the "consumption risk" (the amount by which consumption would fall if unemployment occurs).

[^tbs-least-continuing-employed]: At least, for continuing-employed consumers.

We noted above that for any given {math}`\mRatE_{t}`, an increase in uncertainty constitutes a mean-preserving spread in human wealth; thus the "human wealth effect" of an increase in {math}`\urate` would be zero for a consumer without a precautionary motive. In this small-open-economy model a change in {math}`\urate` also has no effect on the interest rate {math}`\rfree`, and so none of the conventional determinants of consumption in the perfect foresight model (the income, substitution, and human wealth effects) is affected by a change in uncertainty. The increase in consumption growth from an increase in {math}`\urate` in {eq}`eq:TBS-cedelapprox` or {eq}`eq:TBS-cedelapproxLog` therefore must be entirely the result of the precautionary motive. Furthermore, because a profile with faster consumption *growth* can only exhibit the *same PDV* if that faster growth *starts* from a lower initial consumption *level*, we know that for any given initial value of {math}`\mRatE`, the introduction of a risk of becoming unemployed {math}`\urate` induces a (precautionary) decline in consumption (and corresponding increase in saving).

Furthermore, under the (compelling) assumption that {math}`\CRRA > 1`, {eq}`eq:TBS-cedelapprox` implies that a consumer with a higher degree of prudence (larger {math}`\CRRA` and therefore larger {math}`\prudEx`) will anticipate a greater increment to consumption growth as a consequence of the introduction of uncertainty. This reflects the greater precautionary saving motive induced by a higher degree of prudence.

#### Finding the Target

The target level of {math}`\mRat^{e}` (if one exists) will be the point of intersection between the {math}`\dcEqZero` and {math}`\dmEqZero` loci. Here and below, a variable without a time subscript denotes its steady-state value.

The {math}`\dcEqZero` locus can be characterized by substituting {math}`{\cRat}^{e}_{t+1}={\cRat}^{e}_{t} \equiv {\cRat}^{e}`:

```{math}
:label: eq:TBS-straightDef

\begin{aligned}
         1 & = \left\{1+\urate\left[\left(\frac{{\cRat}^{e}_{t+1}}{\cRat_{t+1}^{u}}\right)^{\CRRA}-1\right]\right\} \PatPGro^{\CRRA}
\\ \PatPGro^{-\CRRA} & =  (1-\urate)+\urate\left(\frac{{\cRat}^{e}}{\cRat_{t+1}^{u} }\right)^{\CRRA}
\\ \underbrace{\left(\frac{\PatPGro^{-\CRRA}-1+\urate}{\urate}\right)^{1/\CRRA}}_{\equiv \straight} & =   \left(\frac{{\cRat}^{e}}{\cRatU_{t+1}}\right)
  \\ \underbrace{\left(\overbrace{\urate^{-1}(\PatPGro^{-\CRRA}-1)}^{\equiv \varpi}+1\right)^{1/\CRRA}}_{\straight=(1+\varpi)^{1/\CRRA}} & =   \left(\frac{{\cRat}^{e}}{\cRatU_{t+1}}\right)
\end{aligned}
```

which boils down to

```{math}
:label: eq:TBS-cRatEtfmcRatUtp1

{\cRat}^{e} = \cRat^{u}_{t+1} \straight .
```

The importance of the linearity of the consumption function of the unemployed consumer now becomes evident: It means that the RHS of {eq}`eq:TBS-cRatEtfmcRatUtp1` is linear in {math}`\cRat^{e}_{t}`:

```{math}
:label: eq:TBS-PSTerm

\cRat^{e}_{t} = \overbrace{(\mRat^{e}_{t}-{\cRat}^{e}_{t})\Rnorm \MPC}^{\cRat^{u}_{t+1}} \straight .
```

We know that {math}`\mRatE_{t}-{\cRat}^{e}_{t} > 0` because a consumer in these circumstances (facing possible perpetual unemployment) will never borrow (see below for a full discussion of this point). Since the RIC imposes {math}`\MPC>0`, {eq}`eq:TBS-PSTerm` tells us that steady-state consumption (if it exists)[^tbs-under-some-parameter] is a positive finite number so long as {math}`\straight > 0`. That holds if and only if the numerator on the LHS of {eq}`eq:TBS-straightDef` is a positive finite number, which requires

[^tbs-under-some-parameter]: Under some parameter values, the model has solutions under which the consumer always spends less than the amount that would leave {math}`\mRatE` constant, and so accumulates forever.

```{math}
:label: eq:TBS-GICExistsSoln

\begin{aligned}
        \PGro^{\CRRA}(\Rfree\Discount)^{-1}-(1-\urate) & >  0  \\
       \PGro^{\CRRA} & >  (\Rfree \Discount (1-\urate))
\\     1 & >  \left(\frac{(\Rfree \Discount (1-\urate))^{1/\CRRA}}{\PGro}\right) = \PatPGro (1-\urate)^{1/\CRRA}
.\end{aligned}
```

#### Upper Bounds for {math}`\Discount`, Given Other Parameters

As with the RIC, it may be useful to rewrite this as defining an upper bound to the permissible time preference rates:

```{math}
:label: eq:TBS-DiscountMaxGICTBS

\Discount < \DiscountMaxGICTBS = \left(\frac{\PGro^{\CRRA}}{\Rfree(1-\urate)}\right) .
```

In the limit as {math}`\urate` approaches zero, {eq}`eq:TBS-GICExistsSoln` reduces to a requirement that the growth patience factor is less than one,

```{math}
:label: eq:TBS-GICPGro

\PatPGro < 1 ,
```

which, as in the [perfect foresight CRRA](#sec:PerfForesightCRRA) section, we call a "growth impatience condition" (GIC) by analogy to the "return impatience condition" {eq}`eq:TBS-RIC` imposed earlier. The [perfect foresight CRRA](#sec:PerfForesightCRRA) section shows that the limit of {eq}`eq:TBS-GICExistsSoln` as {math}`\urate \downarrow 0`, {math}`\WGro > \Pat`, ensures that a consumer facing no uncertainty is sufficiently impatient that his wealth-to-permanent-income ratio will fall over time. We label the weaker condition {eq}`eq:TBS-GICExistsSoln` the "GIC-TBS" (the version of the GIC required for a solution to exist in the Tractable Buffer Stock model). It will always hold if the plain-vanilla {math}`\GICWGro` holds because {math}`\urate \geq 0`. Thus, a consumer who, in the absence of uncertainty, would satisfy both the RIC and the {math}`\GICWGro`, will have a positive finite target level of wealth when uncertainty is introduced.[^tbs-appendix-proof-condition]

[^tbs-appendix-proof-condition]: See the [appendix on conditions for a target](#sec:TBS-mTargExists) for a proof that the {math}`\GICPGro` condition is both necessary and sufficient for the existence of a target level of wealth.

When it is useful to distinguish the version of the GIC that applies in the model with income growth of {math}`\WGro` from the corresponding condition when growth is {math}`\PGro` we will label the two conditions {math}`\GICPGro` and {math}`\GICWGro`, and the corresponding bounds on {math}`\Discount` are

```{math}
\begin{aligned}
   \Discount < \DiscountMaxGICPGro & =  \Rfree^{\CRRA-1}\PGro^{\CRRA}
\\ \Discount < \DiscountMaxGICWGro & =  \Rfree^{\CRRA-1}\WGro^{\CRRA}
\end{aligned}
```

Using {math}`\pGro \equiv \log \PGro`, we similarly define the corresponding "growth impatience rate":

```{math}
\patpGro \equiv \log \PatPGro \approx \CRRA^{-1}(\rfree-\timeRate) - \pGro
```

so that the growth impatience condition {eq}`eq:TBS-GICExistsSoln` (the GIC-TBS) can also be written (approximately) as

```{math}
:label: eq:TBS-GICrateUsingpGro

\patpGro - \CRRA^{-1}\urate < 0
```

or, since {math}`\pGro \approx \wGro+\urate`,

```{math}
:label: eq:TBS-GICrateUsingwGro

\CRRA^{-1}(\rfree-\timeRate-\urate)-(\wGro+\urate) < 0 .
```

#### Why Increased Unemployment Risk Increases Effective Growth Impatience

Equation {eq}`eq:TBS-GICrateUsingwGro` becomes easier to satisfy (in the sense of requiring a lower {math}`\timeRate`) as {math}`\urate` increases, since in both places where {math}`\urate` appears on the LHS it is with a negative coefficient.

The reason the two appearances of {math}`\urate` have not been combined in {eq}`eq:TBS-GICrateUsingwGro` is that the separate terms reflect two logically distinct effects. The first appearance, where {math}`\urate` is premultiplied by {math}`-\CRRA^{-1}`, can be interpreted as capturing the sense in which an increase in {math}`\urate` is like an increase in the discounting of the future (the coefficient on {math}`\urate` is the same as that on {math}`\timeRate`). This downweighting of the future occurs precisely because that future might not occur (if the consumer becomes unemployed).[^tbs-different-future-consumer] The effect is much like the increase in discounting that occurs when a positive probability of death is introduced in consumption problems, cf. {cite:t}`blanchardFinite`.

[^tbs-different-future-consumer]: A different future (with the consumer unemployed) does occur; but here we are effectively analyzing the behavior of a consumer *contingent on that consumer remaining employed*.

The second, separate, reason {math}`\urate` weakens growth impatience (that is, the GIC-TBS holds in more circumstances than the {math}`\GICWGro`) is that we adjust labor productivity growth so that {math}`\pGro=\wGro+\urate` in order to maintain constant human wealth for different values of {math}`\urate` (eq. {eq}`eq:TBS-meanPreserve`). For higher {math}`\urate`, permanent income growth is greater *conditional on remaining employed*; the continuously-employed consumer is effectively more "impatient" in the relevant sense of desiring consumption growth slower than income growth.

This is essentially a mechanical result, which reflects our model's design for the purpose of examining thought experiments that manipulate the degree of uncertainty while leaving the perfect-foresight level of human wealth constant.

Note that although {math}`\urate` is our measure of uncertainty, neither of these effects of {math}`\urate` is in any meaningful sense directly a "precautionary" effect; instead, they both reflect effects of {math}`\urate` on the relevant degree of growth impatience in the GIC-TBS condition.

#### The Target Level of {math}`\mRatE`

The [appendix on conditions for a target](#sec:TBS-mTargExists) demonstrates that the RIC and the GIC-TBS are necessary conditions for the existence of a target value of market resources {math}`\mTarg^{e},` and that the {math}`\GICPGro` is sufficient. The [appendix on the exact target formula](#sec:TBS-mTargExact) solves for an explicit formula for that target.

Briefly, this is accomplished as follows. We can obtain the {math}`\dcEqZero` locus by substituting {math}`{\cRat}^{e}_{\tNow+1}={\cRat}^{e}_{\tNow}={\cRat}^{e}` into equation {eq}`eq:TBS-PSTerm`:

```{math}
:label: eq:TBS-cDelEqZero

\begin{aligned}
  {\cRat}^{e} & =  \mRatE \Rnorm\MPC\straight - {\cRat}^{e} \Rnorm\MPC\straight
\\  {\cRat}^{e} & =  \left(\frac{\Rnorm\MPC\straight}{1+\Rnorm\MPC\straight}\right)\mRatE.
\end{aligned}
```

Now we need to use a normalized version of the DBC (equation {eq}`eq:TBS-MLevtp1`),

```{math}
:label: eq:TBS-metp1

\mRatE_{t+1} = (\mRatE_{t}-{\cRat}^{e}_{t})\Rnorm+1
```

to derive the {math}`\mRatE_{t+1}=\mRatE_{t}=\mRatE` locus (also referred to as the {math}`\dmEqZero` locus):

```{math}
:label: eq:TBS-mDelEqZero

\begin{aligned}
      \Rnorm^{-1}(\mRatE-1) & =  \mRatE-{\cRat}^{e}
\\      {\cRat}^{e} & =  \mRatE-\Rnorm^{-1}(\mRatE-1)
\\       & =  (1-\Rnorm^{-1})\mRatE+\Rnorm^{-1}.
\end{aligned}
```

The steady-state levels of {math}`\mRatE` and {math}`{\cRat}^{e}` are the values of these two variables at which both {eq}`eq:TBS-mDelEqZero` and {eq}`eq:TBS-cDelEqZero` hold. This is just a set of two linear equations and two unknowns, and with a bit of algebra can be solved explicitly.

In the special case of logarithmic utility ({math}`\CRRA = 1`), the [approximation appendix](#sec:TBS-mTargApprox) shows that (under some strong assumptions) an approximation to target market resources will be given by

```{math}
:label: eq:TBS-mTargetLogCase

\mTarg^{e} \approx 1 + \left(\frac{1}{(\pGro-\rfree)+\timeRate(1+(\pGro+\timeRate-\rfree)/\urate)}\right)
```

and that the GIC and the RIC guarantee that the denominator of the fraction is a positive number.

This expression encapsulates several of the key intuitions of the model. The "human wealth effect" of growth (cf. {cite:t}`summersCapTax`) is captured by the first {math}`\pGro` term in the denominator; clearly, for any calibration for which the denominator is a positive number, increasing {math}`\pGro` will increase the size of the denominator and therefore reduce the target level of wealth. The human wealth effect of interest rates is correspondingly captured by the {math}`-\rfree` term. An increase in the future discounting rate, {math}`\timeRate`, will also increase the size of the denominator and therefore reduce target wealth. Finally, a reduction in unemployment risk will boost {math}`(\pGro+\timeRate-\rfree)/\urate` and therefore reduce target wealth.[^tbs-guaranteed-under-utility]

[^tbs-guaranteed-under-utility]: {math}`(\pGro+\timeRate-\rfree) > 0` is guaranteed by {eq}`eq:TBS-GICrateUsingwGro` under {math}`\log` utility ({math}`\CRRA=1`).

The assumption of log utility is restrictive, and probably does not capture sufficient aversion to consumption fluctuations. Fortunately, another special case helps to illuminate the effect of higher levels of prudence. The [approximation appendix](#sec:TBS-mTargApprox) shows that, in the special case where {math}`\timeRate=\rfree`, the target level of wealth will be approximable by

```{math}
:label: eq:TBS-mTargetrEqdelta

\mTarg \approx 1 + \left(\frac{1}{(\pGro-\rfree)+\timeRate(1+(\pGro/\urate)(1-(\pGro/\urate)\prudEx))}\right)
```

which is like {eq}`eq:TBS-mTargetLogCase` (with {math}`\timeRate-\rfree=0`) but with the addition of the final term involving {math}`\prudEx` which measures the amount by which prudence exceeds the logarithmic benchmark. An increase in {math}`\prudEx` reduces the denominator of {eq}`eq:TBS-mTargetrEqdelta` and thereby boosts the target level of wealth: Exactly what would be expected from an increase in the intensity of the precautionary motive.

Note that the different effects *interact* with each other, in the sense that the strength of, say, the human wealth effect will vary depending on the values of the other parameters. The ways in which these interactions make intuitive sense will repay deep reflection. (Hint: How much I care about the future governs the power that future events have in determining my targets; use the formula to think about why).

#### Conditions Required for a Perfect Foresight Solution; Existence of Target {math}`\mRatE`

Interestingly, the limit of the buffer stock model as {math}`\urate \downarrow 0` is *not* the perfect foresight solution obtained when {math}`\urate` is exactly equal to zero.

The [perfect foresight CRRA](#sec:PerfForesightCRRA) section shows that in the perfect foresight context, it is necessary to impose the Finite Human Wealth Condition {math}`\Rfree > \WGro` (henceforth, {math}`\FHWCWGro`) to obtain a sensible solution.[^tbs-appendix-perfforesightcrra-shows] But if the {math}`\FHWCWGro` holds, the {math}`\GICWGro` is strictly stronger than the RIC, because the combination {math}`\Pat/\WGro < 1` and {math}`\Rfree > \WGro` obviously implies {math}`\Pat/\Rfree < 1`. If we substitute {math}`\PGro` for {math}`\WGro`, we can define the corresponding version of the condition in the case where growth is {math}`\PGro`: the {math}`\FHWCPGro`.

[^tbs-appendix-perfforesightcrra-shows]: The [appendix to the perfect foresight CRRA section](#sec:PFwhenFHWfails) shows that if the {math}`\FHWCWGro` fails, the limit of the perfect foresight model is {math}`\cFunc(\mRat)=\infty \forall \mRat`, which is not a useful or plausible solution.

It turns out that in the buffer stock model, we can relax the requirement that human wealth is finite.

We pointed out above that {eq}`eq:TBS-GICExistsSoln`, which is necessary for the existence of a steady-state level of consumption, implies that the {math}`\GICPGro` holds in the case being considered here, the limit as {math}`\urate \downarrow 0`. The interesting question is therefore what happens when the {math}`\FHWCWGro` does not hold (that is {math}`\WGro > \Rfree`).

Given that the {math}`\GICWGro` holds, if the {math}`\FHWCWGro` does not hold the RIC may or may not hold: {math}`\WGro > \Rfree` implies that {math}`\Pat/\Rfree > \Pat/\WGro` but {math}`1 > \Pat/\WGro` could be consistent with {math}`\Pat/\Rfree` being greater or less than one. But recall that our assumption is that the unemployed consumer is assumed to behave according to the perfect foresight model with human wealth equal to zero. We must therefore impose the RIC in order to obtain a nondegenerate solution. We therefore impose the RIC.

For any finite horizon, human wealth is finite, and there is a positive probability that income will be zero over the remainder of the horizon. This puts a strict bound on the extent to which consumers are willing to rely for current consumption upon future income that is unbounded in expectation (as the horizon extends) but potentially bounded in practice. In effect, the precautionary motive introduces a self-imposed borrowing constraint that prevents the (arbitrarily large) amount of future income from being something the consumer is willing to borrow against.

The consequence is that the limiting model (as {math}`\urate \downarrow 0`) exhibits a solution with a unique finite target {math}`\mRatE` so long as {eq}`eq:TBS-GICExistsSoln` holds, *even if human wealth is infinite*; in this case the {math}`\dmEqZero` locus is downward sloping (because {math}`1-\Rnorm^{-1}<1`; see {eq}`eq:TBS-mDelEqZero`) while the {math}`\dcEqZero` locus is upward sloping (as guaranteed by {eq}`eq:TBS-GICExistsSoln`). Thus, a target {math}`\mRatE` will exist.

#### The Phase Diagram

{numref}`fig:TBS-PhaseDiag` presents the phase diagram.

:::{figure} #nb-TractableBufferStock-PhaseDiag
:name: fig:TBS-PhaseDiag

Phase Diagram
:::

The {math}`\Delta \mRatE = 0` locus, given in {eq}`eq:TBS-mDelEqZero`, indicates, for a given level of {math}`\mRatE`, how much consumption {math}`{\cRat}^{e}` would be exactly the right amount to leave {math}`\mRatE` unchanged. Call this the "permanently sustainable consumption locus," or for short "sustainable consumption."[^tbs-some-authors-refer] For any given {math}`\mE`, consuming an amount less than the "sustainable" level will cause wealth to rise (and conversely for points above {math}`\Delta \mRatE =0`). This provides the logic for the horizontal arrows of motion in the diagram: Above the sustainable consumption locus they point left, and below they point right.

[^tbs-some-authors-refer]: Some authors refer to {math}`\Delta \mRatE = 0` as giving the level of "permanent income," but this definition differs from {cite:t}`friedmanATheory`'s and is problematic because it could be confused with "permanent labor income" {math}`\Wage_{t} \labor_{t}`.

The intuition for the {math}`\Delta {\cRat}^{e}=0` locus (which comes from {eq}`eq:TBS-cDelEqZero`) is a bit subtler, because it reflects preferences: it comes from the Euler equation, not from the budget constraint, which gives the {math}`\Delta \mRatE = 0` locus. Take a point on the {math}`\Delta {\cRat}^{e}=0` locus, and consider how things would change if {math}`\mE` were a bit higher at the same {math}`\cE`. Recall that the growth rate of consumption consistent with the Euler equation {eq}`eq:TBS-ctp1Oct` depends on the amount by which consumption will fall if the bad state is realized, {math}`\nabla_{t+1} = \cE_{t+1}/\cU_{t+1}`. But {math}`\cU_{t+1} = \MPC \Rfree (\mE_{t} - \cE_{t})` so at the same {math}`\cE_{t}` but a greater {math}`\mE_{t}`, {math}`\cU_{t+1}` will be larger. If {math}`\cE_{t+1}` were to remain unchanged, then with the larger {math}`\cU_{t+1}` the ratio {math}`\nabla_{t+1} = \cE_{t+1}/\cU_{t+1}-1` would be smaller.

The consequences of this are easiest to see in the logarithmic case whose consumption growth equation is derived in {eq}`eq:TBS-cedelapproxLog`, which tells us that {math}`{\cRat}^{e}_{t+1} \approx {\cRat}^{e}_{t}\left(1+ \urate \nabla _{t+1}\right) {\PatPGro}`, which directly implies that the lower {math}`\nabla_{t+1}` will yield a lower {math}`\cE_{t+1}`. That is, for any point to the right of the {math}`\Delta \cE_{t+1}=0` locus, the growth rate of consumption will be lower than at the corresponding point on the locus. Since on the locus, growth was zero, this means that to the right of the locus, {math}`\cE` is declining (hence the down arrow in the phase diagram). Reciprocally, for any point to the left of {math}`\Delta \cE_{t+1}=0`, the Euler equation implies that consumption will rise.

#### The Consumption Function

{numref}`fig:TBS-cFunc` shows the optimal consumption function {math}`\cFunc(m)` for an employed consumer (dropping the {math}`e` superscript to reduce clutter). This is actually just the stable arm in the phase diagram. (Think about why). Also plotted are the 45 degree line along which {math}`\cRat = \mRatE_{t}` as well as the function

```{math}
\bar{\cFunc}(\mRat) = (\mRat-1+\hRat)\MPC
```

where

```{math}
\hRat = \left(\frac{1}{1-\WGro/\Rfree}\right)
```

is the level of (normalized) human wealth. {math}`\bar{\cFunc}(\mRat)` is the solution to a perfect foresight problem in which income grows by the factor {math}`\WGro`; it is depicted in order to introduce a final fact: As wealth approaches infinity, the solution to the problem with uncertain labor income approaches arbitrarily close to the perfect foresight solution.[^tbs-limiting-result-requires]

[^tbs-limiting-result-requires]: This limiting result requires that we impose the {math}`\FHWC (\PGro < \Rfree)`, because the perfect foresight consumption function is not defined if {math}`\PGro \geq \Rfree`. Informally, the proof is as follows. Define {math}`\underline{\cFunc} \equiv (\mRat-1)\MPC=\cFunc^{u}(\mRat)` as the consumption function for the unemployed consumer who will receive no future labor income. Then {math}`\underline{\cFunc}(\mRat) < \cFunc(\mRat) \leq \bar{\cFunc}(\mRat)`, and so {math}`1 < \cFunc(\mRat)/\underline{\cFunc}(\mRat)<\bar{\cFunc}(\mRat)/\underline{\cFunc}(\mRat)`. In the limit as {math}`\mRat \uparrow \infty`, however, human wealth accounts for an arbitrarily small proportion {math}`\MPC \hRat/\MPC (\hRat+\mRat-1)` of consumption, so {math}`\lim_{\mRat \uparrow \infty} \cFunc^{e}(\mRat)/\cFunc^{u}(\mRat) = 1` so the precautionary motive captured by {math}`\nabla` vanishes.

:::{figure} #nb-TractableBufferStock-cFunc
:name: fig:TBS-cFunc

The Consumption Function
:::

Note that {math}`\cFunc(\mRat)` is *concave*.[^tbs-prove-consumption-function] That is, the marginal propensity to consume {math}`\MPCFunc(\mRat) \equiv d \cFunc(\mRat)/d \mRat` is higher at low levels of {math}`m`. This is because of the increase in the intensity of the precautionary motive as resources {math}`\mRat` decline; the consequences of becoming unemployed with little wealth are very painful. The MPC is high at low levels of {math}`\mRat` because at low levels of {math}`\mRat` the *relaxation* in the intensity of the precautionary motive with each extra bit of {math}`\mRat` is quite large ({cite:p}`kimball:smallandlarge`). This diminution in the precautionary motive translates into an increase in consumption; for {math}`m`-poor consumers even a modest increase in {math}`\mRat` can give a substantial boost to {math}`c`.

[^tbs-prove-consumption-function]: {cite:t}`carroll&kimball:concavity` prove that the consumption function must be concave for almost all commonly-used assumptions about risk and utility functions.

This point is clearest as {math}`\mRat` approaches zero. Note that the consumption function always remains below the 45 degree line. This is because if the consumer were to spend all his resources in period {math}`t`, {math}`c_{t}=\mRat_{t}`, then if he became unemployed next period he would have {math}`\mU_{t+1}=(\mRat_{t}-c_{t})\Rnorm=0` which would induce {math}`\cU_{t+1}= \MPC \mU_{t+1}=0`, yielding negative infinite utility. Thus the consumer will never spend all of his resources; he will always leave at least a little bit for next period in case of disaster (unemployment).[^tbs-implication-just-crra]

[^tbs-implication-just-crra]: This is an implication not just of the CRRA utility function used here but of the general class of continuously differentiable utility functions that satisfy the usual *Inada condition* {math}`\uFunc^{\prime}(0) = \infty`.

#### Expected Consumption Growth Is Downward Sloping in {math}`\mRatE`

{numref}`fig:TBS-GrowthA` ("the growth diagram") illustrates some of the same points in a different way. It depicts the growth rate of consumption as a function of {math}`\mRatE_{t}`. Since {math}`\urate \geq 0`, the {math}`\GICPGro` for this model implies:

```{math}
\pGro > \CRRA^{-1}(\rfree-\timeRate) ,
```

a condition that can be visually verified for our benchmark calibration in {numref}`fig:TBS-GrowthA`. Now multiply both sides of {eq}`eq:TBS-ctp1Oct` by {math}`\PGro`, obtaining

```{math}
:label: eq:TBS-cLevGro

\begin{aligned}
        \left(\frac{\cLevBF^{e}_{t+1}}{\cLevBF^{e}_{t}}\right) & =  (\Rfree\Discount)^{1/\CRRA} \left\{1+\urate\left[\left(\frac{{\cRat}^{e}_{t+1}}{\cU_{t+1}}\right)^{\CRRA}-1\right]\right\}^{1/\CRRA}
\\       \Delta \log \cLevBF^{e}_{t+1} & \approx  \CRRA^{-1}(\rfree-\timeRate) +  \urate \nabla _{t+1},
\end{aligned}
```

where the last line uses the same (dubious) approximations used to obtain {eq}`eq:TBS-cedelapprox`.[^tbs-also-assumed-small]

[^tbs-also-assumed-small]: We have also assumed that {math}`(\nabla _{t+1})^{2}` is "small".

Thus consumption growth is equal to what it would be in the absence of uncertainty, plus a precautionary term. Furthermore, the precautionary contribution will become arbitrarily large as {math}`\mRat_{t} \downarrow 0` because {math}`\cU_{t+1} = \mU_{t+1}\MPC = (\mRat_{t}-\cFunc(\mRat_{t}))\Rnorm\MPC` approaches zero as {math}`\mRat_{t} \downarrow 0`. Sure enough, {numref}`fig:TBS-GrowthA` shows that as {math}`\mRatE_{t}` gets low, expected consumption growth gets very large.

:::{figure} #nb-TractableBufferStock-GrowthA
:name: fig:TBS-GrowthA

Income and Consumption Growth
:::

Next, note that the point where the consumption growth locus meets the income growth line is labelled {math}`\mTarg`. This is because the place where consumption growth is equal to income growth is at the target value of {math}`\mRatE`.

#### Summing Up the Intuition

We are finally in position to get an intuitive understanding of how the model works, and why there is a target wealth ratio. On the one hand, consumers are growth-impatient. This prevents their wealth-to-income ratio from heading off to infinity. On the other hand, consumers have a precautionary motive that intensifies more and more as the level of wealth gets lower and lower. At some point the precautionary motive gets strong enough to counterbalance impatience. The point where impatience matches prudence defines the target wealth-to-income ratio.

Now consider the results of increasing the interest rate to {math}`\grave{\rfree}>\rfree`, depicted in {numref}`fig:TBS-GrowthB`. Obviously the perfect foresight consumption growth locus will shift up, to {math}`\CRRA^{-1}(\grave{\rfree}-\timeRate)`, inducing a corresponding increase in the expected consumption growth locus. But we have not changed the expected growth rate of income. It is clear from the figure, therefore, that the new target level of cash-on-hand {math}`\grave{\check{\mRat}}^{e}` will be greater than the original target. That is, an increase in the interest rate increases the target level of wealth, as would be expected on intuitive grounds.

:::{figure} #nb-TractableBufferStock-GrowthB
:name: fig:TBS-GrowthB

Effect of An Increase In {math}`\rfree`
:::

The next exercise, shown in {numref}`fig:TBS-cGroIncreaseMhoPlot`, is an increase in the risk of unemployment {math}`\urate`. The principal effect we are interested in is the upward shift in the expected consumption growth locus to {math}`\Delta \grave{\cLev}_{t+1}`. If the household starts at the original target level of resources {math}`\grave{m}`, the size of the upward shift at that point is captured by the arrow originating at {math}`\{\check{m},\pGro\}`.

In the absence of other consequences of the rise in {math}`\urate`, the effect on the target level of {math}`\mRat` would be unambiguously positive. However, recall our adjustment to the growth rate conditional upon employment, {eq}`eq:TBS-meanPreserve`; this induces the shift in the income growth locus to {math}`\grave{\pGro}` which has an offsetting effect on the target {math}`\mRat` ratio. Under our benchmark parameter values, the target value of {math}`\mRat` is higher than before the increase in risk even after accounting for the effect of higher {math}`\pGro`, but in principle it is possible for the {math}`\pGro` effect to dominate the direct effect. Note, however, that even if the target value of {math}`\mRat` is lower, it is possible that the *saving rate* will be higher; this is possible because the faster rate of {math}`\pGro` makes a given saving rate translate into a lower ratio of wealth to income. In any case, the most useful calibrations of the model are those for which an increase in uncertainty results in either an increase in the saving rate or an increase in the target ratio of resources to permanent income. This is partly because our intent is to use the model to illustrate the general features of precautionary behavior, including the qualitative effects of an increase in the magnitude of transitory shocks, which unambiguously increase both target {math}`\mRat` and saving rates.

:::{figure} #nb-TractableBufferStock-cGroIncreaseMhoPlot
:name: fig:TBS-cGroIncreaseMhoPlot

Effect of an Increase in {math}`\urate`
:::

#### Death to the Log-Linearized Consumption Euler Equation!

{numref}`fig:TBS-GrowthA` and {numref}`fig:TBS-GrowthB` show that, so long as consumers are impatient, the steady state growth rate of consumption will be equal to the steady-state growth rate of income,

```{math}
:label: eq:TBS-ceqg

\Delta \log \cLevBF^{e}_{t+1} = \pGro.
```

Yet the approximate Euler equation for consumption growth, {eq}`eq:TBS-cLevGro`, does not contain any term explicitly involving income growth; in the logarithmic utility case, for example, the expression is

```{math}
:label: eq:TBS-cdelapprox2

\Delta \log \cLevBF^{e}_{t+1} \approx \CRRA^{-1}(\rfree-\timeRate) + \urate \nabla _{t+1}.
```

How can we reconcile these two expressions for consumption growth? Only by realizing that the size of the precautionary term {math}`\urate \nabla_{t+1}` is *endogenous*: It depends on {math}`\pGro`. Indeed, we can solve {eq}`eq:TBS-ceqg` and {eq}`eq:TBS-cdelapprox2` to determine that in steady-state we must have

```{math}
:label: eq:TBS-prectermSS

\urate \check{\nabla} \approx \pGro - \CRRA^{-1}(\rfree-\timeRate).
```

We can use this equation to understand the relationship between parameters and steady-state levels of wealth, by noting that {math}`\nabla_{t+1}(\mRatE_{t})` is a downward-sloping function of {math}`\mRatE_{t}` (see {numref}`fig:TBS-GrowthA` again). This is because at low levels of current wealth, much of the spending of employed consumers is financed by their current income. If they lose that income, they will have no choice but to cut consumption drastically; this is reflected in a large value of {math}`\nabla_{t+1}`.

For example, an increase in the growth rate of income implies that the RHS of equation {eq}`eq:TBS-prectermSS` increases. The new target level of {math}`\mTarg` must be lower, because lower wealth induces greater consumption risk and a corresponding increase in the LHS of {eq}`eq:TBS-prectermSS`. This is how the human wealth effect works in this framework: Consumers who anticipate faster income growth will hold less market wealth.

The fact that consumption growth equals income growth in the steady-state poses major problems for empirical attempts to estimate the Euler equation. To see why, suppose we had a collection of countries indexed by {math}`i`, identical in all respects except that they have different interest rates {math}`\rfree_{i}`. Then in the spirit of {cite:t}`hallSubstitution`, one might be tempted to estimate an equation:

```{math}
\Delta \log \cLev_{i} = \eta_{0} + \eta_{1} \rfree_{i}+\epsilon_{i},
```

and to interpret the coefficient estimate on {math}`\rfree_{i}` as an indication of the value of {math}`\CRRA^{-1}`.

But suppose that all of these countries contained impatient consumers and were in their steady-states where {math}`\Delta \log \cLev_{i} = \pGro_{i}`. Suppose further that all countries had *the same* steady-state income growth rate and unemployment rate.[^tbs-key-point-holds] Then the regression equation would return the estimates

[^tbs-key-point-holds]: The key point holds even if countries have different growth rates, but is easiest to understand if growth rates are identical.

```{math}
\begin{aligned}
        \eta_{0} & =  \pGro  \\
        \eta_{1} & =  0.
\end{aligned}
```

The econometric problem here is that there is an *omitted variable* from the regression specification, the {math}`\urate \nabla` term, which is (perfectly) correlated with the included variable {math}`\rfree_{i}`. Thus, Euler equation estimation cannot be expected to return an unbiased estimate of {math}`\CRRA^{-1}`. For much more on this problem, see {cite:t}`carroll:death`. For empirical evidence that the problem is important in macroeconomic practice, see {cite:t}`ParkerPrestonPrecaution`.

#### A Final Experiment

We now consider a final experiment: A decrease in the time preference rate. To reduce clutter, we drop the {math}`\Delta \cE_{t+1}=0` locus from the phase diagram from {numref}`fig:TBS-PhaseDiag`, and everywhere drop the {math}`e` superscripts. (In exam questions, a figure like this might be referred to as the "simplified consumption phase diagram" or just "the consumption diagram").

{numref}`fig:TBS-DecreaseTheta` depicts the effect on the employed consumer's spending by showing each successive point in time as a dot. Starting at time 0 from the steady-state level of consumption, the decrease in the future discounting rate (an increase in patience) causes an instantaneous drop in the level of consumption. Starting from this diminished base, consumption growth is subsequently faster than before the drop in {math}`\timeRate`.[^tbs-could-also-analyze]

[^tbs-could-also-analyze]: We could also analyze the effects on growth, but the results would be essentially the same as in preceding figure analyzing the effect of an increase the interest rate.

:::{figure} #nb-TractableBufferStock-DecreaseTheta
:name: fig:TBS-DecreaseTheta

Effect of Lower {math}`\timeRate` On Consumption Function
:::

Eventually consumption approaches its new, higher equilibrium ratio to permanent income at a new, higher level of equilibrium {math}`\mRatE`. This higher level of consumption is financed in the long run by the higher interest income earned on the higher level of wealth.

Note again, however, that equilibrium steady-state consumption growth is still equal to the growth rate of income (this follows from the fact that there is a steady-state *level* for the *ratio* of consumption to income, {math}`c`). This means that the higher level of wealth in equilibrium ends up being precisely enough to reduce the precautionary term by an amount that exactly offsets the fact that the {math}`-\CRRA^{-1}\timeRate` term in the Euler equation is now smaller.

{numref}`fig:TBS-cPathAfterThetaDrop`, {numref}`fig:TBS-mPathAfterThetaDrop` and {numref}`fig:TBS-MPCPathAfterThetaDrop` depict the time paths of consumption, market wealth, and the marginal propensity to consume {math}`\MPCFunc(\mRat)` following the decline in {math}`\timeRate`. These are implicit in the phase diagram analysis, but the dots in these three diagrams are spread out evenly over time to give a sense of the time scale over which the model adjusts toward the steady state.

:::{figure} #nb-TractableBufferStock-cPathAfterThetaDrop
:name: fig:TBS-cPathAfterThetaDrop

Path of {math}`{\cRat}^{e}` Before and After {math}`\timeRate` Decline
:::

:::{figure} #nb-TractableBufferStock-mPathAfterThetaDrop
:name: fig:TBS-mPathAfterThetaDrop

Path of {math}`\mRatE` Before and After {math}`\timeRate` Decline
:::

:::{figure} #nb-TractableBufferStock-MPCPathAfterThetaDrop
:name: fig:TBS-MPCPathAfterThetaDrop

Marginal Propensity to Consume {math}`\MPC_{t}` Before and After {math}`\timeRate` Decline
:::

## A Macroeconomic Interpretation

Loosely following {cite:t}`cjSOE` (with some simplifications), this section extends the model to analyze macroeconomic dynamics in a small open economy with a large number of individuals, where the population statistics reflect the fulfillment of individual consumers' *ex ante* expectations; for example, exactly proportion {math}`\urate` of households who are employed in period {math}`t` become "unemployed" before {math}`t+1`, so that the aggregate labor supply of the "active" (still employed) members of a generation evolves according to

```{math}
\PopLev_{t+1,t} = \erate \PopLev_{t,t} ,
```

where the first subscript denotes the date being examined and the second denotes the period of birth of the generation being examined.

We make strong assumptions that permit straightforward aggregation. The first such assumption is that newly unemployed households immediately migrate out of the country (think of British retirees moving to southern Spain).[^tbs-qualitative-story-changed] This means that macroeconomic variables will reflect only the circumstances of employed consumers, rather than a blend of the employed and the unemployed.

[^tbs-qualitative-story-changed]: The qualitative story is not changed if the unemployed stay at home and live off their savings; since they have a simple linear decision rule (they spend a constant proportion of their resources), accounting for their behavior is straightforward but complicates the exposition without adding much substance. See {cite:t}`cjSOE` for a model that incorporates a stay-at-home unemployed population.

Each person is part of a single "generation" of households born at the same time, and every new generation is larger by the factor {math}`\EmpGro` than the newborn generation in the previous period:

```{math}
\PopLev_{t+1,t+1} = \EmpGro \PopLev_{t,t} .
```

We assume that total production by the (surviving) members of a generation grows by the factor {math}`\WGro` every period. If total production is to grow despite a shrinking number of surviving members of the generation, production *per active capita* must grow by {math}`\WGro/\erate` as per {eq}`eq:TBS-meanPreserve`.

Consider the economy in some period 0 in which the size of the newborn population and the wage rate have been normalized to {math}`\PopLev_{0,0} = \Wage_{0} = 1`. If the economy has existed for {math}`-\tThen` periods (where {math}`\tThen` is a negative number, indicating that the economy was created before period 0), the ratio of the total population to the population of newborns will be

```{math}
1 + (\erate/\EmpGro)+ (\erate/\EmpGro)^{2}+ ... +(\erate/\EmpGro)^{-\tThen} = \left(\frac{1-(\erate/\EmpGro)^{-\tThen+1}}{1-(\erate/\EmpGro)}\right)
```

whose limit is a finite number so long as {math}`\erate/\EmpGro < 1`, which we require.

Relative to the labor income of period 0's newborn cohort ({math}`\PopLev_{0,0} \Wage_{0} = 1`), the total labor income in period 0 of the generation born in period {math}`-1` is {math}`\EmpGro^{-1}`; the sum of the incomes of all of the two-period-old individuals is {math}`\EmpGro^{-2}`, and so on; total labor income for all generations in the economy in period 0 is

```{math}
:label: eq:TBS-LabIncTot

1 + \EmpGro^{-1}+ \EmpGro^{-2}+ ...+\EmpGro^{\tThen} = \left(\frac{1-(\EmpGro^{-1})^{-\tThen+1}}{1-\EmpGro^{-1}}\right) ,
```

which is finite so long as either population growth is positive {math}`\EmpGro>1` (which we will assume) or the economy has existed for a finite period of time ({math}`\tThen > -\infty`). In either case, the *proportion* of aggregate income accounted for by a generation born at any specific moment declines toward zero as time passes (old generations never die, they just fade away).

In the balanced growth equilibrium, the growth factor for aggregate population will therefore be {math}`\EmpGro` and output per capita will increase by {math}`\WGro` per period. Total labor income therefore grows by {math}`\EmpGro \WGro.`

### Stakes

We now examine this model under two assumptions about the initial "stake" of newborns in the economy. (We use "stake" to designate a transfer received by newborns). This is explicitly *not* an inheritance, as we have assumed that individuals have no bequest motive and newborns are unrelated to anyone in the existing population. Our motivation is to make the model more tractable, rather than to represent an important feature of the real world; we later perform simulations designed to show that the characteristics of the model with no "stake" are qualitatively and quantitatively similar to those of the more tractable model with the "stake" that makes the model tractable.

#### A "Stake" That Yields a Representative Agent

We first consider a version of the model in which an exogenous redistribution program guarantees that the behavior of employed households can be understood by analyzing the actions of a "representative employed agent."

If a benevolent source outside the economy were to provide every newborn with an initial transfer upon birth of size {math}`\bTarg`, then the newborn's total monetary resources would be

```{math}
\begin{aligned}
  \mRatE_{t,t} & =  \bTarg + 1
\\ & =  \mTarg
.
\end{aligned}
```

Thus, per-capita market resources for members of the newborn generation would be exactly equal to the target level of market resources for a person anticipating the future path of labor income that the members of the newborn generation actually anticipate (which is the same as the future path anticipated by all other generations as well).

If such a transfer policy had been in place forever, the economy at every point in time would consist of employed households whose consumption had been equal to its steady-state value {math}`{\cRat}^{e}` for their whole lives. That is, every individual agent in this economy would be identical in their *ratio* of consumption, market resources, etc. to permanent labor income. The behavior of any individual would therefore be fully captured by the behavior of a representative employed agent.[^tbs-level-permanent-labor]

[^tbs-level-permanent-labor]: The *level* of permanent labor income will differ for different households, depending on their age and accumulated wage seniority; the circumstances of individuals are identical only after their problem has been normalized by their varying levels of permanent labor income.

The foregoing scenario assumed that the "stake" is provided by a mysterious "benevolent source outside the economy." Fortunately, there is an easy way to eliminate this problematic assumption: Assume that the stakes are financed by a wage tax.

The size of the required tax rate is calculated as follows. The total size of the resources transferred to the newborn generation must be

```{math}
\hat{\bRat}^{e}_{t,t} = \hat{\bRat} \PopLev_{t,t} \hat{\Wage}_{t}
```

where

```{math}
\hat{\Wage}_{t} = \underbrace{\left(1-\Tax \right)}_{\equiv \TaxFree}\Wage_{t}
```

is the after-tax wage rate for the economy as a whole (and {math}`\hat{b}` is the steady state target ratio of bank balances to after-tax wages).

From {eq}`eq:TBS-LabIncTot`, the ratio of total aggregate labor income to the labor income of the newborn generation is

```{math}
\left(\frac{1}{1-\EmpGro^{-1}}\right)
```

so the aggregate wage tax rate required to finance a "stake" of size {math}`\hat{b}` for newborns is given by

```{math}
\begin{aligned}
  \hat{b} & =    \left(\frac{\Tax}{1-\EmpGro^{-1}}\right)
\\ \Tax & =  (1-\EmpGro^{-1})\hat{b}
.
\end{aligned}
```

Note, however, that in an economy where this tax has existed forever, the consequence of the tax is effectively just a permanent reduction in after-tax labor income by proportion {math}`\TaxFree`, compared to its value in the absence of the tax. Given the homotheticity of the model, a permanent rescaling by a constant factor leaves the scaled version of the individual's problem (and its solution) unchanged. Thus we can conclude not only that a representative agent exists in this economy, but that the steady-state characteristics of the representative agent's problem are identical (in ratio form) to the characteristics of the unrescaled individual's problem; that is, {math}`\hat{\cFunc}(\mRat) = \cFunc^{e}(\mRat)`, {math}`\hat{b} = \bTarg`, and so on.

Matters are not much more complicated outside the balanced growth steady state, so long as we assume that the government always transfers the amount {math}`\hat{b}` to newborn households, financed by the tax {math}`\Tax` derived above. Consider, for example, an economy that was in steady-state equilibrium leading up to period {math}`\tNow`, and at the beginning of {math}`\tNow` there is a sudden realization that future growth rates will be higher than those anticipated and experienced in the past: {math}`\WGro^{\prime} > \WGro` after {math}`\tNow`. Since expected growth rates affect {math}`\bTarg`, the tax rate must be immediately and permanently changed so that the generations born after {math}`\tNow-1` receive a "stake" of the proper new size. This change in {math}`\Tax` has two consequences for the generations that survive from periods prior to {math}`\tNow`. Under the old tax rate, they would have experienced {math}`\bE_{t} = \bLevBF_{t}/\TaxFree\Wage_{t} = \bTarg`; the change in expectations has no effect on {math}`\bLevBF_{t}` or {math}`\Wage_{t}` but changes the tax rate to {math}`\grave{\Tax}`. Thus these households will have an actual resource ratio that differs from its new target value, {math}`\bE_{t} \neq \Alt{\bTarg}`, both because the after-tax income scaling factor has changed and because the target ratio has changed from {math}`\bTarg` to {math}`\Alt{\bTarg}`.

However, if we started out in steady-state, the *ratio* problem of every member of the continuing-employed population is identical to that of every other such household (though, again, their masses differ depending on age, etc); as a result, the dynamics of the economy are fully captured by keeping track of the relative weights in the economy of the (gradually diminishing) "representative shocked agent" and the (gradually increasing) "representative new agent" whose behavior is locked at its steady-state value.[^tbs-economy-experienced-multiple]

[^tbs-economy-experienced-multiple]: If the economy has experienced multiple shocks, it will be necessary to retain a complete history of the shocks in order to compute the properly population-weighted dynamics. This is not too hard to do, if we start with the assumption that the economy started at its balanced growth equilibrium before the shocks began to arrive.

{numref}`fig:TBS-SOEStakescPathAfterThetaDropPlot` illustrates the dynamics in this economy using an experiment identical to one explored above for the individual's problem: In period 0 there is a one-off decline in the future discounting rate (assuming the economy was in steady state before period 0). In the previous model, each individual consumer's consumption function shifted down, and consumption experienced a discrete jump downward, because the agent became more impatient. Here, there is a modest further effect: With more-patient consumers, the tax rate that the government sets to finance a transfer of {math}`\bTarg` to the newborns must be larger (so that the ratio of initial assets to after-tax income is smaller). Qualitatively, the dynamics are indistinguishable from the individual consumer's dynamics obtainable without working through the extra complication involved in accounting for the "stakes."

:::{figure} #nb-TractableBufferStock-SOEStakescPathAfterThetaDropPlot
:name: fig:TBS-SOEStakescPathAfterThetaDropPlot

Aggregate {math}`c` in PE/SOE Economy Before and After {math}`\timeRate` Decline
:::

#### No Stake

The polar alternative to assuming that newborns get a "stake" is to assume that newborns enter the economy with zero assets. Analysis of this version of the model must be performed using simulation methods, because households of different ages will have different levels of assets. (With a concave and nonanalytical consumption function, analytical aggregation cannot be performed.)

Our simulation procedure assumes that at date 0 the economy has existed forever (so that the age distribution of relative populations and productivities are at their steady-state values), but saving has been impossible prior to period 0.[^tbs-periods-before-unemployment] With everyone's {math}`\bE_{t}=0`, the ratio of market resources to permanent labor income is the same for all individuals:

[^tbs-periods-before-unemployment]: In periods before 0, unemployment presumably would have meant immediate death by starvation; we think of this more as a starting point for the simulations than as a realistic description of a plausible economy.

```{math}
\mRatE_{0,\tThen} = 1 .
```

The consumption ratio in period 0 is therefore {math}`\cFunc(1)` for every household (regardless of age), while the level of total labor income for a generation that is {math}`-\tThen` periods old is {math}`\erate^{\tThen}`.[^tbs-absolute-level-wages] The population of such workers is {math}`(\erate/\EmpGro)^{-\tThen}`, so aggregate consumption will be given by the per-capita consumption ratio, multiplied by the per-capita level of permanent income, multiplied by the population of workers still alive:

[^tbs-absolute-level-wages]: The absolute level of wages will have grown by {math}`\WGro/\erate` per period for these households since their birth, but we have normalized by the level of wages for period-0 newborns, which cancels the {math}`\WGro` from the expression.

```{math}
\begin{aligned}
  \cLev_{0} & =  \sum_{\tThen=0}^{-\infty} \cFunc(1) \erate^{\tThen} (\erate/\EmpGro)^{-\tThen}
\\ & =  \cFunc(1) \sum_{\tThen=0}^{-\infty}  \EmpGro^{\tThen}
\\ & =  \cFunc(1) \left(\frac{1}{1-\EmpGro^{-1}}\right)
.
\end{aligned}
```

The longer a generation lives, the more time it will have had to save toward its target level of wealth; but newborns always begin life with no assets. After period 0, therefore, age-heterogeneity in assets and consumption ratios creeps into the population.

The foregoing discussion contains (in some cases implicitly) all the assumptions necessary to conduct a simulation of this economy. {numref}`fig:TBS-SOENoStakescPath` shows the path of the ratio {math}`\cLev_{t}/\Wage_{t}\PopLev_{t}` starting from period 0 for an economy under our benchmark parameterization that generated our earlier figures. The only extra parameter required beyond those used before is {math}`\EmpGro`; we choose {math}`\EmpGro=1.01` corresponding roughly to the postwar population growth rate in the United States.

:::{figure} #nb-TractableBufferStock-SOENoStakescPath
:name: fig:TBS-SOENoStakescPath

Path of Aggregate {math}`c` in Stakeless PE/SOE Economy From Date 0
:::

## Appendix

(sec:TBS-CGroApprox)=
### Approximate Formula for Consumption Growth

Using from [Math Facts](#fact:mathfactslist) the second-order and then the first-order Taylor approximations [TaylorTwo](#fact:taylortwo) {math}`(1+\epsilon)^{\zeta} \approx 1 + \zeta \epsilon + (1/2)\zeta(\zeta-1) \epsilon^{2}` and then [TaylorOne](#fact:taylorone) {math}`(1+\epsilon)^{\zeta} \approx 1 + \zeta \epsilon`, the expression in braces in {eq}`eq:TBS-ctp1Oct` can be rewritten

```{math}
\begin{aligned}
        \left\{1+\urate\left[\left(\frac{{\cRat}^{e}_{t+1}}{\cU_{t+1}}\right)^{\CRRA}-1\right]\right\}^{1/\CRRA} & =  \left\{1+\urate\left[\left(\frac{\cU_{t+1}+{\cRat}^{e}_{t+1}-\cU_{t+1}}{\cU_{t+1}}\right)^{\CRRA}-1\right]\right\}^{1/\CRRA}
\\      & =  \left\{1+\urate\left[\left(1+\nabla _{t+1}\right)^{\CRRA}-1\right]\right\}^{1/\CRRA}
\\      & \approx       \left\{1+\urate\left[1+\CRRA \nabla _{t+1}+ \CRRA (\nabla _{t+1})^{2}\prudEx-1\right]\right\}^{1/\CRRA}
\\ & =          \left\{1+ \CRRA \urate (\nabla _{t+1}+ (\nabla _{t+1})^{2}\prudEx)\right\}^{1/\CRRA}
\\ & \approx  1+ \urate  \left(1+\nabla _{t+1}\prudEx\right)\nabla _{t+1},
\end{aligned}
```

which leads directly to {eq}`eq:TBS-cedelapprox` in the main text.

(sec:TBS-mTargExists)=
### Conditions for a Target to Exist

#### Using the Phase Diagram Loci

At a steady-state value of {math}`\mRatE`, both {math}`\dcEqZero` and {math}`\dmEqZero` hold (equations {eq}`eq:TBS-cDelEqZero` and {eq}`eq:TBS-mDelEqZero`); for convenience defining {math}`\mu = \Rnorm \MPC \straight + 1`,

```{math}
0 = \overbrace{\left(\frac{\mu-1}{\mu}\right) \mRatE}^{\Delta {\cRat}^{e} } = \overbrace{\left(\frac{\Rnorm-1}{\Rnorm}\right)\mRatE + \Rnorm^{-1}}^{\Delta \mRatE} = 0.
```

But since {math}`\Rnorm^{-1}` is a positive number, at {math}`\mRatE=0` the {math}`\dmEqZero` locus's value is {math}`\Rnorm^{-1}` while the value of the {math}`\dcEqZero` locus is zero, the two loci can intersect for a positive {math}`\mRatE` only if the slope of the {math}`\dcEqZero` locus is greater:[^tbs-also-need-nonnegative]

[^tbs-also-need-nonnegative]: We also need {math}`\mu` to be nonnegative.

```{math}
:label: eq:TBS-cDelEq0SlopeCond

\left(\frac{\mu-1}{\mu}\right) > \left(\frac{\Rnorm-1}{\Rnorm}\right)
```

which is equivalent to

```{math}
:label: eq:TBS-cDelEq0SlopeCondAlt

\overbrace{\Rnorm \MPC \straight}^{= \mu-1} > \Rnorm-1
```

where the LHS is (proportional to) the slope of {math}`\dcEqZero` and the RHS is (proportional to) the slope of {math}`\dmEqZero`.

For any fixed {math}`\urate` and {math}`\WGro` and {math}`\Rfree` we can find some {math}`\alpha` for which {math}`\WGro = \Rfree (1-\alpha \urate)`, and using this {math}`\alpha` it turns out to be useful to rewrite

```{math}
:label: eq:TBS-RnormFromAlpha

\begin{aligned}
  \Rnorm^{-1} & =  \PGro/\Rfree
\\ & =  \WGro/\Rfree(1-\urate)
\\ & =  \Rfree(1-\alpha \urate)/\Rfree(1-\urate)
\\ & =  (1-\alpha \urate + \urate - \urate)/(1-\urate)
\\ & =  (1-\urate+(1-\alpha) \urate)/(1-\urate)
\\ & =  1+(1-\alpha)\urate/(1-\urate)
.
\end{aligned}
```

Note for future use that {eq}`eq:TBS-RnormFromAlpha` implies that whenever {math}`\alpha \leq 1`, the {math}`\FHWCPGro` fails ("human wealth is infinite") because {math}`\Rnorm^{-1} > 1 \Rightarrow \Rfree/\PGro = \Rnorm < 1 \Rightarrow \Rfree < \PGro`.

Multiplying both sides of {eq}`eq:TBS-cDelEq0SlopeCondAlt` by {math}`\Rnorm^{-1}` then substituting the expression for {math}`\Rnorm^{-1}` from {eq}`eq:TBS-RnormFromAlpha` gives

```{math}
:label: eq:TBS-alphaReq

\begin{aligned}
  1- \Rnorm^{-1} & <  \MPC \straight
\\ - (1-\alpha)\urate/(1-\urate) & <  \MPC \straight
\end{aligned}
```

#### A Target Always Exists When Human Wealth Is Infinite

Since {math}`0 < \urate < 1` and {math}`\MPC>0` (as guaranteed by the RIC), {eq}`eq:TBS-alphaReq` is satisfied whenever the {math}`\FHWCPGro` fails ({math}`\alpha \leq 1`) and {math}`\straight > 0`. We now show that under these conditions, {math}`(1+\varpi)^{1/\CRRA}=\straight>0`.

{math}`\straight` from {eq}`eq:TBS-straightDef` is:

```{math}
\straight = \left(1+\overbrace{\urate^{-1}(\PatPGro^{-\CRRA}-1)}^{\equiv \varpi}\right)^{1/\CRRA}
```

but note that

```{math}
\PatPGro = \PatR \overbrace{(\Rfree/\PGro)}^{=\Rnorm}
```

and in the case where {math}`\alpha=1`, {math}`\Rnorm` must also be 1, implying that {math}`\PatPGro = \PatR < 1` (the RIC) so that {math}`\PatPGro^{-\CRRA} > 1` and so {math}`\varpi > 0` and hence {math}`\straight > 1 > 0`. The other interesting case is when {math}`\alpha=0` so that {math}`\WGro=\Rfree` and {math}`\Rnorm=\Rfree/\PGro=\Rfree(1-\urate)/\WGro=(1-\urate)<1`. In this case {math}`\PatPGro < \PatR` and so {math}`\PatPGro^{-\CRRA} > \PatR^{-\CRRA} > 1` and so {math}`\varpi` is even more positive so that {math}`\straight` is even more strongly {math}`>0`. Similar logic holds for any {math}`\alpha \leq 1`.

Thus, we can conclude that, when human wealth is infinite (that is, if {math}`\alpha \leq 1`), a target {math}`\Target{\mRat}^{e}` will exist.

#### Conditions Under Which a Target Exists When Human Wealth is Finite

In the case where human wealth is finite ({math}`\alpha > 1`), we need the RHS of {eq}`eq:TBS-alphaReq` not merely to be positive, but to exceed a specific positive number, {math}`(\alpha-1)\urate/(1-\urate)`:

```{math}
:label: eq:TBS-GPFacRawReqForTarget

\begin{aligned}
    \MPC (1+\varpi)^{1/\CRRA} & >  (\alpha-1)\urate/(1-\urate)
\\   (1+\varpi)^{1/\CRRA} & >  \left(\frac{(\alpha-1)\urate}{\MPC (1-\urate)}\right)
\\   (1+\varpi) & >  \left(\frac{(\alpha-1)\urate}{\MPC (1-\urate)}\right)^{\CRRA}
\\  (\PatPGro^{-\CRRA}-1)\urate^{-1} = \varpi & >  \left(\frac{(\alpha-1)\urate}{\MPC (1-\urate)}\right)^{\CRRA}-1
\\  (\PatPGro^{-\CRRA}-1) & >  \urate \left[\left(\frac{(\alpha-1)\urate}{\MPC (1-\urate)}\right)^{\CRRA}-1\right]
\\  \PatPGro^{-\CRRA} & >  1  + \urate \left[\left(\frac{(\alpha-1)\urate}{\MPC (1-\urate)}\right)^{\CRRA}-1\right]
\\  \PatPGro & <  \left\{1  + \urate \underbrace{\left[\left(\frac{(\alpha-1)\urate}{\MPC (1-\urate)}\right)^{\CRRA}-1\right]}_{\equiv \chi} \right\}^{-1/\CRRA}
\end{aligned}
```

and the boundary will be the point at which this expression holds with equality.

An increase in impatience caused by an increase in the pure time preference rate {math}`\timeRate` (equivalently, a reduction in {math}`\Discount`) has the effect of reducing growth-patience (the LHS of {eq}`eq:TBS-GPFacRawReqForTarget`) and of increasing the RHS. This means that there will be some time preference rate sufficiently large (some {math}`\Discount` sufficiently small) to guarantee that the condition holds with equality. Then {eq}`eq:TBS-GPFacRawReqForTarget` will always be satisfied by any {math}`\Discount` satisfying

```{math}
:label: eq:TBS-DiscountMaxGICWhenFHWCTBSHolds

\Discount < \DiscountMaxGICWhenFHWCTBSHolds .
```

Since we have assumed the RIC (so that {math}`\MPC > 0`), as {math}`\urate \downarrow 0` or {math}`\alpha \downarrow 1`, {eq}`eq:TBS-GPFacRawReqForTarget` asymptotes to the {math}`\GICPGro` for any given value of {math}`\Discount`.

The apparently harder case is when {math}`\alpha>1` and {math}`\urate > 0`. But note that we will have found {math}`\DiscountMaxGICWhenFHWCTBSHolds` if we can find the corresponding {math}`\MPC` at which the first term in {math}`\chi` reaches 1:

```{math}
:label: eq:TBS-DiscountMaxGICWhenFHWCTBSHoldsAndGICPGroIsExactlySatisfied

\begin{aligned}
    \left(\frac{(\alpha-1)\urate}{(1-\PatR) (1-\urate)}\right)^{\CRRA} & =  1
\\  \left(\frac{(\alpha-1)\urate}{(1-\PatR) (1-\urate)}\right) & =  1
\\  \left(\frac{(\alpha-1)\urate}{ (1-\urate)}\right) & =  1-\PatR
\\  1-\left(\frac{(\alpha-1)\urate}{ (1-\urate)}\right) & =  \PatR
\\                  \left[1-\left(\frac{(\alpha-1)\urate}{ (1-\urate)}\right)\right] & =  (\Rfree \Discount)^{1/\CRRA}/\Rfree
\\  \Rfree^{\CRRA}  \left[1-\left(\frac{(\alpha-1)\urate}{ (1-\urate)}\right)\right]^{\CRRA} & =  (\Rfree \Discount)
\\  \Rfree^{\CRRA-1}\left[1-\left(\frac{(\alpha-1)\urate}{ (1-\urate)}\right)\right]^{\CRRA} & =  \DiscountMaxGICWhenFHWCTBSHolds
.\end{aligned}
```

Somewhat miraculously, at this value of {math}`\Discount`, because {math}`\chi=0`, {eq}`eq:TBS-GPFacRawReqForTarget` holds with equality, which means that {math}`\DiscountMaxGICWhenFHWCTBSHolds=\DiscountMaxGICPGro`. This means that the {math}`\GICPGro` defines the definitive boundary condition: A finite target {math}`\mRatE` exists so long as {math}`\Discount < \DiscountMaxGICPGro = \PGro^{\CRRA}/\Rfree.`

#### Solutions Exist Even When Growth Impatience Fails

We have just demonstrated that satisfying the {math}`\GICPGro` condition is necessary and sufficient to guarantee existence of a target {math}`\mTarg^{e}`. But we suggested earlier that a weaker condition, the GIC-TBS, guarantees the existence of a well-defined consumption function.

This can be understood as follows. Rewrite the requirement for existence of a target, {eq}`eq:TBS-cDelEq0SlopeCondAlt`, as

```{math}
:label: eq:TBS-cDelEq0SlopeCondAltAlt

\MPC (1+\varpi)^{1/\CRRA}+1 > \Rnorm ,
```

or taking logs we have approximately

```{math}
:label: eq:TBS-cDelEq0SlopeCondLog

\MPC (1+\varpi)^{1/\CRRA} > \rfree-\pGro .
```

The LHS captures the slope of the {math}`\dcEqZero` locus, which is {math}`\MPC` modified by {math}`\varpi` whose difference from {math}`\varpi=0` captures the degree of growth (im)patience.[^tbs-captures-does-mean] The RHS captures the slope of the {math}`\dmEqZero` locus. Recall that the inequality captures the fact that a target {math}`\mTarg^{e}` exists if these two loci intercept, which happens if the slope of {math}`\dcEqZero` exceeds that of {math}`\dmEqZero`.

[^tbs-captures-does-mean]: "Captures" does not mean "is equal to." Equation {eq}`eq:TBS-cDelEq0SlopeCondAlt` provides the actual formula for the slope.

If the consumer is "growth patience poised" (that is, {math}`\PatPGro = 1`), then {math}`\varpi = 0` and the slope of the {math}`\dcEqZero` locus is identical to the {math}`\MPC` that characterizes the perfect foresight consumption function. In this case {eq}`eq:TBS-cDelEq0SlopeCondLog` becomes

```{math}
:label: eq:TBS-patpGroLT0

\begin{aligned}
  \rfree-\CRRA^{-1}(\rfree-\timeRate) & >   \rfree-\pGro
\\ \pGro & >  \CRRA^{-1}(\rfree-\timeRate)
,\end{aligned}
```

which is the (log version of) the {math}`\GICPGro`. The condition cannot hold both as an equality {math}`\PatPGro=1` (our starting assumption) and an inequality {math}`\PatPGro < 1` (the conclusion of {eq}`eq:TBS-patpGroLT0`). This contradiction constitutes a proof that exactly at {math}`\PatPGro=1` a target does not exist.

As noted above, if the consumer is growth-impatient ({math}`\PatPGro < 1`) then {math}`\varpi > 0` and the slope of {math}`\dcEqZero` is monotonically increased as the degree of growth-impatience increases (so that target {math}`\Target{\mRat}^{e}` is diminished).

But if the consumer is growth-patient ({math}`\PatPGro > 1`) then {math}`\varpi < 0` and the slope of {math}`\dcEqZero` is diminished (which reflects the fact that the greater the degree of patience, the lower will consumption be for any given {math}`\mRatE`).[^tbs-note-fails-slope] The lower bound is defined by the point at which the degree of growth patience becomes so strong that the slope of {math}`\dcEqZero` reaches zero (when {math}`\straight=0`; equivalently, {math}`\varpi` reaches -1). This restricts the permissible degree of growth patience, because {math}`\straight > 0` requires (rewrite {eq}`eq:TBS-GICExistsSoln`):

[^tbs-note-fails-slope]: Note that if the {math}`\GICPGro` fails so that {math}`\straight < 1`, the slope of the {math}`\dcEqZero` locus is shallower than the slope of the perfect foresight consumption function. The fact that these two loci never intersect reflects the fact that the consumer will behave in such a way as to accumulate {math}`\mRatE` forever.

```{math}
\left(\frac{(\Rfree \Discount (1-\urate))^{1/\CRRA}}{\WGro/(1-\urate)}\right) = \left(\frac{(\Rfree \Discount (1-\urate))^{1/\CRRA}}{\PGro}\right) < 1 .
```

Expanding on a discussion in the main text, the numerator in the leftmost expression reflects the sense in which the unemployment risk acts in a manner similar to the effect of an extra degree of discounting (reflecting the fact that the relevant condition applies only so long as the consumer remains in employment, a condition whose probability is {math}`(1-\urate)`), while the denominator reflects the mechanical effect in which the relevant measure of growth is boosted by the adjustment that preserves human wealth. Writing the perfect foresight version of the growth patience factor as {math}`\Pat_{\WGro}` (which is just the limit as {math}`\urate \downarrow 0`), we can see that the expression on the LHS is just {math}`\Pat_{\WGro}(1-\urate)^{1+1/\CRRA}` which is smaller than {math}`\Pat_{\WGro}` because {math}`\urate>0` and {math}`1+\CRRA^{-1} > 0`. So, the GIC-TBS holds whenever the plain-vanilla {math}`\GICPGro` holds, but not vice-versa; there are parametric configurations in which a perfect-foresight consumer with income growth rate {math}`\WGro` would not satisfy the relevant {math}`\GICWGro` (so, their wealth-to-income ratio would go to infinity), but the same consumer faced the same human wealth but with an unemployment risk {math}`\urate` would have a finite target wealth-to-income ratio.

The easiest way to understand all of this is graphically. A *Mathematica* notebook in the handout's repository, [`When-FHWC-Holds.nb`](https://github.com/llorracc/TractableBufferStock/blob/main/Code/Mathematica/Examples/ManipulateParameters/When-FHWC-Holds.nb) ({cite:t}`When-FHWC-Holds`), shows how this works for alternative values of {math}`\Discount`.

(sec:TBS-mTargExact)=
### The Exact Formula for Target {math}`m`

To simplify the expressions in the derivations below, we define {math}`\zeta \equiv \Rnorm \MPC \straight` so that {math}`\Rfree \MPC \straight = \zeta \PGro` and we drop the {math}`e` superscripts, allowing {eq}`eq:TBS-cDelEqZero` to be rewritten as

```{math}
\cRat = \left(\frac{\zeta }{1+\zeta}\right)\mRat .
```

If a target value {math}`\mTarg` exists it will be at the point of intersection between the {math}`\dcEqZero` and the {math}`\dmEqZero` loci:

```{math}
:label: eq:TBS-mTarget

\begin{aligned}
  \left(\frac{\zeta}{1+\zeta}\right)\mTarg & =  (1-\Rnorm^{-1})\mTarg+\Rnorm^{-1}
\\  \left(\Rnorm\frac{\zeta}{1+\zeta}\right)\mTarg & =  (\Rnorm-1)\mTarg+1
\\  \left(\Rnorm\left\{\frac{\zeta}{1+\zeta}-1\right\}+1\right)\mTarg & =  1
\\  \left(\Rnorm\left\{\frac{\zeta-(1+\zeta)}{1+\zeta}\right\}+\frac{1+\zeta}{1+\zeta}\right)\mTarg & =  1
\\  \left(\frac{1+\zeta-\Rnorm}{1+\zeta}\right)\mTarg & =  1
\\  \mTarg & =  \left(\frac{1+\zeta}{1+\zeta-\Rnorm}\right)
\\  \mTarg & =  \left(\frac{1+\zeta+\Rnorm-\Rnorm}{1+\zeta-\Rnorm}\right)
\\ & =  1 + \left(\frac{\Rnorm}{1+\zeta-\Rnorm}\right)
\\ & =  1 + \left(\frac{\Rfree}{\PGro+\zeta\PGro-\Rfree}\right)
.
\end{aligned}
```

A first point about this formula is suggested by the fact that

```{math}
\zeta\PGro = \Rfree \MPC \left(1+\left(\frac{\PatPGro^{-\CRRA} - 1}{\urate}\right)\right)^{1/\CRRA}
```

which is likely to increase as {math}`\urate` approaches zero.[^tbs-likely-but-certain] Note that the limit as {math}`\urate \rightarrow 0` is infinity, which implies that {math}`\lim_{\urate \rightarrow 0} \mTarg = 1`. This is precisely what would be expected from this model in which consumers are impatient but self-constrained to have {math}`\mRatE > 1`: As the risk gets infinitesimally small, the amount by which target {math}`\mRatE` exceeds its minimum possible value shrinks to zero.

[^tbs-likely-but-certain]: "Likely" but not certain because of the fact that {math}`\urate` affects {math}`\PatPGro` as well as appearing in the denominator of {eq}`eq:TBS-mTarget`; however, for plausible calibrations the effect of the denominator predominates.

We now show that the RIC and {math}`\GICPGro` ensure that the denominator of the fraction in {eq}`eq:TBS-mTarget` is positive:

```{math}
\begin{aligned}
\PGro + \zeta \PGro - \Rfree & =  \PGro + \Rfree \MPC \straight - \Rfree
 \\& =  \PGro + \Rfree \left(1- \frac{(\Rfree \Discount)^{1/\rho}}{\Rfree}\right) \left(\frac{(\frac{(\Rfree\Discount)^{1/\CRRA}}{\PGro})^{-\CRRA}-1}{\urate}+1\right)^{1/\CRRA}-\Rfree
 \\& >   \PGro+\Rfree \left(1-\frac{(\Rfree\Discount)^{1/\rho}}{\Rfree}\right)
\left(\frac{(\frac{(\Rfree\Discount)^{1/\CRRA}}{\PGro})^{-\CRRA}-1}{1}+1\right)^{1/\CRRA}-\Rfree
 \\& =  \PGro+\Rfree\left(1-\frac{(\Rfree\Discount)^{1/\rho}}{\Rfree}\right)\frac{\PGro}{(\Rfree\Discount)^{1/\CRRA}}-\Rfree
 \\& =  \PGro+\Rfree \frac{\PGro}{(\Rfree\Discount)^{1/\CRRA}}- \PGro - \Rfree
 \\& =  \Rfree \left(\frac{\PGro}{(\Rfree\Discount)^{1/\CRRA}}-1\right)
 \\& >  0.
\end{aligned}
```

However, note that {math}`\urate` also affects {math}`\PGro`; thus, the first inequality above does not necessarily imply that the denominator is decreasing as {math}`\urate` moves from {math}`0` to {math}`1`.

(sec:TBS-mTargApprox)=
### Approximating Target {math}`m`

Now defining

```{math}
\aleph = \left(\frac{\PatPGro^{-\CRRA} - 1}{\urate}\right),
```

under certain conditions we can obtain further insight into {eq}`eq:TBS-mTarget` using a judicious mix of first- and second-order Taylor expansions (along with {math}`\MPC = -\patr`):[^tbs-below-caveats]

[^tbs-below-caveats]: See below for caveats.

```{math}
:label: eq:TBS-zetaExp

\begin{aligned}
  \zeta\PGro & =  \Rfree \MPC \left(1+\aleph\right)^{1/\CRRA}
\\ & \approx  -\Rfree \patr \left(1+\CRRA^{-1}\aleph+(\CRRA^{-1})(\CRRA^{-1}-1)(\aleph^{2}/2)\right)
\\ & =  -\Rfree \patr \left(1+\CRRA^{-1}\aleph\left\{1+\left(\frac{1-\CRRA}{\CRRA}\right)(\aleph/2)\right\}\right)
.
\end{aligned}
```

But

```{math}
:label: eq:TBS-hatpi

\begin{aligned}
  \aleph & =  \left(\frac{(1+\patpGro)^{-\CRRA}-1}{\urate}\right)
\\ & \approx  \left(\frac{1- \CRRA \patpGro-1}{\urate}\right)
\\ & \approx  -\left(\frac{\CRRA \patpGro}{\urate}\right)
\end{aligned}
```

which is guaranteed to be positive by the {math}`\GICPGro`, but which can take any value in the interval {math}`(0,\infty)`. Note, however, that the approximations above are valid only if {math}`\aleph` is "small" which requires that the degree of growth impatience be small relative to the size of the unemployment risk. Thus, the formulae derived above (and used below) are reliable only in rather special circumstances, in particular when the consumer is only very slightly growth-impatient.[^tbs-other-approximations-better] Under these circumstances, this approximation can be substituted into {eq}`eq:TBS-zetaExp` to obtain

[^tbs-other-approximations-better]: Other approximations are better for consumers who are highly impatient, relative to their unemployment risk; in this case a better approximation to {eq}`eq:TBS-zetaExp` is obtained by rewriting it as {math}`\zeta\PGro = \Rfree \MPC \aleph^{1/\CRRA} \left(\aleph^{-1}1+1\right)^{1/\CRRA}` and approximating using {math}`(1+\aleph^{-1})^{1/\CRRA} \approx 1 + \CRRA^{-1}\aleph^{-1}+\CRRA^{-1}(\CRRA^{-1}-1)\aleph^{-2}/2`.

```{math}
:label: eq:TBS-zetaGammaApprox

\begin{aligned}
  \zeta\PGro & \approx   -\Rfree \patr \left(1-(\patpGro/\urate)(1+(1-\CRRA)(-\patpGro/\urate)/2)\right)
\\ & \approx  \underbrace{-\Rfree \patr}_{>0} \left\{1\underbrace{-(\patpGro/\urate)}_{>0}\left(1+\underbrace{(1-\CRRA)}_{<0}\underbrace{(-\patpGro/\urate)}_{>0}/2\right)\right\}
.
\end{aligned}
```

and inspired by {cite:t}`kimball:smallandlarge` defining a term related to the excess of prudence over the logarithmic case,

```{math}
\prudEx = \left(\frac{\CRRA-1}{2}\right),
```

{eq}`eq:TBS-mTarget` can be approximated by

```{math}
:label: eq:TBS-mTargetApprox

\begin{aligned}
 \mTarg & \approx  1 + \left(\frac{1}{\PGro/\Rfree-\patr \left(1-(\patpGro/\urate)(1-(-\patpGro/\urate)\prudEx) \right)-1}\right)
\\ & \approx  1 + \left(\frac{1}{(\pGro-\rfree)+(-\patr) \left(1+(-\patpGro/\urate)(1-(-\patpGro/\urate)\prudEx)\right)}\right)
\end{aligned}
```

where negative signs have been preserved in front of the {math}`\patr` and {math}`\patpGro` terms as a reminder that the {math}`\GICPGro` and the RIC imply these terms are themselves negative (so that {math}`-\patr` and {math}`-\patpGro` are positive). *Ceteris paribus*, an increase in relative risk aversion {math}`\CRRA` will increase {math}`\prudEx` and thereby decrease the denominator of {eq}`eq:TBS-mTargetApprox`. This suggests that greater risk aversion will result in a larger target level of wealth.[^tbs-suggests-because-derivation]

[^tbs-suggests-because-derivation]: "Suggests" because this derivation used some dubious approximations; the suggestion is verified, however, for plausible numerical calibrations.

The formula also provides insight about how the human wealth effect works in equilibrium. All else equal, the human wealth effect is captured by the {math}`(\pGro-\rfree)` term in the denominator of {eq}`eq:TBS-mTargetApprox`, and it is obvious that a larger value of {math}`\pGro` will result in a smaller target value for {math}`m`. But it is also clear that the size of the human wealth effect will depend on the magnitude of the patience and prudence contributions to the denominator, and that those terms can easily dominate the human wealth effect. This reduction in the human wealth effect is interesting because practitioners have known at least since {cite:t}`summersCapTax` that the human wealth effect is implausibly large in the perfect foresight model.

For {eq}`eq:TBS-mTargetApprox` to make sense, we need the denominator of the fraction to be a positive number; defining

```{math}
\patpGrohat = \patpGro(1-(-\patpGro/\urate)\prudEx),
```

this means that we need:

```{math}
:label: eq:TBS-newDenom

\begin{aligned}
    (\pGro - \rfree) & >  \patr - \patr\patpGrohat/\urate
\\   & =  \left(\CRRA^{-1}(\rfree-\timeRate)-\rfree\right)-  \patr\patpGrohat/\urate
\\ \pGro & >  \CRRA^{-1}(\rfree-\timeRate)-  \patr\patpGrohat/\urate
\\ 0 & >  \underbrace{\CRRA^{-1}(\rfree-\timeRate) - \pGro}_{\patpGro} -  \patr(\patpGrohat/\urate)
\\ 0 & >  \patpGro -  \patr(\patpGrohat/\urate)
.
\end{aligned}
```

But since the RIC guarantees {math}`\patr<0` and the {math}`\GICPGro` guarantees {math}`\patpGro<0` (which, in turn, guarantees {math}`\patpGrohat < 0`), this condition must hold.[^tbs-more-detail-second]

[^tbs-more-detail-second]: In more detail: For the second-order Taylor approximation in {eq}`eq:TBS-zetaExp`, we implicitly assume that the absolute value of the second-order term is much smaller than that of the first-order one, i.e. {math}`|\CRRA^{-1} \aleph | \geq |(\CRRA^{-1})(\CRRA^{-1}-1)(\aleph^{2}/2)|`. Substituting {eq}`eq:TBS-hatpi`, the above could be simplified to {math}`1 \geq (-\patpGro/\urate)\prudEx`, therefore we have {math}`\patpGrohat < 0`. This simple justification is based on the confidence that we have proved above that RIC and {math}`\GICPGro` guarantee the denominator of the fraction in {eq}`eq:TBS-mTarget` is positive.

The same set of derivations imply that we can replace the denominator in {eq}`eq:TBS-mTargetApprox` with the negative of the RHS of {eq}`eq:TBS-newDenom`, yielding a more compact expression for the target level of resources,

```{math}
:label: eq:TBS-mTargetCompact

\begin{aligned}
 \mTarg & \approx  1 + \left(\frac{1}{\patr(\patpGrohat/\urate) - \patpGro }\right)
\\ & =  1 + \left(\frac{1/(-\patpGro)}{1+(-\patr/\urate)(1+(-\patpGro/\urate)\prudEx)  }\right)
.
\end{aligned}
```

This formula makes plain the fact that an increase in either form of impatience, by increasing the denominator of the fraction in {eq}`eq:TBS-mTargetCompact`, will reduce the target level of assets.

We are now in position to discuss {eq}`eq:TBS-mTargetApprox`, understanding that the impatience conditions guarantee that its denominator is a positive number.

Two specializations of the formula are particularly useful. The first is the case where {math}`\CRRA = 1` (logarithmic utility). In this case

```{math}
\begin{aligned}
    \patr & =  -\timeRate
\\  \patpGro & =  \rfree-\timeRate-\pGro
\\  \prudEx & =  0
\end{aligned}
```

and the approximation becomes

```{math}
\mTarg \approx 1 + \left(\frac{1}{(\pGro-\rfree)+\timeRate(1+(\pGro+\timeRate-\rfree)/\urate)}\right)
```

which neatly captures the effect of an increase in human wealth (via either increased {math}`\pGro` or reduced {math}`\rfree`), the effect of increased impatience {math}`\timeRate`, or the effect of a reduction in unemployment risk {math}`\urate` in reducing target wealth.

The other useful case to consider is where {math}`\rfree = \timeRate` but {math}`\CRRA>1`. In this case, we have

```{math}
\begin{aligned}
    \patr & =  -\timeRate
\\  \patpGro & =  -\pGro
\\  \patpGrohat & =  -\pGro (1-(\pGro/\urate)\prudEx)
\end{aligned}
```

so that

```{math}
\mTarg \approx 1 + \left(\frac{1}{(\pGro-\rfree)+\timeRate(1+(\pGro/\urate)(1-(\pGro/\urate)\prudEx))}\right)
```

where the additional term involving {math}`\prudEx` in this equation captures the fact that an increase in the prudence term {math}`\prudEx` shrinks the denominator and thereby boosts the target level of wealth.[^tbs-would-inappropriate-use]

[^tbs-would-inappropriate-use]: It would be inappropriate to use the equation to consider the effect of an increase in {math}`\rfree` because the equation was derived under the assumption {math}`\timeRate=\rfree` so {math}`\rfree` is not free to vary.

(sec:TBS-NumericalSolution)=
### Numerical Solution

#### The Consumption Function

To solve the model by the method of *reverse shooting*,[^tbs-presentation-shooting-methods] we need {math}`{\cRat}^{e}_{t}` as a function of {math}`{\cRat}^{e}_{t+1}`. Starting with {eq}`eq:TBS-ctp1Oct`:

[^tbs-presentation-shooting-methods]: See {cite:t}`judd:book` for a presentation of shooting methods of solution for numerical difference and differential equations.

```{math}
:label: eq:TBS-cReverse

\begin{aligned}
         \left(\frac{{\cRat}^{e}_{t+1}}{{\cRat}^{e}_{t}}\right) & =  \PGro^{-1} (\Rfree\Discount)^{1/\CRRA} \left\{1+\urate\left[\left(\frac{{\cRat}^{e}_{t+1}}{\cU_{t+1}}\right)^{\CRRA}-1\right]\right\}^{1/\CRRA}
\\       {\cRat}^{e}_{t} & =  \left(\frac{{\cRat}^{e}_{t+1}}{\PGro^{-1} (\Rfree\Discount)^{1/\CRRA} \left\{1+\urate\left[\left(\frac{{\cRat}^{e}_{t+1}}{\MPC (\mRatE_{t+1}-1)}\right)^{\CRRA}-1\right]\right\}^{1/\CRRA} }  \right)
\\        & =  \PGro (\Rfree\Discount)^{-1/\CRRA} {\cRat}^{e}_{t+1}\left\{1+\urate\left[\left(\frac{{\cRat}^{e}_{t+1}}{\MPC (\mRatE_{t+1}-1)}\right)^{\CRRA}-1\right]\right\}^{-1/\CRRA}        .
\end{aligned}
```

Inverting {eq}`eq:TBS-metp1`, the reverse shooting equation for {math}`\mRatE_{t}` is

```{math}
:label: eq:TBS-mReverse

\mRatE_{t} = \Rnorm^{-1} (\mRatE_{t+1}-1)+{\cRat}^{e}_{t} .
```

The reverse shooting approximation will be more accurate if we use it to obtain estimates of the marginal propensity to consume as well. These are obtained by differentiating the consumption Euler equation with respect to {math}`m_{t}`:

```{math}
:label: eq:TBS-dEuler

\begin{aligned}
  \uP(\cFunc^{e}(\mRat_{t})) & = \overbrace{\Rnorm \Discount \PGro^{1-\CRRA}}^{\beth} \Ex_{t}[\uP(\cFunc^{\bullet}(\mRat_{t+1}))]
\\  \uFunc^{\prime\prime}(\cFunc^{e}(\mRat_{t}))\MPCFunc^{e}(\mRat_{t}) & = \beth  \Rnorm (1-\MPCFunc^{e}(\mRat_{t}))\Ex_{t}[\uFunc^{\prime\prime}(\cFunc^{\bullet}(\mRat_{t+1}))\MPCFunc^{\bullet}(\mRat_{t+1})]
\end{aligned}
```

so that defining, e.g., {math}`\MPCE_{t} = \MPCFunc^{e}(\mRat_{t})` we have

```{math}
:label: eq:TBS-naturalMPC

\begin{aligned}
 \MPCE_{t} & =  (1-\MPCE_{t}) \underbrace{\beth \Rnorm (1/\uPP({\cRat}^{e}_{t}))\Ex_{t}\left[\uPP(c^{\bullet}_{t+1})\MPC^{\bullet}_{t+1}\right]}_{\equiv \natural_{t+1}}
\\ (1+\natural_{t+1})\MPCE_{t} & = \natural_{t+1}
\\ \MPCE_{t} & = \left(\frac{\natural_{t+1}}{1+\natural_{t+1}}\right)
.
\end{aligned}
```

At the target level of {math}`\mRatE` we have

```{math}
\overbrace{(1/\uPP(\cTarg^{e}))\Ex_{t}\left[\uPP(c^{\bullet})\MPC^{\bullet}\right]}^{\natural / \Rnorm \beth} = \erate \overbrace{(\uPP(\cTarg^{e})/\uPP(\cTarg^{e}))}^{=1}\MPCE+\urate (\uPP(\cTarg^{u})/\uPP(\cTarg^{e}))\MPC
```

so that

```{math}
\natural = \beth \Rnorm (\erate \MPCE + \urate (\cTarg^{u}/\cTarg^{e})^{-\CRRA-1} \MPC)
```

yielding from {eq}`eq:TBS-naturalMPC` a quadratic equation in {math}`\MPCE`:

```{math}
:label: eq:TBS-quadraticForTargetMPC

\left(1+\beth \Rnorm (\erate \MPCE + \urate (\cTarg^{u}/\cTarg^{e})^{-\CRRA-1} \MPC) \right)\MPCE = \beth \Rnorm (\erate \MPCE + \urate (\cTarg^{u}/\cTarg^{e})^{-\CRRA-1} \MPC)
```

which has one solution for {math}`\MPCE` in the interval {math}`[0,1]`, which is the MPC at target wealth.[^tbs-mathematica-code-constructs]

[^tbs-mathematica-code-constructs]: The *Mathematica* code in the handout's [repository](https://github.com/llorracc/TractableBufferStock) constructs this derivative and solves the quadratic equation analytically; its Matlab code simply copies the analytical formula generated by *Mathematica*. This chapter's figures instead use HARK's `TractableConsumerType`, which solves the model by the same reverse shooting.

The limiting MPC as consumption approaches zero, {math}`\bar{\MPC}^{e},` will also be useful; this is obtained by noting that utility in the employed state next year becomes asymptotically irrelevant as {math}`{\cRat}^{e}_{t}` approaches zero, so that

```{math}
\begin{aligned}
  \lim_{{\cRat}^{e}_{t} \rightarrow 0}  \overbrace{ \beth \Rnorm \MPCE_{t+1} \left(\erate ({\cRat}^{e}_{t+1}/{\cRat}^{e}_{t})^{-\CRRA-1}  + \urate (\cU_{t+1}/{\cRat}^{e}_{t})^{-\CRRA-1}\MPC\right)}^{\natural_{t+1}} & =  \beth \Rnorm \urate (\cU_{t+1}/{\cRat}^{e}_{t})^{-\CRRA-1}\MPC
\\  & =  \beth \Rnorm \urate (\MPC \Rnorm \aE_{t}/(\aE_{t}(\bar{\MPC}^{e}/(1-\bar{\MPC}^{e})))^{-\CRRA-1})\MPC
\\ & =  \beth \Rnorm \urate (\MPC \Rnorm ((1-\bar{\MPC}^{e})/\bar{\MPC}^{e}))^{-\CRRA-1}\MPC
\end{aligned}
```

so that from {eq}`eq:TBS-naturalMPC` we have

```{math}
:label: eq:TBS-MPCat0

\bar{\MPC}^{e} \equiv \lim_{\mRat_{t} \rightarrow 0} \MPCFunc^{e}(\mRat_{t}) = \left(\frac{ \beth \Rnorm \urate (\MPC \Rnorm ((1-\bar{\MPC}^{e})/\bar{\MPC}^{e}))^{-\CRRA-1}\MPC }{1+ \beth \Rnorm \urate (\MPC \Rnorm ((1-\bar{\MPC}^{e})/\bar{\MPC}^{e}))^{-\CRRA-1}\MPC }\right)
```

which implicitly defines {math}`\bar{\MPC}^{e}`. An explicit solution is not available, but after parameter values have been defined a numerical rootfinder can calculate a solution almost instantly.

Finally, it will be useful to have an estimate of the curvature (second derivative) of the consumption function. This can be obtained by a procedure analogous to the one used to obtain the MPC: differentiate the differentiated Euler equation {eq}`eq:TBS-dEuler` again. Noting that {math}`\MPC^{u\prime}=0` we can obtain:

```{math}
:label: eq:TBS-kappaPExpr

\begin{aligned}
(\MPCFunc^{e}_{t})^{2} \uPPP(\cFunc^{e}_{t}) +\MPCFunc_{t}^{e\prime}\uPP(\cFunc^{e}_{t}) & = \beth \Rnorm \Big\{(-\MPCFunc_{t}^{e\prime}) \Ex_{t}[\uPP(\cFunc^{\bullet}_{t+1})\MPCFunc^{\bullet}_{t+1}]
\\ & \quad +  \Rnorm (1-\MPCFunc^{e}_{t})^{2}\left(\Ex_{t}[(\MPCFunc_{t+1}^{\bullet})^{2}\uPPP(\cFunc^{\bullet}_{t+1})]+\erate  \uPP(\cFunc^{e}_{t+1})\MPCFunc_{t+1}^{e\prime}\right)\Big\}
\end{aligned}
```

so that

```{math}
:label: eq:TBS-kappaPReverse

\MPCFunc^{e\prime}_{t} = \left(\frac{\beth \Rnorm^{2} (1-\MPCFunc^{e}_{t})^{2} \left( \Ex_{t}[(\MPCFunc_{t+1}^{\bullet})^{2}\uPPP(\cFunc^{\bullet}_{t+1})] +\erate \uPP(\cFunc^{e}_{t+1}) \MPCFunc^{e \prime}_{t+1}\right)-(\MPCFunc^{e}_{t})^{2} \uPPP(\cFunc^{e}_{t})}{\uPP(\cFunc^{e}_{t})+\beth \Rnorm \Ex_{t}[\uPP(\cFunc^{\bullet}_{t+1})\MPCFunc^{\bullet}_{t+1}] }\right)
```

which can be further simplified at the target because {math}`\MPCFunc^{e \prime}_{t}(\mTarg) = \MPCFunc^{e \prime}_{t+1}(\mTarg) = \MPC^{e \prime}` so that

```{math}
:label: eq:TBS-MPCPrimeSS

\MPC^{e\prime} = \left(\frac{\beth \Rnorm^{2} (1-\MPCE)^{2}\Ex_{t}[(\MPC^{\bullet})^{2} \uPPP(c^{\bullet})] -(\MPCE)^{2} \uPPP(\cTarg^{e})}{\uPP(\cTarg^{e}) + \beth \Rnorm \Ex_{t}[\uPP(c^{\bullet})\MPC^{\bullet}]- \beth \Rnorm^{2} (1-\MPCE)^{2}\erate \uPP(\cTarg^{e})}\right) .
```

Another differentiation of {eq}`eq:TBS-kappaPExpr` similarly allows the construction of a formula for the value of {math}`\MPC^{e \prime\prime}` at the target {math}`\mTarg`; in principle, any number of derivatives can be constructed in this manner.[^tbs-mathematica-permits-convenient]

[^tbs-mathematica-permits-convenient]: *Mathematica* permits the convenient computation of the analytical derivatives, and then the substitution of constant target values to obtain analytical expressions like {eq}`eq:TBS-MPCPrimeSS`. These solutions are simply imported by hand into the Matlab code.

Reverse shooting requires us to solve separately for an approximation to the consumption function above the steady state and another approximation below the steady state. Using the approximate steady-state {math}`\MPCE` and {math}`\MPC^{e\prime}` obtained above, we begin by picking a very small number for {math}`\blacktriangle` and then creating a Taylor approximation to the consumption function near the steady state:

```{math}
:label: eq:TBS-revshootmstart

\begin{aligned}
  \mRatE_{\Alt{t}} & = \mTarg + \blacktriangle
\\ \tilde{\mathbf{c}}(\blacktriangle) & = \cTarg^{e} + \blacktriangle \MPCE+ (\blacktriangle^{2}/2) \MPC^{e\prime}+ (\blacktriangle^{3}/6) \MPC^{e\prime\prime}
\end{aligned}
```

and then iterate the reverse-shooting equations until we reach some period {math}`n` in which {math}`\mRatE_{\Alt{t}-n}` escapes some pre-specified interval {math}`[\underline{\mRat}^{e},\bar{\mRat}^{e}]` (where the natural value for {math}`\underline{\mRat}^{e}` is 1 because this is the {math}`\mRat` that would be owned by a consumer who had saved nothing in the prior period and therefore is below any feasible value of {math}`\mRat` that could be realized by an optimizing consumer). This generates a sequence of points all of which are on the consumption function. A parallel procedure (substituting {math}`-` for {math}`+` in {eq}`eq:TBS-revshootmstart` and where appropriate in the corresponding equation for {math}`\cRat` generates the sequence of points for the approximation below the steady state. Taken together with the already-derived characterization of the function at the target level of wealth, these points constitute the basis for a piecewise second-order interpolating approximation to the consumption function on the interval {math}`[\underline{\mRat}^{e},\bar{\mRat}^{e}]`.

#### The Value Function

As a preliminary, note that since {math}`\uFunc(xy)=\uFunc(x)y^{1-\CRRA}`, value for an unemployed consumer is

```{math}
\begin{aligned}
  \VFunc_{t}^{u} & =  \uFunc(C_{t}^{u})+\Discount \uFunc(C_{t+1}^{u}) + \Discount^{2} \uFunc(C_{t+2}^{u})+...
\\ & =  \uFunc(C_{t}^{u})\left(1+\Discount \{(\Rfree \Discount)^{1/\CRRA}\}^{1-\CRRA} + \Discount^{2}\left\{(\Rfree \Discount)^{2/\CRRA}\right\}^{1-\CRRA}+...\right)
\\ & =  \uFunc(C_{t}^{u})\underbrace{\left(\frac{1}{1-\Discount (\Rfree \Discount)^{(1/\CRRA)-1}}\right)}_{\equiv \mathfrak{v}}
\end{aligned}
```

where the RIC guarantees that the denominator in the fraction is a positive number.

From this we can see that value for the normalized problem is similarly:

```{math}
\vFunc^{u}(\mRat_{t}) = \uFunc(\MPC m_{t}) \mathfrak{v} .
```

Turning to the problem of the employed consumer, we have

```{math}
\vFunc^{e}(\mRat_{t}) = \uFunc({\cRat}^{e}_{t})+\Discount \PGro^{1-\CRRA} \Ex_{t}[\vFunc^{\bullet}(\mRat_{t+1})]
```

and at the target level of market resources this will be unchanging for a consumer who remains employed so that

```{math}
\begin{aligned}
  \vTarg^{e} & =  \uFunc(\cTarg^{e})+\Discount \PGro^{1-\CRRA} \left(\erate \vTarg^{e} + \urate \vFunc^{u}(\aE \Rnorm)\right)
\\ (1-\Discount \PGro^{1-\CRRA} \erate) \vTarg^{e} & =  \uFunc(\cTarg^{e})+\Discount \PGro^{1-\CRRA} \urate \vFunc^{u}(\aE \Rnorm)
\\ \vTarg^{e} & =  \left(\frac{\uFunc(\cTarg^{e})+\Discount \PGro^{1-\CRRA} \urate \vFunc^{u}(\aE \Rnorm)}{(1-\Discount \PGro^{1-\CRRA} \erate) }\right)
.
\end{aligned}
```

Given these facts, our recursion for generating a sequence of points on the consumption function can be used at the same time to generate corresponding points on the value function from

```{math}
\vE_{t} = \uFunc({\cRat}^{e}_{t})+\Discount \PGro^{1-\CRRA} \left(\erate \vE_{t+1} + \urate \vFunc^{u}(\aE_{t} \Rnorm)\right)
```

with the first iteration point generated by numerical integration from

```{math}
v^{e}_{\Alt{t}} = \vTarg^{e}+\int_{0}^{\blacktriangle} \uP(\tilde{\mathbf{c}}(\bullet)) d\bullet
```

(sec:TBS-Algorithm)=
### The Algorithm

With the above results in hand, the model is solved and the various functions constructed as follows. Define {math}`\star_{t} = \{\mRatE_{t},{\cRat}^{e}_{t},\MPCE_{t},\vE_{t},\MPC_{t}^{e\prime}\}` as a vector of points that characterizes a particular situation that an optimizing employed household might be in at any given point in time. Using the backwards-shooting functions derived above, for any point {math}`\star_{\Alt{t}}` we can construct the sequence of points that must have led up to it: {math}`\star_{\Alt{t}-1}` and {math}`\star_{\Alt{t}-2}` and so on. And using the approximations near the steady state like {eq}`eq:TBS-revshootmstart`, we can construct a vector-valued function {math}`\pmb{\circ}(\blacktriangle)` that generates, e.g., {math}`\{\mTarg+\blacktriangle,\tilde{\mathbf{c}}(\blacktriangle), ... \}`.

Now define an operator {math}`\cdots` as follows: {math}`\cdots` applied to some starting point {math}`\star_{t}` uses the backwards dynamic equations defined above to produce a vector of points {math}`\star_{t-1},\star_{t-2},...` consistent with the model until the {math}`\mRatE_{t-n}` that is produced goes outside of the pre-defined bounds for solving the problem.

We can merge the points below the steady state with the steady state with the points above the steady state to produce {math}`\overset{\dots}{\star} = \cdots(\pmb{\circ}(-\varepsilon)) \cup \pmb{\circ}(0) \cup \cdots(\pmb{\circ}(\varepsilon))`. These points can then be used to generate appropriate interpolating approximations to the consumption function and other desired functions.

Designate, e.g., the vector of points on the consumption function generated in this manner by {math}`\overset{\dots}{\star}[c]`, so that

```{math}
:label: eq:TBS-cFuncMat

\begin{aligned}
   \{\overset{\dots}{\star}[m],\{\overset{\dots}{\star}[c],\overset{\dots}{\star}[\MPC^{e}],\overset{\dots}{\star}[\MPC^{e\prime}]\}^{\intercal}\}^{\intercal} & =
\begin{pmatrix}
m[1] & \{c[1],\MPC^{e}[1],\MPC^{e\prime}[1]\} \\
m[2] & \{c[2],\MPC^{e}[2],\MPC^{e\prime}[2]\} \\
...  & ...              \\
m[N] & \{c[N],\MPC^{e}[N],\MPC^{e\prime}[N]\} \\
\end{pmatrix}
\end{aligned}
```

where {math}`N` is the number of points that have been generated by the merger of the backward shooting points described above.

The object {eq}`eq:TBS-cFuncMat` is not an arbitrary example; it reflects a set of values that uniquely define a fourth order piecewise polynomial spline such that at every point in the set the polynomial matches the level and first derivative included in the list. Standard numerical mathematics software can produce the interpolating function with this input; for example, the syntax in *Mathematica* is simply

```{math}
\mathtt{cE} = \mathtt{Interpolation}[\{\overset{\dots}{\star}[m],\{\overset{\dots}{\star}[c],\overset{\dots}{\star}[\MPC^{e}],\overset{\dots}{\star}[\MPC^{e\prime}]\}^{\intercal}\}^{\intercal}].
```

which creates a function {math}`\texttt{cE}` that is a {math}`\mathbf{C}^4` interpolating polynomial connecting these points.

The reverse shooting algorithm terminates at some finite maximum point {math}`\bar\mRat`, but for completeness it is useful to have an approximation to the consumption function that is reasonably well behaved for any {math}`\mTarg` no matter how large.[^tbs-extrapolation-approximating-interpolation]

[^tbs-extrapolation-approximating-interpolation]: An extrapolation of the approximating interpolation will not perform well; a polynomial approximation will inevitably "blow up" if evaluated at large enough {math}`\mTarg`.

Since we know that the consumption function in the presence of uncertainty asymptotes to the perfect foresight function, we adopt the following approach. Defining the level of precautionary saving as[^tbs-mnemonic-amount-consumption]

[^tbs-mnemonic-amount-consumption]: Mnemonic: This is the amount of consumption that is cancelled as a result of uncertainty.

```{math}
:label: eq:TBS-pSavFunc

\psavFunc(\mRat) = \bar{\cFunc}(\mRat)-\cFunc(\mRat),
```

we know (see the [appendix on the case where growth exceeds the interest factor](#sec:TBS-PGroGEQRfree) below) that

```{math}
\lim_{\mRat \rightarrow \infty} \psavFunc(\mRat) = 0 .
```

Defining {math}`\vec{\mRat}=m-\bar{\mRat}`, a convenient functional form to postulate for the propensity to precautionary-save is

```{math}
\psavFunc(\mRat) = e^{\phi_{0}-\phi_{1} \vec{\mRat}}+e^{\gamma_{0}-\gamma_{1} \vec{\mRat}}
```

with derivatives

```{math}
\begin{aligned}
    \psavFunc^{\prime}(\mRat) & =  -\phi_{1} e^{\phi_{0}-\phi_{1} \vec{\mRat}} - \gamma_{1} e^{\gamma_{0}-\gamma_{1} \vec{\mRat}}
\\  \psavFunc^{\prime\prime}(\mRat) & =  \phantom{-}\phi_{1}^{2} e^{\phi_{0}-\phi_{1} \vec{\mRat}} + \gamma_{1}^{2} e^{\gamma_{0}-\gamma_{1} \vec{\mRat}}
\\  \psavFunc^{\prime\prime\prime}(\mRat) & =  -\phi_{1}^{3} e^{\phi_{0}-\phi_{1} \vec{\mRat}} - \gamma_{1}^{3} e^{\gamma_{0}-\gamma_{1} \vec{\mRat}}
.
\end{aligned}
```

Evaluated at {math}`\bar{\mRat}` (for which {math}`\psavFunc` and its derivatives will have numerical values assigned by the reverse-shooting solution method described above), this is a system of four equations in four unknowns and, though nonlinear, can be easily solved for values of the {math}`\phi` and {math}`\gamma` coefficients that match the level and first three derivatives of the "true" {math}`\psavFunc` function.[^tbs-exact-symmetry-treatment]

[^tbs-exact-symmetry-treatment]: The exact symmetry in the treatment of {math}`\gamma` and {math}`\phi` means that there will actually be two symmetrical solutions; either can be used.

(sec:TBS-PGroGEQRfree)=
### Modified Formulas For Case Where {math}`\PGro \geq \Rfree`

The text asserts that if {math}`\PGro < \Rfree` the consumption function for a finite-horizon employed consumer approaches the {math}`\bar{\cFunc}_{t}(\mRat)` function that is optimal for a perfect-foresight consumer with the same horizon,

```{math}
\lim_{\mRat \uparrow \infty} \bar{\cFunc}_{t}(\mRat) - \cFunc_{t}(\mRat) = 0 .
```

This proposition can be proven by careful analysis of the consumption Euler equation, noting that as {math}`\mRat` approaches infinity the proportion of consumption will be financed out of (uncertain) labor income approaches zero, and that the magnitude of the precautionary effect is proportional to the square of the proportion of such consumption financed out of uncertain labor income.

A footnote also claims that for employed consumers, {math}`\cFunc(\mRat)` approaches a different, but still well-defined, limit even if {math}`\PGro \geq \Rfree`, so long as the impatience condition holds.

It turns out that the limit in question is the one defined by the solution to a perfect foresight problem with liquidity constraints. A semi-analytical solution does exist in this case, but it requires formidable notation and analysis to present and understand, so the details are not presented here. A continuous-time treatment can be found in {cite:t}`parkLiqConstrContinuous`.

(sec:TBS-MPCatTarget)=
### The Marginal Propensity to Consume at Target Wealth

This appendix is kept for reference. It is not part of the published handout: in the source it follows the end of the document, marked as superseded by the reverse-shooting derivation in the [numerical solution appendix](#sec:TBS-NumericalSolution), and preserved because its derivations are useful for checking.

For any {math}`\mRatE_{t} \neq \mTarg` the marginal propensity to consume can be approximated by

```{math}
\MPCFunc^{e}(\mRatE_{t}) \approx \left(\frac{\Delta {\cRat}^{e}_{t+1}}{\Delta \mRatE_{t+1}}\right)
```

but at the steady state {math}`\mRatE_{\tNow}=\mTarg` both numerator and denominator are zero. We get around this problem using L'Hôpital's rule. Define {math}`\blacktriangle=\mRatE_{t}-\mTarg` and assume that the consumption function can be approximated as

```{math}
\cFunc(\mRatE_{t}) \approx \cTarg^{e} + \blacktriangle_{t} \MPCE
```

where

```{math}
\MPCE \equiv \frac{d \cFunc(\mRatE_{t})}{d \mRatE_{t}} |_{\mRatE_{t}=\mTarg}
```

so that

```{math}
\begin{aligned}
  \blacktriangle_{t+1} & =  (\mTarg + \blacktriangle_{t} -\cFunc(\mTarg+\blacktriangle_{t}))\Rnorm + 1 - \mTarg
\\ & \approx  (\mTarg+\blacktriangle_{t}- (\cTarg^{e}+ \blacktriangle_{t} \MPCE))\Rnorm + 1 - \mTarg
\\ & =  \underbrace{(\mTarg-\cTarg^{e})\Rnorm+1}_{\mTarg} -\mTarg + (1-\MPCE) \Rnorm\blacktriangle_{t}
\\ & =  \underbrace{\left(1-\MPCE\right)}_{\equiv \MPS^{e}}\blacktriangle_{t}\Rnorm
\end{aligned}
```

and note for future use that

```{math}
\Delta \mRatE_{t+1} = \blacktriangle_{t+1} - \blacktriangle_{t}
```

and

```{math}
\left(\frac{\blacktriangle_{t+1}}{\blacktriangle_{t}}\right) = \MPS^{e}\Rnorm
```

while using {eq}`eq:TBS-ctp1Oct` yields

```{math}
:label: eq:TBS-dc

\begin{aligned}
  c_{t+1}& =  {\PatPGro} \left\{1+\urate\left[\left(\frac{\cFunc(\mRatE_{t+1})}{(\mRatE_{t}-\cFunc(\mRatE_{t}))\Rnorm\MPC}\right)^{\CRRA}-1\right]\right\}^{1/\CRRA}c_{t}
\\ \Delta c_{t+1} & \approx  {\PatPGro} \left\{1+\urate\left[\left(\frac{\cTarg^{e}+\MPCE \blacktriangle_{t+1} }{\cTarg^{u}(1 +\blacktriangle_{t}\MPS^{e} \Rnorm \MPC/\cTarg^{u})}\right)^{\CRRA}-1\right]\right\}^{1/\CRRA}c_{t}-c_{t}
\\ & =  \left[{\PatPGro} \left\{1+\urate\left[\left(\left(\frac{\cTarg^{e}}{\cTarg^{u}}\right)\left(\frac{1+\MPCE \blacktriangle_{t}\MPS^{e}\Rnorm/\cTarg^{e} }{1 +\blacktriangle_{t}\MPS^{e} \Rnorm \MPC/\cTarg^{u}}\right)\right)^{\CRRA}-1\right]\right\}^{1/\CRRA}-1\right] (\cTarg^{e}+\blacktriangle_{t})
\\ \Delta c_{t+1} & \approx  \left[{\PatPGro} \left\{1+\urate\left[\left(\left(\frac{\cTarg^{e}}{\cTarg^{u}}\right)\left(1+\MPCE \blacktriangle_{t}\MPS^{e} \Rnorm/\cTarg^{e} -\blacktriangle_{t}\MPS^{e} \Rnorm \MPC/\cTarg^{u}\right)\right)^{\CRRA}-1\right]\right\}^{1/\CRRA}-1\right] c_{t}
\\  & =  \left[{\PatPGro} \left\{1+\urate\left[(\cTarg^{e}/\cTarg^{u})^{\CRRA}\left(1+ \blacktriangle_{t}\MPS^{e} \Rnorm (\MPCE/\cTarg^{e} - \MPC/\cTarg^{u})\right)^{\CRRA}-1\right]\right\}^{1/\CRRA}-1\right] c_{t}
\\  & =  \left[{\PatPGro} \left\{1+\urate\left[(\cTarg^{e}/\cTarg^{u})^{\CRRA}-1\right]+\urate(\cTarg^{e}/\cTarg^{u})^{\CRRA}\CRRA \blacktriangle_{t}\MPS^{e} \Rnorm (\MPCE/\cTarg^{e} - \MPC/\cTarg^{u})\right\}^{1/\CRRA}-1\right] c_{t}
\\  & \approx  \left[\underbrace{{\PatPGro} \left\{1+\urate\left[(\cTarg^{e}/\cTarg^{u})^{\CRRA}-1\right]\right\}}_{=1}(1+\PatPGro^{-1}\urate(\cTarg^{e}/\cTarg^{u})^{\CRRA}\blacktriangle_{t}\MPS^{e} \Rnorm (\MPCE/\cTarg^{e} - \MPC/\cTarg^{u})-1\right] c_{t}
\\  & =  \left[\PatPGro^{-1}\urate(\cTarg^{e}/\cTarg^{u})^{\CRRA}\blacktriangle_{t}\MPS^{e} \Rnorm (\MPCE/\cTarg^{e} - \MPC/\cTarg^{u})\right] c_{t}
\end{aligned}
```

so that

```{math}
\begin{aligned}
  \lim_{\blacktriangle_{t} \rightarrow 0} \left(\frac{\Delta c_{t+1}}{\Delta m_{t+1}}\right) & =  \left(\frac{\left[\PatPGro^{-1}\urate(\cTarg^{e}/\cTarg^{u})^{\CRRA}\MPS^{e} \Rnorm (\MPCE/\cTarg^{e} - \MPC/\cTarg^{u})\right] \cTarg^{e}}{(1-\MPCE)\Rnorm-1}\right)
\\  \MPCE \PatPGro & =  \left(\frac{\left[\urate(\cTarg^{e}/\cTarg^{u})^{\CRRA}\MPS^{e} \Rnorm (\MPCE/\cTarg^{e} - \MPC/\cTarg^{u})\right] \cTarg^{e}}{(1-\MPCE)\Rnorm-1}\right)
\\  \MPCE \PatPGro \left((1-\MPCE)\Rnorm-1\right) & =  \urate(\cTarg^{e}/\cTarg^{u})^{\CRRA}(1-\MPCE) \Rnorm (\MPCE/\cTarg^{e} - \MPC/\cTarg^{u}) \cTarg^{e}
\end{aligned}
```

which is a quadratic equation in {math}`\MPCE`. This equation has only one solution inside the unit interval, which will be the MPC at {math}`\mTarg`.

Note that an alternative approach would be to define {math}`\Delta \cTarg^{e}` using the RHS of {eq}`eq:TBS-dc` and {math}`\Delta \mTarg = (\MPS^{e} \Rnorm - 1)\blacktriangle_{t}` and to use a numerical rootfinding routine to locate the {math}`\hat{\MPC}^{e}` that solves

```{math}
\hat{\MPCFunc}^{e}(\blacktriangle_{t}) = \left(\frac{\Delta \cTarg^{e}}{\Delta \mTarg}\right)
```

using {math}`\MPCE` as the starting point for the numerical search. This approach has the virtue that it can produce estimates of the MPC at points near but not equal to the target level of wealth. (We will use this below).

Differentiating {eq}`eq:TBS-naturalMPC`, dropping arguments, and evaluating at the steady state yields[^tbs-eta-undefined]

[^tbs-eta-undefined]: The source does not define {math}`\eta`; the derivation is reproduced as it stands there.

```{math}
\begin{aligned}
  \MPC^{e\prime} & =  -\eta\MPC^{e\prime} (\erate \MPCE+\urate (\cTarg^{u}/\cTarg^{e})^{-\CRRA-1} \MPC)
\\ &  + \eta  (1-\MPCE)^{2}\Rnorm (\cTarg^{e})^{\CRRA+1}(-\CRRA-1)(\erate  \MPCE + \urate (\cTarg^{u})^{-\CRRA-2} \MPC)
\\ &  + \eta  (1-\MPCE)^{2}\Rnorm (\cTarg^{e})^{\CRRA}(\CRRA+1)(\erate  \MPCE + \urate (\cTarg^{u})^{-\CRRA-1} \MPC)
\\ &  + \eta  (1-\MPCE)\erate \MPC^{e\prime}
\\ \MPC^{e\prime} & =  \left(\frac{\eta  (1-\MPCE)^{2}\Rnorm \left( (\cTarg^{e})^{\CRRA+1}(-\CRRA-1)(\erate  \MPCE + \urate (\cTarg^{u})^{-\CRRA-2} \MPC)+(\cTarg^{e})^{\CRRA}(\CRRA+1)(\erate  \MPCE + \urate (\cTarg^{u})^{-\CRRA-1} \MPC) \right)
}{1+\eta (\erate \MPCE+\urate (\cTarg^{u}/\cTarg^{e})^{-\CRRA-1} \MPC)- \eta  (1-\MPCE)\erate}\right)
\end{aligned}
```
