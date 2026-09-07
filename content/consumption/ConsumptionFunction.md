(sec:ConsumptionFunction)=
# Consumption Functions and the Permanent Income Hypothesis

This section derives the consumption function (the relation between consumption spending and the consumer's economic circumstances) for an optimizing consumer with Certainty Equivalent (CEQ) preferences like those assumed by {cite:t}`hallRandomWalk` and with an income process that has a purely transitory and a purely permanent component.

The consumer wants to

```{math}
\max ~~ \Ex_{t}\left[\sum_{n=0}^{\infty} \Discount^{n} \uFunc({c}_{\tNow+n})\right]
```

subject to the constraint

```{math}
\bRat_{t+1} = (\bRat_{t}+\yRat_{t}-\cRat_{t})\Rfree
```

where {math}`\bRat_{t}` is the consumer's beginning-of-period bank balances, {math}`\yRat_{t}` is current labor income, {math}`\Rfree=(1+\rfree)` is the constant interest factor and {math}`\Discount` is the time preference factor. Suppose the consumer has quadratic utility {math}`\uFunc({c}) = -(1/2)(\cancel{c}-c)^{2}` where {math}`\cancel{c}` is the "bliss point" level of consumption. Assume further that {math}`\Discount \Rfree=1`.

Under these circumstances, the [random walk](#sec:RandomWalk) section shows that consumption will follow a random walk,

```{math}
:label: eq:ConsFunc-rwc

\begin{aligned}
\Delta \cRat_{t+1} & = \epsilon_{t+1}, \\
\Ex_{t}[\epsilon_{t+n}] & = 0 ~\forall~n>0.
\end{aligned}
```

{cite:t}`hallRandomWalk` tested this proposition by examining whether lagged variables had predictive power for consumption growth. Hall's approach largely supplanted a vast earlier literature that had attempted to estimate "the consumption function" which was interpreted as the relationship between observed economic variables like income, and household spending. The "Keynesian" consumption function, for example, was something along the lines of

```{math}
:label: eq:KeynesianC

\begin{aligned}
    \cRat_{t} & = \alpha_{0} + \alpha_{1} \yRat_{t} \\
\Delta  \cRat_{t} & = \alpha_{1} \Delta \yRat_{t}
\end{aligned}
```

where {math}`\yRat_{t}` was disposable household income.

The reason Hall's approach was attractive is that {cite:t}`muthOptimal` showed that the appropriate response of consumption to, say, a shock to current income depends on whether that income shock is transitory or permanent.

To see Muth's point clearly, suppose that the labor income process is

```{math}
\begin{aligned}
        p_{t+1} & = p_{t}+\psi_{t+1} \\
      \yRat_{t+1} & = p_{t+1}+\theta_{t+1},
\end{aligned}
```

where {math}`\theta` is a white noise variable representing a transitory shock to labor income and {math}`\psi` is a white noise variable representing a shock to permanent labor income, {math}`\Ex_{t}[\theta_{t+n}]= \Ex_{t}[\psi_{t+n}]= 0~\forall~n>0`.

We can solve for the level of consumption using the Intertemporal Budget Constraint, which says that the expected PDV of consumption must equal the expected PDV of total wealth, human and nonhuman:

```{math}
\left[\sum_{n=0}^{\infty} \Rfree^{n} \cRat_{\tNow+n}\right] = \bRat_{t} + \left[\sum_{n=0}^{\infty} \Rfree^{n}\yRat_{\tNow+n}\right]
```

Since the IBC must hold for any possible set of realizations of the stochastic shocks, it must hold in expectation, so

```{math}
:label: eq:crlevel

\begin{aligned}
      \Ex_{t}\left[\sum_{s=t}^{\infty} \Rfree^{t-s}\right] \cRat_{t} & = \bRat_{t} + \theta_{t} + \Ex_{t}\left[\sum_{s=t}^{\infty} \Rfree^{t-s}p_{s}\right] \\
      \left(\frac{1}{1-\Rfree^{-1}}\right) \cRat_{t} & = \bRat_{t}+\theta_{t}+p_{t}\left(\frac{1}{1-\Rfree^{-1}}\right) \\
  \cRat_{t} & = \left(\Rfree/\Rfree - 1/\Rfree\right) (\bRat_{t}+\theta_{t}) + p_{t} \\
  \cRat_{t} & = \left(\frac{\rfree}{\Rfree}\right) (\bRat_{t}+\theta_{t}) + p_{t}.
\end{aligned}
```

From {eq}`eq:crlevel` we can see that if a given shock to income is perceived to be transitory, then the marginal propensity to consume will be {math}`\alpha_{1}=(\rfree/\Rfree)` which is a small number (say, 0.05) while if the shock is perceived to be permanent then {math}`\alpha_{1}` will be 1.0. So there is no such thing as the "true" value of {math}`\alpha_{1}` and the "consumption function" conceived as an estimated version of {eq}`eq:KeynesianC` is meaningless (though the consumption function conceived as {eq}`eq:crlevel` is perfectly sensible).

This problem with the existing literature explains why Hall's innovation was so exciting: He showed a way to test the theory that did not depend on arbitrary and difficult-to-test assumptions about decisionmakers' beliefs about the structure of the income process.
