#!/usr/bin/env python3
"""Certify the exact failure of the Rayleigh identity following equation (20)."""
from __future__ import annotations

import json
import pathlib
from fractions import Fraction


Scalar = Fraction
Matrix2 = tuple[tuple[Scalar, Scalar], tuple[Scalar, Scalar]]
Vector2 = tuple[Scalar, Scalar]


def transpose(matrix: Matrix2) -> Matrix2:
    return (
        (matrix[0][0], matrix[1][0]),
        (matrix[0][1], matrix[1][1]),
    )


def matmul(left: Matrix2, right: Matrix2) -> Matrix2:
    return tuple(
        tuple(
            sum((left[i][k] * right[k][j] for k in range(2)), Fraction(0))
            for j in range(2)
        )
        for i in range(2)
    )  # type: ignore[return-value]


def scale(scalar: Scalar, matrix: Matrix2) -> Matrix2:
    return tuple(
        tuple(scalar * entry for entry in row) for row in matrix
    )  # type: ignore[return-value]


def quadratic(vector: Vector2, matrix: Matrix2) -> Scalar:
    product = (
        matrix[0][0] * vector[0] + matrix[0][1] * vector[1],
        matrix[1][0] * vector[0] + matrix[1][1] * vector[1],
    )
    return vector[0] * product[0] + vector[1] * product[1]


def matrix_strings(matrix: Matrix2) -> list[list[str]]:
    return [[str(entry) for entry in row] for row in matrix]


def verify() -> dict:
    """Raise AssertionError if any check fails; return a machine-readable summary."""
    zero: Matrix2 = (
        (Fraction(0), Fraction(0)),
        (Fraction(0), Fraction(0)),
    )
    g: Matrix2 = (
        (Fraction(1), Fraction(0)),
        (Fraction(0), Fraction(0)),
    )
    k: Matrix2 = (
        (Fraction(0), Fraction(0)),
        (Fraction(0), Fraction(-1)),
    )
    x: Vector2 = (Fraction(1), Fraction(2))

    # These are the explicit assumptions on the three local factors.
    assert transpose(zero) == zero
    assert transpose(g) == g
    assert transpose(k) == k
    # G is an orthogonal projection and -K is one too, certifying norm one.
    assert matmul(g, g) == g
    assert matmul(k, k) == scale(Fraction(-1), k)
    assert matmul(g, k) == matmul(k, g)

    norm_squared = quadratic(x, (
        (Fraction(1), Fraction(0)),
        (Fraction(0), Fraction(1)),
    ))
    assert norm_squared == 5

    # Equations (18)--(19), with d=1 and F_1=0.
    h = matmul(g, k)
    assert h == zero
    objective = quadratic(x, h) / norm_squared

    # Equation (20), whose outer scalar prefactor is 1 when d=1.
    k_rayleigh = quadratic(x, k) / norm_squared
    a = scale(k_rayleigh, g)
    proposed_rayleigh = quadratic(x, a) / norm_squared

    assert objective == 0
    assert k_rayleigh == Fraction(-4, 5)
    assert proposed_rayleigh == Fraction(-4, 25)
    assert proposed_rayleigh != objective

    exact_witness = {
        "n": 2,
        "d": 1,
        "F_1": matrix_strings(zero),
        "G_1_1": matrix_strings(g),
        "K_1_1": matrix_strings(k),
        "x_1": [str(entry) for entry in x],
        "x_norm_squared": str(norm_squared),
        "objective_from_equations_18_19": str(objective),
        "rayleigh_from_equation_20": str(proposed_rayleigh),
    }
    return {
        "id": "hamiltonian-nepv-identity",
        "ok": True,
        "summary": "the exact values asserted equal are 0 and -4/25",
        "witness": exact_witness,
    }


if __name__ == "__main__":
    out = verify()
    art = pathlib.Path(__file__).resolve().parent / "artifacts"
    art.mkdir(exist_ok=True)
    (art / "certificate.json").write_text(
        json.dumps(out["witness"], indent=2, sort_keys=True) + "\n"
    )
    print(f"PASS {out['id']}: {out['summary']}")
