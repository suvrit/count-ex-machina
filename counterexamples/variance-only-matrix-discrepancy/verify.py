#!/usr/bin/env python3
"""Exact audit of the counterexample to variance-sensitive Matrix Spencer.

The family of Akbas-Sra (arXiv:2606.16005, Theorem A.1) uses n = 2^m diagonal
matrices of size n x n -- dimension equal to the number of summands, which is
the regime the conjecture is about.  Writing S = {+-1}^m for the coordinate
index set, p and q for the all-plus and all-minus vectors, U subset S \\ {p, q}
with |U| = m, F = S \\ U, and a bijection pi: {m+1, ..., n} -> F:

    (A_i)_{s,s} = s_i / sqrt(m)          for 1 <= i <= m,
    A_k         = E_{pi(k),pi(k)} / sqrt(m)   for m < k <= n.

Every quantity below is an exact integer or Fraction.  Scaling by sqrt(m)
clears the only irrationality: sqrt(m) * A_i has entries in {-1, 0, 1}, so for
a signing x the diagonal of sqrt(m) * sum_i x_i A_i is integral, and

    disc = (1/sqrt(m)) * min_x max_s |integer entry|.

The script checks, by exhaustive enumeration over all 2^n signings:

  1. ||A_i||_op = 1/sqrt(m) <= 1, so the family is admissible;
  2. ||sum_i A_i^2||_op = 1 + 1/m exactly;
  3. min_x max_s |sqrt(m) X_{s,s}| = m - 1, i.e. disc = (m-1)/sqrt(m);
  4. hence (disc / variance^{1/2})^2 = (m-1)^2 / (m+1), which is unbounded.

Independence of the arbitrary choice of U (hence F and pi) is checked by
running several explicit admissible choices, not just one.

Usage:
    python verify.py

Exhaustive signing enumeration costs 2^n, so m <= 4 (n <= 16) is checked.
Stdlib only.
"""

from __future__ import annotations

import json
import pathlib
from fractions import Fraction
from itertools import combinations, product

# 2^n signings are enumerated, so m = 4 (n = 16, 65536 signings) is the ceiling.
M_VALUES = (2, 3, 4)


def coordinates(m):
    """S = {+-1}^m, in a fixed order; |S| = n = 2^m."""
    return [tuple(2 * b - 1 for b in bits) for bits in product((0, 1), repeat=m)]


def admissible_choices_of_U(S, m, limit=3):
    """Subsets U of S \\ {p, q} with |U| = m; F = S \\ U then contains p and q."""
    p, q = (1,) * m, (-1,) * m
    rest = [s for s in S if s not in (p, q)]
    out = []
    for U in combinations(rest, m):
        out.append(set(U))
        if len(out) == limit:
            break
    return out


def scaled_diagonal(m, S, F, pi_inv, x):
    """Diagonal of sqrt(m) * sum_i x_i A_i, as exact integers.

    sqrt(m) * X_{s,s} = sum_{i<=m} x_i s_i + 1{s in F} * x_{pi^{-1}(s)}.
    """
    return [
        sum(x[i] * s[i] for i in range(m)) + (x[pi_inv[s]] if s in F else 0)
        for s in S
    ]


def check_one(m, U):
    """Exact check of the construction for one admissible choice of U."""
    S = coordinates(m)
    n = len(S)
    assert n == 2**m
    p, q = (1,) * m, (-1,) * m
    F = set(S) - U
    assert len(U) == m and p in F and q in F

    # pi: {m+1, ..., n} -> F, as a bijection; store its inverse on F.
    F_list = sorted(F)
    assert len(F_list) == n - m
    pi_inv = {s: m + j for j, s in enumerate(F_list)}

    # (1) ||A_i||_op = 1/sqrt(m) <= 1: every scaled entry is in {-1, 0, 1}.
    for i in range(m):
        assert {abs(s[i]) for s in S} == {1}
    assert m >= 1

    # (2) variance: the s-th diagonal entry of sum_i A_i^2 is 1 + 1{s in F}/m.
    variance_diag = [
        sum(Fraction(s[i] ** 2, m) for i in range(m))
        + sum(Fraction(1, m) for k in range(m, n) if F_list[k - m] == s)
        for s in S
    ]
    expected_diag = [1 + Fraction(1, m) * (1 if s in F else 0) for s in S]
    assert variance_diag == expected_diag
    variance = max(variance_diag)
    assert variance == 1 + Fraction(1, m)

    # (3) discrepancy: exhaustive minimum over all 2^n signings.
    best = None
    for x in product((-1, 1), repeat=n):
        norm = max(abs(v) for v in scaled_diagonal(m, S, F, pi_inv, x))
        if best is None or norm < best:
            best = norm
    assert best == m - 1, (m, best)

    # The signing named in the proof attains it.
    k_p, k_q = pi_inv[p], pi_inv[q]
    witness = [1] * n
    witness[k_p], witness[k_q] = -1, 1
    attained = max(abs(v) for v in scaled_diagonal(m, S, F, pi_inv, tuple(witness)))
    assert attained == m - 1

    # (4) ratio^2 = disc^2 / variance = ((m-1)^2/m) / ((m+1)/m) = (m-1)^2/(m+1).
    disc_squared = Fraction((m - 1) ** 2, m)
    ratio_squared = disc_squared / variance
    assert ratio_squared == Fraction((m - 1) ** 2, m + 1)
    return {
        "m": m,
        "n": n,
        "variance": str(variance),
        "min_scaled_operator_norm": best,
        "disc_squared": str(disc_squared),
        "ratio_squared": str(ratio_squared),
    }


def verify() -> dict:
    """Standard entry point for tools/verify_all.py."""
    records = []
    for m in M_VALUES:
        S = coordinates(m)
        for U in admissible_choices_of_U(S, m):
            records.append(check_one(m, U))
    ratios = {r["m"]: r["ratio_squared"] for r in records}
    return {
        "id": "variance-only-matrix-discrepancy",
        "ok": True,
        "summary": (
            "exact d=n diagonal family; (disc/variance^(1/2))^2 = (m-1)^2/(m+1), "
            f"checked for m in {list(M_VALUES)}"
        ),
        "witness": {
            "source": "Akbas and Sra, An Algebraic Matrix Spencer Theorem, Theorem A.1",
            "regime": "n = 2^m matrices of size n x n (dimension = number of summands)",
            "identities": {
                "variance": "||sum_i A_i^2||_op = 1 + 1/m",
                "discrepancy": "disc = (m-1)/sqrt(m)",
                "ratio_squared": "(m-1)^2/(m+1), unbounded in m = log_2(n)",
            },
            "ratio_squared_by_m": ratios,
            "checks": records,
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
