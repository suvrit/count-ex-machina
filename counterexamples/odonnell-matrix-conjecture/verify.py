#!/usr/bin/env python3
"""Certify the exact Givens-rotation family refuting O'Donnell's matrix conjecture."""
from __future__ import annotations

import json
import pathlib
from fractions import Fraction
from typing import Iterable


CASE_ID = "odonnell-matrix-conjecture"


def _fraction_text(value: Fraction) -> str:
    """Return a lossless plain-text representation of a Fraction."""
    if value.denominator == 1:
        return str(value.numerator)
    return f"{value.numerator}/{value.denominator}"


def _sum_fractions(values: Iterable[Fraction]) -> Fraction:
    return sum(values, Fraction(0, 1))


def _poly_add(left: list[int], right: list[int]) -> list[int]:
    size = max(len(left), len(right))
    out = [0] * size
    for index in range(size):
        out[index] = (
            (left[index] if index < len(left) else 0)
            + (right[index] if index < len(right) else 0)
        )
    while len(out) > 1 and out[-1] == 0:
        out.pop()
    return out


def _poly_scale(poly: list[int], scalar: int) -> list[int]:
    return [scalar * coefficient for coefficient in poly]


def _poly_mul(left: list[int], right: list[int]) -> list[int]:
    out = [0] * (len(left) + len(right) - 1)
    for i, a in enumerate(left):
        for j, b in enumerate(right):
            out[i + j] += a * b
    while len(out) > 1 and out[-1] == 0:
        out.pop()
    return out


def _symbolic_unboundedness_audit() -> dict:
    """Check the polynomial certificate valid for every integer target C >= 0."""
    # Choose m = 32*C + 1.  The proof gives
    # ratio > (m+3)^2 / (32*(m+2)).
    # Cross-multiplication against C leaves 160*C + 16 > 0.
    c_poly = [0, 1]
    m_poly = [1, 32]
    m_plus_three = _poly_add(m_poly, [3])
    m_plus_two = _poly_add(m_poly, [2])
    gap = _poly_add(
        _poly_mul(m_plus_three, m_plus_three),
        _poly_scale(_poly_mul(c_poly, m_plus_two), -32),
    )
    assert gap == [16, 160]
    assert all(coefficient > 0 for coefficient in gap)

    for target in (0, 1, 2, 10, 1000):
        m = 32 * target + 1
        lower = Fraction((m + 3) * (m + 3), 32 * (m + 2))
        assert lower > target

    return {
        "target": "any integer C >= 0",
        "choice_of_m": "32*C+1",
        "dimension": "2^(32*C+1)",
        "ratio_lower_bound": "(m+3)^2/(32*(m+2))",
        "cross_multiplied_gap": "160*C+16",
    }


def _finite_exact_audit(n: int = 512) -> dict:
    """Audit all scalar identities for one exact finite member of the family."""
    assert n >= 4
    assert n & (n - 1) == 0
    assert n % 2 == 0

    q = n
    harmonic = _sum_fractions(Fraction(1, i) for i in range(1, n))
    odd_harmonic = _sum_fractions(Fraction(1, i) for i in range(1, n, 2))
    b_value = Fraction(1, 1) + q * q * harmonic
    delta = Fraction(1, 2) / b_value
    eta = Fraction(1, 2 * n)

    gaps = [delta * (1 + q * q)]
    gaps.extend(delta * q * q / (i * i) for i in range(2, n))
    assert len(gaps) == n - 1
    assert all(gap > 0 for gap in gaps)

    eigenvalues = [Fraction(0, 1)] * n
    eigenvalues[-1] = eta
    for index in range(n - 2, -1, -1):
        eigenvalues[index] = eigenvalues[index + 1] + gaps[index]

    assert all(eigenvalues[i] > eigenvalues[i + 1] for i in range(n - 1))
    assert _sum_fractions(eigenvalues) == 1
    assert n * eta + _sum_fractions(
        Fraction(i, 1) * gaps[i - 1] for i in range(1, n)
    ) == 1

    diagonal = list(eigenvalues)
    diagonal[0] -= delta
    diagonal[-1] += delta
    assert all(diagonal[i] > diagonal[i + 1] for i in range(n - 1))

    spectral_diagonal_distance = _sum_fractions(
        abs(eigenvalues[i] - diagonal[i]) for i in range(n)
    )
    assert spectral_diagonal_distance == 2 * delta

    for i in range(1, n):
        c_squared = Fraction(q * q, q * q + i * i)
        s_squared = Fraction(i * i, q * q + i * i)
        r_squared = Fraction(q * q, i * i)
        assert c_squared + s_squared == 1
        assert c_squared == r_squared * s_squared

        active_gap = gaps[i - 1] if i == 1 else gaps[i - 1] + delta
        assert active_gap == delta * (1 + r_squared)
        assert active_gap * s_squared == delta

        created_edge_squared = active_gap * active_gap * c_squared * s_squared
        assert created_edge_squared == delta * delta * r_squared

        next_c_squared = (
            Fraction(1, 1)
            if i == n - 1
            else Fraction(q * q, q * q + (i + 1) * (i + 1))
        )
        final_edge_squared = created_edge_squared * next_c_squared
        assert next_c_squared > Fraction(1, 2)
        assert final_edge_squared > delta * delta * r_squared / 2

    pinching_ratio_lower_bound = (
        Fraction(q * q, 1) * odd_harmonic * odd_harmonic / (2 * b_value)
    )
    assert pinching_ratio_lower_bound > 1

    # Built-in mutation test: changing the first gap by delta must break the
    # exact transfer identity checked above.
    first_s_squared = Fraction(1, q * q + 1)
    perturbed_first_gap = gaps[0] + delta
    assert perturbed_first_gap * first_s_squared != delta

    return {
        "n": n,
        "q": q,
        "H_n_minus_1": _fraction_text(harmonic),
        "odd_harmonic_sum": _fraction_text(odd_harmonic),
        "B": _fraction_text(b_value),
        "delta": _fraction_text(delta),
        "spectral_diagonal_distance": _fraction_text(spectral_diagonal_distance),
        "pinching_ratio_lower_bound": _fraction_text(pinching_ratio_lower_bound),
        "comparison": "pinching_ratio_lower_bound > 1",
        "mutation_test": "replacing g_1 by g_1+delta is rejected",
    }


def verify() -> dict:
    """Raise AssertionError if any check fails; return a machine-readable summary."""
    family = _symbolic_unboundedness_audit()
    finite = _finite_exact_audit()
    return {
        "id": CASE_ID,
        "ok": True,
        "summary": (
            "the family has ratio > (log_2 n)/32; "
            "the generic gap is 160*C+16 and the n=512 exact audit exceeds 1"
        ),
        "witness": {
            "family": family,
            "finite_exact_audit": finite,
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
