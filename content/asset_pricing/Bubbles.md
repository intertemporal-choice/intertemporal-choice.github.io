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

If this investor's only goal is to maximize the present discounted utility of consumption and the investor uses a discount factor of {math}`\Risky^{-1}` then we have

```{math}
\VFunc_{t}(M_{t}) = \max_{\{C_{t}\}} \uFunc(C_{t})+\Risky^{-1} \Ex_{t}\left[\VFunc_{t+1}\left((\Price_{t+1}+\dvdnd_{t+1})\left(\frac{M_{t}-C_{t}}{\Price_{t}}\right)\right)\right]
```

with FOC

```{math}
:label: eq:ceuler

\begin{aligned}
\uFunc^{\prime}(C_{t}) &= \Risky^{-1} \Ex_{t}\left[\left(\frac{\Price_{t+1}+\dvdnd_{t+1}}{\Price_{t}}\right)\VFunc^{\prime}_{t+1}(M_{t+1})\right] \\
\uFunc^{\prime}(C_{t}) &= \Risky^{-1} \Ex_{t}\left[\left(\frac{\Price_{t+1}+\dvdnd_{t+1}}{\Price_{t}}\right)\uFunc^{\prime}_{t+1}(C_{t+1})\right].
\end{aligned}
```

Now suppose that the investor is risk neutral ({math}`\uFunc(C) = C`) so that {math}`\uFunc^{\prime}(C_{t+1})=\uFunc^{\prime}(C_{t})=1`; {eq}`eq:ceuler` becomes

```{math}
:label: eq:pteq

\begin{aligned}
\Risky &= \Ex_{t}\left[\frac{\Price_{t+1}+\dvdnd_{t+1}}{\Price_{t}}\right] \\
\Price_{t} &= \Ex_{t}\left[\frac{\Price_{t+1}+\dvdnd_{t+1}}{\Risky} \right]
\end{aligned}
```

Of course, similar logic can be employed to show that

```{math}
\Price_{t+1} = \Ex_{t+1}[(\Price_{t+2}+\dvdnd_{t+2})/\Risky]
```

and we can use the law of iterated expectations to substitute repeatedly, obtaining

```{math}
\Price_{t} = \Ex_{t}\left[\sum_{s=t+1}^{T+1} \Risky^{t-s}\dvdnd_{s}\right] + \Risky^{-(T+1-t)}\Ex_{t}[\Price_{T+1}]
```

We usually assume the "no-bubbles" condition that says that {math}`\lim_{T \rightarrow \infty} \Ex_{t}[\Risky^{-(T+1-t)}\Price_{T+1}] = 0`. In this case it is clear that the equilibrium price must equal the present discounted value of dividends:

```{math}
\Price_{t}^{*} = \Ex_{t}\left[\sum_{s=t+1}^{\infty} \Risky^{t-s}\dvdnd_{s}\right]
```

This result is very similar to what emerges from the [Lucas Asset Pricing model](#sec:LucasAssetPrice), though there the stochastic discount factor plays the role that {math}`\Risky^{-1}` plays here.

Suppose now that dividends are expected to grow by a constant factor {math}`\PGro` henceforth. In that case we have

```{math}
\begin{aligned}
\Price_{t}^{*} &= \Ex_{t}\left[\sum_{s=t+1}^{\infty} \Risky^{t-s}\PGro^{s-t}\dvdnd_{t}\right] \\
&= \Ex_{t} \left[\sum_{s=t+1}^{\infty} (\PGro/\Risky)^{s-t}\dvdnd_{t}\right] \\
&= \dvdnd_{t} \left(\frac{\PGro/\Risky}{1-\PGro/\Risky}\right) \\
&\approx \dvdnd_{t} \left(\frac{1}{\risky-\pGro}\right),
\end{aligned}
```

where the final approximation uses log rates: {math}`\risky \equiv \log \Risky` and {math}`\pGro \equiv \log \PGro`. This is known as the "Gordon formula." The tricky thing in applying the formula is to know what to assume for {math}`\Risky` and {math}`\PGro`. The return factor {math}`\Risky` should be the one "appropriate" for discounting risky quantities. The usual assumption is that {math}`\risky = \rfree+\EpremLog`, where {math}`\rfree` is the log of the return factor on perfectly safe (riskfree) assets and {math}`\EpremLog` is the premium that people demand as compensation for the risk inherent in future dividends.

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

A stock's price is not such a martingale: by {eq}`eq:pteq`, its expected price rises each period by the return it must pay, net of the dividend, {math}`\Ex_{t}[\Price_{t+1}] = \Risky \Price_{t} - \Ex_{t}[\dvdnd_{t+1}]`. What follows a martingale for a stock is its price plus the dividends it has paid, all discounted back to a fixed date.

## Deterministic Bubbles

Note, however, that we simply *assumed* the no-bubbles condition; we did not justify it with economic logic. Consider the following candidate process for {math}`\Price_{t}`:

```{math}
:label: eq:pbubble

\begin{aligned}
\Price_{t} &= \Price_{t}^{*}+B_{t} \\
B_{t+1} &= \Rfree B_{t}.
\end{aligned}
```

That is, price is equal to the fundamental price plus a "bubble" term {math}`B_{t}` which grows nonstochastically by the factor {math}`\Rfree` from period to period. (Here we will assume that there is no risk premium, {math}`\EpremLog = 0`, which would be true in equilibrium for risk-neutral consumers.) The question at hand is whether this equation satisfies the first order condition {eq}`eq:pteq`. We can show that it does by starting with the formula for {math}`\Price_{t+1}` and working backwards:

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

In words, this says that the first order condition has an infinite number of solutions of the form {math}`\Price_{t}= \Price_{t}^{*}+B_{t}`. Thus, nothing about the logic of the problem thus far rules out a *rational deterministic bubble*, which is a bubble whose size grows at the rate of interest forever. Thus, in principle any level of the stock price is possible at period {math}`t`; all that the theory implies is that *if a bubble exists*, its value must rise by a factor {math}`\Rfree` in every period.

## Stochastically Bursting Bubbles

{cite:t}`blanchard:burstingbubbles` considers another possible candidate process for {math}`\Price_{t}`:

```{math}
:label: eq:pburst

\Price_{t} = \Price_{t}^{*}+B_{t}
```

```{math}
B_{t+1} =
\begin{cases}
(\Rfree/\LivPrb)B_{t} & \text{with probability } \LivPrb \\
0 & \text{with probability } \DiePrb = 1-\LivPrb
\end{cases}
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

Note that the probability that the bubble has burst by time {math}`t+s` is the probability that it bursts in {math}`t+1` plus the probability that it survives {math}`t+1` and bursts in {math}`t+2`, and so on:

```{math}
:label: eq:pnotburst

\text{Prob(burst by } t+s) = \DiePrb(1+\LivPrb+\LivPrb^{2}+\ldots+\LivPrb^{s-1}).
```

Summing the geometric series collapses the right-hand side of {eq}`eq:pnotburst` to {math}`1-\LivPrb^{s}`. Since {math}`\LivPrb<1`, letting {math}`s \rightarrow \infty` drives {math}`\LivPrb^{s}` to zero, so the probability that the bubble has burst by time {math}`t+s` approaches one: a stochastic bubble bursts eventually with probability one.

(WhyBubblesCannotExist)=
## Arguments for Why Bubbles Cannot Exist

Note that the bubble term in equation {eq}`eq:pbubble` rises without bound. It turns out that this fact rules out negative bubbles. To see why, note that if {math}`B_{t}` is negative and if the fundamental price {math}`\Price_{t}^{*}` is bounded, then eventually {math}`B_{t}` grows large enough so that the predicted price of a share is negative. But if share prices were negative, people could make themselves better off by simply throwing away their stock certificates. Thus, the restriction that prices must be positive rules out negative bubbles.

Bubbles can also be ruled out if there is a maximum possible price that the asset can have. Consider, for example, the question of whether there can be a bubble on the price of diamonds. Suppose that there is a fixed supply of natural diamonds in existence, but that artificial diamonds can be made at a cost {math}`\bar{\Price}` above the current market price. A bubble would eventually carry the market price past {math}`\bar{\Price}`, but nobody will pay more than {math}`\bar{\Price}` for a natural diamond when an artificial one costs {math}`\bar{\Price}`, so the price cannot rise beyond {math}`\bar{\Price}`. In the period before the bubble would pass {math}`\bar{\Price}`, then, the price cannot rise by the factor the bubble needs to earn the required return, so nobody holds the bubble then; and by the same logic nobody holds it in the period before that, or in any earlier period, today included. Thus, rational bubbles are ruled out for assets which are reproducible.

We assumed, in deriving these results, that the investor's utility function was linear. It is more difficult to justify rational bubbles in an economy with risk averse investors.

There are also some general equilibrium arguments against bubbles, which basically boil down to the observation that if the value of the bubble is growing forever, its size will eventually exceed the size of the entire capital stock, and in that case productive capital will have been driven to zero because everybody owns the bubble instead of capital, which cannot make sense.
