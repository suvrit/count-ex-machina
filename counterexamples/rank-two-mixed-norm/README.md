# A rank-two completely-positive mixed-norm inequality

**Status:** refuted (ledger row 8 of the main paper)
**Certificate level:** computer-assisted

## Statement

A rank-two completely-positive mixed-norm interpolation inequality at (s, q) = (6/5, 6) — a formal problem posed by the author.

## Counterexample

An explicit 21-vector rank-two Gram matrix whose interpolation ratio exceeds 1. The Python script evaluates the ratio at 100 digits; the Sage script provides the outward-rounded interval certificate.

## How to verify

```sh
pip install -r ../../requirements.txt   # needs: mpmath
python verify.py
sage verify_mixed_norm.sage   # independent interval-arithmetic cross-check
```

`verify.py` raises an `AssertionError` if any exact check fails; on success it
prints a `PASS` line and (re)generates the artifacts below.

## Artifacts

- `artifacts/certificate.json` — Construction data of the 21-vector Gram matrix and the high-precision ratio; the Sage script provides the interval certificate.

## Dossier and credits

The LaTeX dossier is `dossier.tex`; it is compiled into the main paper
(section “Counterexample dossiers”) with its title and credit line generated
from `case.json` by `tools/build.py`. Attribution roles (posed by, found by,
formalized by, audited by, contributed by) live in the `credits` block of
`case.json`. Cite via the main paper (see `/CITATION.cff`).
