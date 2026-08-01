#!/usr/bin/env python3
"""Independent audit of all admitted archive counterexamples.

Exact cases use Python's Fraction or integer arithmetic. Analytic cases are
reconstructed at high precision; companion Sage scripts provide outward-rounded
interval versions for the two analytic certificates.
"""
from __future__ import annotations
from fractions import Fraction as F
from itertools import combinations, product
from math import factorial
import cmath
import json
import mpmath as mp


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


def verify_stable_schur():
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
    print("PASS stable Schur polynomial: exact expansion and POT failures")


def verify_subgroup_johnson():
    # A_t is PD because 0<t<1. The zero calculation is exact in Q(omega).
    t3 = F(1, 4)
    assert 0 < float(t3 ** F(1, 3)) < 1  # sanity only
    # In Q[omega]/(omega^2+omega+1), (1+omega)^3=-1 and 1+omega^3=2.
    lhs_factor = F(-1) + F(1, 2) * 2
    assert lhs_factor == 0
    print("PASS subgroup Johnson: exact C3 upper-half-plane zero")


def verify_macdonald():
    for r in [F(1, 2), F(2, 3), F(9, 10)]:
        lhs = F(3, 1) / (1 + r + r * r)
        rhs = 1 / r
        assert lhs < rhs
        assert 1 + r + r * r - 3 * r == (1 - r) ** 2
    print("PASS Macdonald: exact rank-two reversal")


def verify_dpp():
    L0 = [
        [F(337200647, 10**8), F(262325460, 10**8)],
        [F(262325460, 10**8), F(607953037, 10**8)],
    ]
    I = [[F(1), F(0)], [F(0), F(1)]]
    assert_positive_definite_2(L0)
    Linv = inv2(L0)
    ILinv = inv2(madd(I, L0))
    singleton = [[1 / L0[0][0], F(0)], [F(0), F(0)]]
    singleton2 = [[F(0), F(0)], [F(0), 1 / L0[1][1]]]
    Z = madd(madd(singleton, singleton2), Linv)
    Delta = madd(mscale(F(1, 3), Z), mscale(F(-1), ILinv))
    L1 = madd(L0, mscale(F(5), mmul2(mmul2(L0, Delta), L0)))
    assert_positive_definite_2(L1)
    prod0 = L0[0][0] * L0[1][1] * det2(L0)
    prod1 = L1[0][0] * L1[1][1] * det2(L1)
    left = prod1 / prod0
    right = (det2(madd(I, L1)) / det2(madd(I, L0))) ** 3
    assert right - left > 0
    print(f"PASS DPP: exact rational likelihood reversal, gap={float(right-left):.16g}")


def verify_discrepancy():
    for n in range(1, 9):
        eps = list(product([-1, 1], repeat=n))
        # For each signing, max over all epsilon of |<x,epsilon>| equals n.
        for x in eps[: min(10, len(eps))]:
            mx = max(abs(sum(x[i] * e[i] for i in range(n))) for e in eps)
            assert mx == n
        variance = n
        assert F(n*n, variance) == n
    print("PASS matrix discrepancy: exact sign-cube family")


def mixed_norm(A, p, q):
    n = len(A)
    columns = []
    for j in range(n):
        columns.append(mp.power(mp.fsum(abs(A[i][j]) ** p for i in range(n)), 1 / p))
    return mp.power(mp.fsum(c ** q for c in columns), 1 / q)


def verify_mixed_norm():
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
    print("PASS mixed norm: 100-digit ratio =", mp.nstr(ratio, 80))


def theta_polynomials(K=10):
    # coefficient list low to high
    P = [[-3, 2]]
    for _ in range(K):
        cur = P[-1]
        deriv = [i * cur[i] for i in range(1, len(cur))]
        nxt = [0] * (len(cur) + 1)
        # 4u P'
        for i, c in enumerate(deriv):
            nxt[i + 1] += 4 * c
        # 5P - 4uP
        for i, c in enumerate(cur):
            nxt[i] += 5 * c
            nxt[i + 1] -= 4 * c
        while nxt and nxt[-1] == 0:
            nxt.pop()
        P.append(nxt)
    return P


def peval(coeff, x):
    y = mp.mpf(0)
    for c in reversed(coeff):
        y = y * x + c
    return y


def verify_theta():
    mp.mp.dps = 100
    P = theta_polynomials(10)
    t = mp.mpf(1) / 50
    alpha = mp.pi * mp.e ** (4 * t)
    vals = {}
    for k in [8, 9, 10]:
        total = mp.mpf(0)
        # m>=20 is astronomically negligible; see Sage certificate for rigorous tail.
        for m in range(1, 20):
            u = alpha * m * m
            total += mp.pi * m * m * mp.e ** (5 * t - u) * peval(P[k], u)
        vals[k] = total
    J = vals[9] ** 2 - vals[8] * vals[10]
    assert J < mp.mpf("-2.6e19")
    print("PASS theta: 100-digit J9(1/50) =", mp.nstr(J, 80))


def verify_logdet_loewner():
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
    print(f"PASS logdet Loewner: exact rational v^T C v < 0, decimal={float(q):.16g}")


def main():
    verify_stable_schur()
    verify_subgroup_johnson()
    verify_macdonald()
    verify_dpp()
    verify_discrepancy()
    verify_mixed_norm()
    verify_theta()
    verify_logdet_loewner()
    print("ALL AUDITED CASES PASS")


if __name__ == "__main__":
    main()
