# count-ex-machina

Companion repository for the paper **“GPT: The Counterexample Machine”**
(Suvrit Sra, TU Munich). It archives AI-assisted counterexamples to published
conjectures and to formal problems posed by the author, together with
independently checkable certificates: every admitted case is verified by exact
arithmetic or by a rigorous interval computation — never by floating-point
evidence alone.

## Layout

- `counterexamples/<id>/` — one directory per counterexample: `case.json`
  (metadata + attribution), `README.md` (how to validate), `dossier.tex`
  (the paper dossier body), `verify.py` (certificate check), optional Sage
  cross-checks, and `artifacts/` (machine-readable certificates).
- `tex/` — the main paper. `tex/generated/` and `registry.json` are generated
  from the per-case `case.json` files by `tools/build.py` (checked in; do not
  edit by hand).
- `tools/` — `build.py` (validate + regenerate), `verify_all.py` (run every
  case), `exactcert.py` (shared exact-arithmetic helpers).

## Quickstart

```sh
python3 -m venv .venv && .venv/bin/pip install -r requirements.txt
.venv/bin/python tools/verify_all.py     # verify every counterexample
cd tex && latexmk -pdf main              # build the paper (compile from tex/)
```

Individual cases run standalone: `cd counterexamples/<id> && python verify.py`.
Sage cross-checks (where present) are optional and are skipped when `sage` is
not installed. Note for Overleaf: import the whole repository and set the main
document to `tex/main.tex`.

## The cases

<!-- BEGIN CASE TABLE -->
| No. | Case | Status | Class | Certificate | Found by |
|---|---|---|---|---|---|
| 1 | [aim-problem-35](counterexamples/stable-schur/) | refuted | external formal problem | exact | TODO (TODO) |
| 2 | [aim-problem-38](counterexamples/stable-schur/) | refuted | external formal problem | exact | TODO (TODO) |
| 3 | [subgroup-johnson](counterexamples/subgroup-johnson/) | refuted | user formal problem | exact | TODO (TODO) |
| 4 | [macdonald-schur-convexity](counterexamples/macdonald-schur-convexity/) | refuted | published theorem | exact | TODO (TODO) |
| 5 | [theta-derivative-log-concavity](counterexamples/theta-derivative-log-concavity/) | refuted | external conjecture | computer-assisted | TODO (TODO) |
| 6 | [dpp-feasible-step](counterexamples/dpp-feasible-step/) | refuted | published conjecture | exact | TODO (TODO) |
| 7 | [variance-only-matrix-discrepancy](counterexamples/variance-only-matrix-discrepancy/) | refuted | user formal problem | exact | TODO (TODO) |
| 8 | [rank-two-mixed-norm](counterexamples/rank-two-mixed-norm/) | refuted | user formal problem | computer-assisted | TODO (TODO) |
| 9 | [logdet-loewner](counterexamples/logdet-loewner/) | refuted | user formal problem | exact | TODO (TODO) |
| — | [aim-problem-36](counterexamples/aim-problem-36/) | withheld | external formal problem | exact | TODO (TODO) |
| — | [lorentzian-jensen](counterexamples/lorentzian-jensen/) | withheld | user formal problem | exact | TODO (TODO) |
<!-- END CASE TABLE -->

Withheld cases are documented but excluded from the paper's admitted ledger;
see `audit_notes.md` and each case's README for the reason.

## Contributing

New counterexamples are welcome once the repository is public — the admission
criteria and workflow are in [CONTRIBUTING.md](CONTRIBUTING.md). Attribution
(who posed the statement, which model found the witness, who formalized and
audited it) is recorded per case in `case.json` and rendered into the paper
automatically.
