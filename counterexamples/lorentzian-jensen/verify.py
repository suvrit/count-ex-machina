"""Exact certificate for the Lorentzian Jensen triangle violation.

The code uses only fractions.Fraction and integer square roots.  Logarithms are
bounded through

    log(x) = 2 * sum_{k>=0} z^(2k+1)/(2k+1),  z=(x-1)/(x+1),

with an explicit geometric-series remainder.  Thus the final positive lower
bound is obtained with exact rational arithmetic.
"""

from fractions import Fraction
from math import isqrt


def G(point: tuple[Fraction, Fraction]) -> Fraction:
    x, y = point
    return (
        y**3
        + Fraction(11, 5) * x * y**2
        + Fraction(3, 2) * x**2 * y
        + Fraction(1, 10) * x**3
    )


def midpoint(a: tuple[Fraction, Fraction], b: tuple[Fraction, Fraction]):
    return tuple((a[i] + b[i]) / 2 for i in range(2))


def ratio(a, b) -> Fraction:
    """Return G((a+b)/2)^2/(G(a)G(b))."""
    return G(midpoint(a, b)) ** 2 / (G(a) * G(b))


def log_interval(x: Fraction, n_terms: int = 100):
    """Exact rational lower/upper bounds for log(x).

    For x>1, z=(x-1)/(x+1) lies in (0,1), and

      log(x) = 2 sum_{k=0}^{N-1} z^(2k+1)/(2k+1) + R_N,
      0 < R_N < 2 z^(2N+1)/((2N+1)(1-z^2)).
    """
    if x <= 0:
        raise ValueError("x must be positive")
    if x == 1:
        return Fraction(0), Fraction(0)
    if x < 1:
        lower, upper = log_interval(1 / x, n_terms)
        return -upper, -lower

    z = (x - 1) / (x + 1)
    z2 = z * z
    power = z
    partial = Fraction(0)
    for k in range(n_terms):
        partial += 2 * power / Fraction(2 * k + 1)
        power *= z2

    remainder_upper = 2 * power / (Fraction(2 * n_terms + 1) * (1 - z2))
    return partial, partial + remainder_upper


def sqrt_decimal_interval(x: Fraction, digits: int = 45):
    """Exact decimal-grid enclosure of sqrt(x).

    Returns consecutive multiples of 10^(-digits) enclosing sqrt(x).
    """
    if x < 0:
        raise ValueError("x must be nonnegative")
    scale = 10**digits
    floor_argument = (x.numerator * scale * scale) // x.denominator
    lower_integer = isqrt(floor_argument)
    return Fraction(lower_integer, scale), Fraction(lower_integer + 1, scale)


def decimal_floor(q: Fraction, digits: int = 50) -> str:
    """Print the decimal truncation of a rational number."""
    sign = "-" if q < 0 else ""
    q = abs(q)
    scaled = q.numerator * 10**digits // q.denominator
    text = str(scaled).rjust(digits + 1, "0")
    return sign + text[:-digits] + "." + text[-digits:]


def verify() -> dict:
    """Standard entry point for tools/verify_all.py."""
    p = (Fraction(35), Fraction(2))
    q = (Fraction(11, 2), Fraction(23, 2))
    r = (Fraction(1, 500), Fraction(15))

    R_pq = ratio(p, q)
    R_qr = ratio(q, r)
    R_pr = ratio(p, r)

    L_pq, U_pq = log_interval(R_pq)
    L_qr, U_qr = log_interval(R_qr)
    L_pr, U_pr = log_interval(R_pr)

    J_pq = (L_pq / 2, U_pq / 2)
    J_qr = (L_qr / 2, U_qr / 2)
    J_pr = (L_pr / 2, U_pr / 2)

    # For a rigorous lower bound on sqrt(J_pr)-sqrt(J_pq)-sqrt(J_qr),
    # use a lower bound for the first square root and upper bounds for the other two.
    sqrt_pr_lower, _ = sqrt_decimal_interval(J_pr[0])
    _, sqrt_pq_upper = sqrt_decimal_interval(J_pq[1])
    _, sqrt_qr_upper = sqrt_decimal_interval(J_qr[1])

    violation_lower = sqrt_pr_lower - sqrt_pq_upper - sqrt_qr_upper

    assert violation_lower > 0
    return {
        "id": "lorentzian-jensen",
        "ok": True,
        "summary": (
            "exact rational triangle-violation lower bound = "
            + decimal_floor(violation_lower)
        ),
        "witness": {
            "p": [str(x) for x in p],
            "q": [str(x) for x in q],
            "r": [str(x) for x in r],
            "G_values": [str(G(p)), str(G(q)), str(G(r))],
            "R_pq": str(R_pq),
            "R_qr": str(R_qr),
            "R_pr": str(R_pr),
            "J_pq_lower": decimal_floor(J_pq[0]),
            "J_qr_lower": decimal_floor(J_qr[0]),
            "J_pr_lower": decimal_floor(J_pr[0]),
            "violation_lower_exact": str(violation_lower),
            "violation_lower_decimal": decimal_floor(violation_lower),
        },
    }


if __name__ == "__main__":
    import json
    import pathlib

    out = verify()
    w = out["witness"]
    print("G(p), G(q), G(r):", ", ".join(w["G_values"]))
    print("R_pq =", w["R_pq"])
    print("R_qr =", w["R_qr"])
    print("R_pr =", w["R_pr"])
    print("J(p,q) approximately", w["J_pq_lower"])
    print("J(q,r) approximately", w["J_qr_lower"])
    print("J(p,r) approximately", w["J_pr_lower"])
    print("exact rational lower bound for triangle violation =", w["violation_lower_exact"])
    print("decimal lower bound =", w["violation_lower_decimal"])
    art = pathlib.Path(__file__).resolve().parent / "artifacts"
    art.mkdir(exist_ok=True)
    (art / "certificate.json").write_text(
        json.dumps(w, indent=2, sort_keys=True) + "\n"
    )
    print(f"PASS {out['id']}: {out['summary']}")
