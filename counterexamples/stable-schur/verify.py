#!/usr/bin/env python3
"""Exact audit of the two Borcea--Branden problems (AIM Problems 35 and 38).

Expands the stable degree-five polynomial exactly, extracts monomial and
Schur coefficients, and exhibits the four POT-violating partitions.
"""
from __future__ import annotations
import json
import pathlib


def verify() -> dict:
    # Expand the product of five linear forms. Exponents are 5-tuples.
    coeff = {(0, 0, 0, 0, 0): 1}
    for i in range(5):
        new = {}
        for exp, c in coeff.items():
            for j in range(5):
                e = list(exp)
                e[j] += 1
                e = tuple(e)
                new[e] = new.get(e, 0) + c * (1 if i == j else 5)
        coeff = new
    parts = [
        (5,), (4, 1), (3, 2), (3, 1, 1),
        (2, 2, 1), (2, 1, 1, 1), (1, 1, 1, 1, 1),
    ]
    monomial = {}
    for mu in parts:
        exp = tuple(mu) + (0,) * (5 - len(mu))
        monomial[mu] = coeff[exp]
    expected_m = [625, 5125, 12250, 24900, 39550, 81580, 168376]
    assert [monomial[p] for p in parts] == expected_m
    # Rows lambda, columns mu in dominance order.
    K = [
        [1, 1, 1, 1, 1, 1, 1],
        [0, 1, 1, 2, 2, 3, 4],
        [0, 0, 1, 1, 2, 3, 5],
        [0, 0, 0, 1, 1, 3, 6],
        [0, 0, 0, 0, 1, 2, 5],
        [0, 0, 0, 0, 0, 1, 4],
        [0, 0, 0, 0, 0, 0, 1],
    ]
    a = []
    for j, mu in enumerate(parts):
        known = sum(a[i] * K[i][j] for i in range(j))
        a.append(monomial[mu] - known)
    expected_a = [625, 4500, 7125, 8150, 7525, 6580, 1281]
    assert a == expected_a
    f = [1, 4, 5, 6, 5, 4, 1]
    failures = [i for i in range(7) if a[i] > f[i] * a[-1]]
    assert failures == [2, 3, 4, 5]
    return {
        "id": "stable-schur",
        "ok": True,
        "summary": "exact expansion and POT failures at four partitions",
        "witness": {
            "partitions": [list(p) for p in parts],
            "monomial_coefficients": expected_m,
            "schur_coefficients": expected_a,
            "immanant_f_vector": f,
            "violating_partitions": [list(parts[i]) for i in failures],
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
