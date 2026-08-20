#!/usr/bin/env python3
"""Exact certificate for a counterexample to Borcea--Branden AIM Problem 36.

The script uses only exact rational/integer arithmetic (SymPy); no floating-point
calculation is used in any assertion.  It performs the following independent checks:

  1. Constructs the 5-dimensional S_5-module ker(B) inside the permutation
     representation on 2-subsets.
  2. Constructs the rank-3 orthogonal projections P_i and verifies idempotence,
     self-adjointness, covariance, and sum_i P_i = 3 I.
  3. Constructs explicit symmetric positive-definite integer matrices
         J_i = 2 G (I + 5 P_i).
  4. Expands det(sum_i x_i J_i) exactly and checks all 126 degree-5 monomials,
     S_5 symmetry, and strict coefficient positivity.
  5. Computes the Kostka matrix by direct enumeration of semistandard Young
     tableaux (it is not hard-coded), obtains the Schur expansion, and checks the
     negative s_(1^5) coefficient.
  6. Independently re-extracts every Schur coefficient by the bialternant formula.
  7. Verifies the closed one-parameter formulas for
         p_t(x) = det(sum_i x_i (I + t P_i)).
  8. Builds the t=4 member of the same family and checks that it is Schur
     POSITIVE and still violates the Problem 37 lower endpoint at lam=(1^5).
     This is the witness Problem 37 actually needs: q at t=5 breaks that
     endpoint only because it is not Schur positive at all, which makes it a
     restatement of the Problem 36 refutation rather than a separate one.

Usage:
    python verify_pencil.py         # run all checks, write artifacts/certificate-36-37.json
    python verify_pencil.py --verbose  # additionally print all matrices and expansions

Requires: sympy
"""

from __future__ import annotations

import argparse
import json
from itertools import combinations, permutations
from pathlib import Path
from typing import Dict, Iterable, List, Sequence, Tuple

import sympy as sp

N = 5
PARTS: List[Tuple[int, ...]] = [
    (5,),
    (4, 1),
    (3, 2),
    (3, 1, 1),
    (2, 2, 1),
    (2, 1, 1, 1),
    (1, 1, 1, 1, 1),
]


def permutation_sign(sigma: Sequence[int]) -> int:
    inversions = sum(
        sigma[i] > sigma[j]
        for i in range(len(sigma))
        for j in range(i + 1, len(sigma))
    )
    return -1 if inversions % 2 else 1


def inverse_permutation(g: Sequence[int]) -> Tuple[int, ...]:
    inv = [0] * len(g)
    for i, image in enumerate(g):
        inv[image] = i
    return tuple(inv)


def enumerate_ssyt(shape: Tuple[int, ...], content: Tuple[int, ...]) -> int:
    """Count SSYT of a fixed shape and content by exact backtracking.

    Rows are weakly increasing; columns are strictly increasing.  The symbol r
    occurs content[r-1] times.  Since |shape|=5 here, brute force is tiny.
    """

    cells = [(r, c) for r, row_len in enumerate(shape) for c in range(row_len)]
    values: Dict[Tuple[int, int], int] = {}
    remaining = list(content)
    max_symbol = len(content)
    count = 0

    def backtrack(k: int) -> None:
        nonlocal count
        if k == len(cells):
            count += 1
            return

        r, c = cells[k]
        lower = 1
        if c > 0:
            lower = max(lower, values[(r, c - 1)])
        if r > 0 and c < shape[r - 1]:
            lower = max(lower, values[(r - 1, c)] + 1)

        for symbol in range(lower, max_symbol + 1):
            idx = symbol - 1
            if remaining[idx] == 0:
                continue
            remaining[idx] -= 1
            values[(r, c)] = symbol
            backtrack(k + 1)
            del values[(r, c)]
            remaining[idx] += 1

    backtrack(0)
    return count


def kostka_matrix(parts: Sequence[Tuple[int, ...]]) -> sp.Matrix:
    return sp.Matrix(
        [
            [enumerate_ssyt(lam, mu) for mu in parts]
            for lam in parts
        ]
    )


def construct_representation():
    edges = list(combinations(range(N), 2))
    edge_index = {e: i for i, e in enumerate(edges)}

    # Unsigned vertex-edge incidence map B: R^{10} -> R^5.
    B = sp.zeros(N, len(edges))
    for j, (a, b) in enumerate(edges):
        B[a, j] = 1
        B[b, j] = 1

    # BB^T = 3I + 11^T, hence B is surjective and dim ker(B)=5.
    assert B * B.T == 3 * sp.eye(N) + sp.ones(N)
    assert B.rank() == N

    # Fixed rational basis of V=ker(B), included explicitly so the certificate
    # does not depend on a computer-algebra system's nullspace basis convention.
    K = sp.Matrix([
        [0, 0, 1, 1, 1],
        [1, 1, 0, 0, 1],
        [-1, 0, -1, 0, -1],
        [0, -1, 0, -1, -1],
        [-1, -1, -1, -1, -1],
        [1, 0, 0, 0, 0],
        [0, 1, 0, 0, 0],
        [0, 0, 1, 0, 0],
        [0, 0, 0, 1, 0],
        [0, 0, 0, 0, 1],
    ])
    assert K.shape == (10, 5)
    assert K.rank() == 5
    assert B * K == sp.zeros(5, 5)

    G = K.T * K
    assert G.det() > 0
    L = G.inv() * K.T
    assert L * K == sp.eye(5)

    def edge_permutation_matrix(g: Sequence[int]) -> sp.Matrix:
        R = sp.zeros(len(edges))
        for j, (a, b) in enumerate(edges):
            image = tuple(sorted((g[a], g[b])))
            R[edge_index[image], j] = 1
        return R

    def rho(g: Sequence[int]) -> sp.Matrix:
        return sp.simplify(L * edge_permutation_matrix(g) * K)

    def transposition(a: int, b: int) -> Tuple[int, ...]:
        g = list(range(N))
        g[a], g[b] = g[b], g[a]
        return tuple(g)

    P: List[sp.Matrix] = []
    for i in range(N):
        class_sum = sp.zeros(5)
        for a, b in combinations(range(N), 2):
            if i not in (a, b):
                class_sum += rho(transposition(a, b))
        Pi = sp.simplify(class_sum / 2)
        assert Pi * Pi == Pi
        assert Pi.T * G == G * Pi
        assert sp.trace(Pi) == 3
        P.append(Pi)

    assert sum(P, sp.zeros(5)) == 3 * sp.eye(5)

    # Exact covariance under all 120 permutations.
    all_perms = list(permutations(range(N)))
    for g in all_perms:
        Rg = rho(g)
        Rginv = rho(inverse_permutation(g))
        assert Rg * Rginv == sp.eye(5)
        for i in range(N):
            assert sp.simplify(Rg * P[i] * Rginv - P[g[i]]) == sp.zeros(5)

    return K, G, P


def coefficient_by_partition(poly: sp.Poly, mu: Tuple[int, ...], variables) -> sp.Expr:
    alpha = mu + (0,) * (len(variables) - len(mu))
    return sp.factor(poly.coeff_monomial(alpha))


def schur_coefficients_from_monomial(
    monomial_coeffs: Dict[Tuple[int, ...], sp.Expr],
    parts: Sequence[Tuple[int, ...]],
    Kmat: sp.Matrix,
) -> Dict[Tuple[int, ...], sp.Expr]:
    # If s_lambda = sum_mu K_{lambda,mu} m_mu, then c = a K.
    c_row = sp.Matrix([[monomial_coeffs[mu] for mu in parts]])
    a_row = sp.simplify(c_row * Kmat.inv())
    return {lam: sp.factor(a_row[0, j]) for j, lam in enumerate(parts)}


def bialternant_extract(poly: sp.Poly, lam: Tuple[int, ...], variables) -> sp.Expr:
    n = len(variables)
    padded = lam + (0,) * (n - len(lam))
    total = 0
    for sigma in permutations(range(1, n + 1)):
        alpha = tuple(padded[i] - (i + 1) + sigma[i] for i in range(n))
        if min(alpha) >= 0:
            total += permutation_sign(sigma) * poly.coeff_monomial(alpha)
    return sp.factor(total)


def build_certificate(verbose: bool = False):
    Kbasis, G, P = construct_representation()

    # A_i=I+5P_i is G-self-adjoint and G-positive with eigenvalues 6,6,6,1,1.
    A = [sp.eye(5) + 5 * Pi for Pi in P]
    lam_symbol = sp.Symbol("lambda")
    for Ai in A:
        assert Ai.T * G == G * Ai
        assert sp.factor(Ai.charpoly(lam_symbol).as_expr()) == (lam_symbol - 6) ** 3 * (lam_symbol - 1) ** 2

    # Convert to ordinary symmetric integer positive-definite matrices.
    # J_i=2GA_i and det(sum x_iJ_i)=2^5 det(G) det(sum x_iA_i)=5184 p_5.
    J = [sp.simplify(2 * G * Ai) for Ai in A]
    leading_minors = []
    for Ji in J:
        assert Ji == Ji.T
        minors = [sp.factor(Ji[:k, :k].det()) for k in range(1, 6)]
        assert all(m > 0 for m in minors)
        leading_minors.append(minors)
    assert 2 ** 5 * G.det() == 5184

    x = sp.symbols("x1:6")
    pencil = sum((x[i] * J[i] for i in range(N)), sp.zeros(5))
    Q = sp.Poly(sp.expand(pencil.det(method="berkowitz")), *x)

    # All 126 degree-5 monomials occur.
    assert len(Q.terms()) == sp.binomial(9, 4) == 126

    monomial_Q = {mu: coefficient_by_partition(Q, mu, x) for mu in PARTS}
    for alpha, coeff in Q.terms():
        mu = tuple(sorted((a for a in alpha if a), reverse=True))
        assert coeff == monomial_Q[mu]
    assert all(v > 0 for v in monomial_Q.values())

    expected_monomial_Q = {
        (5,): 1119744,
        (4, 1): 12597120,
        (3, 2): 43127640,
        (3, 1, 1): 91309680,
        (2, 2, 1): 162285120,
        (2, 1, 1, 1): 354718440,
        (1, 1, 1, 1, 1): 766493280,
    }
    assert monomial_Q == expected_monomial_Q

    Kmat = kostka_matrix(PARTS)
    expected_K = sp.Matrix(
        [
            [1, 1, 1, 1, 1, 1, 1],
            [0, 1, 1, 2, 2, 3, 4],
            [0, 0, 1, 1, 2, 3, 5],
            [0, 0, 0, 1, 1, 3, 6],
            [0, 0, 0, 0, 1, 2, 5],
            [0, 0, 0, 0, 0, 1, 4],
            [0, 0, 0, 0, 0, 0, 1],
        ]
    )
    assert Kmat == expected_K

    schur_Q = schur_coefficients_from_monomial(monomial_Q, PARTS, Kmat)
    expected_schur_Q = {
        (5,): 1119744,
        (4, 1): 11477376,
        (3, 2): 30530520,
        (3, 1, 1): 36704664,
        (2, 2, 1): 40444920,
        (2, 1, 1, 1): 36571176,
        (1, 1, 1, 1, 1): -1925856,
    }
    assert schur_Q == expected_schur_Q

    # Independent bialternant extraction of every Schur coefficient.
    for lam in PARTS:
        assert bialternant_extract(Q, lam, x) == schur_Q[lam]

    # Verify closed one-parameter family p_t=det(sum x_i(I+tP_i)).
    t = sp.Symbol("t")
    family_pencil = sum((x[i] * (sp.eye(5) + t * P[i]) for i in range(N)), sp.zeros(5))
    p_t_poly = sp.Poly(sp.expand(family_pencil.det(method="berkowitz")), *x)
    monomial_t = {mu: coefficient_by_partition(p_t_poly, mu, x) for mu in PARTS}
    schur_t = schur_coefficients_from_monomial(monomial_t, PARTS, Kmat)

    expected_monomial_t = {
        (5,): (t + 1) ** 3,
        (4, 1): (t + 1) ** 2 * (3 * t**2 + 10 * t + 10) / 2,
        (3, 2): (t + 1) * (9 * t**4 + 72 * t**3 + 232 * t**2 + 320 * t + 160) / 16,
        (3, 1, 1): (t + 1) * (t + 2) * (9 * t**3 + 62 * t**2 + 120 * t + 80) / 8,
        (2, 2, 1): (39 * t**5 + 317 * t**4 + 1040 * t**3 + 1728 * t**2 + 1440 * t + 480) / 16,
        (2, 1, 1, 1): (45 * t**5 + 348 * t**4 + 1100 * t**3 + 1764 * t**2 + 1440 * t + 480) / 8,
        (1, 1, 1, 1, 1): (99 * t**5 + 765 * t**4 + 2320 * t**3 + 3600 * t**2 + 2880 * t + 960) / 8,
    }
    expected_schur_t = {
        (5,): (t + 1) ** 3,
        (4, 1): (t + 1) ** 2 * (3 * t**2 + 8 * t + 8) / 2,
        (3, 2): (t + 1) * (9 * t**4 + 48 * t**3 + 128 * t**2 + 160 * t + 80) / 16,
        (3, 1, 1): (t + 1) * (9 * t**4 + 64 * t**3 + 168 * t**2 + 192 * t + 96) / 16,
        (2, 2, 1): (6 * t**5 + 41 * t**4 + 108 * t**3 + 156 * t**2 + 120 * t + 40) / 8,
        (2, 1, 1, 1): (6 * t**5 + 35 * t**4 + 96 * t**3 + 132 * t**2 + 96 * t + 32) / 8,
        (1, 1, 1, 1, 1): -(9 * t**5 - 21 * t**4 - 56 * t**3 - 72 * t**2 - 48 * t - 16) / 16,
    }
    for mu in PARTS:
        assert sp.factor(monomial_t[mu] - expected_monomial_t[mu]) == 0
        assert sp.factor(schur_t[mu] - expected_schur_t[mu]) == 0

    # At t=5, q=8p_5=Q/648 has an integral expansion and negative sign coefficient.
    monomial_q_exact = {mu: sp.cancel(monomial_Q[mu] / 648) for mu in PARTS}
    schur_q_exact = {lam: sp.cancel(schur_Q[lam] / 648) for lam in PARTS}
    assert all(v.is_Integer for v in monomial_q_exact.values())
    assert all(v.is_Integer for v in schur_q_exact.values())
    monomial_q = {mu: int(monomial_q_exact[mu]) for mu in PARTS}
    schur_q = {lam: int(schur_q_exact[lam]) for lam in PARTS}
    assert monomial_q == {
        (5,): 1728,
        (4, 1): 19440,
        (3, 2): 66555,
        (3, 1, 1): 140910,
        (2, 2, 1): 250440,
        (2, 1, 1, 1): 547405,
        (1, 1, 1, 1, 1): 1182860,
    }
    assert schur_q == {
        (5,): 1728,
        (4, 1): 17712,
        (3, 2): 47115,
        (3, 1, 1): 56643,
        (2, 2, 1): 62415,
        (2, 1, 1, 1): 56437,
        (1, 1, 1, 1, 1): -2972,
    }

    # ------------------------------------------------------------------
    # The lower endpoint (Problem 37) needs a SCHUR-POSITIVE witness.
    #
    # q above is not Schur positive, so it refutes Problem 37 only in the
    # reading where that problem inherits nothing but Problem 36's hypotheses
    # -- and in that reading the refutation is a formal corollary of the
    # Problem 36 one, since a_(d) is the coefficient of x_1^d and hence
    # nonnegative, making "a_lam >= f^lam a_(d)" imply Schur positivity.  The
    # t=4 member of the same family settles the substantive reading: it IS
    # Schur positive and still breaks the endpoint at lam=(1^5).
    #
    # f^lam is not hard-coded either: the number of standard Young tableaux of
    # shape lam is K_{lam,(1^d)}, the last column of the Kostka matrix already
    # built above by enumerating semistandard tableaux.
    # ------------------------------------------------------------------
    f_lambda = {lam: Kmat[i, len(PARTS) - 1] for i, lam in enumerate(PARTS)}
    assert f_lambda == {
        (5,): 1, (4, 1): 4, (3, 2): 5, (3, 1, 1): 6,
        (2, 2, 1): 5, (2, 1, 1, 1): 4, (1, 1, 1, 1, 1): 1,
    }

    Jt = [sp.simplify(2 * G * (sp.eye(5) + 4 * Pi)) for Pi in P]
    leading_minors_t = []
    for i, Jti in enumerate(Jt):
        assert Jti == Jti.T
        assert all(e.is_Integer for e in Jti)
        # The body states the second pencil as (4 J_i + 2 G) / 5, so that only
        # G has to be displayed alongside the J_i already given.
        assert Jti == sp.simplify((4 * J[i] + 2 * G) / 5)
        minors = [sp.factor(Jti[:k, :k].det()) for k in range(1, 6)]
        assert all(m > 0 for m in minors)
        leading_minors_t.append(minors)

    pencil_t = sum((x[i] * Jt[i] for i in range(N)), sp.zeros(5))
    Qt = sp.Poly(sp.expand(pencil_t.det(method="berkowitz")), *x)
    assert len(Qt.terms()) == 126

    # det(sum x_i Jt_i) = 2^5 det(G) p_4 = 5184 p_4, and p_4 is already integral.
    monomial_Qt = {mu: coefficient_by_partition(Qt, mu, x) for mu in PARTS}
    for alpha, coeff in Qt.terms():
        mu = tuple(sorted((a for a in alpha if a), reverse=True))
        assert coeff == monomial_Qt[mu]
    assert all(v > 0 for v in monomial_Qt.values())

    schur_Qt = schur_coefficients_from_monomial(monomial_Qt, PARTS, Kmat)
    for lam in PARTS:
        assert bialternant_extract(Qt, lam, x) == schur_Qt[lam]

    monomial_qt_exact = {mu: sp.cancel(monomial_Qt[mu] / 5184) for mu in PARTS}
    schur_qt_exact = {lam: sp.cancel(schur_Qt[lam] / 5184) for lam in PARTS}
    assert all(v.is_Integer for v in monomial_qt_exact.values())
    assert all(v.is_Integer for v in schur_qt_exact.values())
    monomial_qt = {mu: int(monomial_qt_exact[mu]) for mu in PARTS}
    schur_qt = {lam: int(schur_qt_exact[lam]) for lam in PARTS}
    assert monomial_qt == {
        (5,): 125,
        (4, 1): 1225,
        (3, 2): 3770,
        (3, 1, 1): 7980,
        (2, 2, 1): 13846,
        (2, 1, 1, 1): 30004,
        (1, 1, 1, 1, 1): 64472,
    }
    assert schur_qt == {
        (5,): 125,
        (4, 1): 1100,
        (3, 2): 2545,
        (3, 1, 1): 3110,
        (2, 2, 1): 3321,
        (2, 1, 1, 1): 2972,
        (1, 1, 1, 1, 1): 69,
    }

    # This is the whole point: Schur POSITIVE, hence a witness under either
    # reading of Problem 37 -- and still short of the lower endpoint, at
    # exactly one partition.
    assert all(v > 0 for v in schur_qt.values())
    violated = [lam for lam in PARTS if schur_qt[lam] < f_lambda[lam] * schur_qt[(5,)]]
    assert violated == [(1, 1, 1, 1, 1)]
    assert schur_qt[(1, 1, 1, 1, 1)] == 69 < 125 == f_lambda[(1, 1, 1, 1, 1)] * schur_qt[(5,)]
    # q itself is not Schur positive, which is why it cannot serve here.
    assert schur_q[(1, 1, 1, 1, 1)] < 0

    # Where the two regimes sit: (t+1)^3 - [s_(1^5)]p_t = t^2(9t^3-21t^2-40t-24)/16,
    # so the lower endpoint fails past the cubic's root while Schur positivity
    # survives until the quintic's, and t=4 lies strictly between them.
    endpoint_gap = sp.factor(sp.expand((t + 1) ** 3 - schur_t[(1, 1, 1, 1, 1)]))
    assert endpoint_gap == sp.factor(t**2 * (9 * t**3 - 21 * t**2 - 40 * t - 24) / 16)
    cubic = lambda u: 9 * u**3 - 21 * u**2 - 40 * u - 24
    quintic = lambda u: 9 * u**5 - 21 * u**4 - 56 * u**3 - 72 * u**2 - 48 * u - 16
    assert cubic(4) == 56 > 0 and quintic(4) == -1104 < 0   # t=4: endpoint broken, Schur positive
    assert cubic(3) < 0                                     # t=3: endpoint still holds
    assert quintic(5) == 5944 > 0                           # t=5: Schur positivity already gone

    result = {
        "basis_K": [[int(v) for v in row] for row in Kbasis.tolist()],
        "gram_G": [[int(v) for v in row] for row in G.tolist()],
        "J_matrices": [[[int(v) for v in row] for row in Ji.tolist()] for Ji in J],
        "leading_principal_minors": [[int(v) for v in row] for row in leading_minors],
        "normalization": "q(x) = det(sum_i x_i J_i) / 648 = 8 p_5(x)",
        "monomial_symmetric_coefficients_q": {str(mu): int(monomial_q[mu]) for mu in PARTS},
        "schur_coefficients_q": {str(lam): int(schur_q[lam]) for lam in PARTS},
        "negative_coefficient": {"partition": "(1,1,1,1,1)", "value": -2972},
        "standard_young_tableaux": {str(lam): int(f_lambda[lam]) for lam in PARTS},
        "lower_endpoint_witness": {
            "J_matrices": [[[int(v) for v in row] for row in Jti.tolist()] for Jti in Jt],
            "leading_principal_minors": [[int(v) for v in row] for row in leading_minors_t],
            "normalization": "qtilde(x) = det(sum_i x_i Jtilde_i) / 5184 = p_4(x)",
            "monomial_symmetric_coefficients": {str(mu): monomial_qt[mu] for mu in PARTS},
            "schur_coefficients": {str(lam): schur_qt[lam] for lam in PARTS},
            "schur_positive": True,
            "violated_partition": "(1,1,1,1,1)",
            "violation": "a_(1^5) = 69 < 125 = f^(1^5) a_(5)",
        },
    }

    print("All exact checks passed.")
    print("Counterexample: q(x)=det(sum_i x_i J_i)/648.")
    print("Schur coefficient [s_(1^5)] q = -2972.")
    print("Lower endpoint: qtilde(x)=det(sum_i x_i Jtilde_i)/5184 is Schur positive,")
    print("with [s_(1^5)] qtilde = 69 < 125 = f^(1^5) [s_(5)] qtilde.")
    if verbose:
        print("\nJtilde_i matrices (t=4):")
        for i, Jti in enumerate(Jt, 1):
            print(f"Jtilde_{i} =")
            print(Jti)
        print("\nJ_i matrices:")
        for i, Ji in enumerate(J, 1):
            print(f"J_{i} =")
            print(Ji)
        print("\nLeading principal minors:")
        for i, minors in enumerate(leading_minors, 1):
            print(f"J_{i}: {minors}")
        print("\nMonomial-symmetric expansion of q:")
        for mu in PARTS:
            print(f"  {monomial_q[mu]} * m_{mu}")
        print("\nSchur expansion of q:")
        for lam in PARTS:
            print(f"  {schur_q[lam]} * s_{lam}")

    return result


def verify() -> dict:
    """Standard entry point for tools/verify_all.py."""
    certificate = build_certificate()
    negative = certificate["negative_coefficient"]
    return {
        "id": "aim-problems/verify_pencil",
        "ok": True,
        "summary": (
            f"exact det-pencil Schur expansion, "
            f"[s_{negative['partition']}] q = {negative['value']}; "
            f"Schur-positive t=4 witness with {certificate['lower_endpoint_witness']['violation']}"
        ),
        "witness": certificate,
    }


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--verbose", action="store_true", help="print all matrices and expansions")
    parser.add_argument(
        "--write-json",
        type=Path,
        default=Path(__file__).resolve().parent / "artifacts" / "certificate-36-37.json",
        help="write a machine-readable exact certificate (default: artifacts/certificate-36-37.json)",
    )
    args = parser.parse_args()

    result = build_certificate(verbose=args.verbose)
    args.write_json.parent.mkdir(exist_ok=True)
    args.write_json.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(f"Wrote certificate: {args.write_json}")


if __name__ == "__main__":
    main()
