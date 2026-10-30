Maintainer note: **Draft, not admission-ready.** The original source of the supplied Conjecture 4.6 crop and its surrounding hypotheses have not been identified; source metadata remain TODO. The discovery-session model identifier and contributor credit also need confirmation. The exact certificate and a one-entry negative control were run successfully. Do not infer published attribution, priority, or completed admission review from this draft.

```json file=case.json
{
  "id": "hermitian-exponential-determinant",
  "title": "A determinant inequality for sums of Hermitian exponentials",
  "status": "refuted",
  "prose": "case.tex",
  "bib_keys": [
    "ZouPeng2016"
  ],
  "results": [
    {
      "id": "hermitian-exponential-determinant",
      "uid": null,
      "class": "external conjecture",
      "certificate_level": "computer-assisted",
      "theorem_label": "thm:hermitian-exponential-determinant",
      "provenance": {
        "url": "TODO",
        "retrieved": "TODO",
        "fidelity": "paraphrase"
      }
    }
  ],
  "verify": {
    "python": "verify.py",
    "sage": [],
    "requires": []
  },
  "artifacts": [
    {
      "file": "artifacts/certificate.json",
      "description": "Integer witness, rational Taylor-error bounds, outward-rounded rational enclosures, and strict separating inequalities."
    }
  ]
}
```

```latex file=case.tex
\cxtitle{A determinant inequality for sums of Hermitian exponentials}
\begin{cxcredits}
\posedby{TODO: identify the document containing the supplied Conjecture~4.6 and its attribution}
\foundby{ChatGPT (TODO: confirm the exact discovery-session model identifier)}{2026-10}
\formalizedby{ChatGPT, in the present conversation: written proof and Python certificate}
\auditedby{ChatGPT: exact-arithmetic rerun, code review, and a one-entry negative control on 2026-10-30; no independent human audit claimed}
\contributedby{TODO: contributor's preferred name or attribution}
\end{cxcredits}

\begin{cxcontext}
All matrices in a comparison have the same finite order. A Hermitian matrix
satisfies $H=H^*$, where $*$ denotes conjugate transpose, and $e^H$ is the
usual matrix exponential. The notation $\det(e^H+e^K)^2$ means the square
of the determinant, equivalently $\det((e^H+e^K)^2)$, not an entrywise square.
For Hermitian $H,K$, set
\[
 A=e^H,\qquad B=e^K,\qquad E=e^{H+K},\qquad D=B^{-1}=e^{-K}.
\]
These exponentials are positive definite. Products such as $DA$ need not
be Hermitian; the determinant identities used below do not require them to be.
\end{cxcontext}

\begin{cxsource}{hermitian-exponential-determinant}
The user supplied an image headed ``Conjecture 4.6'' at
2026-10-30 07:10:34 UTC, before the counterexample was constructed in this
conversation. The crop says ``Let $H,K$ be Hermitian. Then,'' followed by
exactly the displayed inequality restated below. No document title, author,
page, section heading, URL, publication date, or surrounding paragraphs were
provided. TODO: locate and open the original source, establish its prior
public appearance or prior formal record, verify the surrounding hypotheses,
and replace the unresolved provenance URL and retrieval date. The provisional
class is external conjecture, not published conjecture. The statement is
marked as a paraphrase because the complete original document has not been
consulted. This dossier is not yet admission-ready.

A bounded web literature check on 2026-10-30 did not identify a prior
resolution of precisely this displayed inequality. It did locate
Zou and Peng's Theorem~2.1 and equation~(2.4) in \cite{ZouPeng2016}, a different
inequality with a Kubo--Ando geometric mean in place of the mixed exponential.
That theorem is not a resolution of the present assertion. Without identifying
the original source, the priority check remains incomplete; no novelty or
priority is claimed here.
\end{cxsource}

\begin{cxstatement}{hermitian-exponential-determinant}
For Hermitian matrices $H,K$ of the same order,
\[
 \det(e^H+e^K)^2
 \leq \det\bigl(e^{2H}+e^{2K}+2e^{H+K}\bigr).
\]
\end{cxstatement}

\begin{cxsummary}{hermitian-exponential-determinant}
A proposed determinant inequality comparing sums of Hermitian exponentials.
\end{cxsummary}

\begin{cxcertificate}{hermitian-exponential-determinant}
Integer $3\times3$ symmetric inputs; exact rational Taylor intervals certify normalized right side $<1007/1000<101/100<$ normalized left side.
\end{cxcertificate}

\begin{cxrefutation}
Only the universal assertion visible in the supplied crop is asserted to be
refuted here; its identification with a particular published statement awaits
the source check described above.

\begin{theorem}[\statusfalse: Hermitian exponential determinant comparison]\label{thm:hermitian-exponential-determinant}
The assertion in Problem~\ref{ctx:hermitian-exponential-determinant} is false
already for real symmetric $3\times3$ matrices.
\end{theorem}
\begin{proof}
Take the exact integer matrices
\[
 H=\begin{pmatrix}
 -26&10&-10\\
 10&-16&20\\
 -10&20&-26
 \end{pmatrix},
 \qquad
 K=\begin{pmatrix}
 0&0&0\\
 0&10&0\\
 0&0&20
 \end{pmatrix}.
\]
Both are real symmetric, hence Hermitian, of the same order. Define
\[
 L=\frac{\det(A+B)^2}{\det(B)^2},\qquad
 R=\frac{\det(A^2+B^2+2E)}{\det(B)^2}.
\]
Here $\det(B)^2=e^{2\operatorname{tr}K}=e^{60}>0$, so the proposed
inequality is equivalent to $L\leq R$. Left multiplication and congruence,
respectively, give the exact identities
\[
 L=\det(I+DA)^2,\qquad
 R=\det(I+DA^2D+2DED).
\]
The supplied verifier certifies
\begin{align*}
 1.0106259614312670597488454657
 &<L<1.0106259614312670597488454658,\\
 1.0066369661468304923537507020
 &<R<1.0066369661468304923537507021.
\end{align*}
Every terminating decimal in these strict bounds denotes an exact rational
number, not a rounded estimate. In particular,
\[
 R<\frac{1007}{1000}<\frac{101}{100}<L,
 \qquad L-R>\frac{3}{1000}.
\]
This reverses the claimed comparison.

For completeness, here is the error control behind the certificate.
For a rational matrix $X$ put
\[
 r=\|X\|_\infty=\max_i\sum_j|X_{ij}|,
 \qquad T_m(X)=\sum_{j=0}^{m}\frac{X^j}{j!}.
\]
Submultiplicativity and the power-series definition imply
\[
 \|e^X-T_m(X)\|_\infty
 \leq\sum_{j=m+1}^{\infty}\frac{r^j}{j!}
 \leq\frac{r^{m+1}}{(m+1)!}\,
       \frac{1}{1-r/(m+2)}
 =:\varepsilon_m(r),\qquad r<m+2.
\]
The last bound is a geometric-series bound: after the first omitted term,
each successive ratio is at most $r/(m+2)$. Therefore every entry of $e^X$
lies in the rational interval
$[(T_m(X))_{ij}-\varepsilon_m(r),
  (T_m(X))_{ij}+\varepsilon_m(r)]$.

The verifier takes $m=256$. The required norms are
$\|H\|_\infty=56$, $\|H+K\|_\infty=46$, and $0,10,20$ for the three
scalar exponents forming $D$. Each is strictly below $258$.
The off-diagonal entries of $D$ are exactly zero. Rational interval addition,
subtraction, and multiplication propagate these enclosures through the two
normalized determinant expressions, using the six-term determinant formula
in order three. Before squaring the left determinant interval, its strict
positivity is certified. Interval endpoints and every inequality test use
integers and \texttt{fractions.Fraction}; there is no unbounded truncation
error and no machine-precision comparison. All displayed enclosing bounds
and the strict separation above are checked, not merely printed.
\end{proof}

\begin{remark}[The linear coefficient and the suggested normalization]
The coefficientwise strengthening arose during this conversation, so it is
recorded only as an auxiliary observation, not as a second archival result.
For fixed $A,B,E$, let
\[
 \Delta(t)=\det(B^2+2tE+t^2A^2)-\det(B+tA)^2.
\]
Jacobi's determinant differentiation formula at $t=0$ gives
\[
 \frac{[t]\Delta(t)}{\det(B)^2}
 =2\bigl(\operatorname{tr}(B^{-2}E)
          -\operatorname{tr}(B^{-1}A)\bigr)
 =2\bigl(\operatorname{tr}(DED)-\operatorname{tr}(DA)\bigr).
\]
For the same exact witness, the verifier certifies that this number $c_1$
satisfies
\[
 -0.0081120478335667666163258676
 <c_1<
 -0.0081120478335667666163258675
 <-\frac1{125}<0.
\]
Thus even the linear coefficient has the wrong sign.

This is also the obstruction exposed by the user's suggested log-determinant
normalization. Put $S_t=B^2+t^2A^2$. Since
$(B+tA)^2=S_t+t(AB+BA)$, cancellation of $\det S_t$ gives, for $t$ near zero,
\begin{align*}
 F(t)
 &=\operatorname{tr}\log\bigl(I+2tS_t^{-1/2}ES_t^{-1/2}\bigr)\\
 &\quad-\operatorname{tr}\log\bigl(I+tS_t^{-1/2}(AB+BA)S_t^{-1/2}\bigr)\\
 &=c_1t+O(t^2).
\end{align*}
The logarithms are defined in a neighborhood of zero by positivity and
continuity. The expansion is used to explain the discovery, not as a
substitute for the exact certificate at $t=1$.
\end{remark}

\begin{remark}[An analytic family explaining the failure]
A separate limiting construction explains why counterexamples exist.
Set
\[
 M=\begin{pmatrix}0&1&-1\\1&1&2\\-1&2&0\end{pmatrix},
 \qquad N=\operatorname{diag}(0,1,2),
 \qquad \lambda=\lambda_{\max}(M).
\]
The unit vector $v=(0,1,1)^T/\sqrt2$ has $v^TMv=5/2$, so
$\lambda\geq5/2>2$. No eigenvector of $M$ can have first coordinate zero: writing its eigenvalue
as $\mu$, the first row would give $u_2=u_3$, and the second and third rows
would then give simultaneously $\mu u_2=3u_2$ and $\mu u_2=2u_2$.
This would force the entire vector to vanish. Consequently each eigenspace
is one-dimensional (otherwise a linear combination would have first
coordinate zero). Let $P=uu^T$ be the rank-one top spectral projection,
with $\|u\|=1$, and put $Q=e_1e_1^T$, $\alpha=|u_1|^2>0$.

For $r>0$ define
\[
 H_r=r(M-\lambda I),\quad K_r=rN,\quad
 A_r=e^{H_r},\quad B_r=e^{K_r},\quad
 D_r=B_r^{-1},\quad E_r=e^{H_r+K_r}.
\]
Then $A_r\longrightarrow P$ and $D_r\longrightarrow Q$. The matrix
$T=M+N$ has characteristic polynomial $(x-4)(x^2-2)$ and top unit
eigenvector $v$. Since this vector has zero first coordinate,
\begin{align*}
 \|D_rE_rD_r\|_2
 &\leq e^{(\sqrt2-\lambda)r}
       +e^{(4-\lambda)r}\|D_rv\|^2\\
 &=e^{(\sqrt2-\lambda)r}
   +\tfrac12 e^{(2-\lambda)r}
   +\tfrac12 e^{-\lambda r}
 \longrightarrow0.
\end{align*}
Here $\|\cdot\|_2$ is the operator norm. The contribution from the two
remaining eigenspaces is bounded by $e^{(\sqrt2-\lambda)r}$, since
$\|D_r\|_2=1$.

It follows that, coefficientwise as polynomials in $t$,
\begin{align*}
 \frac{\det(B_r^2+2tE_r+t^2A_r^2)}{\det(B_r)^2}
 &=\det(I+2tD_rE_rD_r+t^2D_rA_r^2D_r)
 \longrightarrow1+\alpha t^2,\\
 \frac{\det(B_r+tA_r)^2}{\det(B_r)^2}
 &=\det(I+tD_rA_r)^2
 \longrightarrow(1+\alpha t)^2.
\end{align*}
Coefficientwise convergence follows because these coefficients are polynomial
functions of the converging matrix entries. The normalized difference tends to
\[
 -2\alpha t+\alpha(1-\alpha)t^2.
\]
At $t=1$ its limit is $-\alpha(1+\alpha)<0$, so the original inequality
fails for all sufficiently large $r$. Its linear coefficient tends to
$-2\alpha<0$. This analytic explanation is not needed to validate the fixed
integer witness above; in particular, no numerical value of $\lambda$ enters
the executable certificate.
\end{remark}

\begin{remark}[Scope]
The certified conclusion concerns the displayed universal assertion for
same-order Hermitian matrices, with the direction $\leq$ and with the term
$2e^{H+K}$ unchanged. The supplied witness satisfies every hypothesis visible
in the crop. The full original document and its surrounding assumptions
remain TODO; this dossier must not be represented as a verified refutation
of a specifically attributed published result until that check is completed.

Commuting pairs satisfy equality, and this case does not dispute that fact.
No claim is made that dimension three is minimal, nor is the dimension-two
case resolved here. The geometric-mean theorem of \cite{ZouPeng2016} is not
refuted: with $P,Q$ positive definite and
$P\#Q=P^{1/2}(P^{-1/2}QP^{-1/2})^{1/2}P^{1/2}$, it states
\[
 \det(P^{1/2}+Q^{1/2})^2\leq\det(P+Q+2(P\#Q)).
\]
For $P=e^{2H}$ and $Q=e^{2K}$, its geometric mean is not generally
$e^{H+K}$. The negative coefficient above is auxiliary, not a separately
provenanced claim. No novelty or priority is asserted.
\end{remark}
\end{cxrefutation}
```

```python file=verify.py
#!/usr/bin/env python3
"""Certify a 3-by-3 Hermitian exponential determinant counterexample.

All arithmetic that decides a check is integral or fractions.Fraction.
Matrix exponentials use rational Taylor sums and a proved norm-tail bound.
The result is a rigorous interval certificate, not a numerical approximation.
"""
from __future__ import annotations

import json
import pathlib
from dataclasses import dataclass
from fractions import Fraction as F

CASE_ID = "hermitian-exponential-determinant"
DEGREE = 256
H = ((-26, 10, -10), (10, -16, 20), (-10, 20, -26))
K = ((0, 0, 0), (0, 10, 0), (0, 0, 20))

# Decimal strings below denote exact rational numbers, not machine decimals.
CLAIMED_BOUNDS = {
    "normalized_lhs": (
        "1.0106259614312670597488454657",
        "1.0106259614312670597488454658",
    ),
    "normalized_rhs": (
        "1.0066369661468304923537507020",
        "1.0066369661468304923537507021",
    ),
    "normalized_linear_coefficient": (
        "-0.0081120478335667666163258676",
        "-0.0081120478335667666163258675",
    ),
}


def require(condition: bool, message: str) -> None:
    """Checks remain active even when Python is invoked with -O."""
    if not condition:
        raise AssertionError(message)


@dataclass(frozen=True)
class Interval:
    lo: F
    hi: F

    def __post_init__(self):
        require(isinstance(self.lo, F) and isinstance(self.hi, F),
                "Interval endpoints must be Fractions")
        require(self.lo <= self.hi, "Reversed interval")

    def __add__(self, other):
        if not isinstance(other, Interval):
            other = point(other)
        return Interval(self.lo + other.lo, self.hi + other.hi)

    __radd__ = __add__

    def __neg__(self):
        return Interval(-self.hi, -self.lo)

    def __sub__(self, other):
        if not isinstance(other, Interval):
            other = point(other)
        return self + (-other)

    def __mul__(self, other):
        if not isinstance(other, Interval):
            other = point(other)
        products = (self.lo * other.lo, self.lo * other.hi,
                    self.hi * other.lo, self.hi * other.hi)
        return Interval(min(products), max(products))

    __rmul__ = __mul__


def rational(x):
    require(isinstance(x, (int, str, F)), "Non-rational input")
    return F(x)


def point(x):
    x = rational(x)
    return Interval(x, x)


def shape(A):
    require(len(A) > 0 and len(A[0]) > 0, "Empty matrix")
    require(all(len(row) == len(A[0]) for row in A), "Ragged matrix")
    return len(A), len(A[0])


def identity(n, constructor=F):
    return [[constructor(int(i == j)) for j in range(n)] for i in range(n)]


def add(A, B):
    require(shape(A) == shape(B), "Addition dimension mismatch")
    return [[a + b for a, b in zip(ar, br)] for ar, br in zip(A, B)]


def scale(A, s):
    return [[s * a for a in row] for row in A]


def matmul(A, B):
    n, k = shape(A)
    k2, m = shape(B)
    require(k == k2, "Multiplication dimension mismatch")
    return [[sum(A[i][h] * B[h][j] for h in range(k))
             for j in range(m)] for i in range(n)]


def trace(A):
    n, m = shape(A)
    require(n == m, "Trace requires a square matrix")
    return sum(A[i][i] for i in range(n))


def det3(A):
    require(shape(A) == (3, 3), "This determinant formula is for size 3")
    return (A[0][0] * (A[1][1] * A[2][2] - A[1][2] * A[2][1])
            - A[0][1] * (A[1][0] * A[2][2] - A[1][2] * A[2][0])
            + A[0][2] * (A[1][0] * A[2][1] - A[1][1] * A[2][0]))


def infinity_norm(M):
    return max(sum(abs(rational(x)) for x in row) for row in M)


def factorial(n):
    require(isinstance(n, int) and n >= 0, "Invalid factorial argument")
    out = 1
    for k in range(2, n + 1):
        out *= k
    return out


def tail_bound(r, degree=DEGREE):
    r = rational(r)
    require(isinstance(degree, int) and degree >= 0, "Invalid Taylor degree")
    require(0 <= r < degree + 2, "Taylor degree too small for tail bound")
    return (r ** (degree + 1) / factorial(degree + 1)
            / (1 - r / (degree + 2)))


def exp_enclosure(M, degree=DEGREE):
    """Enclose exp(M) entrywise by exact rational intervals.

    For r = ||M||_infinity < degree+2, consecutive omitted scalar terms
    have ratio at most r/(degree+2). Submultiplicativity bounds the
    matrix-norm tail by r**(degree+1)/(degree+1)!/(1-r/(degree+2)).
    Each entry is therefore enclosed by the Taylor sum +/- that bound.
    """
    n, m = shape(M)
    require(n == m, "Exponential requires a square matrix")
    M = [[rational(x) for x in row] for row in M]
    error = tail_bound(infinity_norm(M), degree)
    term = identity(n)
    total = identity(n)
    for k in range(1, degree + 1):
        term = scale(matmul(term, M), F(1, k))
        total = add(total, term)
    return [[Interval(x - error, x + error) for x in row] for row in total]


def evaluate(H0, K0):
    """Return enclosures for the two normalized sides and linear coefficient."""
    require(shape(H0) == shape(K0) == (3, 3), "Witness must have size 3")
    for name, M in (("H", H0), ("K", K0)):
        require(all(isinstance(x, int) for row in M for x in row),
                name + " must have integer entries")
        require(all(M[i][j] == M[j][i] for i in range(3) for j in range(3)),
                name + " must be real symmetric, hence Hermitian")
    require(all(K0[i][j] == 0 for i in range(3) for j in range(3) if i != j),
            "The diagonal exponential shortcut requires diagonal K")

    A = exp_enclosure(H0)
    E = exp_enclosure(add(H0, K0))
    D = [[point(0) for _ in range(3)] for _ in range(3)]
    for i in range(3):
        # Read the diagonal from K0, never from a duplicate list of constants.
        D[i][i] = exp_enclosure([[-K0[i][i]]])[0][0]
    I = identity(3, point)
    DA = matmul(D, A)
    lhs_det = det3(add(I, DA))
    require(lhs_det.lo > 0, "Could not certify positive left determinant")
    lhs = Interval(lhs_det.lo ** 2, lhs_det.hi ** 2)
    DED = matmul(matmul(D, E), D)
    DA2D = matmul(matmul(DA, A), D)
    rhs = det3(add(add(I, DA2D), scale(DED, 2)))
    linear = 2 * (trace(DED) - trace(DA))
    return {
        "normalized_lhs": lhs,
        "normalized_rhs": rhs,
        "normalized_linear_coefficient": linear,
    }


def enclosing_rationals(x, digits=45):
    """Compact artifact bounds, rounded OUTWARD using integer division only."""
    den = 10 ** digits
    lo = F((x.lo.numerator * den) // x.lo.denominator, den)
    hi = F(-((-x.hi.numerator * den) // x.hi.denominator), den)
    require(lo <= x.lo <= x.hi <= hi, "Invalid outward rounding")
    return {"lower": str(lo), "upper": str(hi)}


def verify() -> dict:
    """Raise AssertionError on any failed check; return a machine-readable summary."""
    values = evaluate(H, K)
    lhs, rhs = values["normalized_lhs"], values["normalized_rhs"]
    linear = values["normalized_linear_coefficient"]
    require(rhs.lo > 0, "Could not certify positive right determinant")
    require(rhs.hi < lhs.lo, "Determinant refutation not certified")
    require(linear.hi < 0, "Negative auxiliary linear coefficient not certified")
    for name, interval in values.items():
        lower, upper = map(F, CLAIMED_BOUNDS[name])
        require(lower < interval.lo <= interval.hi < upper,
                "Displayed enclosure not certified: " + name)

    # These are deliberately simple, independently readable exact bounds.
    require(rhs.hi < F(1007, 1000) < F(101, 100) < lhs.lo,
            "Simple separating rational bounds failed")
    require(lhs.lo - rhs.hi > F(3, 1000), "Gap lower bound failed")
    require(linear.hi < -F(8, 1000), "Linear-coefficient upper bound failed")

    HK = add(H, K)
    norms = {"H": infinity_norm(H), "H_plus_K": infinity_norm(HK)}
    for i in range(3):
        norms["minus_K_diagonal_" + str(i + 1)] = abs(F(K[i][i]))
    witness = {
        "H": [list(row) for row in H],
        "K": [list(row) for row in K],
        "dimension": 3,
        "normalizing_factor": f"exp(-2*trace(K)) = exp({-2 * trace(K)})",
        "taylor_degree": DEGREE,
        "tail_formula": "r^(degree+1)/(degree+1)!/(1-r/(degree+2))",
        "tail_data": {name: {"infinity_norm": str(r),
                              "absolute_entrywise_error_bound": str(tail_bound(r))}
                      for name, r in norms.items()},
        "normalized_enclosures_outward_rounded": {
            name: enclosing_rationals(x) for name, x in values.items()},
        "displayed_strict_bounds_exact_decimal_strings": CLAIMED_BOUNDS,
        "simple_exact_separation": "R < 1007/1000 < 101/100 < L",
        "normalized_L_minus_R_strict_lower_bound": "3/1000",
        "normalized_linear_coefficient_strict_upper_bound": "-1/125",
        "auxiliary_coefficient_status": "Not a separately sourced archival result",
    }
    return {
        "id": CASE_ID,
        "ok": True,
        "summary": "3x3 integer H,K; R < 1007/1000 < 101/100 < L; "
                   "L-R > 3/1000; auxiliary linear coefficient < -1/125",
        "witness": witness,
    }


if __name__ == "__main__":
    out = verify()
    art = pathlib.Path(__file__).resolve().parent / "artifacts"
    art.mkdir(exist_ok=True)
    (art / "certificate.json").write_text(
        json.dumps(out["witness"], indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )
    print(f"PASS {out['id']}: {out['summary']}")
```

```markdown file=README.md
# A determinant inequality for sums of Hermitian exponentials

**Status:** refuted (the universal assertion visible in the supplied crop).
**Certificate level:** computer-assisted, using rigorous rational intervals.
**Submission readiness:** draft; original-source provenance and attribution are unresolved.

## Statement

The user-supplied image headed “Conjecture 4.6” asserts that, for Hermitian matrices H and K of the same order, the square of the determinant of exp(H) + exp(K) is at most the determinant of exp(2H) + exp(2K) + 2 exp(H+K). The original document citation is **TODO**. Its surrounding hypotheses have not been checked. Zou and Peng (2016), *Some trace inequalities for matrix means*, Theorem 2.1 and equation (2.4), prove a different geometric-mean inequality; that paper is cited only for scope, not as the source of this conjecture.

## Counterexample

Use the exact integer matrices H = ((-26,10,-10),(10,-16,20),(-10,20,-26)) and K = diag(0,10,20). Both are real symmetric of order three. Dividing the two proposed sides by exp(60), the certificate proves R < 1007/1000 < 101/100 < L and L-R > 3/1000, where L is the normalized proposed left side and R the normalized proposed right side. The normalized linear coefficient of the determinant-polynomial difference is also less than -1/125. This coefficientwise strengthening was considered during the discovery conversation and is an auxiliary observation, not a second archival result. The LaTeX proof includes an analytic counterexample family explaining the failure.

## How to verify

Run `python verify.py` using Python 3.9 or later. No third-party packages, Sage, numerical libraries, or network access are needed. The script raises `AssertionError` on any failed check and writes `artifacts/certificate.json` on success. It also exposes `verify() -> dict` for the archive harness. Checks remain active under `python -O`.

Every exponential is enclosed by its rational Taylor polynomial of degree 256 and an explicit induced-infinity-norm tail bound. Interval operations use exact rational endpoints. Terminating decimals in strings are parsed as exact fractions. Compact artifact endpoints are rounded outward by integer division only. The certificate does not assume a numerical eigendecomposition or a rounded value of an eigenvalue.

Expected output: `PASS hermitian-exponential-determinant: 3x3 integer H,K; R < 1007/1000 < 101/100 < L; L-R > 3/1000; auxiliary linear coefficient < -1/125`.

## Negative control and audit

A one-entry negative control was run during packaging: change H[0][0] from -26 to 0, leaving every other entry unchanged. This still gives real symmetric integer input, but exact interval evaluation proves R > L. The verifier then raises `AssertionError: Determinant refutation not certified` before the fixed displayed-enclosure checks. Thus this is an actual broken counterexample, not merely an altered input failing an identity test.

To repeat that control without editing the file, run `python -c "import verify as v; v.H = ((0,10,-10),(10,-16,20),(-10,20,-26)); v.verify()"` in the unpacked directory. Failure is the expected outcome. This import-only test does not overwrite the valid certificate artifact.

The verifier was also checked for prohibited numerical dependencies and floating-point comparison literals. The five bundle blocks, JSON syntax, result identifiers, bibliography keys, and LaTeX region boundaries were checked locally. These checks are not a claim that the archive's complete build or admission review has passed. The unresolved source TODOs deliberately prevent that claim.

## Artifacts

- `artifacts/certificate.json` contains the exact integer matrices, rational Taylor-error bounds, outward-rounded rational enclosures, exact displayed comparison bounds, and separating rational inequalities. It is generated, not required as a sixth bundle block.

## Provenance and priority limits

The screenshot was supplied in the conversation at 2026-10-30 07:10:34 UTC, before the counterexample was constructed. This records the order of events in the conversation, but by itself does not establish when or where the conjecture was previously published or formally recorded. It does not reveal surrounding assumptions. No public source for the exact Conjecture 4.6 was identified in the bounded search performed while preparing this draft.

That search did not identify a previous resolution of exactly the displayed inequality, but the original source remains unlocated, so the literature check is necessarily incomplete. No novelty or priority is claimed. The related Zou-Peng paper was opened and its title, authors, theorem, equation, date, and DOI were checked. It does not supply the missing original provenance.

## TODOs before admission

1. Identify and open the original source of Conjecture 4.6; supply its URL, bibliographic details, prior-publication or prior-formal-record evidence, section/page, and surrounding hypotheses. Replace `results[0].provenance.url` and `results[0].provenance.retrieved` in `case.json`, the posed-by credit, and the source notes in `case.tex`. Recheck the provisional `external conjecture` class and `paraphrase` fidelity against that document. The retrieval date is TODO because the original document has not been retrieved; it is not silently replaced by the screenshot receipt date.
2. Confirm the exact model identifier for the ChatGPT session that found the counterexample on 2026-10-30; the known discovery month is 2026-10.
3. Supply the contributor's preferred public name or attribution. No individual is inferred from the repository owner or the user's location.

The proof and certificate were written and checked by ChatGPT in this conversation. No independent human audit, proof-assistant formalization, repository submission, maintainer approval, or admission-ready status is claimed.
```

```bibtex file=references.bib.add
@article{ZouPeng2016,
  author  = {Zou, Limin and Peng, Yang},
  title   = {Some trace inequalities for matrix means},
  journal = {Journal of Inequalities and Applications},
  volume  = {2016},
  eid     = {283},
  year    = {2016},
  doi     = {10.1186/s13660-016-1236-4},
  url     = {https://link.springer.com/article/10.1186/s13660-016-1236-4},
  note    = {Article 283; Theorem 2.1 and equation (2.4). Consulted 2026-10-30.}
}
```
