# AGENTS.md — the build tools

Scope: `tools/`. Read `/AGENTS.md` first. Most tasks do **not** belong here:
if a case is wrong, fix the case. Change the generator only when the schema or
the paper's structure genuinely changes.

## What each script owns

- **`build.py`** — validates every `counterexamples/*/case.json` and writes
  four generated artifacts: `tex/generated/ledger.tex`,
  `tex/generated/dossiers.tex`, `registry.json`, and two spliced regions of
  `README.md` — the case table (`<!-- BEGIN/END CASE TABLE -->`) and the
  headline count badges (`<!-- BEGIN/END COUNT BADGES -->`). Everything else in
  `README.md`, the rest of the header block included, is hand-written and is
  preserved verbatim by `splice()`. `--check` writes nothing
  and exits 1 if any of them is stale; `--allow-todo` downgrades the
  `found_by` / provenance TODO errors to warnings (migration only — CI runs
  plain `--check`).
- **`verify_all.py`** — discovers cases by scanning `counterexamples/*/case.json`
  and deliberately does **not** trust the generated `registry.json`. Imports
  each `verify.py` by path, calls `verify()`, asserts `ok is True`, runs the
  Sage cross-checks when `sage` is on `PATH` and skips them loudly otherwise.
  Writes the gitignored `verification_report.json`.
- **`new_case.py`** — interactive scaffolder. It **imports** `CLASSES`,
  `CERTIFICATE_LEVELS`, `FIDELITIES`, `GROUPS`, `DATE_RE`, and `mint_uid` from
  `build.py` rather than duplicating them, so the scaffolder can never emit a
  value the validator rejects. Keep it that way. `--mint-uid` prints one uid.
- **`exactcert.py`** — shared `Fraction` matrix helpers (`inv2`, `inv3`,
  `det2`, `det3`, `madd`, `mmul2`, `mscale`, `assert_positive_definite_2/3`).
  Exact arithmetic only; nothing here may return a `float`.

## Invariants to preserve

1. **`build.py` is stdlib-only.** It runs before dependencies matter, and CI
   installs pins with `--no-deps`.
2. **Collect errors, then report together.** `validate()` appends to `errors`
   and `main()` fails once, so a contributor sees every problem in one run
   instead of peeling them off one at a time.
3. **Fail loud on anything unrecognized.** `tex_to_markdown` is deliberately
   narrow: an unhandled macro is reported and fails the build rather than
   leaking raw LaTeX into `README.md`. If you extend `TEX_SUBS` or `ACCENTS`,
   keep the leftover check.
4. **uid immutability is enforced against the committed `registry.json`**
   (`committed_uid_bindings()`). That is the whole mechanism: deleting or
   truncating `registry.json` and regenerating would silently permit rebinding
   a published uid. Never regenerate it from an empty file.
5. **Generated output must be a pure function of the inputs.** No timestamps,
   no randomness, no environment dependence — CI runs `git diff --exit-code`
   after re-verifying, and `--check` compares byte-for-byte. (`mint_uid` is
   random, but it runs only in `new_case.py`, never during a build.)
6. **Schema changes are migrations.** Adding a required field means every one
   of the nine case directories fails until updated. Update them in the same
   change, and check whether `_template/case.json`, `new_case.py`,
   `CONTRIBUTING.md`, `.github/PULL_REQUEST_TEMPLATE.md`, and
   `counterexamples/AGENTS.md` describe the field too.

## After changing anything here

```sh
.venv/bin/python tools/build.py --allow-todo   # regenerate
git diff                                       # expect only what you intended
make check                                     # error list unchanged except by design
make verify                                    # ALL n CASES PASS
make paper
```

A generator change that alters `tex/generated/` or `registry.json` for cases
you did not touch is a red flag: read that diff line by line before committing.
