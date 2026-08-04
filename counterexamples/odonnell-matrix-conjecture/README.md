# No dimension-free constant in O'Donnell's matrix conjecture

**Status:** refuted
**Certificate level:** exact

## Statement
Answering [MathOverflow question 212711](https://mathoverflow.net/a/212759) in August 2015, Ryan O'Donnell reported that he and John Wright had been considering the problem in connection with quantum tomography, and conjectured that for unit-trace positive semidefinite `M` the distance to its own diagonal is `O(sqrt(eps))`, where `eps` is the l1 distance between the diagonal and the sorted spectrum. Equivalently: the squared trace norm of the off-diagonal part is bounded by an absolute constant times `eps`. O'Donnell also put the conjecture to Suvrit Sra in personal communication, which the public answer itself records.

## Counterexample
For every integer m at least 2, the package defines an exact algebraic density matrix of dimension n = 2^m by conjugating a rational diagonal spectrum with a sequence of exact Givens rotations. Its spectrum and diagonal are both strictly decreasing, their l1 distance is exactly 2 delta, and pinching the off-diagonal part gives a ratio greater than m/32. Hence the ratio is unbounded.

## How to verify
Run `python verify.py`; it raises on any failed check and writes the artifact. The verifier uses only integer and Fraction arithmetic, checks the scalar identities behind the Givens construction, proves the generic target gap 160*C+16, audits a finite n = 512 member, and includes a deliberate mutation test.

## Artifacts
- `artifacts/certificate.json` — exact family formulas, the symbolic unboundedness certificate, and exact rational data for the finite audit.
