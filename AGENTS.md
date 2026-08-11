# AGENTS.md — orientation for AI coding agents

Read this before touching anything. It is the tool-neutral brief; `CLAUDE.md`
points here, and `counterexamples/`, `tex/`, and `tools/` each carry a shorter
`AGENTS.md` for work inside them.

## What this repository is

An archive of AI-found counterexamples to publicly posed mathematical
statements, companion to the paper *“GPT: The Counterexample Machine”*
(Suvrit Sra, TU Munich). It is not a software project that happens to contain
mathematics: the artifact being shipped is **seventeen refuted statements, each
with a certificate a stranger can recompute**.

One invariant governs everything:

> Every admitted counterexample is verified by exact arithmetic (integers,
> rationals, algebraic identities) or by a rigorous outward-rounded interval
> computation — **never** by floating-point evidence alone.

The second invariant is honesty of attribution: who posed the statement, which
model found the witness, in which month. Fabricating any of that is worse than
leaving it `TODO`. See “Things that are never OK” below.

Those two invariants are the *only* narrow things here. The scope is broad on
purpose, so do not gatekeep a case on anything else: a statement need not be
famous (this archive is not restaging Riemann or Collatz — catalogues like
mathconjectures.com already cover those), a contributor need not be a
professional, and a certificate need not be machine-checked. A Lean, Rocq, or
Isabelle development is welcome and carried with the case, but it is not a
precondition and earns no higher standing than fifty lines of exact-rational
Python. Judge the evidence, never the pedigree.

## Who owns which file

The archive is written with AI assistance, so the boundary between what a tool
may rewrite and what a person has taken responsibility for has to be explicit.
Two rules, and they are not negotiable by an agent:

1. **A generator may produce a first draft of anything.** Scaffolding a case,
   a section, a table, a whole document is fine and expected.
2. **Once a human edits it, they own it, and no agent regenerates it without
   being told to in that session.** Adoption is one-way. "It drifted from the
   data" is a reason to *report* the drift, never to overwrite the prose.

So each file is in exactly one of three states:

| State | Who writes it | Examples |
|---|---|---|
| **machine-owned** | the generator, every `make regen` | `tex/generated/`, `registry.json`, the two marker-delimited regions of `README.md` |
| **adopted** | the maintainer, by hand; the build only *checks* it | `tex/ledger.tex` |
| **hand-written** | the maintainer, always | `tex/main.tex`, `tex/01-literature.tex`, `tex/02-admission.tex`, `tex/cxcase.sty`, every `case.tex`, all the `AGENTS.md` files |

`tools/build.py` enforces the first row: `machine_owned()` lists the only paths
it may write, and any other output path fails the build rather than silently
overwriting someone's prose. Nothing enforces the second row but this rule —
follow it.

**Adopting a generated file** (the `tex/ledger.tex` worked example): take its
current generated content as the seed, move it out of `tex/generated/`, delete
its entry from `outputs` in `build.py`, and replace the generation with a
*check* that catches the one thing a human can silently get wrong — usually
coverage, not wording. `check_ledger()` verifies every admitted result still
has a row and prints a paste-ready row for anything missing; it says nothing
about how the row reads, because that is the maintainer's. Run such a check
unconditionally, not behind `if not errors`, or it is dead code exactly while
the baseline is red.

## 30-second map

| Path | What it is | May an agent edit it? |
|---|---|---|
| `counterexamples/<dir>/` | one bundle per case: `case.json` (machine facts), `case.tex` (all prose), `verify.py`, `artifacts/` | **yes** — this is where the work is |
| `counterexamples/_template/` | scaffold copied by `tools/new_case.py` | only to change the scaffold itself |
| `tex/01-literature.tex`, `tex/02-admission.tex`, `tex/main.tex`, `tex/references.bib`, `tex/cxcase.sty` | hand-written paper and the case format | yes, carefully |
| `tex/generated/` | `cases.tex`, `appendix-cases.tex`, `appendix-brief.tex` — the ordered `\input` lists and per-case metadata, and nothing else | **no — generated** (but the `\input` lines that place them, in `tex/main.tex` and `tex/09-additional.tex`, are hand-written and yours to move) |
| `tex/09-additional.tex` | Appendix A: its heading, its prose, and two `\input`s | **yes — hand-written.** Nothing regenerates it |
| `tex/ledger.tex` | the archive ledger table, row by row | **yes — hand-written.** Nothing regenerates it; `build.py` only checks that every admitted result still has a row |
| `registry.json` | flattened machine-readable registry | **no — generated** |
| `README.md` between `<!-- BEGIN/END CASE TABLE -->` and `<!-- BEGIN/END COUNT BADGES -->` | case table, headline counts | **no — generated** |
| `tools/` | `build.py`, `verify_all.py`, `new_case.py`, `unpack_submission.py`, `exactcert.py` | yes, but see `tools/AGENTS.md` |
| `verification_report.json` | last run of `verify_all.py` | no — regenerable, gitignored |

A case **directory** is not a case **result**. Seventeen results live in fourteen
directories (`stable-schur` holds `aim-problem-35` and `aim-problem-38`;
`aim-problem-36` holds `aim-problem-36` and `aim-problem-37`;
`lorentzian-jensen` holds `lorentzian-jensen` and `log-volume-distance`).
Ids, ledger rows, credits, and citations are keyed to the **result**.

## Commands

```sh
make venv                    # python3 -m venv .venv + pinned deps, --no-deps
make check                   # build.py --check && verify_all.py   <- the CI gate
make verify                  # certificates only
make regen                   # regenerate the case list, registry, README table
make paper                   # cd tex && latexmk -pdf main
```

`PY` overrides the interpreter (`make check PY=python3`); the default is
`.venv/bin/python`. Single case: `.venv/bin/python tools/verify_all.py --only <case-id>`
(the directory id, not the result id), or `cd counterexamples/<id> && python verify.py`.

Toolchain: Python 3.14.2, `mpmath==1.3.0`, `sympy==1.14.0` — pinned exactly, not
floored, and installed with `--no-deps`. Do not relax a pin to make something
install; a dependency free to drift is a certificate free to drift. Sage
cross-checks run when `sage` is on `PATH` and are skipped loudly otherwise (CI
has no Sage, so every case must stand on its pure-Python certificate alone).

## The baseline is red — know what is *your* failure

As of the current commit, on a clean tree:

- `make verify` → **passes**, `ALL 14 CASES PASS` (two Sage cross-checks pass
  too, if Sage is installed). Keep it that way; this is the gate you can hold
  yourself to.
- `make check` → **fails with 12 pre-existing errors**: one
  `credits.found_by` TODO for each of the seventeen results except
  `quantum-coupon-collector` and `odonnell-matrix-conjecture`, plus a missing
  `provenance` for `rank-two-mixed-norm`. These are the maintainer's to fill in
  — they are facts about real sessions that nobody can reconstruct from the
  repository.
- CI is **temporarily disabled** because of exactly those twelve: the workflow's
  `push` and `pull_request` triggers are commented out in
  `.github/workflows/verify.yml`, so nothing runs automatically and the verify
  badge is parked. Run `make check` yourself; it is still the gate, and the
  workflow can be dispatched by hand from the Actions tab.
- Generated files are nevertheless **current**: `tools/build.py --allow-todo`
  reproduces them byte-for-byte. Because plain `build.py` refuses to write
  while errors stand, use `--allow-todo` to regenerate today, and diff the
  result — anything beyond your own case is drift you introduced.

So: capture the error list *before* you start, and compare. Twelve errors
after your change means you broke nothing; eleven probably means you invented
an attribution.

## Things that are never OK

1. **Inventing attribution or provenance.** `\foundby` model and date,
   `\posedby`, the `cxsource` region, `url`, `retrieved` — these describe events
   in the world. If you do not know, leave the `TODO` and say so in your summary.
   Never mark `fidelity: "verbatim"` unless the text was transcribed from the
   source; `"paraphrase"` is the honest default and the paper labels it as such.
2. **Making a check pass by weakening it.** Loosening a tolerance, deleting an
   `assert`, dropping a case from a loop, or converting an exact comparison to
   a float one destroys the only thing this repository claims.
3. **Floating point in a certificate.** `float`, `numpy`, and bare `math` are
   inadmissible as evidence. Use `fractions.Fraction`, `sympy` exact types, or
   `mpmath` at declared precision with a rigorous tail bound (and add a Sage
   interval cross-check for analytic cases).
4. **Putting LaTeX in `case.json`.** Every word written in LaTeX belongs in
   the case's `case.tex`, inside a `cx...` region; the JSON carries ids, uid,
   enums, dates, urls. The build rejects prose left in the JSON by name.
5. **Hand-editing generated files.** Edit `case.json` (or the case's `case.tex`)
   and regenerate. A hand-edit is reverted by the next `make regen`, and CI
   runs `git diff --exit-code`, so it fails there anyway.
6. **Changing or reusing a `uid`.** It is the registry's immutable primary key,
   checked against the committed `registry.json`. Mint one only with
   `python tools/new_case.py --mint-uid`, never by hand, and never cite one —
   humans cite the result `id`. Renaming a result is the exception, and it
   keeps the uid: change `id` and add the old one to `former_ids`.
7. **Fixing other people's TODOs while passing through.** Renumbering `order`,
   touching a neighbouring case, or reformatting adjacent LaTeX turns a
   reviewable diff into an unreviewable one.
8. **Refuting a strengthening.** If you tightened a hypothesis or flipped a
   quantifier to make the witness work, you have refuted a different statement.
   This is the failure mode that gets a case withdrawn (see `audit_notes.md`).

## Common tasks

| Task | Start here |
|---|---|
| Add a counterexample | `make new`, then `counterexamples/AGENTS.md` |
| Package a case for someone else's repository visit | `SUBMIT.md` — the self-contained brief for a contributor's agent |
| Unpack an incoming submission | `make unpack BUNDLE=submissions/<id>.md` |
| Fix or extend a `verify.py` | `counterexamples/AGENTS.md` § verify.py contract |
| Edit a statement, refutation, or context prose | `counterexamples/AGENTS.md` § case.tex, region by region |
| Understand a build error | `counterexamples/AGENTS.md` § build errors → fixes |
| Change the generator or the schema | `tools/AGENTS.md` |
| Touch the paper or its macros | `tex/AGENTS.md` |
| Decide whether a case is admissible at all | `tex/02-admission.tex`, then `CONTRIBUTING.md` |
| Check whether a case duplicates an admitted one | `audit_notes.md` § duplicates — no build check exists; read the sources |

## Definition of done

1. `make regen` (today: `.venv/bin/python tools/build.py --allow-todo`) run, and
   the regenerated files committed.
2. `make check` shows no error naming your case — the pre-existing fourteen may
   remain.
3. `make verify` ends with `ALL n CASES PASS`.
4. `make paper` compiles.
5. `git status` clean after a second `make verify` — certificates must
   recompute bit-for-bit, which is what CI's `git diff --exit-code` enforces.
6. Your summary states plainly what you did **not** do: every TODO left, every
   assumption made, every check skipped. Under-claiming is cheap here;
   over-claiming corrupts an archive whose entire value is that its claims hold.

License: code Apache-2.0, prose CC BY 4.0. Contributions land under both.
