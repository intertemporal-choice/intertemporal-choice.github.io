(sec:CampManCRRAWithTimeVaryingR)=
# Dynamics of Consumption with Time Varying R

The intertemporal budget constraint for an infinite-horizon representative agent can be written as

```{math}
\begin{aligned}
\PDV_{t}(C) & = \Wmid_{t}+ \overbrace{\PDV_{t}(Y)}^{\equiv \Whum_{t}} \\
& = \WRat_{t}
\end{aligned}
```

where {math}`\Wmid_{t}` is the consumer's beginning-of-period stock of physical assets, {math}`\Whum_{t}` is human wealth, and {math}`\WRat_{t}` is total wealth, human and nonhuman.

{math}`\Rfree_{t+1}` is the riskless, but time-varying, return factor at {math}`t+1`, and so we can define the dynamic budget constraint for total wealth as

```{math}
:label: eq:CM-dbc

\WRat_{t+1} = (\WRat_{t}-\CRat_{t})\Rfree_{t+1}.
```

{cite:t}`cmModel` show that the dynamic budget constraint can be manipulated to generate an expression relating the current levels of wealth and consumption to future interest rates. First, divide both sides of {eq}`eq:CM-dbc` by {math}`\WRat_{t}` to obtain

```{math}
\begin{aligned}
% \WRat_{t+1} & = \Rfree_{t+1}\left(\WRat_{t}-\CRat_{t}\right) \\
\left(\frac{\WRat_{t+1}}{\WRat_{t}}\right) & = \left(1-\frac{\CRat_{t}}{\WRat_{t}}\right)\Rfree_{t+1} \\
\Delta \wRat_{t+1} & \approx \rfree_{t+1}+ \log(1-\exp(c_{t}-\wRat_{t})),
\end{aligned}
```

where the lower-case variables represent the logarithms of their upper-case equivalents. Define {math}`x_{t} \equiv c_{t}-\wRat_{t}` and assume that any variations in interest rates over time are stationary, {math}`\lim_{n \rightarrow \infty} \Ex_{t}[\Rfree_{t+n}] = \Rfree`. In this case, the ratio of consumption to total wealth {math}`x_{t}` will be a stationary variable. It seems reasonable, therefore, to consider a Taylor expansion of the DBC around the steady-state value for {math}`c_{t}-\wRat_{t}`, which we will designate as {math}`x`

```{math}
\begin{aligned}
\Delta \wRat_{t+1} & \approx \rfree_{t+1} + \log(1-\exp(x_{t})) \\
& \approx \rfree_{t+1} + \log(1-\exp(x))+\left(\frac{d}{dx}\log(1-\exp(x))\right)(x_{t}-x) \\
& = \rfree_{t+1} + \log(1-\exp(x))-\left(\frac{\exp(x)}{1-\exp(x)}\right)(x_{t}-x),
\end{aligned}
```

or, for simplicity defining a constant {math}`\xi = 1-\exp(x)` (which will be a number slightly less than one)[^xi-note]

[^xi-note]: {math}`\xi` slightly less than one because {math}`\exp(x) = C/W` is small.

```{math}
:label: eq:dw1

\begin{aligned}
\Delta \wRat_{t+1} & \approx \rfree_{t+1} + \log \xi +\left(\frac{1-\exp(x)-1}{\xi}\right)(x_{t}-x) \\
& = \rfree_{t+1} + \log \xi +\left(\frac{\xi-1}{\xi}\right)(x_{t}-x) \\
& = \rfree_{t+1} + \log \xi +\left(1-\frac{1}{\xi}\right)(x_{t}-x) \\
& = \log \xi - (1-1/\xi) x + \rfree_{t+1}+\left(1-\frac{1}{\xi}\right)(c_{t}-\wRat_{t}) \\
& = \underbrace{\log \xi - (1-1/\xi) \log \xi}_{\equiv k} + \rfree_{t+1}+\left(1-\frac{1}{\xi}\right)(c_{t}-\wRat_{t}) \\
& = k + \rfree_{t+1}+\left(1-\frac{1}{\xi}\right)(c_{t}-\wRat_{t}).
\end{aligned}
```

But the definition of the change in wealth is

```{math}
:label: eq:dw2

\begin{aligned}
\Delta \wRat_{t} & = \wRat_{t+1}-\wRat_{t} \\
& = \wRat_{t+1}-c_{t+1}+c_{t+1}-c_{t}+c_{t} -\wRat_{t} \\
& = \Delta c_{t+1}+(c_{t}-\wRat_{t})-(c_{t+1}-\wRat_{t+1})
\end{aligned}
```

Now set {eq}`eq:dw2` equal to {eq}`eq:dw1` and solve for {math}`c_{t}-\wRat_{t}` to get

```{math}
\begin{aligned}
\Delta c_{t+1}+(c_{t}-\wRat_{t})-(c_{t+1}-\wRat_{t+1}) & = k + \rfree_{t+1}+\left(1-\frac{1}{\xi}\right)(c_{t}-\wRat_{t}) \\
(c_{t}-\wRat_{t})\left[1-\left(1-\frac{1}{\xi}\right) \right] & = k + \rfree_{t+1} + (c_{t+1}-\wRat_{t+1}) \\
c_{t}-\wRat_{t} & = \xi(\rfree_{t+1}-\Delta c_{t+1}) + \xi (c_{t+1}-\wRat_{t+1}) + \xi k.
\end{aligned}
```

Of course, an equivalent expression can be derived for {math}`c_{t+1}-\wRat_{t+1}`; repeated substitution leads to

```{math}
:label: eq:ibcapprox

\begin{aligned}
c_{t}-\wRat_{t} & = \xi(\rfree_{t+1}-\Delta c_{t+1}) + \xi (\xi (\rfree_{t+2}-\Delta c_{t+2}) + \xi (c_{t+2}-\wRat_{t+2}) + \xi k) + \xi k \\
& = \sum_{j=1}^{\infty} \xi^{j}(\rfree_{t+j}-\Delta c_{t+j})+\xi k/(1-\xi).
\end{aligned}
```

This equation is interesting: It says that the ratio of consumption to wealth today (that is, the log difference) must equal the discounted value of the rate of return on wealth minus the growth rate of consumption, plus a constant term. Note that this result derives purely from the dynamic budget constraint, with no behavioral assumptions yet. Thus, holding consumption growth and current wealth constant, higher future interest rates must correspond to higher current consumption. This is just the income effect: If interest rates are higher and future consumption growth the same, you will have more lifetime resources and therefore must spend more today if all resources are to be exhausted (as the IBC requires). Alternatively, if you will have fast consumption growth in the future, you need to have either low consumption today or higher interest rates in the future to earn the income required to finance that fast consumption growth.

This equation is purely the result of the dynamic budget constraint; so far we have said nothing about how consumption is chosen. Now consider a perfect-foresight CRRA utility {math}`\uFunc(c)=c^{1-\CRRA}/(1-\CRRA)` model with risk aversion {math}`\CRRA`, which implies the Euler equation

```{math}
\begin{aligned}
\left(\frac{{C}_{t+1}}{\CRat_{t}}\right) & = (\Rfree_{t+1}\Discount)^{1/\CRRA} \\
\Delta c_{t+1} & = \underbrace{\CRRA^{-1} \log \Discount}_{\equiv \mu} + \CRRA^{-1} \rfree_{t+1}
\end{aligned}
```

where {math}`\CRRA^{-1}` is the intertemporal elasticity of substitution. This equation for consumption growth can be substituted into {eq}`eq:ibcapprox`, to generate

```{math}
:label: eq:cw

c_{t}-\wRat_{t} = (1-\CRRA^{-1})\sum_{j=1}^{\infty} \xi^{j}\rfree_{t+j}+\xi (k-\mu)/(1-\xi).
```

All of these results were derived under the assumption of perfect foresight: Interest rates vary over time, but the consumer knows in advance what the pattern of variation will be. If we wish to allow for truly stochastic interest rates, things get somewhat more complicated. Recall that if interest rates are fixed at {math}`\Rfree` and income grows by factor {math}`\WGro` from period to period, human wealth is

```{math}
\begin{aligned}
\Whum_{t} & = \left(\frac{Y_{t}}{1-\WGro/\Rfree}\right) \\
& \approx \left(\frac{Y_{t}}{\rfree-\wGro}\right).
\end{aligned}
```

{cite:t}`summersCapTax` showed that a permanent change in interest rates has an enormous effect on the value of human wealth. In a model with stochastic interest rates, there is still a large human wealth effect even if interest rates eventually return to some "natural" rate following a shock. Thus, a proper analysis of the effect of changes in interest rates must take account of the effect of that change not only on the expectations of future interest rates on the RHS of {eq}`eq:cw` but also on the level of total wealth {math}`\wRat_{t}` on the LHS of that equation.
