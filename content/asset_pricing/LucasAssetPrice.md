(sec:LucasAssetPrice)=
# The Lucas Asset Pricing Model

## Introduction/Setup

{cite:t}`lucas:assetpricing` considers an economy populated by infinitely many[^aggregation-note] identical individual consumers, in which the only assets are a set of identical infinitely-lived trees. Aggregate output is the fruit that falls from the trees, and cannot be stored (it would rot!); because {math}`\uFunc^{\prime}(\cRat)>0~\forall~\cRat`, the fruit is all eaten:

[^aggregation-note]: As in the [Aggregation](#sec:Aggregation) section.

```{math}
:label: eq:CeqY

\cRat_{t}\Pop_{t} = \dvdnd_{t}\Kap_{t}
```

where {math}`\cRat_{t}` is consumption of fruit per person, {math}`\Pop_{t}` is the population, {math}`\Kap_{t}` measures the stock of trees, and {math}`\dvdnd_{t}` is the exogenous output of fruit that drops from each tree. A crucial assumption is that the stock of trees is exogenous: you cannot consume a little less fruit and have more trees next period.

(In a given year, each tree produces exactly the same amount of fruit as every other tree, but {math}`\dvdnd_{t}` varies from year to year depending on the weather.) An economy like this, in which output arrives without any deliberate actions on the part of residents, is called an "endowment" economy (or, sometimes, an "exchange" economy).[^production-economy]

[^production-economy]: The alternative is a "production" economy, in which factors of production (labor, capital, maybe land, maybe knowledge) combine somehow to generate the output.

(The-Market-for-Trees)=
## The Market for Trees

We now consider a market in which individual consumers can buy and sell trees. This requires some mental gymnastics: with infinitely many identical consumers, we must find a price at which every one of them is simultaneously satisfied. If there is a perfect capital market for trees, the price of trees {math}`\Price_{t}` must be such that, each period, each (identical) consumer does not want either to increase or to decrease their holding of trees.[^equilibrium-price]

[^equilibrium-price]: If, at a hypothesized equilibrium price, every identical consumer wanted (say) to increase their holdings, that price could not be an equilibrium price, because with a fixed supply of trees everyone cannot increase their holding of trees at once!

If a tree is sold, the sale is assumed to occur after the existing owner receives that period's fruit ({math}`\Price_{t}` is the "ex-dividend" price). Total resources available to consumer {math}`i` in period {math}`t` are the sum of the fruit received from the trees owned, {math}`\dvdnd_{t}\kap_{t}^{i}`, plus the potential proceeds if the consumer were to sell all his stock of trees, {math}`\Price_{t}\kap_{t}^{i}`. Total resources are divided into two uses: Current consumption {math}`c_{t}^{i}` and the purchase of trees for next period {math}`\kap_{t+1}^{i}` at price {math}`\Price_{t}`,

```{math}
\overbrace{\kap_{t+1}^{i}\Price_{t}+c_{t}^{i}}^{\text{Uses of resources}} = \overbrace{\dvdnd_{t}\kap_{t}^{i}+\Price_{t}\kap_{t}^{i}}^{\text{Total resources}}
```

```{math}
\kap_{t+1}^{i} = (1+\dvdnd_{t}/\Price_{t})\kap_{t}^{i}-c_{t}^{i}/\Price_{t}.
```

## The Problem of an Individual Consumer

Consumer {math}`i` maximizes

```{math}
:label: eq:origprob

\vFunc({m}_{t}^{i}) = \max ~ \Ex_{t}^{i}\left[\sum_{n=0}^{\infty} \DiscFac^{n} \uFunc(\cRat_{t+n}^{i}) \right]
```

subject to

```{math}
\kap_{t+1}^{i} = (1+\dvdnd_{t}/\Price_{t})\kap_{t}^{i}-c_{t}^{i}/\Price_{t}
```

```{math}
{m}_{t+1}^{i} = (\Price_{t+1}+\dvdnd_{t+1})\kap_{t+1}^{i}.
```

Rewriting in the form of Bellman's equation,

```{math}
\vFunc({m}_{t}^{i}) = \max_{\{c_{t}^{i}\}} ~ \uFunc(c_{t}^{i}) + \DiscFac \Ex_{t}^{i}\left[\vFunc({m}_{t+1}^{i})\right],
```

the first order condition tells us that

```{math}
0 = \uFunc^{\prime}(c_{t}^{i})+\DiscFac \Ex_{t}^{i}\left[\vFunc^{\prime}({m}_{t+1}^{i})\frac{\partial}{\partial c_{t}^{i}}\left(\overbrace{({\Price}_{t+1}+\dvdnd_{t+1})\underbrace{\left((1+\dvdnd_{t}/\Price_{t})\kap_{t}^{i}-c_{t}^{i}/\Price_{t}\right)}_{\kap_{t+1}^{i}}}^{{m}_{t+1}^{i}}\right)\right]
```

Spending one more unit of consumption today buys {math}`1/\Price_{t}` fewer trees, each of which would have paid off {math}`{\Price}_{t+1}+\dvdnd_{t+1}` tomorrow, so the derivative inside the expectation is

```{math}
\frac{\partial {m}_{t+1}^{i}}{\partial c_{t}^{i}} = -\frac{{\Price}_{t+1}+\dvdnd_{t+1}}{\Price_{t}} \equiv -\Risky_{t+1}.
```

Substituting this and moving the resulting negative term to the left-hand side,

```{math}
:label: eq:FOCwithRisky

\uFunc^{\prime}(c_{t}^{i}) = \DiscFac \Ex_{t}^{i}\left[\vFunc^{\prime}({m}_{t+1}^{i})\left(\underbrace{\frac{{\Price}_{t+1}+\dvdnd_{t+1}}{\Price_{t}}}_{\equiv \Risky_{t+1}}\right)\right] = \DiscFac \Ex_{t}^{i}\left[\Risky_{t+1} \vFunc^{\prime}({m}_{t+1}^{i})\right]
```

where {math}`\Risky_{t+1}` is the return factor that measures the resources in period {math}`t+1` that are the reward for owning a unit of trees at the end of {math}`t`.

The [Envelope theorem](#sec:Envelope) tells us that {math}`\vFunc^{\prime}({m}_{t+1}^{i})=\uFunc^{\prime}(c_{t+1}^{i})`, so {eq}`eq:FOCwithRisky` becomes

```{math}
:label: eq:pofci

\uFunc^{\prime}(c_{t}^{i}) = \DiscFac \Ex_{t}^{i}\left[\uFunc^{\prime}(\cRat_{t+1}^{i})\left(\frac{{\Price}_{t+1}+\dvdnd_{t+1}}{\Price_{t}}\right)\right]
```

```{math}
\Price_{t} = \DiscFac \Ex_{t}^{i}
\left[
  \left(
    \frac{\uFunc^{\prime}(\cRat_{t+1}^{i})}{\uFunc^{\prime}(\cRat_{t}^{i})}
  \right)
  \left({\Price}_{t+1}+\dvdnd_{t+1}\right)
\right].
```

## Aggregation

Since all consumers are identical, {math}`c_{t}^{i} = c_{t}^{j}~\forall~i,j`, so henceforth we just call consumption per capita {math}`\cRat_{t}`. Since aggregate consumption must equal aggregate production because fruit cannot be stored, normalizing the population to {math}`\Pop_{t}=1 ~\forall ~ t` and stock of trees to {math}`\Kap_{t}=1 ~\forall~t`, equation {eq}`eq:CeqY` becomes:

```{math}
\cRat_{t} = \dvdnd_{t}.
```

Substituting {math}`\cRat_{t}` and {math}`\cRat_{t+1}` for {math}`c_{t}^{i}` and {math}`c_{t+1}^{i}` in {eq}`eq:pofci` and then substituting {math}`\dvdnd_{t}` for {math}`\cRat_{t}` we get

```{math}
:label: eq:pofd

\Price_{t} = \DiscFac \Ex_{t}\left[\left(\frac{\uFunc^{\prime}(\dvdnd_{t+1})}{\uFunc^{\prime}(\dvdnd_{t})}\right)\left({\Price}_{t+1}+\dvdnd_{t+1}\right)\right].
```

We can rewrite this more simply if we define

```{math}
:label: eq:StochDiscFact

\SDF_{t,t+n} = \DiscFac^{n} \left(\frac{\uFunc^{\prime}(\dvdnd_{t+n})}{\uFunc^{\prime}(\dvdnd_{t})}\right)
```

which is called the "stochastic discount factor" because (a) it is stochastic (thanks to the shocks between {math}`t` and {math}`t+n` that determine the value of {math}`\dvdnd_{t+n}`); and (b) it measures the rate at which all agents in this economy in period {math}`t` will discount a unit of value received in a future period, e.g. {math}`t+1`:

```{math}
:label: eq:Pt

\Price_{t} = \Ex_{t}\left[\SDF_{t,t+1}\left({\Price}_{t+1}+\dvdnd_{t+1}\right)\right].
```

A corresponding equation will hold in period {math}`t+1` (and in period {math}`t+2` and beyond):

```{math}
:label: eq:Ptp1

\Price_{t+1} = \Ex_{t+1}\left[\SDF_{t+1,t+2}\left({\Price}_{t+2}+\dvdnd_{t+2}\right)\right]
```

so we can use repeated substitution, e.g. of {eq}`eq:Ptp1` into {eq}`eq:Pt`, and so on to get

```{math}
:label: eq:PtsubPtp1

\Price_{t} = \Ex_{t}\left[\SDF_{t,t+1}\dvdnd_{t+1}\right]+\Ex_{t}[\SDF_{t,t+1}\Ex_{t+1}[\SDF_{t+1,t+2}\dvdnd_{t+2}]]+ \ldots.
```

The "law of iterated expectations" says that {math}`\Ex_{t}[\Ex_{t+1}[{\Price}_{t+2}]] = \Ex_{t}[{\Price}_{t+2}]`; given this, and noting that {math}`\SDF_{t,t+2} = \SDF_{t,t+1}\SDF_{t+1,t+2}`, {eq}`eq:PtsubPtp1` becomes:

```{math}
:label: eq:PtAsPDV

\Price_{t} = \Ex_{t}\left[\SDF_{t,t+1}\dvdnd_{t+1}+\SDF_{t,t+2}\dvdnd_{t+2}+\SDF_{t,t+3}\dvdnd_{t+3}+...\right].
```

So, the price of the asset is the present discounted value of the stream of future "dividends," where the stochastic factor by which (potentially stochastic) dividends received in {math}`t+n` are discounted back to {math}`t` is {math}`\SDF_{t,t+n}`.

## Specializing the Model

This is as far as we can go without making explicit assumptions about the structure of utility. If utility is CRRA, {math}`\uFunc(\cRat)=(1-\CRRA)^{-1}\cRat^{1-\CRRA},` substituting {math}`\uFunc^{\prime}(\dvdnd)=\dvdnd^{-\CRRA}` into {eq}`eq:pofd` yields

```{math}
:label: eq:pofdCRRA

\Price_{t} = \DiscFac \dvdnd_{t}^{\CRRA} \Ex_{t}\left[\dvdnd_{t+1}^{-\CRRA}(\Price_{t+1}+\dvdnd_{t+1})\right]
```

and the particularly special case of logarithmic utility (which Lucas emphasizes) corresponds to {math}`\CRRA=1`, which (again using the law of iterated expectations) allows us to simplify {eq}`eq:pofdCRRA` to

```{math}
:label: eq:pofdLog

\begin{aligned}
\frac{\Price_{t}}{\dvdnd_{t}} & = \DiscFac \Ex_{t}\left[\dvdnd_{t+1}^{-1}(\Price_{t+1}+\dvdnd_{t+1})\right] \\
& = \DiscFac \left(1+\Ex_{t} \left[\frac{{\Price}_{t+1}}{\dvdnd_{t+1}}\right]\right) \\
& = \DiscFac \left(1+\DiscFac \left(1+\Ex_{t}\left[\frac{{\Price}_{t+2}}{\dvdnd_{t+2}}\right]\right)\right) \\
& = \DiscFac \left(1 + \DiscFac + \DiscFac^{2} + \ldots + \Ex_{t} \left[\lim_{n\rightarrow \infty}\DiscFac^{n-1}\left[\frac{\Price_{t+n}}{\dvdnd_{t+n}}\right]\right]\right) \\
& = \frac{\DiscFac}{1-\DiscFac} + \DiscFac \Ex_{t}\left\{\lim_{n\rightarrow \infty}\DiscFac^{n-1}\left[\frac{\Price_{t+n}}{\dvdnd_{t+n}}\right]\right\}.
\end{aligned}
```

If the price is bounded (it cannot ever go, for example, to a value such that it would cost more than the economy's entire output to buy a single tree), it is possible to show that the limit term in this equation goes to zero. Using the usual definition of the time preference factor as {math}`\DiscFac = 1/(1+\timeRate)` where {math}`\timeRate` is the time preference rate, the equilibrium price is:

```{math}
:label: eq:pWithLogU

\Price_{t} = \dvdnd_{t}\left(\frac{\DiscFac}{1-\DiscFac} \right) = \dvdnd_{t}\left(\frac{1}{1/\DiscFac-1} \right) = \dvdnd_{t}\left(\frac{1}{1+\timeRate-1} \right) = \frac{\dvdnd_{t}}{\timeRate}
```

or, equivalently, the "dividend-price ratio" is always {math}`\dvdnd_{t}/\Price_{t} = \timeRate`.[^crra-derivation]

[^crra-derivation]: A derivation parallel to the one above shows that in the CRRA utility case the solution is {math}`\dvdnd_{t}^{\CRRA}/\Price_{t} = \timeRate.`

It may surprise you that the equilibrium price of trees today does not depend on the expected level of fruit output in the future. If the weather was bad this year, but is expected to return to normal next year (and, by definition, is expected to be equal to normal in subsequent years), you might think that the price today would mostly reflect the "normal" value of fruit production that the trees produce, not the (temporarily low) value that happens to obtain today.

The above derivation says that intuition is wrong: Today's price depends only on today's output.

Nevertheless, the logic (higher future output is a reason for higher current prices) is not wrong; but it is (exactly) counterbalanced by another, and subtler, fact: Since future consumption will equal future fruit output, higher expected fruit output means lower marginal utility of consumption in that future period of (more) abundant fruit (basically, people are starving today, which reduces the attractiveness of cutting their consumption to buy trees that will produce more in a period when they expect *not* to be starving). These two forces are the manifestation of the (pure) income effect and substitution effect in this model (there is no human wealth, and therefore no human wealth effect). In the special case of logarithmic utility considered here, income and substitution effects are of the same size and opposite sign so the two forces exactly offset.

## The Interest Rate and the Rate of Return in a Lucas Model

We can decompose the return factor attributable to ownership of a share of capital (cf. {eq}`eq:FOCwithRisky`) by adding and subtracting {math}`\Price_{t}` in the numerator:

```{math}
:label: eq:RiskyDecomposeFactor

\Risky_{t+1} = \left(\frac{{\Price}_{t+1}+{\Price}_{t}-{\Price}_{t}+\dvdnd_{t+1}}{\Price_{t}}\right) = \left(1+\frac{\Delta {\Price}_{t+1}}{\Price_{t}}+\frac{\dvdnd_{t+1}}{\Price_{t}}\right)
```

so the "rate of return" is

```{math}
:label: eq:riskyDecompose

\risky_{t+1} = \frac{\Delta {\Price}_{t+1}}{\Price_{t}}+\frac{\dvdnd_{t+1}}{\Price_{t}}
```

which is a useful decomposition because the two components have natural interpretations: The first is a "capital gain" (or loss), and the second can plausibly be identified as "the interest rate" paid by the asset (because it corresponds to income received regardless of whether the asset is liquidated).

In models that do not explicitly discuss asset pricing, the implicit assumption is usually that the price of capital is constant (which might be plausible if capital consists mostly of reproducible items like machines,[^capital-price-trend] rather than Lucas trees). In this case

[^capital-price-trend]: The key insights below remain true even if there is a gradual trend in the real price of capital goods, as has in fact been true.

```{math}
\Risky_{t+1} = \left(1+\frac{\dvdnd_{t+1}}{\Price_{t}}\right)
```

says that the only risk in the rate of return is attributable to unpredictable variation in the size of dividend/interest payments. Indeed, if additional assumptions are made (e.g., perfect capital markets) that yield the conclusion that the interest rate matches the marginal product of capital, then such models generally imply that variation in returns (at least at high frequencies) is very small, because aggregate capital typically is very stable from one period to the next in such models, and, if the aggregate production function is stable, this implies great stability in the marginal product of capital.

## Aggregate Returns Versus Individual Returns

One of the subtler entries in {cite:t}`aristotleFallacies`'s catalog of common human reasoning errors was the "fallacy of composition," in which the reasoner supposes that if a proposition is true of each element of a whole, then it must be true of the whole.

The Lucas model provides a counterexample. From the standpoint of any individual (atomistic) agent, it is quite true that a decision to save one more unit will yield greater future resources, in the amount {math}`\Risky_{t+1}`. But from the standpoint of the society as a whole, if everyone decided to do the same thing (save one more unit), there would be no effect on aggregate resources in period {math}`t+1`. Put another way, for any individual agent, it appears that the "marginal product of capital" is {math}`\Risky_{t+1}`, but for the society as a whole the marginal product of capital is zero.

The proposition that the return for society as a whole must be the same as the return that is available to individuals is an error because it implicitly assumes that there are no general equilibrium effects of a generalized desire to save more (or, more broadly, that there is no interaction between the decisions one person makes and the outcomes for another person). The Lucas model provides a counterexample in which, if everyone's preferences change (e.g., {math}`\timeRate` goes down for everyone), the price of the future asset is affected, indeed, it is affected in a way that is sufficient to exactly counteract the increased desire for ownership of future dividends (since there is a fixed supply of assets to be owned, the demand must be reconciled with that preexisting supply).

Aristotle was a smart guy!

## Analytical and Numerical Solutions

The appendices derive various results about the solution to the model under different assumptions. But, unfortunately, the model has analytical solutions (like, {math}`P = d/\vartheta`) or approximate analytical solutions only in very special circumstances. The accompanying [DemARK notebook](https://mybinder.org/v2/gh/econ-ark/DemARK/HEAD?filepath=notebooks/Lucas-Asset-Pricing-Model.ipynb) shows how to solve the model numerically for a simple case where there is no such analytical solution (the case where dividends follow an AR(1) process), and also shows how the numerical solution compares with the approximate analytical solution in the CRRA utility case.

## Appendix: Analytical Solutions in CRRA Utility Case

### When Dividends are IID

Suppose {math}`\dvdnd_{t+n}` is identically individually distributed in every future period, so that its expectation as of {math}`t` is the same for any date {math}`n>0`:

```{math}
:label: eq:dmod

\edvdnd \equiv \Ex_{t}[\dvdnd_{t+n}^{1-\CRRA}].
```

Now note that {eq}`eq:pofdCRRA` can be rewritten as

```{math}
\frac{\Price_{t}}{\dvdnd_{t}^{\CRRA}} = \DiscFac \left( \edvdnd + \Ex_{t}\left[\frac{\Price_{t+1}}{\dvdnd_{t+1}^{\CRRA}}\right] \right)
```

```{math}
= \DiscFac \edvdnd \left(1 + \DiscFac + \DiscFac \Ex_{t}\left[\frac{\Price_{t+2}}{\dvdnd_{t+2}^{\CRRA}}\right]\right)
```

```{math}
= \DiscFac \edvdnd \left(1 + \DiscFac  + \DiscFac^{2} + \ldots + \underbrace{\Ex_{t} \left[\lim_{n\rightarrow \infty}\DiscFac^{n-1}\left[\frac{\Price_{t+n}}{\dvdnd_{t+n}^{\CRRA}}\right]\right]}_{\text{assume goes to zero}}\right)
```

```{math}
:label: eq:PtCRRA

= \left(\frac{\DiscFac \edvdnd}{1-\DiscFac}\right) = \left(\frac{\edvdnd}{\DiscFac^{-1}-1}\right)
```

To make further progress, suppose that the iid process for dividends is a mean-one lognormal: {math}`\log \dvdnd_{t+n} \sim \mathcal{N}(-\sigma^{2}/2,\sigma^{2})~\forall~n` so that {math}`\Ex_{t}[\dvdnd_{t+n}]=1~\forall~n` (see [ELogNormMeanOne](#fact:elognormmeanone)), in which case [ELogNormTimes](#fact:elognormtimes) can be used to show that

```{math}
:label: eq:edvdndSimple

\edvdnd = e^{\CRRA(\CRRA-1)(1/2)\sigma^{2}}
```

and if we approximate {math}`\DiscFac \approx e^{-\timeRate}` then {math}`\DiscFac^{-1} \approx 1+\timeRate` and so {eq}`eq:PtCRRA` becomes

```{math}
\frac{\Price_{t}}{\dvdnd_{t}^{\CRRA}} \approx \left(\frac{e^{\CRRA(\CRRA-1)(1/2)\sigma^{2}}}{\timeRate}\right)
```

```{math}
\Price_{t} \approx \left(\frac{\dvdnd_{t}^{\CRRA} e^{\CRRA(\CRRA-1)(1/2)\sigma^{2}}}{\timeRate}\right)
```

So the log is

```{math}
:label: eq:PtLogIID

\log \Price_{t} \approx \CRRA \log \dvdnd_{t} + \CRRA(\CRRA-1)(1/2)\sigma^{2} - \log \timeRate
```

and thus the variances obey

```{math}
:label: eq:varLogPvsLogd

\var({\log \Price}) = \CRRA^{2} \var(\log \dvdnd).
```

Given that {math}`\CRRA > 1`, this derivation yields some interesting insights:

1. (the log of) asset prices will be more volatile than (the log of) dividends
2. An increase in risk aversion {math}`\CRRA` increases the price {math}`\Price_{t}` (because {math}`\CRRA(\CRRA-1)\sigma^{2}/2 > 0` and an increase in {math}`\CRRA` increases its size)

The second point is surprising, so let me say it again: an *increase* in risk aversion *increases* the price of the risky asset. In a sense, this is an implication of the proposition that risk aversion increases the volatility of asset prices (when they are high, they must be *very* high; when low, *very* low). But, it does not correspond very well to the common narrative in which market analysts often attribute a decline in asset prices to "increased risk aversion."

### When Dividends Follow a Random Walk

The polar alternative to IID shocks would be for dividends to follow a random walk: {math}`\log (\dvdnd_{t+1}/\dvdnd_{t}) \sim \mathcal{N}(-\sigma^{2}/2,\sigma^{2})`.

Now divide both sides of {eq}`eq:pofdCRRA` by {math}`\dvdnd_{t}`, and rewrite the object inside the expectations operator by multiplying the first term by {math}`\dvdnd_{t+1}` and dividing the second term by {math}`\dvdnd_{t+1}`, yielding

```{math}
:label: eq:pofdCRRAWdvdndGro

\left(\frac{\Price_{t}}{\dvdnd_{t}}\right) = \DiscFac \dvdnd_{t}^{-(1-\CRRA)} \Ex_{t}\left[\dvdnd_{t+1}^{1-\CRRA}\left(\frac{\Price_{t+1}}{\dvdnd_{t+1}}+1\right)\right] = \DiscFac  \Ex_{t}\left[\left(\frac{\dvdnd_{t+1}}{\dvdnd_{t}}\right)^{1-\CRRA}\left(\frac{\Price_{t+1}}{\dvdnd_{t+1}}+1\right)\right].
```

Now (1) note that our assumption here about the distribution of {math}`\dvdnd_{t+1}/\dvdnd_{t}` is identical to the assumption about {math}`\dvdnd_{t+1}` above, so the expectation will be the same {math}`\edvdnd`; and (2) hypothesize that there will be a solution under which the price-dividend ratio is a constant; call it {math}`\risky^{-1}`:

```{math}
\risky^{-1} = \DiscFac  \left[\edvdnd(\risky^{-1}+1)\right]
```

```{math}
1 = \DiscFac \edvdnd (1+\risky)
```

```{math}
\left(\frac{1-\DiscFac \edvdnd}{\DiscFac \edvdnd}\right) = \risky
```

```{math}
\left(\frac{1}{(\DiscFac \edvdnd)^{-1}-1}\right) = \risky^{-1}
```

so that we obtain a formula for {math}`\risky^{-1} = \Price_{t}/\dvdnd_{t}`

```{math}
:label: eq:PtLogRW

\log \Price_{t} \approx \log \dvdnd_{t}  - \log (\timeRate -  (1/2)\CRRA (\CRRA-1) \sigma^{2})
```

The difference with {eq}`eq:PtLogIID` is only the absence of the {math}`\CRRA` multiplying {math}`\log \dvdnd_{t}`. The main substantive difference is therefore that the variance of (log) prices and the variance of (log) dividends is now the same. The surprising result that the price-dividend ratio increases when risk aversion increases continues to hold.

## When Dividends Follow an AR(1) Process

The two cases just examined are the polar ones, and the interesting territory lies between them. Dividends that are IID have no memory at all, while dividends that follow a random walk never forget. Actual dividends fall somewhere in the middle, high this year if they were high last year, though not permanently so.

We must impose the persistence on the *log* of dividends rather than on their level, and it is worth being clear about why, because the tempting alternative fails in two separate ways. An AR(1) in levels, {math}`\dvdnd_{t+1} = \alpha \dvdnd_{t} + \err_{t+1}` with normal {math}`\err`, would put positive probability on a negative dividend, which is not a thing a tree can produce. It would also leave {math}`\dvdnd_{t}` sitting inside the expectation in {eq}`eq:pofdCRRAWdvdndGro` in a form admitting no constant price-dividend ratio, so the analytical thread would be lost at the first step.

So write {math}`x_{t} \equiv \log \dvdnd_{t}` and assume

```{math}
:label: eq:AR1logs

x_{t+1} = \alpha x_{t} + \err_{t+1}, \qquad \err_{t+1} \sim \mathcal{N}(-\sigma^{2}/2,\sigma^{2}),
```

which contains both earlier cases: {math}`\alpha=0` is the IID assumption and {math}`\alpha=1` is the random walk.

Rather than guess at a price-dividend ratio, we price each future dividend separately and add up (the guess-and-verify route used above needs a constant ratio, and there is not one to find here). The Lucas price is the present discounted value of the dividend stream evaluated at the consumer's own marginal utility, so with {math}`\cRat=\dvdnd` and {math}`\uFunc^{\prime}(\cRat)=\cRat^{-\CRRA}`,

```{math}
:label: eq:strips

\left(\frac{\Price_{t}}{\dvdnd_{t}}\right) = \sum_{n=1}^{\infty} \DiscFac^{n} \Ex_{t}\left[\left(\frac{\dvdnd_{t+n}}{\dvdnd_{t}}\right)^{1-\CRRA}\right].
```

Iterating {eq}`eq:AR1logs` gives {math}`x_{t+n}-x_{t} = (\alpha^{n}-1)x_{t} + \sum_{j=1}^{n}\alpha^{n-j}\err_{t+j}`, and because the {math}`\err` are independent and lognormal each strip can be evaluated with [ELogNorm](#fact:elognorm). Writing {math}`S_{n} = \sum_{k=0}^{n-1}\alpha^{k}` and {math}`Q_{n} = \sum_{k=0}^{n-1}\alpha^{2k}`,

```{math}
:label: eq:AR1strip

\Ex_{t}\left[\left(\frac{\dvdnd_{t+n}}{\dvdnd_{t}}\right)^{1-\CRRA}\right] = \exp\left((1-\CRRA)(\alpha^{n}-1)x_{t} - \frac{\sigma^{2}}{2}(1-\CRRA)S_{n} + \frac{\sigma^{2}}{2}(1-\CRRA)^{2}Q_{n}\right).
```

Substituting {eq}`eq:AR1strip` into {eq}`eq:strips` gives the price-dividend ratio for any {math}`\alpha`. We know of no closed form for {math}`0<\alpha<1`, since {math}`\alpha^{n}` appears in an exponent and resists the geometric sum that rescues the polar cases, though the series itself converges geometrically and evaluating it costs a single line of code.

The two polar cases fall out. Setting {math}`\alpha=1` makes {math}`S_{n}=Q_{n}=n` and kills the {math}`x_{t}` term, so every strip is {math}`\edvdnd^{n}` and the sum collapses to the constant ratio of {eq}`eq:PtLogRW`. Setting {math}`\alpha=0` makes {math}`S_{n}=Q_{n}=1` for every {math}`n\geq 1`, leaving {math}`\dvdnd_{t}^{\CRRA-1}\edvdnd \DiscFac/(1-\DiscFac)`, which is {eq}`eq:PtLogIID`.

Between the poles the price-dividend ratio is no longer a constant. It depends on {math}`\dvdnd_{t}` through the {math}`(\alpha^{n}-1)x_{t}` term, and it is constant only in the random walk limit, where the level of dividends carries no information about their growth. Raising {math}`\alpha` raises the ratio, steeply as {math}`\alpha` nears one: at {math}`\CRRA=3`, {math}`\sigma=0.1`, {math}`\timeRate=0.04` and {math}`\dvdnd_{t}=1`, the ratio runs 25.8, 26.4, 29.5, 47.6 and 108 for {math}`\alpha=0, 0.6, 0.9, 0.99` and {math}`1`. Mean reversion is what keeps the ratio finite and modest. Remove it and the price of the tree rises sharply, because a high dividend today then forecasts high dividends forever (which is why the random walk deserves to be called the extreme case, and why the ratio there sits so far above the values that surround it).
