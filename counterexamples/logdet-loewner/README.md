# Loewner monotonicity of alternating log-determinants

**Status:** refuted (ledger row 9 of the main paper)
**Certificate level:** exact

## Statement

Loewner monotonicity of the alternating log-determinant inclusion–exclusion form — a formal problem posed by the author.

## Counterexample

Five explicit rational 3×3 positive-definite matrices and a rational test vector on which the alternating sum of inverses is not positive semidefinite: vᵀCv < 0 exactly.

## How to verify

```sh
python verify.py
```

`verify.py` raises an `AssertionError` if any exact check fails; on success it
prints a `PASS` line and (re)generates the artifacts below.

## Artifacts

- `artifacts/certificate.json` — Exact rational matrices $X,A_1,\ldots,A_4$, the test vector, and the negative value of the quadratic form.

## Dossier and credits

The LaTeX dossier is `dossier.tex`; it is compiled into the main paper
(section “Counterexample dossiers”) with its title and credit line generated
from `case.json` by `tools/build.py`. Attribution roles (posed by, found by,
formalized by, audited by, contributed by) live in the `credits` block of
`case.json`. Cite via the main paper (see `/CITATION.cff`).
