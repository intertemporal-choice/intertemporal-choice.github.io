# Development tooling, not published

Everything in this folder stays in the private source repository. `.gitattributes` marks
`dev/**` as `export-ignore`, and `code/publish.py` publishes by `git archive`, so nothing
here reaches the public repository or the site.

- `handout-port/`: the LaTeX-to-MyST conversion used to port the TractableBufferStock
  handout (PR #10), kept for the next handout ported from its `.tex` source.
