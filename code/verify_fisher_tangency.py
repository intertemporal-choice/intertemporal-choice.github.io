"""Gate the Fisher notebook's plotted optimum on the two conditions the figures assert:
the point lies on the drawn budget line, and it satisfies the Euler equation.

Both the corrected rule (MPCmin * W) and the original one (cFunc(W)) are evaluated, so
the test is shown to reject the code it replaced rather than merely passing on the new.
"""

import logging

from HARK.ConsumptionSaving.ConsIndShockModel import PerfForesightConsumerType

logging.basicConfig(level=logging.INFO, format="%(message)s", force=True)
log = logging.getLogger(__name__)

TOL = 1e-8


def solve(R, CRRA=None, DiscFac=None, B_1=0.0):
    pf = PerfForesightConsumerType()
    pf.cycles = 1
    pf.T_cycle = 1
    pf.PermGroFac = [1.0]
    pf.LivPrb = [1.0]
    pf.kLogInitStd = 0.0
    pf.AgentCount = 1
    pf.Rfree = [R]
    pf.kLogInitMean = B_1
    if CRRA is not None:
        pf.CRRA = CRRA
    if DiscFac is not None:
        pf.DiscFac = DiscFac
    pf.solve()
    return pf


def check(name, pf, W, Y_1, Y_2, B_1, R, rule):
    """rule: 'fixed' = MPCmin * W (this notebook), 'original' = cFunc(W) (DemARK)."""
    sol = pf.solution[0]
    C_1 = sol.MPCmin * W if rule == "fixed" else sol.cFunc(W)
    C_2 = pf.solution[1].cFunc((Y_1 + B_1 - C_1) * R + Y_2)

    on_line = abs(C_2 - ((Y_1 + B_1 - C_1) * R + Y_2))
    euler_ratio = C_2 / C_1
    euler_target = (R * pf.DiscFac) ** (1 / pf.CRRA)
    euler_gap = abs(euler_ratio / euler_target - 1)

    ok = on_line < TOL and euler_gap < 1e-10
    log.info(
        "%-28s %-8s C_1=%9.5f  budget_resid=%.2e  C2/C1=%.6f vs %.6f  gap=%7.3f%%  %s",
        name,
        rule,
        C_1,
        on_line,
        euler_ratio,
        euler_target,
        100 * euler_gap,
        "PASS" if ok else "FAIL",
    )
    return ok


results = []

# FisherPlot defaults: Y_1=50, Y_2=50, B_1=2, R=1.05
R, Y_1, Y_2, B_1 = 1.05, 50.0, 50.0, 2.0
pf = solve(R, B_1=B_1)
W = B_1 + Y_1 + Y_2 / R
for rule in ("fixed", "original"):
    results.append(("FisherPlot", rule, check("FisherPlot", pf, W, Y_1, Y_2, B_1, R, rule)))

# FisherPlot1 defaults: Y_1=100, Y_2=0, B_1=0, RHi=2.0, RLo=1.0
for label, R in (("FisherPlot1 R_Lo", 1.0), ("FisherPlot1 R_Hi", 2.0)):
    Y_1, Y_2, B_1 = 100.0, 0.0, 0.0
    pf = solve(R, B_1=B_1)
    W = B_1 + Y_1 + Y_2 / R
    for rule in ("fixed", "original"):
        results.append((label, rule, check(label, pf, W, Y_1, Y_2, B_1, R, rule)))

# FisherPlot2 defaults: Y_1=0, Y_2=100, B_1=0, RHi=2.0, RLo=1.0
for label, R in (("FisherPlot2 R_Lo", 1.0), ("FisherPlot2 R_Hi", 2.0)):
    Y_1, Y_2, B_1 = 0.0, 100.0, 0.0
    pf = solve(R, B_1=B_1)
    W = B_1 + Y_1 + Y_2 / R
    for rule in ("fixed", "original"):
        results.append((label, rule, check(label, pf, W, Y_1, Y_2, B_1, R, rule)))

# FisherPlot3 defaults: M_1=10 (slider max), R=1.02, beta=0.9, CRRA=2.0
M_1, R, beta, CRRA = 10.0, 1.02, 0.9, 2.0
pf = solve(R, CRRA=CRRA, DiscFac=beta)
for rule in ("fixed", "original"):
    results.append(("FisherPlot3", rule, check("FisherPlot3", pf, M_1, 0.0, 0.0, M_1, R, rule)))

fixed_pass = all(ok for _, rule, ok in results if rule == "fixed")
original_pass = any(ok for _, rule, ok in results if rule == "original")
log.info("")
log.info("corrected rule passes everywhere: %s", fixed_pass)
log.info("original rule passes anywhere (rejection test): %s", original_pass)
if not fixed_pass or original_pass:
    raise SystemExit(1)
