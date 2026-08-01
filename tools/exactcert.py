"""Shared exact-arithmetic helpers for counterexample certificates.

Extracted verbatim from the original monolithic verify_all.py audit script.
All operations are exact over Python Fractions (or integers); positive
definiteness is checked via leading principal minors.
"""
from __future__ import annotations
from fractions import Fraction as F


def assert_positive_definite_2(M):
    assert M[0][0] > 0
    assert M[0][0] * M[1][1] - M[0][1] * M[1][0] > 0


def det3(M):
    return (
        M[0][0] * (M[1][1] * M[2][2] - M[1][2] * M[2][1])
        - M[0][1] * (M[1][0] * M[2][2] - M[1][2] * M[2][0])
        + M[0][2] * (M[1][0] * M[2][1] - M[1][1] * M[2][0])
    )


def assert_positive_definite_3(M):
    assert M[0][0] > 0
    assert M[0][0] * M[1][1] - M[0][1] * M[1][0] > 0
    assert det3(M) > 0


def inv2(M):
    a, b = M[0]
    c, d = M[1]
    det = a * d - b * c
    return [[d / det, -b / det], [-c / det, a / det]]


def inv3(M):
    n = 3
    aug = [row[:] + [F(int(i == j)) for j in range(n)] for i, row in enumerate(M)]
    for col in range(n):
        pivot = next(r for r in range(col, n) if aug[r][col] != 0)
        aug[col], aug[pivot] = aug[pivot], aug[col]
        p = aug[col][col]
        aug[col] = [x / p for x in aug[col]]
        for r in range(n):
            if r == col:
                continue
            f = aug[r][col]
            aug[r] = [aug[r][j] - f * aug[col][j] for j in range(2 * n)]
    return [row[n:] for row in aug]


def madd(A, B):
    return [[A[i][j] + B[i][j] for j in range(len(A))] for i in range(len(A))]


def mmul2(A, B):
    return [[sum(A[i][k] * B[k][j] for k in range(2)) for j in range(2)] for i in range(2)]


def mscale(c, A):
    return [[c * x for x in row] for row in A]


def det2(M):
    return M[0][0] * M[1][1] - M[0][1] * M[1][0]
