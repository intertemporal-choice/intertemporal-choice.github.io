(sec:RandomWalk)=
# The Random Walk Model of Consumption

This section derives the {cite:t}`hallRandomWalk` random walk proposition for consumption.

The consumption Euler equation when future consumption is uncertain takes the form

:::{margin}
See the [Envelope theorem](#sec:Envelope) section for the derivation of the Euler equation in the perfect foresight case; we will show later that the consequence of uncertainty is simply to insert the expectations operator.
:::

```{math}
:label: eq:uPEuler

\uFunc^{\prime}(\cNrm_{t}) = \DiscFac \Rfree \Ex_{t}[\uFunc^{\prime}(\cNrm_{t+1})].
```

Suppose the utility function is quadratic:

```{math}
\uFunc(\cNrm) = -(1/2) (\cancel{\cNrm}-\cNrm)^{2}
```

where {math}`\cancel{\cNrm}` is the "bliss point" level of consumption. Marginal utility is

:::{margin}
Assume that the consumer is sufficiently poor that it will be impossible for them ever to achieve consumption as large as {math}`\cancel{\cNrm}`.
:::

```{math}
\uFunc^{\prime}(\cNrm) = (\cancel{\cNrm}-\cNrm)
```

and suppose further that {math}`\Rfree \DiscFac = 1` so that {eq}`eq:uPEuler` becomes

```{math}
\begin{aligned}
  (\cancel{\cNrm}-\cNrm_{t})  & =  \Ex_{t}[(\cancel{\cNrm}-\cNrm_{t+1})]
\\ \Ex_{t}[\cNrm_{t+1}] & =  \cNrm_{t}.
\end{aligned}
```

Defining the innovation to consumption as

```{math}
\begin{aligned}
  \epsilon_{t+1} & =  \cNrm_{t+1}-\cNrm_{t}
\\ & \equiv  \Delta \cNrm_{t+1},
\end{aligned}
```

the random walk proposition is simply that the expectation of consumption changes is zero:

```{math}
\Ex_{t}[\Delta \cNrm_{t+1}] = 0.
```

This means that no information known to the consumer when the consumption choice {math}`\cNrm_{t}` was made can have any predictive power for how consumption will change between period {math}`t` and {math}`t+1` (or for any date beyond {math}`t+1`).
