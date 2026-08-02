# Macdonald lattice Schur-convexity

**Status:** refuted (ledger row 4 of the main paper)
**Certificate level:** exact

## Statement

Theorem 2.1 of McSwiggen–Sahi asserts a lattice Schur-convexity property of normalized Macdonald polynomials.

## Counterexample

A rank-two Schur specialization that reverses the claimed inequality for every parameter 0 < r < 1; the reversal reduces to the exact identity 1 + r + r² − 3r = (1 − r)².

## How to verify

```sh
python verify.py
```

`verify.py` raises an `AssertionError` if any exact check fails; on success it
prints a `PASS` line and (re)generates the artifacts below.

## Artifacts

- `artifacts/certificate.json` — Exact rational reversal checked at sample parameters, with the algebraic identity behind the full one-parameter family.

## Prose and credits

Everything written in LaTeX lives in `case.tex` — the title, the credits, the
context, the statement as posed, the ledger lines, and the refutation — in
`\begin{cx...}` regions that `tools/build.py` extracts into the main paper. The
section title and the credit line are generated. Attribution roles (`\posedby`,
`\foundby`, `\formalizedby`, `\auditedby`, `\contributedby`) are the
`cxcredits` region.

Cite via the main paper (see `/CITATION.cff`).
