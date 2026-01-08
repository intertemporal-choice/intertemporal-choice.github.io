(sec:C-With-Optimal-Portfolio)=

# Consumption with Optimal Portfolio Choice

The [](#sec:CRRA-RateRisk) shows that for a {cite:t}`merton:restat`-{cite:t}`samuelson:portfolio` consumer facing return {math}`\log \RiskyAlt_{t+1} \sim \mathcal{N}(\riskyAlt - \sigma^{2}_{\riskyAlt}/2,\sigma^{2}_{\riskyAlt})` on the only financial asset available, the optimal marginal propensity to consume is approximately

```{math}
:label: eq:MPC

\MPC \approx {\riskyAlt}-\CRRA^{-1}(\riskyAlt-\DiscRate) - (\CRRA-1)\left(\sigma_{\riskyAlt}^{2}/2\right)
```

:::{exercise}
:label: ex:unavoidable-risk
1. Use this equation to discuss the parametric restriction(s) under which an increase in unavoidable financial risk {math}`\sigma_{\riskyAlt}^{2}/2` will cause a (precautionary) decline in consumption (the risk is unavoidable because we have assumed the risky asset is the only financial asset available). Explain whether, under such parameter value(s), the income effect of an increase in {math}`\riskyAlt` outweighs the substitution effect, *and explain in words the intuition for both the income effect and the substitution effect.*

:::

:::{solution} ex:unavoidable-risk
:class: dropdown
The restriction is {math}`\CRRA>1`, which guarantees that an increase in {math}`\sigma_{\riskyAlt}^{2}` reduces {math}`\MPC`. Under this restriction, the income effect outweighs the substitution effect. For a discussion of the two effects, see [](#sec:PerfForesightCRRA).
:::

where the precautionary effect of financial risk on the MPC is captured by the {math}`-(\CRRA-1)\left(\sigma_{\riskyAlt}^{2}/2\right)` term. Since {math}`\CRRA > 1` by assumption, this equation yields the plausible conclusion that an increase in *unavoidable* financial risk {math}`\sigma_{\riskyAlt}^{2}` reduces the level of consumption.

:::{exercise}
:label: ex:consumer-choice
For the remainder of the question, assume that the consumer
:::

We are interested here in understanding how the results change when the consumer

can choose how much to invest in the risky asset, so that financial risk can be avoided by reducing the share of the portfolio allocated to the risky asset. The [](#sec:Portfolio-CRRA) derives the portfolio share {math}`\riskyshare` that an optimizing consumer will invest in a risky asset earning return {math}`\log \RiskyAlt_{t+1} \sim \mathcal{N}(\riskyAlt - \sigma^{2}_{\riskyAlt}/2,\sigma^{2}_{\riskyAlt})` -- so that {math}`\log \RiskyAlt = \riskyAlt` (where the subscriptless version of a variable denotes its expectation unless otherwise noted, e.g. {math}`\RiskyAlt \equiv \Ex_{t}[\RiskyAlt_{t+1}]`.[^footnote-lognormal]

[^footnote-lognormal]: (See fact [LogMeanMPS](#fact:logmeanmps), and note that {math}`\RiskyAlt=\Risky` under the given assumptions; that is, an increase in the degree of risk {math}`\sigma^{2}_{\riskyAlt}` does not change the expected return factor in levels). Note that the subscriptless version of the log of the risky return, {math}`\riskyAlt_{t+1}`, is *not* equal to its mean: {math}`\Ex_{t}[\riskyAlt_{t+1}] = \riskyAlt-\sigma^{2}_{\riskyAlt}/2`.

The remaining proportion {math}`(1-\riskyshare)` of the portfolio earns a riskless return {math}`\rfree = \log \Rfree`,[^riskfree-notation] and we write the log expected return premium factor as {math}`\EPrem \equiv \RiskyAlt/\Rfree` with log expected return premium {math}`\EpremLog \equiv \log \EPrem = \riskyAlt-\rfree = \log \RiskyAlt/\Rfree`; optimal choice of {math}`\riskyshare` yields a portfolio whose realized return factor is written {math}`\Rport`

[^riskfree-notation]: The bold font is used for the risky return and the narrow font for the safe return.

and the log of whose realization is well approximated by[^approximation-quality]

[^approximation-quality]: See [](#sec:Portfolio-CRRA) for a figure examining the quality of the approximation.

```{math}
:label: eq:portLogPrem

\begin{aligned}
\rport_{t+1}-\rfree & \approx \riskyshare \overbrace{(\riskyAlt_{t+1}-\rfree)}^{\equiv \EpremLog_{t+1}} + \riskyshare(1-\riskyshare)\sigma^{2}_{\riskyAlt}/2 \\
& = \riskyshare (\riskyAlt_{t+1}-\rfree+\sigma^{2}_{\riskyAlt}/2) - \riskyshare^{2} \sigma^{2}_{\riskyAlt}/2,
\end{aligned}
```

whose variance (using facts [SumNormsIsNorm](#fact:sumnormsisnorm) and [NormTimes](#fact:normtimes)) is

```{math}
:label: eq:rportVar

\sigma^{2}_{\rport} = \riskyshare^{2} \sigma^{2}_{\riskyAlt},
```

and since {math}`\Ex_{t}[\riskyAlt_{t+1}]=\riskyAlt-\sigma^{2}_{\riskyAlt}/2` the expectation of {eq}`eq:portLogPrem` will be

```{math}
\begin{aligned}
\Ex_{t}[\rport_{t+1}-\rfree] & \approx (\riskyAlt- \sigma^{2}_{\riskyAlt}/2 - \rfree + \sigma^{2}_{\riskyAlt}/2)\riskyshare-\riskyshare^{2}\sigma^{2}_{\riskyAlt}/2 \\
& = \EpremLog \riskyshare -\riskyshare^{2}\sigma^{2}_{\riskyAlt}/2
\end{aligned}
```

so that, using fact [SumNormsIsNorm](#fact:sumnormsisnorm),

```{math}
:label: eq:CwOP-rportDist

\rport_{t+1}-\rfree \sim \mathcal{N}(\EpremLog \riskyshare -\riskyshare^{2}\sigma^{2}_{\riskyAlt}/2,\riskyshare^{2}\sigma^{2}_{\riskyAlt})
```

yielding, using fact [LogELogNormTimes](#fact:logelognormtimes),

```{math}
:label: eq:LogERport

\log \Rport \equiv \log \Ex_{t}[\Rport_{t+1}] = \riskyshare \EpremLog + \rfree
```

and the [](#sec:Portfolio-CRRA) shows that under these circumstances the optimal risky portfolio share is well approximated by

```{math}
:label: eq:CwOP-riskyshareMS

\riskyshare \approx \left(\frac{\EpremLog}{\CRRA \sigma^{2}_{\riskyAlt}}\right)
```

:::{exercise}
while the variance of the return on the optimally-chosen risky portfolio is approximately

```{math}
:label: eq:rportVarExam

\sigma^{2}_{\rport} = \riskyshare^{2} \sigma^{2}_{\riskyAlt}.
```
:::

:::{exercise}
:label: ex:precautionary-effect
2. Show that the precautionary effect of rate-of-return risk on the precautionary contribution to the MPC, after taking account of optimal portfolio adjustment, is

```{math}
:label: eq:PrecEffect

-(\CRRA-1)\left(\frac{(\EpremLog/\CRRA)^{2}}{2 \sigma_{\riskyAlt}^{2}}\right)
```

and explain the intuition for the result that the size of the precautionary effect *shrinks* as the risk grows larger.
:::

:::{solution} ex:precautionary-effect
:class: dropdown

so that substituting from {eq}`eq:CwOP-riskyshareMS` and {eq}`eq:rportVar`, the precautionary effect on consumption after taking account of optimal portfolio adjustment is

```{math}
\begin{aligned}
-(\CRRA-1)\left(\sigma_{\rport}^{2}/2\right) & = -(\CRRA-1)\left(\frac{\riskyshare^{2}\sigma_{\riskyAlt}^{2}}{2}\right) \\
& = -(\CRRA-1)\left(\frac{(\EpremLog/\CRRA)^{2}}{2 \sigma_{\riskyAlt}^{2}}\right)
\end{aligned}
```

The way to understand this is to break down the response to the increase in riskiness into two components. The first is the direct precautionary effect examined in the [](#sec:CRRA-RateRisk), which works in the way intuition suggests (more risk implies lower consumption); the second effect is the "portfolio rebalancing" effect, examined in the [](#sec:Portfolio-CRRA): An increase in riskiness makes the consumer choose to invest less in the risky asset. What {eq}`eq:PrecEffectRaw` tells us is that the consumer's "flight from risk" is so effective in reducing riskiness (because the portfolio share {math}`\riskyshare` enters as a *squared* term in {eq}`eq:PrecEffectRaw`) that the riskiness of the *portfolio* actually *declines* as the riskiness of the risky asset increases. (This result was also derived in the [](#sec:Portfolio-CRRA)). Now the overall reduction in consumption coming through the precautionary term makes sense: Precautionary saving is less than before *because the consumer optimally chooses less exposure to risk* than before.
:::

so that substituting from {eq}`eq:CwOP-riskyshareMS` and {eq}`eq:rportVar`, the precautionary effect after taking account of optimal portfolio adjustment is

```{math}
:label: eq:PrecEffectRaw

\begin{aligned}
-(\CRRA-1)\left(\sigma_{\rport}^{2}/2\right) & = -(\CRRA-1)\left(\frac{\riskyshare^{2}\sigma_{\riskyAlt}^{2}}{2}\right) \\
& = -(\CRRA-1)\left(\frac{(\EpremLog/\CRRA)^{2}}{2 \sigma_{\riskyAlt}^{2}}\right)
\end{aligned}
```

which says that (for {math}`\CRRA>1`) the absolute size of the precautionary term *shrinks* as the risk grows larger. To put it another way, when {math}`\CRRA>1` an *increase* in the riskiness of the risky asset causes consumption to *rise*. At first, this seems bizarre: Intuition suggests that in reality people *cut back* on consumption in the face of greater risk. The resolution is that the consumer's "flight from risk" is so effective in reducing riskiness (because the portfolio share {math}`\riskyshare` enters as a *squared* term in {eq}`eq:PrecEffectRaw`) that the riskiness of the *portfolio* actually *declines* as the riskiness of the risky asset increases.

:::{exercise}
:label: ex:mpc-exogenous
3. Now use the foregoing results to show that the MPC {math}`\MPC` can be rewritten in terms of exogenous parameters (including the riskfree interest factor {math}`\rfree`) as

```{math}
\MPC \approx \rfree-\CRRA^{-1}(\rfree-\DiscRate)+ (\CRRA-1)\left(\frac{(\EpremLog/\CRRA)^{2}}{2 \sigma_{\riskyAlt}^{2}}\right)
```

and use this equation to explain why the total effect of an increase in risk on consumption is *positive* and *explain why this result comes about.*
:::

:::{solution} ex:mpc-exogenous
:class: dropdown

See the derivation above for the result and the logic.
:::

The fact that precautionary saving diminishes when risk is larger does not, by itself, tell us whether consumption increases in response to an increase in risk; in addition to the precautionary channel, the MPC is also affected by the decline in the portfolio's expected rate of return that results from the consumer's choice to invest less in the high-expected-return risky asset and more in the low-return safe asset. Substituting {eq}`eq:CwOP-riskyshareMS` into {eq}`eq:LogERport` indicates that the log of the expected portfolio excess return factor becomes

```{math}
\log \Rport/\Rfree \equiv \log \Ex_{t}[\Rport_{t+1}/\Rfree] = \frac{\EpremLog^{2}}{\CRRA \sigma^{2}_{\riskyAlt}}
```

so an increase in {math}`\sigma^{2}_{\riskyAlt}` can have quite a powerful effect in reducing the consumer's expected portfolio return.

As with the change in the riskfree rate analyzed in the [](#sec:PerfForesightCRRA), this change in the portfolio return has two consequences: An income and a substitution effect, captured respectively by the first and second terms of {eq}`eq:MPC`. Substituting {math}`\rport = \EpremLog^{2}/\CRRA \sigma^{2}_{\riskyAlt}+\rfree` and {math}`\sigma_{\rport}^{2}=(\EpremLog/\CRRA)^2/\sigma_{\riskyAlt}^{2}` into {eq}`eq:MPC` yields

```{math}
:label: eq:MPCsub

\begin{aligned}
\MPC & \approx {\rport}-\CRRA^{-1}(\rport-\DiscRate) - (\CRRA-1)\left(\sigma_{\rport}^{2}/2\right) \\
& = \CRRA^{-1}\DiscRate+{\rport}(1-\CRRA^{-1}) - (\CRRA-1)\left(\frac{(\EpremLog/\CRRA)^{2}}{2 \sigma_{\riskyAlt}^{2}}\right) \\
& = \CRRA^{-1}\DiscRate+(\rfree+\EpremLog^{2}/\CRRA \sigma^{2}_{\riskyAlt})(1-\CRRA^{-1}) - (\CRRA-1)\left(\frac{(\EpremLog/\CRRA)^{2}}{2 \sigma_{\riskyAlt}^{2}}\right) \\
& = \rfree-\CRRA^{-1}(\rfree-\DiscRate)+\underbrace{(\CRRA-1)(\EpremLog^{2}/\CRRA^{2} \sigma^{2}_{\riskyAlt})}_{\text{net inc and sub effect}} - (\CRRA-1)\left(\frac{(\EpremLog/\CRRA)^{2}}{2 \sigma_{\riskyAlt}^{2}}\right)
.
% & = \rfree-\CRRA^{-1}(\rfree-\DiscRate)+ (\CRRA-1)\left(\frac{(\EpremLog/\CRRA)^{2}}{2 \sigma_{\riskyAlt}^{2}}\right)
\end{aligned}
```

Thus, for {math}`\CRRA > 1` the income effect outweighs the substitution effect so that when an increase in financial risk causes consumers to shy away from the risky asset the reduction in consumption from the drop in income ("the income effect") is larger than the increase in consumption from the lowering of the incentive to delay consumption ("the substitution effect").

Note, finally, that the net of the income and substitution effects is (remarkably) of exactly the same functional form as the precautionary effect, but of opposite sign and twice as large. So the combination of all three effects (income, substitution, precautionary) yields:

```{math}
\MPC \approx \rfree-\CRRA^{-1}(\rfree-\DiscRate)+ (\CRRA-1)\left(\frac{(\EpremLog/\CRRA)^{2}}{2 \sigma_{\riskyAlt}^{2}}\right)
```

and we can see that the overall effect of the increase in financial risk is to reduce the marginal propensity to consume because the net of the income and substitution effects channels outweighs the precautionary effect (see the [](#sec:PerfForesightCRRA) for a refresher on income and substitution effects, as well as human wealth effects (which are absent here but could easily be added by giving the consumer an expected stream of future noncapital income)).

{numref}`fig:CwOP-MPCvsSigma` confirms, both using the approximate formulas derived above and using a numerically exact solution, that the MPC declines as risk increases.

:::{exercise}
:label: ex:saving-effect
4. Now show that the effect of an increase in risk on saving is given by

```{math}
\rport - \MPC = \CRRA^{-1}(\rfree-\DiscRate) + \left(\frac{\CRRA+1}{2}\right)\left(\frac{\EpremLog^{2}}{\sigma^{2}_{\riskyAlt}\CRRA^{2}}\right)
```

and *explain how this result relates to the results obtained earlier*. Comment, in particular, on the role played by our assumption that the consumer has no labor income (Hint: What further effect of interest rates is omitted when the consumer has no labor income?)
:::

:::{solution} ex:saving-effect
:class: dropdown

See the discussion above.
:::

Finally, in addition to the effects on consumption, we are interested in the effects on saving. Since saving is income minus consumption, this means we need to know the effects on income. But income for our consumer is entirely from his portfolio investments, so the income effect is captured simply by {math}`\rport`. The "saving effect" is therefore captured by

```{math}
\begin{aligned}
\rport - \MPC & \approx \CRRA^{-1}(\rport-\DiscRate)+(\CRRA-1)\left(\frac{(\EpremLog/\CRRA)^{2}}{2 \sigma_{\riskyAlt}^{2}}\right) \\
& = \CRRA^{-1}\left(\frac{\EpremLog^{2}}{\CRRA \sigma^{2}_{\riskyAlt}}+\rfree-\DiscRate\right)+(\CRRA-1)\left(\frac{(\EpremLog/\CRRA)^{2}}{2 \sigma_{\riskyAlt}^{2}}\right) \\
& = \CRRA^{-1}(\rfree-\DiscRate) + \frac{\EpremLog^{2}}{\CRRA^{2} \sigma^{2}_{\riskyAlt}}+(\CRRA-1)\left(\frac{(\EpremLog/\CRRA)^{2}}{2 \sigma_{\riskyAlt}^{2}}\right) \\
& = \CRRA^{-1}(\rfree-\DiscRate) + \frac{\EpremLog^{2}/\CRRA^{2}}{ \sigma^{2}_{\riskyAlt}}+(\CRRA-1)\left(\frac{(\EpremLog/\CRRA)^{2}}{2 \sigma_{\riskyAlt}^{2}}\right) \\
& = \CRRA^{-1}(\rfree-\DiscRate) + \left(\frac{\CRRA+1}{2}\right)\left(\frac{\EpremLog^{2}}{\sigma^{2}_{\riskyAlt}\CRRA^{2}}\right)
\end{aligned}
```

which indicates that an increase in the riskiness of the financial asset will reduce net saving; although the increase in risk diminishes consumption, the decline in expected income from the decline in the consumer's investment in the high-return asset is greater, and so expected saving declines despite the decline in consumption. It is worth emphasizing again, though, that this decline in saving is *not* properly called a precautionary saving effect; it is a consequence of the portfolio rebalancing which actually reduces the size of the precautionary effect. It would be confusing to refer to this simply as a precautionary effect, when in fact the ultimate outcome (increased saving) depends also on portfolio rebalancing, income, and substitution effects. This can be seen most clearly in the case of logarithmic utility, where the precautionary effect is precisely zero (see the discussion in the [](#sec:Portfolio-CRRA)), yet the portfolio and other effects exist and still generate the conclusion that the increase in risk increases saving.

This analysis has been entirely in partial equilibrium. General equilibrium considerations (which arise, for example, in attempting to use models of this kind to understand global imbalances) complicate the picture further. In particular, consumers' efforts to flee the risky asset result in a lower equilibrium price for that asset (and a correspondingly higher price for the riskless asset, and therefore a lower riskfree rate). This induces yet a *third* round of responses to the increase in risk.

A final important observation is that the assumption that the consumer has no labor income means that perhaps the largest "classical" effect of interest rates on consumption and saving is entirely omitted from the analysis here: The human wealth effect. (See {cite:t}`summersCapTax` for a statement of the argument that the human wealth effect of interest rates is likely in practice to be much larger than the income and substitution effects.) The general equilibrium decline in riskfree rates attendant upon an increase in riskiness of the risky asset should boost human wealth, increase consumption, and reduce saving. For careful and insightful treatments of the general equilibrium problem, see {cite:t}`paEntrep` and {cite:t}`corneliImbalances`.

:::{figure} /content/asset_pricing/C-With-Optimal-Portfolio/LaTeX/Figures/MPCApproxVsExactVsSigma.png
:name: fig:CwOP-MPCvsSigma

MPC as a Function of {math}`\sigma` Calculated Using (Numerically) Exact and Approximate Methods
:::
