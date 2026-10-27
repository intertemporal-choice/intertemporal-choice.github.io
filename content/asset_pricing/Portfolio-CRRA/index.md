(sec:Portfolio-CRRA)=
# Portfolio Choice with CRRA Utility (Merton-Samuelson)

{cite:t}`merton:restat` and {cite:t}`samuelson:portfolio` study the optimal portfolio choice of a consumer with constant relative risk aversion {math}`\CRRA`.[^fn-utility] This consumer has assets at the end of period {math}`t` equal to {math}`a_{t}` and is deciding how much to invest in a risky asset[^fn-multi-asset] with a lognormally distributed return factor {math}`\Risky_{t+1}`, whose log is

[^fn-utility]: {math}`\uFunc(\cRat) = (1-\CRRA)^{-1}\cRat^{1-\CRRA}`.

[^fn-multi-asset]: Both papers present the solution in the case with multiple risky assets; for the two-asset case, see [two risky assets](#sec:Portfolio-Multi-CRRA).

```{math}
\risky_{t+1} = \risky+\ShkMeanOneLog_{t+1}, \qquad \ShkMeanOneLog_{t+1} \sim \mathcal{N}(-\sigma^{2}_{\risky}/2,\sigma^{2}_{\risky}).
```

The shock is mean-one in levels, {math}`\Ex_{t}[e^{\ShkMeanOneLog_{t+1}}]=1` (see [ELogNormMeanOne](#fact:elognormmeanone)), so {math}`\risky` is the log of the expected return factor, {math}`\Ex_{t}[\Risky_{t+1}]=e^{\risky}=\Risky` (upper-case variables like {math}`\Risky` without a subscript are time-invariant means), while the mean of the log return is {math}`\Ex_{t}[\risky_{t+1}]=\risky-\sigma^{2}_{\risky}/2`.

The alternative to the risky asset is a riskfree asset that earns return factor {math}`\Rfree=e^{\rfree}`. Importantly, the consumer is assumed to have no labor income and to face no risk except from the investment in the risky asset.[^fn-retired-investor][^fn-riskless-income]

[^fn-retired-investor]: A common interpretation is that this is the problem of a retired investor who expects to receive no further labor income. Note however that all risks other than the returns from financial investments have been ruled out; for example, health expense risk is not possible in this model, though recent research has argued such risk is important (maybe even dominant) later in life (cf. {cite:t}`aclvJoy`).

[^fn-riskless-income]: Riskless labor income can trivially be added to the problem, because its risklessness means that (in the absence of liquidity constraints) it is indistinguishable from a lump sum of extra current wealth with a value equal to the present discounted value (using the riskless rate) of the (riskless) future labor income. Of course, in practice, labor income is not riskless, but when labor income is risky the problem no longer has the tidy analytical solution described here and must be solved numerically. See {cite:t}`SolvingMicroDSOPs` for an introduction to numerical solution methods.

Both papers consider a multiperiod optimization problem, but here we examine a consumer for whom period {math}`t` is the second-to-last period of life (the insights, and even the formulas, carry over to the multiperiod case).[^fn-samuelson-multi]

[^fn-samuelson-multi]: {cite:t}`samuelson1979we`.

If the period-{math}`t` consumer invests proportion {math}`\riskyshare` in the risky asset, spending all available resources in the last period of life {math}`t+1` will yield:

```{math}
:label: eq:PortCRRA-RportDef

\begin{gathered}\begin{aligned}
        c_{t+1} & =  \left(\Rfree(1-\riskyshare)+\Risky_{t+1}\riskyshare\right)a_{t}
\\ & =  \underbrace{\left(\Rfree+(\Risky_{t+1}-\Rfree)\riskyshare\right)}_{\equiv \Rport_{t+1}}a_{t}
\end{aligned}\end{gathered}
```

where {math}`\Rport_{t+1}` is the realized arithmetic return factor for the portfolio.

The optimal portfolio share will be the one that maximizes expected utility:

```{math}
\begin{gathered}\begin{aligned}
  \varsigma & =  \argmax_{\varsigma} \Ex_{t}[\uFunc(c_{t+1})]
\end{aligned}\end{gathered}
```

and can be calculated numerically for any distribution of returns.

{cite:t}`cvAppendix` point out that if we define the realized log excess return

```{math}
:label: eq:eprem

\begin{gathered}\begin{aligned}
  \EpremLog_{t+1} & =  \risky_{t+1}-\rfree
\end{aligned}\end{gathered}
```

whose mean is {math}`\EpremLog-\sigma^{2}_{\risky}/2`, where {math}`\EpremLog \equiv \log \EPrem = \risky-\rfree` is the log of the expected excess return factor {math}`\EPrem \equiv \Risky/\Rfree`, then for many distributions a good approximation to the log of the portfolio's return factor is obtained by[^fn-appendix-details]

[^fn-appendix-details]: See [The Campbell-Viceira Approximation](#Campbell-Viceira-Approximation).

```{math}
:label: eq:rportCV

\begin{gathered}\begin{aligned}
  \rport_{t+1} & =  \rfree+ \riskyshare \EpremLog_{t+1}+\riskyshare \sigma^{2}_{\risky}/2 - \riskyshare^{2}\sigma^{2}_{\risky}/2
\end{aligned}\end{gathered}
```

Using this approximation, the expectation as of date {math}`t` of utility at date {math}`t+1` is:

```{math}
:label: eq:PortCRRA-exputil

\begin{split}
  \Ex_{t}[\uFunc(c_{t+1})] & \approx  (1-\CRRA)^{-1}\Ex_{t}\left[\left(a_{t}e^{\rfree}e^{\riskyshare \EpremLog_{t+1}+\riskyshare(1-\riskyshare)\sigma^{2}_{\risky}/2 }\right)^{1-\CRRA}\right]
\\                      & =  (1-\CRRA)^{-1}\Ex_{t}\left[(a_{t}\Rfree)^{1-\CRRA}\left( e^{\riskyshare \EpremLog_{t+1}+\riskyshare(1-\riskyshare)\sigma^{2}_{\risky}/2 }\right)^{1-\CRRA}\right]
\\                      & =  (1-\CRRA)^{-1}(a_{t}\Rfree)^{1-\CRRA}\Ex_{t}\left[e^{(\riskyshare \EpremLog_{t+1}+\riskyshare(1-\riskyshare)\sigma^{2}_{\risky}/2)  (1-\CRRA)}\right]
\\                      & =  \underbrace{(1-\CRRA)^{-1}(a_{t}\Rfree)^{1-\CRRA}}_{\text{constant $< 0$}}\underbrace{e^{ (1-\CRRA)\riskyshare(1-\riskyshare)\sigma^{2}_{\risky}/2}\Ex_{t}\left[e^{\riskyshare \EpremLog_{t+1}  (1-\CRRA)}\right]}_{\text{excess return utility factor}}
\end{split}
```

where the first term is a negative constant under the usual assumption that relative risk aversion {math}`\CRRA>1`.

Because the return is lognormal, we can make substantial further progress, by obtaining an analytical approximation to the numerical optimum. In this case {math}`\riskyshare (1-\CRRA) \EpremLog_{t+1} \sim \mathcal{N}(\riskyshare (1-\CRRA)(\EpremLog - \Evarr/2),(\riskyshare(1-\CRRA))^{2}\Evarr)` (using [NormTimes](#fact:normtimes)). With a couple of extra lines of derivation we can show that the log of the expectation in {eq}`eq:PortCRRA-exputil` is

```{math}
:label: eq:PortCRRA-Ex

\begin{split}
  \log \Ex_{t}\left[e^{\riskyshare \EpremLog_{t+1}  (1-\CRRA)}\right] & =  {(1-\CRRA)\riskyshare \EpremLog-(1-\CRRA)\riskyshare\Evarr/2+ ((1-\CRRA)\riskyshare)^{2}\Evarr/2}
\\  & =  {(1-\CRRA)\riskyshare \EpremLog-(1-\CRRA)\riskyshare(1-\riskyshare(1-\CRRA))\Evarr/2}
\\  & =  {(1-\CRRA)\riskyshare \EpremLog-(1-\CRRA)\riskyshare(1-\riskyshare)\Evarr/2-\CRRA (1-\CRRA)\riskyshare^{2}\Evarr/2}
\end{split}
```

Substitute from {eq}`eq:PortCRRA-Ex` for the log of the expectation in {eq}`eq:PortCRRA-exputil` and note that the resulting expression simplifies because it contains {math}`{(1-\CRRA)\riskyshare(1-\riskyshare)\Evarr/2-(1-\CRRA)\riskyshare(1-\riskyshare)\Evarr/2}=0`; thus the log of the "excess return utility factor" in {eq}`eq:PortCRRA-exputil` is

```{math}
-(\CRRA-1)\riskyshare \EpremLog - (\CRRA-1)(- \CRRA \riskyshare^{2}\Evarr/2)
```

and the {math}`\riskyshare` that minimizes the log will also minimize the level; minimizing this when {math}`\CRRA>1` is equivalent to maximizing the terms multiplied by {math}`-(\CRRA-1)`, so our problem reduces to

```{math}
\begin{gathered}\begin{aligned}
\max_{\riskyshare}~~ \riskyshare \EpremLog -\CRRA\riskyshare^{2}\Evarr/2
\end{aligned}\end{gathered}
```

(riskyshareMS)=
with FOC

```{math}
:label: eq:PortCRRA-riskyshareMS

\begin{gathered}\begin{aligned}
         \EpremLog-\riskyshare\CRRA\Evarr  & =  0  \\
\riskyshare & =  \left(\frac{\EpremLog}{\CRRA \Evarr}\right)
\end{aligned}\end{gathered}
```

Equation {eq}`eq:PortCRRA-riskyshareMS` says[^fn-cv-difference] that the consumer allocates a higher proportion of their net worth to the high-risk, high-return asset when

[^fn-cv-difference]: This expression differs slightly from that derived by {cite:t}`cvAppendix`, because we adjust the mean logarithmic return of the risky investment for its variance in order to keep the mean return factor constant for different values of the variance (cf. {eq}`eq:eprem`), which makes comparisons of alternative levels of risk more transparent.

1. the amount {math}`\EpremLog` by which the risky asset's return exceeds the riskless return is greater
2. the consumer is less risk averse ({math}`\CRRA` is lower)
3. riskiness {math}`\sigma^{2}_{\risky}` is less

If there is no excess return, nothing will be put in the risky asset. Similarly, if risk aversion or the variance of the risk is infinity, again nothing will be put in the risky asset.[^fn-approx-quality]

[^fn-approx-quality]: [](#fig:ShareApproxErr) shows the quality of the approximation.

This formula hints at the existence of an "equity premium puzzle" ({cite:t}`mehraPrescottPuzzle`). Interpreting the risky asset as the aggregate stock market, the annual standard deviation of the log of U.S. stock returns has historically been about {math}`\sigma_{\risky}=0.2` yielding {math}`\Evarr = 0.04`. The equity premium over historical periods has been something like {math}`\EpremLog = 0.08` (eight percent). With risk aversion of {math}`\CRRA=2` this formula implies that the share of risky assets in your portfolio should be {math}`0.08/0.08` or 100 percent! The fact that most people hold far less than 100 percent of their wealth in stocks, and that many hold none, is the "stockholding puzzle," the microeconomic manifestation of the equity premium puzzle ({cite:t}`haliassos&bertaut:fewholdstocks`).

To avoid the problems caused by a prediction of a risky portfolio share greater than one, we can calibrate the model with more modest expectations for the equity premium. Taking evidence from other countries and longer periods into account, {cite:t}`dimson&marsh&staunton:smallerpuzzle` estimate that investors can expect a premium of about 3 to 3½ percent on a geometric basis, or 4½ to 5 percent on the arithmetic basis that matches {math}`\EpremLog`. [](#fig:ShareVsCRRA) shows the relationship between the portfolio share and relative risk aversion for a deliberately modest premium of 3 percent and a large standard deviation of {math}`\sigma=0.2`. Even when risks are this high and the premium is this low, if relative risk aversion is close to logarithmic ({math}`\CRRA = 1`) the investor wants to put well over half of the portfolio in the risky asset. Only for values of risk aversion greater than 2 does the predicted portfolio share reach plausible small values.

But remember that these calculations are all assuming that the consumer's *entire* consumption spending is financed by asset income. If the consumer has other income (for example, labor or transfer income) whose covariance with the risky return is small, they should be willing to take more risk. Since, for most consumers, most of their future consumption will be financed from labor or transfer income, it is not surprising to learn that models calibrated to actual data on capital and noncapital income dynamics imply that people should be investing most of their non-human wealth in the risky asset, with reasonable values of {math}`\CRRA` {cite:p}`cocco&gomes&maenhout:lifecycle`.

Another question is what the expected rate of return on the consumer's portfolio will be once the portfolio share in risky assets has been chosen optimally. Note first that {eq}`eq:PortCRRA-rportDist` implies that

```{math}
:label: eq:eport

\begin{gathered}\begin{aligned}
  \log \Ex_{t}[e^{\rport_{t+1}-\rfree}] & =  \riskyshare \EpremLog
\end{aligned}\end{gathered}
```

while the variance of the log of the excess return factor for the portfolio is {math}`\sigma^{2}_{\rport} = \riskyshare^{2} \sigma^{2}_{\risky}`. Substituting the solution {eq}`eq:PortCRRA-riskyshareMS` for {math}`\riskyshare` into {eq}`eq:eport`, we have

```{math}
:label: eq:rportPremOpt

\begin{gathered}\begin{aligned}
  \riskyshare \EpremLog & =  \left(\frac{\EpremLog^{2}}{\CRRA \Evarr}\right)
\\ & =   (\EpremLog/\sigma_{\risky})^{2}/\CRRA
\end{aligned}\end{gathered}
```

which is an interesting formula for the excess return of the optimally chosen portfolio because the object {math}`\EpremLog/\sigma_{\risky}` (the excess return divided by the standard deviation) is a well-known tool in finance for evaluating the tradeoff between risk and return (the "Sharpe ratio"). Equation {eq}`eq:rportPremOpt` says that the consumer will choose a portfolio that earns an excess return proportional to the square of the Sharpe ratio and inversely proportional to the risk aversion coefficient. Higher reward (per unit of risk) convinces the consumer to take the risk necessary to earn higher returns; but higher risk aversion convinces the investor to sacrifice (risky) return for safety.

Finally, we can ask what effect an exogenous increase in the risk of the risky asset has on the endogenous riskiness of the portfolio once the consumer has chosen optimally. The answer is surprising: The variance of the optimally-chosen portfolio is

```{math}
\begin{gathered}\begin{aligned}
\riskyshare^{2} \sigma^{2}_{\risky} & =  \left(\frac{\EpremLog}{\CRRA \Evarr}\right)^{2} \sigma^{2}_{\risky}
\\ & =  \left(\frac{(\EpremLog/\CRRA)^{2}}{\Evarr}\right)
\end{aligned}\end{gathered}
```

which is actually *smaller* when {math}`\sigma^{2}_{\risky}` is larger. The reason: a riskier asset pays less per unit of variance. Cutting the share only enough to restore the portfolio's variance would leave the same risk at a lower expected return, so the investor cuts it further.

:::{figure} figures/ShareVsCRRA.png
:name: fig:ShareVsCRRA
:align: center

The Approximate Risky Portfolio Share {math}`\riskyshare` Declines as Relative Risk Aversion {math}`\CRRA` Increases

Note: The approximation {math}`\riskyshare = \EpremLog/(\CRRA\Evarr)` with a premium of {math}`\EpremLog = 0.03` and {math}`\sigma_{\risky} = 0.2`, drawn by the [notebook](Portfolio-CRRA.ipynb).
:::

:::{figure} figures/ShareApproxErr.png
:name: fig:ShareApproxErr
:align: center

The Approximation Error for the Portfolio Share in Risky Assets {math}`\riskyshare` Is Small

Note: The exactly optimal share minus the approximation, for the same parameters. The [notebook](Portfolio-CRRA.ipynb) finds the exact share numerically, and its sliders vary the premium and the volatility; run it in your browser with nothing to install, in [JupyterLite](https://intertemporal-choice.github.io/lite/notebooks/index.html?path=Portfolio-CRRA.ipynb), or open it in [Colab](https://colab.research.google.com/github/intertemporal-choice/intertemporal-choice.github.io/blob/main/content/asset_pricing/Portfolio-CRRA/Portfolio-CRRA.ipynb) or [Binder](https://mybinder.org/v2/gh/intertemporal-choice/intertemporal-choice.github.io/main?labpath=content/asset_pricing/Portfolio-CRRA/Portfolio-CRRA.ipynb).
:::


(Campbell-Viceira-Approximation)=
## Appendix: The {cite:t}`cvAppendix` Approximation

For mathematical analysis (especially under the assumption of CRRA utility) it would be convenient if we could approximate the realized arithmetic portfolio return factor {math}`\Rport_{t+1}` by the geometric one, {math}`\Rfree^{1-\riskyshare}\Risky_{t+1}^{\riskyshare}`, because the log of the geometric factor is {math}`\rfree (1-\riskyshare)+\risky_{t+1}\riskyshare = \rfree + (\risky_{t+1}-\rfree)\riskyshare = \rfree + \EpremLog_{t+1} \riskyshare`, so the realized "portfolio excess return" would be simply {math}`\riskyshare\EpremLog_{t+1}`. Unfortunately, for {math}`\riskyshare` values well away from 0 and 1 (that is, for any *interesting* values of portfolio shares), the log of the geometric mean is a badly biased approximation to the log of the arithmetic mean when the variance of the risky asset is substantial.

{cite:t}`cvAppendix` propose instead

```{math}
\begin{gathered}\begin{aligned}
  \rport_{t+1} & \approx  \rfree+ \riskyshare \EpremLog_{t+1}+\riskyshare \sigma^{2}_{\risky}/2 - \riskyshare^{2}\sigma^{2}_{\risky}/2
\end{aligned}\end{gathered}
```

To see one virtue of this approximation,[^fn-ito] note (using [NormTimes](#fact:normtimes) and [SumNormsIsNorm](#fact:sumnormsisnorm)) that since the mean and variance of {math}`\EpremLog_{t+1} \riskyshare` are respectively {math}`\riskyshare(\risky - \sigma^{2}_{\risky}/2- \rfree)` and {math}`\riskyshare^{2} \sigma^{2}_{\risky}`, fact [LogELogNormTimes](#fact:logelognormtimes) implies that

[^fn-ito]: The approximation is motivated by the continuous-time solution, which is obtained using Ito's lemma.

```{math}
\begin{gathered}\begin{aligned}
 \log \Ex_{t}[e^{\EpremLog_{t+1} \riskyshare}] & =  \riskyshare (\risky - \rfree - \sigma^{2}_{\risky}/2) + \riskyshare^{2}\sigma^{2}_{\risky}/2
\end{aligned}\end{gathered}
```

which means that exponentiating then taking the expectation then taking the logarithm of {eq}`eq:rportCV` gives

```{math}
:label: eq:PortCRRA-rportDist

\begin{gathered}\begin{aligned}
   \log \Ex_{t}[e^{\rport_{t+1}}] & =  \log e^{\rfree} + \log \Ex_{t}[e^{\riskyshare \EpremLog_{t+1}}] + \log e^{\riskyshare\sigma^{2}_{\risky}/2 - \riskyshare^{2}\sigma^{2}_{\risky}/2}
\\ & =
\rfree + \riskyshare (\risky-\rfree-\sigma^{2}_{\risky}/2)+\riskyshare^{2}\sigma^{2}_{\risky}/2 +\riskyshare \sigma^{2}_{\risky}/2 - \riskyshare^{2}\sigma^{2}_{\risky}/2
\\ \log \Ex_{t}[e^{\rport_{t+1}}] - \rfree & =   \riskyshare (\risky-\rfree)
\end{aligned}\end{gathered}
```

or, in words: The expected excess portfolio return is equal to the proportion invested in the risky asset times the expected excess return of the risky asset.[^fn-return-convention]

[^fn-return-convention]: We use the word "return" always to mean the logarithm of the corresponding "factor"; and when not explicitly specified, we always take the expectation before taking the log; if we wanted to refer to {math}`\Ex_{t}[\rport_{t+1}]` we would call it the expected log portfolio return (to distinguish it from the expected portfolio return, {math}`\log \Ex_{t}[e^{\rport_{t+1}}]`).
