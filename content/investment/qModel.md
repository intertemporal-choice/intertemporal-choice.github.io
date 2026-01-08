(sec:qModel)=

# The Abel (1981)-Hayashi (1982) Marginal q Model
This section presents a discrete-time version of the Abel {cite:t}`abel:q`-Hayashi {cite:t}`hayashi:q` marginal {math}`\q` model of investment.

A corresponding [Jupyter Notebook](https://github.com/econ-ark/DARKolo/blob/master/chimeras/qModel/qModel-Template-Section-Figures.ipynb) implements numerical solutions to the model using [HARK](https://github.com/econ-ark/HARK) and [dolo](https://dolo.readthedocs.io/en/doc/).

(Definitions)=
## Definitions

To simplify some algebra, we assume that a unit of investment purchased in period {math}`t` does not become productive until {math}`t+1`; the cost at {math}`t` reflects the present discounted value of the period-{math}`t+1` price of capital.[^timing-simplification]

[^timing-simplification]: This assumption simplifies many of the expressions that arise in the discrete-time framework; in continuous time the model presentation is simpler, but is hard to map the continuous-time theory into a transparent computational solution like the one that accompanies these notes.

Adjustment costs are priced the same way.[^itc-resale] We repeatedly make approximations motivated by results from the continuous-time model; the key approximation will be the usual calculus result that if {math}`\epsilon` and {math}`\gamma` are "small" then {math}`\epsilon\gamma` can be approximated by zero. (We will call this fact [SmallSmallZero](#fact:smallsmallzero) in the MathFactsList.)[^tax-depreciation]

[^itc-resale]: To avoid arbitrage opportunities, assume that if you claimed an investment tax credit on a unit of investment in period {math}`t`, then if you resell the portion that remains after depreciation in a future period, you must repay the ITC corresponding to the remaining capital. Actual tax treatment of depreciation is too complicated be worth incorporating into the model; these assumptions capture the core of it.

[^tax-depreciation]: We neglect tax depreciation because, as shown in the [](#sec:HallJorgenson) section, it matters only insofar as it affects the cost of capital; since the investment tax credit has a more transparent and direct effect on the cost of capital, including tax depreciation would add complication without adding any fundamental insights to the analysis. In the perfect foresight framework analyzed here, any attempt to analyze the effects of changes in tax depreciation should be translatable into an equivalent modification to the ITC. See {cite:t}`hsITC` for elaboration.

| Symbol | | Definition |
| --- | --- | --- |
| {math}`k_{t}` | - | Firm's capital stock at the beginning of period {math}`t` |
| {math}`\fFunc(k)` | - | Gross output excluding investment and adjustment costs |
| {math}`\TaxCorp` | - | Tax rate on corporate earnings |
| {math}`\TaxFree` | - | {math}`1-\TaxCorp` = Portion of earnings remaining after corporate tax |
| {math}`\rev_{t} = \fFunc(k_{t})\TaxFree` | - | After tax revenues |
| {math}`i_{t}` | - | Investment in period {math}`t` (affects capital stock in period {math}`t+1`) |
| {math}`j_{t} = \adj(i_{t},k_{t})` | - | AdJustment costs incurred in period {math}`t`; smooth and convex |
| {math}`\Discount=\Rfree^{-1}` | - | Discount factor for future profits (inverse of interest factor) |
| {math}`\itc` | - | Investment tax credit (ITC) |
| {math}`\PostITC` | - | {math}`=1-\itc` = Cost of investment after ITC |

**With time-varying price:** {math}`\kPrice_{t}` denotes the price of one unit of investment, and {math}`\kPriceAfterITC_{t}=\PostITC \kPrice_{t}` is the effective after-tax price of 1 unit of investment.

**With constant price:** When {math}`\kPrice_{t}=1`, the after-tax price simplifies to {math}`\PostITC`.

| Symbol | | Definition |
| --- | --- | --- |
| {math}`\xpend_{t} = (i_{t}+j_{t})\kPriceAfterITC_{t+1}\Discount` | - | Total after-tax period-{math}`t` spending on investment (with time-varying price) |
| {math}`\xpend_{t} = (i_{t}+j_{t})\PostITC_{t+1}\Discount` | - | Total after-tax period-{math}`t` spending on investment (with constant price) |
| {math}`\depr` | - | Depreciation rate |
| {math}`\daleth` | - | Depreciation factor {math}`=(1-\depr)` |
| {math}`\omega` | - | Adjustment cost parameter |

(The-Problem)=
## The Problem

The {math}`\q` model assumes that firms maximize the net profits payable to shareholders, definable as the present discounted value of after-tax revenues after subtracting off costs of investment:

```{math}
\begin{aligned}
\vFirm_{t}(k_{t}) & = \max_{\{i\}_{t}^{\infty}}~\Ex_{t}\left[\sum_{n=0}^{\infty} \Discount^{n} \left(\rev_{t+n}-\xpend_{t+n}\right)\right].
\end{aligned}
```

Next period's capital is what remains of this period's capital after depreciation, plus current investment:[^timing-alternative]

[^timing-alternative]: The [software archive](https://github.com/econ-ark/DARKolo/blob/master/chimeras/qModel) that produces the figures for this section makes a slightly different assumption about the timing of depreciation: {math}`k_{t+1} = (i_{t}+k_{t})\daleth.` The timing choice makes no qualitative and very little quantitative difference, but the alternative specification is slightly better for computational reasons.

```{math}
\begin{aligned}
k_{t+1} & = k_{t}\daleth+i_{t}.
\end{aligned}
```

If capital markets are efficient, {math}`\vFirm_{t}(\kap_{t})` will also be the stock market value ("**e**quity" is the mnemonic) of the profit-maximizing firm because it is precisely the amount that a rational investor will be willing to pay if they care only about discounted after-tax income derived from owning (a share of) the firm.

We can simplify by thinking about the firm's shareholders as the suppliers of physical capital, not just financial capital. In this interpretation, {math}`\kap` represents not just the value of the physical machinery owned by the firm, but also the number of shares of stock outstanding in the firm. We can think of the firm in this way if we suppose that every time the firm purchases new physical capital, it does so by issuing new shares at a price equal to the marginal valuation of the firm's capital stock, purchasing the unit of capital at the price given by the after-tax cost of that capital (and after paying any associated adjustment costs).[^itc-share-price]

[^itc-share-price]: This leads to some subtlety in thinking about what happens to the firm's share price when an ITC is introduced; we discuss this briefly below.

The Bellman equation for the firm's value can be derived from

```{math}
:label: eq:nudef

\begin{aligned}
\vFirm_{t}(k_{t}) & = \max_{i_{t}}~ \rev_{t}-\xpend_{t}+\Discount \Ex_{t}\left[\max_{\{i\}_{t+1}^{\infty}}\sum_{n=0}^{\infty} \Discount^{n} \left(\pi_{t+1+n}-\xpend_{t+1+n}\right)\right] \\
& = \max_{i_{t}}~ \rev_{t}-\xpend_{t}+\Discount \Ex_{t}[\vFirm_{t+1}(k_{t}\daleth + i_{t})]
\end{aligned}
```

which is equivalent to

```{math}
:label: eq:nuequiv

\begin{aligned}
\vFirm_{t}(k_{t}) & = \max_{k_{t+1}} \left\{ \rev_{t}-(\overbrace{k_{t+1}-k_{t}\daleth}^{=i_{t}}+\adj(k_{t+1}-k_{t}\daleth,k_{t}))\kPriceAfterITC_{t+1}\Discount+\Discount \Ex_{t}[\vFirm_{t+1}(k_{t+1})]\right\}
\end{aligned}
```

and defining {math}`j_{t}^{i}=\adj^{i}(i_{t},k_{t})` as the derivative of adjustment costs with respect to the level of investment,[^adj-function-structure] the first order condition for optimization with respect to {math}`\kap_{t+1}` (or, equivalently, {math}`i_{t}`) is

[^adj-function-structure]: We implicitly assume in the following derivations that the structure of the {math}`\adj` function is appropriate to our needs; later we will define a specific {math}`\adj` that will always work, but here we want to leave the structure of the function general.

```{math}
:label: eq:qMod-iFOC

\begin{aligned}
(1+j_{t}^{i})\kPriceAfterITC_{t+1}\Discount & = \Discount \Ex_{t}[\vFirm_{t+1}^{k}(k_{t+1})].
\end{aligned}
```

Thus: The PDV of the marginal cost (after tax, including adjustment costs) of an additional unit of investment should match the discounted expected marginal value of the resulting extra capital. (Recall that investment performed today {math}`i_{t}` is paid for tomorrow at price {math}`\kPriceAfterITC_{t+1}` so today's cost is {math}`\kPriceAfterITC_{t+1}\Discount`.)

Recalling that {math}`\pi_{t} = \TaxFree\fFunc(k_{t})`, the [](#sec:Envelope) theorem for this problem can be used on either {eq}`eq:nudef` or {eq}`eq:nuequiv`:

```{math}
\begin{aligned}
\vFirm_{t}^{k}(k_{t}) & = \TaxFree\fFunc^{k}(k_{t})-j_{t}^{k}\kPriceAfterITC_{t+1}\Discount +\daleth \Discount \Ex_{t}[\vFirm_{t+1}^{k}(k_{t+1})] \\
\vFirm_{t}^{k}(k_{t}) & = \TaxFree\fFunc^{k}(k_{t}) + ((1 + j_{t}^{i})\daleth-j_{t}^{k})\kPriceAfterITC_{t+1}\Discount
\end{aligned}
```

and equivalently for period {math}`t+1` so that {eq}`eq:qMod-iFOC` can be rewritten as the Euler equation for investment,

```{math}
:label: eq:qMod-iEuler

\begin{aligned}
(1+j_{t}^{i})\kPriceAfterITC_{t+1} & = \Ex_{t}[\TaxFree\fFunc^{k}(k_{t+1}) +( \daleth + \daleth j_{t+1}^{i}-j_{t+1}^{k})\kPriceAfterITC_{t+2}\Discount] \\
& = \Ex_{t}[\TaxFree\fFunc^{k}(k_{t+1}) +( \daleth + j_{t+1}^{i}-\depr j_{t+1}^{i} -j_{t+1}^{k})\kPriceAfterITC_{t+2}\Discount].
\end{aligned}
```

It will be useful to define the *net investment ratio* as the Greek letter {math}`\iota` (the absence of a dot distinguishes {math}`\iota` from the level of investment {math}`i`),

```{math}
:label: eq:iotaDef

\begin{aligned}
\iota_{t} & = (i_{t}/k_{t} - \depr)
\end{aligned}
```

which measures how much investment differs from the proportion {math}`\depr` necessary to maintain the capital stock unchanged. It has derivatives

```{math}
:label: eq:iotai

\begin{aligned}
\iota_{t}^{i} & = (1/k_{t}) \\
\iota_{t}^{k} & = - (i_{t}/k_{t})/k_{t} \\
& = - (\iota_{t}+\depr)/k_{t}.
\end{aligned}
```

We now specify a convex (quadratic) adjustment cost function as

:::{margin}
Explain why; draw diagram centered around {math}`\depr`.
:::

```{math}
\begin{aligned}
\adj(i_{t},k_{t}) & = (k_{t}/2) \left(\frac{i_{t}-\depr k_{t}}{k_{t}}\right)^{2}\omega \\
& = (k_{t}/2) \iota_{t}^{2}\omega
\end{aligned}
```

with derivatives (using {eq}`eq:iotai` to simplify)

```{math}
:label: eq:jk

\begin{aligned}
\adj^{i} & = k \iota\omega\iota^{i} \\
& = \iota\omega \\
\adj^{k} & = \left(\iota^{2}/2 - k \iota(\iota+\depr)/k\right)\omega \\
& = \left(\iota^{2}/2 - \iota(\iota+\depr)\right)\omega \\
& = -\left(\iota^{2}/2 + \iota \depr\right)\omega \\
\adj^{i} - \depr \adj^{i} - \adj^{k} & = \left(\iota - \depr \iota + \left(\iota^{2}/2 + \iota \depr\right)\right)\omega \\
& = \left(\iota + \iota^2/2\right)\omega \\
& = \adj^{i}+(\omega/2)\iota^{2}
\end{aligned}
```

so the Euler equation for investment {eq}`eq:qMod-iEuler` can be written

```{math}
:label: eq:iEuler2

\begin{aligned}
(1+\adj_{t}^{i})\kPriceAfterITC_{t+1} & = \Ex_{t}[\TaxFree\fFunc^{k}(k_{t+1}) +( \daleth + \adj_{t+1}^{i}+(\omega/2)\iota^{2}_{t+1})\kPriceAfterITC_{t+2}\Discount].
\end{aligned}
```

To begin interpreting this equation, consider first the case where the costs of adjustment are zero, {math}`\omega = 0`. In this case {math}`\adj^{i}=\adj^{k}=0` and the Euler equation reduces to

```{math}
\begin{aligned}
% \kPriceAfterITC_{t+1}\Discount & = \Discount \daleth \Ex_{t}[\TaxFree\fFunc^{k}(k_{t+1}) + \kPriceAfterITC_{t+2}\Discount].
\kPriceAfterITC_{t+1} & = \Ex_{t}[\TaxFree\fFunc^{k}(k_{t+1}) + \daleth \kPriceAfterITC_{t+2}\Discount].
\end{aligned}
```

Simplifying further, suppose that capital prices are constant at {math}`\kPrice_{t}=1` and the ITC is unchanging so that the after-tax price of capital is constant at {math}`\kPriceAfterITC`. Then since {math}`1+\rfree+\depr \approx 1/\Discount \daleth`, the equation becomes

```{math}
:label: eq:qMod-KSS

\begin{aligned}
\kPriceAfterITC & = \Ex_{t}[\TaxFree\fFunc^{k}(k_{t+1})] + \kPriceAfterITC\Discount \daleth \\
(\rfree+\depr)\kPriceAfterITC & \approx \Ex_{t}[\TaxFree\fFunc^{k}(k_{t+1})].
\end{aligned}
```

This says that the cost of buying one unit of capital, {math}`\kPriceAfterITC`, is equal to the opportunity cost in lost interest plus the value lost to depreciation, {math}`(\rfree+\depr)`, which must match the (after-tax) payoff from ownership of that capital. This corresponds exactly to the formula for the equilibrium cost of capital in the [](#sec:HallJorgenson) model: In the presence of an investment tax credit at rate {math}`\itc`, the after-tax price of capital is {math}`\kPriceAfterITC=\PostITC`, and the firm will adjust its holdings of capital to the point where

```{math}
\begin{aligned}
\PostITC(\rfree+\depr)/\TaxFree & = \fFunc^{k}(k).
\end{aligned}
```

Now define {math}`\vk_{t} \equiv \vFirm_{t}^{k}` as the marginal value to the firm of ownership of one more unit of capital at the beginning of period {math}`t`; using this definition, the envelope condition can be written

```{math}
:label: eq:lambdadyn

\begin{aligned}
\vk_{t} & = \TaxFree\fFunc^{k}(k_{t})- j_{t}^{k}\kPriceAfterITC_{t+1}\Discount+\Discount \daleth \Ex_{t}[\vk_{t+1}] \\
& \approx \TaxFree\fFunc^{k}(k_{t})- j_{t}^{k}\kPriceAfterITC_{t+1}\Discount+(1-\depr-\rfree) \Ex_{t}[\vk_{t}+\vk_{t+1}-\vk_{t}] \\
% & = \TaxFree\fFunc^{k}(k_{t})+\Discount \Ex_{t}[\vk_{t}+(\vk_{t+1}-\vk_{t})] + (\daleth+j_{t}^{k})\kPriceAfterITC_{t+1}\Discount
& = \TaxFree\fFunc^{k}(k_{t})- j_{t}^{k}\kPriceAfterITC_{t+1}\Discount+(1-\depr-\rfree) (\vk_{t}+\Ex_{t}[\Delta \vk_{t+1}] ) \\
(\rfree+\depr) \vk_{t} & \approx \TaxFree\fFunc^{k}(k_{t})- j_{t}^{k}\kPriceAfterITC_{t+1}\Discount + \Ex_{t}[\Delta \vk_{t+1}]
\end{aligned}
```

where the last approximation uses {math}`\mathtt{SmallSmallZero}` in the form {math}`(\rfree+\depr) \Ex_{t}[\Delta \vk_{t+1}] \approx 0`. Equation {eq}`eq:lambdadyn` can be rearranged as

```{math}
:label: eq:Edl

\begin{aligned}
\Ex_{t}[\Delta \vk_{t+1}] & \approx \rfree \vk_{t} - \left[\TaxFree\fFunc^{k}(k_{t})- j_{t}^{k}\kPriceAfterITC_{t+1}\Discount-\depr \vk_{t} \right].
\end{aligned}
```

This equation can best be understood as an arbitrage equation for the share price of the company if capital markets are efficient.[^arbitrage-interpretation] The first term on the RHS {math}`\rfree\vk_{t}` is the flow of income that would be obtained from putting the value of an extra unit of capital in the bank. The term in brackets {math}`[]` is the flow value of having an extra unit of capital inside the firm: Extra after-tax revenues are measured by the first term, the second term accounts for the effect of the extra capital on costs of adjustment, and the final term reflects the cost to the firm of the extra depreciation that results from having more capital.

[^arbitrage-interpretation]: This interpretation requires the assumption (made above) that the number of shares outstanding for the firm is equal to the number of units of capital the firm has; this is justifiable by the assumption that in an efficient capital market shares can always be issued or repurchased at an implicit interest rate corresponding to the riskless rate.

Think first about the {math}`\Ex_{t} [\Delta \vk_{t+1}] = 0` case, in which the firm's value, share price, and size will be unchanging because the marginal value of capital inside the firm is equal to the opportunity cost of employing that capital outside the firm (leaving it in the bank). If these two options yield equivalent returns, it is because the firm is already the "right" size and should be neither growing nor shrinking.

Now consider the case where {math}`\Ex_{t} [\Delta \vk_{t+1}] < 0`, because

```{math}
\begin{aligned}
\rfree \vk_{t} & < \left[\TaxFree\fFunc^{k}(k_{t})-\kPriceAfterITC_{t+1}\Discount j_{t}^{k}-\depr \vk_{t} \right].
\end{aligned}
```

This says that an extra unit of capital is more valuable inside the firm than outside it, which means that 1) {math}`\vk_{t}` is above its steady-state value; 2) the firm will have positive net investment; and 3) the firm's share value will be falling over time (because the *level* of its share value today is high, reflecting the fact that the high marginal valuation of the firm's future investment has already been incorporated into {math}`\vk_{t}`).[^rising-prices-symmetric]

[^rising-prices-symmetric]: The case with rising share prices is symmetric.

Now define "marginal {math}`\q`" as the value of an additional unit of capital inside the firm divided by the after-tax purchase price of an additional unit of capital,

:::{margin}
Warn them that choices of variable names are subtly different from Romer's; what I call {math}`\vk` Romer calls {math}`\q`, and Romer also makes a different assumption about the production function.
:::

```{math}
\begin{aligned}
\q_{t} & = \vk_{t}/\kPriceAfterITC_{t}.
\end{aligned}
```

The investment first order condition {eq}`eq:qMod-iFOC` implies

```{math}
\begin{aligned}
(1+\adj^{i})\kPriceAfterITC_{t+1}\Discount & = \Discount \vk_{t+1} \\
1+\iota_{t}\omega & = \q_{t+1}
\end{aligned}
```

which constitutes the implicit definition of a function

```{math}
\begin{aligned}
% 1+\iota_{t}\omega & = \q_{t+1}
\pmb{\iota}(\q_{t+1}) & \equiv (\q_{t+1}-1)/\omega \\
i_{t} & = (\pmb{\iota}(\q_{t+1})+\depr)k_{t}
\end{aligned}
```

and notice that this implies

- At a value of {math}`\q_{t+1}=1`, investment takes place at a rate exactly equal to the depreciation rate ({math}`\pmb{\iota}(1)=0`)
- The investment ratio {math}`\iota_{t}` is monotonically increasing in {math}`\q_{t+1}` ({math}`\pmb{\iota}^{\prime}(\q_{t+1})>0`)
- The strength with which {math}`\iota_{t}` is related to {math}`\q_{t+1}` depends on the magnitude of adjustment costs ({math}`d |\pmb{\iota}_{t}| / d \omega < 0`)

(Phase-Diagrams)=
## Phase Diagrams

(Dynamics-of-k)=
### Dynamics of {math}`k`

The capital accumulation equation can be rewritten as

```{math}
:label: eq:qMod-kdyn

\begin{aligned}
k_{t+1} & = (1-\depr) k_{t} + i_{t} \\
\Delta k_{t+1} & = i_{t} - \depr k_{t} \\
& = \pmb{\iota}(\q_{t+1}) k_{t}.
\end{aligned}
```

(Dynamics-of-q)=
### Dynamics of {math}`\q`

To construct a phase diagram involving {math}`\q`, we need to transform our equation {eq}`eq:lambdadyn` for the dynamics of {math}`\vk` into an equation for the dynamics of {math}`\q`. As a preliminary, define the proportional change in the after-tax price of capital as

```{math}
\begin{aligned}
\nabla \kPriceAfterITC_{t+1} & \equiv \Delta \kPriceAfterITC_{t+1}/\kPriceAfterITC_{t}.
\end{aligned}
```

:::{admonition} Commented alternative definition
:class: dropdown

```{math}
\begin{aligned}
\iCost_{t} & = \kPriceAfterITC_{t}/\cancel{\Omega}_{t}.
\end{aligned}
```
:::

Recalling that {math}`\kPriceAfterITC_{t+1}=\Delta \kPriceAfterITC_{t+1} + \kPriceAfterITC_{t}`, dividing both sides of {eq}`eq:lambdadyn` by {math}`\kPriceAfterITC_{t}` yields

```{math}
:label: eq:qdel

\begin{aligned}
(\rfree+\depr) \q_{t} & = \TaxFree\fFunc^{k}(k_{t})/\kPriceAfterITC_{t} - j_{t}^{k}(\Delta \kPriceAfterITC_{t+1}+\kPriceAfterITC_{t})\Discount/\kPriceAfterITC_{t} + \Ex_{t} \left[\left(\frac{ \vk_{t+1}}{\kPriceAfterITC_{t}}\right)-\left(\frac{ \vk_{t}}{\kPriceAfterITC_{t}}\right)\right] \\
& \approx \TaxFree\fFunc^{k}(k_{t})/\kPriceAfterITC_{t} - (1+\nabla \kPriceAfterITC_{t+1})j_{t}^{k}\Discount + \Ex_{t} \left[\left(\frac{ \vk_{t+1}}{\kPriceAfterITC_{t+1}}(1+\nabla \kPriceAfterITC_{t+1})\right)-\q_{t}\right] \\
& = \TaxFree\fFunc^{k}(k_{t})/\kPriceAfterITC_{t} - (1+\nabla \kPriceAfterITC_{t+1})j_{t}^{k}\Discount + \Ex_{t} \left[(1+\nabla \kPriceAfterITC_{t+1})\q_{t+1}-\q_{t}\right].
\end{aligned}
```

Now assuming that {math}`\Delta \q_{t+1}`, {math}`\nabla \kPriceAfterITC_{t+1}`, {math}`\rfree`, and {math}`j^{k}_{t}` are all "small" so that their interactions are approximately 0, we have

```{math}
:label: eq:dq

\begin{aligned}
% (\rfree+\depr) \q_{t} & \approx \TaxFree\fFunc^{k}(k_{t})/\kPriceAfterITC_{t} + \q_{t+1} \nabla \kPriceAfterITC_{t+1} + \Ex_{t} \left[ \Delta \q_{t+1}\right]
\Ex_{t} \left[ \Delta \q_{t+1}\right] & \approx (\rfree+\depr-\nabla \kPriceAfterITC_{t+1}) \q_{t} - [\TaxFree\fFunc^{k}(k_{t})/\kPriceAfterITC_{t}-j^{k}_{t}\Discount].
\end{aligned}
```

Simplifying further, if the ITC is unchanging, and the pretax price of capital is unchanging at {math}`\kPrice_{t+1}=\kPrice_{t} = 1`, and {math}`\depr=0`, equation {eq}`eq:dq` becomes

```{math}
:label: eq:qdyn

\begin{aligned}
\Ex_{t}[\Delta \q_{t+1}] & \approx \rfree \q_{t} - \fFunc^{k}(k_{t})/\TaxComb_{t} + j_{t}^{k}\Discount
% \Delta k_{t+1} & = k_{t} \pmb{\iota}(\q_{t})
\end{aligned}
```

where

```{math}
\begin{aligned}
\TaxComb_{t} & = \PostITC_{t}/\TaxFree_{t}
\end{aligned}
```

combines the effects of the corporate tax and the investment tax credit into a single tax term.

### Results

Figure {ref}`fig:PhaseDiag` presents two phase diagrams, one for {math}`k` and {math}`\vk` and one for {math}`k` and {math}`\q`.

For most purposes, {math}`\q` diagram is simpler, because our facts about the {math}`\iota` function imply that the {math}`\Delta k_{t+1} = 0` locus is always a horizontal line at {math}`\q = 1`. This is because {math}`\q=1` always corresponds to the circumstance in which the value of a unit of capital inside the firm, {math}`\vk`, matches the after-tax cost of a unit of capital, {math}`\kPriceAfterITC`; {math}`\q=1` is the only value of {math}`\q` at which the firm does not wish to change size ({math}`\Delta k_{t+1}=0`).

The slope of the {math}`\Ex_{t}[\Delta \q_{t+1}]` locus is easiest to think about near the steady state value of {math}`k` where we can approximate {math}`j^{k}_{t} \approx 0`.

Pick a point on the {math}`\Ex_{t}[\Delta \q_{t+1}]=0` locus. Now consider a value of {math}`\q` that is slightly larger. From {eq}`eq:qdyn`, at the initial value of {math}`k` we would have {math}`\Ex_{t} [\Delta \q_{t+1}] > 0`. Thus, the value of {math}`k` corresponding to {math}`\Ex_{t} [\Delta \q_{t+1}] = 0` must be one that balances the higher {math}`\q` by a higher value of {math}`\fFunc^{k}`, which is to say a lower value of {math}`k`. This means that higher {math}`\q` will be associated with lower {math}`k` so that the locus is downward-sloping.

For appropriate choices of parameter values the problem satisfies the usual conditions for stability and will therefore have a [saddle path](https://en.wikipedia.org/wiki/Saddle_point) solution, as depicted in the diagram.

The {math}`\vk` diagram is virtually indistinguishable from the {math}`\q` diagram; the only difference is that the {math}`\Delta k_{t+1}` locus is located at the point {math}`\vk = \kPriceAfterITC` (i.e. the marginal value of investment is equal to the price of a unit of investment). The distinction between the diagrams reflects the fact that an increase in the investment tax credit will result in a rise in the steady-state value of {math}`k` which implies a fall in the pretax marginal product of capital.

:::{note} Corporate Tax and Steady-State Capital
Notice the interesting and important result that a change in the corporate tax rate {math}`\TaxFree` does *not* affect the steady-state marginal product of capital because it does not change the price of investment: That is, at the steady-state where {math}`j^{k}=0`, neglecting depreciation {eq}`eq:lambdadyn` implies that {math}`\Ex_{t}[\Delta \vk_{t+1}]=0` requires

```{math}
\begin{aligned}
\rfree \vk & = \TaxFree \fFunc^{k}(\check{k})
\end{aligned}
```

but since a change in {math}`\TaxFree` does not change {math}`\kPriceAfterITC` it must change the equilibrium {math}`\vk` one-for-one. Thus,

```{math}
\begin{aligned}
\check{\vk} & = (\TaxFree/\rfree) \fFunc^{k}(\check{k})
\end{aligned}
```

and an increase in {math}`\TaxFree` has no effect on {math}`\fFunc^{k}(\check{k})` and therefore no effect on {math}`\check{k}`.
:::

:::{figure} /sources/investment/EntrepreneurPF/LaTeX/Figures/lPhaseDiag.png
:name: fig:qMod-lPhaseDiag

Phase Diagram for {math}`\vk`
:::

:::{figure} /sources/investment/EntrepreneurPF/LaTeX/Figures/qPhaseDiag.png
:name: fig:PhaseDiag

Phase Diagram for {math}`\q`
:::

(Dynamics)=
## Dynamics

(Steady-State)=
### Steady State

The key to understanding the model's dynamics (as, really, with all infinite horizon models) is to figure out the steady state toward which it is heading, then to work out how it gets there. The key to the steady state, in turn, is that the capital stock will eventually reach a point where {math}`\adj^{k}=\adj^{i}=0`.

(PtyShk)=
### A Positive Shock to Productivity

Suppose that the production function for the firm suddenly, permanently, and unexpectedly improves; specifically, leading up to period {math}`t` the firm was in steady state, but in periods {math}`t+1` and beyond the production function will be {math}`\fFunc_{\geq}(k)=\Psi \fFunc_{<}(k)` for some {math}`\Psi>1` where {math}`\fFunc_{<}` and {math}`\fFunc_{\geq}` indicate the production functions before and after the increase in productivity.

Note first that none of the tax terms has changed, and in the long run there is nothing to prevent the firm from adjusting its capital stock to the point consistent with the new level of productivity and then leaving it fixed there so that {math}`\adj^{k}=\adj^{i}=0`. Thus {eq}`eq:qdyn` implies that at the new steady state {math}`\check{k}_{\geq}` we will have {math}`\rfree \check{\q} = \TaxCombInv \fFunc_{\geq}^{k}(\check{k}_{\geq}) = \Psi \TaxCombInv \fFunc_{<}^{k}(\check{k}_{\geq})` which implies {math}`\check{k}_{\geq} > \check{k}_{<}`, since the steady state value of {math}`\q` never changes: {math}`\check{\q}_{\geq} = \check{\q}_{<} = 1`. That is, with higher productivity, the equilibrium capital stock is larger, but the equilibrium *tax adjusted marginal product* of capital is the same.

Obviously in order to get from an initial capital stock of {math}`\check{k}_{<}` to a larger equilibrium capital stock of {math}`\check{k}_{\geq}` the firm will need to engage in investment in excess of the depreciation rate, incurring costs of adjustment. In the absence of a change in the environment, *expected* costs of adjustment will always be declining toward zero, because the firm's capital stock will always be moving toward its equilibrium value in which those costs are zero.

So we can tell the story as follows. Suppose that leading up to period {math}`t` the firm was in its steady-state. When the productivity shock occurs, {math}`\fFunc^{k}` jumps up. {math}`j_{t}^{k}` had been zero (because the firm was at steady state), but now the firm wishes it had more capital because extra capital would reduce future adjustment costs (the firm knows that its old steady-state capital stock is now too small, so it will have to be engaging in {math}`\iota > 0` for a while), so {math}`j_{t}^{k}` becomes negative (that is, the firm knows that having more capital will reduce the adjustment costs associated with the higher investment that it will be undertaking). The combination {math}`\TaxCombInv \fFunc^{k}_{t} - j^{k}_{t} \Discount` therefore becomes a larger positive number, so at the initial level of {math}`\q` the RHS of {eq}`eq:qdyn` would imply {math}`\Ex_{t}[\Delta \q_{t+1}]` less than zero, so the new {math}`\Ex_{t}[\Delta \q_{t+1}]=0` locus must be higher (because the equilibrating value of {math}`\q` is higher for any {math}`k`). The saddle path is therefore also higher. So {math}`\q`, and therefore {math}`\iota`, jump up instantly when the new higher level of productivity is revealed, corresponding also to an immediate increase in the firm's share price (the marginal valuation of an additional unit of capital), since {math}`\TaxComb` has not changed.

The phase diagrams with the saddle paths before and after the productivity increase together with the impulse response functions would be plotted here.

<!-- Figure placeholder: ProductivityIncrease.png - to be generated from notebook -->

(Permanent-Tax-Cut)=
### A Permanent Tax Cut

Again starting from the steady state equilibrium, suppose {math}`\TaxComb` unexpectedly and permanently decreases, which could happen because of a cut in corporate taxes or an increase in the ITC. Equation {eq}`eq:qdyn` implies that in steady state

```{math}
\begin{aligned}
\rfree \overbrace{\check{\q}}^{=1} & = \fFunc^{k}/\TaxComb \\
\fFunc^{k} & = \rfree \TaxComb.
\end{aligned}
```

Dynamically, the story is as follows. Equation {eq}`eq:qdyn` implies that following the tax change the {math}`\Ex_{t}[\Delta \q_{t+1}] = 0` locus must be higher because at any given {math}`\q` the {math}`- \fFunc^{k}/\TaxComb` term is a larger negative number, while at the initial {math}`k` the {math}`j^{k}_{t}` term is also now negative; so the {math}`\Ex_{t}[\Delta \q_{t+1}]=0` locus shifts up.

In contrast to the case with a productivity shock, the equilibrium marginal product of capital will be lower than before. Arbitrage equalizes the *after-tax* marginal product of capital with the interest rate, but with a lower tax rate, that equilibration will occur at a higher level of capital.

Notice that the qualitative story is the same whether the change in {math}`\TaxComb` is due to a permanent reduction in the corporate tax rate (increase in {math}`\TaxFree`) or a permanent increase in the investment tax credit (reduction in {math}`\PostITC`). In either case, {math}`\q` and investment jump upward at time {math}`t` and then gradually decline back downward (though the equilibrium level of investment is higher than before the change).

:::{margin}
Read this carefully and work out the diagrams before lecture.
:::

There is, however, one interesting distinction between a decrease in {math}`\TaxComb` due to a reduction in corporate taxes and a decrease caused by an increase in {math}`\itc`. Since {math}`\vk=\PostITC\q`, an increase in {math}`\itc` reduces {math}`\PostITC` and therefore reduces the equilibrium value of {math}`\vk`, while a change in {math}`\TaxFree` has no effect on equilibrium {math}`\vk`. This reflects a subtle distinction. {math}`\vk` is the after-tax marginal value of extra capital, and the equilibrium in this model will occur at the point where that marginal value is equal to the marginal cost. Changing {math}`\itc` changes that marginal cost, so it changes the equilibrium after-tax marginal value. Changing {math}`\TaxFree` does not change the marginal cost of capital, so the equilibrium *after-tax* marginal value of capital is unchanged. The marginal *product* of capital is lower after a tax cut (equilibrium {math}`\fFunc^{k}` is smaller), but that is exactly counterbalanced by the larger value of {math}`\TaxFree` so that {math}`\TaxFree\fFunc^{k}` is unchanged in the long run by the change in {math}`\TaxFree`.

The phase diagrams with the saddle paths before and after the corporate tax reduction and the ITC increase, together with the impulse response functions, would be plotted here. Note that the {math}`\vk` saddle path actually jumps *downward* after the ITC increase. This is not an error; rather, recall that {math}`\vk` reflects marginal value of a unit of capital inside the firm, and recall that the *price* of purchasing that capital has gone down. Remembering that we are assuming that capital can move in and out of the firm, this has the surprising consequence that, for the original owners of the firm, the ITC is *bad* news because it means that the capital they own has a lower value (its value is ultimately tied to the price of capital, which has gone down). For a potential new shareholder, the investment tax credit means that you can obtain ownership of a share of the firm's capital by buying the capital at the ITC-discounted price, paying the adjustment costs, then giving the capital to the firm. Thus, the ITC has the effect of increasing the absolute value of a dollar of money relative to the value of a unit of capital inside the firm. So in this special case, you should think of the ITC as something that provides a discount to purchasing shares or capital {math}`\vk`. While the new saddle path for {math}`\vk` is lower than the old one, that does not reflect the adjustment for the fact that the new capital is being purchased at a cheaper price. The dynamics of {math}`\q`, in this case, are more intuitive than those of {math}`\vk`: {math}`\q` unambiguously increases, reflecting the fact that the value of capital to the firm exceeds its new (cheaper) cost.

In sum: In terms of effects on capital, the outcome from a corporate tax cut and an ITC tax cut are similar, but the analytics of {math}`\vk` are different, because the former affects the after-tax interest rate while the latter affects the after-tax cost of capital.

<!-- Figure placeholder: CorporateTaxReduction.png - to be generated from notebook -->

<!-- Figure placeholder: ITCIncrease.png - to be generated from notebook -->

(Future-Shock-To-Productivity)=
### A Future Shock to Productivity

Now consider a circumstance where the firm knows that at some date in the future, {math}`t+n`, the level of productivity will increase so that {math}`\fFunc_{\geq t+n} = \Psi \fFunc_{< t+n}` for {math}`\Psi>1`.

The long run steady state is of course the same as in the example where the increase in productivity is immediately effective.

To determine the short run dynamics, notice several things. First, there can be no *anticipated* big jumps in the share price of the firm (the marginal productivity of capital inside the firm). Thus, if the productivity jump occurs in period {math}`t+n` and the time periods are short enough, we must have

```{math}
\begin{aligned}
\Ex_{t+n-1}[\vk_{t+n}-\vk_{t+n-1}] & \approx 0.
\end{aligned}
```

But because the equilibrium capital stock is larger, we know that {math}`{j}^{k}_{\geq t+n}<0` and will stay negative thereafter (asymptoting to zero from below). This reflects the fact that if you know you will need higher capital in the future, the most efficient way to minimize the cost of obtaining that capital is to gradually start building some of it even before you need it, rather than trying to do it all at once. Note further that before period {math}`t+n` the model behaves according to the equations of motion defined by the problem under the {math}`{<}` parameter values,[^jk-path-note] while at {math}`t+n` and after it behaves according to the new {math}`\geq` equations of motion.

[^jk-path-note]: Strictly speaking, this is not true, because {math}`j_{t}^{k}` will now differ from the value associated with the initial problem. For purposes of analyzing problems of this kind (announced future changes in parameters) we will neglect the effects of the path of {math}`j_{t}^{k}` on the equations of motion. Except under extreme circumstances, this should not change the qualitative results of the analysis, and doing anything else would require a very intricate analysis. This treatment is admittedly a bit inconsistent, since in the case under consideration it is precisely the change in {math}`j_{t}^{k}` that motivates the firm to start adjusting its capital stock before the productivity change comes into effect; effectively, we are taking into account the effect of {math}`j_{t}^{k}` on the level of {math}`\vk` before period {math}`t+n` while neglecting its effects on {math}`\vk`'s dynamics during this interval. C'est la vie.

Putting all this together, the story is as follows. Upon announcement of the productivity increase, {math}`\vk` jumps to the level such that, evolving exactly according to its {math}`{<}` equations of motion, it will arrive in period {math}`t+n` at a point exactly on the saddle path of the model corresponding to the {math}`{\geq}` equations of motion. Thereafter it will evolve toward the steady state, which will be at a higher level of capital than before, {math}`\check{k}_{\geq} > \check{k}_{<}`, because the greater productivity justifies a higher equilibrium capital stock.

Thus, {math}`\vk` jumps up at time {math}`t`, evolves to the northeast until time {math}`t+n`, and thereafter asymptotes downward toward the same equilibrium value it had originally before the productivity change. Since {math}`\TaxComb` has not changed, the dynamics of {math}`\q` and {math}`\iota` are the same as those of {math}`\vk`.

(Future-Increase-In-ITC)=
### A Future Increase in the ITC

Consider now the consequences if a surprise increase in the investment tax credit is passed at date {math}`t` that will become effective at date {math}`t+n>t`.

Inspection of {eq}`eq:qdyn` might suggest that the effects of a future tax cut would be identical to the effects of a future increase in {math}`\fFunc^{k}`, since the terms enter multiplicatively via {math}`\TaxCombInv \fFunc^{k}`. And indeed, with respect to the dynamics of {math}`\vk` the two experiments are basically the same. And of course the steady-state value of {math}`\q` is always equal to one.

During the transition, however, {math}`\q` has interesting dynamics. From periods {math}`t` to {math}`t+n-1`, the ITC does not change, leaving {math}`\TaxCombInv` and the after-tax marginal product of capital unchanged, and so the dynamics of {math}`\q` are basically the same as those of {math}`\vk.` But between {math}`t+n-1` and {math}`t+n`, {math}`\vk` cannot jump but {math}`\TaxCombInv` does jump, which implies that {math}`\q` must jump (so there is a predictable change in {math}`\q`).

Dynamics of investment are determined by dynamics of {math}`\q`, so the path of {math}`\iota` is: At {math}`t`, a discrete jump up; between {math}`t` and {math}`t+n-1`, a gently rising path; between {math}`t+n-1` and {math}`t+n`, an upward jump; and after {math}`t+n`, a path that asymptotes downward toward the steady state level of investment.

The steady-state effects on {math}`\vk` are of course determined by the same considerations as apply to the unanticipated tax cut, so they depend on whether the tax change is a drop in {math}`\TaxCorp` or an increase in {math}`\itc`.

## More Figures

Figures for a variety of other experiments have been constructed using the [notebook](https://github.com/econ-ark/DARKolo/blob/master/chimeras/qModel/qModel-Template-Section-Figures.ipynb). Such figures are contained in the "Figures" subdirectory.
