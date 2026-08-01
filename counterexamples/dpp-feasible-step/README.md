# Feasible Picard steps for DPP likelihood

**Status:** refuted (ledger row 6 of the main paper)
**Certificate level:** exact

## Statement

Mariet–Sra proved that the Picard update for DPP likelihood ascends at step a = 1 and conjectured ascent for every feasible step a ≥ 1.

## Counterexample

An exact rational 2×2 kernel and training set for which the feasible step a = 5 strictly decreases the log-likelihood; the reversal is an exact comparison of two rational numbers.

## How to verify

```sh
python verify.py
```

`verify.py` raises an `AssertionError` if any exact check fails; on success it
prints a `PASS` line and (re)generates the artifacts below.

## Artifacts

- `artifacts/certificate.json` — Exact rational kernels $L_0,L_1$ and the positive rational likelihood gap.

## Dossier and credits

The LaTeX dossier is `dossier.tex`; it is compiled into the main paper
(section “Counterexample dossiers”) with its title and credit line generated
from `case.json` by `tools/build.py`. Attribution roles (posed by, found by,
formalized by, audited by, contributed by) live in the `credits` block of
`case.json`. Cite via the main paper (see `/CITATION.cff`).
