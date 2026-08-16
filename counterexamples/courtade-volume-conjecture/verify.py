#!/usr/bin/env python3
"""Exact refutation of Courtade's Minkowski-volume conjecture (ISIT 2017) in R^4.

The conjecture: for bounded convex sets K, L, B in R^d,

    |K+L+B|^{1/d} |B|^{1/d} + |K|^{1/d} |L|^{1/d}  <=  |K+B|^{1/d} |L+B|^{1/d},

with |.| the d-dimensional volume and + the Minkowski sum.  Witness: B := A,
a zonotope in R^4 with seven integer generators, and K, L two segments (then
thin boxes, so all three sets are convex bodies).  Every volume is a zonotope
volume, computed by the classical generator formula

    Vol(Z(v_1..v_m)) = sum over 4-subsets S of |det(v_S)|

(Shephard, Combinatorial structure of zonotopes, 1974), so the whole
certificate is integer respectively rational arithmetic.  Because x -> x^4 is
strictly increasing on the nonnegative reals, each conjectured inequality of
1/4-powers is compared through its exact fourth power; no root is ever
extracted.

Admission standard (see CONTRIBUTING.md): exact arithmetic (fractions,
integers, algebraic identities) or a rigorous interval certificate.
Floating-point-only evidence is inadmissible.
"""
from __future__ import annotations
import itertools
import json
import pathlib
from fractions import Fraction


def det4(rows) -> Fraction:
    """Determinant of a 4x4 matrix given as four row 4-tuples, by cofactors."""
    a, b, c, d = rows

    def det3(r1, r2, r3):
        return (r1[0] * (r2[1] * r3[2] - r2[2] * r3[1])
                - r1[1] * (r2[0] * r3[2] - r2[2] * r3[0])
                + r1[2] * (r2[0] * r3[1] - r2[1] * r3[0]))

    total = 0
    for j in range(4):
        cols = [k for k in range(4) if k != j]
        minor = [tuple(r[k] for k in cols) for r in (b, c, d)]
        total += (-1) ** j * a[j] * det3(*minor)
    return total


def zonotope_volume(generators):
    """Vol of sum_i [0, v_i] in R^4: sum of |det| over all 4-subsets."""
    return sum(abs(det4(S)) for S in itertools.combinations(generators, 4))


# The witness.  A is the zonotope spanned by the four standard basis vectors
# and three further integer generators; b and c generate the two segments.
A_GENS = [
    (1, 0, 0, 0),
    (0, 1, 0, 0),
    (0, 0, 1, 0),
    (0, 0, 0, 1),
    (0, 1, -1, 1),
    (1, 0, -1, 1),
    (0, 0, 1, 1),
]
b = (1, -1, 1, 1)
c = (0, 0, -1, 1)

EPS = Fraction(1, 100)  # thickening for the full-dimensional variant


def verify() -> dict:
    """Raise AssertionError if any check fails; return a machine-readable summary."""
    # --- segment form: K = [0,b], L = [0,c], B = A --------------------------
    vA = zonotope_volume(A_GENS)
    vAB = zonotope_volume(A_GENS + [b])
    vAC = zonotope_volume(A_GENS + [c])
    vABC = zonotope_volume(A_GENS + [b, c])
    assert (vA, vAB, vAC, vABC) == (28, 68, 44, 108)

    # Segments have volume 0, so the conjectured inequality reads
    # (vA * vABC)^{1/4} <= (vAB * vAC)^{1/4}; compare fourth powers.
    assert vAB * vAC == 2992
    assert vA * vABC == 3024
    assert vAB * vAC < vA * vABC  # 2992 < 3024: the conjecture fails.

    # --- full-dimensional form: thicken each segment by an EPS-cube ---------
    cube = [tuple(EPS if i == j else 0 for i in range(4)) for j in range(4)]
    B_eps = [b] + cube
    C_eps = [c] + cube
    vBe = zonotope_volume(B_eps)
    vCe = zonotope_volume(C_eps)
    vABe = zonotope_volume(A_GENS + B_eps)
    vACe = zonotope_volume(A_GENS + C_eps)
    vABCe = zonotope_volume(A_GENS + B_eps + C_eps)

    assert vBe == Fraction(401, 10**8) > 0    # K is a convex body
    assert vCe == Fraction(201, 10**8) > 0    # L is a convex body
    assert vA > 0                              # B is a convex body
    assert vABe == Fraction(6926731601, 10**8)
    assert vACe == Fraction(4484551401, 10**8)
    assert vABCe == Fraction(696978401, 6250000)

    # Conjecture: (vA*vABCe)^{1/4} + (vBe*vCe)^{1/4} <= (vABe*vACe)^{1/4}.
    # Already the first right-hand term beats the left side in fourth powers,
    # and the second term is positive, so the inequality fails a fortiori.
    gap = vA * vABCe - vABe * vACe
    assert gap == Fraction(161348459184476999, 10**16)
    assert gap > 0
    assert vBe * vCe > 0

    return {
        "id": "courtade-volume-conjecture",
        "ok": True,
        "summary": (
            "R^4 zonotope A (7 integer generators) and segments b, c with "
            "Vol(A)=28, Vol(A+B)=68, Vol(A+C)=44, Vol(A+B+C)=108: "
            "68*44 = 2992 < 3024 = 28*108; violation survives thickening "
            "the segments to boxes of side 1/100"
        ),
        "witness": {
            "dimension": 4,
            "A_generators": [list(g) for g in A_GENS],
            "b": list(b),
            "c": list(c),
            "volumes_segment_form": {
                "A": str(vA), "A+B": str(vAB), "A+C": str(vAC), "A+B+C": str(vABC),
            },
            "products_segment_form": {
                "Vol(A+B)*Vol(A+C)": str(vAB * vAC),
                "Vol(A)*Vol(A+B+C)": str(vA * vABC),
            },
            "thickening_eps": str(EPS),
            "volumes_thickened": {
                "B_eps": str(vBe), "C_eps": str(vCe),
                "A+B_eps": str(vABe), "A+C_eps": str(vACe),
                "A+B_eps+C_eps": str(vABCe),
            },
            "thickened_gap_Vol(A)Vol(A+B+C)-Vol(A+B)Vol(A+C)": str(gap),
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
