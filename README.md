<div align="center">

# count-ex-machina

**Counterexamples found by AI, certified by exact arithmetic.**

[![verify](https://github.com/suvrit/count-ex-machina/actions/workflows/verify.yml/badge.svg?branch=main)](https://github.com/suvrit/count-ex-machina/actions/workflows/verify.yml)
<!-- BEGIN COUNT BADGES -->
[![counterexamples](https://img.shields.io/badge/counterexamples-11%20refuted%2C%208%20additional-0b7285)](#the-cases)
[![certificates](https://img.shields.io/badge/certificates-17%20exact%2C%202%20interval-0b7285)](#the-cases)
<!-- END COUNT BADGES -->
[![Python](https://img.shields.io/badge/Python-3.14-3776AB?logo=python&logoColor=white)](requirements.txt)
[![code: Apache 2.0](https://img.shields.io/badge/code-Apache%202.0-4c566a)](LICENSE)
[![docs: CC BY 4.0](https://img.shields.io/badge/docs-CC%20BY%204.0-4c566a)](LICENSE-DOCS)
[![contributions welcome](https://img.shields.io/badge/contributions-welcome-2f9e44)](CONTRIBUTING.md)

<sub>Every admitted case recomputes from source — exact arithmetic or rigorous
intervals, never floating point.</sub>

</div>

Companion repository for the paper **“GPT: The Counterexample Machine”**
(Suvrit Sra, TU Munich). It archives AI-assisted counterexamples to
mathematical statements that were posed publicly — in a paper, a preprint, a
problem list, a talk, a forum thread — together with certificates a stranger
can recompute: every admitted case is verified by exact arithmetic or by a
rigorous interval computation, never by floating-point evidence alone.

The archive is **broad by design**. A refuted statement does not have to be
famous, and you do not have to be a professional mathematician to send one in.
What is not negotiable is the certificate — see [Scope](#scope).

**Read first, run second.** The explicit goal of both the paper and this
repository is that the exposition be human-readable and human-verifiable: every
statement is quoted as it was posed, every witness is written out, and every
refutation is an argument you can follow and check on paper. The
machine-checkable part — `verify.py`, exact arithmetic, interval enclosures —
*accompanies* that reading rather than replacing it. For us the joy of
understanding mathematics, of proving and disproving, and of communicating that
understanding to other humans is the primary ideal we aspire towards; the
certificates exist to serve it, so that nobody has to take our word for
anything.

## Contribute one in a single paste

You have a counterexample and an AI agent open. That is the whole prerequisite
— no clone, no install, nothing below this section to read. Paste this to the
agent:

```text
Read https://raw.githubusercontent.com/suvrit/count-ex-machina/main/SUBMIT.md
and follow it exactly to package the counterexample I have.
```

It reads [SUBMIT.md](SUBMIT.md) — the admission bar, the file format, the
checks to run — and hands you back **one markdown file**. Open an issue and
paste it in, or a pull request adding `submissions/<case-id>.md`. Done.

What that file has to clear, and what your agent is told not to fudge:

- the statement **appeared publicly before you refuted it** — paper, preprint,
  problem list, talk, forum post — or was posed formally and recorded in
  advance;
- its **hypotheses and quantifiers are untouched** — refuting a strengthening
  refutes nothing;
- the witness is checked by **exact arithmetic or rigorous intervals**, never
  by floating point;
- attribution is **real or left blank**: which model found it, in which month,
  and who posed the statement. A guess is worse than a `TODO`.

Numerical evidence you cannot yet certify is still welcome as an issue —
turning it into an exact certificate is much of what this archive is for. The
long-form version of all this, for contributors working in a clone, is
[Adding a counterexample](#adding-a-counterexample).

## Scope

**Not the famous conjectures.** This archive is not trying to restage Riemann,
Collatz, or Hodge. Catalogues of the great open problems already exist and do
the job well — [mathconjectures.com](https://mathconjectures.com), for one,
lists a few hundred, sorted by field and prominence. Nothing here competes with
that, and a case is not more welcome for being about a household name.

What this archive collects is the other end of the distribution: the lemma
stated in passing in someone's preprint, the plausible strengthening on a
problem list, the "surely this holds" from a seminar or a forum thread.
Statements nobody got around to checking, which turn out to be false. They are
individually modest and collectively the point — one of [the cases
below](#the-cases) had stood unanswered on MathOverflow for nine years.

**Anyone may contribute.** Research mathematicians, students, hobbyists, people
who found something odd while poking at a computer algebra system. The archive
does not ask who you are or where you work. It asks whether the statement was
posed publicly before you refuted it, and whether the witness recomputes.

**Any certificate technology.** Exact rational arithmetic in fifty lines of
Python is a perfectly good certificate, and most cases here are exactly that. A
Lean, Rocq, or Isabelle development is very welcome — send it and it will be
carried alongside the case — but it is **not** a precondition, and no case
ranks lower for lacking one. Machine-checked proof is one way to make a
refutation independently checkable, not the definition of it.

What the requirement actually is: an independent reader reruns the check and
gets the same answer. Today's harness runs Python, with optional Sage interval
cross-checks. The one thing that stays inadmissible is floating-point evidence
with no rigorous enclosure — that certifies nothing, in any language.

## Layout

```text
count-ex-machina/
├─ counterexamples/          the archive itself — one directory per case
│  ├─ _template/             scaffold copied by "make new"
│  └─ <case-id>/
│     ├─ case.json           machine facts: ids, uid, enums, dates, urls
│     ├─ case.tex            all the LaTeX: the statement as posed, the context
│     │                      it needs, the ledger lines, the refutation
│     ├─ verify.py           the certificate — exact arithmetic or intervals
│     ├─ verify_*.sage       optional interval cross-check
│     ├─ README.md           what it refutes, how to check it
│     └─ artifacts/          certificate.json, written by verify.py
├─ tex/                      the paper
│  ├─ main.tex               preamble, front matter, the \input's
│  ├─ cases.tex              the body's case list: headings and \input's, by hand
│  ├─ 01-literature.tex      AI-assisted counterexamples in the literature
│  ├─ 02-admission.tex       the authoritative admission rule
│  ├─ references.bib
│  ├─ cxcase.sty             the case format: the cx... environments
│  └─ generated/             metadata.tex — per-result facts LaTeX cannot know
├─ tools/
│  ├─ build.py               validate metadata, regenerate everything derived
│  ├─ verify_all.py          recompute every certificate
│  ├─ new_case.py            scaffold a case ("make new")
│  ├─ unpack_submission.py   turn a SUBMIT.md bundle into a case directory
│  └─ exactcert.py           shared exact-arithmetic helpers
├─ submissions/              inbox for contributed bundles; never built by CI
├─ Makefile                  one-command entry points; "make check" is the gate
├─ registry.json             every result, flattened and machine-readable
├─ SUBMIT.md                 the one-paste brief for a contributor's agent
├─ AGENTS.md                 orientation for AI agents; more in the dirs above
└─ CONTRIBUTING.md           the full contributor workflow
```

Two rules the layout encodes.

**A case is two files.** `case.json` holds machine facts; `case.tex` holds every
word written in LaTeX, in regions the build extracts. No LaTeX ever goes in the
JSON — so you write `$\mathcal{Y}$`, and you edit one file rather than four.

**Generated files are never hand-edited.** `tex/generated/`, `registry.json`,
and this file's case table and count badges all come from the per-case
`case.json` and `case.tex` via `tools/build.py`, and are checked in so a reader
need not run anything.

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
`counterexamples/aim-problems/`, which bundles four refuted problems.

The **ledger numbers** in the table are *not* stable — they are presentation
order, and admitting a case renumbers those after it. Every result also carries
an immutable `uid` in `registry.json`; that is a database key, not a citation.

## The cases

<!-- BEGIN CASE TABLE -->
| No. | Case | Status | Posed in | Certificate | Found by |
|---|---|---|---|---|---|
| 1 | [aim-problem-35](counterexamples/aim-problems/) | refuted | [Borcea–Brändén, AIM problem list, Problem 35](https://www.aimath.org/pastworkshops/polyaschurlaxrep.pdf) | exact | GPT-5 (Pro) (2026-01-10) |
| 2 | [aim-problem-38](counterexamples/aim-problems/) | refuted | [Borcea–Brändén, AIM problem list, Problem 38](https://www.aimath.org/pastworkshops/polyaschurlaxrep.pdf) | exact | GPT-5 (Pro) (2026-01-10) |
| 3 | [aim-problem-36](counterexamples/aim-problems/) | refuted | [Borcea–Brändén, AIM problem list, Problem 36](https://www.aimath.org/pastworkshops/polyaschurlaxrep.pdf) | exact | GPT-5.6 (Pro) (2026-07-30) |
| 4 | [aim-problem-37](counterexamples/aim-problems/) | refuted | [Borcea–Brändén, AIM problem list, Problem 37](https://www.aimath.org/pastworkshops/polyaschurlaxrep.pdf) | exact | GPT-5.6 (Pro) (2026-07-30) and bugfixed by Opus 5 (2026-08-10) |
| 5 | [macdonald-schur-convexity](counterexamples/macdonald-schur-convexity/) | refuted | [C. McSwiggen and S. Sahi, Theorem 2.1](https://arxiv.org/abs/2605.12680v2) | exact | GPT-5.6 (Pro) (2026-05-14) |
| 6 | [theta-derivative-log-concavity](counterexamples/theta-derivative-log-concavity/) | refuted | [G. Csordas, Open Problem 4.13, restating Coffey–Csordas Conjecture 2.5](https://arxiv.org/abs/1309.0055v2) | computer-assisted | GPT-5.5 (Pro) (2026-02-22) |
| 7 | [variance-only-matrix-discrepancy](counterexamples/variance-only-matrix-discrepancy/) | refuted | [Remark 4.25 of A. S. Bandeira's problem collection.](https://arxiv.org/abs/2606.16005) | exact | GPT-5.5 (Pro) (2026-05-24) |
| 8 | [mixed-norm-general-s](counterexamples/rank-two-mixed-norm/) | refuted | [A. Sah, M. Sawhney, D. Stoner and Y. Zhao, the open question stated immediately after inequality (3.1) in §3](https://arxiv.org/abs/1809.09462) | exact | Opus 5 (2026-08) |
| 9 | [yufei-psd](counterexamples/rank-two-mixed-norm/) | refuted | [A. Sah, M. Sawhney, D. Stoner and Y. Zhao, the same open question at $B=A$; shared with S. Sra by Y. Zhao in private communication, May 2018](https://arxiv.org/abs/1809.09462) | computer-assisted | GPT-5.6 Sol (Pro) (2026-07-13) |
| 10 | [quantum-coupon-collector](counterexamples/quantum-coupon-collector/) | refuted | [S. Sra, MathOverflow question 263833](https://mathoverflow.net/questions/263833/quantum-coupon-collection-positivity-of-an-alternating-sum-of-matrices) | exact | GPT Pro (2026-02-16) |
| 11 | [odonnell-matrix-conjecture](counterexamples/odonnell-matrix-conjecture/) | refuted | [R. O'Donnell, answering a question of Nengkun Yu on MathOverflow, reports that he and J. Wright had been considering the problem in connection with quantum tomography, and closes by conjecturing the unit-trace case. The same conjecture was put to S. Sra by O'Donnell in personal communication.](https://mathoverflow.net/a/212759) | exact | GPT-5.6 Pro (2026-08) |
| 12 | [courtade-volume-conjecture](counterexamples/courtade-volume-conjecture/) | refuted by explicit construction | [Courtade's volume conjecture for Minkowski sums is false — Section IV closing question](https://people.eecs.berkeley.edu/~courtade/pdfs/ConcavityEntropy_ISIT2017.pdf) | exact | Suvrit Sra, by hand (2022-05) |
| 13 | [dpp-feasible-step](counterexamples/dpp-feasible-step/) | refuted by explicit construction | [Feasible Picard steps for DPP likelihood — the unnumbered claim in §2](https://proceedings.mlr.press/v37/mariet15.pdf) | exact | GPT-5.6 (2026-08) |
| 14–15 | [lorentzian-jensen](counterexamples/lorentzian-jensen/) | refuted by explicit construction | Log-volume midpoint gap and its Lorentzian generalization — the geometric specialization, as posed, the proposed master theorem, as posed | exact | GPT-5.6 Pro (2026-07-31) |
| 16–19 | [sdd-nystrom-diminishing-returns](counterexamples/sdd-nystrom-diminishing-returns/), [osi-sketch-and-solve](counterexamples/osi-sketch-and-solve/), [hamiltonian-nepv-identity](counterexamples/hamiltonian-nepv-identity/), [qrcp-orthonormal-greedy](counterexamples/qrcp-orthonormal-greedy/) | refuted by explicit construction | [Simons workshop open questions — Problem 4.6(b), Problem 5.1, the identity after eq. (20) in §6.2, Problem 4.3](https://arxiv.org/html/2602.05394v2) | exact | OpenAI Codex (2026-08) |
<!-- END CASE TABLE -->

Withheld cases are documented but excluded from the paper's admitted ledger;
see `audit_notes.md` and each case's README for the reason.

## Adding a counterexample

This is the long form, for contributors working in a clone; most people want
[the single paste](#contribute-one-in-a-single-paste) instead. The admission
bar (exact or rigorous-interval certificates only; no quantifier drift; see
`tex/02-admission.tex` and [CONTRIBUTING.md](CONTRIBUTING.md)) applies either
way, and the mechanical discipline is:

1. **Create the case dir** (kebab-case id; it becomes the directory, registry,
   and link name):

   ```sh
   make new                     # prompts, then wires order/label/id for you
   ```

   or by hand, `cp -r counterexamples/_template counterexamples/<id>`.

   A case is two files. **`case.json` carries machine facts and no LaTeX
   whatsoever; `case.tex` carries every word written in LaTeX.**

2. **`case.json`**:
   - `id` must equal the directory name; `title` is plain text, for the
     registry;
   - `status`: `"refuted"` (goes into the ledger) or `"withheld"` (documented
     but excluded; needs `withheld_reason` and a standalone `paper.tex`);
   - `order`: next free integer, unless the case joins a group (below);
   - `group` (optional): appendix cases sharing a group key collapse to one
     row of the table above — currently only `"amsel"` — and their `order`
     values must be consecutive, so adding one renumbers the cases after it;
     statements that share a section of the paper are instead one case with
     several `results`;
   - one `results` entry per refuted statement (usually one; `aim-problems`
     has four): `class` and `certificate_level` the classification,
     `theorem_label` matching the `\label` in the refutation, and a
     `provenance` block giving `url` and `retrieved` for the copy consulted
     plus `fidelity` — `"verbatim"` only if transcribed from the source's own
     text, otherwise `"paraphrase"`, which the paper labels as such;
   - `verify`: entry script, optional Sage cross-checks, extra pip deps.

3. **`case.tex`** — one region per thing, each `\begin{cx...}` and `\end` alone
   on its line, never nested:
   - `\cxtitle{...}` — the case's section heading in the paper;
   - `cxcredits` — `\posedby`, `\foundby{model}{YYYY-MM}` (repeatable),
     `\formalizedby`, `\auditedby`, `\contributedby`; add `cxcredits{result-id}`
     for a result whose attribution differs, and it merges over the case block
     role by role;
   - `cxcontext` (optional) — our own setup prose, notation and definitions,
     rendered just before the quoted statements so they can be read without the
     source paper at hand. It sits outside the quote boxes, so nothing of ours
     is ever mistaken for the source's words;
   - `cxsource{result-id}` and `cxstatement{result-id}` — who posed it and
     where, and the statement **as originally posed**, quoted ahead of the
     refutation in the paper. The source and `provenance.url` also become the
     linked "Posed in" cell of the case table above, so `url` may be a
     repo-relative path when the statement was posed in a file here; the build
     fails on any LaTeX macro it cannot render as markdown;
   - `cxsummary{result-id}` and `cxcertificate{result-id}` — the two ledger
     columns, one line each;
   - `cxrefutation` — body only; do **not** write the `\section` /
     `\subsection` heading or the credit line (both are generated). Follow the
     house structure: prose stating the original conjecture with `\cite`, a
     `theorem` environment whose bracketed title carries `\statusfalse` and
     whose `\label` equals `theorem_label`, a proof with the explicit witness,
     optionally `\begin{remark}[Scope]`.

4. **`.bib` entries** — add cited works to `tex/references.bib` and list the
   keys in `bib_keys` (the build fails on unknown keys).

5. **`verify.py`** — implements `verify() -> dict` (raises `AssertionError` on
   failure; returns `id`/`ok`/`summary`/`witness`), exact arithmetic or
   rigorous intervals only; the `__main__` block writes
   `artifacts/certificate.json`. Shared Fraction matrix helpers live in
   `tools/exactcert.py`. Add Sage interval cross-checks for analytic cases.

6. **Case `README.md`** — statement summary, how to verify, what the
   artifacts contain.

7. **Regenerate, verify, build**:

   ```sh
   make regen   # validates the metadata, regenerates the case list, registry, this table
   make check   # metadata valid + every certificate recomputes; what CI runs
   make paper
   ```

8. **Commit everything, including the regenerated files** (`tex/generated/`,
   `registry.json`, `README.md`, the case's `artifacts/`). Run
   `python tools/build.py --check` to confirm nothing is stale.

`tools/build.py` fails loudly on TODO placeholders, duplicate orders or
theorem labels, missing bib keys, and missing files — if it is silent about
the new case, the metadata is complete. Attribution from `cxcredits` is
rendered under the case heading in the paper and into `registry.json`
automatically.

## License

Code — `tools/`, every `verify.py`, and the Sage cross-checks — is licensed
under the Apache License 2.0 ([LICENSE](LICENSE)). Prose and mathematical
exposition — `tex/`, every `case.tex`, the case READMEs, and this file — are
licensed under CC BY 4.0 ([LICENSE-DOCS](LICENSE-DOCS)).

Contributions are accepted under these same terms; Apache-2.0 §5 governs
inbound code contributions. Please also read the
[Code of Conduct](CODE_OF_CONDUCT.md).
