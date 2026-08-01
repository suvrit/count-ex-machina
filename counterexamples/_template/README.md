# TODO Title

**Status:** TODO refuted (ledger rows appear after `tools/build.py`) | withheld
**Certificate level:** TODO exact | computer-assisted

## Statement

TODO one-paragraph plain-language summary of the conjecture, with citation.

## Counterexample

TODO one paragraph: what the witness is.

## How to verify

```sh
python verify.py
```

`verify.py` raises an `AssertionError` if any exact check fails; on success it
prints a `PASS` line and (re)generates the artifacts below.

## Artifacts

- `artifacts/certificate.json` — TODO description.

## Dossier and credits

The LaTeX dossier is `dossier.tex`; its title and credit line are generated
from `case.json` by `tools/build.py`. Attribution roles live in the `credits`
block of `case.json`. Cite via the main paper (see `/CITATION.cff`).
