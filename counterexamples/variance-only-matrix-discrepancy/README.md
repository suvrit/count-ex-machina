# Variance-only discrepancy

**Status:** refuted (ledger row 7 of the main paper)
**Certificate level:** exact

## Statement

Whether a dimension-free variance-only bound can control matrix discrepancy without any dimension restriction — a formal problem posed by the author.

## Counterexample

The diagonal sign-cube family: every signing has discrepancy exactly n while the variance proxy stays at n, so the claimed dimension-free bound fails; all checks are exact integer arithmetic.

## How to verify

```sh
python verify.py
```

`verify.py` raises an `AssertionError` if any exact check fails; on success it
prints a `PASS` line and (re)generates the artifacts below.

## Artifacts

- `artifacts/certificate.json` — Exact discrepancy values of the diagonal sign-cube family for $n\le8$.

## Dossier and credits

The LaTeX dossier is `dossier.tex`; it is compiled into the main paper
(section “Counterexample dossiers”) with its title and credit line generated
from `case.json` by `tools/build.py`. Attribution roles (posed by, found by,
formalized by, audited by, contributed by) live in the `credits` block of
`case.json`. Cite via the main paper (see `/CITATION.cff`).
