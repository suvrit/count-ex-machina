## What this changes

<!-- One or two sentences.  If this adds a counterexample, give the case id. -->

## For a new counterexample

Delete this section if the PR does not add a case.

**Admission criteria** (the authoritative statement is `tex/02-admission.tex`;
see [CONTRIBUTING.md](../CONTRIBUTING.md)):

- [ ] **Provenance.** The refuted statement was published or publicly posed by
      someone other than whoever found the counterexample, or was posed
      formally in advance.  `provenance.source_tex` and `provenance.url` record
      where, and `provenance.fidelity` is `verbatim` only if transcribed from
      the source's own text.
- [ ] **No quantifier drift.** The original hypotheses and quantifiers are
      preserved exactly.  This refutes the statement as posed, not a
      strengthening of it.
- [ ] **Independent checkability.** The witness is verified by exact arithmetic
      or a rigorous outward-rounded interval certificate.  No step of the
      verification rests on floating-point evidence.

**Mechanics:**

- [ ] `case.json` is complete, including `credits.found_by` (AI model **and**
      session date) -- the archive exists to document exactly that.
- [ ] Any cited works are in `tex/references.bib` and listed in `bib_keys`.
- [ ] `context_tex` gives whatever notation the quoted statement depends on, so
      a reader need not open the source paper.
- [ ] `python tools/build.py` regenerated the ledger, dossiers, registry, and
      README table, and those regenerated files are committed.
- [ ] `python tools/build.py --check` exits 0.
- [ ] `python tools/verify_all.py` ends with `ALL ... CASES PASS`.
- [ ] `cd tex && latexmk -pdf main` compiles.

## Notes for the reviewer

<!-- Anything about scope, an edge case, or a claim you are unsure of.
     Uncertainty stated here is far more useful than uncertainty discovered
     later. -->
