# AIM Problem 36: stable Schur positivity

**Status:** refuted
**Certificate level:** exact

## Statement

Borcea–Bränden AIM Problem 36: stable Schur positivity.

## Counterexample

An exact det-pencil construction whose degree-five form has strictly positive monomial coefficients yet a negative Schur coefficient [s₍₁⁵₎] q = −2972, verified two independent ways (Kostka inversion and bialternant extraction).

Problem 37 (the lower endpoint) gets a separate witness from the same
one-parameter family, at t = 4 rather than t = 5: it *is* Schur positive, and
still has [s₍₁⁵₎] q̃ = 69 < 125 = f^(1⁵)·[s₍₅₎] q̃. A non-Schur-positive witness
would not do, because under the problem's own hypotheses `a_λ ≥ f^λ a_(d)`
implies Schur positivity, so any counterexample to Problem 36 refutes Problem 37
for free and says nothing more.

## How to verify

```sh
pip install -r ../../requirements.txt   # needs: sympy
python verify.py
```

`verify.py` raises an `AssertionError` if any exact check fails; on success it
prints a `PASS` line and (re)generates the artifacts below.

## Artifacts

- `artifacts/certificate.json` — Exact certificate of the det-pencil construction: basis, Gram data, the five integer PD matrices, and the Schur expansion with its negative coefficient.

## Write-up and credits

The `cxrefutation` region of `case.tex` is the write-up the main paper emits;
the rest of `case.tex` holds the title, credits, context, and the statements as
posed. The Specht-module origin of the pencil is developed in the paper's own
appendix, `tex/04-aim36-pencil.tex`; this case carries no separate write-up.
Attribution roles live in the `cxcredits` region.
