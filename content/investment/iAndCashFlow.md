(sec:iAndCashFlow)=
# Investment and Cash Flow With Imperfect Capital Markets
Many models of capital market imperfections reach the conclusion that financing an investment project is cheaper with "internal" than with "external" funds. (Internal funds are those that the firm owns, for example, in its bank account; external funds are obtained from outsiders like banks or new investors). For a lucid exposition of an example of models of this kind, see the discussion of financial market imperfections in {cite:t}`romer:text`.

Such models tend to be highly specialized, with entrepreneurs who miraculously receive exogenously specified endowments of "internal" cash and who make a one- (or at most two-) period investment decision. This is a striking contrast with the generality of the canonical {math}`\q` model of investment in which optimizing firms make investment decisions that take into account infinite future paths of adjustment costs, marginal products of capital, taxes, and all other features of the environment.

But models with imperfect capital markets are always very clear on who receives what cash, when, and why. In contrast, the power of the {math}`\q` model comes at a high cost: The model has no implications whatsoever for the firm's decisions about when and how to make payments to shareholders and lenders.

## Modigliani-Miller

To see this, consider the benchmark discrete-time framework in the [](#sec:qModel) without taxes or depreciation, and (as in that section) assume that the firm issues or repurchases shares to maintain a number of shares {math}`s_{t}` outstanding equal to the size of the physical capital stock (so {math}`s_{t}=k_{t}` in every period). Suppose we assume that the firm has a "dividend policy": In every period, it pays to each shareholder a dividend equal to the flow of revenues per share.

In this case, the value of all the firm's shares {math}`s_{t}` (the equity value of the firm) will be

```{math}
\begin{aligned}
  \hat{\vFirm}_{t}(s_{t}) & = \max_{\{i\}_{t}^{\infty}}~\Ex_{t}\left[\sum_{n=0}^{\infty} \Discount^{n} \left(\pi_{t+n}-\xpend_{t+n}\right)\right].
\end{aligned}
```

(Notice that because the firm always has {math}`s_{t} = k_{t},` the value of the firm's shares defined here {math}`\hat{\vFirm}_{t}(s_{t})` is identical to the value of the firm's capital {math}`{\vFirm}_{t}(k_{t})` defined in the [](#sec:qModel).)

Now suppose the firm decides to deviate, just a little bit, from this dividend policy. It issues an extra share in period {math}`t`, which (assuming capital markets are efficient) raises an amount of money equal to the share price {math}`\lambda_{t}`; it invests the proceeds in the riskless asset, earning return {math}`\Rfree`, then pays out the resulting cash to shareholders in the next period. However, we assume that the firm continues to maximize its value. This modifies the infinite sum to:

```{math}
\begin{aligned}
  \max_{\{i\}_{t}^{\infty}}~\Ex_{t}\left[\sum_{n=0}^{\infty} \beta^{n} \left(\pi_{t+n}-\xpend_{t+n}\right)\right]+ \lambda_{t} - \Rfree\beta \lambda_{t}.
\end{aligned}
```

but since by assumption {math}`\beta = \Rfree^{-1}` this expression reduces to the original expression.

The point can be extended to show that the firm can raise an arbitrary amount of money in one period, paying it back in another, or vice versa, without having any effect on its value or its optimal investment plans.

This is an example of the famous theorem by {cite:t}`mmTheorem`, who showed that under perfect capital markets the value of the firm is identical whether its investment is financed by equity, debt, or any combination of the two.

It is precisely to get around this result that models of imperfect capital markets were invented, since from the beginning many economists did not believe that the result is a plausible description of reality (including, I believe, Modigliani and Miller). Indeed, the existence (and high salaries) of corporate financial officers constitute a proof that the proposition is not true -- if it were true, CFOs would have no effect on the value of the firm, and could all be fired (thus saving the firm their salaries!). What remains true, however, is that models of investment that relax the assumption of perfect capital markets are much more difficult to work with -- and harder to extract implications from -- than models that assume capital markets are perfect.

A testable result that generally emerges from models of capital market imperfections, however, is that the amount of a firm's investment depends on the amount of cash the firm has on hand, with which it can finance that investment.

## Testing for the Failure of Modigliani-Miller

The [](#sec:qModel) shows that the {math}`\q` model can be manipulated (abstracting from depreciation, taxes, and other complications) to yield an implication for investment dynamics of approximately the following kind:

```{math}
:label: eq:iotaPerf

\begin{aligned}
   \iota & \approx (\q-1)/\omega.
\end{aligned}
```

The simplest class of imperfect capital markets models is one in which the firm is constrained to pay dividends to shareholders equal to whatever is its flow of cash after subtracting off expenses. But the rate of return that the firm must pay for external funds exceeds the return it can earn on internal funds. Without going into details, the rough implication of this is that an empirical model of the firm's investment choices should augment {eq}`eq:iotaPerf` with a measure of the funds the firm has in its hands at the time the investment decision is made:

```{math}
:label: eq:iotaImp

\begin{aligned}
   \iota & \approx \psi_{0} + \psi_{1} \q + \psi_{2} \pi.
\end{aligned}
```

A large literature spurred by the seminal paper of {cite:t}`fhp` estimates equations like this, and virtually always finds a statistically significant estimate of {math}`\psi_{2}`, interpreted as indicating the importance of "cash flow" for investment decisions. But there are many criticisms of this literature, and the importance of imperfections in capital markets remains a lively area of debate. My own view is that the most persuasive evidence of large deviations from the benchmark of the MM theorem is the fact that the financial services industry (including corporate CFOs) absorbs a very substantial amount of resources every year. Why would such a large industry exist if the informational problems were easy to solve? It would not -- especially in the internet era, where it would be a trivial matter to match up borrowers and lenders in the absence of informational and enforcement difficulties.
