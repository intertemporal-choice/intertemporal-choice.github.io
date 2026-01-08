(sec:CARAPortfolio)=

# Portfolio Choice With CARA Utility

Consider a consumer with Constant Absolute Risk Aversion
utility
{math}`\uFunc(\cRat) = -\CARA^{-1} e^{-\alpha \cRat_{}}`, with assets
{math}`\aLev_{T-1}` who is deciding how much to invest in a risky security that
will earn a normally distributed stochastic return {math}`\Risky_{T} \sim
\mathcal{N}(\Risky,\sigma)` versus a safe asset that will earn return
{math}`\Rfree < \Risky` (the risky asset gets a bold font because you must be a bold person to invest in a risky asset!).[^fn1][^fn2]

[^fn1]: The seminal paper examining this problem (in continuous time) was by {cite:t}`merton:restat`; that paper also examines the case with CRRA utility and lognormal returns.

[^fn2]: The assumption that returns are normally distributed is highly implausible. This means that with some positive probability, {math}`\Risky_{T} < 0`. So, owning a \$1 of the risky asset in period {math}`T-1` could result in *negative* wealth in period {math}`T`. You can lose *more than everything*, which is a violation of the legal principle of limited liability. (For a detailed history of limited liability, see {cite:t}`micklethwaitWooldridgeCompany`.) Lognormally distributed returns are therefore much more plausible.

Consumption in the last period of life will be the entire amount
of resources. If the consumer invests an absolute amount of money \${math}`\Stocks` in the risky asset, then

```{math}
\begin{gathered}\begin{aligned}
        \cRat_{T} & =  \Stocks \Risky_{T}+( \aLev_{T-1}-\Stocks)\Rfree  \\
         & =   \aLev_{T-1}\Rfree + \underbrace{(\Risky_{T}-\Rfree)}_{\equiv \EPrem_{T}}\Stocks
\end{aligned}\end{gathered}
```

% \\ & = \aLev_{T-1}\Rfree + \EPrem_{T} \Stocks

where {math}`\EPrem_{T}` is the "excess return" realized in period {math}`T`. Note that {math}`\EPrem_{T}` could be negative: if the risky asset performs badly enough, shareholders lose not just the excess return they hoped to earn, but part of what they would have earned from the safe asset. Given {math}`\Stocks` and defining the expected risk premium as the expected value of the expected return {math}`\EPrem = \Ex_{T-1}[\Risky_{T}-\Rfree]`, the expectation as of time {math}`T-1` is:

```{math}
:label: eq:last

\begin{gathered}\begin{aligned}
        \Ex_{T-1}[\uFunc(\cRat_{T})] & =  \Ex_{T-1}[-\CARA^{-1}e^{-\alpha( \aLev_{T-1}\Rfree+(\Risky_{T}-\Rfree)\Stocks)}]
\\ & =  -\CARA^{-1}e^{-\alpha( \aLev_{T-1}\Rfree)} \Ex_{T-1}[e^{-\alpha(\Risky_{T}-\Rfree)\Stocks}]
\\ & =  -\CARA^{-1}e^{-\alpha( \aLev_{T-1}\Rfree)} e^{-\alpha\Stocks\EPrem+(\alpha\Stocks)^{2}\sigma^{2}/2}
\\ & =  -\CARA^{-1} e^{-\alpha( \aLev_{T-1}\Rfree)}
e^{-\alpha(\Stocks\EPrem-\alpha\Stocks^{2}\sigma^{2}/2)}
\end{aligned}\end{gathered}
```

% \label{eq:removeconst}

and the third line follows from the second because if {math}`z \sim \mathcal{N}(\EPrem_{z},\sigma_{z}^{2})`
then {math}`\Ex[e^{z}] = e^{\EPrem_{z}+\sigma_{z}^{2}/2}.` (See [ELogNorm](#fact:elognorm)).

Because {eq}`eq:last` is negative, the optimal {math}`\Stocks` will be the
one that yields the largest negative exponent on {math}`e`, which occurs at the value of {math}`S`
given by

```{math}
\max_{\Stocks} \left\{ \Stocks \EPrem - \frac{\alpha \Stocks^{2} \sigma^{2}}{2} \right\}
```

with FOC

```{math}
\begin{gathered}\begin{aligned}
        \EPrem & =  \alpha \Stocks \sigma^{2}  \\
        \Stocks & =  \frac{\EPrem}{\alpha \sigma^{2}}.
\end{aligned}\end{gathered}
```

This yields the intuitive result that the greater is risk aversion or
the greater is the risk, the less the consumer wants to invest in the
risky asset, while the greater is the expected excess return, the more
the consumer wants to invest. Note, however, that the model
implausibly says that the dollar amount invested in the risky asset
does not depend on the total dollar amount of resources {math}`\aLev_{T-1}`.
So, Warren Buffett and Homer Simpson should have the exact same dollar
holdings of the risky asset! If Buffett is richer than Simpson, Buffett's
excess wealth is held in the safe form. Not very plausible. (That is why
models with CARA utility are increasingly unfashionable in the economics and finance literatures).
