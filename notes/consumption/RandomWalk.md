(sec:RandomWalk)=

# The Random Walk Model of Consumption
This section derives the {cite:t}`hallRandomWalk` random walk proposition for consumption.

The consumption Euler equation when future consumption is uncertain takes the form[^euler-derivation]

[^euler-derivation]: See the [](#sec:Envelope) for the derivation of the Euler equation in the perfect foresight case; we will show later that the consequence of uncertainty is simply to insert the expectations operator.

```{math}
:label: eq:uPEuler

\uFunc^{\prime}(\cRat_{t}) = \Discount \Rfree \Ex_{t}[\uFunc^{\prime}(\cRat_{t+1})].
```

Suppose the utility function is quadratic:

```{math}
\uFunc(\cRat) = -(1/2) (\cancel{\cRat}-\cRat)^{2}
```

where {math}`\cancel{\cRat}` is the "bliss point" level of consumption.[^bliss-point] Marginal utility is

[^bliss-point]: Assume that the consumer is sufficiently poor that it will be impossible for them ever to achieve consumption as large as {math}`\cancel{\cRat}`.

```{math}
\uFunc^{\prime}(\cRat) = (\cancel{\cRat}-\cRat)
```

and suppose further that {math}`\Rfree \Discount = 1` so that {eq}`eq:uPEuler` becomes

```{math}
\begin{aligned}
  (\cancel{\cRat}-\cRat_{t})  & =  \Ex_{t}[(\cancel{\cRat}-\cRat_{t+1})]
\\ \Ex_{t}[\cRat_{t+1}] & =  \cRat_{t}.
\end{aligned}
```

Defining the innovation to consumption as

```{math}
\begin{aligned}
  \epsilon_{t+1} & =  \cRat_{t+1}-\cRat_{t}
\\ & \equiv  \Delta \cRat_{t+1},
\end{aligned}
```

the random walk proposition is simply that the expectation of consumption changes is zero:

```{math}
\Ex_{t}[\Delta \cRat_{t+1}] = 0.
```

This means that no information known to the consumer when the consumption choice {math}`\cRat_{t}` was made can have any predictive power for how consumption will change between period {math}`t` and {math}`t+1` (or for any date beyond {math}`t+1`).
