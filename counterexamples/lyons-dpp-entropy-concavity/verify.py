#!/usr/bin/env python3
"""Certify a commuting five-dimensional counterexample to DPP entropy concavity.

All calculations that establish the refutation use integers, Fraction, or
the exact field Q(sqrt(5)). Logarithms have rigorous rational enclosures.
There are no third-party dependencies.

The unitary is U[a,b] = exp(2*pi*i*a*b/5)/sqrt(5), with indices 0,...,4.
For K(t) = U diag(SPECTRUM + t*DIRECTION) U*, its exact occupation law is

  p_S(t) = sum_{|J|=|S|} |det U[S,J]|^2
             product_{j in J} lambda_j(t)
             product_{j not in J} (1-lambda_j(t)).

This is the spectral DPP sampling identity, obtained by Cauchy--Binet.
The squared Fourier minors are computed exactly below. Thus no approximate
matrix entries or approximate determinants enter this certificate.
"""

from dataclasses import dataclass
from fractions import Fraction as F
from math import isqrt
import json
import pathlib


# Explicit witness inputs. These are deliberately exposed for mutation tests.
SPECTRUM = (F(1, 1000), F(1, 1000), F(999, 1000),
            F(999, 1000), F(999, 1000))
DIRECTION = (F(1), F(-1), F(1), F(0), F(-1))
STEP = F(1, 10000)
CASE_ID = "lyons-dpp-entropy-concavity"

DIMENSION = 5
STATES = tuple(tuple(i for i in range(DIMENSION) if mask & (1 << i))
               for mask in range(1 << DIMENSION))
ROUND_DENOMINATOR = 10 ** 32
ROOT_DENOMINATOR = 10 ** 40
LOG_TERMS = 40


@dataclass(frozen=True)
class Quadratic:
    """The exact algebraic number a + b*sqrt(5)."""

    a: F = F(0)
    b: F = F(0)

    def __add__(self, other: "Quadratic") -> "Quadratic":
        return Quadratic(self.a + other.a, self.b + other.b)

    def scale(self, scalar: F) -> "Quadratic":
        return Quadratic(self.a * scalar, self.b * scalar)

    def is_zero(self) -> bool:
        return self.a == 0 and self.b == 0

    def as_strings(self) -> list[str]:
        return [str(self.a), str(self.b)]


Interval = tuple[F, F]


def enclose(lower: F, upper: F) -> Interval:
    """Round outward to a fixed rational grid, never inward."""
    assert lower <= upper
    denominator = ROUND_DENOMINATOR
    lower_integer = (lower.numerator * denominator) // lower.denominator
    upper_integer = -((-upper.numerator * denominator) // upper.denominator)
    return F(lower_integer, denominator), F(upper_integer, denominator)


def interval_add(x: Interval, y: Interval) -> Interval:
    return enclose(x[0] + y[0], x[1] + y[1])


def interval_negate(x: Interval) -> Interval:
    return -x[1], -x[0]


def interval_multiply(x: Interval, y: Interval) -> Interval:
    products = tuple(a * b for a in x for b in y)
    return enclose(min(products), max(products))


def quadratic_interval(x: Quadratic, root_interval: Interval) -> Interval:
    lo, hi = root_interval
    if x.b < 0:
        lo, hi = hi, lo
    return enclose(x.a + x.b * lo, x.a + x.b * hi)


def unit_log(x: F) -> Interval:
    """Enclose log(x) for 1 <= x <= 2 using an explicit positive tail.

    Put z=(x-1)/(x+1), so 0 <= z <= 1/3. The identity

      log(x) = 2 sum_{k>=0} z^(2k+1)/(2k+1)

    follows by integrating the geometric series for 2/(1-z*z).
    After LOG_TERMS terms the omitted positive tail is at most

      2*z^(2*LOG_TERMS+1) / ((2*LOG_TERMS+1)*(1-z*z)),

    because every omitted denominator is at least 2*LOG_TERMS+1.
    Both the partial sum and this bound are exact rational numbers.
    """
    assert F(1) <= x <= F(2)
    z = (x - 1) / (x + 1)
    total = F(0)
    power = z
    for k in range(LOG_TERMS):
        total += power / (2 * k + 1)
        power *= z * z
    tail = 2 * power / ((2 * LOG_TERMS + 1) * (1 - z * z))
    return enclose(2 * total, 2 * total + tail)


def rational_log(x: F, log_two: Interval) -> Interval:
    """Enclose log(x) by exact power-of-two range reduction."""
    assert x > 0
    y, exponent = x, 0
    while y < 1:
        y *= 2
        exponent -= 1
    while y > 2:
        y /= 2
        exponent += 1
    shift = interval_multiply((F(exponent), F(exponent)), log_two)
    return interval_add(unit_log(y), shift)


def interval_log(x: Interval, log_two: Interval) -> Interval:
    assert x[0] > 0
    # The logarithm is increasing, so endpoint enclosures suffice.
    lower = rational_log(x[0], log_two)[0]
    upper = rational_log(x[1], log_two)[1]
    return enclose(lower, upper)


def fourier_channel(observed: tuple[int, ...],
                    spectral: tuple[int, ...]) -> Quadratic:
    """Compute |det U[observed,spectral]|^2 exactly in Q(sqrt(5)).

    Empty and full minors have squared modulus 1; single-entry minors have
    squared modulus 1/5. Complementary-minor identities for a unitary give
    the sizes four and three from sizes one and two. For two-element sets,
    with d equal to the product of their index differences modulo five,

      |det U[S,J]|^2 = (2 - 2*cos(2*pi*d/5))/25
                    = (5 - sqrt(5))/50, if d = 1 or 4,
                    = (5 + sqrt(5))/50, if d = 2 or 3.
    """
    size = len(observed)
    if size != len(spectral):
        return Quadratic()
    if size in (0, 5):
        return Quadratic(F(1))
    if size in (1, 4):
        return Quadratic(F(1, 5))
    if size == 3:
        observed = tuple(i for i in range(5) if i not in observed)
        spectral = tuple(i for i in range(5) if i not in spectral)
    difference = ((observed[1] - observed[0])
                  * (spectral[1] - spectral[0])) % 5
    assert difference in (1, 2, 3, 4)
    sign = -1 if difference in (1, 4) else 1
    return Quadratic(F(1, 10), F(sign, 50))


def polynomial_multiply(p: list[F], q: list[F]) -> list[F]:
    result = [F(0)] * (len(p) + len(q) - 1)
    for i, a in enumerate(p):
        for j, b in enumerate(q):
            result[i + j] += a * b
    return result


def probability_polynomials() -> list[list[Quadratic]]:
    spectral_weights = []
    for spectral in STATES:
        weight = [F(1)]
        for i, (eigenvalue, velocity) in enumerate(zip(SPECTRUM, DIRECTION)):
            factor = ([eigenvalue, velocity] if i in spectral
                      else [1 - eigenvalue, -velocity])
            weight = polynomial_multiply(weight, factor)
        spectral_weights.append(weight)

    channel = [[fourier_channel(s, j) for j in STATES] for s in STATES]
    # Independently check exact normalization of the Fourier channel.
    for row in channel:
        assert sum(row, Quadratic()) == Quadratic(F(1))
    for column in zip(*channel):
        assert sum(column, Quadratic()) == Quadratic(F(1))

    result = []
    for row in channel:
        coefficients = [Quadratic() for _ in range(DIMENSION + 1)]
        for transition, weight in zip(row, spectral_weights):
            for degree, coefficient in enumerate(weight):
                coefficients[degree] = (coefficients[degree]
                                        + transition.scale(coefficient))
        result.append(coefficients)
    return result


def evaluate(polynomial: list[Quadratic], t: F) -> Quadratic:
    result = Quadratic()
    for coefficient in reversed(polynomial):
        result = result.scale(t) + coefficient
    return result


def entropy(polynomials: list[list[Quadratic]], t: F,
            root_interval: Interval, log_two: Interval) -> Interval:
    result = (F(0), F(0))
    for polynomial in polynomials:
        probability = quadratic_interval(evaluate(polynomial, t), root_interval)
        assert 0 < probability[0] <= probability[1] < 1
        term = interval_multiply(probability, interval_log(probability, log_two))
        result = interval_add(result, interval_negate(term))
    return result


def interval_strings(interval: Interval) -> dict[str, str]:
    return {"lower": str(interval[0]), "upper": str(interval[1])}


def verify() -> dict:
    """Raise AssertionError on failure; return an exact machine-readable witness."""
    assert len(SPECTRUM) == len(DIRECTION) == DIMENSION
    assert STEP > 0
    spectra = tuple(tuple(a + t * b for a, b in zip(SPECTRUM, DIRECTION))
                    for t in (-STEP, F(0), STEP))
    assert all(0 < eigenvalue < 1 for spectrum in spectra for eigenvalue in spectrum)
    assert all((spectra[0][i] + spectra[2][i]) / 2 == spectra[1][i]
               for i in range(DIMENSION))
    # The three kernels have these spectra in the SAME Fourier basis;
    # hence they are Hermitian, strictly between zero and I, and commute.

    root_integer = isqrt(5 * ROOT_DENOMINATOR * ROOT_DENOMINATOR)
    root_interval = (F(root_integer, ROOT_DENOMINATOR),
                     F(root_integer + 1, ROOT_DENOMINATOR))
    assert root_interval[0] ** 2 < 5 < root_interval[1] ** 2
    log_two = unit_log(F(2))
    polynomials = probability_polynomials()

    # Check total mass as a polynomial, and evenness coefficient by coefficient.
    for degree in range(DIMENSION + 1):
        total = sum((p[degree] for p in polynomials), Quadratic())
        assert total == Quadratic(F(1 if degree == 0 else 0))
    assert all(p[degree].is_zero() for p in polynomials for degree in (1, 3, 5))
    assert all(evaluate(p, STEP) == evaluate(p, -STEP) for p in polynomials)

    h_minus = entropy(polynomials, -STEP, root_interval, log_two)
    h_midpoint = entropy(polynomials, F(0), root_interval, log_two)
    h_plus = entropy(polynomials, STEP, root_interval, log_two)
    assert h_minus == h_plus
    gap = interval_add(h_plus, interval_negate(h_midpoint))
    # This strictly positive exact bound refutes midpoint concavity itself.
    assert gap[0] > F(1, 5000000000)

    # Independent local certificate: p'_S(0)=0, so H''=-sum p''_S log(p_S).
    curvature = (F(0), F(0))
    orbit_classes: dict[tuple[F, F, F, F], int] = {}
    for polynomial in polynomials:
        p_zero = quadratic_interval(polynomial[0], root_interval)
        p_second_exact = polynomial[2].scale(F(2))
        p_second = quadratic_interval(p_second_exact, root_interval)
        term = interval_multiply(p_second, interval_log(p_zero, log_two))
        curvature = interval_add(curvature, interval_negate(term))
        key = (polynomial[0].a, polynomial[0].b,
               p_second_exact.a, p_second_exact.b)
        orbit_classes[key] = orbit_classes.get(key, 0) + 1
    assert F(271, 5000) < curvature[0] <= curvature[1] < F(543, 10000)

    witness = {
        "dimension": DIMENSION,
        "unitary": "U[a,b]=exp(2*pi*i*a*b/5)/sqrt(5), indices a,b=0,...,4",
        "spectrum_at_midpoint": [str(x) for x in SPECTRUM],
        "direction": [str(x) for x in DIRECTION],
        "step": str(STEP),
        "spectrum_minus": [str(x) for x in spectra[0]],
        "spectrum_plus": [str(x) for x in spectra[2]],
        "strict_positive_contractions": True,
        "common_eigenbasis_and_commuting": True,
        "exact_probability_normalization": True,
        "exact_even_probability_polynomials": True,
        "entropy_minus_equals_entropy_plus": True,
        "entropy_midpoint_interval": interval_strings(h_midpoint),
        "entropy_endpoint_interval": interval_strings(h_plus),
        "endpoint_minus_midpoint_interval": interval_strings(gap),
        "strict_gap_lower_bound": "1/5000000000",
        "curvature_interval": interval_strings(curvature),
        "simpler_curvature_bounds": ["271/5000", "543/10000"],
        "sqrt_five_interval": interval_strings(root_interval),
        "log_series_terms": LOG_TERMS,
        "outward_rounding_denominator": str(ROUND_DENOMINATOR),
        "probability_orbit_classes": [
            {"multiplicity": count,
             "p_at_zero_as_a_plus_b_sqrt_five": [str(key[0]), str(key[1])],
             "p_second_as_a_plus_b_sqrt_five": [str(key[2]), str(key[3])]}
            for key, count in orbit_classes.items()
        ],
    }
    return {
        "id": CASE_ID,
        "ok": True,
        "summary": ("Commuting strict positive contractions of dimension 5 have "
                    "endpoint entropy minus midpoint entropy > 1/5000000000; "
                    "all bounds are exact rational enclosures."),
        "witness": witness,
    }


if __name__ == "__main__":
    out = verify()
    artifacts = pathlib.Path(__file__).resolve().parent / "artifacts"
    artifacts.mkdir(exist_ok=True)
    (artifacts / "certificate.json").write_text(
        json.dumps(out["witness"], indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )
    print(f"PASS {out['id']}: {out['summary']}")
