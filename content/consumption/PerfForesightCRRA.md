(sec:PerfForesightCRRA)=
# Consumption Under Perfect Foresight and CRRA Utility
## The Problem

This section solves the problem of a perfect foresight consumer with intertemporally separable CRRA utility {math}`\uFunc(\bullet)= \bullet^{1-\CRRA}/(1-\CRRA)` who discounts future utility geometrically by a factor {math}`\Discount` per period. The finite horizon solution, whose last period is {math}`\TEnd`, extends to the infinite horizon case if intuitive "impatience" and "finite human wealth" conditions hold.

The consumer's problem in period {math}`t` is to

```{math}
:label: eq:PFCRRA-maxprob

\max \sum_{n=0}^{\TEnd-\tNow} \Discount^{n} \uFunc(\cLevBF_{\tNow+n})
```

subject to the constraints

:::{margin}
Introducing {math}`\bLevBF` and {math}`\mLevBF` because useful to have a term for non-income resources at beginning of period.
:::

```{math}
\begin{aligned}
      \aLevBF_{\tNow}   & =  \mLevBF_{\tNow}-\cLevBF_{\tNow}
\\    \bLevBF_{\tNow+1} & =  \aLevBF_{\tNow}\Rfree
\\    \mLevBF_{\tNow+1} & =  \bLevBF_{\tNow+1}+\pLevBF_{\tNow+1}
\end{aligned}
```

where {math}`\pLevBF_{\tNow+1}` is "permanent labor income," which always grows by a factor {math}`\WGro`:

```{math}
\pLevBF_{\tNow+1}/\pLevBF_{\tNow} = {\WGro}.
```

## The Solution

It will be convenient to think of both market resources {math}`\mLevBF_{\tNow}` and permanent noncapital (labor) income {math}`\pLevBF_{\tNow}` as state variables in this problem. Bellman's equation is

:::{margin}
Bellman's equation relates {math}`\vFunc_{\tNow}` and {math}`\vFunc_{\tNow+1}` through the controls and states. It doesn't necessarily require writing out the budget constraint.
:::

```{math}
:label: eq:PFCRRA-vmax

\vFunc_{\tNow}(\mLevBF_{\tNow},\pLevBF_{\tNow}) = \max_{\cLevBF_{\tNow}} \left\{ \uFunc(\cLevBF_{\tNow}) + \Discount \vFunc_{\tNow+1}\left(\overbrace{(\mLevBF_{\tNow}-\cLevBF_{\tNow})\Rfree+\pLevBF_{\tNow+1}}^{=\mLevBF_{\tNow+1}},\pLevBF_{\tNow+1}\right)\right\}.
```

The first order condition for this maximization is

```{math}
:label: eq:upeqrbv

\uFunc^{\prime}(\cLevBF_{\tNow}) = \Discount \left(\Rfree \vFunc_{\tNow+1}^{\mLevBF}(\mLevBF_{\tNow+1},\pLevBF_{\tNow+1})-\overbrace{\frac{d\pLevBF_{\tNow+1}}{d \cLevBF_{\tNow}}}^{=0}\vFunc_{\tNow+1}^{\pLevBF}(\mLevBF_{\tNow+1},\pLevBF_{\tNow+1})\right),
```

and the Envelope theorem tells us that

```{math}
:label: eq:vpeqrbv

\vFunc_{\tNow}^{\mLevBF}(\mLevBF_{\tNow},\pLevBF_{\tNow}) = \Rfree \Discount \vFunc_{\tNow+1}^{\mLevBF}(\mLevBF_{\tNow+1},\pLevBF_{\tNow+1}).
```

But the right hand sides of {eq}`eq:upeqrbv` and {eq}`eq:vpeqrbv` are identical, so

```{math}
\vFunc_{\tNow}^{\mLevBF}(\mLevBF_{\tNow},\pLevBF_{\tNow}) = \uFunc^{\prime}(\cLevBF_{\tNow})
```

and similar logic tells us that {math}`\vFunc_{\tNow+1}^{\mLevBF}(\mLevBF_{\tNow+1},\pLevBF_{\tNow+1})=\uFunc^{\prime}(\cLevBF_{\tNow+1}),` which (substituting {math}`\uFunc^{\prime}` for {math}`\vFunc^{\mLevBF}` in {eq}`eq:vpeqrbv`) gives us the Euler equation for consumption:

```{math}
:label: eq:PFCRRA-cgrow

\begin{aligned}
        \uFunc^{\prime}(\cLevBF_{\tNow}) & =  \Rfree\Discount \uFunc^{\prime}(\cLevBF_{\tNow+1}) \\
        1 & =  \Rfree\Discount \left(\frac{\cLevBF_{\tNow+1}}{\cLevBF_{\tNow}}\right)^{-\CRRA}
\\  \left(\frac{\cLevBF_{\tNow+1}}{\cLevBF_{\tNow}}\right) & =  (\Rfree\Discount)^{1/\CRRA}.
\end{aligned}
```

Thus, consumption grows in every period by a factor {math}`\Pat \equiv (\Rfree\Discount)^{1/\CRRA}`, where we use the Old English letter {math}`\Pat` to measure what we will call the "absolute patience" factor. Specifically, if

```{math}
:label: eq:AIC

\Pat < 1
```

we will say that the consumer exhibits "absolute impatience" because this is the condition that guarantees that the level of consumption will be falling (and what better definition of absolute impatience could there be than deliberately spending so much that you will have to cut your spending in the future?). If {math}`\Pat > 1` the consumer exhibits "absolute patience" (the consumer wants to defer resources into the future in order to achieve consumption growth).

:::{margin}
Note that [InfSum](#fact:infsum) is an obvious implication of [FinSum](#fact:finsum) as {math}`\TEnd \rightarrow \infty`.
:::

The Intertemporal Budget Constraint tells us that the present discounted value of consumption must match the PDV of total resources:

```{math}
:label: eq:PFCRRA-ibc

\PDV_{\tNow}^{\TEnd}(\cLevBF) = \bLevBF_{\tNow}+\PDV_{\tNow}^{\TEnd}(\pLevBF).
```

Fact [FinSum](#fact:finsum) can be used to show that the PDV of labor income (also called "human wealth" {math}`\hLevBF_{\tNow}`) is

```{math}
:label: eq:PFCRRA-yfin

\begin{aligned}
        \hLevBF_{\tNow} = \PDV_{\tNow}^{\TEnd}(\pLevBF) & =  \sum_{n=0}^{\TEnd-\tNow} \Rfree^{-n}\pLevBF_{\tNow+n}
\\       & =  \pLevBF_{\tNow}\sum_{n=0}^{\TEnd-\tNow} \Rfree^{-n}{\WGro}^{n} = \pLevBF_{\tNow}\sum_{n=0}^{\TEnd-\tNow} ({\WGro}/\Rfree)^{n}
\\   & =  \pLevBF_{\tNow}\left(\frac{1-({\WGro}/\Rfree)^{\TEnd-\tNow+1}}{1-({\WGro}/\Rfree)}\right)
\end{aligned}
```

while the PDV of consumption is

```{math}
:label: eq:cfin

\begin{aligned}
        \PDV_{\tNow}^{\TEnd}(\cLevBF) & =  \sum_{n=0}^{\TEnd-\tNow} \Rfree^{-n}\cLevBF_{\tNow+n}
\\       & =  \sum_{n=0}^{\TEnd-\tNow} \Rfree^{-n}\cLevBF_{\tNow}((\Rfree\Discount)^{1/\CRRA})^{n}
\\       & =  \cLevBF_{\tNow} \sum_{n=0}^{\TEnd-\tNow} [\Rfree^{-1}(\Rfree\Discount)^{1/\CRRA}]^{n}
\\   & =  \cLevBF_{\tNow}\left(\frac{1-[\Rfree^{-1}(\Rfree\Discount)^{1/\CRRA}]^{\TEnd-\tNow+1}}{1-[\Rfree^{-1}(\Rfree\Discount)^{1/\CRRA}]}\right).
\end{aligned}
```

(cFuncAnalytical)=
We can solve the model by combining {eq}`eq:cfin` and {eq}`eq:PFCRRA-yfin` using {eq}`eq:PFCRRA-ibc` to obtain:

```{math}
:label: eq:PFCRRA-cfinhoriz

\cLevBF_{\tNow} = \underbrace{\left(\frac{1-[\Rfree^{-1}(\Rfree\Discount)^{1/\CRRA}]}{1-[\Rfree^{-1}(\Rfree\Discount)^{1/\CRRA}]^{\TEnd-\tNow+1}}\right)}_{\equiv \MPC_{t}} \underbrace{\left[\bLevBF_{\tNow}+\pLevBF_{\tNow}\overbrace{\left(\frac{1-({\WGro}/\Rfree)^{\TEnd-\tNow+1}}{1-({\WGro}/\Rfree)}\right)}^{\equiv \hRat_{t}}\right]}_{\equiv \oLev_{t}}
```

where {math}`\MPC_{t}` is the marginal propensity to consume (MPC) out of **o**verall (human plus nonhuman) wealth {math}`\oLev_{t}`.

In order to apply [InfSum](#fact:infsum) to move to the infinite-horizon case ({math}`\TEnd=\infty`), we need to impose the condition

```{math}
:label: eq:FHWCPF

\begin{aligned}
        {\WGro}/\Rfree & <  1
\\  {\WGro}   & <  \Rfree.
\end{aligned}
```

Why? Because if income were expected to grow at a rate greater than the interest rate forever, then the PDV of future income would be infinite; with infinite human wealth, the problem has no well-defined solution. We henceforth call {eq}`eq:FHWCPF` the Finite Human Wealth Condition (FHWC).

Similarly, if consumption starts at a positive level and grows by the factor {math}`\Pat=(\Rfree \Discount)^{1/\CRRA}`, in order for the PDV of consumption to be finite we must impose:

```{math}
:label: eq:PatR

\underbrace{\left(\frac{(\Rfree\Discount)^{1/\CRRA}}{\Rfree}\right)}_{\PatR} < 1
```

and we will henceforth call {math}`\PatR` the "return patience factor" whose log is the "return patience rate" {math}`\patr \equiv \log \PatR` ({math}`\pat` is the lower-case version of {math}`\Pat`) and what {eq}`eq:PatR` says is that the desired growth rate of consumption must be less than the interest rate in order for the model to have a well-defined solution. This condition therefore imposes a requirement that "impatience" be greater than some minimum amount. (For (much) more on the various definitions of impatience used in this section, their implications, and parallel conditions for models with uncertainty, see {cite:t}`BufferStockTheory`).

If both the RIC and the FHWC hold, then the model has a well-defined infinite horizon solution,[^conditions-fail] as can be seen by realizing that

[^conditions-fail]: See {cite:t}`BufferStockTheory` for a discussion of the case where the conditions do not hold.

```{math}
\begin{aligned}
   \lim_{\TEnd \rightarrow \infty} ({\WGro}/\Rfree)^{\TEnd-\tNow+1} & =  0
\\ \lim_{\TEnd \rightarrow \infty} (\Rfree^{-1}(\Rfree\Discount)^{1/\CRRA})^{\TEnd-\tNow+1} & = 0.
\end{aligned}
```

Substituting these zeros into {eq}`eq:PFCRRA-cfinhoriz` yields

```{math}
:label: eq:PFCRRA-cOfw

\begin{aligned}
        \cLevBF_{\tNow} & =  \left(1-\Rfree^{-1}(\Rfree\Discount)^{1/\CRRA}\right)\left[\bLevBF_{\tNow}+\left(\frac{\pLevBF_{\tNow}}{1-({\WGro}/\Rfree)}\right)\right]
\\      & =  \left(1-\Rfree^{-1}(\Rfree\Discount)^{1/\CRRA}\right)\left(\mLevBF_{\tNow}-\pLevBF_{\tNow}+\hLevBF_{\tNow}\right)
\\      & =  \underbrace{\left(\frac{\Rfree -(\Rfree\Discount)^{1/\CRRA}}{\Rfree}\right)}_{ \equiv \MPC} \oLev_{\tNow}
\end{aligned}
```

where {math}`\oLev_{\tNow}` is the consumer's "**o**verall" or "total wealth," the sum of human and nonhuman wealth, and {math}`\MPC` is the infinite-horizon marginal propensity to consume.

Now consider the question "What is the level of {math}`\cLevBF_{\tNow}` that will leave total wealth intact, allowing the same value of consumption in period {math}`t+1` and forever after (that is, allowing {math}`\cLevBF_{\tNow+n}=\cLevBF_{\tNow}~\forall~n>0`)?"

The intuitive answer is that the wealth-preserving level of spending is exactly equal to the (properly conceived) interest earnings on one's total wealth. We call this the "sustainable" level of consumption.

:::{margin}
Note that this was interpreted as "permanent income" in the 1970s and 80s, but will not be called such in this class. Point out that wealth here is exactly like an asset that yields a dividend {math}`P`.
:::

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
        \Rfree-(\Rfree\Discount)^{1/\CRRA} & >  \rfree  \\
        1-(\Rfree\Discount)^{1/\CRRA} & >  0  \\
        1 & >  (\Rfree\Discount)^{1/\CRRA}.
\end{aligned}
```

Finally, if {math}`\Rfree\Discount=1` (which is to say, the interest rate exactly offsets the time preference rate), then {math}`(\Rfree\Discount)^{1/\CRRA}=1` regardless of the value of {math}`\CRRA` so that the consumer is "poised" on the knife-edge between patience and impatience. We refer to such a consumer as "absolutely poised." Similarly, we say that a consumer for whom {math}`\PatR=1` is "return poised."

:::{margin}
Income here means inclusive of interest income on total wealth.
:::

:::{margin}
"Return impatience" guarantees a positive marginal propensity to consume; absolute impatience guarantees a falling level of consumption. If {math}`\rfree > 0`, return impatience will hold even if the consumer is "poised" with respect to absolute patience.
:::

(The consumer will be impatient, spending more than his income, if {math}`\Rfree\Discount<1`, and patient, spending less than his income, if {math}`\Rfree\Discount>1`.)

Equation {eq}`eq:PFCRRA-cOfw` can be simplified into something a bit easier to handle by making some approximations. If {math}`\Discount = 1/(1+\timeRate)`, then we can use facts from the [MathFacts section](#fact:mathfactslist) to discover that

```{math}
\begin{aligned}
      \log (\Rfree\Discount)^{1/\CRRA}/\Rfree & =  (1/\CRRA) (\log \Rfree + \log [1/(1+\timeRate) ]) - \log \Rfree  \\
     & =  (1/\CRRA) (\log(1+r) + \log 1 - \log (1+\timeRate) ) - \log \Rfree  \\
         & \approx  \CRRA^{-1}(\rfree -\timeRate)  - \rfree
\\      (\Rfree\Discount)^{1/\CRRA}/\Rfree & \approx  1+(\CRRA^{-1}(\rfree-\timeRate)-\rfree).
\end{aligned}
```

Substituting this into {eq}`eq:PFCRRA-cOfw` gives

```{math}
:label: eq:PFCRRA-capprox

\cLevBF_{\tNow} \approx \left(\rfree-\CRRA^{-1}(\rfree-\timeRate)\right)\oLev_{\tNow}.
```

From this we can see again that whether the consumer is return patient, return poised, or return impatient depends on the relationship between {math}`\rfree` and {math}`\timeRate`. Note also that if {math}`\CRRA = \infty` then the consumer is infinitely averse to changing the level of consumption, and so once again the consumer spends exactly the sustainable amount. (This consumer is "absolutely poised" but "return impatient").

Now a brief digression on what "income" means in this model. Suppose for simplicity that the consumer had no capital assets ("bank balances" {math}`\bLevBF_{\tNow}=0`), and suppose that income was expected to stay constant at level {math}`\pLevBF_{\tNow+n}=\pLevBF~\forall~n>0` forever. In this case human wealth would be:

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
\cLevBF_{\tNow} \approx \left(\rfree-\CRRA^{-1}(\rfree-\timeRate)\right)\left(\bLevBF_{\tNow}+ \pLevBF\left(\frac{\Rfree}{\rfree}\right)\right).
```

{math}`\rfree` appears three times in this equation, which correspond (in order) to the income effect, the substitution effect, and the human wealth effect. To see this, note that an increase in the first {math}`\rfree` reflects an increase in the payout rate on total wealth (set {math}`\pLevBF = 0` and refer to our formula above for {math}`\PIHMPC`, realizing that for small {math}`\rfree`, {math}`\rfree/\Rfree \approx \rfree`.) That is, it simply reflects the consequence for consumption of an increase in interest income -- so it captures the "income effect" of interest rates. The second term corresponds to the substitution effect, as can be seen from its dependence on the intertemporal elasticity of substitution {math}`\CRRA^{-1}`. Finally, the {math}`\pLevBF(\Rfree/\rfree)` term clearly corresponds to human wealth, and therefore the sensitivity of consumption to {math}`\rfree` coming through this term corresponds to the human wealth *effect*.

:::{margin}
This is why I introduced the concept of the human wealth effect in my original treatment in the Fisher diagram.
:::

## Normalizing By {math}`\pLevBF`

The whole problem can be restated more simply by "dividing through" by the level of permanent income before solving. Hereafter, nonbold variables will be the normalized bold-letter equivalent, e.g. {math}`\cRat_{\tNow}=\cLevBF_{\tNow}/\pLevBF_{\tNow}`, and note that if {math}`\pLevBF_{\tNow+1}={\WGro} \pLevBF_{\tNow}~\forall~t` then from the standpoint of date {math}`t`,

```{math}
\begin{aligned}
        \uFunc(\cLevBF_{\tNow+n}) & =  \frac{\cLevBF_{\tNow+n}^{1-\CRRA}}{1-\CRRA}  \\
         & =  \frac{(\cRat_{\tNow+n}\pLevBF_{\tNow+n})^{1-\CRRA}}{1-\CRRA}  \\
         & =  (\pLevBF_{\tNow}{\WGro}^{n})^{1-\CRRA}\frac{\cRat_{\tNow+n}^{1-\CRRA}}{1-\CRRA}
\end{aligned}
```

which means that

```{math}
:label: eq:PFCRRA-maxc2

\sum_{n=0}^{\TEnd-\tNow} \Discount^{n}\frac{\cLevBF_{\tNow+n}^{1-\CRRA}}{1-\CRRA} = \pLevBF_{\tNow}^{1-\CRRA}\sum_{n=0}^{\TEnd-\tNow} ({\WGro}^{1-\CRRA}\Discount)^{n} \frac{\cRat_{\tNow+n}^{1-\CRRA}}{1-\CRRA}.
```

Furthermore, the accumulation equations can be rewritten by dividing both sides by {math}`\pLevBF_{\tNow+1}`:

```{math}
\begin{aligned}
        \bLevBF_{\tNow+1}/\pLevBF_{\tNow+1} & =  \frac{(\mLevBF_{\tNow}-\cLevBF_{\tNow})\Rfree}{\pLevBF_{\tNow+1}}  \\
        \bRat_{\tNow+1} & =   \left(\frac{(\mLevBF_{\tNow}-\cLevBF_{\tNow})\Rfree}{\pLevBF_{\tNow}}\right)\left(\frac{\pLevBF_{\tNow}}{\pLevBF_{\tNow+1}}\right) \\
         & =  (\mRat_{\tNow}-\cRat_{\tNow})(\Rfree/{\WGro})
\end{aligned}
```

```{math}
\begin{aligned}
        \mLevBF_{\tNow+1} & =  \bLevBF_{\tNow+1}+\pLevBF_{\tNow+1}
\\      \mRat_{\tNow+1} & =  \bRat_{\tNow+1}+1.
\end{aligned}
```

Now if we define {math}`\DiscAlt \equiv {\WGro}^{1-\CRRA}\Discount` and {math}`\RnormWGro \equiv \Rfree/{\WGro}`, the original problem can be rewritten as:

```{math}
:label: eq:PFCRRA-scaledmaxprob

\max~~\pLevBF_{\tNow}^{1-\CRRA}\sum_{n=0}^{\TEnd-\tNow} \DiscAlt^{n} \uFunc(\cRat_{\tNow+n})
```

subject to the constraints

```{math}
\begin{aligned}
   \aRat_{\tNow}   & =  \mRat_{\tNow}-\cRat_{\tNow}
\\ \bRat_{\tNow+1} & =  \aRat_{\tNow}\RnormWGro
\\ \mRat_{\tNow+1} & =  \bRat_{\tNow+1}+1
\end{aligned}
```

and we can go through the same steps as above to find that the solution is

```{math}
:label: eq:normC

\cRat_{\tNow} = (1-\RnormWGro^{-1}(\RnormWGro\DiscAlt)^{1/\CRRA})\left[\mRat_{\tNow}-1+\overbrace{\left(\frac{1}{1-{1}/\RnormWGro}\right)}^{\equiv\hRat}\right]
```

subject to the "finite human wealth" condition

```{math}
\begin{aligned}
        {1} & <  \RnormWGro
\\  1 & <  \Rfree/\WGro
\end{aligned}
```

which is the same condition {eq}`eq:FHWCPF` as above, and also subject to the "return impatience condition"

```{math}
\begin{aligned}
                (\RnormWGro\DiscAlt)^{1/\CRRA} & <  \RnormWGro
\\              \left(\frac{\Rfree}{{\WGro}}\Discount {\WGro}^{1-\CRRA}\right)^{1/\CRRA} & <  \Rfree/{\WGro}
\\              (\Rfree\Discount)^{1/\CRRA} & <  \Rfree
\end{aligned}
```

which is also the same as above in {eq}`eq:PatR`.

Now note that {eq}`eq:normC` can be rewritten

```{math}
\begin{aligned}
        \cRat_{\tNow} & =  \left(\frac{\RnormWGro-(\RnormWGro\DiscAlt)^{1/\CRRA}}{\RnormWGro}\right)\oRat_{\tNow}
\\ & =  \underbrace{(1 - \PatR)}_{\equiv \MPC} \oRat_{\tNow}
\end{aligned}
```

where {math}`\oRat_{\tNow}` is the consumer's total wealth-to-permanent-labor-income ratio, and {math}`\MPC` is the "marginal propensity to consume" out of wealth.

As before, whether {math}`\oRat` is rising or falling depends upon the relationship between {math}`\RnormWGro-1` and {math}`\RnormWGro-(\RnormWGro\DiscAlt)^{1/\CRRA}`. A consumer will be drawing down his wealth-to-income ratio if

```{math}
\begin{aligned}
        \RnormWGro-(\RnormWGro\DiscAlt)^{1/\CRRA} & >  \RnormWGro-1  \\
        1-(\RnormWGro\DiscAlt)^{1/\CRRA} & >  0  \\
        1 & >  (\RnormWGro\DiscAlt)^{1/\CRRA}.
\end{aligned}
```

Now substituting the definitions of {math}`\RnormWGro` and {math}`\DiscAlt` we see that whether {math}`\oRat` is rising or falling depends on whether

```{math}
:label: eq:PatWGroCond

\begin{aligned}
        1 & >  (\frac{\Rfree}{{\WGro}}\Discount {\WGro}^{1-\CRRA})^{1/\CRRA}
\\  1 & >  (\Rfree\Discount {\WGro}^{-\CRRA})^{1/\CRRA}
\\  1 & >  \underbrace{\left(\frac{(\Rfree\Discount)^{1/\CRRA}}{\WGro}\right)}_{\PatWGro},
\end{aligned}
```

where {math}`\PatWGro` is the "growth patience factor." We call {eq}`eq:PatWGroCond` the "growth impatience condition" (GIC),[^gic-pf] and we say that the consumer is "growth impatient" if {eq}`eq:PatWGroCond` holds.

[^gic-pf]: Or, GIC-PF if we want to highlight that this is the condition for the perfect foresight model.

Thus, whether the consumer is patient or impatient in the sense of building up or drawing down a wealth-to-income *ratio* depends on whether the growth rate of labor income is less than, equal to, or greater than the growth rate of consumption. Analogously to our earlier usages, a consumer for whom {math}`\PatWGro=1` (equivalently, {math}`\patwGro= 0`) would be "growth poised."

To get the intuition for this, consider the case of a consumer with no nonhuman wealth, {math}`\bRat_{\tNow}=0`. This consumer's absolute level of consumption will grow at {math}`(\Rfree\Discount)^{1/\CRRA}` and absolute level of income grows at {math}`{\WGro}`, but the PDV of future consumption and future income must be equal. If income is growing faster than consumption but has the same PDV, consumption must be *starting out* at a level *higher* than income - which is the sense in which this consumer is impatient (spending more than his income). "Growth impatience" is therefore the condition that causes consumers with no assets to want to borrow.

## Applications

(subsec:HWEffect)=
### How Large is the Human Wealth Effect?

We can now apply the model to answer our first useful question: How large does the model imply the "human wealth effect" is?

For simplicity, assume that {math}`\bRat_{\tNow} = 0`. Then the original version of the approximate formula {eq}`eq:PFCRRA-capprox` tells us that the *level* of consumption will be given by:

```{math}
:label: eq:PFCRRA-cofw2

\begin{aligned}
        \cLevBF_{\tNow} & \approx  \left(\rfree - \CRRA^{-1}(\rfree-\timeRate)\right)\left(\frac{\pLevBF_{\tNow}}{1-{\WGro}/\Rfree}\right)  \\
         & \approx  \left(\rfree - \CRRA^{-1}(\rfree-\timeRate)\right)\left(\frac{\pLevBF_{\tNow}}{\rfree-\wGro}\right).
\end{aligned}
```

We are interested only in calibrations of the model in which the consumer is "growth impatient" so that {math}`\wGro > \CRRA^{-1}(\rfree-\DiscRate)` so if we define the rate of growth impatience as

```{math}
:label: eq:patwGro

\patwGro \equiv \CRRA^{-1}(\rfree-\DiscRate)-\wGro
```

we can write this as

```{math}
:label: eq:CvsP

\begin{aligned}
        \cLevBF_{\tNow} & \approx  \pLevBF_{\tNow} \left(\frac{\rfree - (\wGro+\patwGro)}{\rfree-\wGro}\right)
\\ & =  \pLevBF_{\tNow} \left(1 - \patwGro/(\rfree - \wGro)\right).
\end{aligned}
```

Remembering that imposition of the growth impatience condition is equivalent to assuming {math}`\patwGro < 0`, while the FHWC requires {math}`\rfree > \wGro`, it is clear that the expression {math}`-\patwGro/(\rfree-\wGro)` will be positive: The consumer will spend more than his permanent labor income.

Now suppose we choose plausible values for {math}`(\rfree, \timeRate, \wGro, \CRRA) = (0.04,0.04,0.02,2)`. Then {eq}`eq:PFCRRA-cofw2` becomes:

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

The point of this example is that for plausible parameter values, the human wealth effect is enormously stronger than the income and substitution effects, so that we should see large drops in consumption when interest rates rise and conversely strong gains when interest rates fall. This is a summary of the main point of the famous paper by {cite:t}`summersCapTax`; Summers derives formulas for an economy with overlapping generations of finite-lifetime consumers, but those complications do not change the basic message.

### How Does the Saving Rate Respond to Interest Rates?

The level of saving can be defined as total income minus total consumption:

```{math}
\sLevBF_{\tNow} \approx \rfree \aLevBF_{\tNow-1} + \pLevBF_{\tNow} - \cLevBF_{\tNow}
```

but substituting from {eq}`eq:CvsP` and {eq}`eq:PFCRRA-capprox`,

```{math}
:label: eq:cFromHandB

\cLevBF_{t} \approx \pLevBF_{\tNow} \left(1 - \patwGro/(\rfree - \wGro)\right)+(\rfree-\CRRA^{-1}(\rfree-\DiscRate))\bLevBF_{\tNow}
```

this can be rewritten as

```{math}
\begin{aligned}
 \sLevBF_{\tNow} & \approx  \rfree \aLevBF_{\tNow-1} + \pLevBF_{\tNow}- \pLevBF_{\tNow} \left(1 - \patwGro/(\rfree - \wGro)\right) - (\rfree-\CRRA^{-1}(\rfree-\DiscRate))\Rfree \aLevBF_{\tNow-1}
\\ & =  \rfree \aLevBF_{\tNow-1} + \pLevBF_{\tNow} \patwGro/(\rfree - \wGro)- (\rfree-\CRRA^{-1}(\rfree-\DiscRate))\Rfree\aLevBF_{\tNow-1}
\\ \sRat_{\tNow} & \approx  \rfree \aRat_{\tNow-1} + \patwGro/(\rfree - \wGro)- (\rfree-\CRRA^{-1}(\rfree-\DiscRate))\Rfree \aRat_{\tNow-1}
\\ & \approx  \patwGro/(\rfree - \wGro)+ \CRRA^{-1}(\rfree-\DiscRate)\aRat_{\tNow-1}
\end{aligned}
```

(where the last approximations come from the assumptions that {math}`1/G \approx 1`) and that {math}`\rfree \times (\rfree-\CRRA^{-1}(\rfree-\DiscRate))` is "small." The saving *rate* (for which we use the letter {math}`\srate` to distinguish it from {math}`\sRat` above) is the ratio of saving to *total* income (not just labor income):

```{math}
\varsigma_{\tNow} = \left(\frac{\patwGro/(\rfree - \wGro)+ \CRRA^{-1}(\rfree-\DiscRate)\aRat_{\tNow-1}}{1+ \rfree \aRat_{\tNow-1}}\right).
```

The first thing to notice about this expression is that as {math}`\aRat_{\tNow-1}` approaches infinity, the saving rate asymptotes to

```{math}
\varsigma_{\tNow} \approx \left(\frac{\CRRA^{-1}(\rfree-\DiscRate)}{\rfree}\right)
```

and whether the saving rate is positive or negative depends on whether the consumer is absolutely impatient, absolutely poised, or absolutely patient.[^partial-eq]

[^partial-eq]: In this partial equilibrium framework, we are assuming that the consumer's wealth can go to infinity without any effect on the aggregate interest rate.

Finally, if we rewrite this as

```{math}
\varsigma \approx \CRRA^{-1} (1 - \timeRate \rfree^{-1})
```

then it is apparent that the response of the saving rate to the interest rate is

```{math}
:label: eq:dsdr

\left(\frac{d \varsigma}{d \rfree}\right) = \CRRA^{-1}\timeRate \rfree^{-2}.
```

If we consider almost any plausible configuration of parameter values, say {math}`\rfree = \timeRate=0.05` and {math}`\CRRA = 2`, this translates to a very large response of the saving rate with respect to {math}`\rfree` (in the case of the parameter values mentioned above, {math}`(1/2)(20)=10`).

## Appendix

(sec:PFwhenFHWfails)=
### The Limiting Solution to the Perfect Foresight Model if the FHWC Fails

#### When the RIC Holds

Consider first a circumstance in which the RIC holds ({math}`\PatR<1`). In this case, the perfect foresight unconstrained model does not have a sensible solution because human wealth is infinite while the model implies that the optimal policy is to consume a positive proportion of human wealth. {math}`\cFunc(\mRat)=\infty~\forall~\mRat` is not a useful (or plausible!) solution.

#### When the RIC Fails

The alternative case is when the RIC fails ({math}`\PatR=1`). Here, the only way to make sense of the model is to think about the limit of the finite horizon model as the horizon extends to infinity. This is because behavior reflects a competition between two pathologies that characterize the infinite horizon solution: It exhibits a limiting MPC of zero out of total wealth, which includes human wealth -- which approaches infinity. A limiting solution of {math}`\cFunc(\mRat) = 0 \times \infty` is even less useful than {math}`\cFunc(\mRat) = \infty`!

It turns out that the limiting solution is not ambiguous, however. The finite horizon solution implies that consumption out of human wealth when the end of life is {math}`n` periods in the future is

```{math}
\MPC_{n} \hRat_{n} = \left(\frac{(\Rfree^{-1}{\WGro})^{{n}+1}-1}{[\Rfree^{-1}(\Rfree\Discount)^{1/\CRRA}]^{{n}+1}-1}\right)
```

whose limit is given by

```{math}
\begin{aligned}
\lim_{{n} \uparrow \infty} \MPC_{n} \hRat_{n} & =  \lim_{n \uparrow \infty} \left(\frac{(\Rfree^{-1}{\WGro})^{{n}+1}}{[\Rfree^{-1}(\Rfree\Discount)^{1/\CRRA}]^{{n}+1}}\right)
\\ & =  \lim_{n \uparrow \infty} \left(\frac{1}{\PatWGro^{(n+1)}}\right)
\\ & =  \infty
\end{aligned}
```

since if the FHWC condition fails ({math}`\WGro > \Rfree`) then if the RIC {math}`\Pat/\Rfree < 1` holds, the GIC {math}`\Pat < \WGro` must hold, which guarantees {math}`\PatWGro < 1` so that {math}`\PatWGro^{n+1}` approaches zero as {math}`n \uparrow \infty`.

(Useful-Analytical-Results)=
### Useful Analytical Results

Given the result from {eq}`eq:PFCRRA-cgrow` that

```{math}
c_{t+n} = \Pat^{n} c_{t}
```

we can rewrite the value function as

```{math}
\begin{aligned}
  v_{\tNow} & =  \uFunc(c_{t}) + \DiscFac \uFunc(c_{t}\Pat) + \DiscFac^{2} \uFunc(c_{t} \Pat^{2}) + ...
  \\ & =  (1-\CRRA)^{-1}\left(c_{t}^{1-\CRRA} + \DiscFac (c_{t}\Pat)^{1-\CRRA} + \DiscFac^{2} (c_{t} \Pat^{2})^{1-\CRRA} + ...\right)
  \\ & =  (1-\CRRA)^{-1}\left(c_{t}^{1-\CRRA}(1+\DiscFac \Pat^{1-\CRRA} + \left(\DiscFac \Pat^{1-\CRRA})^{2} + ... \right) \right)
\\ & =  \uFunc(c_{t})\left(1+\DiscFac \Pat^{1-\CRRA} + (\DiscFac \Pat^{1-\CRRA})^{2} + ... \right)
\end{aligned}
```

but since {math}`\DiscFac \Pat^{1-\CRRA} = \PatR`,[^patr-derivation]

[^patr-derivation]:
    ```{math}
    \begin{aligned}
      \DiscFac \Pat^{1-\CRRA} & =  \DiscFac (\Rfree \DiscFac)^{\frac{1-\CRRA}{\CRRA}}
      \\ & =                               \DiscFac (\Rfree \DiscFac)^{1/\CRRA-1}
      \\ & =             (\Rfree \DiscFac)^{1/\CRRA} / \Rfree
               \\ & =  \PatR
    \end{aligned}
    ```

this reduces to

```{math}
:label: eq:vFuncAnalytical

v_{t} = \uFunc(c_{t})\overbrace{(1+\PatR+\PatR^{2}+...+\PatR^{T-t})}^{\equiv \cPDVFunc_{t}}
```

where {math}`\cPDVFunc_{t}` is the discounted value of future consumption growth (that is, the discounted value of the ratio of future consumption to today's consumption).

{cite:t}`BufferStockTheory` shows ([in an appendix](http://www.econ2.jhu.edu/people/ccarroll/papers/BufferStockTheory/#MPCnvrsIsCPDV)) that {math}`\cPDVFunc_{t} = \MPC_{t}^{-1}`, which means that we can write value as

```{math}
\begin{aligned}
  v_{t} & =  \uFunc(c_{t})\MPC^{-1}_{t}
  \\ & =  \left(\frac{(\oRat_{t}\MPC_{t})^{1-\CRRA}}{1-\CRRA}\right)\MPC_{t}^{-1}
\\ & =  \uFunc(\oRat_{t})\MPC_{t}^{-\CRRA}
\end{aligned}
```

### Additional Derivations

If consumption is simply a function of overall wealth bank balances {math}`\oRat_{t}`, we can derive a convenient recursive formula for the inverse of the MPC:

```{math}
:label: eq:MPCrecursive

\begin{aligned}
  \uFunc^{\prime}(\MPC_{t} \oRat_{t}) & = \Rfree \DiscFac \uFunc^{\prime}(\MPC_{t+1}\overbrace{\oRat_{t}(1-\MPC_{t})\Rfree}^{\oRat_{t+1}})
\\ \MPC_{t} \oRat_{t} & = (\Rfree \DiscFac)^{-1/\CRRA} \MPC_{t+1}\oRat_{t}(1-\MPC_{t}) \Rfree
\\ \underbrace{\Rfree^{-1} (\Rfree \DiscFac)^{1/\CRRA}}_{\PatR} \MPC_{t}  & =  \MPC_{t+1}(1-\MPC_{t})
\\ (\PatR \MPC_{t})^{-1}  & =  \MPC_{t+1}^{-1}(1-\MPC_{t})^{-1}
\\ (1-\MPC_{t}) \MPC_{t}^{-1}  & = \PatR  \MPC_{t+1}^{-1}
\\ \MPC_{t}^{-1}-1  & = \PatR  \MPC_{t+1}^{-1}
\\ \MPC_{t}^{-1}  & = 1+\PatR  \MPC_{t+1}^{-1}
\end{aligned}
```

which implies that if the MPC in the last period {math}`T` is {math}`\MPC_{T}=1` then from any date {math}`t \leq T` we can write

```{math}
:label: eq:MPCrecursiveSum

\MPC_{t}^{-1} = 1 + \PatR + \PatR^{2} + ... + \PatR^{T-t}.
```

But the series on the RHS in {eq}`eq:vFuncAnalytical` and {eq}`eq:MPCrecursiveSum` are identical! So {math}`\MPC^{-1}_{t} = \cPDVFunc_{t}`, and we can equivalently write

```{math}
v_{t} = \uFunc(c_{t})\MPC^{-1}_{t}.
```

Now note that if we define a utility-inverse of the value function as {math}`\vInv \equiv \left((1-\CRRA) \vFunc\right)^{1/(1-\CRRA)}`, then consumption exceeds its minimum possible value at {math}`\underline{\mRat}` (where consumption exceeds {math}`\cFunc(\underline{\mRat})=0`) by {math}`c_{t}=\MPC_{t}(\mRat-\underline{m})`:

```{math}
\begin{aligned}
  \vInv_{t}(m) &= \MPC_{t}(\mRat_{t}-\underline{m}_{t}) \MPC_{t}^{-1/(1-\CRRA)}
  \\ & = (m - \underline{m})\MPC^{((1-\CRRA)/(1-\CRRA)-1/(1-\CRRA))}
  \\ & = (m - \underline{m})\MPC^{-\CRRA/(1-\CRRA)}
\end{aligned}
```

which is linear, and makes it very easy to compute

```{math}
\vFunc_{t}(\mRat) = \uFunc\left((m-\underline{m})\MPC_{t}^{-\CRRA/(1-\CRRA)}\right)
```
