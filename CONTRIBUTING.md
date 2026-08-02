# Contributing a counterexample

Contributions are welcome. The bar is deliberately high: this archive only
admits counterexamples with independently checkable certificates.

## Admission criteria

The authoritative statement is the “Admission rule and audit standard” section
of the paper (`tex/02-admission.tex`); in summary, an admissible archive
counterexample must satisfy all three conditions:

1. **Provenance of the statement.** The refuted statement is published or
   publicly posed by someone other than the discoverer of the counterexample,
   or it is a standalone formal problem explicitly posed in advance.
2. **No quantifier drift.** The original hypotheses and quantifiers are
   preserved exactly; refuting a strengthening of a statement does not count
   as refuting the statement.
3. **Independent checkability.** The witness is verifiable by exact arithmetic
   (integers, rationals, algebraic identities), a complete analytic
   calculation, or a rigorous outward-rounded interval certificate.

Certificate levels (same section): an **exact certificate** uses only exact
arithmetic end to end; a **computer-assisted proof** may use rigorous interval
arithmetic with explicit error control. Floating-point-only evidence is
inadmissible at either level.

## The short path: let an agent package it

If you have an AI agent, you can skip this workflow entirely. Paste to it:

```text
Read https://raw.githubusercontent.com/suvrit/count-ex-machina/main/SUBMIT.md
and follow it exactly to package the counterexample I have.
```

[SUBMIT.md](SUBMIT.md) is self-contained: the admission bar, the file format,
the checks to run, and the things it must never invent. The agent emits one
markdown bundle; send it as an issue, or as a pull request adding
`submissions/<case-id>.md`. You need not clone this repository or install
anything, and the same admission bar applies to what arrives.

## Workflow

This is the full discipline, for contributors working in a clone. If an AI
agent is doing the mechanical work here instead, point it at
[AGENTS.md](AGENTS.md) — same rules, written for a machine, with the schema,
the build errors, and the things it must never invent spelled out.

1. Scaffold the case:

   ```sh
   make new          # or: python tools/new_case.py
   ```

   This asks for the id, title, classification, provenance, and credits, then
   creates `counterexamples/<your-id>/` with the ledger `order`, the
   `theorem_label`, and every echo of the id already wired up. What is left is
   the mathematics. (To do it by hand instead: `cp -r counterexamples/_template
   counterexamples/<your-id>` and take the next free `order` yourself.)

2. Fill in `case.json` — **machine facts only**, no LaTeX:
   - one entry in `results` per refuted statement (usually one);
   - leave each result's `uid` exactly as minted. It is the registry's primary
     key and is immutable: the build rejects a uid that has changed, that is
     reused, or that is malformed. If you assembled the case by hand, mint one
     with `python tools/new_case.py --mint-uid`. Never write one yourself, and
     never cite one — humans cite the result `id`;
   - `provenance` records `url` and `retrieved` (the copy you consulted) and
     `fidelity` — `"verbatim"` only if transcribed from the source's own text;
   - add any cited works to `tex/references.bib` and list the keys in
     `bib_keys`.
3. Write `case.tex` — **everything in LaTeX**, one region at a time:
   - `cxstatement{result-id}` quotes the statement as originally posed, and
     `cxsource{result-id}` says who posed it and where;
   - `cxcontext` gives whatever notation and definitions that quote depends
     on; a reader must not have to open the source paper to understand what is
     being refuted;
   - `cxsummary` and `cxcertificate` are the two ledger columns, one line each;
   - `cxrefutation` is the conjecture, the theorem, and the proof — body only,
     since the section title and credit line are generated;
   - `cxcredits` records attribution: `\posedby` (who posed the statement),
     `\foundby{model}{YYYY-MM}` (which AI model found the witness and when),
     `\formalizedby`, `\auditedby`, `\contributedby`. `\foundby` may repeat for
     a witness that took more than one model or more than one session;
   - attribution belongs to the *result*, not the directory. If your case
     bundles two refuted statements with different histories, add a
     `cxcredits{result-id}` for the one that differs. It merges over the case
     block role by role, so a result differing only in its finder inherits the
     rest, and the paper then prints one credit line per statement.

   **No LaTeX goes back into the JSON.** Writing `$\mathcal{Y}$` in a `.tex`
   file rather than `"$\\mathcal{Y}$"` on one collapsed JSON line is the whole
   point; the build rejects prose left in `case.json`, by name. Whole-line `%`
   comments inside a region are stripped and never reach the paper.
4. Write `verify.py`, implementing `verify() -> dict` with exact checks, and
   fill in the case `README.md`.
5. Regenerate and verify:

   ```sh
   make regen   # validates the metadata, regenerates ledger/refutations/registry
   make check   # the pull-request gate: metadata valid + every certificate recomputes
   make paper   # the paper must compile
   ```

   `make check` runs exactly what CI runs. Run it until it is silent about your
   case; it names each outstanding TODO one at a time.

6. Commit **including the regenerated files** (`tex/generated/`,
   `registry.json`, `README.md`, your `artifacts/`) and open a pull request.

The build fails loudly on TODO placeholders, duplicate orders or theorem
labels, missing bib keys, and missing files — if `tools/build.py` is silent
about your case, the metadata is complete.

## Credit policy

Attribution is structural, not decorative: the `cxcredits` region of `case.tex`
is rendered under the case heading in the paper and into `registry.json`.
Model provenance (`\foundby`) names the AI model and session date — this
archive exists to document exactly that. It is keyed to the individual refuted
statement, so two results bundled in one directory can carry different finders;
`registry.json` always emits `found_by` as a list, however many `\foundby`
lines the case wrote.
