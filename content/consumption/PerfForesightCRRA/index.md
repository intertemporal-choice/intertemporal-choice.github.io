(sec:PerfForesightCRRA)=
# Consumption Under Perfect Foresight and CRRA Utility

The perfect foresight (PF) model with [CRRA](#eq:crrautil) utility is the benchmark for the remaining consumption models. It has a closed-form solution, so every question has an exact answer: how much the consumer spends out of wealth, whether spending rises or falls over time, and how both respond to the interest rate.

:::{margin}
Two Econ-ARK DemARK notebooks provide computational versions: [How Close Is HARK's Infinite-Horizon Solution?](https://econ-ark.github.io/DemARK/perfforesightcrra-convergence/) measures how a solution found by backward iteration approaches the exact formulas, and [Perfect Foresight CRRA Model - Saving Rate](https://econ-ark.github.io/DemARK/perfforesightcrra-savingrate/) computes the saving rate with HARK.
:::

Four conditions organize the answers. The [absolute impatience condition](#eq:AIC) decides whether the level of consumption falls, the [return impatience condition](#eq:PatR) makes the marginal propensity to consume positive, the [finite human wealth condition](#eq:FHWCPF) makes the present value of future income finite, and the [growth impatience condition](#eq:PatWGroCond) decides whether a consumer with no [market assets](#eq:PFCRRA-maxprob) borrows. We derive the solution and the conditions, then apply them to two questions about interest rates: how much consumption responds through the value of future income, and how the saving rate responds. The answers are larger than the evidence supports, and the reasons motivate the later models of uncertainty and liquidity constraints.

## The Problem

Here we solve the problem of a PF consumer with intertemporally separable CRRA utility {math}`\uFunc(\bullet)= \bullet^{1-\CRRA}/(1-\CRRA)` who discounts future utility geometrically by {math}`\DiscFac` per period. The finite horizon solution, whose last period is {math}`\TEnd`, extends to the infinite horizon case if intuitive "impatience" and "finite human wealth" conditions hold.

The problem:

```{math}
:label: eq:PFCRRA-maxprob

\max \sum_{n=0}^{\TEnd-\tNow} \DiscFac^{n} \uFunc(\cLvl_{\tNow+n})
```

subject to these constraints, where bank balances {math}`\bLvl`, the consumer's market assets, are everything held at the start of the period apart from labor income:

```{math}
\begin{aligned}
      \aLvl_{\tNow}   & =  \mLvl_{\tNow}-\cLvl_{\tNow}
\\    \bLvl_{\tNow+1} & =  \aLvl_{\tNow}\Rfree
\\    \mLvl_{\tNow+1} & =  \bLvl_{\tNow+1}+\pLvl_{\tNow+1}
\end{aligned}
```

where {math}`\pLvl_{\tNow+1}` is "permanent labor income," which always grows by {math}`\PermGroFac`:

```{math}
\pLvl_{\tNow+1}/\pLvl_{\tNow} = {\PermGroFac}.
```

Here {math}`\Rfree = 1+\rfree` is the interest factor and {math}`\PermGroFac = 1+\PermGroRte` the growth factor of permanent income.

The consumer can borrow or lend any amount at the interest factor {math}`\Rfree`, against future income as well as current resources, but cannot die in debt: {math}`\aLvl_{\TEnd} \geq 0`. Leaving resources unspent gains nothing, so it binds: {math}`\aLvl_{\TEnd} = 0`. In the infinite-horizon case it becomes the no-Ponzi condition {math}`\lim_{n \rightarrow \infty} \Rfree^{-n}\aLvl_{\tNow+n} \geq 0`, which binds for the same reason. Throughout, {math}`\CRRA \neq 1`; logarithmic utility is the limit as {math}`\CRRA \rightarrow 1`.

## The Solution

It will be convenient to think of both market resources {math}`\mLvl_{\tNow}` and permanent noncapital (labor) income {math}`\pLvl_{\tNow}` as state variables in this problem. Bellman's equation is

:::{margin}
Bellman's equation relates {math}`\vFunc_{\tNow}` and {math}`\vFunc_{\tNow+1}` through the controls and the states, so it does not necessarily require writing out the budget constraint.
:::

```{math}
:label: eq:PFCRRA-vmax

\vFunc_{\tNow}(\mLvl_{\tNow},\pLvl_{\tNow}) = \max_{\cLvl_{\tNow}} \left\{ \uFunc(\cLvl_{\tNow}) + \DiscFac \vFunc_{\tNow+1}\left(\overbrace{(\mLvl_{\tNow}-\cLvl_{\tNow})\Rfree+\pLvl_{\tNow+1}}^{=\mLvl_{\tNow+1}},\pLvl_{\tNow+1}\right)\right\}.
```

The first-order condition is

```{math}
:label: eq:upeqrbv

\uFunc^{\prime}(\cLvl_{\tNow}) = \DiscFac \left(\Rfree \vFunc_{\tNow+1}^{\mLvl}(\mLvl_{\tNow+1},\pLvl_{\tNow+1})-\overbrace{\frac{d\pLvl_{\tNow+1}}{d \cLvl_{\tNow}}}^{=0}\vFunc_{\tNow+1}^{\pLvl}(\mLvl_{\tNow+1},\pLvl_{\tNow+1})\right),
```

and the [Envelope theorem](#sec:Envelope) tells us that

```{math}
:label: eq:vpeqrbv

\vFunc_{\tNow}^{\mLvl}(\mLvl_{\tNow},\pLvl_{\tNow}) = \Rfree \DiscFac \vFunc_{\tNow+1}^{\mLvl}(\mLvl_{\tNow+1},\pLvl_{\tNow+1}).
```

The two right-hand sides are the same, so

```{math}
\vFunc_{\tNow}^{\mLvl}(\mLvl_{\tNow},\pLvl_{\tNow}) = \uFunc^{\prime}(\cLvl_{\tNow})
```

and likewise {math}`\vFunc_{\tNow+1}^{\mLvl}(\mLvl_{\tNow+1},\pLvl_{\tNow+1})=\uFunc^{\prime}(\cLvl_{\tNow+1})`, which, substituted into {eq}`eq:vpeqrbv`, gives the Euler equation for consumption:

:::{margin}
The second line follows from the first with CRRA marginal utility, as in the [two-period model](#eq:c1euler).
:::

```{math}
:label: eq:PFCRRA-cgrow

\begin{aligned}
        \uFunc^{\prime}(\cLvl_{\tNow}) & =  \Rfree\DiscFac \uFunc^{\prime}(\cLvl_{\tNow+1})
\\  \left(\frac{\cLvl_{\tNow+1}}{\cLvl_{\tNow}}\right) & =  \underbrace{(\Rfree\DiscFac)^{1/\CRRA}}_{\equiv \APFac}.
\end{aligned}
```

Thus, consumption grows every period by {math}`\APFac`, where we use the Old English letter {math}`\APFac` to measure what we will call the "absolute patience" factor. Specifically, if

```{math}
:label: eq:AIC

\APFac < 1
```

the consumer is "absolutely impatient": consumption falls, and what better definition of impatience is there than spending so much now that you must cut spending later? If {math}`\APFac > 1` the consumer is "absolutely patient," deferring resources to make consumption grow.

Combining the constraints from {math}`\tNow` to {math}`\TEnd` with {math}`\aLvl_{\TEnd}=0` gives the intertemporal budget constraint: the present discounted value (PDV) of consumption equals the PDV of total resources:

```{math}
:label: eq:PFCRRA-ibc

\PDV_{\tNow}^{\TEnd}(\cLvl) = \bLvl_{\tNow}+\PDV_{\tNow}^{\TEnd}(\pLvl).
```

The PDV of labor income, "human wealth" {math}`\hLvl_{\tNow}`, is

:::{margin}
The last line follows from the middle one by Fact [FinSum](#fact:finsum), the formula for a finite geometric sum.
:::

```{math}
:label: eq:PFCRRA-yfin

\begin{aligned}
        \hLvl_{\tNow} = \PDV_{\tNow}^{\TEnd}(\pLvl) & =  \sum_{n=0}^{\TEnd-\tNow} \Rfree^{-n}\pLvl_{\tNow+n}
\\       & =  \pLvl_{\tNow}\sum_{n=0}^{\TEnd-\tNow} \overbrace{\Rfree^{-n}{\PermGroFac}^{n}}^{=({\PermGroFac}/\Rfree)^{n}}
\\   & =  \pLvl_{\tNow}\left(\frac{1-({\PermGroFac}/\Rfree)^{\TEnd-\tNow+1}}{1-({\PermGroFac}/\Rfree)}\right)
\end{aligned}
```

while, using [the Euler equation for consumption](#eq:PFCRRA-cgrow), the PDV of consumption is

```{math}
:label: eq:cfin

\begin{aligned}
        \PDV_{\tNow}^{\TEnd}(\cLvl) & =  \sum_{n=0}^{\TEnd-\tNow} \Rfree^{-n}\cLvl_{\tNow+n}
\\       & =  \sum_{n=0}^{\TEnd-\tNow} \Rfree^{-n}\cLvl_{\tNow}((\Rfree\DiscFac)^{1/\CRRA})^{n} = \cLvl_{\tNow} \sum_{n=0}^{\TEnd-\tNow} [\overbrace{\Rfree^{-1}(\Rfree\DiscFac)^{1/\CRRA}}^{\equiv \RPFac}]^{n}
\\   & =  \cLvl_{\tNow}\left(\frac{1-\RPFac^{\TEnd-\tNow+1}}{1-\RPFac}\right).
\end{aligned}
```

(cFuncAnalytical)=
We can solve the model by combining {eq}`eq:cfin` and {eq}`eq:PFCRRA-yfin` using {eq}`eq:PFCRRA-ibc`:

```{math}
:label: eq:PFCRRA-cfinhoriz

\cLvl_{\tNow} = \underbrace{\left(\frac{1-\RPFac}{1-\RPFac^{\TEnd-\tNow+1}}\right)}_{\equiv \MPC_{t}} \underbrace{\left[\bLvl_{\tNow}+\pLvl_{\tNow}\overbrace{\left(\frac{1-({\PermGroFac}/\Rfree)^{\TEnd-\tNow+1}}{1-({\PermGroFac}/\Rfree)}\right)}^{\equiv \hNrm_{t}}\right]}_{\equiv \oLvl_{t}}
```

where {math}`\MPC_{t}` is the marginal propensity to consume (MPC) out of **o**verall (human plus nonhuman) wealth {math}`\oLvl_{t}`.

[Human wealth](#eq:PFCRRA-yfin) includes the current period's income: its sum starts at {math}`n=0`. End-of-period human wealth {math}`\hNrmEnd_{t}`, a ratio to {math}`\pLvl_{\tNow}`, leaves it out:

```{math}
:label: eq:PFCRRA-hEnd

\hNrmEnd_{t} \equiv \hNrm_{t}-1 = \sum_{n=1}^{\TEnd-\tNow} ({\PermGroFac}/\Rfree)^{n} = ({\PermGroFac}/\Rfree)\left(\frac{1-({\PermGroFac}/\Rfree)^{\TEnd-\tNow}}{1-({\PermGroFac}/\Rfree)}\right),
```

which approaches {math}`({\PermGroFac}/\Rfree)/(1-{\PermGroFac}/\Rfree)` as {math}`\TEnd \rightarrow \infty` when the [finite human wealth condition](#eq:FHWCPF) below holds.

:::{margin}
The closed forms divide by zero in two cases; the sums give the answer. If {math}`(\Rfree\DiscFac)^{1/\CRRA}=\Rfree`, every term of the sum in [the PDV of consumption](#eq:cfin) is 1, so {math}`\MPC_{t}=1/(\TEnd-\tNow+1)`. If {math}`\PermGroFac=\Rfree`, every term of the human wealth sum is 1, so {math}`\hNrm_{t}=\TEnd-\tNow+1` and {math}`\hNrmEnd_{t}=\TEnd-\tNow`.
:::

To apply [InfSum](#fact:infsum) as {math}`\TEnd \rightarrow \infty`, we need

```{math}
:label: eq:FHWCPF

\begin{aligned}
        {\PermGroFac}/\Rfree & <  1
\\  {\PermGroFac}   & <  \Rfree.
\end{aligned}
```

If income grew faster than the interest rate forever, human wealth would be infinite, and the problem would have no well-defined solution. We call {eq}`eq:FHWCPF` the finite human wealth condition (FHWC).

:::{margin}
[InfSum](#fact:infsum) is the immediate implication of [FinSum](#fact:finsum) as {math}`\TEnd \rightarrow \infty`.
:::

Similarly, if consumption starts at a positive level and grows by {math}`\APFac=(\Rfree \DiscFac)^{1/\CRRA}`, in order for the PDV of consumption to be finite we must impose:

```{math}
:label: eq:PatR

\underbrace{\left(\frac{(\Rfree\DiscFac)^{1/\CRRA}}{\Rfree}\right)}_{\RPFac} < 1
```

and we call {math}`\RPFac` the "return patience factor," whose log is the "return patience rate" {math}`\patr \equiv \log \RPFac` ({math}`\pat` is the lower-case version of {math}`\APFac`). That is, consumption must grow at a rate lower than the interest rate for a well-defined solution: "impatience" must exceed a minimum.

:::{margin}
For much more on these conditions and their counterparts under uncertainty, see {cite:t}`BufferStockTheoryRR`.
:::

We call {eq}`eq:PatR` the "return impatience condition" (RIC).

If the RIC and the FHWC both hold, the model has a well-defined infinite-horizon solution, because

:::{margin}
The [appendix](#sec:PerfForesightCRRA-Appendix) derives [the limiting solution when they do not](#sec:PFwhenFHWfails); see {cite:t}`BufferStockTheoryRR` for a fuller discussion.
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
        \cLvl_{\tNow} & =  \left(1-\Rfree^{-1}(\Rfree\DiscFac)^{1/\CRRA}\right)\left[\bLvl_{\tNow}+\left(\frac{\pLvl_{\tNow}}{1-({\PermGroFac}/\Rfree)}\right)\right]
\\      & =  \left(1-\Rfree^{-1}(\Rfree\DiscFac)^{1/\CRRA}\right)\left(\mLvl_{\tNow}-\pLvl_{\tNow}+\hLvl_{\tNow}\right)
\\      & =  \underbrace{\left(\frac{\Rfree -(\Rfree\DiscFac)^{1/\CRRA}}{\Rfree}\right)}_{ \equiv \MPC} \oLvl_{\tNow}
\end{aligned}
```

where {math}`\oLvl_{\tNow}` is total wealth and {math}`\MPC` is the infinite-horizon MPC.

What level of {math}`\cLvl_{\tNow}` leaves total wealth intact, so the same consumption is possible forever ({math}`\cLvl_{\tNow+n}=\cLvl_{\tNow}~\forall~n>0`)?

Intuitively, the (properly conceived) interest earnings on total wealth: the "sustainable" level of consumption. The literature of the 1970s and 80s called it "permanent income," a term reserved here for {math}`\pLvl`. Wealth in this framework behaves exactly like an asset that pays {math}`\pLvl` each period.

Under PF, human wealth is like any other wealth, so we can work with total wealth {math}`\oLvl` to find the sustainable level of spending. If the consumer spends fraction {math}`\PIHMPC` of total wealth each period, the {math}`\PIHMPC` that leaves wealth intact solves

```{math}
:label: eq:PIHMPC

\begin{aligned}
        \oLvl_{\tNow+1} & =  (\oLvl_{\tNow}-\cLvl_{\tNow})\Rfree
\\  \bar\oLvl & =  (\bar\oLvl-\PIHMPC \bar\oLvl)\Rfree
\\      1 & =  (1-\PIHMPC)  \Rfree
\\  \PIHMPC & =  1-1/\Rfree = \left(\frac{\Rfree -1}{\Rfree}\right) = \rfree/\Rfree.
\end{aligned}
```

Thus, the consumer can spend only the interest earnings {math}`\rfree` on wealth, divided by the return factor {math}`\Rfree`. (The division by {math}`\Rfree` reflects the interest that today's spending forgoes.)

The coefficient on total wealth in {eq}`eq:PFCRRA-cOfw` is also divided by {math}`\Rfree`. Thus, whether the consumer is spending more than the sustainable amount, exactly the sustainable amount, or less than the sustainable amount depends upon whether the numerator in {eq}`eq:PFCRRA-cOfw` is greater than, equal to, or less than {math}`\rfree`. As noted before, the consumer will be "absolutely impatient" if

```{math}
\begin{aligned}
        \Rfree-(\Rfree\DiscFac)^{1/\CRRA} & >  \rfree  \\
        1-(\Rfree\DiscFac)^{1/\CRRA} & >  0  \\
        1 & >  (\Rfree\DiscFac)^{1/\CRRA}.
\end{aligned}
```

Finally, if {math}`\Rfree\DiscFac=1`, the interest rate exactly offsets the time preference rate and {math}`(\Rfree\DiscFac)^{1/\CRRA}=1` whatever {math}`\CRRA`: the consumer, on the knife-edge between patience and impatience, is "absolutely poised." Similarly, a consumer for whom {math}`\RPFac=1` is "return poised."

The two conditions do different work: return impatience guarantees a positive MPC, absolute impatience a falling level of consumption. Whenever {math}`\rfree > 0`, return impatience holds even for a consumer who is poised with respect to absolute patience.

(The consumer will be impatient, spending more than income, if {math}`\Rfree\DiscFac<1`, and patient, spending less than income, if {math}`\Rfree\DiscFac>1`. Income here means income inclusive of the interest earnings on total wealth.)

Approximations make {eq}`eq:PFCRRA-cOfw` easier to handle. If {math}`\DiscFac = 1/(1+\discRte)`, facts from the [MathFacts section](#fact:mathfactslist) give

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

\cLvl_{\tNow} \approx \left(\rfree-\CRRA^{-1}(\rfree-\discRte)\right)\oLvl_{\tNow}.
```

Since {math}`\patr \equiv \log \RPFac`, the approximation just made is a formula for the return patience rate,

```{math}
:label: eq:patrApprox

\patr \approx \CRRA^{-1}(\rfree-\discRte)-\rfree,
```

and the MPC in {eq}`eq:PFCRRA-capprox` is {math}`\MPC \approx -\patr`: the RIC, {math}`\patr<0`, is what makes it positive.

The consumption function {eq}`eq:PFCRRA-cOfw` is exact; {eq}`eq:PFCRRA-capprox` treats {math}`\rfree`, {math}`\discRte` and {math}`\patr` as small, and its error differs from a numerical solution's, which approaches the exact formula, not the approximation.

From this we can see again that whether the consumer is absolutely patient, absolutely poised, or absolutely impatient depends on the relationship between {math}`\rfree` and {math}`\discRte`. If {math}`\CRRA = \infty`, consumption never changes, so the consumer spends exactly the sustainable amount: absolutely poised, but return impatient.

Now a brief digression on what "income" means in this model. Suppose for simplicity that the consumer had no capital assets ("bank balances" {math}`\bLvl_{\tNow}=0`), and suppose that income was expected to stay constant at level {math}`\pLvl_{\tNow+n}=\pLvl~\forall~n\geq 0` forever. In this case human wealth would be:

```{math}
\begin{aligned}
        \hLvl_{\tNow} & = \pLvl+\pLvl/\Rfree+\pLvl/\Rfree^{2}+\ldots  \\
         & = \pLvl(1+1/\Rfree+1/\Rfree^{2}+\ldots)  \\
         & = \pLvl\left(\frac{1}{1-1/\Rfree}\right)
\\   & = \pLvl\left(\frac{\Rfree}{\Rfree -1}\right) = \pLvl\left(\frac{\Rfree}{\rfree}\right).
\end{aligned}
```

We found in equation {eq}`eq:PIHMPC` that the level of consumption that leaves "wealth" {math}`\oLvl_{\tNow}` intact was

```{math}
\begin{aligned}
        \cLvl_{\tNow} & =  \left(\frac{\rfree}{\Rfree}\right) \oLvl_{\tNow}  \\
         & =  \left(\frac{\rfree}{\Rfree}\right) (\underbrace{\bLvl_{\tNow}}_{=0}+\hLvl_{\tNow}) \\
                        & =  \left(\frac{\rfree}{\Rfree}\right)     \pLvl \left(\frac{\Rfree}{\rfree}\right)\\
                        & =  \pLvl.
\end{aligned}
```

So in this case, spending the "interest income on human wealth" corresponds to spending exactly your labor income. This is less mysterious if income {math}`\pLvl_{\tNow}` is the "return" on human capital worth {math}`\hLvl_{\tNow}`: spending the interest on capitalized income is spending the income itself.

With constant {math}`\pLvl` we can rewrite {eq}`eq:PFCRRA-capprox` as

```{math}
\cLvl_{\tNow} \approx \left(\rfree-\CRRA^{-1}(\rfree-\discRte)\right)\left(\bLvl_{\tNow}+ \pLvl\left(\frac{\Rfree}{\rfree}\right)\right).
```

{math}`\rfree` appears in three expressions of this equation. In order, the three are the income effect, the substitution effect and the human wealth effect, as the [two-period model](#sec:2PeriodLCModel) defines them. The first two are inside the MPC out of total wealth, so they are the effects of {math}`\rfree` on consumption for a given total wealth {math}`\bLvl_{\tNow}+\hLvl_{\tNow}`. An increase in the first {math}`\rfree` raises the payout rate on total wealth (set {math}`\pLvl = 0` and use {eq}`eq:PIHMPC` for {math}`\PIHMPC`, with {math}`\rfree/\Rfree \approx \rfree` for small {math}`\rfree`): this is the income effect. The second is the substitution effect, as its dependence on the intertemporal elasticity of substitution {math}`\CRRA^{-1}` shows. The third, in {math}`\pLvl(\Rfree/\rfree)`, is the human wealth effect: the effect of {math}`\rfree` on human wealth itself, which comes from the budget constraint and involves no preference parameter.

Bank balances {math}`\bLvl_{\tNow}` are in none of the three; they are part of the total wealth that the MPC applies to. Because consumption depends on {math}`\bLvl_{\tNow}` and {math}`\hLvl_{\tNow}` only through their sum, this formula, like the two-period model, assumes the consumer can borrow against future income at no penalty. [How Large is the Human Wealth Effect?](#subsec:HWEffect) measures what the human wealth effect does to consumption under that assumption.

## Normalizing By {math}`\pLvl`

Dividing the problem through by permanent income before solving simplifies it. Hereafter, nonbold variables will be the normalized bold-letter equivalent, e.g. {math}`\cNrm_{\tNow}=\cLvl_{\tNow}/\pLvl_{\tNow}`, and if {math}`\pLvl_{\tNow+1}={\PermGroFac} \pLvl_{\tNow}~\forall~t` then from the standpoint of date {math}`t`,

```{math}
\begin{aligned}
        \uFunc(\cLvl_{\tNow+n}) & =  \frac{\cLvl_{\tNow+n}^{1-\CRRA}}{1-\CRRA}  \\
         & =  \frac{(\cNrm_{\tNow+n}\pLvl_{\tNow+n})^{1-\CRRA}}{1-\CRRA}  \\
         & =  (\pLvl_{\tNow}{\PermGroFac}^{n})^{1-\CRRA}\frac{\cNrm_{\tNow+n}^{1-\CRRA}}{1-\CRRA}
\end{aligned}
```

which means that

```{math}
:label: eq:PFCRRA-maxc2

\sum_{n=0}^{\TEnd-\tNow} \DiscFac^{n}\frac{\cLvl_{\tNow+n}^{1-\CRRA}}{1-\CRRA} = \pLvl_{\tNow}^{1-\CRRA}\sum_{n=0}^{\TEnd-\tNow} ({\PermGroFac}^{1-\CRRA}\DiscFac)^{n} \frac{\cNrm_{\tNow+n}^{1-\CRRA}}{1-\CRRA}.
```

Furthermore, the accumulation equations can be rewritten by dividing both sides by {math}`\pLvl_{\tNow+1}`:

```{math}
\begin{aligned}
        \bLvl_{\tNow+1}/\pLvl_{\tNow+1} & =  \frac{(\mLvl_{\tNow}-\cLvl_{\tNow})\Rfree}{\pLvl_{\tNow+1}}  \\
        \bNrm_{\tNow+1} & =   \left(\frac{(\mLvl_{\tNow}-\cLvl_{\tNow})\Rfree}{\pLvl_{\tNow}}\right)\left(\frac{\pLvl_{\tNow}}{\pLvl_{\tNow+1}}\right) \\
         & =  (\mNrm_{\tNow}-\cNrm_{\tNow})(\Rfree/{\PermGroFac})
\end{aligned}
```

```{math}
\begin{aligned}
        \mLvl_{\tNow+1} & =  \bLvl_{\tNow+1}+\pLvl_{\tNow+1}
\\      \mNrm_{\tNow+1} & =  \bNrm_{\tNow+1}+1.
\end{aligned}
```

Now if we define {math}`\DiscAlt \equiv {\PermGroFac}^{1-\CRRA}\DiscFac` and {math}`\RNrmByG \equiv \Rfree/{\PermGroFac}`, the original problem can be rewritten as:

```{math}
:label: eq:PFCRRA-scaledmaxprob

\max~~\pLvl_{\tNow}^{1-\CRRA}\sum_{n=0}^{\TEnd-\tNow} \DiscAlt^{n} \uFunc(\cNrm_{\tNow+n})
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

subject to the FHWC

```{math}
\begin{aligned}
        {1} & <  \RNrmByG
\\  1 & <  \Rfree/\PermGroFac
\end{aligned}
```

which is the same condition {eq}`eq:FHWCPF` as above, and also subject to the RIC

```{math}
\begin{aligned}
                (\RNrmByG\DiscAlt)^{1/\CRRA} & <  \RNrmByG
\\              \left(\frac{\Rfree}{{\PermGroFac}}\DiscFac {\PermGroFac}^{1-\CRRA}\right)^{1/\CRRA} & <  \Rfree/{\PermGroFac}
\\              (\Rfree\DiscFac)^{1/\CRRA} & <  \Rfree
\end{aligned}
```

which is also the same as above in {eq}`eq:PatR`.

The [normalized solution](#eq:normC) can be rewritten

```{math}
\begin{aligned}
        \cNrm_{\tNow} & =  \left(\frac{\RNrmByG-(\RNrmByG\DiscAlt)^{1/\CRRA}}{\RNrmByG}\right)\oNrm_{\tNow}
\\ & =  \underbrace{(1 - \RPFac)}_{\equiv \MPC} \oNrm_{\tNow}
\end{aligned}
```

where {math}`\oNrm_{\tNow}` is the consumer's total wealth-to-permanent-labor-income ratio, and {math}`\MPC` is the MPC out of wealth.

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
Or, GIC-PF if we want to highlight that this is the condition for the PF model.
:::

In this sense the wealth-to-income *ratio* falls when income grows faster than consumption, and rises when it grows more slowly. Analogously to our earlier usages, a consumer for whom {math}`\GPFac=1` (equivalently, a growth patience rate {math}`\GPRte \equiv \log \GPFac = 0`) would be "growth poised."

For intuition, take a consumer with no nonhuman wealth, {math}`\bNrm_{\tNow}=0`: consumption grows by {math}`\APFac` and income by {math}`\PermGroFac`, and their PDVs are equal. If income grows faster, consumption must start above income: the consumer is impatient, spending more than income. Growth impatience is therefore the condition under which consumers with no assets borrow.

The condition also decides where the consumer ends up. Total wealth relative to permanent income evolves as {math}`\oNrm_{\tNow+1} = (\oNrm_{\tNow}-\cNrm_{\tNow})\RNrmByG = (1-\MPC)\RNrmByG\,\oNrm_{\tNow}`, and since {math}`(1-\MPC)\RNrmByG = \RPFac\Rfree/\PermGroFac = \GPFac`,

```{math}
:label: eq:oNrmPath

\oNrm_{\tNow+1} = \GPFac\,\oNrm_{\tNow}.
```

A growth impatient consumer's total wealth therefore shrinks toward zero relative to income. Consumption relative to permanent income falls toward zero, and market resources approach {math}`-\hNrmEnd`, minus end-of-period human wealth: the consumer ends up owing the present value of all future income, the most that could ever be repaid. A consumer whose GIC fails instead accumulates wealth relative to income without bound. [The figure of the paths](#fig:PathsGIC) shows both. Neither end is plausible, which is one reason later chapters add uncertainty and liquidity constraints.

:::{figure} figures/PerfForesightPathsGIC.png
:name: fig:PathsGIC
:align: center

Consumption and market resources when the GIC holds and when it fails

Ratios to permanent income, for a consumer who starts with no bank balances. In both cases {math}`\rfree=\discRte=0.04` and {math}`\CRRA=2`, so the RIC and the FHWC hold. Drawn by the chapter's [notebook](PerfForesightCRRA.ipynb) (open it in [Colab](https://colab.research.google.com/github/intertemporal-choice/intertemporal-choice.github.io/blob/main/content/consumption/PerfForesightCRRA/PerfForesightCRRA.ipynb) or [Binder](https://mybinder.org/v2/gh/intertemporal-choice/intertemporal-choice.github.io/main?labpath=content/consumption/PerfForesightCRRA/PerfForesightCRRA.ipynb)).
:::

## Applications

(subsec:HWEffect)=
### How Large is the Human Wealth Effect?

We can now apply the model to answer our first useful question: How large does the model imply the "human wealth effect" is?

For simplicity, assume that {math}`\bNrm_{\tNow} = 0`. Then the original version of the approximate formula {eq}`eq:PFCRRA-capprox` tells us that the *level* of consumption will be given by:

```{math}
:label: eq:PFCRRA-cofw2

\begin{aligned}
        \cLvl_{\tNow} & \approx  \left(\rfree - \CRRA^{-1}(\rfree-\discRte)\right)\left(\frac{\pLvl_{\tNow}}{1-{\PermGroFac}/\Rfree}\right)  \\
         & \approx  \left(\rfree - \CRRA^{-1}(\rfree-\discRte)\right)\left(\frac{\pLvl_{\tNow}}{\rfree-\PermGroRte}\right).
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
        \cLvl_{\tNow} & \approx  \pLvl_{\tNow} \left(\frac{\rfree - (\PermGroRte+\GPRte)}{\rfree-\PermGroRte}\right)
\\ & =  \pLvl_{\tNow} \left(1 - \GPRte/(\rfree - \PermGroRte)\right).
\end{aligned}
```

Remembering that imposition of the GIC is equivalent to assuming {math}`\GPRte < 0`, while the FHWC requires {math}`\rfree > \PermGroRte`, the expression {math}`-\GPRte/(\rfree-\PermGroRte)` will be positive: The consumer will spend more than permanent labor income.

Now suppose we choose plausible values for {math}`(\rfree, \discRte, \PermGroRte, \CRRA) = (0.04,0.04,0.02,2)`. Then {eq}`eq:PFCRRA-cofw2` becomes:

```{math}
\begin{aligned}
        \cLvl_{\tNow} & \approx  0.04 (\pLvl_{\tNow}/0.02) \\
         & =  2 \pLvl_{\tNow}.
\end{aligned}
```

Now suppose the interest rate changes to {math}`\rfree=0.03`, while all other parameters remain the same. Then {eq}`eq:PFCRRA-cofw2` becomes:

```{math}
\begin{aligned}
        \cLvl_{\tNow} & \approx  0.035 (\pLvl_{\tNow}/0.01)  \\
         & =  3.5 \pLvl_{\tNow}.
\end{aligned}
```

In terms of the three effects of {math}`\rfree` in {eq}`eq:PFCRRA-capprox`, with {math}`\bNrm_{\tNow}=0` consumption is {math}`\MPC\hNrm` times permanent income, where {math}`\MPC = \rfree-\CRRA^{-1}(\rfree-\discRte)` and {math}`\hNrm \approx 1/(\rfree-\PermGroRte)`, so {math}`\log \cNrm_{\tNow} = \log \MPC + \log \hNrm` and the three effects add:

```{math}
:label: eq:dlogcdr

\frac{d \log \cNrm_{\tNow}}{d \rfree} \approx \underbrace{\frac{1}{\MPC}}_{\text{income}} - \underbrace{\frac{\CRRA^{-1}}{\MPC}}_{\text{substitution}} + \underbrace{\frac{1}{\PermGroRte-\rfree}}_{\text{human wealth}}.
```

The income and substitution terms are positive because the RIC makes {math}`\MPC>0`; the human wealth term is negative because the FHWC requires {math}`\rfree>\PermGroRte`. At the calibration above the three terms are 25, −12.5 and −50. In the example, the fall in {math}`\rfree` lowers the MPC from 0.04 to 0.035 (the income effect lowers it by 0.01, the substitution effect raises it by 0.005), while human wealth doubles, from 50 to 100 times permanent income: −0.13 against +0.69 in logs. The human wealth effect exceeds the income effect whenever the consumer is growth impatient, because the two net to {math}`\GPRte/(\MPC(\rfree-\PermGroRte))`, here −25.

These magnitudes depend on the infinite horizon. A consumer with 40 years of permanent income left has human wealth of 28 times permanent income by [the PDV of labor income](#eq:PFCRRA-yfin), against 52 with no end (50 by the approximation above), and by [the finite-horizon consumption function](#eq:PFCRRA-cfinhoriz) consumes 1.36 times permanent income. When {math}`\rfree` falls to 0.03, that consumer's human wealth rises by 18.5 percent rather than doubling, and consumption rises by 10 percent rather than by about three-quarters. The human wealth effect still outweighs the other two together, but by about 2.3 to 1 rather than 4 to 1, because a finite horizon shortens the stream of income that the interest rate discounts.

For plausible parameters, then, the human wealth effect dwarfs the income and substitution effects: consumption should fall sharply when interest rates rise and jump when they fall. This is a summary of the main point of the famous paper by {cite:t}`summersCapTax`; Summers derives formulas for an economy with overlapping generations of finite-lifetime consumers. Finite lifetimes shrink the effect, as the calculation above shows, but in his model it is still large.

Nor is a change of a percentage point in the long-term real interest rate unusual. [The long-term real interest rate figure](#fig:LongTermRealRate) shows two measures of it. One is the Federal Reserve Bank of Cleveland's estimate of the real rate expected over the next ten years, from a model fitted to Treasury yields, inflation, inflation swaps and surveys of expected inflation {cite:p}`haubrichInflationSwaps`. The other is the yield on ten-year inflation-indexed Treasury bonds (TIPS).

The expected rate averaged 5.3 percent a year in the 1980s and 0.6 percent in the 2010s, and reached a low of −0.4 percent in August 2020. The TIPS yield rose by 3.5 percentage points in two years, from −1.07 percent in August 2021 to 2.41 percent in October 2023. Since 1982 the expected rate has moved by a percentage point or more within a year in 13 percent of months, and within two years in 24 percent. The [notebook](PerfForesightCRRA.ipynb) computes these numbers from FRED's data; open it in [Colab](https://colab.research.google.com/github/intertemporal-choice/intertemporal-choice.github.io/blob/main/content/consumption/PerfForesightCRRA/PerfForesightCRRA.ipynb) or [Binder](https://mybinder.org/v2/gh/intertemporal-choice/intertemporal-choice.github.io/main?labpath=content/consumption/PerfForesightCRRA/PerfForesightCRRA.ipynb) to run it without installing anything.

:::{figure} figures/LongTermRealRate.png
:name: fig:LongTermRealRate
:align: center

Two measures of the U.S. long-term real interest rate

Monthly. The Cleveland Fed's [expected ten-year real rate](https://fred.stlouisfed.org/series/REAINTRATREARAT10Y), from 1982, and the [ten-year TIPS yield](https://fred.stlouisfed.org/series/FII10), from 2003, as FRED reported them on 2026-10-20. Drawn by the chapter's [notebook](PerfForesightCRRA.ipynb) (open it in [Colab](https://colab.research.google.com/github/intertemporal-choice/intertemporal-choice.github.io/blob/main/content/consumption/PerfForesightCRRA/PerfForesightCRRA.ipynb) or [Binder](https://mybinder.org/v2/gh/intertemporal-choice/intertemporal-choice.github.io/main?labpath=content/consumption/PerfForesightCRRA/PerfForesightCRRA.ipynb)).
:::

The model's predictions for these episodes are not borne out. With {math}`\PermGroRte=0.02`, the FHWC fails whenever {math}`\rfree<0.02`, as the expected real rate did throughout the 2010s; the infinite-horizon formula then has no answer, and only a finite horizon gives one. At the same calibration, with 40 years left, the rise in the TIPS yield from −1.07 to 2.41 percent would cut consumption by about a third, from 2.5 to 1.6 times permanent income. Nothing of the kind happened: real consumer spending in the United States kept growing through 2022 and 2023.

The model's response is too large for several reasons. It takes the change in the interest rate to be permanent and known. Its consumers can borrow freely against future income, so the whole change in human wealth reaches their spending. And it ignores general equilibrium, in which incomes and other prices move with the interest rate: in a model with uninsurable income risk and assets of different liquidity, the indirect effects of a change in the interest rate, through labor demand, far outweigh direct effects such as intertemporal substitution {cite:p}`kmvHANK`.

(subsec:SavingRateResponse)=
### How Does the Saving Rate Respond to Interest Rates?

The level of saving can be defined as total income minus total consumption:

```{math}
\sLvl_{\tNow} = \rfree \aLvl_{\tNow-1} + \pLvl_{\tNow} - \cLvl_{\tNow}
```

but substituting from {eq}`eq:CvsP` and {eq}`eq:PFCRRA-capprox`,

```{math}
:label: eq:cFromHandB

\cLvl_{t} \approx \pLvl_{\tNow} \left(1 - \GPRte/(\rfree - \PermGroRte)\right)-\patr\bLvl_{\tNow}
```

this can be rewritten as

```{math}
\begin{aligned}
 \sLvl_{\tNow} & \approx  \rfree \aLvl_{\tNow-1} + \pLvl_{\tNow}- \pLvl_{\tNow} \left(1 - \GPRte/(\rfree - \PermGroRte)\right) + \patr\Rfree \aLvl_{\tNow-1}
\\ & =  \rfree \aLvl_{\tNow-1} + \pLvl_{\tNow} \GPRte/(\rfree - \PermGroRte) + \patr\Rfree\aLvl_{\tNow-1}
\\ \sNrm_{\tNow} & \approx  \rfree \aNrm_{\tNow-1} + \GPRte/(\rfree - \PermGroRte) + \patr\Rfree \aNrm_{\tNow-1}
\\ & \approx  \GPRte/(\rfree - \PermGroRte)+ \CRRA^{-1}(\rfree-\discRte)\aNrm_{\tNow-1}
\end{aligned}
```

(where the last approximations come from the assumptions that {math}`1/\PermGroFac \approx 1` and that {math}`\rfree\patr`, the product of two small rates, is zero, so that {math}`\rfree+\patr\Rfree \approx \rfree+\patr = \CRRA^{-1}(\rfree-\discRte)` by {eq}`eq:patrApprox`). The saving *rate* {math}`\savRte`, not {math}`\sNrm`, is saving as a share of *total* income, not just labor income:

```{math}
\savRte_{\tNow} = \left(\frac{\GPRte/(\rfree - \PermGroRte)+ \CRRA^{-1}(\rfree-\discRte)\aNrm_{\tNow-1}}{1+ \rfree \aNrm_{\tNow-1}}\right).
```

The first thing to notice about this expression is that as {math}`\aNrm_{\tNow-1}` approaches infinity, the saving rate asymptotes to

```{math}
\savRte_{\tNow} \approx \left(\frac{\CRRA^{-1}(\rfree-\discRte)}{\rfree}\right)
```

and whether the saving rate is positive or negative depends on whether the consumer is absolutely impatient, absolutely poised, or absolutely patient.

:::{margin}
In partial equilibrium, the consumer's wealth can grow without bound without moving the interest rate.
:::

If we rewrite this as

```{math}
\savRte \approx \CRRA^{-1} (1 - \discRte \rfree^{-1})
```

then it is apparent that the response of the asymptotic saving rate to the interest rate is

```{math}
:label: eq:dsdr

\left(\frac{d \savRte}{d \rfree}\right) = \CRRA^{-1}\discRte \rfree^{-2}.
```

If we consider almost any plausible configuration of parameter values, say {math}`\rfree = \discRte=0.05` and {math}`\CRRA = 2`, this is a very large response: {math}`(1/2)(20)=10`.

In terms of the three effects of {math}`\rfree` in {eq}`eq:PFCRRA-capprox`, this response is entirely a substitution effect. A consumer whose wealth is enormous relative to income has negligible human wealth, so the human wealth effect is negligible too. The income effect raises the MPC by the rise in {math}`\rfree`, and so raises consumption by the rise in {math}`\rfree` times wealth, but capital income rises by exactly as much, so the income effect leaves saving unchanged. What remains is the substitution effect: consumption grows faster by {math}`\CRRA^{-1}` times the rise in {math}`\rfree`, and a consumer who lives on capital income can make consumption grow faster only by making wealth grow faster, so saving rises by {math}`\CRRA^{-1}` times the rise in {math}`\rfree` times wealth.

The saving *rate* responds so strongly because it divides that change by income, which is only {math}`\rfree` times wealth. Writing {eq}`eq:dsdr` as {math}`\CRRA^{-1}\rfree^{-1} - \savRte\rfree^{-1}` shows this: the first term is the substitution effect, and the second, zero for an absolutely poised consumer, is only the effect of higher income on the rate's denominator.

A consumer with no wealth responds even more strongly, and for a different reason. With {math}`\aNrm_{\tNow-1}=0`, the saving rate is {math}`\GPRte/(\rfree-\PermGroRte) = 1-\MPC\hNrm`, with {math}`\hNrm \approx 1/(\rfree-\PermGroRte)`, and its response to the interest rate is

```{math}
:label: eq:dsdrNoWealth

\left(\frac{d \savRte}{d \rfree}\right)_{\aNrm_{\tNow-1}=0} = -\underbrace{\hNrm}_{\text{income}}+\underbrace{\CRRA^{-1}\hNrm}_{\text{substitution}}+\underbrace{\MPC\hNrm^{2}}_{\text{human wealth}} = \frac{(1-\CRRA^{-1})\PermGroRte+\CRRA^{-1}\discRte}{(\rfree-\PermGroRte)^{2}}.
```

All three effects are at work, each measured in its own terms and then turned into saving. The income effect raises the MPC one for one with {math}`\rfree`, which raises consumption, and so lowers saving, by {math}`\hNrm` per unit of {math}`\rfree`; with no wealth, there is no capital income to offset it. The substitution effect lowers the MPC by {math}`\CRRA^{-1}` per unit of {math}`\rfree`, which raises saving by {math}`\CRRA^{-1}\hNrm`. The human wealth effect lowers human wealth by {math}`\hNrm/(\rfree-\PermGroRte) = \hNrm^{2}`, which at the MPC {math}`\MPC` raises saving by {math}`\MPC\hNrm^{2}`.

With the calibration of [How Large is the Human Wealth Effect?](#subsec:HWEffect), {math}`(\rfree, \discRte, \PermGroRte, \CRRA) = (0.04,0.04,0.02,2)`, human wealth is 50 times income and {math}`\MPC=0.04`, so the three terms are −50, 25 and 100, and the response is 75, six times the 12.5 that {eq}`eq:dsdr` gives at the same parameter values. When {math}`\rfree` falls to 0.03, the saving rate falls from −1 to −2.5, the mirror image of that section's rise in consumption from 2 to 3.5 times income.

The human wealth effect is the largest of the three here, and it exceeds the income effect whenever the consumer is growth impatient: {math}`\MPC\hNrm^{2}>\hNrm` exactly when {math}`\MPC\hNrm>1`, that is, when a consumer with no wealth spends more than income, which is {math}`\GPRte<0`. It is also the effect that mechanisms later in the course, liquidity constraints and precautionary saving, drastically attenuate for some households while leaving a meaningful income effect in place. Their human wealth falls by just as much when {math}`\rfree` rises, but because they will not borrow against future income, the fall does much less to their consumption and their saving.

The evidence also tempers the response at the other end. For a consumer with large wealth the response is entirely intertemporal substitution, and many estimates of the elasticity of intertemporal substitution are below the 0.5 used here; {cite:t}`hallSubstitution` finds it close to zero.

(sec:PerfForesightCRRA-AppendixResults)=
## Results in the Appendix

The [appendix](#sec:PerfForesightCRRA-Appendix) derives three further results, which are stated here without their derivations.

- *[The limiting solution if the FHWC fails](#sec:PFwhenFHWfails).* If the FHWC fails, the limit of the finite-horizon solutions depends on the GIC. If it holds, as it must when the RIC holds, consumption out of human wealth grows without bound. If the RIC and the GIC both fail, consumption goes to zero; on the boundary between the two, {math}`\GPFac=1`, it converges to permanent income.
- *[The MPC recursion](#sec:PerfForesightCRRA-MPCRecursion).* The inverse of the MPC satisfies {math}`\MPC_{t}^{-1} = 1+\RPFac\MPC_{t+1}^{-1}`.
  Starting from {math}`\MPC_{T}=1`, this makes {math}`\MPC_{t}^{-1}` the sum {math}`1+\RPFac+\RPFac^{2}+\dots+\RPFac^{T-t}`.
- *[Value in closed form](#sec:PerfForesightCRRA-ValueClosedForm).* Value is current utility times the inverse of the MPC: {math}`\vLvl_{t} = \uFunc(\cLvl_{t})\MPC_{t}^{-1} = \uFunc(\oLvl_{t})\MPC_{t}^{-\CRRA}`.
  One consequence is that the utility-inverse of value is linear in market resources above their minimum, so value is easy to compute.
