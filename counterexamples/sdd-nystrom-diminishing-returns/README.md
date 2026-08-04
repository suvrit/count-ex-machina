# Strict diagonal dominance does not ensure diminishing Nyström error reductions

**Status:** refuted
**Certificate level:** exact

## Statement
Problem 4.6(b) of Amsel et al., posed there by Mark Fornace, asks whether nuclear Nyström error has diminishing reductions for a positive-definite symmetric diagonally dominant matrix. Colbrook resolved the problem negatively in July 2026; this package records an independently found exact witness and does not claim priority.

## Counterexample
An integer 4 by 4 matrix, shifted by one half of the identity, is strictly SDD and positive definite. On a nonempty selected base, its two exact marginal error reductions differ in the forbidden direction by 2165/14833896.

## How to verify
Run `python verify.py`; it uses only exact rational arithmetic, raises on any failed check, and writes the artifact.

## Artifacts
- `artifacts/certificate.json` — exact matrix, shift, SDD margins, four errors, marginal reductions, and violation gap.
