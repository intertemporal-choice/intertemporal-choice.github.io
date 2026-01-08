(sec:Habits)=

# Consumption Models with Habit Formation

## The Problem

Consider a consumer whose goal at date {math}`t` is to solve the problem

:::{margin}
This section is a simplified version of {cite:t}`carroll:solvinghabits`.
:::

:::{margin}
This is not necessarily the first idea that the term "habit formation" brings to mind. Often people speak of forming the "habit" of saving, and what is meant seems to be a rule of thumb for behavior.
:::

```{math}
\max \sum_{n=0}^{T-\tNow} \Discount^{n} \uFunc(c_{t+n},\habit_{t+n})
```

where {math}`\habit_{t+n}` is the habit stock, and all other variables are as usually defined. The DBC is

:::{margin}
{math}`\uFunc^{h}<0`.
:::

:::{margin}
This utility function is not "time separable" in the sense originally discussed, but *once habits are included* it becomes time-separable.
:::

```{math}
:label: eq:Hab-xaccum

\mRat_{t+1} = (\mRat_{t}-c_{t})\Rfree + y_{t+1}.
```

However, when habits affect utility we must also specify a process that describes how habits evolve over time. Our assumption will be:

**FirstYearVersion=true:**

```{math}
\habit_{t+1} = c_{t}.
```

**FirstYearVersion=false:**

```{math}
\habit_{t+1} = \habit_{t} + \lambda (c_{t} - \habit_{t}).
```

Bellman's equation for this problem is therefore

```{math}
:label: eq:bellmanmax

\vFunc_{t}(\mRat_{t},\habit_{t}) = \max_{\{c_{t}\}} ~~\uFunc(c_{t},\habit_{t}) + \Discount \vFunc_{t+1}((\mRat_{t}-c_{t})\Rfree+y_{t+1},c_{t}).
```

To clarify the workings of the Envelope theorem in the case with two state variables, let's define a function[^vfunc-notation]

[^vfunc-notation]: {math}`\underline{\vFunc}` looks like {math}`\vFunc` but is curved.

```{math}
\underline{\vFunc}_{t}(\mRat_{t},\habit_{t},c_{t}) = \uFunc(c_{t},\habit_{t}) +\Discount \vFunc_{t+1}((\mRat_{t}-c_{t})\Rfree+y_{t+1},c_{t})
```

and define the function {math}`\mathbf{c}_{t}(\mRat_{t},\habit_{t})` as the choice of {math}`c_{t}` that solves the maximization {eq}`eq:bellmanmax`, so that we have

```{math}
\vFunc_{t}(\mRat_{t},\habit_{t}) = \underline{\vFunc}_{t}(\mRat_{t},\habit_{t},\mathbf{c}_{t}(\mRat_{t},\habit_{t})).
```

## Optimality Conditions

### The First Order Condition

The first order condition for {eq}`eq:bellmanmax` with respect to {math}`c_{t}` is (dropping arguments for brevity and denoting the derivative of {math}`f` with respect to {math}`x` at time {math}`t` as {math}`f^{x}_{t}`):

```{math}
:label: eq:ctfocraw

0 = \uFunc^{c}_{t} + \Discount \left(\vFunc^{h}_{t+1} - \Rfree \vFunc^{\mRat}_{t+1} \right)
```

or, equivalently,

```{math}
:label: eq:ctfoc

\uFunc^{c}_{t} = \Discount \left(\Rfree \vFunc_{t+1}^{\mRat}- \vFunc_{t+1}^{h}\right).
```

The intuition is as follows. Note first that if utility is not affected by habits, then {math}`\vFunc^{h}_{t+1}=0` and equation {eq}`eq:ctfoc` reduces to the usual first order condition for consumption, which tells us that increasing consumption by {math}`\epsilon` today and reducing it by {math}`\Rfree \epsilon` in the next period must not change expected discounted utility. With habits, an increase in consumption today has a consequence beyond its effect on tomorrow's resources {math}`\mRat_{t+1}`: tomorrow's habit stock will be changed as well. An increase in consumption today of size {math}`\epsilon` increases the size of the habit stock which tomorrow's consumption is compared to, and therefore reduces tomorrow's utility by an amount corresponding to the marginal utility of higher habits tomorrow {math}`\vFunc^{h}_{t+1}`. Since {math}`\vFunc^{h}_{t+1}` is negative (higher habits make utility lower), this tells us that the RHS of equation {eq}`eq:ctfoc` will be a larger positive number than it would be without habits. This means that the level of {math}`c_{t}` that satisfies the first order condition will be a lower number (higher marginal utility) than before. Hence, habits increase the willingness to delay spending, and increase the saving rate.

Note that the first order condition also implies that

```{math}
\frac{d \underline{\vFunc}_{t}}{d c_{t}} = 0
```

when evaluated at {math}`c_{t}=\mathbf{c}_{t}(\mRat_{t},\habit_{t})`.

### Envelope Conditions

Now consider the total derivative of {math}`\underline{\vFunc}_{t}(\mRat_{t},\habit_{t},\mathbf{c}_{t}(\mRat_{t},\habit_{t}))` with respect to {math}`\mRat_{t}`. (To reduce clutter, I will write {math}`d \mathbf{c}_{t}(\mRat_{t},\habit_{t})/d \mRat_{t}` as {math}`d \mathbf{c}_{t}/d \mRat_{t}`). The chain rule tells us that

```{math}
\begin{aligned}
        \frac{d \underline{\vFunc}_{t}}{d \mRat_{t}} & = \frac{d \mathbf{c}_{t}}{d \mRat_{t}}\uFunc^{c}_{t}+\overbrace{\frac{d \habit_{t}}{d \mRat_{t}}}^{=0} \uFunc^{h}_{t}
         + \Discount \left((\frac{d \mathbf{c}_{t}}{d \mRat_{t}})(\vFunc^{h}_{t+1}-\Rfree \vFunc_{t+1}^{\mRat}) + \Rfree \vFunc_{t+1}^{\mRat} \right) \\
& = \left(\frac{d \mathbf{c}_{t}}{d \mRat_{t}}\right)
\underbrace{(\uFunc_{t}^{c}+\Discount\left(\vFunc_{t+1}^{h}-\Rfree \vFunc_{t+1}^{\mRat}\right))}_{=0}+\Discount \Rfree \vFunc_{t+1}^{\mRat}
\end{aligned}
```

where the underbraced term vanishes at {math}`c_{t}=\mathbf{c}_{t}(\mRat_{t},\habit_{t})` by the first-order condition {eq}`eq:ctfocraw`. Thus we have that

```{math}
\begin{aligned}
        \vFunc_{t}^{\mRat} & = \frac{d \underline{\vFunc}_{t}}{d \mRat_{t}}|_{c_{t}=\mathbf{c}_{t}(\mRat_{t},\habit_{t})} \\
         & = \Discount \Rfree \vFunc^{\mRat}_{t+1}.
\end{aligned}
```

The Envelope theorem is the shortcut way to obtain this conclusion. The clearest way to use the theorem is by taking the partial derivatives of the {math}`\underline{\vFunc}_{t}` function with respect to each of its three arguments, using the Chain Rule to take into account the possible dependency of {math}`\habit_{t}` and {math}`c_{t}` on {math}`\mRat_{t}`:

```{math}
:label: eq:vx

\begin{aligned}
        \vFunc_{t}(\mRat_{t},\habit_{t}) & = \underline{\vFunc}_{t}(\mRat_{t},\habit_{t},\mathbf{c}_{t}(\mRat_{t},\habit_{t})) \\
        \vFunc_{t}^{\mRat} & = \frac{\partial \underline{\vFunc}_{t}}{\partial \mRat_{t}}
        + \frac{\partial \underline{\vFunc}_{t}}{\partial \habit_{t}}\underbrace{\frac{\partial \habit_{t}}{\partial \mRat_{t}}}_{=0}
        + \underbrace{\frac{\partial \underline{\vFunc}_{t}}{\partial c_{t}}}_{=0}\frac{\partial \mathbf{c}_{t}}{\partial \mRat_{t}}+\frac{\partial \underline{\vFunc}_{t}}{\partial c_{t}}\frac{\partial c_{t}}{\partial \habit_{t}}\underbrace{\frac{\partial \habit_{t}}{\partial \mRat_{t}}}_{=0}
\end{aligned}
```

where the Envelope theorem is what tells you that the {math}`\partial \underline{\vFunc}_{t}/\partial c_{t}` term is equal to zero because you are evaluating the function at {math}`c_{t}=\mathbf{c}_{t}(\mRat_{t},\habit_{t})` (and {math}`\partial \habit_{t}/\partial \mRat_{t}` is zero by the assumed structure of the problem in which {math}`\habit_{t}` is predetermined).

Now writing out {math}`\partial \underline{\vFunc}_{t}/\partial \mRat_{t}`, {eq}`eq:vx` becomes

```{math}
:label: eq:partialx

\vFunc^{\mRat}_{t} = \frac{\partial}{\partial \mRat_{t}}\left[\Discount \vFunc_{t+1}((\mRat_{t}-c_{t})\Rfree+y_{t+1},\habit_{t+1})\right]
```

which the envelope theorem says is equivalent to

```{math}
:label: eq:envelopex

\vFunc^{\mRat}_{t} = \Discount  \Rfree \vFunc_{t+1}^{\mRat}.
```

There is a potentially confusing thing about doing it this way, however: when you reach an expression like {eq}`eq:partialx` it is tempting to think to yourself as follows: "{math}`c_{t}` is a function of {math}`\mRat_{t}`, and {math}`\habit_{t+1}=c_{t}` is also indirectly a function of {math}`\mRat_{t}`, so the chain rule tells me that when I take the derivative in {eq}`eq:partialx` I need to keep track of these." In fact, you must treat {math}`\partial c_{t}/\partial \mRat_{t}` and {math}`\partial \habit_{t+1}/\partial \mRat_{t}` as zero here. The reason is that this is a *partial* derivative with respect to {math}`\mRat_{t}`. The dependence of {math}`c_{t}` (and indirectly {math}`\habit_{t+1}`) on {math}`\mRat_{t}` has already been taken care of in the two terms in {eq}`eq:vx` that were equal to zero. The confusion here is caused largely by the fact that partial differentiation is an area where standard mathematical notation is basically confusing and poorly chosen.[^partial-diff-notation]

[^partial-diff-notation]: Google the string "partial differentiation confusing OCW" to find a fuller description of the problems of standard notation on partial differentiation.

The shortest way to obtain the end result is, as in the single variable problem, to start with Bellman's equation and take the partial derivative with respect to {math}`\mRat_{t}` directly (treating the problem as though {math}`c_{t}` were a constant):

```{math}
\begin{aligned}
        \vFunc_{t}(\mRat_{t},\habit_{t}) & = \uFunc(c_{t},\habit_{t})+\Discount \vFunc_{t+1}((\mRat_{t}-c_{t})\Rfree+y_{t+1},\habit_{t+1}) \\
        \vFunc_{t}^{\mRat}(\mRat_{t},\habit_{t}) & = \Discount \Rfree \vFunc_{t+1}^{\mRat}(\mRat_{t+1},\habit_{t+1}).
\end{aligned}
```

Whichever way you do it, substituting {eq}`eq:envelopex` into the FOC equation {eq}`eq:ctfoc` gives

```{math}
:label: eq:ctfocsubx

\vFunc_{t}^{\mRat} = \uFunc^{c}_{t}+\Discount \vFunc_{t+1}^{h}.
```

The intuition for this is as follows. The marginal value of wealth must be equal to the marginal value associated with a tiny bit more consumption. In the presence of habits, the extra consumption yields extra utility today {math}`\uFunc^{c}_{t}` but affects value next period by {math}`\vFunc^{h}_{t+1}` (which is a negative number), the discounted consequence of which from today's perspective is the {math}`\Discount \vFunc^{h}_{t+1}` term.

### Envelope Theorem for {math}`\habit_{t}`

<!-- Original LaTeX had this as a commented-out subsection: %\subsubsection{Envelope Theorem for $\habit_{t}$} -->

In a problem with two state variables, the Envelope theorem can be applied to each state (and indeed in general must be applied in order to solve the model).

Again let's start the brute force way by working through the total derivative of {math}`\underline{\vFunc}_{t}`. For this problem, the total derivative (again denoting {math}`d \mathbf{c}_{t}(\mRat_{t},\habit_{t})/d {h}_{t}` as {math}`d \mathbf{c}_{t}/d \habit_{t}`) is:

```{math}
\begin{aligned}
        \frac{d \underline{\vFunc}_{t}}{d \habit_{t}} & = \frac{d \mathbf{c}_{t}}{d \habit_{t}} \uFunc^{c}_{t}       + \uFunc^{h}_{t}
        + \Discount \left( \frac{d \habit_{t+1}}{d \habit_{t}}\vFunc_{t+1}^{h}
        + \frac{d \mRat_{t+1}}{d \habit_{t}} \vFunc_{t+1}^{\mRat}\right) \\
 & = \frac{d \mathbf{c}_{t}}{d \habit_{t}} \uFunc^{c}_{t}        + \uFunc^{h}_{t}
        + \Discount \left(\frac{d \habit_{t+1}}{d \mathbf{c}_{t}}\frac{d \mathbf{c}_{t}}{d \habit_{t}} \vFunc_{t+1}^{h}
        + \frac{d \mRat_{t+1}}{d \mathbf{c}_{t}}\frac{d \mathbf{c}_{t}}{d \habit_{t}} \vFunc_{t+1}^{\mRat}
        \right) \\
 & = \uFunc^{h}_{t} +
 \frac{d \mathbf{c}_{t}}{d \habit_{t}} \underbrace{\left(\uFunc^{c}_{t}
        + \Discount (\vFunc_{t+1}^{h}
        - \Rfree \vFunc_{t+1}^{\mRat} )\right)}_{= 0}
\end{aligned}
```

where again the underbraced term vanishes at {math}`c_{t}=\mathbf{c}_{t}(\mRat_{t},\habit_{t})` by {eq}`eq:ctfocraw`. Thus we have

```{math}
\begin{aligned}
        \vFunc_{t}^{h} & = \frac{d \underline{\vFunc}_{t}}{d \habit_{t}}|_{c_{t} = \mathbf{c}_{t}(\mRat_{t},\habit_{t})} \\
       & = \uFunc_{t}^{h}.
\end{aligned}
```

Turning now to more direct use of the envelope theorem, the Chain Rule tells us

```{math}
\vFunc_{t}^{h} = \frac{\partial \underline{\vFunc}_{t}}{\partial \mRat_{t}}
        \overbrace{\frac{\partial \mRat_{t}}{\partial \habit_{t}}}^{=0}
+ \frac{\partial \underline{\vFunc}_{t}}{\partial \habit_{t}}
+ \frac{\partial \underline{\vFunc}_{t}}{\partial c_{t}}\frac{\partial \mathbf{c}_{t}}{\partial \habit_{t}}
```

while the Envelope theorem once again says {math}`\partial \underline{\vFunc}_{t}/\partial c_{t} = 0` at {math}`c_{t}=\mathbf{c}_{t}(\mRat_{t},\habit_{t})` so we obtain

```{math}
\begin{aligned}
        \vFunc_{t}^{h} & = \frac{\partial \underline{\vFunc}_{t}}{\partial \habit_{t}} \\
         & = \uFunc_{t}^{h}
\end{aligned}
```

since {math}`\habit_{t}` appears directly only in the {math}`\uFunc(c_{t},\habit_{t})` part of {math}`\underline{\vFunc}_{t}(\mRat_{t},\habit_{t},c_{t})`. And once again, the shortest way to the answer is to treat {math}`c_{t}` as though it were a constant in the value function, which yields

```{math}
\begin{aligned}
        \vFunc_{t}(\mRat_t,\habit_{t}) & = \uFunc(c_{t},\habit_{t})+\Discount \vFunc_{t+1}((\mRat_{t}-c_{t})\Rfree+y_{t+1},c_{t}) \\
        \vFunc_{t}^{h}(\mRat_{t},\habit_{t}) & = \uFunc_{t}^{h}.
\end{aligned}
```

From {eq}`eq:ctfocsubx` this implies that

```{math}
\vFunc_{t}^{\mRat} = \uFunc^{c}_{t}+\Discount \uFunc_{t+1}^{h}.
```

Roll this equation forward one period and substitute into equation {eq}`eq:envelopex` to obtain:

```{math}
:label: eq:focfull2

\uFunc^{c}_{t} + \Discount \uFunc_{t+1}^{h} = \Rfree \Discount \left[\uFunc^{c}_{t+1}+\Discount \uFunc^{h}_{t+2}\right]
```

Note that if {math}`\uFunc_{t+1}^{h}=\uFunc_{t+2}^{h}=0` so that habits have no effect on utility, {eq}`eq:focfull2` again is solved by the standard time-separable Euler equation.

Now assume that the utility function takes the specific form

```{math}
\uFunc(c,h) = \mathbf{f}(c-\alpha h)
```

which implies derivatives of

```{math}
\begin{aligned}
        \uFunc^{c} & = \mathbf{f}^{\prime} \\
        \uFunc^{h} & = -\alpha \mathbf{f}^{\prime}.
\end{aligned}
```

Substituting these into equation {eq}`eq:focfull2` we obtain,

```{math}
:label: eq:vpeq

\mathbf{f}_{t}^{\prime}-\alpha \Discount \mathbf{f}_{t+1}^{\prime} = \Rfree\Discount[\mathbf{f}_{t+1}^{\prime} -\alpha \Discount \mathbf{f}_{t+2}^{\prime}]
```

Now assume that there is a solution in which marginal utility of consumption grows at a constant rate over time, {math}`\mathbf{f}_{t}^{\prime}=k \mathbf{f}_{t+1}^{\prime}` and substitute into {eq}`eq:vpeq`

```{math}
:label: eq:vpec

\begin{aligned}
        \mathbf{f}_{t+1}^{\prime}(k-\alpha \Discount) & = \Rfree\Discount[\mathbf{f}_{t+2}^{\prime}(k-\alpha \Discount)] \\
      k \mathbf{f}_{t+2}^{\prime}(k-\alpha \Discount) & = \Rfree\Discount[\mathbf{f}_{t+2}^{\prime}(k-\alpha \Discount)] \\
  k & = \Rfree\Discount
\end{aligned}
```

so marginal utility grows at rate {math}`1/\Rfree\Discount`. Note that if we assume {math}`\alpha=0` so that habits do not matter, we again obtain the standard result that {math}`\uFunc^{\prime}(c_{t}) = \Rfree\Discount \uFunc^{\prime}(c_{t+1})`.

Now make the final assumption that {math}`\mathbf{f}(z) = z^{1-\CRRA}/(1-\CRRA)`, implying of course that {math}`\mathbf{f}^{\prime}(z) = z^{-\CRRA}`. Equation {eq}`eq:vpec` can be rewritten

```{math}
:label: eq:zfoc

1 = \Rfree\Discount (z_{t+1}/z_{t})^{-\CRRA}
```

Now expand {math}`z_{t+1}/z_{t}`

```{math}
:label: eq:noapprox

\frac{c_{t+1}-\alpha c_{t}}{c_{t}-\alpha c_{t-1}} = \frac{c_{t+1}/c_{t}-\alpha}{1-\alpha c_{t-1}/c_{t}}
```

```{math}
:label: eq:firstapprox

\approx \frac{1+\Delta \log c_{t+1}-\alpha}{1 - \alpha + \alpha \Delta \log c_{t}}
```

```{math}
:label: eq:secondapprox

= \frac{1-\alpha+\Delta \log c_{t+1}}{1 - \alpha + \alpha \Delta \log c_{t}}
```

```{math}
:label: eq:thirdapprox

= \frac{1+(\Delta \log c_{t+1})/(1-\alpha)}{1 + (\alpha/(1-\alpha)) \Delta \log c_{t}}
```

```{math}
:label: eq:cgrowapprox

\approx 1+\left(\frac{1}{1-\alpha}\right)\left(\Delta \log c_{t+1} - \alpha \Delta \log c_{t} \right)
```

where {eq}`eq:firstapprox` follows from {eq}`eq:noapprox` because {math}`c_{t+1}/c_{t} = 1+(c_{t+1}-c_{t})/c_{t} \approx 1+\Delta \log c_{t+1}` and {math}`c_{t-1}/c_{t} = (c_{t}-(c_{t}-c_{t-1}))/c_{t} \approx 1 - \Delta \log c_{t}`, and {eq}`eq:cgrowapprox` follows from {eq}`eq:thirdapprox` because for small {math}`\eta` and {math}`\epsilon`, {math}`(1+\eta)/(1+\epsilon) \approx 1+\eta-\epsilon`.

Substituting {eq}`eq:cgrowapprox` into {eq}`eq:zfoc` gives

```{math}
\begin{aligned}
        1 & \approx \Rfree\Discount (1+\left(\frac{1}{1-\alpha}\right)\left(\Delta \log c_{t+1} - \alpha \Delta \log c_{t} \right))^{-\CRRA} \\
      0  & \approx \log [\Rfree\Discount] - \CRRA \left(\frac{1}{1-\alpha}\right)\left(\Delta \log c_{t+1} - \alpha \Delta \log c_{t} \right) \\
\Delta \log c_{t+1} & \approx (1-\alpha)\CRRA^{-1}(\rfree - \timeRate) + \alpha \Delta \log c_{t}.
\end{aligned}
```

Thus, this formulation of habit formation implies that the growth rate of consumption is serially correlated.
