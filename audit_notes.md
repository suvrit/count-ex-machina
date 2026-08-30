# Archive audit notes

Included: nineteen formal disproofs in fourteen case directories.

Withheld or withdrawn:
- Subgroup Johnson stability: a false target raised during an investigation, never a
  conjecture posed or published anywhere, so it fails the first admission condition.
  Removed from the archive entirely.
- The 2^n-dimensional diagonal family previously entered for variance-sensitive Matrix
  Spencer: arithmetically correct but vacuous, since it inflates the dimension to 2^n
  while the conjecture concerns n matrices of size n x n.  Withdrawn and replaced by the
  d = n family of Akbas-Sra, Theorem A.1, which refutes the conjecture in its own regime.
- Foulkes: the recovered negative plethysm used the reversed parameter range.
- The planar-zonotope route to the log-volume midpoint-gap claim: regeneration of the
  earlier search produced no violation, and the claimed data file was absent.  The claim
  itself is refuted in the `lorentzian-jensen` case via Shephard realization, so only
  the zonotope construction is withdrawn.
- Unshifted inverse inclusion-exclusion: found on Feb 16, 2026 with the GPT Pro model then
  current, but the exact n=6 and trace n=10 matrices from that session were not preserved,
  leaving only archive summaries that mentioned them.  Both witnesses were re-derived in
  August 2026 and are now admitted as `quantum-coupon-collector`, against the conjecture Sra
  posed on MathOverflow in March 2017 (question 263833) rather than against an unsourced
  summary.  The credit line reads `GPT Pro (2026-02-16)`: the February model version was
  never recorded, and no version is guessed for it.
- Loewner monotonicity of alternating log-determinants (`logdet-loewner`): the same
  alternating sum of inverses, but taken about a base point X, so a distinct statement --
  and one for which no source was ever recovered.  The case carried no quoted statement and
  no provenance; its working note recorded only the same "Feb 16, 2026; GPT-Pro" session.
  Withdrawn in favour of `quantum-coupon-collector`, which refutes a publicly posed statement
  with a permalink.  Its retired uid is 2MRX3236 and must never be reused.
- Tensor-network strict approximation (Problem 6.1 of the Simons workshop collection,
  arXiv:2602.05394v2): the item asks for a polynomial-time algorithm, not a universal claim,
  so no witness can refute it.  What the bundle exhibited is that the requested strict
  inequality demands a negative squared norm whenever the input is representable -- a `<`
  that should be a `≤`, i.e. a proofreading note on the manuscript.  The arithmetic is
  exact and correct; the item is simply not refutable.  Bundle preserved in
  `submissions/not-admitted/`.
- Krylov defective compression (Problem 3.5 of the same collection): refuted only by taking
  the full Krylov space, k = n, where Q is unitary and Q*AQ is a similarity transform of A
  rather than a compression.  The paper's Motivation, four lines below the statement, says
  "for all k < n", so the witness needs precisely the value the surrounding text excludes.
  Discarding a stated hypothesis is the mirror image of the strengthening ban in AGENTS.md
  section 8 and yields a counterexample to something nobody posed.  Bundle preserved in
  `submissions/not-admitted/`.
- Both of the above were declined in August 2026 and are the reason `SUBMIT.md` now carries
  a condition 0 (the item must be a statement, not a request) and an amendment to condition 2
  (dropping a hypothesis is quantifier drift too).  Neither was ever unpacked, so neither
  holds a uid; nothing needs retiring.
- All intermediate route-killers, sufficient-condition failures, and assistant-generated strengthenings.

Appendix placement, set in August 2026:

Five results carry `"appendix": true` and are typeset as subsections of "Additional
counterexamples" rather than as body sections.  Four are the Simons-workshop batch
(`sdd-nystrom-diminishing-returns`, `osi-sketch-and-solve`, `hamiltonian-nepv-identity`,
`qrcp-orthonormal-greedy`); two reasons, neither evidential: the statements are slight, and
three of the four were already resolved publicly by others -- Colbrook on Problem 4.6(b),
Townsend and Wang on Problem 5.1, Chen-Liu-He-Dong on Problem 4.3 -- with each dossier
crediting the prior work and claiming no priority.

The fifth is `dpp-feasible-step`, the Mariet-Sra feasible-step Picard ascent claim, moved
there in August 2026 at the maintainer's direction.  No reason beyond editorial emphasis is
recorded, and none should be inferred: the case is unchanged, its certificate still passes,
and it keeps uid 7X8N5PV5 and its place in the count.  They clear the same three admission conditions as every other case, keep their
uids, and are still counted by statement; the ledger row is collapsed to one line spanning
their four ledger numbers so the table does not spend four rows on them, and the headline
badge reports them as "additional" rather than folding them into the count.

This is presentation policy, not a fourth admission condition.  Prior art in the literature
still does not disqualify a case (see below); it is now a reason to place one in the appendix
rather than to withhold it.  `appendix` is a maintainer's disposition and never a submitter's.

Duplicates and statement identity:

`tools/build.py` enforces uniqueness only on keys the archive mints for itself --
`order`, result `id`, `uid`, `theorem_label`.  None of them identifies a *statement*, so
nothing in the build can tell that two records refute the same thing.  `provenance.url` is
the only field pointing at the statement rather than at our record of it, and it is not
unique by construction: the same claim reaches us through different copies.

Detection is a review task, performed by hand with AI assistance.  No automated duplicate
check is planned.  The cheap one -- reject two results sharing a `provenance.url` -- is
deliberately not built: it catches only the easiest kind below and would buy false
confidence about the other three.

Four kinds, and the standing disposition of each:
- Same statement, two submitters.  First admitted wins.  The second is credited in the
  case's `cxcredits`, which already accepts a repeated `\foundby` for a witness that took
  more than one model or session.  The only kind a url comparison would find.
- Same statement reached through different sources.  Already present in the archive:
  `variance-only-matrix-discrepancy` quotes Bandeira's Remark 4.25 *as restated* in
  Conjecture 1.2 of Akbas-Sra.  Two urls, one statement -- so a url check would have
  called it clean.  Only someone reading both sources catches this.
- One witness, several statements.  Not a duplicate at all, and the reason a case
  directory is not a case result: `aim-problems` refutes Problems 35 and 38 with one
  polynomial, and one Lorentzian cubic settles both `lorentzian-jensen` and
  `log-volume-distance`.  Count by statement, never by witness or by directory.
- Already refuted in the literature.  The damaging kind, since the archive would be
  claiming news that is not news.  Not detectable from anything in the repository, and not
  currently one of the three admission conditions; if it ever needs to be enforced, it
  belongs in `tex/02-admission.tex` as a fourth condition rather than in code.

Two dispositions set in August 2026, recorded here because they are precedent:
- A record that duplicates another is withdrawn rather than merged: the surviving case
  keeps its own uid, the withdrawn one has its uid retired permanently, and the reason is
  written into this file.  See `logdet-loewner` above.
- One phenomenon gets one ledger row when only one statement was actually posed.  The
  quantum coupon collector's trace consequence fails independently, at n=10, but was never
  posed anywhere on its own, so it is a second theorem inside that case's refutation rather
  than a second ledger row.  The ledger counts statements that someone posed, not theorems
  that we proved false.
