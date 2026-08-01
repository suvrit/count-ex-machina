# Lorentzian Jensen-Bregman metric principle

**Status:** withheld — Log-volume midpoint gap as a squared distance: regeneration of the earlier search produced no violation and the claimed data file was absent; the standalone audit in paper.tex documents the exact triangle-inequality violation that was recovered.
**Certificate level:** exact

## Statement

A proposed Lorentzian Jensen–Bregman metric principle: that the log-volume midpoint gap defines a squared distance.

## Counterexample

Three explicit rational points whose Jensen–Bregman distances violate the triangle inequality, with an exact rational positive lower bound for the violation obtained without floating point.

## How to verify

```sh
python verify.py
```

`verify.py` raises an `AssertionError` if any exact check fails; on success it
prints a `PASS` line and (re)generates the artifacts below.

## Artifacts

- `artifacts/certificate.json` — Exact rational triangle-inequality violation bound with the three witness points.

## Write-up and credits

This case is excluded from the admitted ledger of the main paper (see
`/audit_notes.md` and the paper's “Excluded and withdrawn items” section).
A standalone write-up is `paper.tex` (self-contained; compile with
`latexmk -pdf paper`). Attribution roles live in the `credits` block of
`case.json`.
