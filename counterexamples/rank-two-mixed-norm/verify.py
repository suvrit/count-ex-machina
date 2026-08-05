#!/usr/bin/env python3
"""Audits of the two mixed-norm counterexamples in this dossier.

rank-two-mixed-norm: builds the 21-vector Gram matrix and evaluates the
interpolation ratio at 100 digits with mpmath.  The companion Sage script
verify_mixed_norm.sage provides the outward-rounded interval certificate.

mixed-norm-general-s: at s = 3/2 the deficit is a Z-linear combination of
square roots of integers, so SymPy decides its sign exactly -- no floating
point and no interval enclosure enter the assertion.
"""
from __future__ import annotations
import json
import pathlib
import mpmath as mp
import sympy as sp


def mixed_norm(A, p, q):
    n = len(A)
    columns = []
    for j in range(n):
        columns.append(mp.power(mp.fsum(abs(A[i][j]) ** p for i in range(n)), 1 / p))
    return mp.power(mp.fsum(c ** q for c in columns), 1 / q)


# --- mixed-norm-general-s -------------------------------------------------
# A, B are nonnegative integer matrices, so this refutes the conjecture under
# its own hypothesis (A, B >= 0), not merely under the weaker "products are
# nonnegative" variant.  At p = q the mixed norm is the entrywise l_p norm, so
# the row/column convention of the two sources cannot matter here.
A_GEN = [[2, 4], [5, 0], [1, 0]]
B_GEN = [[0, 5], [4, 2], [1, 0]]


def _gram(X, W):
    return [[sum(X[r][i] * W[r][j] for r in range(len(X))) for j in range(len(W[0]))]
            for i in range(len(X[0]))]


def verify_general_s() -> dict:
    """Exact refutation at s = q = 3/2, via a negative FitzGerald--Horn deficit."""
    AtA, BtB, AtB = _gram(A_GEN, A_GEN), _gram(B_GEN, B_GEN), _gram(A_GEN, B_GEN)
    three_halves = sp.Rational(3, 2)
    deficit = sp.simplify(
        sum(sp.Integer(v) ** three_halves for row in AtA for v in row)
        + sum(sp.Integer(v) ** three_halves for row in BtB for v in row)
        - 2 * sum(sp.Integer(v) ** three_halves for row in AtB for v in row)
    )
    # Sign of an algebraic number, decided exactly by SymPy.
    assert deficit.is_negative is True, deficit
    # The deficit being negative is, by AM-GM, exactly the failure of
    # ||A^T B||_{s,s} <= ||A^T A||_{s,s}^{1/2} ||B^T B||_{s,s}^{1/2}.
    mp.mp.dps = 60
    s = mp.mpf(3) / 2

    def ss(M):
        return mp.power(mp.fsum(mp.power(abs(v), s) for row in M for v in row), 1 / s)

    ratio = ss(AtB) / mp.sqrt(ss(AtA) * ss(BtB))
    assert ratio > 1
    return {
        "A": A_GEN,
        "B": B_GEN,
        "AtA": AtA,
        "BtB": BtB,
        "AtB": AtB,
        "s_q": ["3/2", "3/2"],
        "deficit_exact": sp.sstr(deficit),
        "deficit_decimal": sp.sstr(sp.N(deficit, 50)),
        "deficit_is_negative": True,
        "ratio": mp.nstr(ratio, 50),
    }


def verify() -> dict:
    general = verify_general_s()
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
        "summary": (
            "100-digit ratio = " + mp.nstr(ratio, 80)
            + "; general-s exact deficit = " + general["deficit_decimal"]
            + " < 0 (s=q=3/2), ratio = " + general["ratio"]
        ),
        "witness": {
            "mixed_norm_general_s": general,
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
