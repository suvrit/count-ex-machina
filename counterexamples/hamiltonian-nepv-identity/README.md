# Failure of the proposed Hamiltonian NEPv Rayleigh identity

**Status:** refuted
**Certificate level:** exact

## Statement

Immediately after equation (20), Section 6.2 of Amsel et al. asserts that its
block diagonal NEPv matrix has Rayleigh quotient equal to the product-state
objective in equation (19).

## Counterexample

With `n=2`, `d=1`, exact Hermitian norm-one matrices, and `x=(1,2)`, the
objective from equations (18)--(19) is exactly zero, while the proposed NEPv
Rayleigh quotient is exactly `-4/25`. The discrepancy occurs because an
`i=j` interaction is an expectation of a matrix product, not the product of
the two separate expectations.

## How to verify

Run `python verify.py`; it uses only exact rational arithmetic, raises on any
failed check, and writes the certificate artifact. As a mutation test, change
the upper-left entry of `K_1_1` from `0` to `1`; the exact-value assertions
fail.

## Artifacts

- `artifacts/certificate.json` — the exact matrices, vector, and unequal
  Rayleigh quotients.
