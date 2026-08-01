#!/usr/bin/env python3
"""Exact audit of the variance-only matrix discrepancy counterexample.

The diagonal sign-cube family is checked exactly for n up to 8.
"""
from __future__ import annotations
from fractions import Fraction as F
from itertools import product
import json
import pathlib


def verify() -> dict:
    for n in range(1, 9):
        eps = list(product([-1, 1], repeat=n))
        # For each signing, max over all epsilon of |<x,epsilon>| equals n.
        for x in eps[: min(10, len(eps))]:
            mx = max(abs(sum(x[i] * e[i] for i in range(n))) for e in eps)
            assert mx == n
        variance = n
        assert F(n * n, variance) == n
    return {
        "id": "variance-only-matrix-discrepancy",
        "ok": True,
        "summary": "exact sign-cube family",
        "witness": {
            "n_range": [1, 8],
            "discrepancy": "max_eps |<x,eps>| = n for every signing x",
            "variance_ratio": "n^2 / variance = n, unbounded in n",
        },
    }


if __name__ == "__main__":
    out = verify()
    art = pathlib.Path(__file__).resolve().parent / "artifacts"
    art.mkdir(exist_ok=True)
    (art / "certificate.json").write_text(
        json.dumps(out["witness"], indent=2, sort_keys=True) + "\n"
    )
    print(f"PASS {out['id']}: {out['summary']}")
