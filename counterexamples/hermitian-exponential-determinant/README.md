# A determinant inequality for sums of Hermitian exponentials

**Status:** refuted
**Certificate level:** computer-assisted, using rigorous rational intervals.

## Statement

S. Sra's Conjecture 4.6, posed in 2015 while studying MathOverflow question 224121 (https://mathoverflow.net/questions/224121): for Hermitian matrices H and K of the same order, the square of the determinant of exp(H) + exp(K) is at most the determinant of exp(2H) + exp(2K) + 2 exp(H+K). The conjecture was never published, so the case sits in the paper's appendix.

## Counterexample

Use the exact integer matrices H = ((-26,10,-10),(10,-16,20),(-10,20,-26)) and K = diag(0,10,20). Both are real symmetric of order three. Dividing the two proposed sides by exp(60), the certificate proves R < 1007/1000 < 101/100 < L and L-R > 3/1000, where L is the normalized proposed left side and R the normalized proposed right side. The normalized linear coefficient of the determinant-polynomial difference is also less than -1/125. This coefficientwise strengthening is an auxiliary observation, not a second archival result. The LaTeX proof includes an analytic counterexample family explaining the failure.

## How to verify

Run `python verify.py` using Python 3.9 or later. No third-party packages, Sage, numerical libraries, or network access are needed. The script raises `AssertionError` on any failed check and writes `artifacts/certificate.json` on success. It also exposes `verify() -> dict` for the archive harness. Checks remain active under `python -O`.

Every exponential is enclosed by its rational Taylor polynomial of degree 256 and an explicit induced-infinity-norm tail bound. Interval operations use exact rational endpoints. Terminating decimals in strings are parsed as exact fractions. Compact artifact endpoints are rounded outward by integer division only. The certificate does not assume a numerical eigendecomposition or a rounded value of an eigenvalue.

Expected output: `PASS hermitian-exponential-determinant: 3x3 integer H,K; R < 1007/1000 < 101/100 < L; L-R > 3/1000; auxiliary linear coefficient < -1/125`.

## Negative control and audit

A one-entry negative control was run during packaging: change H[0][0] from -26 to 0, leaving every other entry unchanged. This still gives real symmetric integer input, but exact interval evaluation proves R > L. The verifier then raises `AssertionError: Determinant refutation not certified` before the fixed displayed-enclosure checks. Thus this is an actual broken counterexample, not merely an altered input failing an identity test.

To repeat that control without editing the file, run `python -c "import verify as v; v.H = ((0,10,-10),(10,-16,20),(-10,20,-26)); v.verify()"` in the unpacked directory. Failure is the expected outcome. This import-only test does not overwrite the valid certificate artifact.

The verifier was also checked for prohibited numerical dependencies and floating-point comparison literals.

## Artifacts

- `artifacts/certificate.json` contains the exact integer matrices, rational Taylor-error bounds, outward-rounded rational enclosures, exact displayed comparison bounds, and separating rational inequalities. It is generated, not required as a sixth bundle block.

## Attribution and scope

Posed by S. Sra (2015). Found by GPT Astra (Pro) on 2026-10-30, which also wrote the proof and the certificate; contributed by S. Sra. No independent human audit or literature priority is claimed. MathOverflow question 224121 (asked by Wolfgang, 20 November 2015, unanswered) concerns different inequalities; it is the context in which the conjecture was formulated, not its source.
