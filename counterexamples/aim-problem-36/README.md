# AIM Problem 36: stable Schur positivity

**Status:** refuted
**Certificate level:** exact

## Statement

Borcea–Bränden AIM Problem 36: stable Schur positivity.

## Counterexample

An exact det-pencil construction whose degree-five form has strictly positive monomial coefficients yet a negative Schur coefficient [s₍₁⁵₎] q = −2972, verified two independent ways (Kostka inversion and bialternant extraction).

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

`dossier.tex` is the condensed write-up that the main paper inputs. `paper.tex`
is the self-contained long form, including the Specht-module origin of the
pencil (compile with `latexmk -pdf paper`). Attribution roles live in the
`credits` block of `case.json`.
