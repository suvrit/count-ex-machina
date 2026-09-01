# Quantum coupon collection: positivity of an alternating sum of inverses

**Status:** refuted
**Certificate level:** exact

## Statement

For symmetric positive definite $X_1,\ldots,X_n$, let

$$Q_n(X_1,\ldots,X_n)=\sum_{k=1}^n(-1)^{k+1}\sum_{1\le i_1<\cdots<i_k\le n}(X_{i_1}+\cdots+X_{i_k})^{-1},$$

the matrix analogue of the coupon collector's expected waiting time. Sra
conjectured on [MathOverflow](https://mathoverflow.net/questions/263833/quantum-coupon-collection-positivity-of-an-alternating-sum-of-matrices)
in March 2017 that $Q_n \succ 0$ for every $n\ge1$, noting that $n\le3$ is
trivial and that $n=4$ held numerically. The question stood unanswered for
nine years.

## Counterexample

The conjecture is true for every $n\le5$ — proved here by an operator-convexity
facet-averaging argument — and false at $n=6$: six rank-one-plus-$\varepsilon I$
matrices of size three and the integer vector `(4, 1, 3)` give a quadratic form
in `(-96, -95)`.

Even the scalar consequence $\operatorname{tr} Q_n > 0$ fails: ten moment-curve
matrices in dimension three give an exact alternating trace in
`(-13901, -13900)`. The prose derives the asymptotic coefficient
`n(9-n)/(4 epsilon)` that explains why this family turns negative at ten.

## How to verify

`python verify.py` — raises on any failed check and writes the artifact. Only
Python's exact `fractions.Fraction` arithmetic is used; no float appears.

## Artifacts

- `artifacts/certificate.json` — exact witness parameters, exact rational
  numerator/denominator pairs, certified sign intervals, and the structural
  checks (positive definiteness, noncommutativity, general position).

## Provenance

Both counterexamples were found on 16 February 2026, in a session with the GPT
Pro model then current; **which version that was is not recorded**, so the
credit line says `GPT Pro` and claims no more. The exact matrices from that
session were not preserved, and were re-derived in
August 2026, which is what `verify.py` certifies. The refuted statement itself
is nine years older than either session.
