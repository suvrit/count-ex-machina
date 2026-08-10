#!/usr/bin/env python3
"""Exact audit of the Macdonald lattice Schur-convexity counterexample.

The rank-two reversal is checked at sample rational parameters together with
the algebraic identity 1 + r + r^2 - 3r = (1-r)^2 that yields the full
one-parameter family 0 < r < 1.

Everything past that is the general (q,t) statement developed in the paper's
appendix, and none of it is quoted: the rank-two Macdonald polynomial itself is
recovered from the (q,t) Hall inner product, the reversal is proved as a
rational-function identity in q and t, the lattice membership that makes the
point admissible is checked symbolically, and the 1^n-normalized ratio is shown
to satisfy the inequality that Omega fails -- which is what confines the
refutation to the principal-specialization normalization.

Requires: sympy
"""
from __future__ import annotations
from fractions import Fraction as F
import json
import pathlib

import sympy as sp

SAMPLES = [F(1, 2), F(2, 3), F(9, 10)]
# (q, t) with t = q^k, so that 1^2 lies on the lattice; k = 1 is the Schur case.
LATTICE_SAMPLES = [(F(1, 2), 1), (F(1, 2), 2), (F(2, 3), 3)]

q, t, x1, x2 = sp.symbols("q t x1 x2", positive=True)
A_CLOSED = (1 + q) * (1 - t) / (1 - q * t)


def macdonald_coefficient():
    """The coefficient A in P_(2,0) = m_(2) + A m_(1,1), from orthogonality.

    Not quoted: in degree two the (q,t) Hall inner product
    <p_l, p_m> = delta_lm z_l prod_i (1-q^l_i)/(1-t^l_i) together with the
    triangularity P_lambda = m_lambda + (lower terms) determines A outright,
    since P_(1,1) = e_2 = m_(1,1) is the only lower Macdonald polynomial.
    """
    ip_22 = 2 * (1 - q**2) / (1 - t**2)          # <p_2, p_2>
    ip_1111 = 2 * ((1 - q) / (1 - t)) ** 2       # <p_1^2, p_1^2>;  <p_2, p_1^2> = 0
    A = sp.Symbol("A")
    # Coordinates in the basis (p_2, p_1^2): e_2 = (p_1^2 - p_2)/2, m_(2) = p_2.
    P11 = (sp.Rational(-1, 2), sp.Rational(1, 2))
    P20 = (1 - A / 2, A / 2)
    pairing = P20[0] * P11[0] * ip_22 + P20[1] * P11[1] * ip_1111
    solutions = sp.solve(sp.Eq(sp.simplify(pairing), 0), A)
    assert len(solutions) == 1
    return sp.simplify(solutions[0])


def verify() -> dict:
    # --- the rank-two Schur specialization carried in the body of the paper ---
    for r in SAMPLES:
        lhs = F(3, 1) / (1 + r + r * r)
        rhs = 1 / r
        assert lhs < rhs
        assert 1 + r + r * r - 3 * r == (1 - r) ** 2

    # --- the Macdonald polynomial itself, recovered rather than quoted ---
    A = macdonald_coefficient()
    assert sp.simplify(A - A_CLOSED) == 0
    assert sp.simplify(A.subs(t, q)) == 1          # q=t: P_(2,0) becomes s_(2)

    P20 = x1**2 + x2**2 + A_CLOSED * x1 * x2
    P11 = x1 * x2
    # Omega_lambda(x) = P_lambda(x) / P_lambda(t^delta), t^delta = (t, 1) here.
    omega20 = P20.subs({x1: 1, x2: 1}) / P20.subs({x1: t, x2: 1})
    omega11 = P11.subs({x1: 1, x2: 1}) / P11.subs({x1: t, x2: 1})
    assert sp.simplify(omega11 - 1 / t) == 0

    # --- the reversal, as an identity in q and t ---
    gap = sp.simplify(omega11 - omega20)
    gap_closed = (1 - t) ** 2 * (1 - q * t) / (t * (1 + t) * (1 - q * t**2))
    assert sp.simplify(gap - gap_closed) == 0
    # The denominator's factorization is what makes every factor's sign visible.
    assert sp.simplify((1 + t**2 + A_CLOSED * t) - (1 + t) * (1 - q * t**2) / (1 - q * t)) == 0
    # On 0<q,t<1 each of (1-t)^2, (1-qt), t, (1+t), (1-qt^2) is strictly
    # positive, so the gap is too; checked at exact rationals as well.
    for qv, k in LATTICE_SAMPLES:
        tv = qv**k
        a = (1 + qv) * (1 - tv) / (1 - qv * tv)
        assert (2 + a) / (1 + tv * tv + a * tv) < 1 / tv

    # --- lattice membership: 1^n lies on L_n^{q,q^k,1}, so the point is legal ---
    k, n, i = sp.symbols("k n i", positive=True, integer=True)
    # mu_i = k(n-i) is weakly decreasing in i, and q^{-mu_i} t^{n-i} = 1 at t=q^k.
    assert sp.simplify((q ** (-k * (n - i))) * (q**k) ** (n - i) - 1) == 0
    assert sp.simplify((k * (n - i)) - (k * (n - (i + 1)))) == k   # decreasing

    # --- why it happens: the determinant shift is not free for Omega ---
    # P_lambda(y) = (y_1...y_N)^c P_{lambda-c(1^N)}(y) evaluated at t^delta picks
    # up prod_i t^{N-i} = t^{N(N-1)/2} per unit of c, so Omega carries a t-power
    # that the naive shift omits.
    N = sp.Symbol("N", positive=True, integer=True)
    assert sp.simplify(sp.summation(N - i, (i, 1, N)) - N * (N - 1) / 2) == 0
    # Instance N=2, lambda=(1,1), c=1, so lambda-c(1^2)=(0,0) and Omega_(0,0)=1.
    # P_(1,1)(y)=y_1y_2 and P_(1,1)(t^delta)=P_(1,1)(t,1)=t, so Omega is y_1y_2/t.
    y1, y2 = sp.symbols("y1 y2", positive=True)
    shift, omega_00 = 2 * (2 - 1) // 2, sp.Integer(1)
    omega_11_actual = (y1 * y2) / t
    omega_11_lemma = ((y1 * y2) / t**shift) ** 1 * omega_00
    assert sp.simplify(omega_11_actual - omega_11_lemma) == 0
    # The shift without the t-power is off by exactly the factor that drives the
    # counterexample, and agrees only at t=1.
    omega_11_naive = y1 * y2
    assert sp.simplify(omega_11_actual - omega_11_naive - (1 - t) * y1 * y2 / t) == 0
    assert sp.simplify((omega_11_actual - omega_11_naive).subs(t, 1)) == 0

    # --- scope: the 1^n-normalized ratio satisfies what Omega violates ---
    W20 = P20 / P20.subs({x1: 1, x2: 1})
    W11 = P11 / P11.subs({x1: 1, x2: 1})
    assert sp.simplify((W20 - W11) - (x1 - x2) ** 2 / (2 + A_CLOSED)) == 0
    assert sp.simplify(W20.subs({x1: 1, x2: 1})) == 1
    assert sp.simplify(W11.subs({x1: 1, x2: 1})) == 1

    return {
        "id": "macdonald-schur-convexity",
        "ok": True,
        "summary": (
            "exact rank-two reversal; general (q,t) gap "
            "(1-t)^2(1-qt)/(t(1+t)(1-qt^2)) > 0 on the lattice t=q^k"
        ),
        "witness": {
            "sample_r": [str(r) for r in SAMPLES],
            "reversal": "3/(1+r+r^2) < 1/r for all 0<r<1",
            "identity": "1+r+r^2-3r = (1-r)^2",
            "macdonald_coefficient": "A = (1+q)(1-t)/(1-qt), from the (q,t) Hall inner product",
            "general_gap": "Omega_(1,1)(1^2) - Omega_(2,0)(1^2) = (1-t)^2(1-qt)/(t(1+t)(1-qt^2))",
            "lattice_membership": "1^n in L_n^{q,q^k,1} via mu_i = k(n-i)",
            "lattice_samples": [f"q={qv}, t=q^{k}={qv**k}" for qv, k in LATTICE_SAMPLES],
            "determinant_shift": (
                "Omega_lambda(y) = ((y_1...y_N)/t^{N(N-1)/2})^c Omega_{lambda-c(1^N)}(y); "
                "the naive shift omits the t-power and is false already at N=2, lambda=(1,1)"
            ),
            "scope": "W_(2,0)(x) - W_(1,1)(x) = (x_1-x_2)^2/(2+A) >= 0, so the 1^n normalization survives",
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
