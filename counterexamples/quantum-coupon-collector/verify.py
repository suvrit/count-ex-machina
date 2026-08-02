#!/usr/bin/env python3
"""Certify exact rational counterexamples to quantum coupon-collector positivity.

Admission standard (see CONTRIBUTING.md): exact arithmetic only.  Every number
below is a `fractions.Fraction` or a Python int; no float is used anywhere.
"""
from __future__ import annotations

from fractions import Fraction
import itertools
import json
import pathlib
import sys
from typing import Sequence

if hasattr(sys, "set_int_max_str_digits"):
    sys.set_int_max_str_digits(0)

Scalar = Fraction
Vector = tuple[int, int, int]
Matrix = list[list[Scalar]]


def zero3() -> Matrix:
    return [[Fraction(0) for _ in range(3)] for _ in range(3)]


def identity3(scale: Scalar = Fraction(1)) -> Matrix:
    out = zero3()
    for i in range(3):
        out[i][i] = scale
    return out


def add3(a: Matrix, b: Matrix) -> Matrix:
    return [[a[i][j] + b[i][j] for j in range(3)] for i in range(3)]


def scale3(c: Scalar, a: Matrix) -> Matrix:
    return [[c * a[i][j] for j in range(3)] for i in range(3)]


def outer3(u: Sequence[int | Scalar]) -> Matrix:
    return [[Fraction(u[i]) * Fraction(u[j]) for j in range(3)] for i in range(3)]


def transpose3(a: Matrix) -> Matrix:
    return [[a[j][i] for j in range(3)] for i in range(3)]


def multiply3(a: Matrix, b: Matrix) -> Matrix:
    return [
        [sum((a[i][k] * b[k][j] for k in range(3)), Fraction(0)) for j in range(3)]
        for i in range(3)
    ]


def subtract3(a: Matrix, b: Matrix) -> Matrix:
    return [[a[i][j] - b[i][j] for j in range(3)] for i in range(3)]


def determinant3(a: Matrix) -> Scalar:
    a00, a01, a02 = a[0]
    a10, a11, a12 = a[1]
    a20, a21, a22 = a[2]
    return (
        a00 * (a11 * a22 - a12 * a21)
        - a01 * (a10 * a22 - a12 * a20)
        + a02 * (a10 * a21 - a11 * a20)
    )


def inverse3(a: Matrix) -> Matrix:
    a00, a01, a02 = a[0]
    a10, a11, a12 = a[1]
    a20, a21, a22 = a[2]
    det = determinant3(a)
    assert det != 0
    return [
        [
            (a11 * a22 - a12 * a21) / det,
            (a02 * a21 - a01 * a22) / det,
            (a01 * a12 - a02 * a11) / det,
        ],
        [
            (a12 * a20 - a10 * a22) / det,
            (a00 * a22 - a02 * a20) / det,
            (a02 * a10 - a00 * a12) / det,
        ],
        [
            (a10 * a21 - a11 * a20) / det,
            (a01 * a20 - a00 * a21) / det,
            (a00 * a11 - a01 * a10) / det,
        ],
    ]


def trace_inverse3(a: Matrix) -> Scalar:
    """tr(A^{-1}) as tr(adj A)/det A, so no full inverse is formed."""
    a00, a01, a02 = a[0]
    a10, a11, a12 = a[1]
    a20, a21, a22 = a[2]
    det = determinant3(a)
    assert det != 0
    trace_adjugate = (
        (a11 * a22 - a12 * a21)
        + (a00 * a22 - a02 * a20)
        + (a00 * a11 - a01 * a10)
    )
    return trace_adjugate / det


def is_symmetric3(a: Matrix) -> bool:
    return a == transpose3(a)


def leading_principal_minors3(a: Matrix) -> tuple[Scalar, Scalar, Scalar]:
    first = a[0][0]
    second = a[0][0] * a[1][1] - a[0][1] * a[1][0]
    third = determinant3(a)
    return first, second, third


def is_spd3(a: Matrix) -> bool:
    return is_symmetric3(a) and all(x > 0 for x in leading_principal_minors3(a))


def quadratic_form3(a: Matrix, v: Sequence[int | Scalar]) -> Scalar:
    return sum(
        (
            Fraction(v[i]) * a[i][j] * Fraction(v[j])
            for i in range(3)
            for j in range(3)
        ),
        Fraction(0),
    )


def coupon_matrix3(matrices: Sequence[Matrix]) -> Matrix:
    """Q_n = sum over nonempty S of (-1)^{|S|-1} (sum_{i in S} X_i)^{-1}."""
    n = len(matrices)
    out = zero3()
    subset_sums: list[Matrix] = [zero3() for _ in range(1 << n)]
    subset_sizes = [0 for _ in range(1 << n)]
    for mask in range(1, 1 << n):
        least_bit = mask & -mask
        index = least_bit.bit_length() - 1
        previous = mask ^ least_bit
        subset_sums[mask] = add3(subset_sums[previous], matrices[index])
        subset_sizes[mask] = subset_sizes[previous] + 1
        sign = Fraction(1 if subset_sizes[mask] % 2 else -1)
        out = add3(out, scale3(sign, inverse3(subset_sums[mask])))
    return out


def coupon_trace3(matrices: Sequence[Matrix]) -> Scalar:
    """Delta_n = tr Q_n, accumulated without forming Q_n."""
    n = len(matrices)
    out = Fraction(0)
    subset_sums: list[Matrix] = [zero3() for _ in range(1 << n)]
    subset_sizes = [0 for _ in range(1 << n)]
    for mask in range(1, 1 << n):
        least_bit = mask & -mask
        index = least_bit.bit_length() - 1
        previous = mask ^ least_bit
        subset_sums[mask] = add3(subset_sums[previous], matrices[index])
        subset_sizes[mask] = subset_sizes[previous] + 1
        sign = Fraction(1 if subset_sizes[mask] % 2 else -1)
        out += sign * trace_inverse3(subset_sums[mask])
    return out


def commutator3(a: Matrix, b: Matrix) -> Matrix:
    return subtract3(multiply3(a, b), multiply3(b, a))


def matrix_is_nonzero3(a: Matrix) -> bool:
    return any(a[i][j] != 0 for i in range(3) for j in range(3))


def rank_one_regularization(u: Vector, weight: int, epsilon: Scalar) -> Matrix:
    return add3(scale3(Fraction(weight), outer3(u)), identity3(epsilon))


def vandermonde_vector(t: int) -> Vector:
    return (1, t, t * t)


def determinant_of_columns(u: Vector, v: Vector, w: Vector) -> Scalar:
    matrix = [
        [Fraction(u[row]), Fraction(v[row]), Fraction(w[row])]
        for row in range(3)
    ]
    return determinant3(matrix)


def fraction_record(x: Scalar) -> dict[str, str]:
    return {"numerator": str(x.numerator), "denominator": str(x.denominator)}


def verify() -> dict:
    """Raise AssertionError if any check fails; return a machine-readable summary."""
    # Theorem thm:quantum-coupon-collector -- the conjecture as posed, at n = 6.
    n6_parameters: tuple[tuple[Vector, int], ...] = (
        ((-1, 2, 1), 10),
        ((0, -3, 1), 10),
        ((-3, -2, 0), 100),
        ((2, -2, -2), 100),
        ((-1, 0, 2), 100),
        ((-1, 3, 0), 100),
    )
    epsilon6 = Fraction(1, 100)
    matrices6 = [rank_one_regularization(u, w, epsilon6) for u, w in n6_parameters]
    assert all(is_spd3(matrix) for matrix in matrices6)
    assert matrix_is_nonzero3(commutator3(matrices6[0], matrices6[1]))

    coupon6 = coupon_matrix3(matrices6)
    test_vector6: Vector = (4, 1, 3)
    negative_quadratic_form6 = quadratic_form3(coupon6, test_vector6)
    assert Fraction(-96) < negative_quadratic_form6 < Fraction(-95)

    # Theorem thm:quantum-coupon-collector-trace -- the scalar consequence, at n = 10.
    epsilon10 = Fraction(1, 10_000)
    vectors10 = [vandermonde_vector(t) for t in range(10)]
    matrices10 = [rank_one_regularization(u, 1, epsilon10) for u in vectors10]
    assert all(is_spd3(matrix) for matrix in matrices10)
    assert matrix_is_nonzero3(commutator3(matrices10[0], matrices10[1]))
    assert all(
        determinant_of_columns(vectors10[i], vectors10[j], vectors10[k]) != 0
        for i, j, k in itertools.combinations(range(10), 3)
    )

    negative_trace10 = coupon_trace3(matrices10)
    assert Fraction(-13_901) < negative_trace10 < Fraction(-13_900)

    return {
        "id": "quantum-coupon-collector",
        "ok": True,
        "summary": (
            "exact n=6 negative quadratic form in (-96,-95); "
            "exact n=10 trace sum in (-13901,-13900)"
        ),
        "witness": {
            "loewner_n6": {
                "dimension": 3,
                "epsilon": "1/100",
                "parameters": [
                    {"u": list(u), "weight": w} for u, w in n6_parameters
                ],
                "test_vector": list(test_vector6),
                "quadratic_form": fraction_record(negative_quadratic_form6),
                "certified_interval": ["-96", "-95"],
                "strictly_positive_definite": True,
                "noncommuting": True,
            },
            "trace_n10": {
                "dimension": 3,
                "epsilon": "1/10000",
                "vectors": [list(u) for u in vectors10],
                "trace_inclusion_exclusion": fraction_record(negative_trace10),
                "certified_interval": ["-13901", "-13900"],
                "all_triples_independent": True,
                "strictly_positive_definite": True,
                "noncommuting": True,
            },
            "positive_range": {"proved_positive_definite_for_n": [1, 2, 3, 4, 5]},
        },
    }


if __name__ == "__main__":
    output = verify()
    artifacts = pathlib.Path(__file__).resolve().parent / "artifacts"
    artifacts.mkdir(exist_ok=True)
    (artifacts / "certificate.json").write_text(
        json.dumps(output["witness"], indent=2, sort_keys=True) + "\n"
    )
    print(f"PASS {output['id']}: {output['summary']}")
