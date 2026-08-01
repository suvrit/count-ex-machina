#!/usr/bin/env python3
"""Exact audit of the log-determinant Loewner monotonicity counterexample.

All matrices are exact rationals; the alternating inclusion-exclusion sum of
inverses is evaluated exactly and the quadratic form is a negative rational.
"""
from __future__ import annotations
from fractions import Fraction as F
from itertools import combinations
import json
import pathlib
import sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2]))
from tools.exactcert import assert_positive_definite_3, inv3, madd


def verify() -> dict:
    den = 10**6
    X = [[F(302766, den), F(-89057, den), F(-179370, den)],
         [F(-89057, den), F(27282, den), F(52935, den)],
         [F(-179370, den), F(52935, den), F(107617, den)]]
    A1 = [[F(227979, den), F(-1264394, den), F(-740843, den)],
          [F(-1264394, den), F(7052829, den), F(4136214, den)],
          [F(-740843, den), F(4136214, den), F(2429309, den)]]
    A2 = [[F(712456619, den), F(657821465, den), F(-108957581, den)],
          [F(657821465, den), F(607377892, den), F(-100602246, den)],
          [F(-108957581, den), F(-100602246, den), F(16664150, den)]]
    A3 = [[F(2117478, den), F(-450289, den), F(-2782586, den)],
          [F(-450289, den), F(96801, den), F(592006, den)],
          [F(-2782586, den), F(592006, den), F(3659335, den)]]
    A4 = [[F(176290, den), F(-490538, den), F(-778637, den)],
          [F(-490538, den), F(1373736, den), F(2178964, den)],
          [F(-778637, den), F(2178964, den), F(3459701, den)]]
    As = [A1, A2, A3, A4]
    for M in [X] + As:
        assert_positive_definite_3(M)
    C = [[F(0) for _ in range(3)] for __ in range(3)]
    for r in range(1, 5):
        for S in combinations(range(4), r):
            M = [row[:] for row in X]
            for i in S:
                M = madd(M, As[i])
            inv = inv3(M)
            sign = 1 if r % 2 == 1 else -1
            C = [[C[i][j] + sign * inv[i][j] for j in range(3)] for i in range(3)]
    v = [F(844), F(-249), F(-475)]
    q = sum(v[i] * C[i][j] * v[j] for i in range(3) for j in range(3))
    assert q < 0
    return {
        "id": "logdet-loewner",
        "ok": True,
        "summary": f"exact rational v^T C v < 0, decimal={float(q):.16g}",
        "witness": {
            "X": [[str(x) for x in row] for row in X],
            "A": [[[str(x) for x in row] for row in M] for M in As],
            "v": [str(x) for x in v],
            "quadratic_form": str(q),
            "quadratic_form_decimal": f"{float(q):.16g}",
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
