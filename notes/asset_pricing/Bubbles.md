(sec:Bubbles)=

# Canonical Asset Pricing and Rational Bubbles

## Prices as the PDV of Dividends

Denoting dividends as {math}`\mathbf{r}_{t}` for a stock with a market price of {math}`\mathsf{P}_{t}` per share, consider an investor who owns {math}`K_{t}` shares at the beginning of period {math}`t` yielding total wealth {math}`M_{t}=\mathsf{P}_{t}K_{t}+\mathbf{r}_{t}K_{t}`. Assuming the investor has no other source of income (no labor income, for instance) the investor's budget constraint will be

```{math}
\begin{aligned}
M_{t}&=\underbrace{\mathbf{r}_{t}K_{t}+\mathsf{P}_{t}K_{t}}_{\text{Total resources}} \\
    &= \underbrace{K_{t+1}\mathsf{P}_{t}+C_{t}}_{\text{Uses of resources}}
\end{aligned}
```

which can be rearranged to indicate how many shares the investor will own next period, as a function of this period's wealth and consumption:

```{math}
\begin{aligned}
K_{t+1} &= \frac{M_{t}-C_{t}}{\mathsf{P}_{t}} \\
M_{t+1} &= K_{t+1}(\mathsf{P}_{t+1}+\mathbf{r}_{t+1}) \\
        &= (\mathsf{P}_{t+1}+\mathbf{r}_{t+1})\left(\frac{M_{t}-C_{t}}{\mathsf{P}_{t}}\right).
\end{aligned}
```

If this investor's only goal is to maximize the present discounted utility of consumption and the investor uses a discount factor of {math}`\mathbf{R}^{-1}` then we have

```{math}
\mathrm{V}_{t}(M_{t}) = \max_{\{C_{t}\}} \mathrm{u}(C_{t})+\mathbf{R}^{-1} \mathbb{E}_{t}\left[\mathrm{V}_{t+1}\left((\mathsf{P}_{t+1}+\mathbf{r}_{t+1})\left(\frac{M_{t}-C_{t}}{\mathsf{P}_{t}}\right)\right)\right]
```

with FOC

```{math}
:label: eq:ceuler

\begin{aligned}
\mathrm{u}^{\prime}(C_{t}) &= \mathbf{R}^{-1} \mathbb{E}_{t}\left[\left(\frac{\mathsf{P}_{t+1}+\mathbf{r}_{t+1}}{\mathsf{P}_{t}}\right)\mathrm{V}^{\prime}_{t+1}(M_{t+1})\right] \\
\mathrm{u}^{\prime}(C_{t}) &= \mathbf{R}^{-1} \mathbb{E}_{t}\left[\left(\frac{\mathsf{P}_{t+1}+\mathbf{r}_{t+1}}{\mathsf{P}_{t}}\right)\mathrm{u}^{\prime}_{t+1}(C_{t+1})\right].
\end{aligned}
```

Now suppose that the investor is risk neutral ({math}`\mathrm{u}(C) = C`) so that {math}`\mathrm{u}^{\prime}(C_{t+1})=\mathrm{u}^{\prime}(C_{t})=1`; {eq}`eq:ceuler` becomes

```{math}
:label: eq:pteq

\begin{aligned}
\mathbf{R} &= \mathbb{E}_{t}\left[\left(\frac{\mathsf{P}_{t+1}+\mathbf{r}_{t+1}}{\mathsf{P}_{t}}\right)\mathrm{u}^{\prime}_{t+1}(C_{t+1})\right] \\
\mathsf{P}_{t} &= \mathbb{E}_{t}\left[\frac{\mathsf{P}_{t+1}+\mathbf{r}_{t+1}}{\mathbf{R}} \right]
\end{aligned}
```

Of course, similar logic can be employed to show that

```{math}
\mathsf{P}_{t+1} = \mathbb{E}_{t+1}[(\mathsf{P}_{t+2}+\mathbf{r}_{t+2})/\mathbf{R}]
```

and we can use the law of iterated expectations to substitute repeatedly, obtaining

```{math}
\mathsf{P}_{t} = \mathbb{E}_{t}\left[\sum_{s=t+1}^{T+1} \mathbf{R}^{t-s}\mathbf{r}_{s}\right] + \mathbf{R}^{-(T+1-t)}\mathbb{E}_{t}[\mathsf{P}_{T+1}]
```

We usually assume the "no-bubbles" condition that says that {math}`\lim_{T \rightarrow \infty} \mathbb{E}_{t}[\mathbf{R}^{-(T+1-t)}\mathsf{P}_{T+1}] = 0`. In this case it is clear that the equilibrium price must equal the present discounted value of dividends:

:::{margin}
Compare this to the Lucas Asset Pricing model, which is very similar.
:::

```{math}
\mathsf{P}_{t}^{*} = \mathbb{E}_{t}\left[\sum_{s=t+1}^{\infty} \mathbf{R}^{t-s}\mathbf{r}_{s}\right]
```

Suppose now that dividends are expected to grow by a constant factor {math}`\Gamma` henceforth. In that case we have

```{math}
\begin{aligned}
\mathsf{P}_{t}^{*} &= \mathbb{E}_{t}\left[\sum_{s=t+1}^{\infty} \mathbf{R}^{t-s}\Gamma^{s-t}\mathbf{r}_{t}\right] \\
&= \mathbb{E}_{t} \left[\sum_{s=t+1}^{\infty} (\Gamma/\mathbf{R})^{s-t}\mathbf{r}_{t}\right] \\
&= \mathbf{r}_{t} \left(\frac{\Gamma/\mathbf{R}}{1-\Gamma/\mathbf{R}}\right) \\
&\approx \mathbf{r}_{t} \left(\frac{1}{\mathbf{r}-\gamma}\right),
\end{aligned}
```

which is known as the "Gordon formula." The tricky thing in applying the formula is to know what to assume for {math}`\mathbf{R}` and {math}`\Gamma`. The interest rate {math}`\mathbf{R}` should be the interest rate "appropriate" for discounting risky quantities. The usual assumption is that {math}`\mathbf{R} = \mathsf{R}+\Phi` where {math}`\mathsf{R}` is the rate of return on perfectly safe (riskfree) assets and {math}`\Phi` is the rate-of-return premium that people demand as compensation for the risk inherent in future dividends.

## The Random Walk of Asset Pricing

### The Law of Iterated Expectations

Suppose that a security price at time {math}`t`, {math}`\mathsf{P}_{t}`, can be written as the rational expectation of some "fundamental value" {math}`V^{*}` conditional on information available at time {math}`t` (the usual example of the "fundamental value" in question is the present discounted value of dividends). Then we have

```{math}
\mathsf{P}_{t} = \mathbb{E}_{t}[V^{*}].
```

The same formula holds in period {math}`t+1`:

```{math}
\mathsf{P}_{t+1} = \mathbb{E}_{t+1}[V^{*}].
```

Then the expectation of the change in the price over the next period is

```{math}
\begin{aligned}
\mathbb{E}_{t}[\mathsf{P}_{t+1}-\mathsf{P}_{t}] &= \mathbb{E}_{t}\left[\mathbb{E}_{t+1}[V^{*}]-\mathbb{E}_{t}[V^{*}]\right] \\
&= \mathbb{E}_{t}[V^{*}]-\mathbb{E}_{t}[V^{*}] \\
&= 0
\end{aligned}
```

because any information known at time {math}`t` must be known at time {math}`t+1` and so the only thing that should cause a *change* in prices should be the arrival of new information that was not known at time {math}`t`.

## Deterministic Bubbles

Note, however, that we simply *assumed* the no-bubbles condition; we did not justify it with economic logic. Consider the following candidate process for {math}`\mathsf{P}_{t}`:

```{math}
:label: eq:pbubble

\begin{aligned}
\mathsf{P}_{t} &= \mathsf{P}_{t}^{*}+B_{t} \\
B_{t+1} &= \mathsf{R} B_{t}.
\end{aligned}
```

That is, price is equal to the fundamental price plus a "bubble" term {math}`B_{t}` which grows nonstochastically at rate {math}`\mathsf{R}` from period to period. (Here we will assume that the risk premium {math}`\Phi` is zero, which would be true in equilibrium for risk-neutral consumers). The question at hand is whether this equation satisfies the first order condition {eq}`eq:pteq`. We can show that it does by starting with the formula for {math}`\mathsf{P}_{t+1}` and working backwards:

```{math}
\begin{aligned}
\mathsf{P}_{t+1} &= \mathsf{P}_{t+1}^{*}+B_{t+1} \\
\mathbb{E}_{t}[\mathsf{P}_{t+1}] &= \mathbb{E}_{t}[\mathsf{P}_{t+1}^{*}]+ B_{t} \mathsf{R} \\
\mathbb{E}_{t}[\mathsf{P}_{t+1}] &= \mathbb{E}_{t}\left[\sum_{s=t+2}^{\infty}\mathsf{R}^{t+1-s}\mathbf{r}_{s}\right]+ B_{t} \mathsf{R} \\
\mathbb{E}_{t}[\mathsf{P}_{t+1}]/\mathsf{R} &= \mathbb{E}_{t}\left[\sum_{s=t+2}^{\infty}\mathsf{R}^{t-s}\mathbf{r}_{s}\right]+ B_{t} \\
\underbrace{\mathbb{E}_{t}[\mathsf{P}_{t+1}+\mathbf{r}_{t+1}]/\mathsf{R}}_{= \mathsf{P}_{t}} &= \mathbb{E}_{t}[\mathbf{r}_{t+1}/\mathsf{R}] + \mathbb{E}_{t}\left[\sum_{s=t+2}^{\infty}\mathsf{R}^{t-s}\mathbf{r}_{s}\right]+ B_{t} \\
\mathsf{P}_{t} &= \mathbb{E}_{t}\left[\sum_{s=t+1}^{\infty}\mathsf{R}^{t-s}\mathbf{r}_{s}\right]+ B_{t} \\
\mathsf{P}_{t} &= \mathsf{P}_{t}^{*}+ B_{t}
\end{aligned}
```

where the underbraced equality follows from {eq}`eq:pteq`.

In words, this says that the first order condition has an infinite number of solutions of the form {math}`\mathsf{P}_{t}= \mathsf{P}_{t}^{*}+B_{t}`. Thus, nothing about the logic of the problem thus far rules out a *rational deterministic bubble*, which is a bubble whose size grows at the rate of interest forever. Thus, in principle any level of the stock price is possible at period {math}`t`; all that the theory implies is that *if a bubble exists*, its value must rise by a factor {math}`\mathsf{R}` in every period.

## Stochastically Bursting Bubbles

{cite:t}`blanchard:burstingbubbles` considers another possible candidate process for {math}`P`:

```{math}
:label: eq:pburst

\mathsf{P}_{t} = \mathsf{P}_{t}^{*}+q_{t}
```

```{math}
q_{t+1} =
\begin{cases}
(\mathsf{R}/\alpha)q_{t} & \text{with probability $\alpha$} \\
0 & \text{with probability $1-\alpha$}
\end{cases}
```

Roll equation {eq}`eq:pburst` forward one period, and take its expectation as of time {math}`t`:

```{math}
\begin{aligned}
\mathsf{P}_{t+1} &= \mathsf{P}_{t+1}^{*}+q_{t+1} \\
\mathbb{E}_{t}[\mathsf{P}_{t+1}] &= \mathbb{E}_{t}[\mathsf{P}_{t+1}^{*}]+ q_{t}(\mathsf{R}/\alpha) \alpha + (0)(1-\alpha) \\
\mathbb{E}_{t}[\mathsf{P}_{t+1}] &= \mathbb{E}_{t}\left[\sum_{s=t+2}^{\infty}\mathsf{R}^{t+1-s}\mathbf{r}_{s}\right]+ q_{t} \mathsf{R} \\
\mathbb{E}_{t}[\mathsf{P}_{t+1}]/\mathsf{R} &= \mathbb{E}_{t}\left[\sum_{s=t+2}^{\infty}\mathsf{R}^{t-s}\mathbf{r}_{s}\right]+ q_{t} \\
\mathbb{E}_{t}[\mathsf{P}_{t+1}+\mathbf{r}_{t+1}]/\mathsf{R} &= \mathbb{E}_{t}[\mathbf{r}_{t+1}/\mathsf{R}] + \mathbb{E}_{t}\left[\sum_{s=t+2}^{\infty}\mathsf{R}^{t-s}\mathbf{r}_{s}\right]+ q_{t} \\
\mathsf{P}_{t} &= \mathbb{E}_{t}\left[\sum_{s=t+1}^{\infty}\mathsf{R}^{t-s}\mathbf{r}_{s}\right]+ q_{t}
\end{aligned}
```

Thus, the model allows stochastic bubbles which, during the period of their inflation, rise at a rate that is enough faster than the gross interest rate to exactly compensate shareholders (in expected value terms) for their expected capital loss when the bubble collapses.

Note that the probability that the bubble has burst by time {math}`t+s` is the probability that it bursts in {math}`t+1` plus the probability that it bursts in {math}`t+2` given that it did not burst in {math}`t+1`, and so on:

```{math}
:label: eq:pnotburst

\text{Prob(burst by t+s)} = (1-\alpha)(1+\alpha+\alpha^{2}+\ldots+\alpha^{s-1}).
```

As we let {math}`s \rightarrow \infty`, then since {math}`\alpha<1`, the RHS of {eq}`eq:pnotburst` converges to {math}`1/(1-\alpha)`. Thus, the probability that the bubble has burst by time {math}`t+s`, as {math}`s` goes to infinity, approaches one.

(WhyBubblesCannotExist)=
## Arguments for Why Bubbles Cannot Exist

Note that the bubble term in equation {eq}`eq:pbubble` rises without bound. It turns out that this fact rules out negative bubbles. To see why, note that if {math}`B_{t}` is negative and if the fundamental price {math}`\mathsf{P}_{t}^{*}` is bounded, then eventually {math}`B_{t}` grows large enough so that the predicted price of a share is negative. But if share prices were negative, people could make themselves better off by simply throwing away their stock certificates. Thus, the restriction that prices must be positive rules out negative bubbles.

Bubbles can also be ruled out if there is a maximum possible price that the asset can have. Consider, for example, the question of whether there can be a bubble on the price of diamonds. Suppose that there is a fixed supply of natural diamonds in existence, but suppose that new artificial diamonds can be made at some price {math}`\bar{\mathsf{P}}>4\mathsf{P}_{t}`, that is diamonds can be made at a cost 4 times higher than the current market price. But if there is a bubble, then it will imply that eventually the market price would exceed {math}`\bar{\mathsf{P}}`. At that point, nobody will be willing to pay {math}`\mathsf{P}_{t}>\bar{\mathsf{P}}` for natural diamonds, so the bubble's price cannot keep rising beyond {math}`\bar{\mathsf{P}}`. Thus, rational bubbles are ruled out for assets which are reproducible.

We assumed, in deriving these results, that the investor's utility function was linear. It is more difficult to justify rational bubbles in an economy with risk averse investors.

There are also some general equilibrium arguments against bubbles, which basically boil down to the observation that if the value of the bubble is growing forever, its size will eventually exceed the size of the entire capital stock, and in that case productive capital will have been driven to zero because everybody owns the bubble instead of capital, which cannot make sense.
