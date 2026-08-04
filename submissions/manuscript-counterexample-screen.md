# Counterexample screen for arXiv:2602.05394v2

Retrieved 2026-08-04. All 47 numbered problems were checked against their
printed hypotheses and surrounding definitions. Numerical exploration was used
only to locate candidates; every packaged witness is certified with exact
integer or rational arithmetic.

## Certified refutations

| Item | Verdict | Exact obstruction | Package |
| --- | --- | --- | --- |
| Problem 3.5 | **[FALSE as written]** | The statement omits `k<n`. For the full Krylov space of the defective Jordan block `J_2`, a random starting vector is cyclic almost surely and the compression has infinite eigenvector condition number. | `krylov-defective-compression.md` |
| Problem 4.3 | **[FALSE; previously resolved]** | Chen, Liu, He, and Dong first gave an asymptotic low-coherence family. The package supplies a later independent exact $k=3,n=8$ rational-projector witness with strict pivots and a different Grassmann-chart technique. | `qrcp-orthonormal-greedy.md` |
| Problem 4.6(b) | **[FALSE; previously resolved]** | A strictly SDD positive-definite 4-by-4 witness has a nonempty-base Nyström error reduction that increases after another index is selected. Colbrook had already resolved the problem in July 2026; the packaged matrix is an independent witness and claims no priority. | `sdd-nystrom-diminishing-returns.md` |
| Problem 5.1 | **[FALSE]** | A three-atom exact OSI has injectivity 1 with failure at most 1/100, but sketch-and-solve suffers squared residual ratio 2 with probability 1/50. Townsend and Wang had already resolved the general question; the packaged distribution is an independent witness. | `osi-sketch-and-solve.md` |
| Problem 6.1 | **[FALSE as written]** | On any representable input the optimum is zero, so the requested strict inequality demands a negative squared norm. The package uses the nonzero rank-one matrix `diag(1,0)`. | `tensor-network-strict-approximation.md` |
| Section 6.2 setup | **[FALSE]** | The displayed Rayleigh-quotient identity fails for diagonal interactions `i=j`; commuting Hermitian local factors give a Hermitian Hamiltonian and exact values 0 and -4/25. | `hamiltonian-nepv-identity.md` |

## Exact failures not packaged

- **[FALSE but typographical]** Problem 3.1 reverses the preceding bound
  `(n/delta)^c` to `(delta/n)^c`. For `n=2` and `A=0`, every perturbation of
  norm at most `delta` has eigenvalue gap at most `2 delta`, contradicting the
  displayed bound for small `delta` under the implicit convention `c>0`.
  Because positivity of `c` is implicit rather than stated in the problem, no
  submission bundle was made.
- **[FALSE only under a universal reading]** Problem 3.9 uses “any” for a
  near-maximal eigenvalue. The eigenvalues `+1` and `-1` give an immediate
  contradiction at epsilon `1/2` if one output must approximate both. The
  intended existential reading is plausible, so no bundle was made.
- **[FALSE after repairing an ill-typed display]** Problem 5.2 writes a matrix
  product with incompatible dimensions. Under the evident dimensional repair,
  an exact two-dimensional OSI counterexample gives fixed approximation ratio
  `sqrt(8/5)`. Repairing the statement would violate the no-quantifier-drift
  packaging rule.
- **[FALSE under both standard interpretations, but underspecified]** Problem
  6.4 does not specify the measure, nodes, or weights behind its `ell^2` norm.
  Exact counterexamples exist for both Lebesgue `L^2` and an equally weighted
  symmetric six-node grid, but choosing either interpretation silently would
  alter the stated problem. No bundle was made.

## No validated counterexample

Problem 2.20 (the Forsythe conjecture) is the principal clean universal
conjecture in Sections 2-3; no counterexample was found. Problems 5.4-5.6 also
survived this counterexample search. Most remaining numbered items ask for an
algorithm, a complexity characterization, software, sufficient conditions, or
an explanation; they are research prompts rather than universal statements
refutable by a finite witness.

## Easy positive byproducts

- **[PROVED]** In Problem 6.5, at one composition stage,
  `epsilon_2^comp = epsilon_2^*`: every polynomial computable with two products
  has degree at most four, odd symmetrization cannot worsen uniform
  approximation to `sign` on a symmetric interval, and every odd quartic is
  `a x + b x^3`, exactly the one-stage composition class.
- **[PROVED]** The SDDM half of Problem 4.6 is true; it is an existing
  inverse-trace supermodularity result, also recorded in Colbrook's resolution.
