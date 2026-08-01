#!/usr/bin/env python3
"""High-precision audit of the rank-two mixed-norm counterexample.

Builds the 21-vector Gram matrix and evaluates the interpolation ratio at
100 digits with mpmath.  The companion Sage script verify_mixed_norm.sage
provides the outward-rounded interval certificate.
"""
from __future__ import annotations
import json
import pathlib
import mpmath as mp


def mixed_norm(A, p, q):
    n = len(A)
    columns = []
    for j in range(n):
        columns.append(mp.power(mp.fsum(abs(A[i][j]) ** p for i in range(n)), 1 / p))
    return mp.power(mp.fsum(c ** q for c in columns), 1 / q)


def verify() -> dict:
    mp.mp.dps = 100
    mult = [1, 18, 1, 1]
    weights = [46, 17, 42, 1]
    dirs = [(1, 0), (1, mp.mpf(1) / 50), (1, mp.mpf(3) / 50), (0, 1)]
    rows = []
    for m, w, y in zip(mult, weights, dirs):
        scale = mp.power(w, mp.mpf(5) / 6)
        rows.extend([(scale * y[0], scale * y[1])] * m)
    A = [[rows[i][0] * rows[j][0] + rows[i][1] * rows[j][1] for j in range(21)] for i in range(21)]
    s, q = mp.mpf(6) / 5, mp.mpf(6)
    ratio = mixed_norm(A, s, q) / mp.sqrt(mixed_norm(A, s, s) * mixed_norm(A, q, q))
    assert ratio > mp.mpf("1.0000006")
    return {
        "id": "rank-two-mixed-norm",
        "ok": True,
        "summary": "100-digit ratio = " + mp.nstr(ratio, 80),
        "witness": {
            "s_q": ["6/5", "6"],
            "multiplicities": [1, 18, 1, 1],
            "weights": [46, 17, 42, 1],
            "directions": ["(1,0)", "(1,1/50)", "(1,3/50)", "(0,1)"],
            "weight_exponent": "5/6",
            "ratio": mp.nstr(ratio, 80),
            "threshold": "1.0000006",
            "rigorous_certificate": "verify_mixed_norm.sage (outward-rounded intervals)",
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
