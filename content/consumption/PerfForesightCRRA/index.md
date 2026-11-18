(sec:PerfForesightCRRA)=
# Consumption Under Perfect Foresight and CRRA Utility

The perfect foresight model with constant relative risk aversion is the benchmark for the models of consumption that follow. It has a closed-form solution, so every question about it has an exact answer: how much the consumer spends out of wealth, whether spending rises or falls over time, and how both respond to the interest rate. Three conditions organize the answers. The return impatience condition makes the marginal propensity to consume positive, the finite human wealth condition makes the present value of future income finite, and the growth impatience condition decides whether a consumer with no assets wants to borrow, and where the consumer ends up. The chapter derives the solution and the conditions, and then applies the model to two questions about interest rates: how much consumption responds through the value of future income, and how the saving rate responds. Its answers are large, larger than the evidence supports, and the reasons they are too large motivate the models of uncertainty and liquidity constraints that come later.

Two companion notebooks in the Econ-ARK DemARK collection work this model numerically.
[How Close Is HARK's Infinite-Horizon Solution?](https://econ-ark.github.io/DemARK/perfforesightcrra-convergence/)
measures how a numerical solution, found by iterating backward from the last period of life, approaches the exact formulas derived here.
[Perfect Foresight CRRA Model - Saving Rate](https://econ-ark.github.io/DemARK/perfforesightcrra-savingrate/)
uses HARK to compute the consumer's saving rate.

## The Problem

This section solves the problem of a perfect foresight consumer with intertemporally separable CRRA utility {math}`\uFunc(\bullet)= \bullet^{1-\CRRA}/(1-\CRRA)` who discounts future utility geometrically by a factor {math}`\DiscFac` per period. The finite horizon solution, whose last period is {math}`\TEnd`, extends to the infinite horizon case if intuitive "impatience" and "finite human wealth" conditions hold.

The consumer's problem in period {math}`t` is to

```{math}
:label: eq:PFCRRA-maxprob

\max \sum_{n=0}^{\TEnd-\tNow} \DiscFac^{n} \uFunc(\cLevBF_{\tNow+n})
```

subject to the constraints below, in which we introduce {math}`\bLevBF` and {math}`\mLevBF` because it is useful to have a term for the consumer's non-income resources at the beginning of the period,

```{math}
\begin{aligned}
      \aLevBF_{\tNow}   & =  \mLevBF_{\tNow}-\cLevBF_{\tNow}
\\    \bLevBF_{\tNow+1} & =  \aLevBF_{\tNow}\Rfree
\\    \mLevBF_{\tNow+1} & =  \bLevBF_{\tNow+1}+\pLevBF_{\tNow+1}
\end{aligned}
```

where {math}`\pLevBF_{\tNow+1}` is "permanent labor income," which always grows by a factor {math}`\PermGroFac`:

```{math}
\pLevBF_{\tNow+1}/\pLevBF_{\tNow} = {\PermGroFac}.
```

Here {math}`\Rfree = 1+\rfree` is the interest factor and {math}`\PermGroFac = 1+\PermGroRte` the growth factor of permanent income.

The consumer can borrow or lend any amount at the interest factor {math}`\Rfree`, against future income as well as current resources, but cannot die in debt: {math}`\aLevBF_{\TEnd} \geq 0`. Since nothing is gained by leaving resources unspent, this constraint binds, {math}`\aLevBF_{\TEnd} = 0`. In the infinite-horizon case it becomes the no-Ponzi condition {math}`\lim_{n \rightarrow \infty} \Rfree^{-n}\aLevBF_{\tNow+n} \geq 0`, which binds for the same reason. Throughout, {math}`\CRRA \neq 1`; logarithmic utility is the limit as {math}`\CRRA \rightarrow 1`.

## The Solution

It will be convenient to think of both market resources {math}`\mLevBF_{\tNow}` and permanent noncapital (labor) income {math}`\pLevBF_{\tNow}` as state variables in this problem. Bellman's equation is

:::{margin}
Bellman's equation relates {math}`\vFunc_{\tNow}` and {math}`\vFunc_{\tNow+1}` through the controls and the states, so it does not necessarily require writing out the budget constraint.
:::

```{math}
:label: eq:PFCRRA-vmax

\vFunc_{\tNow}(\mLevBF_{\tNow},\pLevBF_{\tNow}) = \max_{\cLevBF_{\tNow}} \left\{ \uFunc(\cLevBF_{\tNow}) + \DiscFac \vFunc_{\tNow+1}\left(\overbrace{(\mLevBF_{\tNow}-\cLevBF_{\tNow})\Rfree+\pLevBF_{\tNow+1}}^{=\mLevBF_{\tNow+1}},\pLevBF_{\tNow+1}\right)\right\}.
```

The first order condition for this maximization is

```{math}
:label: eq:upeqrbv

\uFunc^{\prime}(\cLevBF_{\tNow}) = \DiscFac \left(\Rfree \vFunc_{\tNow+1}^{\mLevBF}(\mLevBF_{\tNow+1},\pLevBF_{\tNow+1})-\overbrace{\frac{d\pLevBF_{\tNow+1}}{d \cLevBF_{\tNow}}}^{=0}\vFunc_{\tNow+1}^{\pLevBF}(\mLevBF_{\tNow+1},\pLevBF_{\tNow+1})\right),
```

and the [Envelope theorem](#sec:Envelope) tells us that

```{math}
:label: eq:vpeqrbv

\vFunc_{\tNow}^{\mLevBF}(\mLevBF_{\tNow},\pLevBF_{\tNow}) = \Rfree \DiscFac \vFunc_{\tNow+1}^{\mLevBF}(\mLevBF_{\tNow+1},\pLevBF_{\tNow+1}).
```

But the right hand sides of {eq}`eq:upeqrbv` and {eq}`eq:vpeqrbv` are identical, so

```{math}
\vFunc_{\tNow}^{\mLevBF}(\mLevBF_{\tNow},\pLevBF_{\tNow}) = \uFunc^{\prime}(\cLevBF_{\tNow})
```

and similar logic tells us that {math}`\vFunc_{\tNow+1}^{\mLevBF}(\mLevBF_{\tNow+1},\pLevBF_{\tNow+1})=\uFunc^{\prime}(\cLevBF_{\tNow+1}),` which (substituting {math}`\uFunc^{\prime}` for {math}`\vFunc^{\mLevBF}` in {eq}`eq:vpeqrbv`) gives us the Euler equation for consumption:

```{math}
:label: eq:PFCRRA-cgrow

\begin{aligned}
        \uFunc^{\prime}(\cLevBF_{\tNow}) & =  \Rfree\DiscFac \uFunc^{\prime}(\cLevBF_{\tNow+1}) \\
        1 & =  \Rfree\DiscFac \left(\frac{\cLevBF_{\tNow+1}}{\cLevBF_{\tNow}}\right)^{-\CRRA}
\\  \left(\frac{\cLevBF_{\tNow+1}}{\cLevBF_{\tNow}}\right) & =  (\Rfree\DiscFac)^{1/\CRRA}.
\end{aligned}
```

Thus, consumption grows in every period by a factor {math}`\APFac \equiv (\Rfree\DiscFac)^{1/\CRRA}`, where we use the Old English letter {math}`\APFac` to measure what we will call the "absolute patience" factor. Specifically, if

```{math}
:label: eq:AIC

\APFac < 1
```

we will say that the consumer exhibits "absolute impatience" because this is the condition that guarantees that the level of consumption will be falling (and what better definition of absolute impatience could there be than deliberately spending so much that you will have to cut your spending in the future?). If {math}`\APFac > 1` the consumer exhibits "absolute patience" (the consumer wants to defer resources into the future in order to achieve consumption growth).

Combining the constraints from period {math}`\tNow` to period {math}`\TEnd` and imposing {math}`\aLevBF_{\TEnd}=0`, the Intertemporal Budget Constraint tells us that the present discounted value of consumption must match the PDV of total resources:

```{math}
:label: eq:PFCRRA-ibc

\PDV_{\tNow}^{\TEnd}(\cLevBF) = \bLevBF_{\tNow}+\PDV_{\tNow}^{\TEnd}(\pLevBF).
```

Fact [FinSum](#fact:finsum) can be used to show that the PDV of labor income (also called "human wealth" {math}`\hLevBF_{\tNow}`) is

```{math}
:label: eq:PFCRRA-yfin

\begin{aligned}
        \hLevBF_{\tNow} = \PDV_{\tNow}^{\TEnd}(\pLevBF) & =  \sum_{n=0}^{\TEnd-\tNow} \Rfree^{-n}\pLevBF_{\tNow+n}
\\       & =  \pLevBF_{\tNow}\sum_{n=0}^{\TEnd-\tNow} \Rfree^{-n}{\PermGroFac}^{n} = \pLevBF_{\tNow}\sum_{n=0}^{\TEnd-\tNow} ({\PermGroFac}/\Rfree)^{n}
\\   & =  \pLevBF_{\tNow}\left(\frac{1-({\PermGroFac}/\Rfree)^{\TEnd-\tNow+1}}{1-({\PermGroFac}/\Rfree)}\right)
\end{aligned}
```

while the PDV of consumption is

```{math}
:label: eq:cfin

\begin{aligned}
        \PDV_{\tNow}^{\TEnd}(\cLevBF) & =  \sum_{n=0}^{\TEnd-\tNow} \Rfree^{-n}\cLevBF_{\tNow+n}
\\       & =  \sum_{n=0}^{\TEnd-\tNow} \Rfree^{-n}\cLevBF_{\tNow}((\Rfree\DiscFac)^{1/\CRRA})^{n}
\\       & =  \cLevBF_{\tNow} \sum_{n=0}^{\TEnd-\tNow} [\Rfree^{-1}(\Rfree\DiscFac)^{1/\CRRA}]^{n}
\\   & =  \cLevBF_{\tNow}\left(\frac{1-[\Rfree^{-1}(\Rfree\DiscFac)^{1/\CRRA}]^{\TEnd-\tNow+1}}{1-[\Rfree^{-1}(\Rfree\DiscFac)^{1/\CRRA}]}\right).
\end{aligned}
```

(cFuncAnalytical)=
We can solve the model by combining {eq}`eq:cfin` and {eq}`eq:PFCRRA-yfin` using {eq}`eq:PFCRRA-ibc` to obtain:

```{math}
:label: eq:PFCRRA-cfinhoriz

\cLevBF_{\tNow} = \underbrace{\left(\frac{1-[\Rfree^{-1}(\Rfree\DiscFac)^{1/\CRRA}]}{1-[\Rfree^{-1}(\Rfree\DiscFac)^{1/\CRRA}]^{\TEnd-\tNow+1}}\right)}_{\equiv \MPC_{t}} \underbrace{\left[\bLevBF_{\tNow}+\pLevBF_{\tNow}\overbrace{\left(\frac{1-({\PermGroFac}/\Rfree)^{\TEnd-\tNow+1}}{1-({\PermGroFac}/\Rfree)}\right)}^{\equiv \hNrm_{t}}\right]}_{\equiv \oLev_{t}}
```

where {math}`\MPC_{t}` is the marginal propensity to consume (MPC) out of **o**verall (human plus nonhuman) wealth {math}`\oLev_{t}`.

Human wealth as defined in [the PDV of labor income](#eq:PFCRRA-yfin) includes the current period's income: its sum starts at {math}`n=0`. Human wealth from the next period on, called end-of-period human wealth {math}`\hNrmEnd_{t}` and measured as a ratio to {math}`\pLevBF_{\tNow}`, leaves that income out:

```{math}
:label: eq:PFCRRA-hEnd

\hNrmEnd_{t} \equiv \hNrm_{t}-1 = \sum_{n=1}^{\TEnd-\tNow} ({\PermGroFac}/\Rfree)^{n} = ({\PermGroFac}/\Rfree)\left(\frac{1-({\PermGroFac}/\Rfree)^{\TEnd-\tNow}}{1-({\PermGroFac}/\Rfree)}\right),
```

which approaches {math}`({\PermGroFac}/\Rfree)/(1-{\PermGroFac}/\Rfree)` as {math}`\TEnd \rightarrow \infty` when the [finite human wealth condition](#eq:FHWCPF) below holds.

:::{margin}
The closed forms divide by zero in two cases, and the sums they come from give the answer. If {math}`(\Rfree\DiscFac)^{1/\CRRA}=\Rfree`, every term of the sum in [the PDV of consumption](#eq:cfin) is 1, so {math}`\MPC_{t}=1/(\TEnd-\tNow+1)`. If {math}`\PermGroFac=\Rfree`, every term of the human wealth sum is 1, so {math}`\hNrm_{t}=\TEnd-\tNow+1` and {math}`\hNrmEnd_{t}=\TEnd-\tNow`.
:::

In order to apply [InfSum](#fact:infsum) to move to the infinite-horizon case ({math}`\TEnd=\infty`), we need to impose the condition

```{math}
:label: eq:FHWCPF

\begin{aligned}
        {\PermGroFac}/\Rfree & <  1
\\  {\PermGroFac}   & <  \Rfree.
\end{aligned}
```

Why? Because if income were expected to grow at a rate greater than the interest rate forever, then the PDV of future income would be infinite; with infinite human wealth, the problem has no well-defined solution. We henceforth call {eq}`eq:FHWCPF` the Finite Human Wealth Condition (FHWC).

:::{margin}
[InfSum](#fact:infsum) is the immediate implication of [FinSum](#fact:finsum) as {math}`\TEnd \rightarrow \infty`.
:::

Similarly, if consumption starts at a positive level and grows by the factor {math}`\APFac=(\Rfree \DiscFac)^{1/\CRRA}`, in order for the PDV of consumption to be finite we must impose:

```{math}
:label: eq:PatR

\underbrace{\left(\frac{(\Rfree\DiscFac)^{1/\CRRA}}{\Rfree}\right)}_{\RPFac} < 1
```

and we will henceforth call {math}`\RPFac` the "return patience factor" whose log is the "return patience rate" {math}`\patr \equiv \log \RPFac` ({math}`\pat` is the lower-case version of {math}`\APFac`) and what {eq}`eq:PatR` says is that the desired growth rate of consumption must be less than the interest rate in order for the model to have a well-defined solution. This condition therefore imposes a requirement that "impatience" be greater than some minimum amount. (For (much) more on the various definitions of impatience used in this section, their implications, and parallel conditions for models with uncertainty, see {cite:t}`BufferStockTheory`).

We call {eq}`eq:PatR` the "return impatience condition" (RIC).

If both the RIC and the FHWC hold, then the model has a well-defined infinite horizon solution, as can be seen by realizing that

:::{margin}
The [appendix](#sec:PerfForesightCRRA-Appendix) derives [the limiting solution when they do not](#sec:PFwhenFHWfails); see {cite:t}`BufferStockTheory` for a fuller discussion.
:::

```{math}
\begin{aligned}
   \lim_{\TEnd \rightarrow \infty} ({\PermGroFac}/\Rfree)^{\TEnd-\tNow+1} & =  0
\\ \lim_{\TEnd \rightarrow \infty} (\Rfree^{-1}(\Rfree\DiscFac)^{1/\CRRA})^{\TEnd-\tNow+1} & = 0.
\end{aligned}
```

Substituting these zeros into {eq}`eq:PFCRRA-cfinhoriz` yields

```{math}
:label: eq:PFCRRA-cOfw

\begin{aligned}
        \cLevBF_{\tNow} & =  \left(1-\Rfree^{-1}(\Rfree\DiscFac)^{1/\CRRA}\right)\left[\bLevBF_{\tNow}+\left(\frac{\pLevBF_{\tNow}}{1-({\PermGroFac}/\Rfree)}\right)\right]
\\      & =  \left(1-\Rfree^{-1}(\Rfree\DiscFac)^{1/\CRRA}\right)\left(\mLevBF_{\tNow}-\pLevBF_{\tNow}+\hLevBF_{\tNow}\right)
\\      & =  \underbrace{\left(\frac{\Rfree -(\Rfree\DiscFac)^{1/\CRRA}}{\Rfree}\right)}_{ \equiv \MPC} \oLev_{\tNow}
\end{aligned}
```

where {math}`\oLev_{\tNow}` is the consumer's "**o**verall" or "total wealth," the sum of human and nonhuman wealth, and {math}`\MPC` is the infinite-horizon marginal propensity to consume.

Now consider the question "What is the level of {math}`\cLevBF_{\tNow}` that will leave total wealth intact, allowing the same value of consumption in period {math}`t+1` and forever after (that is, allowing {math}`\cLevBF_{\tNow+n}=\cLevBF_{\tNow}~\forall~n>0`)?"

The intuitive answer is that the wealth-preserving level of spending is exactly equal to the (properly conceived) interest earnings on one's total wealth. We call this the "sustainable" level of consumption. The literature of the 1970s and 80s interpreted that quantity as "permanent income," but we reserve that term here for {math}`\pLevBF` itself. Wealth in this framework behaves exactly like an asset that pays {math}`\pLevBF` each period.

Because human wealth is exactly like any other kind of wealth in this perfect foresight framework, it is possible to work directly with the level of total wealth {math}`\oLev` to find the sustainable level of spending. Suppose we assume the consumer will spend fraction {math}`\PIHMPC` of total wealth in each period; the {math}`\PIHMPC` that leaves wealth intact will be given by {math}`\PIHMPC` in

```{math}
:label: eq:PIHMPC

\begin{aligned}
        \oLev_{\tNow+1} & =  (\oLev_{\tNow}-\cLevBF_{\tNow})\Rfree
\\  \bar\oLev & =  (\bar\oLev-\PIHMPC \bar\oLev)\Rfree
\\      1 & =  (1-\PIHMPC)  \Rfree
\\      1/\Rfree & =  (1-\PIHMPC)
\\  \PIHMPC & =  1-1/\Rfree
\\  & =  \left(\frac{\Rfree -1}{\Rfree}\right)
\\  & =  \rfree/\Rfree.
\end{aligned}
```

Thus, the consumer can spend only the interest earnings {math}`\rfree` on wealth, divided by the return factor {math}`\Rfree`. (The division occurs because the requirement is to be able to spend the same amount *next* period, so you need to account for the time cost of today's spending by dividing by {math}`\Rfree` which connects today's spending to tomorrow's wealth.)

Note that the coefficient multiplying total wealth in {eq}`eq:PFCRRA-cOfw` is also divided by {math}`\Rfree`. Thus, whether the consumer is spending more than the sustainable amount, exactly the sustainable amount, or less than the sustainable amount depends upon whether the numerator in {eq}`eq:PFCRRA-cOfw` is greater than, equal to, or less than {math}`\rfree`. As noted before, the consumer will be "absolutely impatient" if

```{math}
\begin{aligned}
        \Rfree-(\Rfree\DiscFac)^{1/\CRRA} & >  \rfree  \\
        1-(\Rfree\DiscFac)^{1/\CRRA} & >  0  \\
        1 & >  (\Rfree\DiscFac)^{1/\CRRA}.
\end{aligned}
```

Finally, if {math}`\Rfree\DiscFac=1` (which is to say, the interest rate exactly offsets the time preference rate), then {math}`(\Rfree\DiscFac)^{1/\CRRA}=1` regardless of the value of {math}`\CRRA` so that the consumer is "poised" on the knife-edge between patience and impatience. We refer to such a consumer as "absolutely poised." Similarly, we say that a consumer for whom {math}`\RPFac=1` is "return poised."

The two conditions do different work. Return impatience guarantees a positive marginal propensity to consume, while absolute impatience guarantees a falling level of consumption. Whenever {math}`\rfree > 0`, return impatience holds even for a consumer who is poised with respect to absolute patience.

(The consumer will be impatient, spending more than income, if {math}`\Rfree\DiscFac<1`, and patient, spending less than income, if {math}`\Rfree\DiscFac>1`. Income here means income inclusive of the interest earnings on total wealth.)

Equation {eq}`eq:PFCRRA-cOfw` can be simplified into something a bit easier to handle by making some approximations. If {math}`\DiscFac = 1/(1+\discRte)`, then we can use facts from the [MathFacts section](#fact:mathfactslist) to discover that

```{math}
\begin{aligned}
      \log (\Rfree\DiscFac)^{1/\CRRA}/\Rfree & =  (1/\CRRA) (\log \Rfree + \log [1/(1+\discRte) ]) - \log \Rfree  \\
     & =  (1/\CRRA) (\log(1+\rfree) + \log 1 - \log (1+\discRte) ) - \log \Rfree  \\
         & \approx  \CRRA^{-1}(\rfree -\discRte)  - \rfree
\\      (\Rfree\DiscFac)^{1/\CRRA}/\Rfree & \approx  1+(\CRRA^{-1}(\rfree-\discRte)-\rfree).
\end{aligned}
```

Substituting this into {eq}`eq:PFCRRA-cOfw` gives

```{math}
:label: eq:PFCRRA-capprox

\cLevBF_{\tNow} \approx \left(\rfree-\CRRA^{-1}(\rfree-\discRte)\right)\oLev_{\tNow}.
```

Since {math}`\patr \equiv \log \RPFac`, the approximation just made is a formula for the return patience rate,

```{math}
:label: eq:patrApprox

\patr \approx \CRRA^{-1}(\rfree-\discRte)-\rfree,
```

and the marginal propensity to consume in {eq}`eq:PFCRRA-capprox` is {math}`\MPC \approx -\patr`: the RIC, {math}`\patr<0`, is what makes it positive.

The consumption function {eq}`eq:PFCRRA-cOfw` is exact; {eq}`eq:PFCRRA-capprox` treats {math}`\rfree`, {math}`\discRte` and the return patience rate {math}`\patr` as small. Its error is a different thing from the error of a numerical solution, which approaches the exact formula, not the approximation.

From this we can see again that whether the consumer is absolutely patient, absolutely poised, or absolutely impatient depends on the relationship between {math}`\rfree` and {math}`\discRte`. Note also that if {math}`\CRRA = \infty` then the consumer is infinitely averse to changing the level of consumption, and so once again the consumer spends exactly the sustainable amount. (This consumer is "absolutely poised" but "return impatient").

Now a brief digression on what "income" means in this model. Suppose for simplicity that the consumer had no capital assets ("bank balances" {math}`\bLevBF_{\tNow}=0`), and suppose that income was expected to stay constant at level {math}`\pLevBF_{\tNow+n}=\pLevBF~\forall~n\geq 0` forever. In this case human wealth would be:

```{math}
\begin{aligned}
        \hLevBF_{\tNow} & = \pLevBF+\pLevBF/\Rfree+\pLevBF/\Rfree^{2}+\ldots  \\
         & = \pLevBF(1+1/\Rfree+1/\Rfree^{2}+\ldots)  \\
         & = \pLevBF\left(\frac{1}{1-1/\Rfree}\right)
\\   & = \pLevBF\left(\frac{\Rfree}{\Rfree -1}\right)
\\   & = \pLevBF\left(\frac{\Rfree}{\rfree}\right).
\end{aligned}
```

We found in equation {eq}`eq:PIHMPC` that the level of consumption that leaves "wealth" {math}`\oLev_{\tNow}` intact was

```{math}
\begin{aligned}
        \cLevBF_{\tNow} & =  \left(\frac{\rfree}{\Rfree}\right) \oLev_{\tNow}  \\
         & =  \left(\frac{\rfree}{\Rfree}\right) (\underbrace{\bLevBF_{\tNow}}_{=0}+\hLevBF_{\tNow}) \\
                        & =  \left(\frac{\rfree}{\Rfree}\right)     \pLevBF \left(\frac{\Rfree}{\rfree}\right)\\
                        & =  \pLevBF.
\end{aligned}
```

So in this case, spending the "interest income on human wealth" corresponds to spending exactly your labor income. This seems less mysterious if you think of income {math}`\pLevBF_{\tNow}` as the "return" on your human capital, which is an asset whose value is {math}`\hLevBF_{\tNow}`. If you "capitalize" your stream of income using the interest factor {math}`\Rfree` and then spend the interest income on the capitalized stream, it stands to reason that you are spending the flow of income from that source.

With constant {math}`\pLevBF` we can rewrite {eq}`eq:PFCRRA-capprox` as

```{math}
\cLevBF_{\tNow} \approx \left(\rfree-\CRRA^{-1}(\rfree-\discRte)\right)\left(\bLevBF_{\tNow}+ \pLevBF\left(\frac{\Rfree}{\rfree}\right)\right).
```

{math}`\rfree` appears in three expressions of this equation. In order, the three are the income effect, the substitution effect and the human wealth effect, as the [two-period model](#sec:2PeriodLCModel) defines them. The first two are inside the marginal propensity to consume out of total wealth, so they are the effects of {math}`\rfree` on consumption for a given total wealth {math}`\bLevBF_{\tNow}+\hLevBF_{\tNow}`. An increase in the first {math}`\rfree` raises the payout rate on total wealth (set {math}`\pLevBF = 0` and use {eq}`eq:PIHMPC` for {math}`\PIHMPC`, with {math}`\rfree/\Rfree \approx \rfree` for small {math}`\rfree`): this is the income effect. The second is the substitution effect, as its dependence on the intertemporal elasticity of substitution {math}`\CRRA^{-1}` shows. The third, in {math}`\pLevBF(\Rfree/\rfree)`, is the human wealth effect: the effect of {math}`\rfree` on human wealth itself, which comes from the budget constraint and involves no preference parameter. Bank balances {math}`\bLevBF_{\tNow}` are in none of the three; they are part of the total wealth that the marginal propensity to consume applies to. Because consumption depends on {math}`\bLevBF_{\tNow}` and {math}`\hLevBF_{\tNow}` only through their sum, this formula, like the two-period model, rests on the assumption, made at the start, that the consumer can borrow against future income at no penalty. [How Large is the Human Wealth Effect?](#subsec:HWEffect) measures what the human wealth effect does to consumption under that assumption.

## Normalizing By {math}`\pLevBF`

The whole problem can be restated more simply by "dividing through" by the level of permanent income before solving. Hereafter, nonbold variables will be the normalized bold-letter equivalent, e.g. {math}`\cNrm_{\tNow}=\cLevBF_{\tNow}/\pLevBF_{\tNow}`, and note that if {math}`\pLevBF_{\tNow+1}={\PermGroFac} \pLevBF_{\tNow}~\forall~t` then from the standpoint of date {math}`t`,

```{math}
\begin{aligned}
        \uFunc(\cLevBF_{\tNow+n}) & =  \frac{\cLevBF_{\tNow+n}^{1-\CRRA}}{1-\CRRA}  \\
         & =  \frac{(\cNrm_{\tNow+n}\pLevBF_{\tNow+n})^{1-\CRRA}}{1-\CRRA}  \\
         & =  (\pLevBF_{\tNow}{\PermGroFac}^{n})^{1-\CRRA}\frac{\cNrm_{\tNow+n}^{1-\CRRA}}{1-\CRRA}
\end{aligned}
```

which means that

```{math}
:label: eq:PFCRRA-maxc2

\sum_{n=0}^{\TEnd-\tNow} \DiscFac^{n}\frac{\cLevBF_{\tNow+n}^{1-\CRRA}}{1-\CRRA} = \pLevBF_{\tNow}^{1-\CRRA}\sum_{n=0}^{\TEnd-\tNow} ({\PermGroFac}^{1-\CRRA}\DiscFac)^{n} \frac{\cNrm_{\tNow+n}^{1-\CRRA}}{1-\CRRA}.
```

Furthermore, the accumulation equations can be rewritten by dividing both sides by {math}`\pLevBF_{\tNow+1}`:

```{math}
\begin{aligned}
        \bLevBF_{\tNow+1}/\pLevBF_{\tNow+1} & =  \frac{(\mLevBF_{\tNow}-\cLevBF_{\tNow})\Rfree}{\pLevBF_{\tNow+1}}  \\
        \bNrm_{\tNow+1} & =   \left(\frac{(\mLevBF_{\tNow}-\cLevBF_{\tNow})\Rfree}{\pLevBF_{\tNow}}\right)\left(\frac{\pLevBF_{\tNow}}{\pLevBF_{\tNow+1}}\right) \\
         & =  (\mNrm_{\tNow}-\cNrm_{\tNow})(\Rfree/{\PermGroFac})
\end{aligned}
```

```{math}
\begin{aligned}
        \mLevBF_{\tNow+1} & =  \bLevBF_{\tNow+1}+\pLevBF_{\tNow+1}
\\      \mNrm_{\tNow+1} & =  \bNrm_{\tNow+1}+1.
\end{aligned}
```

Now if we define {math}`\DiscAlt \equiv {\PermGroFac}^{1-\CRRA}\DiscFac` and {math}`\RNrmByG \equiv \Rfree/{\PermGroFac}`, the original problem can be rewritten as:

```{math}
:label: eq:PFCRRA-scaledmaxprob

\max~~\pLevBF_{\tNow}^{1-\CRRA}\sum_{n=0}^{\TEnd-\tNow} \DiscAlt^{n} \uFunc(\cNrm_{\tNow+n})
```

subject to the constraints

```{math}
\begin{aligned}
   \aNrm_{\tNow}   & =  \mNrm_{\tNow}-\cNrm_{\tNow}
\\ \bNrm_{\tNow+1} & =  \aNrm_{\tNow}\RNrmByG
\\ \mNrm_{\tNow+1} & =  \bNrm_{\tNow+1}+1
\end{aligned}
```

and we can go through the same steps as above to find that the solution is

```{math}
:label: eq:normC

\cNrm_{\tNow} = (1-\RNrmByG^{-1}(\RNrmByG\DiscAlt)^{1/\CRRA})\left[\mNrm_{\tNow}-1+\overbrace{\left(\frac{1}{1-{1}/\RNrmByG}\right)}^{\equiv\hNrm}\right]
```

subject to the "finite human wealth" condition

```{math}
\begin{aligned}
        {1} & <  \RNrmByG
\\  1 & <  \Rfree/\PermGroFac
\end{aligned}
```

which is the same condition {eq}`eq:FHWCPF` as above, and also subject to the "return impatience condition"

```{math}
\begin{aligned}
                (\RNrmByG\DiscAlt)^{1/\CRRA} & <  \RNrmByG
\\              \left(\frac{\Rfree}{{\PermGroFac}}\DiscFac {\PermGroFac}^{1-\CRRA}\right)^{1/\CRRA} & <  \Rfree/{\PermGroFac}
\\              (\Rfree\DiscFac)^{1/\CRRA} & <  \Rfree
\end{aligned}
```

which is also the same as above in {eq}`eq:PatR`.

Now note that {eq}`eq:normC` can be rewritten

```{math}
\begin{aligned}
        \cNrm_{\tNow} & =  \left(\frac{\RNrmByG-(\RNrmByG\DiscAlt)^{1/\CRRA}}{\RNrmByG}\right)\oNrm_{\tNow}
\\ & =  \underbrace{(1 - \RPFac)}_{\equiv \MPC} \oNrm_{\tNow}
\end{aligned}
```

where {math}`\oNrm_{\tNow}` is the consumer's total wealth-to-permanent-labor-income ratio, and {math}`\MPC` is the "marginal propensity to consume" out of wealth.

As before, whether {math}`\oNrm` is rising or falling depends upon the relationship between {math}`\RNrmByG-1` and {math}`\RNrmByG-(\RNrmByG\DiscAlt)^{1/\CRRA}`. A consumer will be drawing down the wealth-to-income ratio if

```{math}
\begin{aligned}
        \RNrmByG-(\RNrmByG\DiscAlt)^{1/\CRRA} & >  \RNrmByG-1  \\
        1-(\RNrmByG\DiscAlt)^{1/\CRRA} & >  0  \\
        1 & >  (\RNrmByG\DiscAlt)^{1/\CRRA}.
\end{aligned}
```

Now substituting the definitions of {math}`\RNrmByG` and {math}`\DiscAlt` we see that whether {math}`\oNrm` is rising or falling depends on whether

```{math}
:label: eq:PatWGroCond

\begin{aligned}
        1 & >  (\frac{\Rfree}{{\PermGroFac}}\DiscFac {\PermGroFac}^{1-\CRRA})^{1/\CRRA}
\\  1 & >  (\Rfree\DiscFac {\PermGroFac}^{-\CRRA})^{1/\CRRA}
\\  1 & >  \underbrace{\left(\frac{(\Rfree\DiscFac)^{1/\CRRA}}{\PermGroFac}\right)}_{\GPFac},
\end{aligned}
```

where {math}`\GPFac` is the "growth patience factor." We call {eq}`eq:PatWGroCond` the "growth impatience condition" (GIC), and we say that the consumer is "growth impatient" if {eq}`eq:PatWGroCond` holds.

:::{margin}
Or, GIC-PF if we want to highlight that this is the condition for the perfect foresight model.
:::

Thus, whether the consumer is patient or impatient in the sense of building up or drawing down a wealth-to-income *ratio* depends on whether the growth rate of labor income is less than, equal to, or greater than the growth rate of consumption. Analogously to our earlier usages, a consumer for whom {math}`\GPFac=1` (equivalently, a growth patience rate {math}`\GPRte \equiv \log \GPFac = 0`) would be "growth poised."

To get the intuition for this, consider the case of a consumer with no nonhuman wealth, {math}`\bNrm_{\tNow}=0`. This consumer's absolute level of consumption will grow at {math}`(\Rfree\DiscFac)^{1/\CRRA}` and absolute level of income grows at {math}`{\PermGroFac}`, but the PDV of future consumption and future income must be equal. If income is growing faster than consumption but has the same PDV, consumption must be *starting out* at a level *higher* than income, which is the sense in which this consumer is impatient (spending more than income). "Growth impatience" is therefore the condition that causes consumers with no assets to want to borrow.

The condition also decides where the consumer ends up. Total wealth relative to permanent income evolves as {math}`\oNrm_{\tNow+1} = (\oNrm_{\tNow}-\cNrm_{\tNow})\RNrmByG = (1-\MPC)\RNrmByG\,\oNrm_{\tNow}`, and since {math}`(1-\MPC)\RNrmByG = \RPFac\Rfree/\PermGroFac = \GPFac`,

```{math}
:label: eq:oNrmPath

\oNrm_{\tNow+1} = \GPFac\,\oNrm_{\tNow}.
```

A growth impatient consumer's total wealth therefore shrinks toward zero relative to income. Consumption relative to permanent income falls toward zero, and market resources approach {math}`-\hNrmEnd`, minus end-of-period human wealth: the consumer ends up owing the present value of all future income, the most that could ever be repaid. A consumer whose GIC fails instead accumulates wealth relative to income without bound. [The figure of the paths](#fig:PathsGIC) shows both. Neither end is plausible, which is one reason later chapters add uncertainty and liquidity constraints.

:::{figure} figures/PerfForesightPathsGIC.png
:name: fig:PathsGIC
:align: center

Consumption and market resources relative to permanent income over 100 years, for a consumer who starts with no bank balances, when the GIC holds ({math}`\PermGroRte=0.02`) and when it fails ({math}`\PermGroRte=-0.01`). In both, {math}`\rfree=\discRte=0.04` and {math}`\CRRA=2`, so the RIC and the FHWC hold. The dotted line is {math}`-\hNrmEnd` when the GIC holds. Drawn by the chapter's [notebook](PerfForesightCRRA.ipynb); open it in [Colab](https://colab.research.google.com/github/intertemporal-choice/intertemporal-choice.github.io/blob/main/content/consumption/PerfForesightCRRA/PerfForesightCRRA.ipynb) or [Binder](https://mybinder.org/v2/gh/intertemporal-choice/intertemporal-choice.github.io/main?labpath=content/consumption/PerfForesightCRRA/PerfForesightCRRA.ipynb) to run it without installing anything.
:::

## Applications

(subsec:HWEffect)=
### How Large is the Human Wealth Effect?

We can now apply the model to answer our first useful question: How large does the model imply the "human wealth effect" is?

For simplicity, assume that {math}`\bNrm_{\tNow} = 0`. Then the original version of the approximate formula {eq}`eq:PFCRRA-capprox` tells us that the *level* of consumption will be given by:

```{math}
:label: eq:PFCRRA-cofw2

\begin{aligned}
        \cLevBF_{\tNow} & \approx  \left(\rfree - \CRRA^{-1}(\rfree-\discRte)\right)\left(\frac{\pLevBF_{\tNow}}{1-{\PermGroFac}/\Rfree}\right)  \\
         & \approx  \left(\rfree - \CRRA^{-1}(\rfree-\discRte)\right)\left(\frac{\pLevBF_{\tNow}}{\rfree-\PermGroRte}\right).
\end{aligned}
```

We are interested only in calibrations of the model in which the consumer is "growth impatient" so that {math}`\PermGroRte > \CRRA^{-1}(\rfree-\discRte)`. By the same approximation as {eq}`eq:patrApprox`, the growth patience rate is

```{math}
:label: eq:patwGro

\GPRte \approx \CRRA^{-1}(\rfree-\discRte)-\PermGroRte
```

so we can write this as

```{math}
:label: eq:CvsP

\begin{aligned}
        \cLevBF_{\tNow} & \approx  \pLevBF_{\tNow} \left(\frac{\rfree - (\PermGroRte+\GPRte)}{\rfree-\PermGroRte}\right)
\\ & =  \pLevBF_{\tNow} \left(1 - \GPRte/(\rfree - \PermGroRte)\right).
\end{aligned}
```

Remembering that imposition of the growth impatience condition is equivalent to assuming {math}`\GPRte < 0`, while the FHWC requires {math}`\rfree > \PermGroRte`, it is clear that the expression {math}`-\GPRte/(\rfree-\PermGroRte)` will be positive: The consumer will spend more than permanent labor income.

Now suppose we choose plausible values for {math}`(\rfree, \discRte, \PermGroRte, \CRRA) = (0.04,0.04,0.02,2)`. Then {eq}`eq:PFCRRA-cofw2` becomes:

```{math}
\begin{aligned}
        \cLevBF_{\tNow} & \approx  0.04 (\pLevBF_{\tNow}/0.02) \\
         & =  2 \pLevBF_{\tNow}.
\end{aligned}
```

Now suppose the interest rate changes to {math}`\rfree=0.03`, while all other parameters remain the same. Then {eq}`eq:PFCRRA-cofw2` becomes:

```{math}
\begin{aligned}
        \cLevBF_{\tNow} & \approx  0.035 (\pLevBF_{\tNow}/0.01)  \\
         & =  3.5 \pLevBF_{\tNow}.
\end{aligned}
```

In terms of the three effects of {math}`\rfree` in {eq}`eq:PFCRRA-capprox`, with {math}`\bNrm_{\tNow}=0` consumption is {math}`\MPC\hNrm` times permanent income, where {math}`\MPC = \rfree-\CRRA^{-1}(\rfree-\discRte)` and {math}`\hNrm \approx 1/(\rfree-\PermGroRte)`, so {math}`\log \cNrm_{\tNow} = \log \MPC + \log \hNrm` and the three effects add:

```{math}
:label: eq:dlogcdr

\frac{d \log \cNrm_{\tNow}}{d \rfree} \approx \underbrace{\frac{1}{\MPC}}_{\text{income}} - \underbrace{\frac{\CRRA^{-1}}{\MPC}}_{\text{substitution}} + \underbrace{\frac{1}{\PermGroRte-\rfree}}_{\text{human wealth}}.
```

The income and substitution terms are positive because the RIC makes {math}`\MPC>0`; the human wealth term is negative because the FHWC requires {math}`\rfree>\PermGroRte`. At the calibration above the three terms are 25, −12.5 and −50. In the example, the fall in {math}`\rfree` lowers the marginal propensity to consume from 0.04 to 0.035 (the income effect lowers it by 0.01, the substitution effect raises it by 0.005), while human wealth doubles, from 50 to 100 times permanent income: −0.13 against +0.69 in logs. The human wealth effect exceeds the income effect whenever the consumer is growth impatient, because the two net to {math}`\GPRte/(\MPC(\rfree-\PermGroRte))`, here −25.

These magnitudes depend on the infinite horizon. A consumer with {math}`\TEnd-\tNow+1=40` years left, earning permanent income in each of them, has human wealth of 28 times permanent income by [the PDV of labor income](#eq:PFCRRA-yfin), against 52 with no end (50 by the approximation above), and by [the finite-horizon consumption function](#eq:PFCRRA-cfinhoriz) consumes 1.36 times permanent income. When {math}`\rfree` falls to 0.03, that consumer's human wealth rises by 18.5 percent rather than doubling, and consumption rises by 10 percent rather than by about three-quarters. The human wealth effect still outweighs the other two together, but by about 2.3 to 1 rather than 4 to 1, because a finite horizon shortens the stream of income that the interest rate discounts.

The point of this example is that for plausible parameter values, the human wealth effect is enormously stronger than the income and substitution effects, so that we should see large drops in consumption when interest rates rise and conversely strong gains when interest rates fall. This is a summary of the main point of the famous paper by {cite:t}`summersCapTax`; Summers derives formulas for an economy with overlapping generations of finite-lifetime consumers. Finite lifetimes shrink the effect, as the calculation above shows, but in his model it is still large.

Nor is a change of a percentage point in the long-term real interest rate unusual. [The long-term real interest rate figure](#fig:LongTermRealRate) shows two measures of it. One is the Federal Reserve Bank of Cleveland's estimate of the real rate expected over the next ten years, from a model fitted to Treasury yields, inflation, inflation swaps and surveys of expected inflation {cite:p}`haubrichInflationSwaps`. The other is the yield on ten-year inflation-indexed Treasury bonds (TIPS). The expected rate averaged 5.3 percent a year in the 1980s and 0.6 percent in the 2010s, and reached a low of −0.4 percent in August 2020. The TIPS yield rose by 3.5 percentage points in two years, from −1.07 percent in August 2021 to 2.41 percent in October 2023. Since 1982 the expected rate has moved by a percentage point or more within a year in 13 percent of months, and within two years in 24 percent. The [notebook](PerfForesightCRRA.ipynb) computes these numbers from FRED's data; open it in [Colab](https://colab.research.google.com/github/intertemporal-choice/intertemporal-choice.github.io/blob/main/content/consumption/PerfForesightCRRA/PerfForesightCRRA.ipynb) or [Binder](https://mybinder.org/v2/gh/intertemporal-choice/intertemporal-choice.github.io/main?labpath=content/consumption/PerfForesightCRRA/PerfForesightCRRA.ipynb) to run it without installing anything.

:::{figure} figures/LongTermRealRate.png
:name: fig:LongTermRealRate
:align: center

Two measures of the U.S. long-term real interest rate, monthly, in percent a year: the Federal Reserve Bank of Cleveland's estimate of the real rate expected over the next ten years (FRED series REAINTRATREARAT10Y, from 1982), and the yield on ten-year inflation-indexed Treasury bonds (FRED series FII10, from 2003). Downloaded from FRED on 2026-10-20. Drawn by the chapter's [notebook](PerfForesightCRRA.ipynb); open it in [Colab](https://colab.research.google.com/github/intertemporal-choice/intertemporal-choice.github.io/blob/main/content/consumption/PerfForesightCRRA/PerfForesightCRRA.ipynb) or [Binder](https://mybinder.org/v2/gh/intertemporal-choice/intertemporal-choice.github.io/main?labpath=content/consumption/PerfForesightCRRA/PerfForesightCRRA.ipynb) to run it without installing anything.
:::

The model's predictions for these episodes are not borne out. With {math}`\PermGroRte=0.02`, the finite human wealth condition fails whenever {math}`\rfree<0.02`, as the expected real rate did throughout the 2010s; the infinite-horizon formula then has no answer, and only a finite horizon gives one. At the same calibration, with 40 years left, the rise in the TIPS yield from −1.07 to 2.41 percent would cut consumption by about a third, from 2.5 to 1.6 times permanent income. Nothing of the kind happened: real consumer spending in the United States kept growing through 2022 and 2023. The model's response is too large for several reasons. It takes the change in the interest rate to be permanent and known. Its consumers can borrow freely against future income, so the whole change in human wealth reaches their spending. And it ignores general equilibrium, in which incomes and other prices move with the interest rate: in a model with uninsurable income risk and assets of different liquidity, the indirect effects of a change in the interest rate, through labor demand, far outweigh direct effects such as intertemporal substitution {cite:p}`kmvHANK`.

(subsec:SavingRateResponse)=
### How Does the Saving Rate Respond to Interest Rates?

The level of saving can be defined as total income minus total consumption:

```{math}
\sLevBF_{\tNow} = \rfree \aLevBF_{\tNow-1} + \pLevBF_{\tNow} - \cLevBF_{\tNow}
```

but substituting from {eq}`eq:CvsP` and {eq}`eq:PFCRRA-capprox`,

```{math}
:label: eq:cFromHandB

\cLevBF_{t} \approx \pLevBF_{\tNow} \left(1 - \GPRte/(\rfree - \PermGroRte)\right)-\patr\bLevBF_{\tNow}
```

this can be rewritten as

```{math}
\begin{aligned}
 \sLevBF_{\tNow} & \approx  \rfree \aLevBF_{\tNow-1} + \pLevBF_{\tNow}- \pLevBF_{\tNow} \left(1 - \GPRte/(\rfree - \PermGroRte)\right) + \patr\Rfree \aLevBF_{\tNow-1}
\\ & =  \rfree \aLevBF_{\tNow-1} + \pLevBF_{\tNow} \GPRte/(\rfree - \PermGroRte) + \patr\Rfree\aLevBF_{\tNow-1}
\\ \sNrm_{\tNow} & \approx  \rfree \aNrm_{\tNow-1} + \GPRte/(\rfree - \PermGroRte) + \patr\Rfree \aNrm_{\tNow-1}
\\ & \approx  \GPRte/(\rfree - \PermGroRte)+ \CRRA^{-1}(\rfree-\discRte)\aNrm_{\tNow-1}
\end{aligned}
```

(where the last approximations come from the assumptions that {math}`1/\PermGroFac \approx 1` and that {math}`\rfree\patr`, the product of two small rates, is zero, so that {math}`\rfree+\patr\Rfree \approx \rfree+\patr = \CRRA^{-1}(\rfree-\discRte)` by {eq}`eq:patrApprox`). The saving *rate* (for which we use the letter {math}`\srate` to distinguish it from {math}`\sNrm` above) is the ratio of saving to *total* income (not just labor income):

```{math}
\varsigma_{\tNow} = \left(\frac{\GPRte/(\rfree - \PermGroRte)+ \CRRA^{-1}(\rfree-\discRte)\aNrm_{\tNow-1}}{1+ \rfree \aNrm_{\tNow-1}}\right).
```

The first thing to notice about this expression is that as {math}`\aNrm_{\tNow-1}` approaches infinity, the saving rate asymptotes to

```{math}
\varsigma_{\tNow} \approx \left(\frac{\CRRA^{-1}(\rfree-\discRte)}{\rfree}\right)
```

and whether the saving rate is positive or negative depends on whether the consumer is absolutely impatient, absolutely poised, or absolutely patient.

:::{margin}
In this partial equilibrium framework, we are assuming that the consumer's wealth can go to infinity without any effect on the aggregate interest rate.
:::

If we rewrite this as

```{math}
\varsigma \approx \CRRA^{-1} (1 - \discRte \rfree^{-1})
```

then it is apparent that the response of the asymptotic saving rate to the interest rate is

```{math}
:label: eq:dsdr

\left(\frac{d \varsigma}{d \rfree}\right) = \CRRA^{-1}\discRte \rfree^{-2}.
```

If we consider almost any plausible configuration of parameter values, say {math}`\rfree = \discRte=0.05` and {math}`\CRRA = 2`, this translates to a very large response of the saving rate with respect to {math}`\rfree` (in the case of the parameter values mentioned above, {math}`(1/2)(20)=10`).

In terms of the three effects of {math}`\rfree` in {eq}`eq:PFCRRA-capprox`, this response is entirely a substitution effect. A consumer whose wealth is enormous relative to income has negligible human wealth, so the human wealth effect is negligible too. The income effect raises the marginal propensity to consume by the rise in {math}`\rfree`, and so raises consumption by the rise in {math}`\rfree` times wealth, but capital income rises by exactly as much, so the income effect leaves saving unchanged. What remains is the substitution effect: consumption grows faster by {math}`\CRRA^{-1}` times the rise in {math}`\rfree`, and a consumer who lives on capital income can make consumption grow faster only by making wealth grow faster, so saving rises by {math}`\CRRA^{-1}` times the rise in {math}`\rfree` times wealth. The saving *rate* responds so strongly because it divides that change by income, which is only {math}`\rfree` times wealth. Writing {eq}`eq:dsdr` as {math}`\CRRA^{-1}\rfree^{-1} - \varsigma\rfree^{-1}` shows this: the first term is the substitution effect, and the second, zero for an absolutely poised consumer, is only the effect of higher income on the rate's denominator.

A consumer with no wealth responds even more strongly, and for a different reason. With {math}`\aNrm_{\tNow-1}=0`, the saving rate is {math}`\GPRte/(\rfree-\PermGroRte) = 1-\MPC\hNrm`, with {math}`\hNrm \approx 1/(\rfree-\PermGroRte)`, and its response to the interest rate is

```{math}
:label: eq:dsdrNoWealth

\left(\frac{d \varsigma}{d \rfree}\right)_{\aNrm_{\tNow-1}=0} = -\underbrace{\hNrm}_{\text{income}}+\underbrace{\CRRA^{-1}\hNrm}_{\text{substitution}}+\underbrace{\MPC\hNrm^{2}}_{\text{human wealth}} = \frac{(1-\CRRA^{-1})\PermGroRte+\CRRA^{-1}\discRte}{(\rfree-\PermGroRte)^{2}}.
```

All three effects are at work, each measured in its own terms and then turned into saving. The income effect raises the marginal propensity to consume one for one with {math}`\rfree`, which raises consumption, and so lowers saving, by {math}`\hNrm` per unit of {math}`\rfree`; with no wealth, there is no capital income to offset it. The substitution effect lowers the marginal propensity to consume by {math}`\CRRA^{-1}` per unit of {math}`\rfree`, which raises saving by {math}`\CRRA^{-1}\hNrm`. The human wealth effect lowers human wealth by {math}`\hNrm/(\rfree-\PermGroRte) = \hNrm^{2}`, which at the marginal propensity to consume {math}`\MPC` raises saving by {math}`\MPC\hNrm^{2}`.

With the calibration of [How Large is the Human Wealth Effect?](#subsec:HWEffect), {math}`(\rfree, \discRte, \PermGroRte, \CRRA) = (0.04,0.04,0.02,2)`, human wealth is 50 times income and {math}`\MPC=0.04`, so the three terms are −50, 25 and 100, and the response is 75, six times the 12.5 that {eq}`eq:dsdr` gives at the same parameter values. When {math}`\rfree` falls to 0.03, the saving rate falls from −1 to −2.5, the mirror image of that section's rise in consumption from 2 to 3.5 times income.

The human wealth effect is the largest of the three here, and it exceeds the income effect whenever the consumer is growth impatient: {math}`\MPC\hNrm^{2}>\hNrm` exactly when {math}`\MPC\hNrm>1`, that is, when a consumer with no wealth spends more than income, which is {math}`\GPRte<0`. It is also the effect that mechanisms later in the course, liquidity constraints and precautionary saving, drastically attenuate for some households while leaving a meaningful income effect in place. Their human wealth falls by just as much when {math}`\rfree` rises, but because they will not borrow against future income, the fall does much less to their consumption and their saving.

The evidence also tempers the response at the other end. For a consumer with large wealth the response is entirely intertemporal substitution, and many estimates of the elasticity of intertemporal substitution are below the 0.5 used here; {cite:t}`hallSubstitution` finds it close to zero.

(sec:PerfForesightCRRA-AppendixResults)=
## Results in the Appendix

The [appendix](#sec:PerfForesightCRRA-Appendix) derives three further results, which are stated here without their derivations.

- *[The limiting solution if the FHWC fails](#sec:PFwhenFHWfails).* If the finite human wealth condition fails, the limit of the finite-horizon solutions depends on the growth impatience condition. If it holds, as it must when the return impatience condition holds, consumption out of human wealth grows without bound. If the return and growth impatience conditions both fail, consumption goes to zero; on the boundary between the two, {math}`\GPFac=1`, it converges to permanent income.
- *[The MPC recursion](#sec:PerfForesightCRRA-MPCRecursion).* The inverse of the MPC satisfies {math}`\MPC_{t}^{-1} = 1+\RPFac\MPC_{t+1}^{-1}`.
  Starting from {math}`\MPC_{T}=1`, this makes {math}`\MPC_{t}^{-1}` the sum {math}`1+\RPFac+\RPFac^{2}+\dots+\RPFac^{T-t}`.
- *[Value in closed form](#sec:PerfForesightCRRA-ValueClosedForm).* Value is current utility times the inverse of the MPC: {math}`\vFunc_{t} = \uFunc(\cLevBF_{t})\MPC_{t}^{-1} = \uFunc(\oLev_{t})\MPC_{t}^{-\CRRA}`.
  One consequence is that the utility-inverse of value is linear in market resources above their minimum, so value is easy to compute.
