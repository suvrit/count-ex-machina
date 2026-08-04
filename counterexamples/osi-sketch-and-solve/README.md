# An oblivious subspace injection need not give relative-error sketch-and-solve

**Status:** refuted
**Certificate level:** exact

## Statement
Problem 5.1 of Amsel et al. asks whether an oblivious subspace injection with injectivity near one necessarily gives a relative-error sketch-and-solve approximation at the OSI success probability.

## Counterexample
For a one-variable least-squares problem in two dimensions, a three-atom isotropic sketch distribution is injective on every fixed line with probability at least 99/100, yet produces residual ratio square root of two with probability 1/50.

## How to verify
Run `python verify.py`; it uses only exact rational arithmetic, raises on any failed check, and writes the artifact.

## Artifacts
- `artifacts/certificate.json` — exact sketch atoms, probabilities, isotropy, OSI success bound, and residual ratios.
