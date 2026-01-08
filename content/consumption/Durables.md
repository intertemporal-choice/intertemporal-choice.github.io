(sec:Durables)=

# Durables

The consumer's goal is to

:::{margin}
Define "durable."
:::

```{math}
\max \sum_{s=t}^{T} \beta^{s-t} \uFunc(c_{s},d_{s})
```

where {math}`d_{s}` is the stock of the durable good, and all other variables are as usually defined.

We will assume that the stock of the durable good evolves over time according to

:::{margin}
Discuss alternative: "one-hoss-shay" depreciation: small prob in each period that durable completely dies. Harder to analyze, though there is a lit that does it.
:::

```{math}
:label: eq:zeqn

d_{t+1} = (1-\delta)d_{t}+{x}_{t+1},
```

where {math}`{x}_{t}` is period-t eXpenditure on the durable good and {math}`\delta` is the durable good's depreciation rate (a good with a lower value of {math}`\delta` is said to be "more durable").

:::{margin}
Note features of reality left out: no asymmetry between buying and selling the durable good (i.e. there is no restriction saying {math}`{x}_{t}>0`).
:::

The dynamic budget constraint is

:::{margin}
Only difference is must subtract expenditures on durables.
:::

```{math}
:label: eq:Dur-xaccum

{m}_{t+1} = ({m}_{t}-c_{t}-{x}_{t})\Rfree + y_{t+1}.
```

Bellman's equation is

:::{margin}
The reason {math}`d_{t-1}` is the state is that the level of durables in period {math}`t` is not determined until you choose spending on durables in that period.
:::

```{math}
\vFunc_{t}({m}_{t},d_{t-1}) = \max_{\{c_{t},{x}_{t}\}} \left[\uFunc(c_{t},d_{t}) + \beta \vFunc_{t+1}({m}_{t+1},d_{t})\right],
```

or, equivalently,

:::{margin}
Difference is that in second version {math}`d_{t}` is treated as control.
:::

```{math}
:label: eq:bell

\vFunc_{t}({m}_{t},d_{t-1}) = \max_{\{c_{t},d_{t}\}} \left[\uFunc(c_{t},d_{t}) + \beta \vFunc_{t+1}({m}_{t+1},d_{t})\right],
```

subject to

```{math}
{m}_{t+1} = \left({m}_{t}-c_{t}-\overbrace{(d_{t}-(1-\delta)d_{t-1})}^{={x}_{t}}\right)\Rfree+y_{t+1}
```

or (substituting this into {eq}`eq:bell`),

```{math}
\vFunc_{t}({m}_{t},d_{t-1}) = \max_{\{c_{t},d_{t}\}} \left\{\uFunc(c_{t},d_{t}) + \beta \vFunc_{t+1}(({m}_{t}-c_{t}-(d_{t}-(1-\delta)d_{t-1}))\Rfree+y_{t+1},d_{t})\right\}.
```

Since this equation has two control variables, {math}`c_{t}` and {math}`d_{t}`, there are two first order conditions:

wrt {math}`c_{t}`:

```{math}
\begin{aligned}
\uFunc_{t}^{c} - \Rfree\beta \vFunc^{{m}}_{t+1}& = 0 \\
\uFunc_{t}^{c}& = \Rfree\beta \vFunc^{{m}}_{t+1}
\end{aligned}
```

wrt {math}`d_{t}`:

```{math}
:label: eq:ud

\uFunc_{t}^{d} = \beta(\Rfree \vFunc_{t+1}^{{m}} - \vFunc^{d}_{t+1}) = \Rfree\beta \vFunc_{t+1}^{{m}}-\beta \vFunc^{d}_{t+1}.
```

Note that when taking the derivative with respect to {math}`c_{t}` you assume that {math}`\partial d_{t}/\partial c_{t} = 0` and vice versa. Although the first order conditions will define a relationship between the *optimal* values of {math}`c_{t}` and {math}`d_{t}`, there is no *mechanical* link that applies at this point.

Now we want to apply the Envelope theorem. Basically, the Envelope theorem says that at the optimal levels of the control variables the partial derivative of the entire value function with respect to each control variable is zero. This means that when taking the derivative with respect to a *state* variable you can simply ignore all terms that involve {math}`\partial c_{t}/ \partial {m}_{t}, \partial d_{t} / \partial {m}_{t}, \partial c_{t} / \partial d_{t-1},` and {math}`\partial d_{t} / \partial d_{t-1}.` So, for example, the full expression for the derivative of the value function with respect to {math}`{m}_{t}` is:

```{math}
:label: eq:vmt

\begin{aligned}
\vFunc_{t}^{{m}} & = \frac{\partial \uFunc(c_{t},d_{t})}{\partial c_{t}}
                \frac{\partial c_{t}}{\partial {m}_{t}}
          + \frac{\partial \uFunc(c_{t},d_{t})}{\partial d_{t}}
                \frac{\partial d_{t}}{\partial {m}_{t}} \\
      &  + \left[\frac{\partial {m}_{t+1}}{\partial {m}_{t}}
          +       \frac{\partial {m}_{t+1}}{\partial c_{t}}
                      \frac{\partial c_{t}}{\partial {m}_{t}}
          +       \frac{\partial {m}_{t+1}}{\partial d_{t}}
                      \frac{\partial d_{t}}{\partial {m}_{t}}
                \right] \beta \vFunc^{{m}}_{t+1} + \beta
                      \vFunc^{d}_{t+1} \frac{\partial d_{t}}{\partial
                      {m}_{t}}
\end{aligned}
```

but the Envelope theorem tells us to ignore all the terms that involve {math}`\partial c_{t}/\partial {m}_{t}` or {math}`\partial d_{t}/\partial {m}_{t}`; then because the only term in that whole mess above that does *not* involve either {math}`\partial c_{t}/\partial {m}_{t}` or {math}`\partial d_{t}/\partial {m}_{t}` is {math}`\partial {m}_{t+1}/\partial {m}_{t} = \Rfree` we have:

```{math}
:label: eq:vxtEqvxtp1

\vFunc_{t}^{{m}} = \Rfree \beta \vFunc_{t+1}^{{m}}
```

Applying the same Envelope theorem logic for {math}`d_{t-1}` yields:[^derivative-note]

[^derivative-note]: Both here and in {eq}`eq:vmt`, the derivative {math}`\vFunc^{d}_{t}` should be understood as a differentiation with respect to {math}`d_{t-1}`.

```{math}
:label: eq:vdvsvx

\begin{aligned}
\vFunc_{t}^{d}  & = \Rfree(1-\delta) \beta \vFunc^{{m}}_{t+1} \\
     & = (1-\delta)  \Rfree \beta \vFunc_{t+1}^{{m}} \\
     & = (1-\delta) \vFunc^{{m}}_{t}
\end{aligned}
```

Think now about the case where depreciation is 100 percent ({math}`\delta=1`); from {eq}`eq:vdvsvx` it is clear that in this case {math}`\vFunc_{t}^{d} = 0`. This makes sense because in this case the "durable" good is really a totally nondurable good. {math}`\vFunc^{d_{t-1}}_{t} = 0` because the amount that you consumed of a nondurable good last period has no direct effect on your current utility (we have assumed that utility is time separable).

The {math}`\delta= 0` case is more interesting. In this case the marginal utility of having an extra unit of durable good last period is equal to the marginal utility of having an extra unit of wealth this period. Why? Because if {math}`\delta=0` the durable good doesn't depreciate at all. How much would it cost to buy another unit of durable good today? One unit of wealth. Because the durable does not depreciate from period to period and can be transformed into and out of wealth at a one-to-one price, it is exactly as valuable as a unit of wealth.

Now we want to try to derive a relationship between the contemporaneous marginal utilities of {math}`d` and {math}`c`. From {eq}`eq:ud` we have:

```{math}
:label: eq:beqns

\uFunc^{d}_{t} = \Rfree \beta \vFunc^{{m}}_{t+1} - \beta \vFunc^{d}_{t+1}.
```

and {math}`\Rfree \beta \vFunc^{{m}}_{t+1} = \uFunc^{c}_{t}` and from {eq}`eq:vdvsvx` {math}`\vFunc_{t+1}^{d} = (1-\delta) \vFunc^{{m}}_{t+1}`. Substituting these into {eq}`eq:beqns`:

```{math}
:label: eq:uprimeeqn

\begin{aligned}
 \uFunc_{t}^{d} & =  \uFunc_{t}^{c}-\beta(1-\delta) \vFunc_{t+1}^{{m}} \\
 & = \uFunc_{t}^{c} - \frac{(1-\delta)}{\Rfree} \Rfree\beta \vFunc_{t+1}^{{m}}  \\
 & = \left[1-\frac{(1-\delta)}{\Rfree}\right] \uFunc_{t}^{c} \\
 & = \left[\frac{\rfree + \delta}{\Rfree}\right]   \uFunc_{t}^{c}
\end{aligned}
```

Assuming {math}`\delta<1`, this equation tells us that the marginal utility *in the current period* of a unit of spending on the durable good is lower than the marginal utility of spending on the nondurable. Why? Because the durable good will yield utility in the future as well as in the present. What should be equated to the marginal utility of nondurables consumption is the total discounted lifetime utility from an extra unit of the durable good, not simply the marginal utility it yields right now.

:::{margin}
You're going to own this thing for a long time. You don't buy a car because it is worth \$20,000 to you on the day you buy it; you buy a car because its *expected discounted* value to you over its lifetime is \$20,000 (or more).
:::

Now assume the utility function is of the Cobb-Douglas form: {math}`\uFunc(c,d)=\frac{({c^{1-\alpha }d^{\alpha })}^{1-\rho }}{1-\rho }.` This implies that the instantaneous marginal utilities with respect to {math}`c` and {math}`d` are:

```{math}
\begin{aligned}
\uFunc^{c} & = (c^{1-\alpha}d^{\alpha})^{-\rho}
(1-\alpha)c^{-\alpha}d^{\alpha}  \\
           & =  (c^{1-\alpha}d^{\alpha})^{-\rho} (1-\alpha)(d/c)^{\alpha}
\\ \uFunc^{d} & = (c^{1-\alpha}d^{\alpha})^{-\rho} \alpha c^{1-\alpha}
d^{\alpha-1} \\
      & = (c^{1-\alpha}d^{\alpha})^{-\rho}  \alpha (d/c)^{\alpha-1}
\end{aligned}
```

**Commented-out alternative derivations and second-order derivatives:**

```{math}
\begin{aligned}
% \uFunc^{c} & = \left(c(d/c)^{\alpha}\right)^{-\rho} (1-\alpha)(d/c)^{\alpha} \\
% & = c^{-\rho} (1-\alpha)(d/c)^{\alpha(1-\rho)} \\
% \uFunc^{cc} & = c^{-\rho} (1-\alpha)(\alpha(1-\rho))(d/c)^{\alpha(1-\rho)-1}(-dc^{-2})-\rho c^{-\rho-1}(1-\alpha)(d/c)^{\alpha(1-\rho)} \\
% \uFunc^{cc} & = c^{-\rho} (1-\alpha)(\alpha(1-\rho))(d/c)^{\alpha(1-\rho)-1}(-d/c)c^{-1}) \\
% \uFunc^{cc} & = c^{-\rho-1} (1-\alpha)(\alpha(1-\rho))(d/c)^{\alpha(1-\rho)-1}(-d/c) \\
% \uFunc^{cc} & = -\rho(c^{0.5}d^{0.5})^{-\rho-1}0.5(d/c)^{0.5}+(c^{1-\alpha}d^{\alpha})^{-\rho} 0.5 (d/c)^{-0.5}(-d/c)/c \\
% \uFunc^{cd} & = -\rho(c^{0.5}d^{0.5})^{-\rho-1}0.5(d/c)^{-0.5}(c^{-1}-d c^{-2}) \\
% \uFunc^{dd} & = -\rho(c^{0.5}d^{0.5})^{-\rho-1}0.5(c/d)^{0.5}+(c^{1-\alpha}d^{\alpha})^{-\rho} 0.5 (d/c)^{-0.5}c^{-1}
\end{aligned}
```

Substituting these definitions into {eq}`eq:uprimeeqn` gives:

```{math}
:label: eq:gamma

\begin{aligned}
(c^{1-\alpha}d^{\alpha})^{-\rho} \alpha (d/c)^{\alpha-1}& =
(c^{1-\alpha}d^{\alpha})^{-\rho}  (1-\alpha)
(d/c)^{\alpha}\left(\frac{\rfree+\delta}{\Rfree}\right) \\
\frac{\alpha}{1-\alpha} & = (d/c)\left(\frac{\rfree+\delta}{\Rfree}\right)  \\
d/c & = \left(\frac{\alpha}{1-\alpha}\right)\left( \frac{\Rfree}{\rfree+\delta} \right)\equiv \gamma
\end{aligned}
```

What this implies is that whenever the level of nondurables consumption changes, the level of the *stock* of durables should change by the same proportion. Because *expenditures* on durable goods are equal to the *change* in the stock plus depreciation, a change in {math}`c` implies spending on durables large enough to immediately adjust the stock to the new target level. (Recall that {math}`d_{t}` was the *stock* of durable good owned in period {math}`t`, while *spending* on the durable good was defined as {math}`{x}_{t} = d_{t} - (1-\delta) d_{t-1}`.)

Define {math}`\gamma = d_{t}/c_{t}` as in {eq}`eq:gamma`. Now consider a consumer who had consumed the same amount of the nondurable good for periods {math}`c_{t-2} = c_{t-1}` but who between period {math}`t-1` and period {math}`t` learns some good news about permanent income; she adjusts her nondurables consumption up so that {math}`c_{t}/c_{t-1} = (1+\epsilon_{t})`. This implies that the level of *spending* in period {math}`t` is:

```{math}
:label: eq:dursspending

\begin{aligned}
{x}_{t}   & = d_{t} - (1-\delta) d_{t-1} = \gamma [c_{t} - (1-\delta)
c_{t-1}]\\
{x}_{t-1} & =
\gamma [c_{t-1} - (1-\delta) c_{t-2}]  \\
        & = \gamma \delta c_{t-1}  \\
{x}_{t}/{x}_{t-1} & = \gamma[c_{t-1}(1+\epsilon_{t}) -
(1-\delta)c_{t-1}]/ \gamma \delta c_{t-1}  \\
 & = \frac{\epsilon_{t} + \delta}{\delta}
\end{aligned}
```

Assuming {math}`\delta < 1`, this equation implies that *spending on durable goods should be more variable than spending on nondurable goods.*[^volatility-discussion] For goods with a low depreciation rate, spending should be much more variable. This is true because the ratio of the stock of durables to income is much larger than the ratio of the average level of spending on durables to income.

[^volatility-discussion]: Briefly discuss meaning: your house is 3 times your perm income; so fluctuations in perm income mean you will be perpetually buying new chunks of house (when P goes up) or selling off chunks of your house (when P goes down). Obviously missing transactions costs; take class next year to learn about those! (Also point out that durables spending is in fact much more volatile than nondurables.)

A further implication of this model is that the degree of correlation between nondurables spending growth and durables spending growth depends on the frequency under consideration. For a given quarterly depreciation rate (say, 5 percent per quarter), the durable good will have almost completely depreciated over the course of 10 years = 40 quarters because {math}`0.95^{40}=0.12`. According to the model, over an interval long enough for the durable to have completely depreciated, the rate of growth of spending on the durable should match the rate of growth of spending of the nondurable, because over such a long interval they are really both nondurable.

Some evidence on this proposition is provided in the Jupyter notebook available [here](https://github.com/llorracc/Jupyter/blob/master/notebooks/Durables-vs-Nondurables-At-Low-And-High-Frequencies.ipynb).

**Commented-out:** The notebook was previously also runnable via [mybinder](https://mybinder.org/v2/gh/llorracc/Jupyter/master?filepath=notebooks%2FDurables-vs-Nondurables-10y-vs-1q.ipynb), but as of 2018-12-06 this was disabled because it requires too many dependencies (matplotlib, seaborn, pandas) that are not part of requirements.txt and are large.
