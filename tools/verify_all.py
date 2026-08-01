#!/usr/bin/env python3
"""Run every counterexample's verify.py and aggregate the results.

Discovers cases by scanning counterexamples/*/case.json (the checked-in
registry.json is generated output and is deliberately not trusted here).
For each case the standard entry point verify() is called; Sage cross-checks
listed in case.json are run as subprocesses when sage is installed and are
skipped (loudly) otherwise.

Usage:
  python tools/verify_all.py             run everything
  python tools/verify_all.py --only ID   run a single case

Exit status is nonzero unless every case passes. Writes a regenerable
verification_report.json at the repository root (gitignored).
"""
from __future__ import annotations

import argparse
import importlib.util
import json
import shutil
import subprocess
import sys
import traceback
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CASES_DIR = ROOT / "counterexamples"
REPORT = ROOT / "verification_report.json"


def load_verify(case_dir: Path, entry: str):
    spec = importlib.util.spec_from_file_location(
        f"verify_{case_dir.name.replace('-', '_')}", case_dir / entry
    )
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module.verify


def run_case(case: dict, case_dir: Path, sage_path: str | None) -> dict:
    record = {"id": case["id"], "status": case["status"]}
    try:
        result = load_verify(case_dir, case["verify"]["python"])()
        assert result.get("ok") is True
        record["python"] = "pass"
        record["summary"] = result["summary"]
        print(f"PASS {case['id']}: {result['summary']}")
    except Exception:
        record["python"] = "fail"
        record["summary"] = traceback.format_exc().strip().splitlines()[-1]
        print(f"FAIL {case['id']}", file=sys.stderr)
        traceback.print_exc()
        return record

    sage_scripts = case["verify"].get("sage", [])
    if not sage_scripts:
        record["sage"] = None
    elif sage_path is None:
        record["sage"] = "skipped"
        for script in sage_scripts:
            print(f"SKIP {case['id']} sage cross-check {script} (sage not installed)")
    else:
        for script in sage_scripts:
            proc = subprocess.run([sage_path, script], cwd=case_dir, capture_output=True, text=True)
            if proc.returncode != 0:
                record["python"] = "fail"
                record["sage"] = f"fail: {script}"
                print(f"FAIL {case['id']} sage cross-check {script}", file=sys.stderr)
                print(proc.stdout + proc.stderr, file=sys.stderr)
                return record
            print(f"PASS {case['id']} sage cross-check {script}")
        record["sage"] = "pass"
    return record


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--only", metavar="ID", help="run a single case by id")
    args = parser.parse_args()

    cases = []
    for d in sorted(CASES_DIR.iterdir()):
        if not d.is_dir() or d.name.startswith("_"):
            continue
        case = json.loads((d / "case.json").read_text())
        if args.only and case["id"] != args.only:
            continue
        cases.append((case, d))
    if not cases:
        print("error: no cases found" + (f" matching {args.only!r}" if args.only else ""), file=sys.stderr)
        sys.exit(1)

    sage_path = shutil.which("sage")
    records = [run_case(case, d, sage_path) for case, d in cases]
    REPORT.write_text(json.dumps(records, indent=2) + "\n")

    failed = [r["id"] for r in records if r["python"] != "pass"]
    if failed:
        print(f"FAILED cases: {', '.join(failed)}", file=sys.stderr)
        sys.exit(1)
    print(f"ALL {len(records)} CASES PASS")


if __name__ == "__main__":
    main()
