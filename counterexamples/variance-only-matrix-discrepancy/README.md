# Variance-sensitive Matrix Spencer

**Status:** refuted
**Certificate level:** exact

## Statement

The variance-sensitive strengthening of the Matrix Spencer conjecture: that some
universal `C` gives a signing with `||sum_i x_i A_i||_op <= C ||sum_i A_i^2||_op^(1/2)`
for any `n` symmetric contractions of size `n x n`. It is Remark 4.25 of Bandeira's
[problem collection](https://people.math.ethz.ch/~abandeira/TenLecturesFortyTwoProblems.pdf)
and Conjecture 1.2 of [Akbaş–Sra](https://arxiv.org/abs/2606.16005).

## Counterexample

Theorem A.1 of Akbaş–Sra: with `n = 2^m`, a family of `n` diagonal `n x n` matrices whose
discrepancy is `(m-1)/sqrt(m)` while the variance parameter is only `1 + 1/m`, so the ratio
grows like `sqrt(log n)` and no universal `C` exists.

The dimension regime is the point. An earlier version of this entry used `n` matrices of
size `2^n x 2^n`; that is the trivial regime and says nothing about Matrix Spencer, whose
content lies in dimension comparable to the number of summands. Here `d = n`.

## How to verify

```sh
python verify.py
```

`verify.py` raises an `AssertionError` if any exact check fails; on success it
prints a `PASS` line and (re)generates the artifacts below. It enumerates all
`2^n` signings for `m = 2, 3, 4`, over several admissible choices of the free
subset `U`, and confirms the variance, the discrepancy, and the ratio identity
in exact integer and `Fraction` arithmetic.

## Artifacts

- `artifacts/certificate.json` — Exact record of the `d = n` diagonal family: the variance
  parameter, the exhaustive discrepancy minimum over all `2^n` signings, and the ratio
  identity, for each checked `m`.

## Prose and credits

Everything written in LaTeX lives in `case.tex`, in `\begin{cx...}` regions that
`tools/build.py` extracts into the main paper; the section title and credit line
are generated. The `cxcredits` region records the roles: the conjecture is
Bandeira's, the counterexample was found by GPT-5.5 (Pro) — as recorded in the
statement on LLM use in Akbaş–Sra — and formalized by Akbaş and Sra, whose
disproof this case reproduces. Cite via the main paper (see `/CITATION.cff`).
