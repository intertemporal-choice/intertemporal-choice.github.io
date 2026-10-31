(sec:HallJorgenson)=
# The Hall-Jorgenson Model of Investment

{cite:t}`hall&jorgenson:i` consider the problem of a firm that produces output using capital {math}`\kap` as its only input,

```{math}
\inc = \fFunc(\kap)
```

and which obtains its capital {math}`\kap` from a market in which a unit of capital can be rented for a unit of time at rate {math}`\kapRent_{t}`.

In period {math}`t`, the firm maximizes profit (implicitly normalizing the price of output to 1),

```{math}
\max_{\kap_{t}} ~ \kap_{t}^{\kapShare}-\kapRent_{t}\kap_{t}
```

yielding first order conditions

```{math}
:label: eq:khj

\begin{gathered}\begin{aligned}
\fFunc^{\prime}(\kap_{t}) & =  \kapRent_{t}
\\        \kapShare \kap_{t}^{\kapShare-1} & =  \kapRent_{t}  \\
         (\inc_{t}/\kap_{t}) \kapShare & =  \kapRent_{t}  \\
        \kap_{t} & =  (\inc_{t}/\kapRent_{t})\kapShare .
\end{aligned}\end{gathered}
```

This equation says the level of capital is always instantly adjusted to {math}`\inc_{t}` and {math}`\kapRent_{t}`, with no costs of adjustment.

What determines the cost of capital? In the simple case with no taxes and no capital market frictions of any kind, an investor must be indifferent between putting their money in the bank and earning interest at rate {math}`\rfree`, and buying a unit of capital, renting it out at rate {math}`\kapRent_{t}`, and then reselling it the next period.

Let {math}`\Price_{t}` be the purchase price of one unit of capital at date {math}`t` (distinct from the rental rate, and typically much larger); in continuous time, the rate of change of {math}`\Price_{t}` is {math}`\dot{\Price}_{t}`. Assume that capital depreciates geometrically at rate {math}`\depr`. The net profit from the *continuous time* purchase-and-rent strategy is the income from renting, minus the loss from depreciation, plus the capital gain from the change in the price of capital:

```{math}
\kapRent_{t}-\depr \Price_{t}+\dot{\Price}_{t}.
```

Thus, the no-arbitrage condition is

```{math}
:label: eq:ctarb

\begin{gathered}\begin{aligned}
        \rfree \Price_{t} & =  \kapRent_{t} - \depr \Price_{t} + \dot{\Price}_{t}
\\  (\rfree+\depr) \Price_{t} & =  \kapRent_{t}+\dot{\Price}_{t}     .
\end{aligned}\end{gathered}
```

where the left-hand side is the return from putting money in the bank at rate {math}`\rfree`, which we assume is perfectly certain and time-invariant.

Now to simplify our lives we will assume constant capital goods prices, {math}`\dot{\Price}_{t}=0`. Thus, substituting the value for {math}`\kapRent_{t}` from {eq}`eq:ctarb` into {eq}`eq:khj` we have:

```{math}
\begin{gathered}\begin{aligned}
        \kap_{t} & =  \kapShare \inc_{t}/\kapRent_{t}  \\
         & =  \frac{\kapShare \inc_{t}}{(\rfree+\depr)\Price_{t}}.
\end{aligned}\end{gathered}
```

(HallJorgensonTaxes)=
## Taxes

Now let's introduce taxes. Let {math}`\taxCorp` be the corporate tax rate, and {math}`\itc` the rate of the investment tax credit (ITC), which returns to the firm the fraction {math}`\itc` of what it spends on new capital. In the United States, the federal corporate tax rate has been 21 percent since the Tax Cuts and Jobs Act of 2017 took effect in 2018; it was 35 percent from 1993, 34 percent from 1988, and 46 percent from 1979 until the Tax Reform Act of 1986. A general investment tax credit was introduced at 7 percent in 1962, suspended in 1966-67 and repealed in 1969, restored in 1971, raised to 10 percent in 1975, and repealed for good by the Tax Reform Act of 1986.

The tax code also lets the firm deduct the depreciation of its capital from its taxable income, on a schedule the code sets, and these deductions are the heart of the analysis of {cite:t}`hall&jorgenson:i`. Let {math}`z` be the present value of the deductions per dollar of investment. Each dollar of investment then reduces the firm's taxes by {math}`\taxCorp z` in present value, and the net, discounted, after-tax price of capital to the firm is[^footnote1]

[^footnote1]: Assume that if the firm sells the capital, it must repay the ITC on a pro-rata basis; this prevents tax arbitrage opportunities.

```{math}
\hat{\Price}_{t} = (1-\itc-\taxCorp z) \Price_{t}.
```

Now let's rewrite the arbitrage equation {eq}`eq:ctarb` taking account of taxes. The rental income {math}`\kapRent_{t}` must be multiplied by {math}`(1-\taxCorp)` because the capital-rental business must pay taxes too:

```{math}
(\rfree+\depr) \hat{\Price}_{t} = (1-\taxCorp) \kapRent_{t}+\dot{\hat{\Price}}_{t}.
```

If we simplify again by assuming that {math}`\dot{\hat{\Price}}_{t}=0`, we have the Hall-Jorgenson cost of capital,

```{math}
:label: eq:hjUserCost

\kapRent_{t} = (\rfree+\depr)\Price_{t}\frac{1-\itc-\taxCorp z}{1-\taxCorp}.
```

(If the price of capital is changing, the same steps give {math}`\kapRent_{t} = (\rfree+\depr-\dot{\Price}_{t}/\Price_{t})\Price_{t}(1-\itc-\taxCorp z)/(1-\taxCorp)`.)

Two special cases show why the deductions matter so much. If investment can be deducted in full at once ("expensing"), {math}`z=1`, and with no ITC

```{math}
\kapRent_{t} = (\rfree+\depr)\Price_{t},
```

so the corporate tax has no effect on the cost of capital, and so none on the capital stock. The government takes the share {math}`\taxCorp` of the returns, but it also pays the same share of the cost; this is the neutrality of a tax on cash flow {cite:p}`brownCashFlowTax`. If instead the deductions match the true economic depreciation of the capital, a deduction of {math}`\depr` per period on capital that is itself depreciating at the rate {math}`\depr`, then {math}`z = \depr/(\rfree+\depr)` and

```{math}
\kapRent_{t} = \left(\frac{\rfree}{1-\taxCorp}+\depr\right)\Price_{t},
```

so the tax falls in full on the return to capital, which must be {math}`\rfree/(1-\taxCorp)` before tax to pay {math}`\rfree` after it. Actual tax codes lie in between. American law has at times allowed "bonus depreciation," an immediate deduction of part of the cost of new equipment: 100 percent from 2017 under the Tax Cuts and Jobs Act, falling by 20 percentage points a year after 2022, and 100 percent again, permanently, for property acquired after 19 January 2025 (Public Law 119-21).

For the [{math}`\q` model](#sec:qModel), the point is that deductions worth {math}`z` per dollar of investment work exactly like an investment tax credit at the rate {math}`\taxCorp z`, since both lower the after-tax price of capital by the same amount. So, for a given tax rate, a model with an ITC alone covers tax depreciation too.

Much of what is known about how strongly investment responds to the cost of capital comes from changes in taxes. {cite:t}`chh:reconsider` use tax reforms as natural experiments, and {cite:t}`hsITC` and {cite:t}`zwickMahonBonus` find large responses to bonus depreciation, especially in the timing of investment and among small firms; {cite:t}`czzTCJA` review the effects of the 2017 tax cuts. The neoclassical model with a Cobb-Douglas production function implies that the capital stock has an elasticity of {math}`-1` with respect to the cost of capital, while {cite:t}`cfmUserCost` estimate about {math}`-0.25` in firm-level data.

(HallJorgensonEuler)=
## The User Cost from the Firm's Euler Equation

The arbitrage argument can also be made as the solution of the firm's optimization problem, which brings out the parallel with the consumer's problem {cite:p}`jorgensonCapitalTheory`. In discrete time, a firm with no taxes that buys capital at the price {math}`\Price_{t}` and discounts by the riskless interest factor {math}`\Rfree = 1+\rfree` solves

```{math}
\max_{\{\inv_{t}\}} \sum_{t=0}^{\infty} \Rfree^{-t}\left[\fFunc(\kap_{t}) - \Price_{t}\inv_{t}\right] \quad \text{s.t.} \quad \kap_{t+1} = (1-\depr)\kap_{t}+\inv_{t}.
```

Buying one more unit of capital at {math}`t` costs {math}`\Price_{t}`; it raises output next period by {math}`\fFunc^{\prime}(\kap_{t+1})`, and what is left of it after depreciation can then be sold for {math}`(1-\depr)\Price_{t+1}`. At the optimum the firm is indifferent to that purchase:

```{math}
:label: eq:hjEuler

\Rfree = \frac{\fFunc^{\prime}(\kap_{t+1})+(1-\depr)\Price_{t+1}}{\Price_{t}}.
```

This is the consumer's Euler equation in the firm's clothes. The consumer equates the interest factor to the marginal rate of substitution, {math}`\Rfree = \uFunc^{\prime}(c_{t})/(\DiscFac\uFunc^{\prime}(c_{t+1}))`, and the firm equates it to the return on a unit of capital. Rearranging,

```{math}
\fFunc^{\prime}(\kap_{t+1}) = \Rfree\Price_{t} - (1-\depr)\Price_{t+1} = (\rfree+\depr)\Price_{t} - (1-\depr)\Delta\Price_{t+1} \approx (\rfree+\depr)\Price_{t} - \Delta\Price_{t+1},
```

the discrete-time counterpart of the user cost {math}`\kapRent_{t} = (\rfree+\depr)\Price_{t}-\dot{\Price}_{t}` in {eq}`eq:ctarb`.

## What the Model Leaves Out

Note that so far we have not derived a formula for investment; we have derived a formula for the *level* of the capital stock. But net investment is just the difference between the capital stock in periods {math}`t` and {math}`t-1`. Thus, the Hall-Jorgenson model of gross investment is

```{math}
\begin{gathered}\begin{aligned}
        \inv_{t-1} & =  \kap_{t}-\kap_{t-1}+\depr \kap_{t-1}  \\
         & =  \left(\Delta \frac{\inc_{t}}{\kapRent_{t}}\right)\kapShare+\depr \kap_{t-1}
\end{aligned}\end{gathered}
```

(where we neglect some minor complications having to do with the distinction between continuous and discrete time).

This exposes the model's weakness. A permanent change in the cost of capital, from a tax reform say, changes the desired capital stock at once, so in continuous time it implies an infinite rate of investment at the moment of the change, and in discrete time the whole adjustment within a single period. Investment in the data responds gradually. Hall and Jorgenson bridged the gap empirically by letting investment respond to changes in the desired capital stock with distributed lags, which fit the data but do not come from the firm's problem. Costs of adjustment, the subject of the [{math}`\q` model](#sec:qModel), derive the gradual response from the firm's own optimization.
