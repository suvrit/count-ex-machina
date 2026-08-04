#!/usr/bin/env python3
"""Certify the exact three-atom OSI and its sketch-and-solve failure."""
from __future__ import annotations
from fractions import Fraction as F
import json
import pathlib


def transpose(a):
    return [list(row) for row in zip(*a)]


def matmul(a, b):
    return [
        [sum((a[i][t] * b[t][j] for t in range(len(b))), F(0))
         for j in range(len(b[0]))]
        for i in range(len(a))
    ]


def add_scaled(acc, scale, a):
    for i in range(len(a)):
        for j in range(len(a[0])):
            acc[i][j] += scale * a[i][j]


def gram(omega):
    return matmul(omega, transpose(omega))


def sketch_inner(omega, u, v):
    g = gram(omega)
    return sum((u[i] * g[i][j] * v[j]
                for i in range(len(u)) for j in range(len(v))), F(0))


def s(x):
    return str(x)


def verify() -> dict:
    """Raise AssertionError if any exact check fails; return a summary."""
    rho = F(1, 100)
    identity = [[F(1), F(0)], [F(0), F(1)]]
    b_plus = [[F(1), F(0)], [F(1), F(0)]]
    b_minus = [[F(1), F(0)], [F(-1), F(0)]]
    atoms = [(F(1) - 2 * rho, identity), (rho, b_plus), (rho, b_minus)]

    expectation = [[F(0), F(0)], [F(0), F(0)]]
    for probability, omega in atoms:
        add_scaled(expectation, probability, gram(omega))
    assert expectation == identity

    # The exact quadratic-form identity proves that, on every fixed line,
    # at least one of the two signed atoms has injectivity one.
    g_plus = gram(b_plus)
    g_minus = gram(b_minus)
    assert [[g_plus[i][j] + g_minus[i][j] for j in range(2)]
            for i in range(2)] == [[F(2), F(0)], [F(0), F(2)]]
    injection_success_lower_bound = F(1) - rho
    assert injection_success_lower_bound == F(99, 100)

    a = [F(1), F(0)]
    b = [F(0), F(1)]
    residuals = []
    bad_probability = F(0)
    for probability, omega in atoms:
        denominator = sketch_inner(omega, a, a)
        assert denominator > 0
        x_tilde = sketch_inner(omega, a, b) / denominator
        residual_squared = x_tilde * x_tilde + F(1)
        residuals.append((probability, x_tilde, residual_squared))
        if residual_squared > 1:
            bad_probability += probability
    assert residuals == [
        (F(49, 50), F(0), F(1)),
        (F(1, 100), F(1), F(2)),
        (F(1, 100), F(-1), F(2)),
    ]
    assert bad_probability == F(1, 50) > rho

    # For any proposed positive hidden constant C, epsilon=1/(4C)
    # makes (1+C epsilon)^2=25/16<2 on the bad atoms.
    assert F(25, 16) < F(2)

    witness = {
        "rho": s(rho),
        "atoms": [
            {"probability": s(p), "matrix": [[s(x) for x in row] for row in o]}
            for p, o in atoms
        ],
        "isotropy": [[s(x) for x in row] for row in expectation],
        "injection_success_probability_at_least": s(injection_success_lower_bound),
        "bad_probability": s(bad_probability),
        "squared_residual_ratios": [s(item[2]) for item in residuals],
    }
    return {
        "id": "osi-sketch-and-solve",
        "ok": True,
        "summary": "isotropy is exact; OSI success is at least 99/100; squared residual ratio 2 occurs with probability 1/50",
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
