# count-ex-machina

Companion repository for the paper **“GPT: The Counterexample Machine”**
(Suvrit Sra, TU Munich). It archives AI-assisted counterexamples to published
conjectures and to formal problems posed by the author, together with
independently checkable certificates: every admitted case is verified by exact
arithmetic or by a rigorous interval computation — never by floating-point
evidence alone.

## Layout

- `counterexamples/<id>/` — one directory per counterexample: `case.json`
  (metadata + attribution), `README.md` (how to validate), `dossier.tex`
  (the paper dossier body), `verify.py` (certificate check), optional Sage
  cross-checks, and `artifacts/` (machine-readable certificates).
- `tex/` — the main paper. `tex/generated/` and `registry.json` are generated
  from the per-case `case.json` files by `tools/build.py` (checked in; do not
  edit by hand).
- `tools/` — `build.py` (validate + regenerate), `verify_all.py` (run every
  case), `exactcert.py` (shared exact-arithmetic helpers).

## Quickstart

```sh
python3 -m venv .venv && .venv/bin/pip install -r requirements.txt
.venv/bin/python tools/verify_all.py     # verify every counterexample
cd tex && latexmk -pdf main              # build the paper (compile from tex/)
```

Individual cases run standalone: `cd counterexamples/<id> && python verify.py`.
Sage cross-checks (where present) are optional and are skipped when `sage` is
not installed. Note for Overleaf: import the whole repository and set the main
document to `tex/main.tex`.

## The cases

<!-- BEGIN CASE TABLE -->
| No. | Case | Status | Class | Certificate | Found by |
|---|---|---|---|---|---|
| 1 | [aim-problem-35](counterexamples/stable-schur/) | refuted | external formal problem | exact | TODO (TODO) |
| 2 | [aim-problem-38](counterexamples/stable-schur/) | refuted | external formal problem | exact | TODO (TODO) |
| 3 | [aim-problem-36](counterexamples/aim-problem-36/) | refuted | external formal problem | exact | TODO (TODO) |
| 4 | [aim-problem-37](counterexamples/aim-problem-36/) | refuted | external formal problem | exact | TODO (TODO) |
| 5 | [subgroup-johnson](counterexamples/subgroup-johnson/) | refuted | user formal problem | exact | TODO (TODO) |
| 6 | [macdonald-schur-convexity](counterexamples/macdonald-schur-convexity/) | refuted | published theorem | exact | TODO (TODO) |
| 7 | [theta-derivative-log-concavity](counterexamples/theta-derivative-log-concavity/) | refuted | external conjecture | computer-assisted | TODO (TODO) |
| 8 | [dpp-feasible-step](counterexamples/dpp-feasible-step/) | refuted | published conjecture | exact | TODO (TODO) |
| 9 | [variance-only-matrix-discrepancy](counterexamples/variance-only-matrix-discrepancy/) | refuted | user formal problem | exact | TODO (TODO) |
| 10 | [rank-two-mixed-norm](counterexamples/rank-two-mixed-norm/) | refuted | user formal problem | computer-assisted | TODO (TODO) |
| 11 | [logdet-loewner](counterexamples/logdet-loewner/) | refuted | user formal problem | exact | TODO (TODO) |
| — | [lorentzian-jensen](counterexamples/lorentzian-jensen/) | withheld | user formal problem | exact | TODO (TODO) |
<!-- END CASE TABLE -->

Withheld cases are documented but excluded from the paper's admitted ledger;
see `audit_notes.md` and each case's README for the reason.

## Adding a counterexample

The admission bar (exact or rigorous-interval certificates only; no
quantifier drift; see `tex/02-admission.tex` and
[CONTRIBUTING.md](CONTRIBUTING.md)) applies to every new case. The mechanical
discipline is:

1. **Create the case dir** (kebab-case id; it becomes the directory, registry,
   and link name):

   ```sh
   cp -r counterexamples/_template counterexamples/<id>
   ```

2. **`case.json`** — the single source of truth; everything else is generated
   from it:
   - `id` must equal the directory name; `title` / `title_tex` become the
     case's own section heading in the paper;
   - `status`: `"refuted"` (goes into the ledger) or `"withheld"` (documented
     but excluded; needs `withheld_reason` and a standalone `paper.tex`
     instead of a dossier);
   - `order`: next free integer, unless the case joins a group (below);
   - `group` (optional): cases sharing a group key are emitted as
     subsections of one common section — currently only `"aim"`, the
     Borcea–Brändén AIM problems — and their `order` values must be
     consecutive, so adding one renumbers the cases after it;
   - one `results` entry per refuted statement (usually one; `stable-schur`
     has two): `statement_tex` and `certificate_tex` are the ledger columns,
     `class` and `certificate_level` the classification, `theorem_label` must
     match the `\label` in the dossier;
   - `provenance` (per result): the statement **as originally posed**, quoted
     ahead of the dossier in the paper — `statement_tex` (the quote),
     `source_tex` (who posed it and where, with `\cite{...}`), `url` and
     `retrieved` for the copy consulted, and `fidelity`: `"verbatim"` only if
     transcribed from the source's own text, otherwise `"paraphrase"`, which
     the paper labels as such;
   - `credits`: `posed_by` (use `\cite{...}` for external sources),
     `found_by` (AI model + session date `YYYY-MM`), `formalized_by`,
     `audited_by`, `contributed_by`;
   - `verify`: entry script, optional Sage cross-checks, extra pip deps.

3. **`.bib` entries** — add cited works to `tex/references.bib` and list the
   keys in `bib_keys` (the build fails on unknown keys).

4. **`dossier.tex`** — body only; do **not** write the `\section` /
   `\subsection` heading or the credit line (both are generated). Follow the house structure: prose stating the
   original conjecture with `\cite`, a `theorem` environment whose bracketed
   title carries `\statusfalse` and whose `\label` equals `theorem_label`, a
   proof with the explicit witness, optionally `\begin{remark}[Scope]`.

5. **`verify.py`** — implements `verify() -> dict` (raises `AssertionError` on
   failure; returns `id`/`ok`/`summary`/`witness`), exact arithmetic or
   rigorous intervals only; the `__main__` block writes
   `artifacts/certificate.json`. Shared Fraction matrix helpers live in
   `tools/exactcert.py`. Add Sage interval cross-checks for analytic cases.

6. **Case `README.md`** — statement summary, how to verify, what the
   artifacts contain.

7. **Regenerate, verify, build**:

   ```sh
   python tools/build.py        # validates case.json, regenerates ledger/dossiers/registry/this table
   python tools/verify_all.py   # must end with ALL ... CASES PASS
   cd tex && latexmk -pdf main
   ```

8. **Commit everything, including the regenerated files** (`tex/generated/`,
   `registry.json`, `README.md`, the case's `artifacts/`). Run
   `python tools/build.py --check` to confirm nothing is stale.

`tools/build.py` fails loudly on TODO placeholders, duplicate orders or
theorem labels, missing bib keys, and missing files — if it is silent about
the new case, the metadata is complete. Attribution from `case.json` is
rendered under the dossier heading in the paper and into `registry.json`
automatically.
