# Commuting counterexamples to determinantal entropy concavity

**Status:** refuted
**Certificate level:** computer-assisted

## Statement

Russell Lyons, "Determinantal probability: basic properties and conjectures," Proceedings of the International Congress of Mathematicians 2014, volume IV, pages 137–161, Conjecture 2.6, equation (2.14), section 2.3, page 141, conjectures midpoint concavity of exact-set Shannon entropy for positive-contraction determinantal kernels. The source explicitly permits complex Hilbert spaces. Consulted source: https://rdlyons.pages.iu.edu/pdf/icm-pub.pdf (retrieved 2026-10-30). The same inequality was first posed as Conjecture 9.2, equation (9.1), of Lyons, "Determinantal probability measures," Publ. Math. IHES 98 (2003), 167–212.

## Counterexample

Use the five-point unitary Fourier matrix, indexed 0 through 4, as a common eigenbasis. The two exact spectra are (11,9,9991,9990,9989)/10000 and (9,11,9989,9990,9991)/10000. The commuting kernels are strictly between zero and identity. Their occupation distributions are identical, but each endpoint entropy exceeds the midpoint entropy by more than 1/5000000000. The proof in case.tex also establishes an analytic positive-curvature limit, without computation.

## How to verify

Run `python verify.py`; it raises on any failed check, prints a PASS line, and writes `artifacts/certificate.json`. Python's standard library suffices. All probability arithmetic is exact over the rational numbers with the square root of five adjoined. Logarithms use rigorous rational series bounds and outward rounding. No floating-point comparison establishes the result.

The verifier checks strict admissibility, exact normalization, evenness, the finite entropy gap, and positive curvature. The required negative-control test was performed on a separate copy: changing the first direction entry from 1 to 2 raises AssertionError. The original verifier was left unchanged. The bundle was also unpacked and the extracted verifier was run independently of its working-directory original.

The source statement, nearby hypotheses, bibliography, and scope were checked independently.

## Artifacts

- `artifacts/certificate.json` — exact spectra, square-root bounds, outward rational entropy and curvature intervals, and exact occupation-probability coefficients.

## Attribution and scope

Found by GPT Astra (Pro) on 2026-10-30; formalized and audited by OpenAI Codex; contributed by Suvrit Sra. No external human audit or literature priority is claimed. One prior-work lead remains unassessed: a publicly indexed LinkedIn listing (https://www.linkedin.com/in/lianxin-h-74b30626) titled "On Concavity of the Entropy of Determinantal Point Processes", dated 10 May 2012. Neither the listing nor any work by that title could be retrieved, and its authorship, contents, and relation to this counterexample are unknown. The separate beam-splitter consequence is not registered as a second published conjecture.
