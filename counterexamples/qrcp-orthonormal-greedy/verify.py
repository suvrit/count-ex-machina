#!/usr/bin/env python3
"""Certify an exact rank-three QRCP counterexample using rational arithmetic."""
from __future__ import annotations

import json
import pathlib
from fractions import Fraction as F


def transpose(a):
    return [list(row) for row in zip(*a)]


def matmul(a, b):
    bt = transpose(b)
    return [[sum((x * y for x, y in zip(row, col)), F(0)) for col in bt]
            for row in a]


def identity(n):
    return [[F(i == j) for j in range(n)] for i in range(n)]


def inverse(a):
    n = len(a)
    aug = [row[:] + identity(n)[i] for i, row in enumerate(a)]
    for col in range(n):
        pivot = next(i for i in range(col, n) if aug[i][col] != 0)
        aug[col], aug[pivot] = aug[pivot], aug[col]
        scale = aug[col][col]
        aug[col] = [x / scale for x in aug[col]]
        for i in range(n):
            if i != col:
                scale = aug[i][col]
                aug[i] = [x - scale * y for x, y in zip(aug[i], aug[col])]
    return [row[n:] for row in aug]


def principal(a, indices):
    return [[a[i][j] for j in indices] for i in indices]


def schur_residuals(p, selected):
    if not selected:
        return [p[i][i] for i in range(len(p))]
    pinv = inverse(principal(p, selected))
    out = []
    for i in range(len(p)):
        u = [p[i][j] for j in selected]
        correction = sum(
            (u[a] * pinv[a][b] * u[b]
             for a in range(len(selected)) for b in range(len(selected))),
            F(0),
        )
        out.append(p[i][i] - correction)
    return out


def fs(x):
    return str(x.numerator) if x.denominator == 1 else f"{x.numerator}/{x.denominator}"


def verify() -> dict:
    """Raise AssertionError if any exact check fails; return a summary."""
    w = [
        [F(707, 1000), F(-23, 1000), F(-985, 1000)],
        [F(1639, 1000), F(1259, 1000), F(-985, 1000)],
        [F(1639, 1000), F(1259, 1000), F(-985, 1000)],
        [F(-707, 1000), F(23, 1000), F(985, 1000)],
        [F(1639, 1000), F(1259, 1000), F(-985, 1000)],
    ]
    v = identity(3) + w
    h = matmul(transpose(v), v)
    assert h == [[identity(3)[i][j] + matmul(transpose(w), w)[i][j]
                  for j in range(3)] for i in range(3)]
    hinv = inverse(h)
    p = matmul(matmul(v, hinv), transpose(v))

    # P is exactly the rank-three orthogonal projector QQ^T.
    assert p == transpose(p)
    assert matmul(p, p) == p
    assert sum((p[i][i] for i in range(8)), F(0)) == 3

    selected = []
    residual_tables = []
    gaps = []
    for _ in range(3):
        residuals = schur_residuals(p, selected)
        remaining = [i for i in range(8) if i not in selected]
        ordered = sorted(remaining, key=lambda i: (-residuals[i], i))
        pivot, runner_up = ordered[0], ordered[1]
        gap = residuals[pivot] - residuals[runner_up]
        assert gap > 0
        residual_tables.append({
            "selected_before": [i + 1 for i in selected],
            "pivot": pivot + 1,
            "pivot_residual": fs(residuals[pivot]),
            "runner_up_residual": fs(residuals[runner_up]),
            "strict_gap": fs(gap),
        })
        gaps.append(gap)
        selected.append(pivot)

    assert selected == [0, 1, 2]
    assert gaps == [
        F(487510152, 98637920341),
        F(474120000, 100874772187),
        F(397, 78015),
    ]

    # Q = V H^(-1/2), so Q({1,2,3},:)^(-1) has squared norm
    # lambda_max(H)=1+lambda_max(W^T W).  A rational Rayleigh vector
    # certifies lambda_max(W^T W)>17 without computing any radicals.
    x = [[F(2)], [F(1)], [F(-1)]]
    wx = matmul(w, x)
    wx_sq = sum((row[0] ** 2 for row in wx), F(0))
    x_sq = sum((row[0] ** 2 for row in x), F(0))
    rayleigh_gap = wx_sq - 17 * x_sq
    assert x_sq == 6
    assert rayleigh_gap == F(192051, 250000) > 0

    witness = {
        "n": 8,
        "k": 3,
        "W": [[fs(x) for x in row] for row in w],
        "V": [[fs(x) for x in row] for row in v],
        "P": [[fs(x) for x in row] for row in p],
        "pivot_sequence_one_based": [i + 1 for i in selected],
        "pivot_steps": residual_tables,
        "rayleigh_vector": ["2", "1", "-1"],
        "rayleigh_gap_over_17": fs(rayleigh_gap),
        "claimed_bound_squared": "18",
    }
    return {
        "id": "qrcp-orthonormal-greedy",
        "ok": True,
        "summary": "strict QRCP pivots are 1,2,3 and the exact Rayleigh gap over the squared bound is 192051/250000",
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
