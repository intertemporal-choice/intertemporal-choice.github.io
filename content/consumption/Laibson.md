(sec:Laibson)=
# The Laibson Model of Time Inconsistency

This section provides a simple example of a discrete-time solution to the problem of a consumer with a self-control problem *à la* {cite:t}`laibson:goldeneggs`.[^laibson-notes]

[^laibson-notes]: Laibson's own lecture notes are available on his website, and are very good; as of this writing, they are in lecture 6 of his course 2010c, handouts, lecture06.

Suppose a value function {math}`\vFunc_{t+1}(m_{t+1})` exists for period {math}`t+1`. Then for any period-{math}`t` consumption function {math}`\pmb{\chi}_{t}` we can define

```{math}
:label: eq:bv

\begin{aligned}
{\vFunc}_{t}(m_{t};\pmb{\chi}_{t}) & = \uFunc(\pmb{\chi}_{t}(m_{t})) + \phantom{\delta} \Discount  \Ex_{t}[{\vFunc}_{t+1}((m_{t}-\pmb{\chi}_{t}(m_{t}))\Rfree+y_{t+1})]
\\ {\mathfrak{v}}_{t}(m_{t};\pmb{\chi}_{t}) & = \uFunc(\pmb{\chi}_{t}(m_{t})) +          \delta  \Discount  \Ex_{t}[{\vFunc}_{t+1}((m_{t}-\pmb{\chi}_{t}(m_{t}))\Rfree+y_{t+1})]
\end{aligned}
```

Notice that these functions are well defined for any consumption function {math}`\pmb{\chi}_{t}(m_{t})` that is feasible; they are *not* Bellman equations because they do not assume that the consumption function {math}`\pmb{\chi}_{t}` is optimal. For example, these functions would be well defined for {math}`\pmb{\chi}_{t}(m_{t}) = m_{t}`, or for {math}`\pmb{\chi}_{t}(m_{t})=1`, or for many other potential consumption rules.

What these functions capture is the value of behaving according to the rule {math}`\pmb{\chi}_{t}` in the current period, under two possible assumptions about discounting of the future: Either next period's value is discounted by the factor {math}`\Discount` (for {math}`\vFunc_{t}`) or by {math}`\delta \Discount` (for {math}`\mathfrak{v}_{t}`).

Now consider two possible candidates for {math}`\pmb{\chi}_{t}`:

```{math}
:label: eq:cexpvshyp

\begin{aligned}
\mathbf{c}_{t}(m_{t}) & = \argmax_{c}~~ \uFunc(c) +  \phantom{\delta} \Discount \Ex_{t}[\vFunc_{t+1}((m_{t}-c)\Rfree+y_{t+1})]
\\  \mathfrak{c}_{t}(m_{t}) & = \argmax_{c}~~ \uFunc(c) +           \delta  \Discount \Ex_{t}[\vFunc_{t+1}((m_{t}-c)\Rfree+y_{t+1})]
\end{aligned}
```

If we solve the problem recursively using {math}`\pmb{\chi}=\mathbf{c}` in every period, we obtain the standard time consistent solution. (Think about why).

The Laibson alternative is to suppose that there is something special about "now": Next period's value is discounted not only by the standard geometric discount factor {math}`\Discount`, but also by an extra factor {math}`\delta` (Laibson argues that at an annual frequency the appropriate value of {math}`\delta` is about 0.7). This may reflect the fact that certain areas of the brain associated with emotional rewards are activated only by instant gratification, and are not activated by thoughts of future gratification (see, e.g., {cite:t}`laibsonNeuro`).

It is clear from comparing the equations in {eq}`eq:cexpvshyp` that the consumer with Laibson preferences will consume more in the current period, because he values future rewards less.

More insight about the solution can be obtained from the modified Euler equation that can be derived for the Laibson problem. This is derived as follows.

Note first that if {math}`\pmb{\chi}_{t} = \mathfrak{c}_{t}` the [Envelope theorem](#sec:Envelope) implies that

```{math}
\mathfrak{v}_{t}^{m}(m_{t}) = \uFunc^{\prime}(c_{t})
```

while the first order condition from the maximization problem implies that

```{math}
:label: eq:foc

\uFunc^{\prime}(c_{t}) = \delta \Rfree\Discount \Ex_{t}[\vFunc_{t+1}^{m}(m_{t+1})]
```

Now note that for {math}`\pmb{\chi}_{t}=\mathfrak{c}_{t}` there is a simple identity linking {math}`\vFunc` and {math}`\mathfrak{v}`:

```{math}
:label: eq:dbv

\delta \vFunc_{t} = \mathfrak{v}_{t} - (1-\delta) \uFunc(\mathfrak{c}_{t}(m_{t}))
```

(to see this, multiply the first equation in {eq}`eq:bv` by {math}`\delta` and note that the difference between the result and the second equation is {math}`(1-\delta) \uFunc(c_{t})`). Now differentiate {eq}`eq:dbv`

```{math}
\delta \vFunc_{t}^{m} = \mathfrak{v}_{t}^{m} - (1-\delta) \uFunc^{\prime}(c_{t})\mathfrak{c}_{t}^{m}(m_{t})
```

and substitute the envelope relation {math}`\mathfrak{v}_{t}^{m}(m_{t}) = \uFunc^{\prime}(c_{t})` to express the marginal long-run value of wealth in terms of the marginal utility of consumption,

```{math}
:label: eq:dvm

\delta \vFunc_{t}^{m}(m_{t}) = \left(1-(1-\delta)\mathfrak{c}_{t}^{m}(m_{t})\right)\uFunc^{\prime}(c_{t}).
```

Advancing {eq}`eq:dvm` by one period and substituting it into {eq}`eq:foc` yields the modified Euler equation,

```{math}
:label: eq:LaibEul

\uFunc^{\prime}(c_{t}) = \Rfree\Discount \Ex_{t}\left[\left(1-(1-\delta)\mathfrak{c}_{t+1}^{m}(m_{t+1})\right)\uFunc^{\prime}(c_{t+1})\right].
```

If {math}`\delta=1`, this collapses to the usual consumption Euler equation {math}`\uFunc^{\prime}(c_{t}) = \Rfree\Discount \Ex_{t}[\uFunc^{\prime}(c_{t+1})]`. However, if {math}`\delta < 1` (the Laibson case), the equation says several interesting things. First, note that since {math}`(1-\delta)` and {math}`\uFunc^{\prime}(c_{t+1})` and {math}`\mathfrak{c}^{m}_{t+1}` are all positive, the contribution of the "Laibson" term in {eq}`eq:LaibEul` is to reduce the RHS of the equation. In order to match a lower RHS, the LHS must be smaller. But a smaller marginal utility of consumption implies a higher level of consumption, so the Laibson consumer spends more.

Second, notice that the magnitude of the "present-bias" effect depends on the size of next period's marginal propensity to consume {math}`\mathfrak{c}_{t+1}^{m}`. If the MPC is small, the size of the Laibson bias will be small. The reason is transparent if the bracketed term in {eq}`eq:LaibEul` is rewritten as

```{math}
1-(1-\delta)\mathfrak{c}_{t+1}^{m} = \delta \mathfrak{c}_{t+1}^{m} + (1-\mathfrak{c}_{t+1}^{m}),
```

which shows that the effective discount factor applied to next period's marginal utility is a weighted average of the short-horizon factor {math}`\delta \Discount` and the long-horizon factor {math}`\Discount`. The weight on the short-horizon factor is next period's marginal propensity to consume {math}`\mathfrak{c}_{t+1}^{m}` and the weight on the long-horizon factor is next period's marginal propensity to save {math}`1-\mathfrak{c}_{t+1}^{m}`. Resources that the next-period self will spend immediately get discounted at the present-biased rate, while resources that the next-period self will pass along to still-later selves get discounted geometrically. A consumer whose next-period MPC is near zero therefore behaves almost like an exponential discounter.

Finally, notice that this model nicely captures the commonplace psychological tension in which the cost of deviating from the optimal plan in a single period may be trivially small ("eating dessert this one time will not make me fat"), but the consequences of perpetual deviation could be quite large ("but if I give in to temptation this time, maybe that means I will always give in.")
