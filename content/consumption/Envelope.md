(sec:Envelope)=

# The Envelope Theorem and the Euler Equation
This section shows how the Envelope theorem is used to derive the consumption Euler equation in a multiperiod optimization problem with geometric discounting and intertemporally separable utility.

The consumer's goal from the perspective of date {math}`\tNow` is to

:::{margin}
Define "geometric discounting."
:::

```{math}
\max \sum_{n=0}^{\TEnd-\tNow} \Discount^{n} \uFunc(c_{\tNow+n})
```

subject to the dynamic budget constraint

```{math}
:label: eq:Env-xaccum

{m}_{\tNow+1} = ({m}_{\tNow}-{c}_{\tNow})\Rfree + {y}_{\tNow+1}.
```

The problem can be written in Bellman equation form as

```{math}
:label: eq:bellman

\vFunc_{\tNow}({m}_{\tNow}) = \max_{\{{c}_{\tNow}\}} ~\uFunc({c}_{\tNow}) + \Discount \vFunc_{\tNow+1}(({m}_{\tNow}-{c}_{\tNow})\Rfree+{y}_{\tNow+1}).
```

The first order condition for {eq}`eq:bellman` can be written as

```{math}
:label: eq:Env-cfoc

\begin{aligned}
0 & = \uFunc^{\prime}({c}_{\tNow})+\overbrace{\left(\frac{d {m}_{\tNow+1}}{d {c}_{\tNow}}\right)}^{=-\Rfree} \Discount \vFunc_{\tNow+1}^{\prime}({m}_{\tNow+1}) \\
\uFunc^{\prime}({c}_{\tNow}) & = \Rfree \Discount \vFunc_{\tNow+1}^{\prime}({m}_{\tNow+1}),
\end{aligned}
```

where the derivative {math}`d {m}_{\tNow+1}/d {c}_{\tNow} = -\Rfree` follows from {eq}`eq:Env-xaccum`. We can define a function {math}`\cFunc_{\tNow}({m})` that returns the {math}`{c}_{\tNow}` that solves the max problem for any given {math}`{m}_{\tNow}`. That is, for {math}`{c}_{\tNow}=\cFunc_{\tNow}({m}_{\tNow})` the first order condition {eq}`eq:Env-cfoc` will hold so that

```{math}
:label: eq:cstarfoc

\uFunc^{\prime}(\cFunc_{\tNow}({m}_{\tNow})) - \Rfree \Discount \vFunc_{\tNow+1}^{\prime}(({m}_{\tNow}-\cFunc_{\tNow}({m}_{\tNow}))\Rfree+{y}_{\tNow+1}) = 0.
```

Now define a function

:::{margin}
The underscore indicates it's a (weak) lower bound.
:::

```{math}
\underline{\vFunc}_{\tNow}({m}_{\tNow},{c}_{\tNow}) = \uFunc({c}_{\tNow})+\Discount \vFunc_{\tNow+1}(({m}_{\tNow}-{c}_{\tNow})\Rfree+{y}_{\tNow+1})
```

with partial derivatives

```{math}
:label: eq:nuc

\underline{\vFunc}^{c}_{\tNow}({m}_{\tNow},{c}_{\tNow}) \equiv \left(\frac{\partial \underline{\vFunc}_{\tNow}}{\partial {c}_{\tNow}}\right) = \uFunc^{\prime}({c}_{\tNow}) - \Rfree\Discount \vFunc_{\tNow+1}^{m}(({m}_{\tNow}-{c}_{\tNow})\Rfree+{y}_{\tNow+1})
```

```{math}
:label: eq:nuprimevtp1

\underline{\vFunc}^{{m}}_{\tNow}({m}_{\tNow},{c}_{\tNow}) \equiv \left(\frac{\partial \underline{\vFunc}_{\tNow}}{\partial {m}_{\tNow}}\right) = \Rfree \Discount \vFunc_{\tNow+1}^{{m}}({m}_{\tNow+1})
```

and note that by definition

```{math}
\vFunc_{\tNow}({m}_{\tNow}) = \underline{\vFunc}_{\tNow}({m}_{\tNow},\cFunc_{\tNow}({m}_{\tNow})).
```

The Chain Rule of differentiation tells us that

```{math}
:label: eq:partdiff

\vFunc^{\prime}_{\tNow}({m}_{\tNow})\equiv \vFunc_{\tNow}^{{m}}({m}_{\tNow}) \equiv \left(\frac{d \vFunc_{\tNow}}{d {m}_{\tNow}}\right) = \underline{\vFunc}_{\tNow}^{{m}}({m}_{\tNow},\cFunc_{\tNow}({m}_{\tNow})) + \left(\frac{\partial \cFunc_{\tNow}({m}_{\tNow})}{\partial {m}_{\tNow}}\right)\underline{\vFunc}_{\tNow}^{c}({m}_{\tNow},\cFunc_{\tNow}({m}_{\tNow})).
```

Here's the key insight: The assumption that consumers are optimizing means that we will always be evaluating the value function and its derivatives at a {math}`{c}_{\tNow}` that satisfies the first-order optimality condition {eq}`eq:cstarfoc`.[^liquidity-constraint] Thus we have from {eq}`eq:nuc` that

```{math}
\begin{aligned}
\underline{\vFunc}_{\tNow}^{c}({m}_{\tNow},\cFunc_{\tNow}({m}_{\tNow})) & = \uFunc^{\prime}(\cFunc_{\tNow}({m}_{\tNow})) - \Rfree\Discount \vFunc^{\prime}_{\tNow+1}(({m}_{\tNow}-\cFunc_{\tNow}({m}_{\tNow}))\Rfree+{y}_{\tNow+1}) \\
& = 0.
\end{aligned}
```

This means that the second term in {eq}`eq:partdiff` is always equal to zero, so from {eq}`eq:nuprimevtp1` we obtain

```{math}
:label: eq:eulerv

\vFunc^{\prime}_{\tNow}({m}_{\tNow}) = \Rfree \Discount \vFunc_{\tNow+1}^{\prime}({m}_{\tNow+1}).
```

Now notice that the RHS's of {eq}`eq:Env-cfoc` and {eq}`eq:eulerv` are identical, so we can equate the left hand sides,

```{math}
\vFunc_{\tNow}^{\prime}({m}_{\tNow}) = \uFunc^{\prime}({c}_{\tNow})
```

and since a corresponding equation will hold in period {math}`t+1` we can rewrite {eq}`eq:eulerv` as

```{math}
\uFunc^{\prime}({c}_{\tNow}) = \Rfree \Discount \uFunc^{\prime}({c}_{\tNow+1}).
```

The general principle can be condensed into a rule of thumb by realizing that the Envelope theorem will always imply that the total derivative of a value function with respect to any choice variable must be equal to zero for optimizing consumers (because the first order condition holds). Thus we could have obtained the result immediately by treating {math}`{c}_{\tNow}` as though it were a constant (that is, treating the problem as though {math}`\cFunc_{\tNow}^{\prime}(m_{\tNow})=0`) and taking the derivative of Bellman's equation with respect to {math}`{m}_{\tNow}` directly. This leads immediately to the key result:

```{math}
\begin{aligned}
\vFunc_{\tNow}({m}_{\tNow}) & = \uFunc(\cFunc({m}_{\tNow})) + \Discount \vFunc_{\tNow+1}(({m}_{\tNow}-\cFunc_{\tNow}({m}_{\tNow}))\Rfree+{y}_{\tNow+1}) \\
\vFunc_{\tNow}^{\prime}({m}_{\tNow}) & = \Discount \Rfree \vFunc_{\tNow+1}^{\prime}({m}_{\tNow+1}).
\end{aligned}
```

:::{figure} /sources/consumption/Envelope/LaTeX/Figures/Envelope.png
:name: fig:Envelope

Illustration of the Envelope Theorem at Alternative Values of {math}`\mRat`
:::

:::{margin}
Using the figure, discuss the consequences of an increase in {math}`m`, and show that the increase in utility is about the same whether you consume all or none of it.
:::
