# AGENTS.md — authoring a case

Scope: everything under `counterexamples/`. Read `/AGENTS.md` first for the
invariants; this file is the mechanics. The human-facing versions are
`/CONTRIBUTING.md` (workflow) and `/tex/02-admission.tex` (the authoritative
admission rule).

## Anatomy of a case directory

```
counterexamples/<case-id>/
  case.json      machine facts only: ids, uid, enums, dates, urls
  case.tex       every word written in LaTeX, in \begin{cx...} regions
  verify.py      the certificate: verify() -> dict, exact arithmetic only
  verify_*.sage  optional Sage interval cross-check (+ its .sage.py transcript)
  README.md      statement summary, how to verify, what the artifacts hold
  artifacts/     certificate.json, written by `python verify.py`
  paper.tex      standalone write-up — withheld cases only
```

`case-id` is kebab-case and **must equal** `case.json`'s `id`. One directory may
hold several `results`; each result has its own id, `uid`, ledger row, theorem,
and (optionally) credits. Scaffold with `make new` — it wires the id, the next
free `order`, the `theorem_label`, and the minted `uid`, leaving TODOs only
where mathematics goes.

## The two-file rule

**`case.json` holds machine facts. `case.tex` holds everything written in
LaTeX.** No exceptions: a field that would carry LaTeX is a region, not a key,
and `tools/build.py` rejects by name any prose left in the JSON. This is why
you write `$\mathcal{Y}$` rather than `"$\\mathcal{Y}$"` collapsed onto one
line, and why editing a case means reading one file top to bottom instead of
four — which is where consistency between the notation, the quoted statement,
and the proof actually gets lost.

## case.tex, region by region

A `\begin{cx...}` and its `\end` must each sit alone on a line. Regions may not
nest. Whole-line `%` comments inside a region are stripped before the paper
sees them, so the template's guidance costs nothing — and cannot hide an
unfilled TODO.

| Region | | |
|---|---|---|
| `\cxtitle{...}` | once | the case's section heading (a macro: a run-in subsection heading issued from inside an environment is dropped by LaTeX) |
| `cxcredits` | once, `[result-id]` to override | `\posedby` `\foundby{model}{YYYY-MM}` `\formalizedby` `\auditedby` `\contributedby` |
| `cxcontext` | optional | our setup prose: notation the quoted statement needs, rendered outside the quote boxes so our words are never mistaken for the source's |
| `cxsource{rid}` | per result | who posed it and where, with `\cite{...}` |
| `cxstatement{rid}` | per result | the statement **as originally posed**, and nothing else: the box is labelled `ctx:rid` for you, so point at it with `Problem~\ref{ctx:rid}` rather than putting a `\label` inside the source's words — and never by the source's own number, which resolves to nothing |
| `cxsummary{rid}` | per result | one line: the ledger's statement column |
| `cxcertificate{rid}` | per result | one line: the ledger's certificate column |
| `cxrefutation` | once, or split | the conjecture in prose, the theorem, the proof. A case refuting several statements may **close it before the next `cxstatement` and reopen after**, so each quote box stands with the theorem that answers it; the pieces are read as one region, in file order. Regions may not nest, so this is the only way to interleave them |

`\foundby` may repeat when a witness took more than one model or session. A
`cxcredits[rid]` merges over the case block role by role, so a result that
differs only in its finder need not restate the rest.

`cxrefutation` is body only — the `\section` / `\subsection` heading and the
credit line are **generated**, and writing them yourself duplicates them in the
PDF:

```tex
\begin{cxrefutation}
Prose stating the original conjecture, with \cite{key}.

\begin{theorem}[\statusfalse: short name]\label{thm:<case-id>}
  The claim, refuted as posed.
\end{theorem}
\begin{proof}
  The explicit witness, with exact values.  Say how displayed decimals are to
  be read — e.g. "interpret all displayed six-decimal entries as exact rationals
  of denominator $10^6$".
\end{proof}

\begin{remark}[Scope]  % optional: what is and is not refuted
\end{remark}
\end{cxrefutation}
```

These are **real LaTeX environments**, defined in `tex/cxcase.sty`, which also
defines the theorem environments, status tags and notation a case may use — so
a misspelled or unclosed region is a compile error, and one case compiles on its
own: `make preview CASE=<id>`. `tools/build.py` reads the same regions for
`registry.json` and the README table, which are not LaTeX's to produce.
The macros you may use and must not redefine are listed in `tex/AGENTS.md`.

## case.json, field by field

Enums are enforced; the exact spellings are in `tools/build.py`.

- `id` — equals the directory name.
- `title` — plain text, for `registry.json`. The typeset title is `cxtitle`.
- `status` — `"refuted"` (enters the ledger) or `"withheld"` (documented,
  excluded; then needs `withheld_reason`, no `order`, and a standalone
  `paper.tex`).
- `order` — positive int, unique, presentation order only. **Not stable, not a
  citation.** Take the next free integer; renumber nothing.
- `group` — optional, currently `"aim"` or `"amsel"`. Members must be
  **contiguous** in `order`, so joining a group renumbers cases you do not own:
  do it explicitly and say so in the PR, never silently.
- `appendix` — optional bool, default false, and a **maintainer's disposition,
  not a submitter's**. `true` typesets the case as a subsection of the paper's
  shared "Additional counterexamples" appendix instead of a body section, and
  collapses its ledger row in with the rest of its `group`. It changes
  presentation only: an appendix case clears exactly the same three admission
  conditions, keeps its `uid`, and is still counted by statement. Use it for a
  statement too slight to carry a section of its own, or one whose public
  resolution belongs to someone else. The headline badge reports these
  separately, as "N refuted, M additional".
- `brief` — optional bool, default false, and only legal alongside
  `appendix: true`. One step further down: the case is listed as a single
  bullet in the appendix's "Statements recorded without a dossier" and carries
  **no ledger row at all**, so its statement, refutation and proof are not
  typeset in the paper. Nothing else changes — the certificate still runs in
  `make verify`, the `uid` and the `registry.json` entry stay, and the README
  case table still lists it, because those index the archive rather than the
  paper. `build.py` errors if a brief result still has a row in
  `tex/ledger.tex`, and the bullet's wording comes from the case's own
  `cxsummary` and `cxcertificate` regions, so edit those and `make regen`.
- `prose` — the LaTeX file, `case.tex`.
- `bib_keys` — every key must exist in `tex/references.bib`.
- `results[]` — one entry per refuted statement:
  - `id` — globally unique across all cases; this is what humans cite, and what
    every `cx...{rid}` region names.
  - `uid` — 8 chars of Crockford base32, minted by
    `python tools/new_case.py --mint-uid`. Immutable, never reused, never
    cited; the build compares against the committed `registry.json`.
  - `former_ids` — optional list, omit it unless you renamed something. **To
    rename a result, change `id` and add the old id here**; keep the `uid`,
    which is precisely what it is for. Without this the build cannot tell a
    rename from a retired uid being repointed at a new statement, so it refuses
    the change — the error names the id to add. Every `cx...{rid}` region in
    `case.tex` must be renamed too, including the optional `cxcredits[rid]`
    override, which is **not** validated against `case.json` and will otherwise
    be dropped in silence. A former id is dead: it can never become the live id
    of any result again, and `registry.json` carries it so a reference written
    against an older registry still resolves.
  - `class` — `published theorem` | `published conjecture` |
    `external conjecture` | `external formal problem` | `user formal problem`.
  - `certificate_level` — `exact` | `computer-assisted`.
  - `theorem_label` — must appear verbatim as `\label{...}` in `cxrefutation`.
  - `ledger_label` — plain text, required only when the case sets
    `appendix: true`. Names the item this result refutes, as the source numbers
    it (`"Problem 4.6(b)"`), because the collapsed ledger row has to say which
    statements it stands for and nothing else in the case records that in plain
    text. No LaTeX: it is spliced straight into `README.md`, and on a `brief`
    case it is typeset as well, so the build rejects TeX specials there.
  - `provenance` — `url` and `retrieved` (the copy consulted; `url` may be a
    repo-relative path when the statement was posed in a file here) and
    `fidelity` (`verbatim` **only** if transcribed from the source's own text,
    else `paraphrase`). The words themselves are `cxsource` and `cxstatement`.
- `verify` — `python` (entry script), `sage` (list of cross-checks),
  `requires` (extra pip deps).
- `artifacts[]` — `file` + `description` (plain text); a TODO description fails
  the build.

## verify.py contract

```python
def verify() -> dict:
    """Raise AssertionError if any check fails."""
    ...
    return {"id": "<result or case id>", "ok": True,
            "summary": "one line, including the key exact values",
            "witness": {...}}          # stringify Fractions
```

`tools/verify_all.py` imports the file by path, calls `verify()`, and asserts
`ok is True`. The `__main__` block writes
`artifacts/certificate.json` as `json.dumps(witness, indent=2, sort_keys=True)`.

Hard requirements:

- **Exact or rigorous only.** `fractions.Fraction`, exact `sympy`, or `mpmath`
  at a declared `mp.dps` with a tail bound you can justify — plus a Sage
  interval cross-check for analytic cases. No `float`, no `numpy`, no bare
  `math` as evidence. A decimal in the `summary` is a human convenience printed
  *from* the exact value, never the thing being tested.
- **Deterministic, byte-for-byte.** No timestamps, no randomness, no dict order
  dependence — CI re-runs every certificate and then `git diff --exit-code`.
- **Standalone.** `cd counterexamples/<id> && python verify.py` must work.
  Shared Fraction helpers (`inv2`, `inv3`, `det2`, `det3`, `madd`, `mmul2`,
  `mscale`, `assert_positive_definite_2/3`) come from `tools/exactcert.py` via
  the `sys.path` insert shown in `_template/verify.py`.
- **Never weaken an assertion to make it pass.** If it fails, the mathematics
  is wrong or the witness is wrong; say so rather than adjusting the threshold.

## Build errors → fixes

| Error | Fix |
|---|---|
| `id "x" does not equal directory name "y"` | rename the directory or the id; they are one name |
| `order N already used by case X` | take the next free integer, do not renumber X |
| `group 'aim' is not contiguous in 'order'` | grouped cases share one section; make their orders adjacent, deliberately |
| `prose file 'case.tex' does not exist` | create it, or fix `prose` in `case.json` |
| `[...] no longer belong in case.json; that prose lives in case.tex` | move those words into the named region; LaTeX never goes back into the JSON |
| `unknown region cxfoo` / `cxfoo{x} names no result in case.json` | check the spelling and the result id — they must match `results[].id` |
| `\begin{cxfoo} is never closed` / `inside cxbar; these regions may not nest` | one region at a time, each delimiter alone on its line |
| `cxsummary{x} appears twice` | one region per result; delete the duplicate |
| `missing 'uid'` | `python tools/new_case.py --mint-uid` — never invent one |
| `uid changed from A to B` | restore the committed uid; it is immutable |
| `uid ... is already bound to result R` | restore the committed uid — unless you renamed `R`, in which case keep the uid and add `R` to `former_ids` |
| `former id 'x' is the live id of a result` / `is already claimed by` | a renamed-away name is dead; pick a different `id` |
| `\label{thm:x} not found in the cxrefutation region` | make `theorem_label` and the `\label` identical |
| `bib key 'k' not found` | add the entry to `tex/references.bib` |
| `unbalanced braces in ...` | count `{}` in that region |
| `\foundby needs a real model and date` | supply the real model and `YYYY-MM`, or leave it and report it — **never guess** |
| `case.tex needs cxsource{x} and cxstatement{x}` | same: find the source or leave the TODO standing |
| `unknown credit macro \foo` | the roles are `\posedby` `\foundby` `\formalizedby` `\auditedby` `\contributedby` |
| `unhandled LaTeX [...] ; extend TEX_SUBS` | the README table renderer is deliberately narrow — simplify the fragment, or extend `TEX_SUBS` in `tools/build.py` |
| `stale generated file: ...` | run `make regen` and commit the result |

`--allow-todo` downgrades the `found_by` and provenance errors to warnings so
the generated files can be rebuilt; it is a migration switch, not a way to pass
CI, which runs plain `--check`.

## Before you call it done

```sh
make regen        # today, while the eleven found_by TODOs stand:
                  #   .venv/bin/python tools/build.py --allow-todo
make check        # no error may name your case; the pre-existing 12 may remain
make verify       # ALL n CASES PASS
make paper
```

Then commit the regenerated files too — `tex/generated/`, `registry.json`,
`README.md`, and your `artifacts/`. State every TODO you left.
