(sec:EntrepreneurPF)=

# An Entrepreneur's Problem Under Perfect Foresight
Consider a firm characterized by the following:

| Symbol | Description |
|--------|-------------|
| {math}`\kap_{t}` | Firm's capital stock at the beginning of period {math}`t` |
| {math}`\fFunc(\kap)` | The firm's total output depends only on {math}`k` |
| {math}`\inv_{t}` | Investment in period {math}`t` |
| {math}`\jFunc(i,k)` | Adjustment costs associated with investment {math}`\inv` given capital {math}`k` |
| {math}`\xpend_{t} = \inv_{t}+\adj_{t}` | Expenditures (purchases plus adjustment costs) on investment |
| {math}`\Discount=1/\Rfree` | Discount factor for future profits (inverse of interest factor) |

**With taxes:**[^tax-version]

[^tax-version]: The model can include corporate taxes. With taxes, additional parameters are: {math}`\TaxCorp` (tax rate on corporate earnings), {math}`\TaxFree = 1-\TaxCorp` (portion of earnings untaxed), {math}`\rev_{t} = \fFunc(\kap_{t})\TaxFree` (after tax revenues), {math}`\itc` (investment tax credit), {math}`\kPriceAfterITC=\PostITC = 1-\itc` (cost of 1 unit of investment after ITC), and {math}`\xpend_{t} = (\inv_{t}+\adj_{t})\kPriceAfterITC` (after-tax expenditures on investment).

Suppose that the firm's goal is to pick the sequence {math}`\iFunc_{t}` that solves:

```{math}
\begin{gathered}\begin{aligned}
  \vFirm(\kap_{t}) & =  \max_{\{\iFunc\}_{t}^{\infty}}~\sum_{n=0}^{\infty} \Discount^{n} \left(f_{t+n}-\inv_{t+n}-\adj_{t+n}\right)
\end{aligned}\end{gathered}
```

**With taxes:** {math}`\vFirm(\kap_{t}) = \max_{\{\iFunc\}_{t}^{\infty}}~\sum_{n=0}^{\infty} \Discount^{n} \left(\rev_{t+n}-\xpend_{t+n}\right)`

subject to the transition equation for capital,

```{math}
:label: eq:kAccum

\begin{gathered}\begin{aligned}
  \kap_{t+1} & =  (\kap_{t}+\inv_{t})\DeprFac
\end{aligned}\end{gathered}
```

where {math}`\DeprFac = (1-\depr)` is the amount of capital left after one period of depreciation at rate {math}`\depr`.[^timing-note] {math}`\vFirm_{t}` is the value of the profit-maximizing firm: If capital markets are efficient this is the equity value that the firm would command if somebody wanted to buy it.

[^timing-note]: There are some small differences between the formulation of the model here and in the [](#sec:qModel). Here, investment costs are paid at the time of investment and the depreciation factor applies to {math}`(\kap_{t}+\inv_{t})` rather than just {math}`\kap_{t}`. These changes simplify the computational solution without changing any key results.

:::{exercise}
:label: ex:firm-bellman
Show that the Bellman equation for the firm can be derived as follows:

```{math}
\begin{gathered}\begin{aligned}
  \vFirm_{t}(\kap_{t}) & =  \max_{\{\inv_{t}\}}~ f_{t}-\inv_{t}-\adj_{t}+\Discount \vFirm_{t+1}\left((\kap_{t}+\inv_{t})\DeprFac\right)
\end{aligned}\end{gathered}
```
:::

:::{solution} ex:firm-bellman
:class: dropdown
The firm's Bellman equation can be written:

```{math}
\begin{gathered}\begin{aligned}
  \vFirm_{t}(\kap_{t}) & =  \max_{\{\iFunc\}_{t}^{\infty}}~\sum_{n=0}^{\infty} \Discount^{n} \left(f_{t+n}-\inv_{t+n}-\adj_{t+n}\right)
  \\ & =  \max_{\{\inv_{t}\}}~ f_{t}-\inv_{t}-\jFunc(\inv_{t},\kap_{t})+\Discount \left[\max_{\{i\}_{t+1}^{\infty}}\sum_{n=0}^{\infty} \Discount^{n} \left(f_{t+1+n}-\inv_{t+1+n}-\adj_{t+1+n}\right)\right]
\\ & =  \max_{\{\inv_{t}\}}~ f_{t}-\inv_{t}-\jFunc(\inv_{t},\kap_{t})+\Discount \vFirm_{t+1}\left((\kap_{t}+\inv_{t})\DeprFac\right)
\end{aligned}\end{gathered}
```
:::

Define {math}`\adj_{t}^{\inv}` as the derivative of adjustment costs with respect to the level of investment.

:::{exercise}
:label: ex:inv-foc
Show that the first order condition for optimal investment implies

```{math}
\begin{gathered}\begin{aligned}
1+j^{\inv}_{t} & =  \DeprFac\Discount \vFirm_{t+1}^{\kap}(\kap_{t+1})
\end{aligned}\end{gathered}
```

and provide a verbal interpretation of the condition.
:::

:::{solution} ex:inv-foc
:class: dropdown
The first order condition for optimal investment implies:

```{math}
:label: eq:Entrep-iFOC

\begin{gathered}\begin{aligned}
  0 & =  -1 -j^{\inv}_{t} + \DeprFac\Discount \vFirm_{t+1}^{\kap}(\kap_{t+1})
\\ 1+j^{\inv}_{t} & =  \DeprFac\Discount \vFirm_{t+1}^{\kap}(\kap_{t+1})
\end{aligned}\end{gathered}
```

In words: The marginal cost of an additional unit of investment (the LHS) should be equal to the discounted marginal value of the resulting extra capital (the RHS).
:::

**With taxes:** {math}`(1+j^{\inv}_{t})\kPriceAfterITC = \DeprFac\Discount \vFirm_{t+1}^{\kap}(\kap_{t+1})`, where the LHS is the after-tax marginal cost of investment.

:::{exercise}
:label: ex:inv-euler
Now use the Envelope theorem to derive the Euler equation for investment

```{math}
\begin{gathered}\begin{aligned}
 (1+\adj_{t}^{\inv})  & = \DeprFac\Discount \left[ \fFunc^{\kap}(\kap_{t+1})+(1+\adj_{t+1}^{\inv}-\adj_{t+1}^{\kap})\right]
\end{aligned}\end{gathered}
```
:::

:::{solution} ex:inv-euler
:class: dropdown
The Envelope theorem says

```{math}
:label: eq:iEnvelope

\begin{gathered}\begin{aligned}
  \vFirm_{t}^{\kap}(\kap_{t}) & =  \fFunc^{\kap}(\kap_{t}) - \adj_{t}^{\kap}+\Discount \vFirm_{t+1}^{\kap}(\kap_{t+1})\overbrace{\left(\frac{\partial \kap_{t+1}}{\partial \kap_{t}}\right)}^{\DeprFac}
\\  & =  \fFunc^{\kap}(\kap_{t}) - \adj_{t}^{\kap}+\underbrace{\Discount \DeprFac \vFirm_{t+1}^{\kap}(\kap_{t+1})}_{=(1+\adj_{t}^{\inv})}
\end{aligned}\end{gathered}
```

where the underbraced term follows from {eq}`eq:Entrep-iFOC`. So the corresponding {math}`t+1` equation can be substituted into {eq}`eq:Entrep-iFOC` to obtain

```{math}
:label: eq:Entrep-iEuler

\begin{gathered}\begin{aligned}
 (1+\adj_{t}^{\inv})  & = \left( \fFunc^{\kap}(\kap_{t+1})+(1+\adj_{t+1}^{\inv}-\adj_{t+1}^{\kap})\right)\DeprFac\Discount
\end{aligned}\end{gathered}
```

which is the Euler equation for investment.
:::

**With taxes:** {math}`(1+\adj_{t}^{\inv})\kPriceAfterITC = \DeprFac\Discount \left[ \TaxFree\fFunc^{\kap}(\kap_{t+1})+(1+\adj_{t+1}^{\inv}-\adj_{t+1}^{\kap})\kPriceAfterITC\right]`

## Steady State

Now suppose that a steady state exists in which the capital stock is at its optimal level and is not adjusting, so costs of adjustment are zero: {math}`\adj_{t}=\adj_{t+1}=j^{\inv}_{t}=j^{\inv}_{t+1}=j^{\kap}_{t}=j^{\kap}_{t+1}=0`.

:::{exercise}
:label: ex:ss-capital
Use the investment Euler equation to show that the steady state level of the capital stock {math}`\check{k}` satisfies the equation below, and provide an intuitive interpretation of the equation.

```{math}
:label: eq:sskbar

\begin{gathered}\begin{aligned}
 \Rfree & =  \DeprFac (1+\fFunc^{\kap}(\check{k}))
\end{aligned}\end{gathered}
```
:::

:::{solution} ex:ss-capital
:class: dropdown
If {math}`j^{\inv}_{t} = j^{\inv}_{t+1} = j^{\kap}_{t+1}` then {eq}`eq:Entrep-iEuler` reduces to

```{math}
:label: eq:kSSimplicit

\begin{gathered}\begin{aligned}
 1 & = \overbrace{\Discount}^{=\Rfree^{-1}} \DeprFac\left[\fFunc^{\kap}(\check{k})+1\right]
\\ \Rfree & =  \DeprFac (1+\fFunc^{\kap}(\check{k}))
\end{aligned}\end{gathered}
```

so that the capital stock is equal to the value that causes its marginal product to match the interest factor, after compensating for depreciation.
:::

**With taxes:** {math}`\kPriceAfterITC\Rfree = \DeprFac (\kPriceAfterITC+\TaxFree\fFunc^{\kap}(\check{k}))`, so the capital stock equals the value that causes its after-tax marginal product to match the interest factor.

## Phase Diagram Analysis

Another way to analyze this problem is in terms of the marginal value of capital, {math}`\ek_{t} \equiv \vFirm_{t}^{\kap}(\kap_{t})`.

:::{exercise}
:label: ex:phase-diagram
Show that in the vicinity of the steady state, assuming that adjustment costs are approximately zero, the equation for {math}`\ek` will be

```{math}
\begin{gathered}\begin{aligned}
\ek_{t} & =  \frac{\fFunc^{\kap}(\kap_{t}) - \adj_{t}^{\kap}+\Delta \ek_{t+1}}{(1-\Discount\DeprFac)}
\end{aligned}\end{gathered}
```

and use this equation along with the transition equation for capital to draw a phase diagram in {math}`(\kap,\ek)` space for this model. Be sure to explain why the {math}`\Delta \ek_{t+1}=0` locus is downward sloping in the vicinity of the steady state.
:::

:::{solution} ex:phase-diagram
:class: dropdown
Rewrite {eq}`eq:iEnvelope` as

```{math}
\begin{gathered}\begin{aligned}
  \ek_{t} & =  \fFunc^{\kap}(\kap_{t}) - \adj_{t}^{\kap}+\Discount \DeprFac (\ek_{t}+\ek_{t+1}-\ek_{t})
\\ & =  \fFunc^{\kap}(\kap_{t}) - \adj_{t}^{\kap}+\Discount \DeprFac (\ek_{t}+\Delta \ek_{t+1})
\\ (1-\Discount\DeprFac) \ek_{t} & =  \fFunc^{\kap}(\kap_{t}) - \adj_{t}^{\kap}+\Delta \ek_{t+1}
\\ \ek_{t} & =  \frac{\fFunc^{\kap}(\kap_{t}) - \adj_{t}^{\kap}+\Delta \ek_{t+1}}{(1-\Discount\DeprFac)}
\end{aligned}\end{gathered}
```

and the phase diagram is constructed using the {math}`\Delta \ek_{t+1} = 0` locus. In the vicinity of the steady state, we can assume {math}`\adj_{t}^{\kap} \approx 0` in which case the {math}`\Delta \ek_{t+1}=0` locus becomes

```{math}
:label: eq:lamNearSS

\begin{gathered}\begin{aligned}
 \ek_{t} & =  \frac{\fFunc^{\kap}(\kap_{t})}{(1-\Discount\DeprFac)}
\end{aligned}\end{gathered}
```

which implies (since {math}`\fFunc^{\kap}(\kap_{t})` is downward sloping in {math}`\kap_{t}`) that the {math}`\Delta \ek_{t}=0` locus (that is, the {math}`\lambda_{t}(\kap_{t})` function that corresponds to {math}`\Delta \ek_{t}=0`) is downward sloping.

The phase diagram is depicted in {numref}`fig:Entrep-lPhaseDiag`.

:::{figure} ../sources/investment/EntrepreneurPF/LaTeX/Figures/lPhaseDiag.png
:name: fig:Entrep-lPhaseDiag
:width: 80%

Phase diagram showing the {math}`\Delta \ek=0` and {math}`\Delta \kap=0` loci.
:::
:::

The steady state of the model will be the point at which {math}`\kap_{t+1}=\kap_{t}=\check{\kap}`, implying from {eq}`eq:kAccum` a steady-state investment rate of

```{math}
:label: eq:iSS

\begin{gathered}\begin{aligned}
  \check{\kap} & =  (\check{\kap}+\check{i})\DeprFac
\\ \check{i} & =  (1-\DeprFac)\check{\kap}/\DeprFac = (\depr/\DeprFac) \check{\kap}
\end{aligned}\end{gathered}
```

and solving {eq}`eq:kSSimplicit` for {math}`\fFunc^{\kap}(\check{k})`

```{math}
\begin{gathered}\begin{aligned}
 \left(\frac{(1 - \Discount\DeprFac)}{\Discount \DeprFac}\right) & =   \fFunc^{\kap}(\check{k})
\end{aligned}\end{gathered}
```

which can be substituted into {eq}`eq:lamNearSS` to obtain the steady-state value of {math}`\ek`:

```{math}
\begin{gathered}\begin{aligned}
\check{\ek} & =   \left(\frac{\Rfree}{\DeprFac}\right) .
\end{aligned}\end{gathered}
```

## The Entrepreneur's Problem

We now wish to modify the problem in two ways. First, we have been assuming that the firm has only physical capital, and no financial assets. Second, we have been assuming that the manager running the firm only cares about the PDV of profits; suppose instead we want to assume that the firm is a small business run by an entrepreneur who must live off the dividends of the firm, and thus they are maximizing the discounted sum of utility from dividends {math}`\utilFunc(\cRat_t)` rather than just the level of discounted profits. (Note that we designate dividends by {math}`\cRat_{t}`; dividends were not explicitly chosen in the {math}`\q`-model version of the problem, because the Modigliani-Miller theorem says that the firm's value is unaffected by its dividend policy).

We call the maximizer running this firm the "entrepreneur." The entrepreneur's level of monetary assets {math}`m_{t}` evolves according to

```{math}
\begin{gathered}\begin{aligned}
  m_{t+1} & =  f_{t+1}+\left(m_{t}-\inv_{t}-\adj_{t}-\cRat_{t}\right)\Rfree.
\end{aligned}\end{gathered}
```

That is, next period the firm's money is next period's profits plus the return factor on the money at the beginning of this period, minus this period's investment and associated adjustment costs, minus dividends paid out (which, having been paid out, are no longer part of the firm's money).

**With taxes:** {math}`m_{t+1} = \rev_{t+1}+\left(m_{t}-\xpend_{t}-\cRat_{t}\right)\Rfree`

:::{exercise}
:label: ex:ent-bellman
Show that the entrepreneur's Bellman equation can now be written
:::

:::{solution} ex:ent-bellman
:class: dropdown
The entrepreneur's Bellman equation can now be written

```{math}
\begin{gathered}\begin{aligned}
  \vFunc_{t}(\kap_{t},m_{t}) & =  \max_{\{\inv_{t},\cRat_{t}\}}~~\utilFunc(\cRat_{t}) +\Discount \vFunc_{t+1}(\kap_{t+1},m_{t+1})
\end{aligned}\end{gathered}
```

**Derivation:** Value is simply the discounted sum of utility from future dividends:

```{math}
\begin{gathered}\begin{aligned}
  \vFunc_{t}(\kap_{t},m_{t}) & =  \max_{\{i,c\}_{t}^{\infty}} \sum_{n=0}^{\infty} \Discount^{n} \utilFunc(\cRat_{t+n})
\\ & =  \max_{\{i,c\}_{t}^{\infty}} \left(\utilFunc(\cRat_{t})+\Discount\sum_{n=0}^{\infty} \Discount^{n} \utilFunc(\cRat_{t+1+n})\right)
\\ & =  \max_{\{\inv_{t},\cRat_{t}\}}~~\utilFunc(\cRat_{t})+\Discount \vFunc_{t+1}(\kap_{t+1},m_{t+1}).
\end{aligned}\end{gathered}
```
:::

Assume that {math}`\fFunc` and {math}`\jFunc` do not depend directly on {math}`m_{t}`. That is, their partial derivatives with respect to {math}`m_{t}` are zero.

## Euler Equation for Dividends

:::{exercise}
:label: ex:div-euler
Use the first order condition with respect to dividends and the Envelope theorem with respect to money to show that the Euler equation for dividends is

```{math}
\begin{gathered}\begin{aligned}
 \uP(\cRat_{t}) & =  \Rfree\Discount \uP(\cRat_{t+1}) .
\end{aligned}\end{gathered}
```
:::

:::{solution} ex:div-euler
:class: dropdown
Then we will have

<!-- Version where it's $\uP(d)$: -->

FOC wrt {math}`\cRat_{t}`:

```{math}
\begin{gathered}\begin{aligned}
\uP(\cRat_{t}) & =  \Rfree\Discount \vNum^{m}_{t+1}
\end{aligned}\end{gathered}
```

Envelope wrt {math}`m_{t}`:

```{math}
\begin{gathered}\begin{aligned}
  \vNum_{t}^{m} & =  \Rfree\Discount \vNum_{t+1}^{m}
\end{aligned}\end{gathered}
```

and combining the FOC with the Envelope theorem we get the usual

```{math}
\begin{gathered}\begin{aligned}
  \vNum^{m}_{t} & =  \Rfree \Discount \vNum^{m}_{t+1}
\\ & =  \uP(\cRat_{t})
\\ & =  \Rfree\Discount \uP(\cRat_{t+1})
\\ & =  \uP(\cRat_{t+1})
\end{aligned}\end{gathered}
```

where the last line follows because we have assumed {math}`\Rfree\Discount=1`.
:::

## Alternative Formulation

:::{exercise}
:label: ex:alt-formulation
Next explain why the value function can be rewritten as shown below.
:::

:::{solution} ex:alt-formulation
:class: dropdown
Now note that the value function can be rewritten as

```{math}
:label: eq:vOfmtp1

\begin{gathered}\begin{aligned}
  \vFunc_{t}(\kap_{t},m_{t}) & =  \max_{\{\inv_{t},m_{t+1}\}}~~\utilFunc((f_{t+1}-m_{t+1})/\Rfree+m_{t}-\inv_{t}-\adj_{t}) +\Discount \vFunc_{t+1}(\kap_{t+1},m_{t+1})
\end{aligned}\end{gathered}
```

This holds because maximizing with respect to {math}`m_{t+1}` (subject to the accumulation equation) is equivalent to maximizing with respect to the components of {math}`m_{t+1}`.
:::

## Investment FOC for Entrepreneur

:::{exercise}
:label: ex:inv-foc-ent
Now show that for the version in {eq}`eq:vOfmtp1` the FOC with respect to {math}`\inv_{t}` is

```{math}
\begin{gathered}\begin{aligned}
  \uP(\cRat_{t})((1+\adj_{t}^{\inv})-f_{t+1}^{\kap}\DeprFac/\Rfree)& =  \DeprFac\Discount \vNum_{t+1}^{\kap}
\end{aligned}\end{gathered}
```
:::

:::{solution} ex:inv-foc-ent
:class: dropdown
For the version in {eq}`eq:vOfmtp1` the FOC with respect to {math}`\inv_{t}` is

```{math}
:label: eq:iFOCGen

\begin{gathered}\begin{aligned}
  \uP(\cRat_{t})((1+\adj_{t}^{\inv})-f_{t+1}^{\kap}\DeprFac/\Rfree)& =  \DeprFac\Discount \vNum_{t+1}^{\kap}
\end{aligned}\end{gathered}
```

**Derivation:** This holds because the derivative of the RHS of {eq}`eq:vOfmtp1` with respect to {math}`\inv_{t}` is

```{math}
\begin{gathered}\begin{aligned}
  \uP(\cRat_{t})\left(\left(\frac{\partial f_{t+1}}{\partial \kap_{t+1}}\frac{\partial \kap_{t+1}}{\partial \inv_{t}}\right)/\Rfree-\frac{\partial \inv_{t}}{\partial \inv_{t}}-\frac{\partial \adj_{t}}{\partial \inv_{t}}\right)+\Discount\left(\frac{\partial \kap_{t+1}}{\partial \inv_{t}}\right)\vFunc^{\kap}_{t+1}(\kap_{t+1},m_{t+1})
\end{aligned}\end{gathered}
```

(remember that {math}`m_{t+1}` is a control variable and thus its derivative with respect to investment is zero) so the FOC translates to

```{math}
\begin{gathered}\begin{aligned}
  \uP(\cRat_{t})(f_{t+1}^{\kap}\DeprFac/\Rfree-1-\adj_{t}^{\inv})+\Discount\DeprFac \vNum_{t+1}^{\kap}&=0
\end{aligned}\end{gathered}
```

which reduces to {eq}`eq:iFOCGen`.
:::

**With taxes:** {math}`\uP(\cRat_{t})(\kPriceAfterITC(1+\adj_{t}^{\inv})-\TaxFree f_{t+1}^{\kap}\DeprFac/\Rfree) = \DeprFac\Discount \vNum_{t+1}^{\kap}`

## Envelope Theorem for Capital

:::{exercise}
:label: ex:env-capital
Now use the envelope theorem with respect to {math}`\kap_{t}` to show that

```{math}
\begin{gathered}\begin{aligned}
  \vNum_{t}^{\kap} & =  \uP(\cRat_t)(f_{t+1}^{\kap}\DeprFac/\Rfree-\adj_{t}^{\kap})+\Discount \DeprFac \vNum_{t+1}^{\kap}
\end{aligned}\end{gathered}
```
:::

:::{solution} ex:env-capital
:class: dropdown
Now we can use the envelope theorem with respect to {math}`\kap_{t}` to show that

```{math}
:label: eq:kEnvelopeGen

\begin{gathered}\begin{aligned}
  \vNum_{t}^{\kap} & =  \uP(\cRat_t)(f_{t+1}^{\kap}\DeprFac/\Rfree-\adj_{t}^{\kap})+\Discount \DeprFac \vNum_{t+1}^{\kap}
\end{aligned}\end{gathered}
```

This can be seen by directly taking the derivative of the RHS of {eq}`eq:vOfmtp1` with respect to {math}`\kap_{t}`:

```{math}
\begin{gathered}\begin{aligned}
  \uP(\cRat_{t})\left(\left(\frac{\partial f_{t+1}}{\partial \kap_{t+1}}\frac{\partial \kap_{t+1}}{\partial \kap_{t}}\right)/\Rfree-\frac{\partial \adj_{t}}{\partial \kap_{t}}\right)+ \Discount \left(\frac{\partial \kap_{t+1}}{\partial \kap_{t}}\right) \vNum_{t+1}^{\kap}
\end{aligned}\end{gathered}
```

and noting that the Envelope theorem tells us the derivatives with respect to the controls {math}`m_{t+1}` and {math}`\inv_{t}` are zero while {math}`\partial \kap_{t+1}/\partial \kap_{t} = \DeprFac`.
:::

## Euler Equation for Investment (Entrepreneur)

:::{exercise}
:label: ex:inv-euler-ent
Next show how to combine {eq}`eq:iFOCGen` and {eq}`eq:kEnvelopeGen` to derive the Euler equation for investment.
:::

:::{solution} ex:inv-euler-ent
:class: dropdown
Now we can combine {eq}`eq:iFOCGen` and {eq}`eq:kEnvelopeGen` to derive the Euler equation for investment

```{math}
:label: eq:iEulerGen

\begin{gathered}\begin{aligned}
   (1+\adj_{t}^{\inv}) & = \DeprFac\Discount \left[ \fFunc^{\kap}(\kap_{t+1})+(1+\adj_{t+1}^{\inv}-\adj_{t+1}^{\kap})\right]
.
\end{aligned}\end{gathered}
```

**Derivation:** To see this, start with the Envelope theorem and substitute from {eq}`eq:iFOCGen`,

```{math}
:label: eq:vkEqup

\begin{gathered}\begin{aligned}
  \vNum_{t}^{\kap} & =  \uP(\cRat_{t})(f_{t+1}^{\kap}\DeprFac/\Rfree-\adj_{t}^{\kap})+\overbrace{\DeprFac \Discount \vNum_{t+1}^{\kap}}^{= \uP(\cRat_{t})((1+\adj_{t}^{\inv})-f_{t+1}^{\kap}\DeprFac /\Rfree)}
\\ & =  \uP(\cRat_{t})(f_{t+1}^{\kap}\DeprFac/\Rfree-\adj_{t}^{\kap})+\uP(\cRat_{t})((1+\adj_{t}^{\inv})-f_{t+1}^{\kap}\DeprFac /\Rfree)
\\ & =  \uP(\cRat_{t})\left(1+\adj_{t}^{\inv}-\adj_{t}^{\kap}\right)
\end{aligned}\end{gathered}
```

which means that we can rewrite {eq}`eq:iFOCGen` substituting the rolled-forward version:

```{math}
\begin{gathered}\begin{aligned}
  \uP(\cRat_{t})((1+\adj_{t}^{\inv})-f_{t+1}^{\kap}\DeprFac/\Rfree)& =  \DeprFac\Discount \vNum_{t+1}^{\kap}
\\  & =  \DeprFac\Discount \uP(\cRat_{t+1})\left(1+\adj_{t+1}^{\inv}-\adj_{t+1}^{\kap}\right)
\\   (1+\adj_{t}^{\inv}) & = \DeprFac\Discount \left[ \fFunc^{\kap}(\kap_{t+1})+(1+\adj_{t+1}^{\inv}-\adj_{t+1}^{\kap})\right]
\end{aligned}\end{gathered}
```

where the last line follows because with {math}`\Rfree\Discount=1` we know that {math}`\cRat_{t+1}=\cRat_{t}` implying {math}`\uP(\cRat_{t+1})=\uP(\cRat_{t})`.
:::

**With taxes:** {math}`\kPriceAfterITC (1+\adj_{t}^{\inv}) = \DeprFac\Discount \left[ \TaxFree\fFunc^{\kap}(\kap_{t+1})+\kPriceAfterITC(1+\adj_{t+1}^{\inv}-\adj_{t+1}^{\kap})\right]`

## Observational Equivalence

:::{exercise}
:label: ex:obs-equiv
Comment on the fact that the Euler equation for investment for the firm being run by a utility-maximizing manager, {eq}`eq:iEulerGen`, is identical to the Euler equation for the profit maximizing manager, {eq}`eq:Entrep-iEuler`, to discuss whether it matters, in this model, whether managers maximize profits or utility. Similarly comment on whether there would be any evidence from consumption dynamics that the consumer was running a business with costly capital adjustment.
:::

:::{solution} ex:obs-equiv
:class: dropdown
Since behavior (for either a firm manager or a consumer) is determined by Euler equations, and the Euler equations for both consumption and investment are identical in this model to the Euler equations for the standard models, there is no observable consequence for investment of the fact that the firm is being run by a utility maximizer, and there is no observable consequence for consumption of the fact that the consumer owns a business enterprise with costly capital adjustment.
:::

## Impulse Responses: Monetary Shock

Now consider a firm of this kind that happens to have arrived in period {math}`t` with positive monetary assets {math}`m_{t}>0` and with capital equal to the steady-state target value {math}`\kap_{t}=\check{k}`.

Suppose that a thief steals all the firm's monetary assets.

:::{exercise}
:label: ex:irf-monetary
Use the investment and consumption Euler equations to show the consequences for monetary assets, capital, dividends, and investment subsequently.
:::

:::{solution} ex:irf-monetary
:class: dropdown
The consequences for the firm are depicted in {numref}`fig:mlossIRF`.

:::{figure} ../sources/investment/EntrepreneurPF/LaTeX/Figures/mlossIRF.png
:name: fig:mlossIRF
:width: 80%

Impulse response to a negative shock to {math}`m_t` (monetary assets stolen).
:::

Dividends follow a random walk. Thus, there is a one-time downward adjustment to the level of dividends to reflect the stolen money. Thereafter dividends are constant, as are monetary assets (which are constant at zero forever).

The theft of the money has no effect on investment or the capital stock, because the firm's investment decisions are made on the basis of whether they are profitable and the theft of the money has no effect on the profitability of investments.
:::

## Impulse Responses: Capital Shock

Now consider another kind of shock: The firm's main building gets hit by a meteor, destroying some of the firm's capital stock.

:::{exercise}
:label: ex:irf-capital
Again show dynamics of monetary assets, capital, consumption, and investment.
:::

:::{solution} ex:irf-capital
:class: dropdown
The results are depicted in {numref}`fig:klossIRF`.

:::{figure} ../sources/investment/EntrepreneurPF/LaTeX/Figures/klossIRF.png
:name: fig:klossIRF
:width: 80%

Impulse response to a negative shock to {math}`k_t` (capital destroyed by meteor).
:::

Again, because dividends follow a random walk, what the firm's managers do is to assess the effect of the meteor shock on the firm's total value and they adjust the level of dividends downward immediately to the sustainable new level of dividends. Thereafter there is no change in the level of dividends.

Investment is more complicated. The firm's capital stock is obviously reduced below its steady-state value by the meteor, so there must be a period of high investment expenditures to bring capital back toward its steady state. However, the firm started out with monetary assets of zero. Therefore the high initial investment expenditures will be paid for by borrowing, driving the firm's monetary assets to a permanent negative value (the firm goes into debt to pay for its rebuilding). Gradually over time the capital stock is rebuilt back to its target level, and investment expenditures return to zero (or the level consistent with replacing depreciated capital).
:::

## Numerical Solution

The solution code uses the following definitions for the production and adjustment cost functions:[^numerical-note]

[^numerical-note]: The slight modification to the cost-of-adjustment function (relative to the formulation in the [](#sec:qModel)) reflects the changed timing of depreciation in {eq}`eq:kAccum` compared to the corresponding equation in qModel. In the continuous-time limit the two equations become the same, but the formulation here makes the representation of the problem slightly more transparent in the discrete-time computer code. The code also includes the parameters {math}`\kPriceAfterITC` and {math}`\TaxFree` (respectively the investment cost after the Investment Tax Credit and the untaxed portion of earnings) in order to study the impact of tax policies. Both parameters are however assumed equal to 1 and thus the equations in the code are equivalent to the simpler ones described in this section.

```{math}
:label: eq:fjFuncs

\begin{gathered}\begin{aligned}
\fFunc(k,\labor)&= \Psi k^\kapShare \labor^{1-\kapShare} \\
\jFunc(i,\kap)&=\frac{\omega k}{2}\left(\frac{i}{k}-\frac{\depr}{\DeprFac}\right)^2
\end{aligned}\end{gathered}
```

where {math}`\Psi` is the firm's productivity and {math}`\labor` is the labor supplied by the entrepreneur (assumed equal to 1).

The policy functions are obtained using the method of *reverse shooting*, which is based on recovering for a given {math}`k_{t+1}` and {math}`\vFirm_{t+1}(k_{t+1})` the values of {math}`k_t`, {math}`i_t` and {math}`\vFirm_{t}(k_{t})` consistent with the first order conditions and transition equations.

The reverse-shooting equation for capital comes from a combination of the dynamic budget constraint and the Euler equation. For convenience defining

```{math}
\begin{gathered}\begin{aligned}
  z_t& \equiv k_{t+1}/\DeprFac
\end{aligned}\end{gathered}
```

so that

```{math}
:label: eq:izk

\begin{gathered}\begin{aligned}
  i_{t} = z_{t}-k_{t},
\end{aligned}\end{gathered}
```

we can rewrite the investment Euler equation as

```{math}
\begin{gathered}\begin{aligned}
 (1+j_{t}^{i}) & = \DeprFac\Discount \left( \fFunc^{k}(k_{t+1})+(1+j_{t+1}^{i}-j_{t+1}^{k})\right)\\
 \left(1+\omega\left(\frac{\overbrace{i_t}^{z_{t}-k_{t}}}{k_t}-\frac{\depr}{\DeprFac}\right)\right) & = \DeprFac\Discount \left( \fFunc^{k}(k_{t+1})+(1+j_{t+1}^{i}-j_{t+1}^{k})\right)
\end{aligned}\end{gathered}
```

so that

```{math}
\begin{gathered}\begin{aligned}
\frac{z_t}{k_t}-1 & =\DeprFac\Discount\left( \fFunc^{k}(k_{t+1})+(1+j_{t+1}^{i}-j_{t+1}^{k})\right)/\omega-1/\omega+\depr/\DeprFac\\
k_t&=\frac{z_t}{\DeprFac\Discount\left( \fFunc^{k}(k_{t+1})+(1+j_{t+1}^{i}-j_{t+1}^{k})\right)/\omega-1/\omega+\depr/\DeprFac+1}.
\end{aligned}\end{gathered}
```

With the values of {math}`i_{t}` and {math}`j_{t}` obtained from these reverse-shooting equations, the reverse-shooting equation for value is very simple: It is the Bellman equation

```{math}
\begin{gathered}\begin{aligned}
  \vFirm_{t}(k_{t})&=f_{t}-i_{t}-j_{t}+\vFirm_{t+1}(k_{t+1})/\Rfree,
\end{aligned}\end{gathered}
```

where note that {math}`f_{t}` and {math}`i_{t}-j_{t}` are direct functions of {math}`k_{t}` and {math}`i_{t}` which we have already computed.

The steady-state level of capital can be obtained from {eq}`eq:kSSimplicit`:

```{math}
:label: eq:Entrep-kSS

\begin{gathered}\begin{aligned}
 \Rfree/\DeprFac -1 & =   \fFunc^{k}(\check{k})
\\ \frac{1}{\alpha} \left(\Rfree/\DeprFac -1\right) & =   \check{k}^{\kapShare-1}
\\ \left(\frac{1}{\alpha} \left(\Rfree/\DeprFac -1\right)\right)^{1/(\kapShare-1)} & =   \check{k}
\end{aligned}\end{gathered}
```

while the steady-state value of {math}`\ek` comes from substituting {math}`\check{\kap}` into {eq}`eq:lamNearSS`. Steady-state value is straightforward to compute, given that in the steady state the capital stock and amount of investment are constant:

```{math}
\begin{gathered}\begin{aligned}
  \check{\vFirm} & =  \sum_{n=0}^{\infty} (\fFunc(\check{\kap})-\check{i})\Discount^{n}
\\ & =  (\Rfree/\rfree)(\fFunc(\check{\kap}) - \check{i}).
\end{aligned}\end{gathered}
```

The reverse shooting routine starts its backwards iterations from a {math}`k_{\hat{t}}` level very close to the steady state of the model and, as discussed in the methodological appendix to the TractableBufferStock section, the accuracy of the solution is improved if we approximate {math}`i_{\hat{t}}` with a first order Taylor expansion using the derivative of investment at the steady state:

```{math}
\begin{gathered}\begin{aligned}
    i_{\hat{t}}&=\check{i}+\check{i}^k\epsilon
\end{aligned}\end{gathered}
```

where the {math}`\check{~}` identifies variables at the steady state and {math}`\epsilon` is the deviation from the steady state. {math}`\check{i}^k` is computed by differentiating the Euler equation with respect to {math}`\kap`:

```{math}
\begin{gathered}\begin{aligned}
    (j^{ii}_t i^k_t+j^{ik}_t) = \DeprFac\Discount\left(f^{kk}_{\hat{t}}\DeprFac(1+i^k_t)+(j^{ik}_{\hat{t}}\DeprFac(1+i^k_t)+j^{ii}_{\hat{t}}i^k_{\hat{t}}
-j^{kk}_{\hat{t}}\DeprFac(1+i^k_t)-j^{ki}_{\hat{t}}i^k_{\hat{t}})\right)
\end{aligned}\end{gathered}
```

which at the steady-state where {math}`i^{k}_{\hat{t}}=i^{k}_{t}=\check{i}^{k}` becomes:

```{math}
:label: eq:iEulerSS

\begin{gathered}\begin{aligned}
    (j^{ii}_t \check{i}^k+j^{ik}_t)=\DeprFac\Discount\left(f^{kk}_{\hat{t}}\DeprFac(1+\check{i}^k)+(j^{ik}_{\hat{t}}\DeprFac(1+\check{i}^k)+j^{ii}_{\hat{t}}\check{i}^k-j^{kk}_{\hat{t}}\DeprFac(1+\check{i}^k)
    -j^{ki}_{\hat{t}}\check{i}^k)\right)
\end{aligned}\end{gathered}
```

and given any particular set of parameter values {math}`\check{i}^k` can be found using standard numerical rootfinding methods.

Finally since the problem is solved under perfect foresight the entrepreneur's consumption function is simply:

```{math}
\begin{gathered}\begin{aligned}
    \cons_t=\left(\frac{\Rfree-(\Rfree\Discount)^{1/\CRRA}}{\Rfree}\right)(m_t+\vFirm_{t}(k_{t})-f_t)
\end{aligned}\end{gathered}
```

because this corresponds to the solution to a perfect foresight consumption problem in which the consumer has monetary resources {math}`m_{t}` and net nonmonetary financial resources {math}`\vFirm_{t}(k_{t})-f_t` (see the [](#sec:PerfForesightCRRA)).
