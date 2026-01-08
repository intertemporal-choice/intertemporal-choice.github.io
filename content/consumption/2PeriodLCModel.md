(sec:2PeriodLCModel)=
# The Fisher Two-Period Optimal Consumption Problem
Irving {cite:t}`fisherInterestTheory` first analyzed the optimization problem of a consumer who faces no uncertainty and lives for two periods.

## Mathematical Analysis

In its most general form, the household's lifetime value function can be written

```{math}
\ValueFunc(\cNbr_{1},\cNbr_{2})
```

where the first argument reflects consumption in "youth" while the second argument represents consumption in "old age" and we assume that the derivatives with respect to the first and second arguments are positive,

```{math}
:label: eq:uprimepos

\ValueFunc_{1}, \ValueFunc_{2} > 0,
```

while the second derivatives are negative,

```{math}
:label: eq:uprimeprimeneg

\ValueFunc_{11}, \ValueFunc_{22}<0 .
```

The consumer begins the first period with resources of {math}`\bNbr_{1}` (think "bank balances") and income of {math}`\yNbr_{1}`. Total resources are divided between consumption and end-of-period assets {math}`\aNbr_{1}` ("assets after all actions" in period {math}`1`):

```{math}
\begin{aligned}
\bNbr_{1}+\yNbr_{1} & = \cNbr_{1}+\aNbr_{1}, \\
\aNbr_{1} & = \bNbr_{1}+\yNbr_{1}-\cNbr_{1}.
\end{aligned}
```

Balances at the beginning of period 2 are equal to end-of-first-period accumulated assets {math}`\aNbr_{1}`, rewarded by a gross interest factor {math}`\Rfree = (1+\rfree)`:

```{math}
\bNbr_{2} = \aNbr_{1}\Rfree.
```

This is the *dynamic budget constraint* or DBC for this problem. A DBC links two adjacent periods of time. A more comprehensive kind of constraint is the *intertemporal* budget constraint (IBC):

```{math}
:label: eq:ibcineq

\cNbr_{1}+\cNbr_{2}/\Rfree \leq \yNbr_{1}+\yNbr_{2}/\Rfree+\bNbr_{1},
```

which must be satisfied over an extended (multiperiod) span of time like a lifetime.

For various purposes, it is useful to keep track of *human wealth* {math}`\hNbr_{t}`, defined as the present discounted value of future labor income (the operator {math}`\PDV_{t}(\bullet)` denotes the present discounted value of the variable {math}`\bullet` from the perspective of the beginning of period {math}`t` through the end of the horizon),

```{math}
:label: eq:humw

\begin{aligned}
\hNbr_{t} & = \PDV_{t}(y) \\
\hNbr_{1} & = \yNbr_{1}+\yNbr_{2}/\Rfree
\end{aligned}
```

Because we have assumed (in {eq}`eq:uprimepos`) that an additional unit of consumption always yields extra utility, we can reach our first conclusion (as opposed to assumption) in the model: Once the consumer has reached the last period of life, he will consume all available resources:

```{math}
\cNbr_{2} = \bNbr_{2}+\yNbr_{2}.
```

This means that the IBC will hold with equality (if it did not, utility could be increased by consuming more in one or both periods). Thus, the IBC can be rewritten as

```{math}
:label: eq:2PLC-ibc

\cNbr_{1}+\cNbr_{2}/\Rfree = \hNbr_{1}+\bNbr_{1}.
```

The general form that the IBC will take is that the present discounted value of lifetime spending must equal the present discounted value of lifetime resources:

```{math}
:label: eq:ibcgen

\PDV_{t}(\cNbr) = \PDV_{t}(y)+\bNbr_{t}.
```

Substituting in the definition of {math}`\bNbr_{2}` means that our problem can now be stated as:

```{math}
\begin{aligned}
\max_{\{\cNbr_{1},\cNbr_{2}\}} & \quad \ValueFunc(\cNbr_{1},\cNbr_{2}) \\
& \text{s.t.} \\
\cNbr_{2} & = (\bNbr_{1}+\yNbr_{1}-\cNbr_{1})\Rfree+\yNbr_{2}.
\end{aligned}
```

Now we can write the problem as a [Lagrange multiplier](https://en.wikipedia.org/wiki/Lagrange_multiplier) problem, where the maximand is:

```{math}
\ValueFunc(\cNbr_{1},\cNbr_{2}) + \left(\cNbr_{2}- (\bNbr_{1}+\yNbr_{1}-\cNbr_{1})\Rfree-\yNbr_{2}\right)\lambda.
```

The first order conditions are:

```{math}
:label: eq:lagrange1

\begin{aligned}
\ValueFunc_{1} + \Rfree\lambda & = 0 \\
\ValueFunc_{2} & = -\lambda
\end{aligned}
```

and substituting the second of these into the first we get

```{math}
:label: eq:timeprice

\ValueFunc_{1} = \Rfree \ValueFunc_{2}.
```

This is the same condition you get when deciding between two commodities at a point in time, where we can now think of {math}`\Rfree` as the intertemporal price: How much of good 2 (consumption in period 2) do I get in exchange for giving up a unit of good 1 (consumption in period 1).

Now suppose that the consumer's utility is *time-separable*, and the felicity function (felicity is the utility obtained in a single period of a multi-period problem) is the same in both periods of life, so that

```{math}
\ValueFunc(\cNbr_{1},\cNbr_{2}) = \uFunc(\cNbr_{1})+\DiscFac \uFunc(\cNbr_{2})
```

where {math}`\DiscFac` is a *time preference factor* that specifies how the consumer trades off utility in period 1 against utility in period 2.[^samuelson]

[^samuelson]: Paul {cite:t}`samuelson1937note,samuelson:olg` introduced the discounting of future utility into the problem. See {cite:t}`floDiscounting` for a comprehensive review of the still-controversial topic of time discounting.

From our assumptions {eq}`eq:uprimepos` and {eq}`eq:uprimeprimeneg` we know that the felicity function must satisfy

```{math}
\begin{aligned}
\uFunc^{\prime}(\bullet) & > 0 \\
\uFunc^{\prime\prime}(\bullet) & < 0,
\end{aligned}
```

and since the felicity functions are the same in both periods we have that

```{math}
\begin{aligned}
\ValueFunc_{1}(\cNbr_{1},\cNbr_{2}) & = \uFunc^{\prime}(\cNbr_{1}) \\
\ValueFunc_{2}(\cNbr_{1},\cNbr_{2}) & = \DiscFac \uFunc^{\prime}(\cNbr_{2}).
\end{aligned}
```

Substituting these equations into {eq}`eq:timeprice` yields the *Euler equation* for consumption:

```{math}
:label: eq:2PLC-euler

\uFunc^{\prime}(\cNbr_{1}) = \Rfree \DiscFac \uFunc^{\prime}(\cNbr_{2}).
```

The Euler equation is a central result in intertemporal optimization theory, and will be used again and again as the course progresses. It is therefore worth studying carefully to be sure you understand it thoroughly.

To help obtain the intuition for why the Euler equation is necessary for optimality, consider the following thought experiment. Designate {math}`\cNbr^{*}_{1}` and {math}`\cNbr^{*}_{2}` as the optimal levels of consumption in this problem, the levels that solve the maximization problem under some set of circumstances. Thus, the highest attainable utility is

```{math}
:label: eq:2PLC-maxutil

\uFunc(\cNbr_{1}^{*})+\DiscFac \uFunc(\cNbr_{2}^{*}).
```

Now consider reducing consumption by some small amount {math}`\epsilon` in period 1, investing that {math}`\epsilon` so that it grows to {math}`\Rfree \epsilon` in period 2, and then consuming it in period 2. What happens to utility?

Taking first-order Taylor expansions, the levels of first-period and second-period utility are now

```{math}
\begin{aligned}
\uFunc(\cNbr_{1}^{*}-\epsilon) & \approx \uFunc(\cNbr_{1}^{*})-\uFunc^{\prime}(\cNbr_{1}^{*})\epsilon \\
\uFunc(\cNbr_{2}^{*}+\Rfree\epsilon) & \approx \uFunc(\cNbr_{2}^{*})+\uFunc^{\prime}(\cNbr_{2}^{*})\Rfree\epsilon.
\end{aligned}
```

Now the difference between the maximum possible utility and the new situation is given by

```{math}
:label: eq:diffutil

\uFunc(\cNbr_{1}^{*})+\DiscFac \uFunc(\cNbr_{2}^{*}) - \left[\uFunc(\cNbr_{1}^{*})-\uFunc^{\prime}(\cNbr_{1}^{*})\epsilon + \DiscFac \left(\uFunc(\cNbr_{2}^{*})+\uFunc^{\prime}(\cNbr_{2}^{*})\Rfree\epsilon \right) \right]
= \uFunc^{\prime}(\cNbr_{1}^{*})\epsilon - \DiscFac \uFunc^{\prime}(\cNbr_{2}^{*})\Rfree\epsilon.
```

But it must be the case that {eq}`eq:diffutil` is approximately equal to zero. To see why, suppose it were a negative number. That would mean that moving from the original situation with {math}`\{\cNbr_{1},\cNbr_{2}\} = \{\cNbr_{1}^{*},\cNbr_{2}^{*}\}` to the new situation with {math}`\{\cNbr_{1},\cNbr_{2}\} = \{\cNbr_{1}^{*}-\epsilon,\cNbr_{2}^{*}+\Rfree\epsilon\}` resulted in an *increase* in utility. But we assumed that {math}`\cNbr_{1}^{*},\cNbr_{2}^{*}` were already the utility-maximizing choices, which clearly could not be true if adjusting {math}`\cNbr_{1}^{*}` downward by {math}`\epsilon` and {math}`\cNbr^{*}_{2}` upward by {math}`\Rfree \epsilon` increased utility. Similarly, if the expression were positive, then utility could be increased by doing the opposite (i.e. increasing consumption in period 1 by {math}`\epsilon` and reducing it in period 2 by {math}`\Rfree\epsilon`). Thus, in either case if the expression is not zero, we have a contradiction to the assumption that {math}`\cNbr_{1}^{*}` and {math}`\cNbr_{2}^{*}` are the utility-maximizing choices.

To make further progress, it is necessary to make more specific assumptions about the structure of the utility function. The most common assumption is that utility takes the Constant Relative Risk Aversion form,

```{math}
:label: eq:crrautil

\uFunc(\cNbr) = \frac{\cNbr^{1-\CRRA}}{1-\CRRA},
```

with marginal utility

```{math}
:label: eq:crramargutil

\uFunc^{\prime}(\cNbr) = \cNbr^{-\CRRA}.
```

Consider equation {eq}`eq:2PLC-euler` with CRRA utility,

```{math}
:label: eq:c1euler

\begin{aligned}
\cNbr_{1}^{-\CRRA} & = \Rfree\DiscFac \cNbr_{2}^{-\CRRA} \\
\cNbr_{2}/\cNbr_{1} & = (\Rfree\DiscFac)^{1/\CRRA} \\
\cNbr_{2} & = (\Rfree\DiscFac)^{1/\CRRA}\cNbr_{1}.
\end{aligned}
```

Now note that this equation allows us to calculate the *intertemporal elasticity of substitution* as the change in the ratio of the log of {math}`\cNbr_{2}/\cNbr_{1}` to the log change in the intertemporal price {math}`\Rfree`:

```{math}
\begin{aligned}
\left(\frac{d}{d \log \Rfree}\right) \log \left(\frac{\cNbr_{2}}{\cNbr_{1}}\right) & = \left(\frac{d}{d \log \Rfree}\right) \log (\Rfree \DiscFac)^{1/\CRRA} \\
& = \CRRA^{-1}.
\end{aligned}
```

Next note that from {eq}`eq:c1euler` we can calculate the PDV of lifetime consumption from the perspective of the first period of life as

```{math}
\begin{aligned}
\PDV_{1}(\cNbr) & = \cNbr_{1} + \Rfree^{-1}\cNbr_{2} \\
& = \left(1+\Rfree^{-1}(\Rfree\DiscFac)^{1/\CRRA}\right)\cNbr_{1}.
\end{aligned}
```

Now we can use the intertemporal budget constraint:

```{math}
\begin{aligned}
\PDV_{t}(\cNbr) & = \bNbr_{t}+\PDV_{t}(y) \\
\cNbr_{1}\left(1+\Rfree^{-1}(\Rfree\DiscFac)^{1/\CRRA}\right) & = \bNbr_{1}+\yNbr_{1}+\Rfree^{-1}\yNbr_{2} \\
\cNbr_{1} & = \frac{\bNbr_{1}+\hNbr_{1}}{1+\Rfree^{-1}(\Rfree\DiscFac)^{1/\CRRA}}.
\end{aligned}
```

Thus, we have solved the two-period life cycle saving problem for the *consumption function* {math}`\cFunc_{1}` relating the level of consumption to all of the parameters of the problem.

One of the surprising features of the solution goes by the name of "Fisherian Separation": Notice that the *profile* of consumption growth over the lifetime is given by {eq}`eq:c1euler` *regardless of the shape of the income profile*. For two consumers with the same total amount of lifetime wealth (combined {math}`\bNbr_{1}` and {math}`\hNbr_{1}`), the level and growth rates of consumption over the lifetime will be identical whether the consumer's lifetime wealth is entirely concentrated in the first period (that is, {math}`\hNbr_{1}=0`), entirely concentrated in the last period ({math}`\bNbr_{1}=0`), split half-and-half, or organized any other way. Fisherian Separation is a pervasive feature of models that combine perfect foresight and a lack of liquidity constraints.

A common assumption (for simplicity, not realism) is that {math}`\CRRA=1`, which is equivalent to assuming that the utility function is logarithmic:[^crralim]

[^crralim]: See the math fact showing that {math}`\lim_{\CRRA \rightarrow 1} \frac{c^{1-\CRRA}}{1-\CRRA} = \log c` in the [Math Facts section](#fact:mathfactslist).

```{math}
\lim_{\CRRA \rightarrow 1} \frac{\cNbr^{1-\CRRA}}{1-\CRRA} = \log c.
```

In this case it turns out that we can simply substitute {math}`\CRRA=1` into the solution for consumption, obtaining

```{math}
\cFunc_{1} = \frac{\bNbr_{1}+\hNbr_{1}}{1+\DiscFac}.
```

## Graphical Analysis

The classic graphical analysis of this problem is shown in {numref}`fig:Fisher`.

The top figure depicts a situation in which all of the consumer's lifetime income is earned in the first period of life. The budget constraint in the initial situation, associated with a "Low {math}`\Rfree`", yields an optimal consumption choice labeled as point {math}`A` where the budget constraint is tangent to the indifference curve. When the interest factor is increased to the "High {math}`\Rfree`" situation, the optimal consumption choice moves to point {math}`C`.

Note first that if all income is earned in the first period of life, an increase in the interest factor is unambiguously good for the consumer: the set of consumption possibilities is strictly larger.

Second, the movement from point {math}`A` to point {math}`C` can be decomposed into two parts: an income effect {math}`AB` and a substitution effect {math}`BC`.

Call the low and the high interest factors respectively {math}`\underline{\Rfree}` and {math}`\bar{\Rfree}`.

The income effect is the answer to the question "Suppose we wanted to change lifetime value by the same amount as it is changed by going from {math}`\underline{\Rfree}` to {math}`\bar{\Rfree}`, but we wanted to achieve this change in value at the initial interest factor {math}`\underline{\Rfree}`. Supposing we gave the consumer enough extra initial resources to achieve the change in value, how would their consumption allocation change?"

In order to relate this back to the algebraic analysis above, it will be useful to rewrite lifetime value as a function simply of initial resources and the interest factor (taking {math}`\{\yNbr_{1},\yNbr_{2}\}` and other parts of the problem as given):

```{math}
\ValueFunc^{*}(\bNbr_{1},\Rfree) = \uFunc(\cFunc_{1}^{*}(\bNbr_{1},\Rfree))+\DiscFac \uFunc(\cFunc_{2}^{*}(\bNbr_{1},\Rfree))
```

Using this function, the income effect is obtained as the value of {math}`\Delta \bNbr_{1}` in the equation {math}`\ValueFunc^{*}(\bNbr_{1}+\Delta\bNbr_{1},\underline{\Rfree})=\ValueFunc^{*}(\bNbr_{1},\bar{\Rfree})`.

The substitution effect is the answer to the question, "Staying on the new indifference curve, how much does the allocation of consumption change as a consequence of the difference in interest factors between {math}`\underline{\Rfree}` and {math}`\bar{\Rfree}`?" This is captured in the movement from {math}`B` to {math}`C`.

Note that the income and the substitution effects on {math}`\cNbr_{1}` are opposite in sign. A higher interest factor gives consumers the incentive to substitute future for current consumption ({math}`\cNbr_{1}` is lower at point {math}`C` than at {math}`B`). But a higher interest factor also gives consumers the ability to consume more in both periods. Whether {math}`\cNbr_{1}` rises or falls in response to the increase in interest factors will depend on the relative magnitudes of the income and substitution effects.

The lower figure shows a similar experiment, with the sole difference that the consumer's lifetime resources are exclusively concentrated in period 2.

In this case, the period 1 consumer must borrow against future income in order to consume anything. An increase in interest factors is therefore unambiguously bad (the available set of consumption choices is strictly smaller).

The optimal choice again moves from point {math}`A` to point {math}`C`. However, we now decompose the movement into three parts. The first part is called the *human wealth effect*. It captures the fact that the present discounted value of lifetime resources {math}`\PDV_{1}(y)` is smaller when interest rates are higher; the magnitude of the change in human wealth is depicted on the horizontal axis of the figure. The human wealth *effect* is the consequence that an equivalent change in lifetime resources would have *in the absence of any change in interest factors*. So the human wealth effect takes the consumer from point {math}`A` to point {math}`D`.

Notice that once we have computed the human wealth effect, if we treat point {math}`D` as the starting point of our analysis, the remaining analysis is identical to that for the upper figure: We can increase the interest factor from {math}`\underline{\Rfree}` to {math}`\bar{\Rfree}`, which causes the equilibrium point to change from point {math}`D` to point {math}`C`, a movement that can be decomposed into an income effect {math}`DB` (analogous to the income effect {math}`AB` in the original analysis) and a substitution effect {math}`BC`.

The terminology here is a modification (refinement) of the terminology often employed in micro textbooks, where the "income effect" is defined in a way that would incorporate both what I am calling the income effect and what I am calling the human wealth effect.

The reason to make this distinction is that it is important to distinguish between effects on behavior caused by the fact that the discounted value of future income is changed, and effects caused by the fact that the income that will be earned on savings is different. {cite:t}`summersCapTax` vigorously made the point that in standard life cycle models, the quantitative magnitude of the human wealth effect dwarfs the size of either the income or the substitution effects, because for most people most of their lifetime income is in the future.

:::{figure} /sources/consumption/2PeriodLCModel/LaTeX/Figures/FisherFigureY1.png
:name: fig:Fisher

![](/sources/consumption/2PeriodLCModel/LaTeX/Figures/FisherFigureY2.png)

Fisher Figure Analysis
:::
