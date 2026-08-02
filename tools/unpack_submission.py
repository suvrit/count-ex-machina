#!/usr/bin/env python3
"""Unpack a SUBMIT.md bundle into counterexamples/<id>/.

A contributor's agent produces one markdown file of fenced blocks tagged
``file=<name>`` (the format is specified in SUBMIT.md).  This turns that file
back into a case directory, and assigns the two fields a submitter must never
choose for themselves: the immutable ``uid`` and the ledger ``order``, both of
which would collide with real values if invented off-repository.

    python tools/unpack_submission.py submissions/my-case.md
    python tools/unpack_submission.py my-case.md --id other-name

Nothing here validates the mathematics.  It writes files and then hands over to
`make check`, which is the gate that actually has opinions.

Stdlib only, like build.py.
"""
from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from tools.build import CASES_DIR, mint_uid  # noqa: E402
from tools.new_case import ID_RE, next_order  # noqa: E402

# An opening fence records its own length: a block whose content contains a
# shorter fence (a ```sh inside a README) must not be closed by it.
OPEN_RE = re.compile(r"^(`{3,})\s*[A-Za-z]*\s+file=(\S+)\s*$")
REQUIRED = {"case.json", "dossier.tex", "verify.py", "README.md"}
KNOWN = REQUIRED | {"statement.tex", "context.tex", "references.bib.add"}


def parse_blocks(text, errors):
    """Map file= tag -> block content, in the order the bundle presents them."""
    blocks = {}
    lines = text.splitlines()
    i = 0
    while i < len(lines):
        m = OPEN_RE.match(lines[i])
        if not m:
            i += 1
            continue
        ticks, name = m.group(1), m.group(2)
        close = re.compile(rf"^`{{{len(ticks)},}}\s*$")
        body, i = [], i + 1
        while i < len(lines) and not close.match(lines[i]):
            body.append(lines[i])
            i += 1
        if i >= len(lines):
            errors.append(f"block {name!r} is never closed by a matching fence")
        i += 1
        if name in blocks:
            errors.append(f"block {name!r} appears twice")
        blocks[name] = "\n".join(body).strip("\n") + "\n"
    return blocks


def main():
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("bundle", help="the submitted markdown file")
    ap.add_argument("--id", help="override the case id in case.json")
    args = ap.parse_args()

    errors = []
    text = Path(args.bundle).read_text()
    blocks = parse_blocks(text, errors)

    missing = REQUIRED - set(blocks)
    if missing:
        errors.append(f"bundle is missing required block(s): {sorted(missing)}")
    for name in sorted(set(blocks) - KNOWN):
        # A stray tag is far more likely to be a typo in a filename than a file
        # this archive wants, and writing it would create a case nobody reviewed.
        errors.append(f"unknown block {name!r}; expected one of {sorted(KNOWN)}")

    case = {}
    if "case.json" in blocks:
        try:
            case = json.loads(blocks["case.json"])
        except json.JSONDecodeError as e:
            errors.append(f"case.json is not valid JSON ({e})")

    case_id = args.id or case.get("id")
    if not case_id or not ID_RE.match(str(case_id)):
        errors.append(f"case id {case_id!r} must be kebab-case: lowercase, digits, single hyphens")
    elif (CASES_DIR / case_id).exists():
        errors.append(f"counterexamples/{case_id}/ already exists; unpack under a different --id")

    if errors:
        for e in errors:
            print("error:", e, file=sys.stderr)
        return 1

    # The submitter is told to leave these out; fill them from the repository's
    # own state rather than trusting whatever arrived.
    case["id"] = case_id
    case["order"] = next_order()
    for r in case.get("results") or []:
        r["uid"] = mint_uid()
        r.setdefault("id", case_id)

    dest = CASES_DIR / case_id
    (dest / "artifacts").mkdir(parents=True)
    (dest / "case.json").write_text(json.dumps(case, indent=2, ensure_ascii=False) + "\n")
    written = ["case.json"]
    for name, body in blocks.items():
        if name in ("case.json", "references.bib.add"):
            continue
        (dest / name).write_text(body)
        written.append(name)

    print(f"unpacked into counterexamples/{case_id}/ as ledger order {case['order']}")
    print("  files:", ", ".join(sorted(written)))
    print("  uid(s) minted:", ", ".join(r["uid"] for r in case.get("results") or []))

    if "references.bib.add" in blocks:
        # Not appended automatically: a duplicate or malformed entry in
        # references.bib breaks every case's bibliography, not just this one.
        (dest / "references.bib.add").write_text(blocks["references.bib.add"])
        print(f"\n  bib entries to review and paste into tex/references.bib:")
        print(f"    counterexamples/{case_id}/references.bib.add")
        print("    (delete that file once the entries are in)")

    print("\nNext: read the mathematics, then")
    print("  make check    # names every TODO and every metadata error")
    print("  make verify")
    print("  make paper")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
