#!/usr/bin/env python3
"""Scaffold a new counterexample directory with every cross-reference wired.

The mechanical parts of a case -- the id echoed into four files, the ledger
`order`, the `theorem_label` that has to match the `\\label` in the dossier --
are exactly the parts contributors get wrong, and none of them require any
judgement.  This script fills those in and leaves TODO markers only where
actual mathematics has to be written.

    python tools/new_case.py             # prompts for everything
    python tools/new_case.py --id my-case

The scaffolded case deliberately does *not* pass `tools/build.py --check` yet:
what remains is the statement, the certificate description, and the prose, and
build.py will name each one until it is filled in.
"""
from __future__ import annotations

import argparse
import datetime
import json
import re
import shutil
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

# Imported rather than duplicated: the scaffolder must never be able to emit a
# value that build.py would reject.
from tools.build import (  # noqa: E402  (needs the sys.path insert above)
    CASES_DIR,
    CERTIFICATE_LEVELS,
    CLASSES,
    DATE_RE,
    FIDELITIES,
    GROUPS,
)

TEMPLATE = CASES_DIR / "_template"
ID_RE = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")


def ask(prompt: str, default: str | None = None, validate=None) -> str:
    """Prompt until the answer is non-empty and passes `validate`."""
    suffix = f" [{default}]" if default else ""
    while True:
        try:
            raw = input(f"{prompt}{suffix}: ").strip()
        except EOFError:
            sys.exit("\naborted: input ended before the case was complete")
        value = raw or (default or "")
        if not value:
            print("  (required)")
            continue
        if validate:
            problem = validate(value)
            if problem:
                print(f"  {problem}")
                continue
        return value


def choose(prompt: str, options: list[str]) -> str:
    """Numbered menu; contributors should not have to memorise the enums."""
    print(f"\n{prompt}")
    for i, opt in enumerate(options, 1):
        print(f"  {i}. {opt}")
    while True:
        raw = input(f"  choice [1-{len(options)}]: ").strip()
        if raw.isdigit() and 1 <= int(raw) <= len(options):
            return options[int(raw) - 1]
        print("  (pick a number from the list)")


def next_order() -> int:
    """One past the highest ledger order currently in use."""
    orders = []
    for path in CASES_DIR.glob("*/case.json"):
        if path.parent.name == "_template":
            continue
        order = json.loads(path.read_text()).get("order")
        if isinstance(order, int):
            orders.append(order)
    return max(orders, default=0) + 1


def check_id(value: str) -> str | None:
    if not ID_RE.match(value):
        return "kebab-case only: lowercase letters, digits, single hyphens"
    if (CASES_DIR / value).exists():
        return f"counterexamples/{value}/ already exists"
    return None


def check_month(value: str) -> str | None:
    return None if DATE_RE.match(value) else "must be YYYY-MM (or YYYY-MM-DD)"


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("--id", help="case id (kebab-case); prompted for if omitted")
    args = parser.parse_args()

    if not TEMPLATE.exists():
        sys.exit(f"error: template missing at {TEMPLATE}")

    print("Scaffolding a new counterexample. Press Ctrl-C to abort.\n")

    case_id = args.id or ask("case id (kebab-case)", validate=check_id)
    if problem := check_id(case_id):
        sys.exit(f"error: {problem}")

    title = ask("title (plain text, for the paper's section heading)")
    klass = choose("How is the refuted statement classified?", sorted(CLASSES))
    level = choose("Certificate level", sorted(CERTIFICATE_LEVELS))

    print("\nProvenance -- where the statement was posed.")
    posed_by = ask("posed by (LaTeX; use \\cite{...} for published sources)")
    source_tex = ask("source, with section or problem number (LaTeX)")
    url = ask("url of the copy you consulted")
    retrieved = ask("retrieved (YYYY-MM-DD)", default=str(datetime.date.today()))
    fidelity = choose(
        "Is the quoted statement transcribed from the source's own text?",
        sorted(FIDELITIES),
    )

    print("\nAttribution -- this archive exists to document exactly this.")
    model = ask("found by (AI model name)")
    found_date = ask("session date (YYYY-MM)", validate=check_month)
    formalized_by = ask("formalized by")
    audited_by = ask("audited by", default=formalized_by)
    contributed_by = ask("contributed by", default=formalized_by)

    bib_raw = ask("bib keys for tex/references.bib (comma-separated, or -)", default="-")
    bib_keys = [] if bib_raw == "-" else [k.strip() for k in bib_raw.split(",") if k.strip()]

    # Grouped cases require every member's `order` to stay contiguous, so adding
    # one renumbers the cases after it -- a change to files this contributor
    # does not own.  Refuse rather than silently rewrite them.
    if any(json.loads(p.read_text()).get("group") for p in CASES_DIR.glob("*/case.json")):
        print(
            f"\nNote: groups ({', '.join(sorted(GROUPS))}) need contiguous orders and"
            "\nrenumber existing cases. If this case belongs to a group, set 'group'"
            "\nand fix the orders by hand, or say so in your pull request."
        )

    order = next_order()
    label = f"thm:{case_id}"
    dest = CASES_DIR / case_id
    shutil.copytree(TEMPLATE, dest)

    case = json.loads((TEMPLATE / "case.json").read_text())
    case["id"] = case_id
    case["title"] = title
    case["title_tex"] = title
    case["status"] = "refuted"
    case["order"] = order
    case["bib_keys"] = bib_keys
    result = case["results"][0]
    result["id"] = case_id
    result["class"] = klass
    result["certificate_level"] = level
    result["theorem_label"] = label
    result["provenance"].update(
        {"source_tex": source_tex, "url": url, "retrieved": retrieved, "fidelity": fidelity}
    )
    case["credits"] = {
        "posed_by": posed_by,
        "found_by": {"model": model, "date": found_date},
        "formalized_by": formalized_by,
        "audited_by": audited_by,
        "contributed_by": contributed_by,
    }
    (dest / "case.json").write_text(json.dumps(case, indent=2, ensure_ascii=False) + "\n")

    # Wire the label the build cross-checks between case.json and the dossier.
    dossier = (dest / "dossier.tex").read_text().replace("thm:TODO", label)
    (dest / "dossier.tex").write_text(dossier)

    verify = (dest / "verify.py").read_text().replace("TODO-must-match-case.json-id", case_id)
    (dest / "verify.py").write_text(verify)

    readme = (dest / "README.md").read_text()
    readme = readme.replace("# TODO Title", f"# {title}", 1)
    readme = readme.replace(
        "**Status:** TODO refuted (ledger rows appear after `tools/build.py`) | withheld",
        "**Status:** refuted",
        1,
    )
    readme = readme.replace(
        "**Certificate level:** TODO exact | computer-assisted",
        f"**Certificate level:** {level}",
        1,
    )
    (dest / "README.md").write_text(readme)

    print(f"\nCreated counterexamples/{case_id}/ as ledger order {order}.\n")
    print("What is filled in: id, order, theorem label, classification, provenance,")
    print("credits. What is left: the mathematics.\n")
    print("  1. dossier.tex  -- the conjecture, the theorem, the proof")
    print(f"  2. verify.py    -- exact checks; `python counterexamples/{case_id}/verify.py`")
    print("  3. case.json    -- statement_tex, certificate_tex, context_tex, and the")
    print("                     provenance statement quoted as originally posed")
    print("  4. README.md    -- summary and artifact description\n")
    print("Then run `make check`. It will name every TODO that is still outstanding.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
