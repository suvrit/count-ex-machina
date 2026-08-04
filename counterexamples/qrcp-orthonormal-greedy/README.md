# Exact QRCP can miss the orthonormal-row conditioning bound

**Status:** refuted
**Certificate level:** exact

## Statement
Problem 4.3 of Amsel et al., sourced there to Anil Damle and Daniel Kressner, asks whether practical QRCP attains the displayed bound for selecting rows from a matrix with orthonormal columns. Chen, Liu, He, and Dong first published a negative resolution in June 2026. This package records a later independent witness and claims no priority.

## Counterexample
A rational 8 by 3 Grassmann-chart matrix defines an exact rank-three orthogonal projector. Its three QRCP pivots are strict and select rows 1, 2, 3, but a rational Rayleigh certificate proves that the inverse norm of the selected 3 by 3 matrix is strictly larger than sqrt(18).

## How to verify
Run `python verify.py`; it uses only exact rational arithmetic, raises on any failed check, and writes the artifact.

## Artifacts
- `artifacts/certificate.json` — exact rational chart, projector, pivot residuals and gaps, and the Rayleigh certificate.
