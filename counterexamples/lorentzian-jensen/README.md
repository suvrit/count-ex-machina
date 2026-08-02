# Lorentzian Jensen-Bregman metric principle

**Status:** refuted
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

The `cxrefutation` region of `case.tex` is the condensed write-up the main
paper emits; it carries both admitted statements, the metric principle and its
convex-body specialization. `paper.tex` is the self-contained long-form audit,
including the exact enclosure procedure and the parts of the earlier positive
argument that survive (compile with `latexmk -pdf paper`). Attribution roles
live in the `cxcredits` region of `case.tex`.
