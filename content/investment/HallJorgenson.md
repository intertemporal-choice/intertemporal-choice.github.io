(sec:HallJorgenson)=
# The Hall-Jorgenson Model of Investment
{cite:t}`hall&jorgenson:i` consider the problem of a firm that produces output using capital {math}`\kap` as its only input,

```{math}
\begin{gathered}\begin{aligned}
       \inc  & =  \fFunc(\kap)
\end{aligned}\end{gathered}
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
\fFunc^{\prime}(k_{t}) & =  \kapRent_{t}
\\        \kapShare \kap_{t}^{\kapShare-1} & =  \kapRent_{t}  \\
         (\inc_{t}/\kap_{t}) \kapShare & =  \kapRent_{t}  \\
        \kap_{t} & =  (\inc_{t}/\kapRent_{t})\kapShare .
\end{aligned}\end{gathered}
```

This equation says the level of capital is always instantly adjusted to {math}`\inc_{t}` and {math}`\kapRent_{t}`, with no costs of adjustment.

What determines the cost of capital? In the simple case with no taxes and no capital market frictions of any kind, an investor must be indifferent between putting his money in the bank and earning interest at rate {math}`\rfree`, and buying a unit of capital, renting it out at rate {math}`\kapRent_{t}`, and then reselling it the next period.

The purchase price at which capital goods can be bought at date {math}`t` (distinct from the rental rate, and typically much larger) is:

```{math}
\begin{gathered}\begin{aligned}
        \Price_{t} & - & \text{purchase price of one unit of capital},
\end{aligned}\end{gathered}
```

and in continuous time, the rate of change of {math}`\Price_{t}` is {math}`\dot{\Price}_{t}`. Assume that capital depreciates geometrically at rate {math}`\depr`. The net profit from the *continuous time* purchase-and-rent strategy is

```{math}
\begin{gathered}\begin{aligned}
        \kapRent_{t}-\depr \Price_{t}+\dot{\Price}_{t} & - & \text{Income from renting, minus loss from depreciation}  \\
         &   \text{plus capital gain from the change in price of capital}.
\end{aligned}\end{gathered}
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
         & =  \kapShare \inc_{t}/(\rfree+\depr)\Price_{t}.
\end{aligned}\end{gathered}
```

Now let's introduce taxes, defined as follows:

```{math}
\begin{gathered}\begin{aligned}
        \taxCorp & - & \text{corporate tax rate ($\approx 0.34$ in US) }
\\      \itc & - & \text{investment tax credit (sometimes 10 percent, sometimes 0) }
\end{aligned}\end{gathered}
```

The net, discounted, after-tax price of capital to the firm is[^footnote1]

[^footnote1]: Assume that if the firm sells the capital, it must repay the ITC on a pro-rata basis; this prevents tax arbitrage opportunities.

```{math}
\begin{gathered}\begin{aligned}
        \hat{\Price}_{t} & =  (1-\itc) \Price_{t}.
\end{aligned}\end{gathered}
```

Now let's rewrite the arbitrage equation {eq}`eq:ctarb` taking account of taxes. The rental income {math}`\kapRent_{t}` must be multiplied by {math}`(1-\taxCorp)` because the capital-rental business must pay taxes too:

```{math}
\begin{gathered}\begin{aligned}
        (\rfree+\depr) \hat{\Price}_{t} & =  (1-\taxCorp) \kapRent_{t}+\dot{\hat{\Price}}_{t}.
\end{aligned}\end{gathered}
```

If we simplify again by assuming that {math}`\dot{\hat{\Price}}_{t}=0`, we have

```{math}
\begin{gathered}\begin{aligned}
        \kapRent_{t} & =  (\rfree+\depr)\Price_{t}(1-\itc)/(1-\taxCorp)
.
\end{aligned}\end{gathered}
```

Note that so far we have not derived a formula for investment - we have derived a formula for the *level* of the capital stock. But net investment is just the difference between the capital stock in periods {math}`t` and {math}`t-1`. Thus, the Hall-Jorgenson model of gross investment is

```{math}
\begin{gathered}\begin{aligned}
        \inv_{t-1} & =  \kap_{t}-\kap_{t-1}+\depr \kap_{t-1}  \\
         & =  \left(\Delta \frac{\inc_{t}}{\kapRent_{t}}\right)\kapShare+\depr \kap_{t-1}
\end{aligned}\end{gathered}
```

(where we neglect some minor complications having to do with the distinction between continuous and discrete time).
