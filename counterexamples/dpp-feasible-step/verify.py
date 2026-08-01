#!/usr/bin/env python3
"""Exact audit of the DPP feasible-step Picard ascent counterexample.

All arithmetic is over exact rationals; the likelihood reversal reduces to a
positive difference of two rational numbers.
"""
from __future__ import annotations
from fractions import Fraction as F
import json
import pathlib
import sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2]))
from tools.exactcert import (
    assert_positive_definite_2,
    det2,
    inv2,
    madd,
    mmul2,
    mscale,
)


def verify() -> dict:
    L0 = [
        [F(337200647, 10**8), F(262325460, 10**8)],
        [F(262325460, 10**8), F(607953037, 10**8)],
    ]
    I = [[F(1), F(0)], [F(0), F(1)]]
    assert_positive_definite_2(L0)
    Linv = inv2(L0)
    ILinv = inv2(madd(I, L0))
    singleton = [[1 / L0[0][0], F(0)], [F(0), F(0)]]
    singleton2 = [[F(0), F(0)], [F(0), 1 / L0[1][1]]]
    Z = madd(madd(singleton, singleton2), Linv)
    Delta = madd(mscale(F(1, 3), Z), mscale(F(-1), ILinv))
    L1 = madd(L0, mscale(F(5), mmul2(mmul2(L0, Delta), L0)))
    assert_positive_definite_2(L1)
    prod0 = L0[0][0] * L0[1][1] * det2(L0)
    prod1 = L1[0][0] * L1[1][1] * det2(L1)
    left = prod1 / prod0
    right = (det2(madd(I, L1)) / det2(madd(I, L0))) ** 3
    assert right - left > 0
    return {
        "id": "dpp-feasible-step",
        "ok": True,
        "summary": f"exact rational likelihood reversal, gap={float(right - left):.16g}",
        "witness": {
            "L0": [[str(x) for x in row] for row in L0],
            "L1": [[str(x) for x in row] for row in L1],
            "step": "a=5",
            "left": str(left),
            "right": str(right),
            "gap": str(right - left),
            "gap_decimal": f"{float(right - left):.16g}",
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
