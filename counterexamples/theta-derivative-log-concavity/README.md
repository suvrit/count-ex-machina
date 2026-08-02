# Derivatives of the Jacobi-theta kernel

**Status:** refuted (ledger row 5 of the main paper)
**Certificate level:** computer-assisted

## Statement

Coffey–Csordas Conjecture 2.5 (equivalently Csordas Problem 4.13) on the log-concavity of the derivative sequence of the Jacobi theta kernel.

## Counterexample

The quantity J₉(1/50) = Φ₉² − Φ₈Φ₁₀ is negative. The Python script reconstructs it at 100 digits; the Sage script certifies the sign with outward-rounded interval arithmetic and a rigorous tail bound.

## How to verify

```sh
pip install -r ../../requirements.txt   # needs: mpmath
python verify.py
sage verify_theta.sage   # independent interval-arithmetic cross-check
```

`verify.py` raises an `AssertionError` if any exact check fails; on success it
prints a `PASS` line and (re)generates the artifacts below.

## Artifacts

- `artifacts/certificate.json` — High-precision value of $J_9(1/50)$; the Sage script provides the outward-rounded interval certificate.

## Prose and credits

Everything written in LaTeX lives in `case.tex` — the title, the credits, the
context, the statement as posed, the ledger lines, and the refutation — in
`\begin{cx...}` regions that `tools/build.py` extracts into the main paper. The
section title and the credit line are generated. Attribution roles (`\posedby`,
`\foundby`, `\formalizedby`, `\auditedby`, `\contributedby`) are the
`cxcredits` region.

Cite via the main paper (see `/CITATION.cff`).
