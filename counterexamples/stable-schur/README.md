# Two Borcea-Branden problems

**Status:** refuted (ledger rows 1–2 of the main paper)
**Certificate level:** exact

## Statement

Borcea and Bränden posed a family of problems on real stable polynomials (AIM problem list). Problem 35 asks for a common-matrix mixed-determinant representation of stable polynomials; Problem 38 is the stable Permanent-on-Top property.

## Counterexample

A stable degree-five polynomial, given as an explicit product of five linear forms, whose exact Schur expansion violates the POT bounds at four partitions, refuting Problem 38; combined with a size-five immanant obstruction it also refutes the common-matrix representation of Problem 35.

## How to verify

```sh
python verify.py
```

`verify.py` raises an `AssertionError` if any exact check fails; on success it
prints a `PASS` line and (re)generates the artifacts below.

## Artifacts

- `artifacts/certificate.json` — Exact monomial and Schur coefficients of the stable degree-five polynomial, with the four POT-violating partitions.

## Prose and credits

Everything written in LaTeX lives in `case.tex` — the title, the credits, the
context, the statement as posed, the ledger lines, and the refutation — in
`\begin{cx...}` regions that `tools/build.py` extracts into the main paper. The
section title and the credit line are generated. Attribution roles (`\posedby`,
`\foundby`, `\formalizedby`, `\auditedby`, `\contributedby`) are the
`cxcredits` region.

Cite via the main paper (see `/CITATION.cff`).
