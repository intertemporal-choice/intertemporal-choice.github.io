"""Run the self-test of every module in the package.

Usage: uv run python -m intertemporal_choice --self-test
"""

import argparse
import logging
import sys

import matplotlib

matplotlib.use("Agg")  # no display in CI

from intertemporal_choice import style  # noqa: E402

MODULES = [style]

logging.basicConfig(level=logging.INFO, format="%(message)s", force=True)
log = logging.getLogger(__name__)


def self_test() -> bool:
    failures = [f for module in MODULES for f in module.self_test()]
    for f in failures:
        log.error("SELF-TEST FAIL: %s", f)
    log.info("self-test %s", "FAILED" if failures else "passed")
    return not failures


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--self-test", action="store_true")
    args = parser.parse_args()
    if not args.self_test:
        parser.error("nothing to do; pass --self-test")
    sys.exit(0 if self_test() else 1)
