# Subgroup Johnson stability

**Status:** withheld — removed from the paper at the author's request; the exact certificate stands and `verify.py` passes.
**Certificate level:** exact

## Statement

Whether the Johnson polynomial attached to an arbitrary subgroup H ≤ S_d is always stable (no zeros in the upper half-plane) — a formal problem posed by the author.

## Counterexample

The minimal case d = 3 with H = C₃: an exact upper-half-plane zero, computed in the cyclotomic field Q(ω) with no floating point.

## How to verify

```sh
python verify.py
```

`verify.py` raises an `AssertionError` if any exact check fails; on success it
prints a `PASS` line and (re)generates the artifacts below.

## Artifacts

- `artifacts/certificate.json` — Exact vanishing certificate for the $C_3$ upper-half-plane zero.

## Dossier and credits

The LaTeX dossier is `dossier.tex`; it is compiled into the main paper
(section “Counterexample dossiers”) with its title and credit line generated
from `case.json` by `tools/build.py`. Attribution roles (posed by, found by,
formalized by, audited by, contributed by) live in the `credits` block of
`case.json`. Cite via the main paper (see `/CITATION.cff`).
