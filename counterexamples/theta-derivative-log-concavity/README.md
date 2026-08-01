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

## Dossier and credits

The LaTeX dossier is `dossier.tex`; it is compiled into the main paper
(section “Counterexample dossiers”) with its title and credit line generated
from `case.json` by `tools/build.py`. Attribution roles (posed by, found by,
formalized by, audited by, contributed by) live in the `credits` block of
`case.json`. Cite via the main paper (see `/CITATION.cff`).
