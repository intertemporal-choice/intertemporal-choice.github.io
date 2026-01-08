(sec:GrowthAndGrossSaving)=
# Gross Saving and Growth in the RCK Model

In the neoclassical growth model with labor-augmenting technological

progress at rate {math}`\pGro`, utility function {math}`\util(c) = c^{1-\CRRA}/(1-\CRRA)`,

time preference rate {math}`\DiscRate` and depreciation rate {math}`\delta` the

steady-state will be at the point where the growth rate of consumption

is equal to the growth rate of labor-augmenting technological

progress, {math}`\pGro`,

```{math}
\begin{gathered}\begin{aligned}
        \frac{\dot{C}}{C} & =  \CRRA^{-1}(f^{\prime}(k)-\delta-\DiscRate)  \\
         & =  \pGro  
\end{aligned}\end{gathered}
```

which implies that

```{math}
\begin{gathered}\begin{aligned}
        f^{\prime}(k) & =  \CRRA \pGro + \DiscRate + \delta  \\
        \alpha k^{\alpha-1} & =  \CRRA \pGro + \DiscRate + \delta  \\
    k & =  \left[\frac{\CRRA \pGro + \DiscRate + \delta}{\alpha}\right]^{\frac{1}{\alpha-1}}. 
\end{aligned}\end{gathered}
```

The aggregate gross saving rate is defined as

```{math}
:label: eq:grossavrate

\begin{gathered}\begin{aligned}
     s & =     \frac{y-c}{y} \\
         & =  \frac{k^{\alpha}-c}{k^{\alpha}} \\
         & =  1-c/k^{\alpha}. 
\end{aligned}\end{gathered}
```

In steady-state by definition

```{math}
:label: eq:kdotOk

\begin{gathered}\begin{aligned}
        \dot{k} & =  0  
\end{aligned}\end{gathered}
```

but from the capital accumulation equation we know that

```{math}
:label: eq:dotk

\begin{gathered}\begin{aligned}
        \dot{k} & =  k^{\alpha}-(\delta+\pGro)k - c 
\end{aligned}\end{gathered}
```

so in steady-state

```{math}
\begin{gathered}\begin{aligned}
        c & =  k^{\alpha}-(\delta+\pGro)k.
\end{aligned}\end{gathered}
```

This can be substituted into {eq}`eq:grossavrate` to obtain

```{math}
\begin{gathered}\begin{aligned}
        s & =  1-\frac{k^{\alpha}-(\delta+\pGro)k}{k^{\alpha}}  \\
         & =  (\delta+\pGro)k^{1-\alpha}
\end{aligned}\end{gathered}
```

and the expression for the steady-state level of capital per capita

can be substituted in to yield

```{math}
\begin{gathered}\begin{aligned}
        s & =  (\delta+\pGro)\left(\frac{\CRRA \pGro+ \DiscRate + \delta}{\alpha}\right)^{-1}  
\\ & =  \left(\frac{\alpha(\pGro+\delta)}{\delta+\DiscRate+\CRRA \pGro}\right)     
\end{aligned}\end{gathered}
```

The derivative of this expression with respect to {math}`\pGro` is

```{math}
\begin{gathered}\begin{aligned}
        \frac{ds}{d\pGro} & =  \left(\frac{\alpha(\delta + \DiscRate + \CRRA \pGro)-\alpha 
(\pGro+\delta) \CRRA}{(\delta+\DiscRate+\CRRA \pGro)^{2}}\right)
\\ & =  \left(\frac{\alpha(\delta(1-\CRRA) + \DiscRate)}{(\delta+\DiscRate+\CRRA 
\pGro)^{2}}\right)
.
\end{aligned}\end{gathered}
```

This will be positive if its numerator is positive, i.e. if

```{math}
\begin{gathered}\begin{aligned}
         \CRRA \delta & <  \DiscRate + \delta
\\  \CRRA & <  1+\DiscRate/\delta  .
\end{aligned}\end{gathered}
```

A typical assumption is {math}`\DiscRate = .04` and {math}`\delta = .08`, implying that

the steady-state relationship between saving and growth in the neoclassical

model is positive only if the coefficient of relative risk aversion {math}`\CRRA`

is less than 1.5. Typically we assume values of {math}`\CRRA` in the range from

2 to 5, so the model leads us to expect a negative relationship between saving

and growth.