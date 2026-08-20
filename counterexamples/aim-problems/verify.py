#!/usr/bin/env python3
"""Exact certificates for the four Borcea--Branden AIM problems refuted here.

Two independent computations, one per pair of problems, each kept in its own
module because they share nothing -- not the witness, not the method, not the
dependencies:

  verify_pot.py     Problems 35 and 38: the stable degree-five product and its
                    exact Schur expansion (stdlib only)
  verify_pencil.py  Problems 36 and 37: the Specht-module det-pencil and its
                    Schur-positive t=4 member (sympy)

verify() runs both and fails if either does.  The __main__ block writes each
module's certificate to artifacts/, under the names case.json lists.
"""
from __future__ import annotations

import json
import pathlib
import sys

# tools/verify_all.py imports this file by path, so the two modules next to it
# are not importable until their directory is on sys.path.
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
import verify_pencil  # noqa: E402
import verify_pot  # noqa: E402


def verify() -> dict:
    pot = verify_pot.verify()
    pencil = verify_pencil.verify()
    assert pot["ok"] is True
    assert pencil["ok"] is True
    return {
        "id": "aim-problems",
        "ok": True,
        "summary": f"Problems 35 and 38: {pot['summary']}; Problems 36 and 37: {pencil['summary']}",
        "witness": {
            "problems-35-38": pot["witness"],
            "problems-36-37": pencil["witness"],
        },
    }


if __name__ == "__main__":
    out = verify()
    art = pathlib.Path(__file__).resolve().parent / "artifacts"
    art.mkdir(exist_ok=True)
    # Each file is written exactly as its module wrote it before the two cases
    # were merged, so the committed certificates recompute byte-for-byte.
    (art / "certificate-35-38.json").write_text(
        json.dumps(out["witness"]["problems-35-38"], indent=2, sort_keys=True) + "\n"
    )
    (art / "certificate-36-37.json").write_text(
        json.dumps(out["witness"]["problems-36-37"], indent=2) + "\n", encoding="utf-8"
    )
    print(f"PASS {out['id']}: {out['summary']}")
