<div align="center">

# count-ex-machina

**Counterexamples found by AI, certified by exact arithmetic.**

[![verify](https://github.com/suvrit/count-ex-machina/actions/workflows/verify.yml/badge.svg?branch=main)](https://github.com/suvrit/count-ex-machina/actions/workflows/verify.yml)
<!-- BEGIN COUNT BADGES -->
[![counterexamples](https://img.shields.io/badge/counterexamples-12%20refuted-0b7285)](#the-cases)
[![certificates](https://img.shields.io/badge/certificates-10%20exact%2C%202%20interval-0b7285)](#the-cases)
<!-- END COUNT BADGES -->
[![Python](https://img.shields.io/badge/Python-3.14-3776AB?logo=python&logoColor=white)](requirements.txt)
[![code: Apache 2.0](https://img.shields.io/badge/code-Apache%202.0-4c566a)](LICENSE)
[![docs: CC BY 4.0](https://img.shields.io/badge/docs-CC%20BY%204.0-4c566a)](LICENSE-DOCS)
[![contributions welcome](https://img.shields.io/badge/contributions-welcome-2f9e44)](CONTRIBUTING.md)

<sub>Every admitted case recomputes from source — exact arithmetic or rigorous
intervals, never floating point.</sub>

</div>

Companion repository for the paper **“GPT: The Counterexample Machine”**
(Suvrit Sra, TU Munich). It archives AI-assisted counterexamples to published
conjectures and to formal problems posed by the author, together with
independently checkable certificates: every admitted case is verified by exact
arithmetic or by a rigorous interval computation — never by floating-point
evidence alone.

## Layout

- `counterexamples/<id>/` — one directory per counterexample: `case.json`
  (metadata + attribution), `context.tex` (notation the quoted statement
  needs), `statement.tex` (the statement as originally posed), `README.md`
  (how to validate), `dossier.tex` (the paper dossier body), `verify.py`
  (certificate check), optional Sage cross-checks, and `artifacts/`
  (machine-readable certificates). Prose is always a `.tex` file that
  `case.json` names; it is never embedded in the JSON.
- `tex/` — the main paper. `tex/generated/` and `registry.json` are generated
  from the per-case `case.json` files by `tools/build.py` (checked in; do not
  edit by hand).
- `tools/` — `build.py` (validate + regenerate), `verify_all.py` (run every
  case), `exactcert.py` (shared exact-arithmetic helpers).
- `AGENTS.md` — orientation for AI coding agents, with shorter briefs in
  `counterexamples/`, `tex/`, and `tools/`. Human contributors want
  [CONTRIBUTING.md](CONTRIBUTING.md) instead.

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

The archive is verified against **Python 3.14.2** with the exact versions
pinned in `requirements.txt` (mpmath 1.3.0, sympy 1.14.0); the Sage
cross-checks are verified against **SageMath 10.8**. The pins are exact rather
than lower bounds on purpose — a dependency free to drift is a certificate free
to drift. CI installs those pins with `--no-deps` and runs the same checks on
every push and pull request.

## Citing

The paper is being submitted to the arXiv; until the identifier is assigned,
replace `ARXIV-ID` below (and update `CITATION.cff` to match).

```bibtex
@misc{Sra2026CountExMachina,
  author        = {Suvrit Sra},
  title         = {{GPT}: The Counterexample Machine},
  year          = {2026},
  eprint        = {ARXIV-ID},
  archivePrefix = {arXiv},
  primaryClass  = {math.HO},
  note          = {Code and certificates:
                   \url{https://github.com/suvrit/count-ex-machina}}
}
```

To cite an individual counterexample rather than the paper, give its **result
id** — for example, `aim-problem-35`. Result ids are what the table below and
`registry.json` enumerate, and they are stable across revisions. A result need
not share the name of the directory holding it: `aim-problem-35` lives in
`counterexamples/stable-schur/`, which bundles two refuted problems.

The **ledger numbers** in the table are *not* stable — they are presentation
order, and admitting a case renumbers those after it. Every result also carries
an immutable `uid` in `registry.json`; that is a database key, not a citation.

## The cases

<!-- BEGIN CASE TABLE -->
| No. | Case | Status | Posed in | Certificate | Found by |
|---|---|---|---|---|---|
| 1 | [aim-problem-35](counterexamples/stable-schur/) | refuted | [Borcea–Brändén, AIM problem list, Problem 35](https://www.aimath.org/pastworkshops/polyaschurlaxrep.pdf) | exact | TODO (TODO) |
| 2 | [aim-problem-38](counterexamples/stable-schur/) | refuted | [Borcea–Brändén, AIM problem list, Problem 38](https://www.aimath.org/pastworkshops/polyaschurlaxrep.pdf) | exact | TODO (TODO) |
| 3 | [aim-problem-36](counterexamples/aim-problem-36/) | refuted | [Borcea–Brändén, AIM problem list, Problem 36](https://www.aimath.org/pastworkshops/polyaschurlaxrep.pdf) | exact | TODO (TODO) |
| 4 | [aim-problem-37](counterexamples/aim-problem-36/) | refuted | [Borcea–Brändén, AIM problem list, Problem 37](https://www.aimath.org/pastworkshops/polyaschurlaxrep.pdf) | exact | TODO (TODO) |
| 5 | [macdonald-schur-convexity](counterexamples/macdonald-schur-convexity/) | refuted | [C. McSwiggen and S. Sahi, Theorem 2.1](https://arxiv.org/abs/2605.12680v2) | exact | TODO (TODO) |
| 6 | [theta-derivative-log-concavity](counterexamples/theta-derivative-log-concavity/) | refuted | [G. Csordas, Open Problem 4.13, restating Coffey–Csordas Conjecture 2.5](https://arxiv.org/abs/1309.0055v2) | computer-assisted | TODO (TODO) |
| 7 | [dpp-feasible-step](counterexamples/dpp-feasible-step/) | refuted | [Z. Mariet and S. Sra, §2 (unnumbered)](https://proceedings.mlr.press/v37/mariet15.pdf) | exact | TODO (TODO) |
| 8 | [variance-only-matrix-discrepancy](counterexamples/variance-only-matrix-discrepancy/) | refuted | [Remark 4.25 of A. S. Bandeira's problem collection, quoted here from its restatement as Conjecture 1.2 of E. Akbaş and S. Sra](https://arxiv.org/abs/2606.16005) | exact | GPT-5.5 (Pro) (TODO) |
| 9 | [rank-two-mixed-norm](counterexamples/rank-two-mixed-norm/) | refuted | S. Sra — statement TODO | computer-assisted | TODO (TODO) |
| 10 | [logdet-loewner](counterexamples/logdet-loewner/) | refuted | S. Sra — statement TODO | exact | TODO (TODO) |
| 11 | [lorentzian-jensen](counterexamples/lorentzian-jensen/) | refuted | [S. Sra, standalone problem; formulation as recorded in §1 of the case's `paper.tex`](counterexamples/lorentzian-jensen/paper.tex) | exact | TODO (TODO) |
| 12 | [log-volume-distance](counterexamples/lorentzian-jensen/) | refuted | [S. Sra, standalone problem (geometric specialization of the same principle); formulation as recorded in §1 of the case's `paper.tex`](counterexamples/lorentzian-jensen/paper.tex) | exact | TODO (TODO) |
<!-- END CASE TABLE -->

Withheld cases are documented but excluded from the paper's admitted ledger;
see `audit_notes.md` and each case's README for the reason.

## Adding a counterexample

**The short path.** If you have a counterexample and an AI agent, you do not
need to clone this repository or learn its layout — paste this to the agent:

```text
Read https://raw.githubusercontent.com/suvrit/count-ex-machina/main/SUBMIT.md
and follow it exactly to package the counterexample I have.
```

It produces one file; send it as an issue or as a pull request adding
`submissions/<case-id>.md`. See [SUBMIT.md](SUBMIT.md).

The admission bar (exact or rigorous-interval certificates only; no
quantifier drift; see `tex/02-admission.tex` and
[CONTRIBUTING.md](CONTRIBUTING.md)) applies either way, and the full mechanical
discipline is:

1. **Create the case dir** (kebab-case id; it becomes the directory, registry,
   and link name):

   ```sh
   make new                     # prompts, then wires order/label/id for you
   ```

   or by hand, `cp -r counterexamples/_template counterexamples/<id>`.

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
   - `context_tex` (optional, per case): our own setup prose — notation and
     definitions — rendered just before the quoted statements so they can be
     read without the source paper at hand. It sits outside the quote boxes,
     so nothing of ours is ever mistaken for the source's words;
   - `provenance` (per result): the statement **as originally posed**, quoted
     ahead of the dossier in the paper — `statement_tex` (the quote),
     `source_tex` (who posed it and where, with `\cite{...}`), `url` and
     `retrieved` for the copy consulted, and `fidelity`: `"verbatim"` only if
     transcribed from the source's own text, otherwise `"paraphrase"`, which
     the paper labels as such. `source_tex` and `url` also become the linked
     "Posed in" cell of the case table above, so `url` may be a repo-relative
     path when the statement was posed in a file here; the build fails on any
     LaTeX macro it cannot render as markdown;
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
   make regen   # validates case.json, regenerates ledger/dossiers/registry/this table
   make check   # metadata valid + every certificate recomputes; what CI runs
   make paper
   ```

8. **Commit everything, including the regenerated files** (`tex/generated/`,
   `registry.json`, `README.md`, the case's `artifacts/`). Run
   `python tools/build.py --check` to confirm nothing is stale.

`tools/build.py` fails loudly on TODO placeholders, duplicate orders or
theorem labels, missing bib keys, and missing files — if it is silent about
the new case, the metadata is complete. Attribution from `case.json` is
rendered under the dossier heading in the paper and into `registry.json`
automatically.

## License

Code — `tools/`, every `verify.py`, and the Sage cross-checks — is licensed
under the Apache License 2.0 ([LICENSE](LICENSE)). Prose and mathematical
exposition — `tex/`, the dossiers, the case READMEs, and this file — are
licensed under CC BY 4.0 ([LICENSE-DOCS](LICENSE-DOCS)).

Contributions are accepted under these same terms; Apache-2.0 §5 governs
inbound code contributions. Please also read the
[Code of Conduct](CODE_OF_CONDUCT.md).
