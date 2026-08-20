# Borcea–Brändén AIM problems

**Status:** refuted (ledger rows 1–4 of the main paper: Problems 35, 38, 36, 37)
**Certificate level:** exact

## Statement

Borcea and Brändén posed a family of problems on real stable polynomials (AIM
problem list). Problem 35 asks for a common-matrix mixed-determinant
representation of stable polynomials; Problem 36 asks whether a stable symmetric
polynomial with positive coefficients is Schur-positive; Problems 37 and 38 are
the two endpoint inequalities — the stable analogues of Schur's inequality and
of the Permanent-on-Top property.

## Counterexamples

*Problems 35 and 38.* A stable degree-five polynomial, given as an explicit
product of five linear forms, whose exact Schur expansion violates the POT
bounds at four partitions, refuting Problem 38; combined with a size-five
immanant obstruction it also refutes the common-matrix representation of
Problem 35.

*Problems 36 and 37.* An exact det-pencil construction whose degree-five form
has strictly positive monomial coefficients yet a negative Schur coefficient
[s₍₁⁵₎] q = −2972, verified two independent ways (Kostka inversion and
bialternant extraction). Problem 37 (the lower endpoint) gets a separate witness
from the same one-parameter family, at t = 4 rather than t = 5: it *is* Schur
positive, and still has [s₍₁⁵₎] q̃ = 69 < 125 = f^(1⁵)·[s₍₅₎] q̃. A
non-Schur-positive witness would not do, because under the problem's own
hypotheses `a_λ ≥ f^λ a_(d)` implies Schur positivity, so any counterexample to
Problem 36 refutes Problem 37 for free and says nothing more.

## How to verify

```sh
pip install -r ../../requirements.txt   # needs: sympy (for verify_pencil.py)
python verify.py
```

`verify.py` runs both certificate modules — `verify_pot.py` (Problems 35 and
38, stdlib only) and `verify_pencil.py` (Problems 36 and 37, sympy) — raises an
`AssertionError` if any exact check fails, and on success prints a `PASS` line
and (re)generates the artifacts below. Each module also runs on its own.

## Artifacts

- `artifacts/certificate-35-38.json` — Exact monomial and Schur coefficients of the stable degree-five polynomial, with the four POT-violating partitions.
- `artifacts/certificate-36-37.json` — Exact certificate of the det-pencil construction: basis, Gram data, the five integer PD matrices, and the Schur expansion with its negative coefficient.

## Write-up and credits

Everything written in LaTeX lives in `case.tex` — the title, the credits, the
context, the statements as posed, the ledger lines, and the refutations — in
`\begin{cx...}` regions that `tools/build.py` extracts into the main paper. The
section heading and the credit lines are generated; the two pairs of problems
are the case's two `\cxsubtitle` subsections. The Specht-module origin of the
pencil is developed in the paper's own appendix, `tex/04-aim36-pencil.tex`.
Attribution roles (`\posedby`, `\foundby`, `\formalizedby`, `\auditedby`,
`\contributedby`) are the `cxcredits` regions; Problems 36 and 37 carry their
own, since they were found in a later session.

Until August 2026 these four results lived in two directories,
`stable-schur` (35, 38) and `aim-problem-36` (36, 37). The result ids and uids
are unchanged.

Cite via the main paper (see `/CITATION.cff`).
