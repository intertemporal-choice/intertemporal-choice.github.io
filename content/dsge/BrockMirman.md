(sec:BrockMirman)=
# The Brock-Mirman Stochastic Growth Model

{cite:t}`brockmirman:growth` provided the first optimizing growth model with unpredictable (stochastic) shocks.

The social planner's goal is to solve the problem:

```{math}
\max ~~ \Ex\left[ \sum_{n=0}^{\infty} \Discount^{n} \log \Cons_{t+n}\right]
```

```{math}
:label: eq:delk

\begin{gathered}\begin{aligned}
         & \text{s.t.}  \nonumber
\\      \Kap_{t+1} & =  \Inc_{t}-\Cons_{t}
  \\  \Inc_{t+1}   & =  \PtyLev_{t+1} \Kap_{t+1}^{\kapShare}
\end{aligned}\end{gathered}
```

where {math}`\PtyLev_{t}` is the level of productivity in period {math}`t`, which is now allowed to be stochastic (alternative assumptions about the nature of productivity shocks are explored below). Note the key assumption

that the depreciation rate on capital is 100 percent.

%  and $\epsilon_{t}$ is an i.i.d.  shock to log productivity such that $E_{t-1} \epsilon_{t}=0$.

In this model the capital stock is not useful as a state variable: Because capital has a 100 percent depreciation rate, all that matters to the consumer when choosing how much to consume is how much income they have now, and not how that income breaks down into a part due to {math}`\Kap` and a part due to {math}`\PtyLev`.

The first step is to rewrite the problem in Bellman equation form

```{math}
\Value_{t}(\Inc_{t}) = \max_{\Cons_{t}} ~~ \log \Cons_{t} + \Discount \Ex_{t} [\Value_{t+1}(\Inc_{t+1})]
```

and take the first order condition:

```{math}
\begin{gathered}\begin{aligned}
        \uP(\Cons_{t}) & =  \Discount \Ex_{t}\left[\PtyLev_{t+1} \kapShare \Kap_{t+1}^{\kapShare-1} \uP(\Cons_{t+1})\right]  \\
        \frac{1}{\Cons_{t}} & =  \Discount \Ex_{t}\left[\frac{\PtyLev_{t+1} \kapShare \Kap_{t+1}^{\kapShare-1}}{\Cons_{t+1}}\right]  \\
        1 & =  \Discount \Ex_{t} \left[\underbrace{\kapShare \PtyLev_{t+1} \Kap_{t+1}^{\kapShare-1}}_{\equiv \Risky_{t+1}}\frac{\Cons_{t}}{\Cons_{t+1}}\right]
\end{aligned}\end{gathered}
```

where our definition of {math}`\Risky_{t+1}` helps clarify the relationship of this equation

to the usual consumption Euler equation (and you should think about why this is the

right definition of the interest factor in this model).

Now we show that this FOC is satisfied by the consumption function {math}`\Cons_{t} = \MPC \Inc_{t}`, where {math}`\MPC = 1-\kapShare \Discount`. To see this, note

first that the proposed consumption rule implies that {math}`\Kap_{t+1} = (1-\MPC) \Inc_{t}`.

The first order condition says

```{math}
\begin{gathered}\begin{aligned}
1  & =  \Discount \Ex_{t} \left[\kapShare \frac{\PtyLev_{t+1} \Kap_{t+1}^{\kapShare}}{\Kap_{t+1}}\frac{\MPC \Inc_{t}}{\MPC \Inc_{t+1}}\right]
\\  & =  \Discount \Ex_{t} \left[\kapShare \frac{\Inc_{t+1}}{\Kap_{t+1}}\frac{\MPC \Inc_{t}}{\MPC \Inc_{t+1}}\right]
\\ & =  \Discount \phantom{\Ex_{t}} \left[\kapShare \frac{\Inc_{t}}{\Kap_{t+1}}\right]
\\ & =  \Discount \phantom{\Ex_{t}} \left[\kapShare \frac{\Inc_{t}}{\Inc_{t}-\Cons_{t}}\right]
\\ & =  \Discount \phantom{\Ex_{t}} \left[\kapShare \frac{\Inc_{t}}{\Inc_{t}(1-\MPC)}\right]
\\ & =  \Discount \phantom{\Ex_{t}} \left[\kapShare \frac{1}{(1-\MPC)}\right]
\\ (1-\MPC) & =  \kapShare \Discount
\\ \MPC     & =  1-\kapShare \Discount.
\end{aligned}\end{gathered}
```

An important way of judging a macroeconomic

model and deciding whether it makes sense is to examine the model's

implications for the dynamics of aggregate variables. Defining lower

case variables as the log of the corresponding upper case variable,

this model says that the dynamics of the capital stock are given by

```{math}
:label: eq:BM-kDyn

\begin{gathered}\begin{aligned}
   \Kap_{t+1} & =  (1-\MPC) \Inc_{t}
\\ & =  \kapShare\Discount \PtyLev_{t}\Kap_{t}^{\kapShare}
\\ \kap_{t+1} & =  \log \kapShare\Discount + \ptyLev_{t} + \kapShare \kap_{t}
\end{aligned}\end{gathered}
```

which tells us that the dynamics of the (log) capital stock have two

components: One component ({math}`\ptyLev_{t}`) mirrors whatever happens

to the aggregate production technology; the other

is serially correlated with coefficient {math}`\kapShare` equal

to capital's share in output.

Similarly, since log output is simply {math}`\inc = \ptyLev + \kapShare \kap`, the dynamics

of output can be obtained from

```{math}
\begin{gathered}\begin{aligned}
  \inc_{t+1} & =  \ptyLev_{t+1} + \kapShare \kap_{t+1}
\\ & =  \kapShare (\log \Kap_{t+1}) + \ptyLev_{t+1}
\\ & =  \kapShare (\log \kapShare \Discount \Inc_{t}) + \ptyLev_{t+1}
\\ & =  \kapShare (\inc_{t} + \log \kapShare \Discount ) + \ptyLev_{t+1}
\end{aligned}\end{gathered}
```

so the dynamics of aggregate output, like aggregate capital,

reflect a component that mirrors {math}`\ptyLev` and a serially correlated

component with serial correlation coefficient {math}`\kapShare`.

The simplest assumption to make about the level of technology

is that its log follows a random walk:

```{math}
\begin{gathered}\begin{aligned}
  \ptyLev_{t+1} & =  \ptyLev_{t} + \epsilon_{t+1}.
\end{aligned}\end{gathered}
```

Under this assumption, consider the dynamic effects on the level of

output from a unit positive shock to

the log of technology in period {math}`t` (that is, {math}`\epsilon_{t+1}=1` where {math}`\epsilon_{s} = 0~\forall~s \neq t+1`). Suppose that

the economy had been at its original steady-state level of output {math}`\Target{y}`

in the prior period. Then the expected dynamics of output would be given

by

```{math}
\begin{gathered}\begin{aligned}
  \inc_{t} & =  \Target{y} + \ptyLev_{t}
\\ \Ex_{t}[\inc_{t+1}] & =  \Target{y}+\ptyLev_{t}+\kapShare \ptyLev_{t}
\\ \Ex_{t}[\inc_{t+2}] & =  \Target{y}+\ptyLev_{t}+\kapShare \ptyLev_{t}+\kapShare^{2} \ptyLev_{t}
\end{aligned}\end{gathered}
```

and so on, as depicted in {numref}`fig:zRandWalk`.

% \begin{figure}

% \caption{Dynamics of Output With a Random Walk Shock}

% \label{fig:zRandWalk}

% \includegraphics[width=6in]{../Figures/zRandWalk}

% \end{figure}

:::{figure} /content/figures/BrockMirman/yPlotBrockMirman.png
:name: fig:zRandWalk

Dynamics of Output With a Random Walk Shock
:::

Also interesting is the case where the level of

technology follows a white noise process,

```{math}
\begin{gathered}\begin{aligned}
  \ptyLev_{t+1} & =  \Target{\ptyLev} + \epsilon_{t+1}.
\end{aligned}\end{gathered}
```

The dynamics of income in this case are depicted in {numref}`fig:zWhiteNoise`.

:::{figure} /content/figures/BrockMirman/zWhiteNoise.png
:name: fig:zWhiteNoise

Dynamics of Output With A White Noise Shock
:::

The key point of this analysis, again, is that the dynamics of the model

are governed by two components: The dynamics of the technology shock, and

the assumption about the saving/accumulation process.

For further analysis, consider a nonstochastic version of this model,

with {math}`\PtyLev_{t} = 1 ~ \forall ~ t`. The consumption Euler equation is

```{math}
\begin{gathered}\begin{aligned}
        \frac{\Cons_{t+1}}{\Cons_{t}} & =  (\Discount \Rfree_{t+1})^{1/\CRRA}  \\
\end{aligned}\end{gathered}
```

But this is an economy with no technological progress, so the steady-state

interest rate must take on the value such that {math}`\Cons_{t+1}/\Cons_{t}=1`. Thus we

must have {math}`\Discount \Rfree = 1` or {math}`\Rfree = 1/\Discount`.

We can further derive the steady state level of capital of a nonstochastic version of the model in which {math}`\ptyLev_{t}=\ptyLev~\forall~t`

from {eq}`eq:BM-kDyn`:

```{math}
:label: eq:BM-kSS

\begin{gathered}\begin{aligned}
  \kap & =  \log \kapShare\Discount  + \ptyLev + \kapShare \kap
  \\ (1-\kapShare) \kap & =  \log \kapShare\Discount + \ptyLev
\\ \kap & =  \frac{\log \kapShare\Discount + \ptyLev}{1-\kapShare}
\end{aligned}\end{gathered}
```

The nonstochastic version of the model is of course not very interesting, except as a point of comparison to the stochastic version of the model. But what could be meant by the 'steady state' of a stochastic mdoel that never settles down? We can define a 'stochastic steady state' for such models in a number of (potentially) different ways:

*   The location (if one exists) to which the model will converge after an arbitrarily long period in which no shocks occurred {math}`\ptyLev_{t+1}=\ptyLev_{t}~\forall~t` (even if in every period agents *expect* that shocks will occur)

*   The mean value of some variable in the model (say, {math}`\Kap`)

*   The value of some state variable, say {math}`\Target{\Kap}`, such that {math}`\Ex_{t}[\Kap_{t+1}] = \Kap_{t}` if {math}`\Kap_{t}=\Target{\Kap}`.

We consider here the last of these, which we will show reduces (in this special case) to the same equation as for the nonstochastic version of the model, {math}`\Kap_{t+1}=\Kap_{t}`. To see this, rewrite the Euler equation as:

```{math}
\begin{gathered}\begin{aligned}
  1 & =  \Discount \Ex_{t} \left[\underbrace{\kapShare \PtyLev_{t+1} \Kap_{t+1}^{\kapShare-1}}_{\equiv \Risky_{t+1}}\frac{\Cons_{t}}{\Cons_{t+1}}\right]
  \\   1 & =  \Discount \Ex_{t} \left[\kapShare \PtyLev_{t+1} \Kap_{t+1}^{\kapShare-1}\frac{Y_{t}}{Y_{t+1}}\right]
  \\   1 & =  \Discount \Ex_{t} \left[\kapShare \PtyLev_{t+1} \Kap_{t+1}^{\kapShare-1}\frac{\PtyLev_{t} \Kap_{t}^{\kapShare}}{\PtyLev_{t+1} \Kap_{t+1}^{\kapShare}}\right]
  \\   1 & =  \Discount \Ex_{t} \left[\kapShare \Kap_{t+1}^{\kapShare-1}\frac{\PtyLev_{t} \Kap_{t}^{\kapShare}}{\Kap_{t+1}^{\kapShare}}\right]
  \\   1 & =  \Discount \left[\kapShare \Kap_{t+1}^{\kapShare-1}\frac{\PtyLev_{t} \Kap_{t}^{\kapShare}}{\Kap_{t+1}^{\kapShare}}\right]
%  \\   1 & =  \Discount \left[\kapShare \frac{\PtyLev_{t} \Kap_{t}^{\kapShare}}{\Kap_{t+1}}\right]
\end{aligned}\end{gathered}
```

where the expectations operator disappears because no variables are stochastic (the {math}`\PtyLev_{t+1}'s` in the numerator and denominator cancel, and {math}`\Kap_{t+1}` is directly chosen in {math}`t` so is known. For any given {math}`\PtyLev_{t}`, the steady state where {math}`\Kap_{t+1}=\Kap_{t}=\Target{\Kap}` is then where

```{math}
\begin{gathered}\begin{aligned}
  1 & =  \Discount \kapShare \PtyLev_{t} \Target{\Kap}_{t}^{\kapShare-1}
\\ \Target{\kap} & =  \frac{\log \Discount \kapShare + \ptyLev_{t}}{1-\kapShare}
\end{aligned}\end{gathered}
```

which is the generalization of the nonstochastic solution derived in {eq}`eq:BM-kSS`.

The result that the nonstochastic and stochastic steady states are the same is special to the Brock-Mirman model; it is NOT true of many other models of growth; it occurs here because the linearity of the consumption function, among other special assumptions. Furthermore, the third of our possible definitions of a steady state will generally differ at least a little bit from either of the first two.

