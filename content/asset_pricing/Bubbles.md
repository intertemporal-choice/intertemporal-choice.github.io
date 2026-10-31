(sec:Bubbles)=
# Canonical Asset Pricing and Rational Bubbles

## Prices as the PDV of Dividends

Denoting dividends as {math}`\dvdnd_{t}` for a stock with a market price of {math}`\Price_{t}` per share, consider an investor who owns {math}`K_{t}` shares at the beginning of period {math}`t` yielding total wealth {math}`M_{t}=\Price_{t}K_{t}+\dvdnd_{t}K_{t}`. Assuming the investor has no other source of income (no labor income, for instance) the investor's budget constraint will be

```{math}
\begin{aligned}
M_{t}&=\underbrace{\dvdnd_{t}K_{t}+\Price_{t}K_{t}}_{\text{Total resources}} \\
    &= \underbrace{K_{t+1}\Price_{t}+C_{t}}_{\text{Uses of resources}}
\end{aligned}
```

which can be rearranged to indicate how many shares the investor will own next period, as a function of this period's wealth and consumption:

```{math}
\begin{aligned}
K_{t+1} &= \frac{M_{t}-C_{t}}{\Price_{t}} \\
M_{t+1} &= K_{t+1}(\Price_{t+1}+\dvdnd_{t+1}) \\
        &= (\Price_{t+1}+\dvdnd_{t+1})\left(\frac{M_{t}-C_{t}}{\Price_{t}}\right).
\end{aligned}
```

If this investor's only goal is to maximize the present discounted utility of consumption, discounting future utility by the factor {math}`\DiscFac`, then we have

```{math}
\VFunc_{t}(M_{t}) = \max_{\{C_{t}\}} \uFunc(C_{t})+\DiscFac \Ex_{t}\left[\VFunc_{t+1}\left((\Price_{t+1}+\dvdnd_{t+1})\left(\frac{M_{t}-C_{t}}{\Price_{t}}\right)\right)\right]
```

with FOC

```{math}
:label: eq:ceuler

\begin{aligned}
\uFunc^{\prime}(C_{t}) &= \DiscFac \Ex_{t}\left[\left(\frac{\Price_{t+1}+\dvdnd_{t+1}}{\Price_{t}}\right)\VFunc^{\prime}_{t+1}(M_{t+1})\right] \\
\uFunc^{\prime}(C_{t}) &= \DiscFac \Ex_{t}\left[\left(\frac{\Price_{t+1}+\dvdnd_{t+1}}{\Price_{t}}\right)\uFunc^{\prime}(C_{t+1})\right].
\end{aligned}
```

Defining the stochastic discount factor {math}`\SDF_{t,t+1} \equiv \DiscFac \uFunc^{\prime}(C_{t+1})/\uFunc^{\prime}(C_{t})`, the second line says {math}`\Price_{t} = \Ex_{t}[\SDF_{t,t+1}(\Price_{t+1}+\dvdnd_{t+1})]`, which is the pricing equation {eq}`eq:Pt` of the [Lucas model](#sec:LucasAssetPrice). Substituting forward as in that model, with {math}`\SDF_{t,s} \equiv \DiscFac^{s-t}\uFunc^{\prime}(C_{s})/\uFunc^{\prime}(C_{t})`, gives

```{math}
:label: eq:pdvWithSDF

\Price_{t} = \Ex_{t}\left[\sum_{s=t+1}^{T} \SDF_{t,s}\dvdnd_{s}\right] + \Ex_{t}\left[\SDF_{t,T}\Price_{T}\right].
```

Nothing so far assumes anything about the investor's attitude toward risk.

Now suppose that the investor is risk neutral ({math}`\uFunc(C) = C`), so that {math}`\uFunc^{\prime}(C_{t+1})=\uFunc^{\prime}(C_{t})=1` and {math}`\SDF_{t,s} = \DiscFac^{s-t}`. A perfectly safe asset with return factor {math}`\Rfree` must satisfy the same first order condition, {math}`1 = \DiscFac \Rfree`, so {math}`\Rfree = 1/\DiscFac`, and {eq}`eq:ceuler` becomes

```{math}
:label: eq:pteq

\begin{aligned}
\Rfree &= \Ex_{t}\left[\frac{\Price_{t+1}+\dvdnd_{t+1}}{\Price_{t}}\right] \\
\Price_{t} &= \Ex_{t}\left[\frac{\Price_{t+1}+\dvdnd_{t+1}}{\Rfree} \right].
\end{aligned}
```

A risk-neutral investor holds the stock only if it is expected to earn the riskless return. In {eq}`eq:pdvWithSDF`, the discount factor becomes {math}`\Rfree^{t-s}`:

```{math}
\Price_{t} = \Ex_{t}\left[\sum_{s=t+1}^{T} \Rfree^{t-s}\dvdnd_{s}\right] + \Rfree^{-(T-t)}\Ex_{t}[\Price_{T}].
```

We usually assume the "no-bubbles" condition that says that {math}`\lim_{T \rightarrow \infty} \Rfree^{-(T-t)}\Ex_{t}[\Price_{T}] = 0` (with risk aversion, {math}`\lim_{T \rightarrow \infty} \Ex_{t}[\SDF_{t,T}\Price_{T}] = 0`). In this case it is clear that the equilibrium price must equal the present discounted value of dividends:

```{math}
:label: eq:pstar

\Price_{t}^{*} = \Ex_{t}\left[\sum_{s=t+1}^{\infty} \Rfree^{t-s}\dvdnd_{s}\right].
```

Suppose now that dividends are expected to grow by a constant factor {math}`\PGro` henceforth, {math}`\Ex_{t}[\dvdnd_{s}] = \PGro^{s-t}\dvdnd_{t}`. In that case, provided {math}`\PGro < \Rfree` so that the sum converges, we have

```{math}
:label: eq:gordon

\begin{aligned}
\Price_{t}^{*} &= \sum_{s=t+1}^{\infty} (\PGro/\Rfree)^{s-t}\dvdnd_{t} \\
&= \dvdnd_{t} \left(\frac{\PGro/\Rfree}{1-\PGro/\Rfree}\right) \\
&= \frac{\Ex_{t}[\dvdnd_{t+1}]}{\Rfree-\PGro} \\
&\approx \frac{\dvdnd_{t}}{\rfree-\pGro}.
\end{aligned}
```

The third line is exact: the price is next period's expected dividend divided by the difference between the interest factor and the growth factor of dividends, which is also the difference between the net interest rate and the net growth rate. The final approximation uses log rates, {math}`\rfree \equiv \log \Rfree` and {math}`\pGro \equiv \log \PGro`. This is known as the "Gordon formula," after {cite:t}`gordonDividends` and {cite:t}`gordonShapiro`; the idea of valuing a stock as the present value of its dividends is older {cite:p}`williamsInvestmentValue`.

The tricky thing in applying the formula is to know what to assume for the discount rate and for {math}`\PGro`. It is common to discount at a rate {math}`\risky = \rfree+\EpremLog`, where {math}`\EpremLog` is a premium that compensates for the risk in future dividends. But that is inconsistent with the derivation, which assumed a risk-neutral investor: such an investor demands no premium, and discounts at {math}`\rfree`. A premium can enter consistently only in a model in which risk is priced. In the [Lucas model with random-walk dividends](#When-Dividends-Follow-a-Random-Walk), for example, the price-dividend ratio is a constant, so the realized return factor {math}`\Risky_{t+1} = (\Price_{t+1}+\dvdnd_{t+1})/\Price_{t}` is the dividend growth factor {math}`\dvdnd_{t+1}/\dvdnd_{t}` times a constant. Taking expectations and solving for the price-dividend ratio gives, exactly,

```{math}
\Price_{t} = \frac{\Ex_{t}[\dvdnd_{t+1}]}{\Ex_{t}[\Risky_{t+1}]-\PGro},
```

a Gordon formula in which the asset's own expected return replaces {math}`\Rfree`. The premium {math}`\Ex_{t}[\Risky_{t+1}]-\Rfree` is whatever the model's stochastic discount factor makes it, not a number chosen separately.

{cite:t}`campbellShillerDP` derive the general version, which allows expected returns and expected dividend growth to change over time. Linearizing the definition of the log return {math}`\risky_{t+1} \equiv \log \Risky_{t+1}` around the average price-dividend ratio gives, approximately,

```{math}
:label: eq:campbellShiller

\log (\Price_{t}/\dvdnd_{t}) \approx \frac{\kappa}{1-\varrho} + \Ex_{t}\left[\sum_{j=0}^{\infty} \varrho^{j}\left(\Delta \log \dvdnd_{t+1+j} - \risky_{t+1+j}\right)\right]
```

where {math}`\varrho` is the average of {math}`\Price/(\Price+\dvdnd)`, a number just below one, and {math}`\kappa` is a constant from the linearization. A price that is high relative to dividends must be followed, on average, either by high growth of dividends or by low returns.

## Prices as Martingales

### The Law of Iterated Expectations

Suppose that a security price at time {math}`t`, {math}`\Price_{t}`, can be written as the rational expectation of some "fundamental value" {math}`V^{*}` conditional on information available at time {math}`t` (the classic example, from {cite:t}`samuelson:proof`, is a futures contract, whose fundamental value is the spot price on its delivery date). Then we have

```{math}
\Price_{t} = \Ex_{t}[V^{*}].
```

The same formula holds in period {math}`t+1`:

```{math}
\Price_{t+1} = \Ex_{t+1}[V^{*}].
```

Then the expectation of the change in the price over the next period is

```{math}
\begin{aligned}
\Ex_{t}[\Price_{t+1}-\Price_{t}] &= \Ex_{t}\left[\Ex_{t+1}[V^{*}]-\Ex_{t}[V^{*}]\right] \\
&= \Ex_{t}[V^{*}]-\Ex_{t}[V^{*}] \\
&= 0
\end{aligned}
```

because any information known at time {math}`t` must be known at time {math}`t+1` and so the only thing that should cause a *change* in prices should be the arrival of new information that was not known at time {math}`t`.

A stock's price is not such a martingale: by {eq}`eq:pteq`, its expected price rises each period by the return it must pay, net of the dividend, {math}`\Ex_{t}[\Price_{t+1}] = \Rfree \Price_{t} - \Ex_{t}[\dvdnd_{t+1}]`. What follows a martingale for a stock is its price plus the dividends it has paid, all discounted back to a fixed date.

Even that requires risk neutrality. With risk-averse investors, the martingale is the price plus past dividends, each weighted by the stochastic discount factor back to a fixed date {math}`0`: by the pricing equation,

```{math}
\Ex_{t}\left[\SDF_{0,t+1}\Price_{t+1} + \sum_{s=1}^{t+1}\SDF_{0,s}\dvdnd_{s}\right] = \SDF_{0,t}\Price_{t} + \sum_{s=1}^{t}\SDF_{0,s}\dvdnd_{s}.
```

Prices and dividends discounted at the riskless rate are a martingale only under "risk-neutral" probabilities, the true probabilities reweighted by the stochastic discount factor {cite:p}`harrisonKrepsMartingales`; under the true probabilities they need not be {cite:p}`leroyMartingale,lucas:assetpricing`. That is why a test of whether markets are efficient, in the sense of {cite:t}`famaEfficient`, is always also a test of a model of expected returns.

(PricesMoveTooMuch)=
## Do Prices Move Too Much?

Define the *ex post rational* price as the present value of the dividends that were actually paid:

```{math}
\tilde{\Price}_{t} \equiv \sum_{s=t+1}^{\infty} \Rfree^{t-s}\dvdnd_{s}.
```

By {eq}`eq:pstar`, {math}`\Price_{t}^{*} = \Ex_{t}[\tilde{\Price}_{t}]`, so {math}`\tilde{\Price}_{t} = \Price_{t}^{*} + \epsilon_{t}`, where {math}`\epsilon_{t}` is the error made at {math}`t` in forecasting {math}`\tilde{\Price}_{t}`. A rational forecast error cannot be predicted from anything known at {math}`t`, so its covariance with {math}`\Price_{t}^{*}` is zero, and

```{math}
:label: eq:varianceBound

\text{var}(\tilde{\Price}_{t}) = \text{var}(\Price_{t}^{*}) + \text{var}(\epsilon_{t}) \geq \text{var}(\Price_{t}^{*}).
```

A forecast cannot vary more than the thing it forecasts. {cite:t}`shillerExcessVol` and {cite:t}`leroyPorterBounds` found that U.S. stock prices vary far more than this allows. The ex post rational price, computed from a century of dividends, is a smooth trend, while actual prices swing widely around it; in Shiller's tests, the measures of price volatility exceeded their bounds by factors of five to thirteen.

There are two ways to read the violation. One is that prices contain something other than the expected present value of dividends: a bubble, the subject of the rest of this chapter. The other is that the discount rate is not constant. Prices then move with expected returns even when expected dividends do not, and {eq}`eq:varianceBound`, which assumed a constant {math}`\Rfree`, does not apply. The Campbell-Shiller approximation {eq}`eq:campbellShiller` makes the second reading testable: if dividend growth is hard to forecast, the price-dividend ratio must forecast returns. {cite:t}`cochraneDiscountRates` summarizes the evidence that it does, and that nearly all of the variation in the price-dividend ratio corresponds to variation in expected returns.

## Deterministic Bubbles

The no-bubbles condition, however, was simply *assumed*; we did not justify it with economic logic. Consider the following candidate process for {math}`\Price_{t}`:

```{math}
:label: eq:pbubble

\begin{aligned}
\Price_{t} &= \Price_{t}^{*}+B_{t} \\
B_{t+1} &= \Rfree B_{t}.
\end{aligned}
```

That is, price is equal to the fundamental price plus a "bubble" term {math}`B_{t}` which grows nonstochastically by the factor {math}`\Rfree` from period to period. The question at hand is whether this equation satisfies the first order condition {eq}`eq:pteq`. We can show that it does by starting with the formula for {math}`\Price_{t+1}` and working backwards:

```{math}
\begin{aligned}
\Price_{t+1} &= \Price_{t+1}^{*}+B_{t+1} \\
\Ex_{t}[\Price_{t+1}] &= \Ex_{t}[\Price_{t+1}^{*}]+ B_{t} \Rfree \\
\Ex_{t}[\Price_{t+1}] &= \Ex_{t}\left[\sum_{s=t+2}^{\infty}\Rfree^{t+1-s}\dvdnd_{s}\right]+ B_{t} \Rfree \\
\Ex_{t}[\Price_{t+1}]/\Rfree &= \Ex_{t}\left[\sum_{s=t+2}^{\infty}\Rfree^{t-s}\dvdnd_{s}\right]+ B_{t} \\
\underbrace{\Ex_{t}[\Price_{t+1}+\dvdnd_{t+1}]/\Rfree}_{= \Price_{t}} &= \Ex_{t}[\dvdnd_{t+1}/\Rfree] + \Ex_{t}\left[\sum_{s=t+2}^{\infty}\Rfree^{t-s}\dvdnd_{s}\right]+ B_{t} \\
\Price_{t} &= \Ex_{t}\left[\sum_{s=t+1}^{\infty}\Rfree^{t-s}\dvdnd_{s}\right]+ B_{t} \\
\Price_{t} &= \Price_{t}^{*}+ B_{t}
\end{aligned}
```

where the underbraced equality follows from {eq}`eq:pteq`.

In words, the first order condition has infinitely many solutions of the form {math}`\Price_{t}= \Price_{t}^{*}+B_{t}`. Nothing in the logic of the problem so far rules out a *rational deterministic bubble*, one whose size grows at the rate of interest forever. In principle, then, any level of the stock price is possible at period {math}`t`; all the theory implies is that *if a bubble exists*, its value must rise by the factor {math}`\Rfree` every period.

## Stochastically Bursting Bubbles

{cite:t}`blanchard:burstingbubbles` considers another possible candidate process for {math}`\Price_{t}`:

```{math}
:label: eq:pburst

\begin{aligned}
\Price_{t} &= \Price_{t}^{*}+B_{t} \\
B_{t+1} &=
\begin{cases}
(\Rfree/\LivPrb)B_{t} & \text{with probability } \LivPrb \\
0 & \text{with probability } \DiePrb = 1-\LivPrb
\end{cases}
\end{aligned}
```

Roll equation {eq}`eq:pburst` forward one period, and take its expectation as of time {math}`t`:

```{math}
\begin{aligned}
\Price_{t+1} &= \Price_{t+1}^{*}+B_{t+1} \\
\Ex_{t}[\Price_{t+1}] &= \Ex_{t}[\Price_{t+1}^{*}]+ B_{t}(\Rfree/\LivPrb) \LivPrb + (0)\DiePrb \\
\Ex_{t}[\Price_{t+1}] &= \Ex_{t}\left[\sum_{s=t+2}^{\infty}\Rfree^{t+1-s}\dvdnd_{s}\right]+ B_{t} \Rfree \\
\Ex_{t}[\Price_{t+1}]/\Rfree &= \Ex_{t}\left[\sum_{s=t+2}^{\infty}\Rfree^{t-s}\dvdnd_{s}\right]+ B_{t} \\
\Ex_{t}[\Price_{t+1}+\dvdnd_{t+1}]/\Rfree &= \Ex_{t}[\dvdnd_{t+1}/\Rfree] + \Ex_{t}\left[\sum_{s=t+2}^{\infty}\Rfree^{t-s}\dvdnd_{s}\right]+ B_{t} \\
\Price_{t} &= \Ex_{t}\left[\sum_{s=t+1}^{\infty}\Rfree^{t-s}\dvdnd_{s}\right]+ B_{t}
\end{aligned}
```

Thus, the model allows stochastic bubbles which, while they last, grow by the factor {math}`\Rfree/\LivPrb`, enough faster than {math}`\Rfree` to exactly compensate shareholders (in expected value terms) for their expected capital loss when the bubble collapses.

The probability that the bubble has burst by time {math}`t+s` adds the probability that it bursts in {math}`t+1`, the probability that it survives {math}`t+1` and bursts in {math}`t+2`, and so on:

```{math}
:label: eq:probburst

\text{Prob(burst by } t+s) = \DiePrb(1+\LivPrb+\LivPrb^{2}+\ldots+\LivPrb^{s-1}).
```

The sum is {math}`1-\LivPrb^{s}`, which goes to one as {math}`s` grows: a stochastic bubble bursts eventually with probability one. Its lifetime is random, with a geometric distribution: the probability that it is still alive after {math}`s` periods is {math}`\LivPrb^{s}`, and the expected number of periods until it bursts is {math}`1/\DiePrb`. The probability of survival falls by half every

```{math}
\frac{\log 2}{-\log \LivPrb}
```

periods, a little less than {math}`69.3/(100\DiePrb)`, which is the halving form of the [rule of 72](#fact:ruleof72). With a 5 percent chance of bursting each period, a bubble's chance of surviving halves every 13.5 periods, while its expected lifetime is 20 periods: the mean exceeds the half-life because a few bubbles last a very long time.

Both kinds of bubble are special cases of a general solution: adding to {math}`\Price_{t}^{*}` any process {math}`B_{t}` with {math}`\Ex_{t}[B_{t+1}] = \Rfree B_{t}` satisfies the first order condition {eq}`eq:pteq` {cite:p}`floodGarberBubbles,blanchardWatsonBubbles`. Other members of the family have been built to resemble the data. The "intrinsic" bubbles of {cite:t}`frootObstfeldIntrinsic` depend on dividends themselves, so that prices overreact to news about dividends. The bubbles of {cite:t}`evansPitfalls` collapse periodically to a small positive value and then grow again, and standard tests for bubbles miss them. {cite:t}`westSpecTest` tests for a bubble by comparing two estimates of the present-value relation that should agree if there is none, and {cite:t}`phillipsShiYuBubbles` date periods of explosive growth in the S&P 500.

(WhyBubblesCannotExist)=
## Arguments for Why Bubbles Cannot Exist

Note that the bubble term in equation {eq}`eq:pbubble` grows without bound in absolute value. It turns out that this fact rules out negative bubbles. To see why, note that if {math}`B_{t}` is negative and if the fundamental price {math}`\Price_{t}^{*}` is bounded, then eventually {math}`|B_{t}|` grows large enough so that the predicted price of a share is negative. But if share prices were negative, people could make themselves better off by simply throwing away their stock certificates. Thus, the restriction that prices must be positive rules out negative bubbles.

{cite:t}`dibaGrossmanTheory` turn this into a more striking result. If negative bubbles are impossible, then {math}`B_{t} \geq 0` always. Suppose that the bubble is zero at some date. Its expected value next period is then zero too, and a quantity that cannot be negative and is expected to be zero must be zero with probability one:

```{math}
:label: eq:dibaGrossman

B_{t} = 0 \Rightarrow \Ex_{t}[B_{t+1}] = \Rfree B_{t} = 0 \Rightarrow B_{t+1} = 0,
```

and the same holds in every later period. So a bubble cannot start: if one exists now, it has existed since the asset was first traded. Nor can a bubble that has burst restart. (The bubbles of {cite:t}`evansPitfalls` escape this by never collapsing all the way to zero.)

Bubbles can also be ruled out if there is a maximum possible price that the asset can have. Consider, for example, the question of whether there can be a bubble on the price of diamonds. Suppose that there is a fixed supply of natural diamonds in existence, but that artificial diamonds can be made at a cost {math}`\bar{\Price}` above the current market price. A bubble would eventually carry the market price past {math}`\bar{\Price}`, but nobody will pay more than {math}`\bar{\Price}` for a natural diamond when an artificial one costs {math}`\bar{\Price}`, so the price cannot rise beyond {math}`\bar{\Price}`. In the period before the bubble would pass {math}`\bar{\Price}`, then, the price cannot rise by the factor the bubble needs to earn the required return, so nobody holds the bubble then; and by the same logic nobody holds it in the period before that, or in any earlier period, today included. Thus, rational bubbles are ruled out for assets which are reproducible.

Two formal results make these arguments general. With finitely many traders, all rational and all sharing the same prior beliefs, there can be no bubble and no purely speculative trade {cite:p}`tiroleSpeculation`; that is the backward induction of the diamonds example in general form. With infinitely lived traders, {cite:t}`santosWoodfordBubbles` show that bubbles are impossible in a wide class of economies, in particular whenever the present value of the economy's aggregate endowment is finite, the infinite-horizon counterpart of an interest rate above the growth rate.

These results were derived for risk-neutral investors, but none depends on it. With risk-averse investors every argument goes through with the stochastic discount factor {math}`\SDF_{t,t+1}` in place of {math}`1/\Rfree`. A bubble is then any {math}`B_{t}` with

```{math}
\Ex_{t}[\SDF_{t,t+1}B_{t+1}] = B_{t},
```

and the arguments against negative bubbles, against bubbles that start, and against bubbles on assets that can be reproduced are unchanged.

There are also some general equilibrium arguments against bubbles, which basically boil down to the observation that if the value of the bubble is growing forever, its size will eventually exceed the size of the entire capital stock, and in that case productive capital will have been driven to zero because everybody owns the bubble instead of capital, which cannot make sense. The argument needs the interest rate to exceed the economy's growth rate: a bubble grows at the rate of interest {math}`\rfree`, so it outgrows the economy only if {math}`\rfree` exceeds the growth rate {math}`\pGro`, which in a steady state is also the growth rate of dividends. In a dynamically inefficient economy, where {math}`\rfree < \pGro`, as can happen in [Diamond's overlapping generations model](#sec:OLGModel), a bubble can survive in general equilibrium {cite:p}`tirole:bubbles`. The idea goes back to {cite:t}`samuelsonOLG`, whose money is a bubble: an asset that pays no dividend and has value only because each generation expects the next to accept it. {cite:t}`weilConfidence` shows that such a bubble can burst at random, as Blanchard's does. But {cite:t}`amszDynamicEfficiency` find that actual economies are dynamically efficient, which seems to close this route to a rational bubble.

More recent work finds room for bubbles even in dynamically efficient economies, through frictions in financial markets: bubbles that relax firms' borrowing constraints, and so can crowd investment in rather than out {cite:p}`martinVenturaBubbles`; bubbles that supply the liquidity firms need {cite:p}`farhiTiroleBubbly`; and a rational bubble that grows faster when the central bank raises interest rates to lean against it {cite:p}`galiBubbles`.

A separate literature explains episodes that look like bubbles without any rational bubble. When investors disagree, an asset's price includes the value of the option to resell it to someone more optimistic, so it can exceed every investor's own valuation {cite:p}`harrisonKrepsSpeculative,scheinkmanXiongOverconfidence`. Noise traders can make an asset risky to arbitrageurs, who therefore do not trade its mispricing away {cite:p}`delongNoiseTrader`, and arbitrageurs who cannot coordinate a sale may ride a bubble rather than attack it {cite:p}`abreuBrunnermeierBubbles`. {cite:t}`brunnermeierOehmkeBubbles` survey the field. {cite:t}`garberBubbles` reexamines the most famous early bubbles and finds fundamentals behind most of them, while {cite:t}`shillerExuberance` makes the case that modern markets have them.
