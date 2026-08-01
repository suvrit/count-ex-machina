# Contributing a counterexample

Contributions are welcome. The bar is deliberately high: this archive only
admits counterexamples with independently checkable certificates.

## Admission criteria

The authoritative statement is the “Admission rule and audit standard” section
of the paper (`tex/02-admission.tex`); in summary, an admissible archive
counterexample must satisfy all three conditions:

1. **Provenance of the statement.** The refuted statement is published or
   publicly posed by someone other than the discoverer of the counterexample,
   or it is a standalone formal problem explicitly posed in advance.
2. **No quantifier drift.** The original hypotheses and quantifiers are
   preserved exactly; refuting a strengthening of a statement does not count
   as refuting the statement.
3. **Independent checkability.** The witness is verifiable by exact arithmetic
   (integers, rationals, algebraic identities), a complete analytic
   calculation, or a rigorous outward-rounded interval certificate.

Certificate levels (same section): an **exact certificate** uses only exact
arithmetic end to end; a **computer-assisted proof** may use rigorous interval
arithmetic with explicit error control. Floating-point-only evidence is
inadmissible at either level.

## Workflow

1. Scaffold the case:

   ```sh
   make new          # or: python tools/new_case.py
   ```

   This asks for the id, title, classification, provenance, and credits, then
   creates `counterexamples/<your-id>/` with the ledger `order`, the
   `theorem_label`, and every echo of the id already wired up. What is left is
   the mathematics. (To do it by hand instead: `cp -r counterexamples/_template
   counterexamples/<your-id>` and take the next free `order` yourself.)

2. Fill in the rest of `case.json`:
   - one entry in `results` per refuted statement (usually one);
   - leave each result's `uid` exactly as minted. It is the registry's primary
     key and is immutable: the build rejects a uid that has changed, that is
     reused, or that is malformed. If you assembled the case by hand, mint one
     with `python tools/new_case.py --mint-uid`. Never write one yourself, and
     never cite one — humans cite the result `id`;
   - quote the statement as originally posed in `statement.tex`, and record
     where it came from in each result's `provenance` (`source_tex`, `url`,
     `retrieved`, and `fidelity` — `"verbatim"` only if transcribed from the
     source's own text). A case with several results names one file per
     result, e.g. `statement-<result-id>.tex`;
   - put whatever notation and definitions that quote depends on into
     `context.tex`; a reader must not have to open the source paper to
     understand what is being refuted;
   - **prose lives in `.tex` files, never in JSON.** `case.json` names the
     file (`"context"`, and `provenance.statement`) and the build inlines it,
     so you write `$\mathcal{Y}$` rather than `"$\\mathcal{Y}$"` on a single
     line. Whole-line `%` comments in those files are stripped and never reach
     the paper. Putting the prose back into `case.json` is a build error, not
     a silent fallback;
   - add any cited works to `tex/references.bib` and list the keys in
     `bib_keys`;
   - record attribution in `credits`: who posed the statement (`posed_by`),
     which AI model found the witness and when (`found_by`), who formalized
     the argument (`formalized_by`), who audited the certificate
     (`audited_by`), and who is submitting (`contributed_by`);
   - `found_by` may be a single `{"model", "date"}` object or a **list** of
     them, for a witness that took more than one model or more than one
     session to reach;
   - attribution belongs to the *result*, not the directory. If your case
     bundles two refuted statements with different histories, give the
     differing result its own `credits` block. It is merged over the case's
     key by key, so a result that differs only in `found_by` inherits the
     rest. The paper then prints one credit line per statement instead of one
     for the case.
3. Write `dossier.tex` (body only — the section title and credit line are
   generated) following the structure of the existing dossiers, and
   `verify.py` implementing `verify() -> dict` with exact checks.
4. Fill in the case `README.md`.
5. Regenerate and verify:

   ```sh
   make regen   # validates case.json, regenerates ledger/dossiers/registry
   make check   # the pull-request gate: metadata valid + every certificate recomputes
   make paper   # the paper must compile
   ```

   `make check` runs exactly what CI runs. Run it until it is silent about your
   case; it names each outstanding TODO one at a time.

6. Commit **including the regenerated files** (`tex/generated/`,
   `registry.json`, `README.md`, your `artifacts/`) and open a pull request.

The build fails loudly on TODO placeholders, duplicate orders or theorem
labels, missing bib keys, and missing files — if `tools/build.py` is silent
about your case, the metadata is complete.

## Credit policy

Attribution is structural, not decorative: the `credits` block of `case.json`
is rendered under the dossier heading in the paper and into `registry.json`.
Model provenance (`found_by`) names the AI model and session date — this
archive exists to document exactly that. It is keyed to the individual refuted
statement, so two results bundled in one directory can carry different finders;
`registry.json` always emits `found_by` as a list, whichever form `case.json`
used.
