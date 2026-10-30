#!/usr/bin/env python3
"""Certify a 3-by-3 Hermitian exponential determinant counterexample.

All arithmetic that decides a check is integral or fractions.Fraction.
Matrix exponentials use rational Taylor sums and a proved norm-tail bound.
The result is a rigorous interval certificate, not a numerical approximation.
"""

import json
import pathlib
from dataclasses import dataclass
from fractions import Fraction as F

CASE_ID = "hermitian-exponential-determinant"
DEGREE = 256
H = ((-26, 10, -10), (10, -16, 20), (-10, 20, -26))
K = ((0, 0, 0), (0, 10, 0), (0, 0, 20))

# Decimal strings below denote exact rational numbers, not machine decimals.
CLAIMED_BOUNDS = {
    "normalized_lhs": (
        "1.0106259614312670597488454657",
        "1.0106259614312670597488454658",
    ),
    "normalized_rhs": (
        "1.0066369661468304923537507020",
        "1.0066369661468304923537507021",
    ),
    "normalized_linear_coefficient": (
        "-0.0081120478335667666163258676",
        "-0.0081120478335667666163258675",
    ),
}


def require(condition: bool, message: str) -> None:
    """Checks remain active even when Python is invoked with -O."""
    if not condition:
        raise AssertionError(message)


@dataclass(frozen=True)
class Interval:
    lo: F
    hi: F

    def __post_init__(self):
        require(isinstance(self.lo, F) and isinstance(self.hi, F),
                "Interval endpoints must be Fractions")
        require(self.lo <= self.hi, "Reversed interval")

    def __add__(self, other):
        if not isinstance(other, Interval):
            other = point(other)
        return Interval(self.lo + other.lo, self.hi + other.hi)

    __radd__ = __add__

    def __neg__(self):
        return Interval(-self.hi, -self.lo)

    def __sub__(self, other):
        if not isinstance(other, Interval):
            other = point(other)
        return self + (-other)

    def __mul__(self, other):
        if not isinstance(other, Interval):
            other = point(other)
        products = (self.lo * other.lo, self.lo * other.hi,
                    self.hi * other.lo, self.hi * other.hi)
        return Interval(min(products), max(products))

    __rmul__ = __mul__


def rational(x):
    require(isinstance(x, (int, str, F)), "Non-rational input")
    return F(x)


def point(x):
    x = rational(x)
    return Interval(x, x)


def shape(A):
    require(len(A) > 0 and len(A[0]) > 0, "Empty matrix")
    require(all(len(row) == len(A[0]) for row in A), "Ragged matrix")
    return len(A), len(A[0])


def identity(n, constructor=F):
    return [[constructor(int(i == j)) for j in range(n)] for i in range(n)]


def add(A, B):
    require(shape(A) == shape(B), "Addition dimension mismatch")
    return [[a + b for a, b in zip(ar, br)] for ar, br in zip(A, B)]


def scale(A, s):
    return [[s * a for a in row] for row in A]


def matmul(A, B):
    n, k = shape(A)
    k2, m = shape(B)
    require(k == k2, "Multiplication dimension mismatch")
    return [[sum(A[i][h] * B[h][j] for h in range(k))
             for j in range(m)] for i in range(n)]


def trace(A):
    n, m = shape(A)
    require(n == m, "Trace requires a square matrix")
    return sum(A[i][i] for i in range(n))


def det3(A):
    require(shape(A) == (3, 3), "This determinant formula is for size 3")
    return (A[0][0] * (A[1][1] * A[2][2] - A[1][2] * A[2][1])
            - A[0][1] * (A[1][0] * A[2][2] - A[1][2] * A[2][0])
            + A[0][2] * (A[1][0] * A[2][1] - A[1][1] * A[2][0]))


def infinity_norm(M):
    return max(sum(abs(rational(x)) for x in row) for row in M)


def factorial(n):
    require(isinstance(n, int) and n >= 0, "Invalid factorial argument")
    out = 1
    for k in range(2, n + 1):
        out *= k
    return out


def tail_bound(r, degree=DEGREE):
    r = rational(r)
    require(isinstance(degree, int) and degree >= 0, "Invalid Taylor degree")
    require(0 <= r < degree + 2, "Taylor degree too small for tail bound")
    return (r ** (degree + 1) / factorial(degree + 1)
            / (1 - r / (degree + 2)))


def exp_enclosure(M, degree=DEGREE):
    """Enclose exp(M) entrywise by exact rational intervals.

    For r = ||M||_infinity < degree+2, consecutive omitted scalar terms
    have ratio at most r/(degree+2). Submultiplicativity bounds the
    matrix-norm tail by r**(degree+1)/(degree+1)!/(1-r/(degree+2)).
    Each entry is therefore enclosed by the Taylor sum +/- that bound.
    """
    n, m = shape(M)
    require(n == m, "Exponential requires a square matrix")
    M = [[rational(x) for x in row] for row in M]
    error = tail_bound(infinity_norm(M), degree)
    term = identity(n)
    total = identity(n)
    for k in range(1, degree + 1):
        term = scale(matmul(term, M), F(1, k))
        total = add(total, term)
    return [[Interval(x - error, x + error) for x in row] for row in total]


def evaluate(H0, K0):
    """Return enclosures for the two normalized sides and linear coefficient."""
    require(shape(H0) == shape(K0) == (3, 3), "Witness must have size 3")
    for name, M in (("H", H0), ("K", K0)):
        require(all(isinstance(x, int) for row in M for x in row),
                name + " must have integer entries")
        require(all(M[i][j] == M[j][i] for i in range(3) for j in range(3)),
                name + " must be real symmetric, hence Hermitian")
    require(all(K0[i][j] == 0 for i in range(3) for j in range(3) if i != j),
            "The diagonal exponential shortcut requires diagonal K")

    A = exp_enclosure(H0)
    E = exp_enclosure(add(H0, K0))
    D = [[point(0) for _ in range(3)] for _ in range(3)]
    for i in range(3):
        # Read the diagonal from K0, never from a duplicate list of constants.
        D[i][i] = exp_enclosure([[-K0[i][i]]])[0][0]
    I = identity(3, point)
    DA = matmul(D, A)
    lhs_det = det3(add(I, DA))
    require(lhs_det.lo > 0, "Could not certify positive left determinant")
    lhs = Interval(lhs_det.lo ** 2, lhs_det.hi ** 2)
    DED = matmul(matmul(D, E), D)
    DA2D = matmul(matmul(DA, A), D)
    rhs = det3(add(add(I, DA2D), scale(DED, 2)))
    linear = 2 * (trace(DED) - trace(DA))
    return {
        "normalized_lhs": lhs,
        "normalized_rhs": rhs,
        "normalized_linear_coefficient": linear,
    }


def enclosing_rationals(x, digits=45):
    """Compact artifact bounds, rounded OUTWARD using integer division only."""
    den = 10 ** digits
    lo = F((x.lo.numerator * den) // x.lo.denominator, den)
    hi = F(-((-x.hi.numerator * den) // x.hi.denominator), den)
    require(lo <= x.lo <= x.hi <= hi, "Invalid outward rounding")
    return {"lower": str(lo), "upper": str(hi)}


def verify() -> dict:
    """Raise AssertionError on any failed check; return a machine-readable summary."""
    values = evaluate(H, K)
    lhs, rhs = values["normalized_lhs"], values["normalized_rhs"]
    linear = values["normalized_linear_coefficient"]
    require(rhs.lo > 0, "Could not certify positive right determinant")
    require(rhs.hi < lhs.lo, "Determinant refutation not certified")
    require(linear.hi < 0, "Negative auxiliary linear coefficient not certified")
    for name, interval in values.items():
        lower, upper = map(F, CLAIMED_BOUNDS[name])
        require(lower < interval.lo <= interval.hi < upper,
                "Displayed enclosure not certified: " + name)

    # These are deliberately simple, independently readable exact bounds.
    require(rhs.hi < F(1007, 1000) < F(101, 100) < lhs.lo,
            "Simple separating rational bounds failed")
    require(lhs.lo - rhs.hi > F(3, 1000), "Gap lower bound failed")
    require(linear.hi < -F(8, 1000), "Linear-coefficient upper bound failed")

    HK = add(H, K)
    norms = {"H": infinity_norm(H), "H_plus_K": infinity_norm(HK)}
    for i in range(3):
        norms["minus_K_diagonal_" + str(i + 1)] = abs(F(K[i][i]))
    witness = {
        "H": [list(row) for row in H],
        "K": [list(row) for row in K],
        "dimension": 3,
        "normalizing_factor": f"exp(-2*trace(K)) = exp({-2 * trace(K)})",
        "taylor_degree": DEGREE,
        "tail_formula": "r^(degree+1)/(degree+1)!/(1-r/(degree+2))",
        "tail_data": {name: {"infinity_norm": str(r),
                              "absolute_entrywise_error_bound": str(tail_bound(r))}
                      for name, r in norms.items()},
        "normalized_enclosures_outward_rounded": {
            name: enclosing_rationals(x) for name, x in values.items()},
        "displayed_strict_bounds_exact_decimal_strings": CLAIMED_BOUNDS,
        "simple_exact_separation": "R < 1007/1000 < 101/100 < L",
        "normalized_L_minus_R_strict_lower_bound": "3/1000",
        "normalized_linear_coefficient_strict_upper_bound": "-1/125",
        "auxiliary_coefficient_status": "Not a separately sourced archival result",
    }
    return {
        "id": CASE_ID,
        "ok": True,
        "summary": "3x3 integer H,K; R < 1007/1000 < 101/100 < L; "
                   "L-R > 3/1000; auxiliary linear coefficient < -1/125",
        "witness": witness,
    }


if __name__ == "__main__":
    out = verify()
    art = pathlib.Path(__file__).resolve().parent / "artifacts"
    art.mkdir(exist_ok=True)
    (art / "certificate.json").write_text(
        json.dumps(out["witness"], indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )
    print(f"PASS {out['id']}: {out['summary']}")
