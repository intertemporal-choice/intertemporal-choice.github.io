(sec:qRamsey)=
# A q-Ramsey Model

<!-- \usepackage{endfloat}  % uncomment to put figures at the end -->
<!-- Definitions specific to this document -->

Consider a Ramsey economy in which the capital stock

cannot be freely adjusted; instead, as in the {math}`\q` model of investment,

capital is subject to quadratic costs of adjustment.

<!-- \provideboolean{DeprTF} -->
<!-- \setboolean{DeprTF}{true} % Whether or not to include the depreciation rate in the formulas etc -->
<!-- \setboolean{DeprTF}{false} -->
<!-- When DeprTF is true: "Defining the depreciation factor \DeprFac=(1-\depr) as the amount of capital left after one period of depreciation, the" -->
<!-- When DeprTF is false: "The" -->

The dynamic budget constraint is

```{math}
:label: eq:1perBC

\begin{gathered}\begin{aligned}
\digamma(\kap_{t}) & =  \kap_{t}+\kap_{t}^{\kapShare} \\
\aRat_{t} & =  \digamma(\kap_{t})-\cons_{t}-j_{t}\\
\kap_{t+1} & =  \aRat_{t}
\end{aligned}\end{gathered}
```

where for analytical simplicity we neglect capital depreciation (though the illustrative figures below show results of a model that properly includes depreciation) and the cost-of-adjustment function takes the form

```{math}
:label: eq:jDef

\begin{gathered}\begin{aligned}
  \jFunc(\inv,\kap) & =  (\kap/2)(\inv/\kap)^{2}\adjPar
\end{aligned}\end{gathered}
```

for some constant {math}`\adjPar`, so that the cost of adjustment incurred in period {math}`t`

is given by

```{math}
\begin{gathered}\begin{aligned}
  j_{t} & =  \jFunc(\overbrace{\aRat_{t}-\kap_{t}}^{\equiv \inv_{t}},\kap_{t}).
\end{aligned}\end{gathered}
```

A social planner is assumed to maximize the discounted sum of

utility from consumption {math}`\cons_{t}`, where the utility function is CRRA, {math}`\uFunc(\cons )=\cons^{1-\CRRA}/(1-\CRRA)`.

% \begin{enumerate}

The social planner's problem can be rewritten in the form of a Bellman equation,

```{math}
\begin{gathered}\begin{aligned}
\vFunc(\kap_t) &= %\max_{\{ \cons_{t+n} \}_{n=0}^\infty} \sum_{n=0}^\infty \Discount^{n} \uFunc(\cons_{t+n})\\
%&= \max_{\{ \cons_{t+n} \}_{n=0}^\infty} ~\Discount^0 \uFunc(\cons_t)+\beta \sum_{n=0}^\infty \Discount^{n} \uFunc(\cons_{t+1+n})\\
% &=
\max_{\cons_t} ~\uFunc(\cons_t)+\Discount \vFunc(\kap_{t+1})
\\ & \text{s.t.}  \notag
\\ \kap_{t+1} & =  \digamma_t-\cons_t-j_t.
\end{aligned}\end{gathered}
```

% \ifa{%\textit{Answer:}

Because (given {math}`\kRat_{t}`), choosing {math}`\aRat_t` is equivalent to choosing {math}`\cons_t`,[^ddyOSlXk7d]

[^ddyOSlXk7d]: Solving {eq}`eq:1perBC` for {math}`\cons_t` and substituting this expression in

    the place of {math}`\cons_t` in the Bellman equation, and then

    substituting {math}`\aRat_t` for {math}`\kap_{t+1}`. we can rewrite

the problem as:

```{math}
:label: eq:aEnd

\vFunc(\kap_{t})=\max_{\aRat_{t}}
~\uFunc(\digamma(\kap_{t})-\aRat_{t}-\jFunc(\aRat_{t}-\kap_{t},\kap_{t}))+\Discount
\vFunc(\aRat_{t}).
```

% \end{quotation}

The first order condition is found by setting the derivative w.r.t. {math}`\aRat_t` to zero:

```{math}
:label: eq:genFOC

\begin{gathered}\begin{aligned}
(1+j^i_t)\uFunc^{\prime}(\cons_t) &= \Discount \vFunc^{\kap}(\underbrace{\aRat_t}_{=\kap_{t+1}}). %\\

%&= \Discount \vFunc^{\kap}(\kap_{t+1})
\end{aligned}\end{gathered}
```

The envelope theorem tells us that the marginal value of capital does not depend on its effect on the investment policy function {math}`\aFunc(\kap)`:

```{math}
:label: eq:genEnv

\begin{gathered}\begin{aligned}

 \vFunc^{\kap}(\kap_t) &= (\digamma^{\prime}(\kap_t)+\jFunc^i(\aRat_t-\kap_t,\kap_t)-\jFunc^k(\aRat_t-\kap_t,\kap_t))\uFunc^{\prime}(\cons_t)\\
 & \equiv \lambda_t,
\end{aligned}\end{gathered}
```

(where notice that {math}`\lambda_{t}` does  not have the simple interpretation of a share price as in [](#sec:qModel) because here it involves {math}`\uFunc^{\prime}(\cRat_{t})`).

Substituting period {math}`t+1`'s version of {eq}`eq:genEnv` into {eq}`eq:genFOC` allows us to rewrite the Euler equation in the form:

```{math}
:label: eq:Euler

\begin{gathered}\begin{aligned}
\uFunc^{\prime}(\cons_{t})(1+j^{i}_{t})
& =  \Discount (\digamma^{\prime}(\kap_{t+1})+j^{i}_{t+1}-j^{\kap }_{t+1})\uFunc^{\prime}(\cons_{t+1})\\
\uFunc^{\prime}(\cons_{t})
& =  \Discount \underbrace{(\digamma^{\prime}(\kap_{t+1})+j^{i}_{t+1}-j^{\kap }_{t+1})/(1+j^{i}_{t})}_{\Rfree_{t+1}}\uFunc^{\prime}(\cons_{t+1}).
\end{aligned}\end{gathered}
```

% \ifa{

% \textit{Answer:}

% }{\vspace{2in}}

This economy reduces to a standard Ramsey model when the cost of

adjustment parameter is set to {math}`\adjPar=0`, because all the {math}`\adj`

terms disappear so that the interest factor becomes the usual

{math}`\Rfree_{t+1}=\digamma^{\prime}(\kap_{t+1}) = 1 +
\fFunc^{\prime}(\kap_{t+1})`. The presence of adjustment costs does

not change the steady state of the model (because in steady state,

adjustment costs are zero), but reduces the speed of convergence

toward that steady state. This can be seen by considering the policy

functions plotted in {numref}`fig:PolFuncAdjCost0VsBase`, where the

solid lines reflect the solution to a model with {math}`\adjPar=0` (the

standard Ramsey model) while the dashed lines reflect a model with a

high cost of adjustment (the '{math}`q`-Ramsey' model).

The differences between the solid and the dashed loci indicate that a

faster rate of convergence to the steady state requires a high level

of {math}`\iRat` below the steady state at which {math}`\kap=\Target{\kap}` and

low level of {math}`\iRat` when {math}`\kap` is above {math}`\Target{\kap}`. Higher

adjustment costs work against fast convergence, since, when {math}`\kap` is

below the steady state (and positive investment is needed to increase

{math}`\kap` toward {math}`\Target{\kap}`, adjustment costs reduce investment,

while they increase investment (making it less negative) when {math}`\kap`

is above the equilibrium. In both cases, the difference occurs because

because adjusting capital involves convex costs, and thus it is

optimal to proceed slowly in moving the capital stock to minimize

those costs. Interestingly, even though the optimal choices of

investment and consumption change quite substantially in the model

with a larger adjustment cost parameter, the actual size of costs of

adjustment borne is quite modest (the dashing line for {math}`j_{t}` is

barely distinguishable from the horizontal axis except very far from

the steady state). This tells us that even if the observed costs paid

are not very large, those costs can have a large effect in

changing behavior away from the frictionless optimum.

:::{figure} /sources/growth/qRamsey/LaTeX/Figures/PolFuncAdjCost0VsBase.png
:name: fig:PolFuncAdjCost0VsBase
:align: center

Solid Loci: Standard Ramsey Model; Dashed: With Costs of Adjustment
:::

Increasing the desired degree of consumption smoothing, captured by

the coefficient of relative risk aversion {math}`\CRRA`, leads to similar

implications. {numref}`fig:PolFuncRRALoVsHi` shows that a higher

{math}`\CRRA` (the dashed loci), implies again lower

investment below the steady state and higher above it. This is now

caused by a low intertemporal elasticity of substitution: if the

economy falls below steady state, a larger {math}`\CRRA` implies that the

representative agent is less willing to cut consumption in order to

boost investment and quickly return to the steady state. Similarly,

the increase in consumption above the steady state is more moderate,

thus leading to a smaller reduction in investment and a more gradual

return to equilibrium.

:::{figure} /sources/growth/qRamsey/LaTeX/Figures/PolFuncRRALoVsHi.png
:name: fig:PolFuncRRALoVsHi
:align: center

Higher {math}`\CRRA` (Dashed Loci) Has a Similar Effect to Adjustment Costs
:::

By comparing the policy functions, we have thus seen that either an

intensified consumption smoothing motive (higher {math}`\CRRA`) and or a stronger investment

smoothing motive (higher {math}`\adjPar`) have similar implications: they

restrain sharp adjustments to consumption and investment, thus slowing

down the speed of convergence to the steady state.

We now consider the responses of the model to several shocks, starting

from steady state. {numref}`fig:kDropCostAdj0VsBase` shows the

economy's dynamics following the destruction of part of the capital

stock. In the standard Ramsey {math}`\adjPar=0` model (black), this leads to

an increase in the marginal productivity of capital which boosts

investment. In the {math}`\adjPar>0` model with adjustment costs (red), the

level of investment actually falls. This is because costs of

adjustment are assumed to be  relative to the size of the capital

stock, and with a shrunken capital stock the original level of

investment would incur very large costs of adjustment. Investment

therefore drops to a level that is large relative to the (shrunken)

capital stock but nevertheless smaller than its initial level. Even this lower

investment level, though, is large relative to the new lower level of the

capital stock, and so the capital stock rises back toward the original

equilibrium – just more slowly than in the frictionless model.

Consumption drops due to the negative wealth effect and

the need to finance investment. But since investment is lower initially in

the model with investment costs, consumption can be higher initially (the first

red consumption dot is above the first black one, post-shock).

:::{figure} /sources/growth/qRamsey/LaTeX/Figures/kDropCostAdj0VsBase.png
:name: fig:kDropCostAdj0VsBase
:align: center

Impulse response functions to 50% destruction of the capital stock

{math}`\adjPar=0` (standard Ramsey) in black; {math}`\adjPar > 0` ({math}`q`-Ramsey) in red
:::

{numref}`fig:PatRiseCostAdj0VsBase` shows the dynamics triggered by an

increase in patience, captured by a permanent rise in

{math}`\Discount`. The most striking difference is in the interest factor {math}`\Rfree`.

In the Ramsey model with no investment costs, the interest rate is simply

the marginal product of capital. Here, it must also take account of costs

of adjustment. Since costs of adjustment are high when the economy is

trying to change the size of the capital stock, the interest rate is lower.

This result is interesting because one problem with using the Ramsey model

for studying business cycle dynamics is that the aggregate capital stock

barely moves at all over such a short time period as a business cycle,

so the non-{math}`q` Ramsey model has no hope of matching empirical interest rate fluctuations.

Adding costs of adjustment allows much bigger movements in {math}`\Rfree` and

thus gives the model a fighting chance.

Given the lower interest rate (and its implications through the

consumption Euler equation), the growth rate of consumption after the

increase in patience will be less than in the standard Ramsey model.

Even though consumption drops less, {math}`\lambda_{t}` rises more. Recall

that {math}`\lambda_{t}` is a composition of the marginal utility of

consumption and the "share price" of ownership of a unit of capital.

The extra rise in {math}`\lambda` reflects the fact that the existing

capital is more valuable in a period when the rate of investment will

be high (going forward), so the market value of a unit of

"installed" capital rises to above the purchase price of a unit of

capital (which is always 1). This can be interpreted as a boom in

asset prices.

:::{figure} /sources/growth/qRamsey/LaTeX/Figures/PatRiseCostAdj0VsBase.png
:name: fig:PatRiseCostAdj0VsBase
:align: center

Impulse responses to an increase in patience (higher {math}`\Discount`)

Black: Ramsey; Red: {math}`q`-Ramsey
:::

<!-- The following section appears only when DeprTF is true (depreciation included in formulas) -->
<!-- Since DeprTF is set to false, this section is conditional content -->

Finally, we consider in {numref}`fig:DeprRiseCostAdj0VsBase`

the responses to an increase in the

depreciation rate. This reduces the marginal product of capital and

consequently the desired level of capital. In the Ramsey model,

investment contracts, freeing resources for consumption which

temporarily increases. The economy converges to an equilibrium with

lower capital (at which the marginal productivity returns to its

initial level), lower consumption and investment. In the model with

adjustment costs, consumption initially contracts because investment

actually rises (since the cost of adjustment is defined as

*relative to* the amount of depreciation, which has suddenly

increased). Because investment increases initially, consumption

falls a bit. As always, however, the economy with costs of

adjustment eventually asymptotes to the same equilibrium as the

frictionless economy.

:::{figure} /sources/growth/qRamsey/LaTeX/Figures/DeprRiseCostAdj0VsBase.png
:name: fig:DeprRiseCostAdj0VsBase
:align: center

Impulse response functions to an increase in depreciation (higher {math}`\delta`)
:::

% \end{enumerate}

