# Not admitted

Bundles that were screened, found arithmetically correct, and still kept out of
the archive. They are preserved here rather than deleted: each one records a
boundary decision, and the next contributor who packages something similar
should be able to read why it did not land.

Nothing in this directory is built, verified, counted, or cited. These are not
withheld *cases* — a withheld case is admitted into the repository with
`status: "withheld"`, a `withheld_reason`, and its own `paper.tex`. These never
became cases at all, so they have no `uid` and no ledger `order`, and none was
minted for them. See `../../audit_notes.md` for the archive-level record.

The standing reason in both instances is that the refuted item was not the kind
of thing a witness can refute, or was refuted only by discarding a hypothesis
its authors had stated a few lines away. Both are now written into
`../../SUBMIT.md` — condition 0 and the amendment to condition 2 — so that a
contributor's agent stops before packaging rather than after.

---

## `tensor-network-strict-approximation.md`

**Item.** Problem 6.1 of the Simons workshop collection
([arXiv:2602.05394v2](https://arxiv.org/abs/2602.05394v2)), §6.1, proposed
there by Mehrdad Ghadiri.

**What the bundle showed.** Problem 6.1 asks for a polynomial-time algorithm
returning `X ∈ S` with `‖X − A‖_F² < (m−1)·min_{Y∈S} ‖Y − A‖_F²`. If the input
`A` is itself representable, the minimum is `0`, so the requested strict
inequality asks for a squared norm below zero. The witness is the nonzero
rank-one matrix `diag(1,0)`. The certificate is exact and passes.

**Why it was not admitted.** Problem 6.1 is a request for an algorithm, not a
universal claim that is either true or false, so there is nothing for a witness
to refute. What the bundle actually exhibits is that a `<` should have been a
`≤` at the degenerate input — a proofreading note on the manuscript, which
belongs in a note to its authors rather than in an archive of refuted
mathematics. Publishing it as a counterexample would overstate what was found.

The screen that produced this bundle had already articulated the correct test
in its own closing section: most remaining items "ask for an algorithm, a
complexity characterization, software, sufficient conditions, or an
explanation; they are research prompts rather than universal statements
refutable by a finite witness." Problem 6.1 is such a prompt. The screen also
declined to package Problem 3.1 for a closely related reason — an implicit
positivity convention — so admitting this one would have been inconsistent with
its own standard.

---

## `krylov-defective-compression.md`

**Item.** Problem 3.5 of the same collection, §3.

**What the bundle showed.** Problem 3.5 asks whether `κ_V(Q*AQ)` is bounded by
a polynomial in `n` with high probability, for `Q` an orthonormal basis of a
Krylov space of `A` with random starting vector `b`. Taking `A` to be the
defective `2×2` Jordan block `J₂` and the *full* Krylov space (`k = n`), a
random `b` is cyclic almost surely, `Q` is unitary, `Q*AQ` is similar to `A`,
and the eigenvector condition number is infinite. The certificate is exact and
passes.

**Why it was not admitted.** The construction takes `k = n`, where `Q*AQ` is
merely a similarity transform of `A` and no compression is happening. The
paper's own Motivation, four lines below the problem statement, says "for all
`k < n`, the Rayleigh quotient `Q*AQ` is a Jordan block" — so the intended
range of `k` is stated in the surrounding text, and the witness needs exactly
the value that text excludes. The bundle's own screen conceded the point:
"The statement omits `k<n`."

Refuting a statement by discarding a hypothesis its authors stated nearby is
the mirror image of the strengthening ban in `AGENTS.md` §8. It yields a
counterexample to something nobody posed. This is a judgement about the
statement, not about the arithmetic, which is correct as far as it goes.
