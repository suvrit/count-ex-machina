#!/usr/bin/env python3
"""Certify the exact strict-SDD Nyström diminishing-returns obstruction."""
from __future__ import annotations
from fractions import Fraction as F
import json
import pathlib


def identity(n):
    return [[F(int(i == j)) for j in range(n)] for i in range(n)]


def transpose(a):
    return [list(row) for row in zip(*a)]


def matmul(a, b):
    return [
        [sum((a[i][t] * b[t][j] for t in range(len(b))), F(0))
         for j in range(len(b[0]))]
        for i in range(len(a))
    ]


def inverse(a):
    n = len(a)
    aug = [list(a[i]) + identity(n)[i] for i in range(n)]
    for col in range(n):
        pivot = next(row for row in range(col, n) if aug[row][col] != 0)
        aug[col], aug[pivot] = aug[pivot], aug[col]
        scale = aug[col][col]
        aug[col] = [x / scale for x in aug[col]]
        for row in range(n):
            if row != col:
                factor = aug[row][col]
                aug[row] = [aug[row][j] - factor * aug[col][j]
                            for j in range(2 * n)]
    return [row[n:] for row in aug]


def principal(a, indices):
    return [[a[i][j] for j in indices] for i in indices]


def trace(a):
    return sum((a[i][i] for i in range(len(a))), F(0))


def ldl_pivots(a):
    n = len(a)
    lower = identity(n)
    pivots = [F(0) for _ in range(n)]
    for j in range(n):
        pivots[j] = a[j][j] - sum(
            (lower[j][k] * lower[j][k] * pivots[k] for k in range(j)), F(0)
        )
        assert pivots[j] != 0
        for i in range(j + 1, n):
            numerator = a[i][j] - sum(
                (lower[i][k] * lower[j][k] * pivots[k] for k in range(j)), F(0)
            )
            lower[i][j] = numerator / pivots[j]
    return pivots


def nystrom_residual(k, selected):
    n = len(k)
    chosen = sorted(selected)
    kii_inv = inverse(principal(k, chosen))
    k_col = [[k[i][j] for j in chosen] for i in range(n)]
    k_row = [[k[i][j] for j in range(n)] for i in chosen]
    approx = matmul(matmul(k_col, kii_inv), k_row)
    return [[k[i][j] - approx[i][j] for j in range(n)] for i in range(n)]


def s(x):
    return str(x)


def verify() -> dict:
    """Raise AssertionError if any exact check fails; return a summary."""
    m = [
        [F(11), F(3), F(-4), F(3)],
        [F(3), F(12), F(4), F(-1)],
        [F(-4), F(4), F(14), F(-2)],
        [F(3), F(-1), F(-2), F(11)],
    ]
    gamma = F(1, 2)
    l = [[m[i][j] - (gamma if i == j else F(0)) for j in range(4)]
         for i in range(4)]
    assert l == transpose(l)
    margins = [
        l[i][i] - sum((abs(l[i][j]) for j in range(4) if j != i), F(0))
        for i in range(4)
    ]
    assert margins == [F(1, 2), F(7, 2), F(7, 2), F(9, 2)]
    assert all(x > 0 for x in margins)
    assert all(x > 0 for x in ldl_pivots(l))

    k = inverse(m)
    assert matmul(m, k) == identity(4)
    sets = {
        "2": {1},
        "23": {1, 2},
        "24": {1, 3},
        "234": {1, 2, 3},
    }
    expected = {
        "2": F(100, 349),
        "23": F(11, 56),
        "24": F(25, 138),
        "234": F(1, 11),
    }
    errors = {}
    for name, selected in sets.items():
        complement = [i for i in range(4) if i not in selected]
        complement_formula = trace(inverse(principal(m, complement)))
        residual = nystrom_residual(k, selected)
        direct_formula = trace(residual)
        assert complement_formula == direct_formula
        # Exact LDL check on the nonzero principal residual block certifies PSD,
        # so its nuclear norm equals its trace.
        residual_block = principal(residual, complement)
        assert all(x > 0 for x in ldl_pivots(residual_block))
        errors[name] = direct_formula
    assert errors == expected

    first_reduction = errors["2"] - errors["23"]
    later_reduction = errors["24"] - errors["234"]
    gap = later_reduction - first_reduction
    assert first_reduction == F(1761, 19544)
    assert later_reduction == F(137, 1518)
    assert gap == F(2165, 14833896) > 0

    witness = {
        "M": [[s(x) for x in row] for row in m],
        "gamma": s(gamma),
        "strict_diagonal_dominance_margins_of_L": [s(x) for x in margins],
        "errors": {name: s(value) for name, value in errors.items()},
        "first_reduction": s(first_reduction),
        "later_reduction": s(later_reduction),
        "violation_gap": s(gap),
    }
    return {
        "id": "sdd-nystrom-diminishing-returns",
        "ok": True,
        "summary": "strict SDD margins are positive and the exact later-minus-earlier marginal reduction is 2165/14833896",
        "witness": witness,
    }


if __name__ == "__main__":
    out = verify()
    art = pathlib.Path(__file__).resolve().parent / "artifacts"
    art.mkdir(exist_ok=True)
    (art / "certificate.json").write_text(
        json.dumps(out["witness"], indent=2, sort_keys=True) + "\n"
    )
    print(f"PASS {out['id']}: {out['summary']}")
