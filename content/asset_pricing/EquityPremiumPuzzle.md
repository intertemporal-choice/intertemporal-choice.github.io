(sec:EquityPremiumPuzzle)=
# The Equity Premium Puzzle and the Riskfree Rate

Applied to the stock market, the [consumption CAPM](#sec:C-CAPM) relation {eq}`eq:CCAPM-eqprem` gives the equity premium puzzle of {cite:t}`mehraPrescottPuzzle`. With {math}`\Risky_{t+1}` the return factor on equities and {math}`\Rfree` that on a perfectly riskless asset, it says

```{math}
:label: eq:EPP-eqprem

\begin{aligned}
\Ex_{t}[\Risky_{t+1}]-\Rfree & \approx \frac{\CRRA \cov_{t}(\Delta \log {c}_{t+1},\Risky_{t+1})}{1-\CRRA \Ex_{t}[ \Delta \log {c}_{t+1}]} \\
& \approx \CRRA \cov_{t}(\Delta \log {c}_{t+1},\Risky_{t+1})
\end{aligned}
```

where the last approximation holds when {math}`\CRRA\Ex_{t}[\Delta \log {c}_{t+1}]` is small.

## The Equity Premium Puzzle

Because this expression must hold at all {math}`t`, we can check it empirically by calculating empirical estimates of the two components and assuming that the sample averages correspond to the representative agent's expectations. That is, if we have data for periods {math}`1 \ldots n`, we assume that the unconditional expectations correspond to the sample means, {math}`\Ex [\Risky] = (1/n) \sum_{s=1}^{n} \Risky_{s}`; {math}`\Ex [\Delta \log c] = (1/n) \sum_{s=1}^{n} \Delta \log c_{s}`; and {math}`\cov(\Delta \log c,\Risky) = (1/n) \sum_{s=1}^{n} (\Delta \log c_{s} - \Ex [\Delta \log c])(\Risky_{s}-\Ex [\Risky])`.

The equity premium puzzle is essentially that {math}`\cov(\Delta \log c,\Risky)` is very small (about 0.004) but {math}`\Ex [\Risky]-\Rfree` is about 0.08 (stocks have earned real returns of about 8 percent more than riskless assets over the historical period), which means that the only way equation {eq}`eq:EPP-eqprem` can hold is if {math}`\CRRA` is implausibly large (these values imply {math}`\CRRA=20`; keeping the denominator of {eq}`eq:EPP-eqprem`, with consumption growth of 1.5 percent, lowers that only to about 15).

How do we know what plausible values of {math}`\CRRA` are? Consider the following. You must choose between a gamble in which you consume \$50,000 for the rest of your life with probability 0.5 and \$100,000 with probability 0.5, or consuming some amount {math}`X` with certainty. The coefficient of relative risk aversion determines the {math}`X` which would make you indifferent between consuming X and being exposed to the gamble. For example, if {math}`\CRRA = 0`, then you have no risk aversion at all and you will be indifferent between \$75,000 with certainty and the 50/50 gamble with expected value of \$75,000. Here are the values of X associated with different values of {math}`\CRRA` (table taken from {cite:t}`mankiw&zeldes:stockholders`).

:::{list-table} Certainty equivalent {math}`X` for different coefficients of relative risk aversion
:header-rows: 1
:name: tbl:crra-certainty-equiv

* - {math}`\CRRA`
  - {math}`X`
* - 1
  - 70,711
* - 3
  - 63,246
* - 5
  - 58,566
* - 10
  - 53,991
* - 20
  - 51,858
* - 30
  - 51,209
* - {math}`\infty`
  - 50,000
:::

{math}`\CRRA = 20` means being indifferent between \$51,858 for sure and a fifty-fifty chance at \$50,000 or \$100,000, far more risk aversion than people show.

## The Riskfree Rate Puzzle

Rewrite the consumption Euler equation {eq}`eq:CCAPM-ceuler`, for a single risky asset held in the share {math}`\riskyshare_{t}`, as

```{math}
:label: eq:EPP-newgam

\uFunc^{\prime}(c_{t}) = \Ex_{t}\left[\Discount (\Rfree + \riskyshare_{t} [\Risky_{t+1} - \Rfree])\uFunc^{\prime}({c}_{t+1})\right]
```

and note that from {eq}`eq:CCAPM-gameuler` we know that {math}`\Ex_{t}[\Discount \riskyshare_{t}(\Risky_{t+1}-\Rfree)\uFunc^{\prime}({c}_{t+1})] = 0` so that {eq}`eq:EPP-newgam` reduces to the ordinary Euler equation

```{math}
\begin{aligned}
\uFunc^{\prime}(c_{t}) & = \Ex_{t}[\Discount \Rfree \uFunc^{\prime}({c}_{t+1})] \\
1 & = \Discount \Rfree \Ex_{t}[ ({c}_{t+1}/c_{t})^{-\CRRA}]
\end{aligned}
```

Using the same approximations ([ExpEps](#fact:expeps) and [TaylorOne](#fact:taylorone)), we get the standard approximation to the Euler equation,

```{math}
\Ex_{t}[\Delta \log c_{t+1}] \approx (1/\CRRA) (\rfree - \timeRate)
```

The "riskfree rate puzzle" is that average consumption growth per capita has been about 1.5 percent (in the US in the postwar period) while real riskfree interest rates have been at most 1 percent. Even if we assume a time preference rate of {math}`\timeRate=0` (no impatience at all, i.e. {math}`\Discount=1`), the only way this equation can hold is if {math}`\CRRA` is a very small number: with a riskless rate of at most 1 percent and growth of 1.5 percent, {math}`\CRRA \leq 2/3`. Of course, this is precisely the opposite of the conclusion of the equity premium puzzle, which implies the {math}`\CRRA` must be very large.

The riskfree rate puzzle might in principle be explicable by [overlapping generations](#sec:OLGModel), whose riskless rate is not pinned down by a representative consumer's Euler equation and can even fall below the growth rate, though in practice it is hard to make that work well. A precautionary saving motive also cuts against the puzzle, by adding a variance term to consumption growth.
