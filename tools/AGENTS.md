# AGENTS.md — the build tools

Scope: `tools/`. Read `/AGENTS.md` first. Most tasks do **not** belong here:
if a case is wrong, fix the case. Change the generator only when the schema or
the paper's structure genuinely changes.

## What each script owns

- **`build.py`** — validates every case (`case.json` + `case.tex`) and writes
  four generated artifacts: `tex/generated/metadata.tex` (per result, its
  `\cxtheorem` label and `\cxverbatim` / `\cxparaphrase` / `\cxpending`
  flag — declared once, loaded by `main.tex`'s preamble) and
  `tex/generated/appendix-brief.tex` (bare `\cxbriefitem` lines for cases
  marked `"brief": true`, written even when empty so the `\input` never
  dangles, and carrying **no heading, list environment, or word of prose**:
  those belong to the hand-written `tex/09-additional.tex`). Then
  `registry.json`, and two spliced regions of
  `README.md` — the case table (`<!-- BEGIN/END CASE TABLE -->`) and the
  headline count badges (`<!-- BEGIN/END COUNT BADGES -->`). Everything else in
  `README.md`, the rest of the header block included, is hand-written and is
  preserved verbatim by `splice()`. `--check` writes nothing
  and exits 1 if any of them is stale; `--allow-todo` downgrades the
  `found_by` / provenance TODO errors to warnings (migration only — CI runs
  plain `--check`).

  It also **checks, but never writes, the two case lists**: `tex/cases.tex`
  (the body's section headings, `\cxlevel`s and `\input` lines) and the
  dossier `\input`s in `tex/09-additional.tex`. `check_case_inputs()` requires
  the set of cases `\input` in each to equal what the `appendix` / `brief`
  flags put there — nothing missing, nothing twice, nothing in the wrong file,
  no withheld or brief case — and prints the `\input` line to paste for a
  missing one. Headings, order and levels are the maintainer's. Until August
  2026 both lists were generated, and the one shared section heading came from
  the `GROUPS` table here, which now serves only the README's collapsed rows.

  It also **checks, but never writes, `tex/ledger.tex`**: that table is
  hand-written, and `check_ledger()` only confirms that every refuted result's
  `theorem_label` appears in a `\ref` there and that no row names a result that
  does not exist, printing a paste-ready row for anything missing. A `"brief"`
  result inverts that check: it must have *no* row, and a leftover one is an
  error rather than a silent duplicate of its appendix bullet. It runs
  unconditionally rather than only when the rest of validation passes —
  otherwise it would be dead code for as long as the baseline carries errors,
  which is exactly when a missing row would slip through.
- **`verify_all.py`** — discovers cases by scanning `counterexamples/*/case.json`
  and deliberately does **not** trust the generated `registry.json`. Imports
  each `verify.py` by path, calls `verify()`, asserts `ok is True`, runs the
  Sage cross-checks when `sage` is on `PATH` and skips them loudly otherwise.
  Writes the gitignored `verification_report.json`.
- **`new_case.py`** — interactive scaffolder. It **imports** `CLASSES`,
  `CERTIFICATE_LEVELS`, `FIDELITIES`, `GROUPS`, `DATE_RE`, and `mint_uid` from
  `build.py` rather than duplicating them, so the scaffolder can never emit a
  value the validator rejects. Keep it that way. `--mint-uid` prints one uid.
- **`unpack_submission.py`** — turns a `SUBMIT.md` bundle (one markdown file of
  `file=`-tagged fences, produced by a contributor's agent) back into
  `counterexamples/<id>/`. It assigns the two fields a submitter must never
  choose off-repository — the `uid` and the ledger `order` — and refuses an
  existing directory, an unknown block tag, or a missing required block. It
  validates no mathematics; `make check` does that.
- **`exactcert.py`** — shared `Fraction` matrix helpers (`inv2`, `inv3`,
  `det2`, `det3`, `madd`, `mmul2`, `mscale`, `assert_positive_definite_2/3`).
  Exact arithmetic only; nothing here may return a `float`.

## Invariants to preserve

0. **No LaTeX in `case.json`.** Every word an author writes in LaTeX lives in
   `case.tex`, delimited by the `cx...` environments `parse_case_tex()` reads;
   the JSON carries ids, uid, enums, dates, urls. `load_prose()` rejects a
   case.json that still holds prose, by name. A new field that would carry
   LaTeX is a new region, not a new key.
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
   a published uid. Never regenerate it from an empty file. The one sanctioned
   way past the reuse check is a result declaring the old id in `former_ids` —
   a rename, where the uid is supposed to follow the statement. Keep that an
   explicit claim in `case.json`; never infer it from the diff.
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
make regen                                     # regenerate
git diff                                       # expect only what you intended
make check                                     # must pass
make verify                                    # ALL n CASES PASS
make paper
```

A generator change that alters `tex/generated/` or `registry.json` for cases
you did not touch is a red flag: read that diff line by line before committing.
