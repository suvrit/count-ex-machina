#!/usr/bin/env python3
"""High-precision audit of the theta-derivative log-concavity counterexample.

Reconstructs J_9(1/50) at 100 digits with mpmath.  The companion Sage script
verify_theta.sage provides the outward-rounded interval certificate with a
rigorous tail bound.
"""
from __future__ import annotations
import json
import pathlib
import mpmath as mp


def theta_polynomials(K=10):
    # coefficient list low to high
    P = [[-3, 2]]
    for _ in range(K):
        cur = P[-1]
        deriv = [i * cur[i] for i in range(1, len(cur))]
        nxt = [0] * (len(cur) + 1)
        # 4u P'
        for i, c in enumerate(deriv):
            nxt[i + 1] += 4 * c
        # 5P - 4uP
        for i, c in enumerate(cur):
            nxt[i] += 5 * c
            nxt[i + 1] -= 4 * c
        while nxt and nxt[-1] == 0:
            nxt.pop()
        P.append(nxt)
    return P


def peval(coeff, x):
    y = mp.mpf(0)
    for c in reversed(coeff):
        y = y * x + c
    return y


def verify() -> dict:
    mp.mp.dps = 100
    P = theta_polynomials(10)
    t = mp.mpf(1) / 50
    alpha = mp.pi * mp.e ** (4 * t)
    vals = {}
    for k in [8, 9, 10]:
        total = mp.mpf(0)
        # m>=20 is astronomically negligible; see Sage certificate for rigorous tail.
        for m in range(1, 20):
            u = alpha * m * m
            total += mp.pi * m * m * mp.e ** (5 * t - u) * peval(P[k], u)
        vals[k] = total
    J = vals[9] ** 2 - vals[8] * vals[10]
    assert J < mp.mpf("-2.6e19")
    return {
        "id": "theta-derivative-log-concavity",
        "ok": True,
        "summary": "100-digit J9(1/50) = " + mp.nstr(J, 80),
        "witness": {
            "t": "1/50",
            "J9": mp.nstr(J, 80),
            "Phi8": mp.nstr(vals[8], 60),
            "Phi9": mp.nstr(vals[9], 60),
            "Phi10": mp.nstr(vals[10], 60),
            "threshold": "-2.6e19",
            "rigorous_certificate": "verify_theta.sage (outward-rounded intervals, tail bound)",
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
