#!/usr/bin/env python3
"""TODO: one-line description of what this script certifies.

Admission standard (see CONTRIBUTING.md): exact arithmetic (fractions,
integers, algebraic identities) or a rigorous interval certificate.
Floating-point-only evidence is inadmissible.
"""
from __future__ import annotations
import json
import pathlib

# Shared exact-arithmetic helpers (Fraction matrix ops), if needed:
# import sys
# sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2]))
# from tools.exactcert import inv2, inv3, madd, det2, det3, ...


def verify() -> dict:
    """Raise AssertionError if any check fails; return a machine-readable summary."""
    # TODO exact checks here
    return {
        "id": "TODO-must-match-case.json-id",
        "ok": True,
        "summary": "TODO one-line summary, include key exact values",
        "witness": {
            # TODO the exact data worth certifying (stringify Fractions)
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
