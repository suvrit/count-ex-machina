#!/usr/bin/env python3
"""Exact audit of the Macdonald lattice Schur-convexity counterexample.

The rank-two reversal is checked at sample rational parameters together with
the algebraic identity 1 + r + r^2 - 3r = (1-r)^2 that yields the full
one-parameter family 0 < r < 1.
"""
from __future__ import annotations
from fractions import Fraction as F
import json
import pathlib

SAMPLES = [F(1, 2), F(2, 3), F(9, 10)]


def verify() -> dict:
    for r in SAMPLES:
        lhs = F(3, 1) / (1 + r + r * r)
        rhs = 1 / r
        assert lhs < rhs
        assert 1 + r + r * r - 3 * r == (1 - r) ** 2
    return {
        "id": "macdonald-schur-convexity",
        "ok": True,
        "summary": "exact rank-two reversal",
        "witness": {
            "sample_r": [str(r) for r in SAMPLES],
            "reversal": "3/(1+r+r^2) < 1/r for all 0<r<1",
            "identity": "1+r+r^2-3r = (1-r)^2",
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
