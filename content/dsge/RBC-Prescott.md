(sec:RBC-Prescott)=
# The Prescott Real Business Cycle Model

This section presents the elements of the original

Real Business Cycle model of aggregate fluctuations, as laid out

by {cite:t}`prescottTheoryAhead`, along with a few critiques articulated by {cite:t}`summers:skeptical` and others.

:::{margin}
The good news is that you already understand the subtlest and hardest parts of the model - the intertemporal consumption optimization problem.
:::

Consider a representative household whose goal is to maximize

```{math}
\Ex_{t} \left[\sum_{t=0}^{\infty} \Discount^{t}\uFunc(\cons_{t},\leisure_{t})      \right]
```

where {math}`\leisure_{t}` is the fraction of time the representative agent spends at leisure (not working); the

alternative to leisure is the number of hours you work, which will be designated

{math}`\labor_{t}`, and the time endowment is normalized to 1, so that

```{math}
\begin{gathered}\begin{aligned}
        \labor_{t}+\leisure_{t} & =  1.
\end{aligned}\end{gathered}
```

Assume that the structure of the utility function is

```{math}
\begin{gathered}\begin{aligned}
        \uFunc(\cons,\leisure) & =  \left(\frac{(\cons^{1-\zeta}\leisure^{\zeta})^{1-\CRRA}}{1-\CRRA}\right)
\\  \uFunc^{\cons}     & =  (\cons^{1-\zeta}\leisure^{\zeta})^{-\CRRA}\cons^{-\zeta}\leisure^{\zeta}(1-\zeta)
\\  \uFunc^{\leisure }  & =  (\cons^{1-\zeta}\leisure^{\zeta})^{-\CRRA}\cons^{1-\zeta}\leisure^{\zeta-1}\zeta.
\end{aligned}\end{gathered}
```

Think about the maximum amount of income that could be gained if the representative agent

worked every waking hour:

:::{margin}
Since the time endowment is one, resources are {math}`\Wage_{t}*1`.
:::

```{math}
\begin{gathered}\begin{aligned}
        \inc_{t} & =  \Wage_{t}.
\end{aligned}\end{gathered}
```

The representative agent can then think of deciding to 'purchase' two things with this

endowment of income: leisure {math}`\leisure_{t}` whose price is {math}`\Wage_{t}`, or

consumption, whose price is normalized to one.

Over the past century in the U.S., wages have risen very substantially, but hours

worked have not declined much if at all. ({cite:t}`rameyFrancisLeisure`). What kind of utility

function implies that the budget share of a good

(leisure) remains constant even as the price of the good changes

sharply? A Cobb-Douglas utility function. Hence the assumption that

utility is obtained from a Cobb-Douglas aggregate of consumption and

leisure is consistent with the lack of a strong trend in hours worked per

worker.

Since workers are choosing how many hours to work

as well how much to consume, a first order condition

will characterize the optimal choice  between consumption

and leisure  within a period. In particular, the price of leisure

is {math}`\Wage_{t}` and the price of consumption is 1, so the ratio of the

marginal utility of leisure to the marginal utility of consumption

should be

```{math}
:label: eq:RBC-focwucul

\begin{gathered}\begin{aligned}
        \left(\frac{\Wage_{t}}{1}\right) & =  \left(\frac{\uFunc^{\leisure }_{t}}{\uFunc^{\cons}_{t}}\right).
\end{aligned}\end{gathered}
```

To see this, note that the consumer's goal is to

```{math}
:label: eq:RBC-intramax

\max_{\{\cons_{t},\leisure_{t}\}} \uFunc(\cons_{t},\leisure_{t})     .
```

Suppose the consumer has decided to spend a given amount {math}`\chi_{t}` in period {math}`t`

on a combination of consumption and leisure,

```{math}
\begin{gathered}\begin{aligned}
        \cons_{t}+\Wage_{t}\leisure_{t} & =  \chi_{t}
\end{aligned}\end{gathered}
```

Then {eq}`eq:RBC-intramax` becomes

```{math}
:label: eq:RBC-intramax2

\max_{\{ \leisure_{t} \}} \uFunc(\chi_{t}-\Wage_{t}\leisure_{t},\leisure_{t})
```

for which the FOC is

```{math}
\begin{gathered}\begin{aligned}
        - \uFunc^{\cons}_{t}\Wage_{t} + \uFunc_{t}^{\leisure } & =  0
\\      \Wage_{t} & =  (\uFunc^{\leisure }_{t}/\uFunc_{t}^{\cons}).
\end{aligned}\end{gathered}
```

Returning to {eq}`eq:RBC-focwucul`

```{math}
\begin{gathered}\begin{aligned}
        \left(\frac{\Wage_{t}}{1}\right) & =  \left(\frac{\uFunc^{\leisure }_{t}}{\uFunc^{\cons}_{t}}\right)
\\ \Wage_{t} & =  \left(\frac{\cons_{t}^{1-\zeta}\leisure_{t}^{\zeta-1}}{\cons_{t}^{-\zeta}\leisure^{\zeta}_{t}}\right)\left(\frac{\zeta}{1-\zeta}\right)
\\  & =  \left(\frac{\cons_{t}}{\leisure_{t}}\right)\left(\frac{\zeta}{1-\zeta}\right)
\end{aligned}\end{gathered}
```

or

```{math}
:label: eq:wlc

\begin{gathered}\begin{aligned}
        \Wage_{t}\leisure_{t}/\cons_{t} & =  \left(\frac{\zeta}{1-\zeta}\right)      .
\end{aligned}\end{gathered}
```

Since we know that {math}`\leisure` has been roughly constant over long periods

of time, this implies that as wages rise, consumption rises by roughly

the same amount.

One of the original proimises of the DSGE literature was to calibrate

its business-cycle models based on either long-run facts (like the lack

of a trend in {math}`\leisure`) or on micro data (like intertemporal elasticities

estimated using household data). So how is {math}`\zeta` calibrated?

If wages are defined as per unit of labor, then if on average consumption

roughly equals labor income {math}`\cons = (1-z)w` we have

```{math}
\begin{gathered}\begin{aligned}
        \left(\frac{\wage  \leisure}{\wage (1-z)}\right) & =  \left(\frac{\zeta}{1-\zeta}\right)  \\
        \left(\frac{1-\leisure}{\leisure }\right) & =  \left(\frac{1-\zeta}{\zeta}\right)
\\      1/\leisure - 1 & =  1/\zeta - 1
\\  \leisure & =  \zeta     .
\end{aligned}\end{gathered}
```

So {math}`\zeta` should be calibrated to be equal to the proportion of their

available (i.e.  non-sleep) time people spend not working. A 40-hour

work week (along with 8 hours of sleep a day) would yield {math}`\zeta = 2/3`. Among other taste parameters, Prescott chooses log utility

({math}`\lim_{\CRRA \rightarrow 1}\uFunc(\cons)`) and {math}`\Discount = 0.96.`

The aggregate production function is assumed to be Cobb-Douglas,

```{math}
\begin{gathered}\begin{aligned}
        \Kap_{t+1} & =  \overbrace{\daleth}^{1-\depr} \Kap_{t}+\Inc_{t}-\Cons_{t}  \\
        \Inc_{t} & =  \PtyLev_{t}\Kap_{t}^{1-\labShare}\Labor_{t}^{\labShare}
\end{aligned}\end{gathered}
```

where {math}`\labor_{t} = (1-\leisure_{t})\Hours_{t} = \labor_{t}\Hours_{t}`

where {math}`\Hours_{t}=\sum_{i} \hours_{i}` is the aggregate amount of

Hours available to members of the working population. Constant income

shares and perfect competition imply

```{math}
\begin{gathered}\begin{aligned}
        \FFunc_{\Labor}\Labor/\Inc & =  \labShare \PtyLev_{t}\Kap_{t}^{1-\labShare}\Labor^{\labShare-1}\Labor_{t}/\Inc_{t}  \\
         & =  \labShare
\end{aligned}\end{gathered}
```

so that labor's share of GDP is roughly constant. Prescott sets

labor's share to a constant 64 percent, and chooses a depreciation

rate of {math}`\depr = 0.10`.

The crucial assumption, however, is about the productivity process,

since 'technology shocks' are assumed to drive business cycles.

Prescott defines the 'hat' operator {math}`\hat{}` as:

```{math}
\begin{gathered}\begin{aligned}
        \hat{X}_{t} & =  \left(\frac{X_{t}-X_{t-1}}{X_{t-1}}\right)
\end{aligned}\end{gathered}
```

which implies from the production function that

```{math}
\begin{gathered}\begin{aligned}
        \hat{\PtyLev}_{t} & \approx  \hat{Y}_{t}-\labShare \hat{\Labor}_{t} - (1-\labShare)\hat{\Kap}_{t}.
\end{aligned}\end{gathered}
```

(this is just the Solow residual).

Prescott 'estimates' a productivity process that takes the form

```{math}
\begin{gathered}\begin{aligned}
        \hat{\PtyLev}_{t} & =  \ptyGro_{t} + \epsilon_{t}
\end{aligned}\end{gathered}
```

with a standard deviation of {math}`\sigma_{\epsilon} = 0.76` per quarter.

Prescott makes sufficient assumptions (perfect competition, etc.) so

that the social planner's problem is the same as the decentralized

solution. With log utility, the social planner's problem is

```{math}
:label: eq:objlog

\max \Ex_{t}\left[\sum_{t=0}^{\infty}\Discount^{t} \left((1-\zeta) \log \cons_{t} + \zeta \log (1-\labor_{t})\right)\right]
```

subject to

```{math}
\begin{gathered}\begin{aligned}
        \kap_{t+1} & =  \daleth \kap_{t}+\PtyLev_{t}k^{1-\labShare}_{t}\labor^{\labShare} - \cons_{t}  \\
        \hat{\PtyLev}_{t} & =  \ptyGro + \epsilon_{t}.
\end{aligned}\end{gathered}
```

Prescott argues that the way to judge the model is by whether it

produces plausible statistics for standard deviations of the

key variables. He produces a table that argues it does:

:::{list-table}
:header-rows: 0

*   *

    *   {math}`\sigma_{\leisure }`

    *   {math}`\sigma_{y}`

        {math}`\sigma_{n}`

*   *   US Data

    *   0.76

    *   1.76 1.67

*   *   Model

    *   0.76

    *   1.48 0.76
:::

Since the first column is calibrated, it isn't a test of the model.

The second column comes out of the model, and isn't too bad a fit.

However, the third column is a terrible fit. What it says is that

labor input is much more variable over the course of the business

cycle than this model would suggest.

What's going on? To understand the answer, we need to understand why

hours fluctuate in this model at all. Recall that we deliberately constructed the

model (by choosing a utility function that was Cobb-Douglas in consumption and

leisure) in a way designed to  prohibit any  long-run response of hours

worked to wages. Since hours worked are being chosen freely on a

day-by-day basis by workers in this model, there must be some

incentive that causes them to be willing to put up with  short-term

variation in hours (over the business cycle).

The answer is that transitory productivity shocks provide an incentive

to work harder some times than others. In particular, if there is a

temporary positive productivity shock you will be willing to work longer hours

than usual, while if there is a negative productivity shock everybody

wants to take a vacation.

:::{margin}
Thus the 1930s in the US could be characterized as 'The Great Vacation ...'
:::

To see this formally, consider again the first order conditions from

the maximization problem. We showed in {eq}`eq:wlc` that

:::{margin}
Intuition: u must be unchanged if {math}`\leisure` increases one and {math}`\cons` decreases by {math}`\Wage_{t}`.
:::

```{math}
:label: eq:wlcttp1

\begin{gathered}\begin{aligned}
        \Wage_{t}\leisure_{t}/\cons_{t} & =  \left(\frac{\zeta}{1-\zeta}\right)  \\
         & =  \Wage_{t+1}\leisure_{t+1}/\cons_{t+1}.
\end{aligned}\end{gathered}
```

Now note that since {eq}`eq:objlog` is separable in consumption

and leisure the intertemporal FOC will imply that

```{math}
\begin{gathered}\begin{aligned}
        1/\cons_{t}   & =  \Rfree_{t+1}\Discount /\cons_{t+1}
\\  \cons_{t+1}   & =  \Rfree_{t+1}\Discount \cons_{t}.
\end{aligned}\end{gathered}
```

Combining this with {eq}`eq:wlcttp1` gives

```{math}
\begin{gathered}\begin{aligned}
        \Wage_{t}\leisure_{t} & =  \Wage_{t+1}\leisure_{t+1}/\Rfree_{t+1}\Discount  \\
        \leisure_{t+1}/\leisure_{t} & =  \left(\frac{\Rfree_{t+1}\Discount}{\Wage_{t+1}/\Wage_{t}}\right)  \\
        \hat{\leisure }_{t+1} & \approx  -\hat{\wage }_{t+1}+(\rfree_{t+1}-\theta)
\end{aligned}\end{gathered}
```

What this equation tells us is that there are two ways to make {math}`\leisure_{t}`

(and therefore {math}`\labor_{t}`) fluctuate over the business cycle:

1.  Make transitory movements in real wages induce a strong labor supply response

    *   Problem: A large number of microeconomic studies have estimated

        the elasticity of labor supply with respect to wages to be much too small to explain

        the observed fluctuations in hours over the business cycle. Indeed, there is even controversy

        about whether real wages rise or fall over the business cycle. But even if we accept that

        wages fall during recessions, the evidence at the micro level does not seem to suggest that people are willing

        to dramatically change their work hours in response to transitory fluctuations in wages

2.  Make movements in interest rates induce a strong labor

    supply response (the idea is that you will work hard during the

    period of high interest rates in order to earn more cash

    which can be invested to take advantage of the high interest rate - in thinking about this,

    consider that a high value of {math}`\Rfree_{t+1}` will induce high leisure

    growth between {math}`t` and {math}`t+1` by resulting in low leisure in period

    {math}`t`)

    *   Problem: If this is the mechanism, there should at the same time be a strong consumption

        response:

        ```{math}
        \begin{gathered}\begin{aligned}
                        \Wage_{t}\leisure_{t}/\cons_{t} & =  \Wage_{t+1}\leisure_{t+1}/\cons_{t+1}  \\
                        \cons_{t+1}/\cons_{t} & =  \Wage_{t+1}\leisure_{t+1}/\Wage_{t}\leisure_{t}
                \end{aligned}\end{gathered}
        ```

        so if the labor supply response is not being driven by wage differences,

        there should be a one-for-one comovement of consumption with leisure - i.e. recessions should be periods of high consumption and booms should be periods

        of low consumption!

This latter is a quite general problem with the DSGE framework in which

fluctuations in employment over the business cycle are driven by

voluntary changes in hours worked.

