Maintainer notes: the exact model identifier and contributor name remain TODO. Assessment of the inaccessible 2012 prior-work lead disclosed in case.tex also remains TODO; no priority is claimed. All required mathematical and packaging checks pass. An additional LaTeX compile attempt was blocked by missing local TeX format files and packages.

```json file=case.json
{
  "id": "lyons-dpp-entropy-concavity",
  "title": "Commuting counterexamples to determinantal entropy concavity",
  "status": "refuted",
  "prose": "case.tex",
  "bib_keys": ["Lyons2014DPP"],
  "results": [
    {
      "id": "lyons-dpp-entropy-concavity",
      "uid": null,
      "class": "published conjecture",
      "certificate_level": "computer-assisted",
      "theorem_label": "thm:lyons-dpp-entropy-concavity",
      "provenance": {
        "url": "https://rdlyons.pages.iu.edu/pdf/icm-pub.pdf",
        "retrieved": "2026-10-30",
        "fidelity": "verbatim"
      }
    }
  ],
  "verify": {"python": "verify.py", "sage": [], "requires": []},
  "artifacts": [
    {
      "file": "artifacts/certificate.json",
      "description": "Exact spectra, occupation probability coefficients, and outward rational intervals certifying the entropy midpoint violation and positive curvature."
    }
  ]
}
```

```latex file=case.tex
\cxtitle{Commuting counterexamples to determinantal entropy concavity}

\begin{cxcredits}
\posedby{Russell Lyons \citeyearpar{Lyons2014DPP}}
\foundby{Codex (GPT-6 family; exact model identifier TODO)}{2026-10}
\formalizedby{Codex research agents in the discovery session}
\auditedby{Independent Codex research agents; no external human audit recorded}
\contributedby{TODO: contributor name}
\end{cxcredits}

\begin{cxcontext}
Fix a finite coordinate set $E$. A positive contraction $Q$ is a self-adjoint
operator on the real or complex Hilbert space $\ell^2(E)$ satisfying
$0\preceq Q\preceq I$. Its determinantal law $\mathbf P^Q$ is defined by
$\mathbf P^Q[A\subseteq X]=\det Q_{A,A}$ for every $A\subseteq E$.
The entropy in the statement is the Shannon entropy of the entire occupied
set, with the coordinate basis fixed:
\[
 \operatorname{Ent}(Q)
 =-\sum_{S\subseteq E}\mathbf P^Q(\{S\})\log\mathbf P^Q(\{S\}),
 \qquad 0\log0=0.
\]
We use natural logarithms. Write $H(Q)=\operatorname{Ent}(Q)$ below. For the
coordinate projection $P_{S^c}$, the exact-set convention is
\[
 p_S(Q):=\mathbf P^Q(\{S\})
 =(-1)^{|S^c|}\det(Q-P_{S^c}).
\]
This is not the entropy of the particle count and not the sum of binary
entropies of the eigenvalues.
\end{cxcontext}

\begin{cxsource}{lyons-dpp-entropy-concavity}
Russell Lyons, \cite{Lyons2014DPP}, Conjecture~2.6, equation~(2.14),
Section~2.3, printed page~141 (page~5 of the consulted published PDF).
The finite-set entropy definition immediately precedes the conjecture.
Section~2.1, page~138, explicitly permits real or complex Hilbert spaces;
Section~2.3, page~140, defines positive contractions as self-adjoint operators
between zero and identity. Thus complex Hermitian kernels are within the
stated domain. Commutativity is an additional property of our witness, not a
hypothesis imposed on the source statement.

The conjecture and its surrounding context were opened and checked on
2026-10-30. A bounded prior-work search did not establish priority for this
counterexample; no priority is claimed. The author's published survey and
the author-linked errata were inspected. The auxiliary beam-splitter
inequality discussed below is not attributed to Lyons and is not entered as
a second independently sourced conjecture.

An unresolved search lead is a publicly indexed listing titled
\emph{On Concavity of the Entropy of Determinantal Point Processes}, dated
10 May 2012, at \url{https://www.linkedin.com/in/lianxin-h-74b30626}.
Direct retrieval of the listing failed and the underlying work was not
obtained. Its authorship, publication status, contents, and relation to this
counterexample remain unverified: TODO, assess this prior-work lead.
This is a disclosure of an unchecked lead, not a citation asserting a prior
resolution or a verified bibliographic entry.
\end{cxsource}

\begin{cxstatement}{lyons-dpp-entropy-concavity}
For all positive contractions $Q_1$ and $Q_2$, we have
\[
 \operatorname{Ent}\bigl((Q_1+Q_2)/2\bigr)
 \ge \bigl(\operatorname{Ent}(Q_1)+\operatorname{Ent}(Q_2)\bigr)/2.
\]
\end{cxstatement}

\begin{cxsummary}{lyons-dpp-entropy-concavity}
The exact-set Shannon entropy of a determinantal law is midpoint concave in its positive-contraction kernel.
\end{cxsummary}

\begin{cxcertificate}{lyons-dpp-entropy-concavity}
Commuting $5\times5$ Hermitian kernels with rational spectra; rigorous rational logarithm bounds certify an entropy midpoint deficit exceeding $1/5{,}000{,}000{,}000$.
\end{cxcertificate}

\begin{cxrefutation}
The entropy conjecture of \cite{Lyons2014DPP} fails along a commuting affine
family. The matrices have an exact Fourier eigenbasis and rational spectra;
all squared minors needed for their occupation probabilities lie in
$\mathbb Q(\sqrt5)$.

\begin{theorem}[\statusfalse: determinantal entropy concavity]\label{thm:lyons-dpp-entropy-concavity}
Let $E=\{0,1,2,3,4\}$, let
\[
 \omega=e^{2\pi i/5},\qquad F_{jk}=5^{-1/2}\omega^{jk}
 \quad(0\le j,k\le4),
\]
and set
\[
 \lambda_+=\frac1{10000}(11,9,9991,9990,9989),\qquad
 \lambda_-=\frac1{10000}(9,11,9989,9990,9991),\qquad
 K_\pm=F\operatorname{diag}(\lambda_\pm)F^*.
\]
These are commuting Hermitian strict positive contractions, but
\[
 H(K_+)=H(K_-),\qquad
 H(K_+)-H\left(\frac{K_++K_-}{2}\right)
 >\frac1{5{,}000{,}000{,}000}>0.
\]
In particular Conjecture~2.6 of \cite{Lyons2014DPP} is false as stated.
\end{theorem}
\begin{proof}
All displayed spectral entries are exact rational numbers. Because $F$ is
unitary, the two matrices commute, and their eigenvalues are strictly between
zero and one. Introduce the family
\[
 \lambda_\varepsilon(t)=
 (\varepsilon+t,\varepsilon-t,1-\varepsilon+t,
  1-\varepsilon,1-\varepsilon-t),\qquad
 K_\varepsilon(t)=F\operatorname{diag}(\lambda_\varepsilon(t))F^*.
\]
The theorem uses $\varepsilon=1/1000$ and $t=\pm1/10000$.
For every $0<\varepsilon<1/2$ and $|t|<\varepsilon$, the entire family
consists of commuting strict positive contractions.

For $J\subseteq E$ put
\[
 q_J(\lambda)=\prod_{j\in J}\lambda_j\prod_{j\notin J}(1-\lambda_j),
 \qquad M(S,J)=|\det F_{S,J}|^2.
\]
The exact-set probabilities satisfy
\begin{equation}\label{eq:lyons-dpp-spectral-probability}
 p_S(F\operatorname{diag}(\lambda)F^*)
 =\sum_{J:\,|J|=|S|}M(S,J)q_J(\lambda).
\end{equation}
Indeed the inclusion convention gives the probability generating polynomial
$\det(I-K+KZ)$, with $Z=\operatorname{diag}(z_i)$. Conjugating by $F$ and
expanding in the rows of $I-\operatorname{diag}(\lambda)$ and
$\operatorname{diag}(\lambda)F^*ZF$ gives
$\sum_Jq_J(\lambda)\det((F^*ZF)_{J,J})$. Cauchy--Binet expands the latter
minor as $\sum_{|S|=|J|}M(S,J)\prod_{i\in S}z_i$; comparison of coefficients
proves \eqref{eq:lyons-dpp-spectral-probability}.

Write $s=\sqrt5$. Squared Fourier minors of sizes zero and five equal one;
those of sizes one and four equal $1/5$. For two-element sets
$S=\{a,b\}$ and $J=\{c,d\}$,
\[
 M(S,J)=\frac{|\omega^{ac+bd}-\omega^{ad+bc}|^2}{25}
 =\begin{cases}
 (5-s)/50,&(b-a)(d-c)\equiv\pm1\pmod5,\\
 (5+s)/50,&(b-a)(d-c)\equiv\pm2\pmod5.
 \end{cases}
\]
The size-three values are the complementary size-two values, by the
complementary-minor identity for a unitary matrix. Thus every $p_S$ is an
explicit polynomial in $\varepsilon,t$ with coefficients in
$\mathbb Q(\sqrt5)$.

Let $R$ permute eigenmodes by $j\mapsto1-j\pmod5$. It fixes
$\lambda_\varepsilon(0)$ and reverses the direction $(1,-1,1,0,-1)$.
Since $FR=D\overline F$, where $D_{jj}=\omega^j$, we have
\[
 K_\varepsilon(-t)=D\overline{K_\varepsilon(t)}D^*.
\]
Complex conjugation and diagonal unitary conjugation preserve each exact-set
probability. Hence every $p_S(\varepsilon,t)$ is even in $t$, proving the
equality of the endpoint distributions and entropies.

It remains to establish the strictly positive finite entropy difference.
The accompanying \texttt{verify.py} evaluates
\eqref{eq:lyons-dpp-spectral-probability} with exact rational coefficients
and encloses all logarithms by rational bounds. It computes the eigenvalues
at both endpoints and checks strict admissibility, polynomial normalization,
and coefficientwise evenness. Its enclosure $[L,U]$ for
$H(K_+)-H((K_++K_-)/2)$ satisfies the exact assertions
\[
 L>\frac1{5{,}000{,}000{,}000}>0,
 \qquad
 L\le H(K_+)-H\left(\frac{K_++K_-}{2}\right)\le U.
\]
Here is the complete error-control method used by that finite computation.
With $D_0=10^{40}$ and $r=\lfloor\sqrt{5D_0^2}\rfloor$, integer square
root gives
\[
 r/D_0<\sqrt5<(r+1)/D_0.
\]
After exact power-of-two range reduction, logarithms of positive rational
endpoints reduce to arguments $1\le x\le2$. For
$z=(x-1)/(x+1)$ and $N=40$,
\[
 \log x=2\sum_{k=0}^{N-1}\frac{z^{2k+1}}{2k+1}+R_N,\qquad
 0\le R_N\le\frac{2z^{2N+1}}{(2N+1)(1-z^2)}.
\]
The series follows by integrating the geometric series; the tail bound
replaces each omitted denominator by $2N+1$. Algebraic arguments are
enclosed using the bounds on $\sqrt5$, and logarithms by monotonicity.
Interval multiplication uses the minimum and maximum of all four endpoint
products. Endpoints are rounded outward, using integer floor and ceiling,
to a grid of denominator $10^{32}$. These operations preserve containment
at each step. Every calculation and decisive inequality uses integers or
\texttt{fractions.Fraction}; no floating-point evidence is used. This proves
the stated finite inequality.
\end{proof}

There is also a complete analytic existence proof for the same family,
independent of executing the certificate. It explains the sign of the
curvature near a rank-three projection.

\begin{proposition}
For the family above,
\[
 \lim_{\varepsilon\downarrow0}
 \left.\frac{d^2}{dt^2}H(K_\varepsilon(t))\right|_{t=0}
 =2\log\frac{15}{44}
  +\frac2{\sqrt5}\log\frac{147+65\sqrt5}{22}>0.
\]
\end{proposition}
\begin{proof}
The kernel is circulant, so translating $S$ preserves its probability. For
the eight translation classes write
\[
 p_S(\varepsilon,0)=c_S\varepsilon^{m_S}(1+O(\varepsilon)),\qquad
 \partial_t^2p_S(\varepsilon,0)=d_S+O(\varepsilon).
\]
The Fourier-minor formula gives the following table; the last column is per
individual outcome, before multiplication by the class size.
\[
\begin{array}{c|r|r|c|c}
 S&\text{class size}&m_S&c_S&d_S\\\hline
 \varnothing&1&3&1&0\\
 \{0\}&5&2&3/5&-2/5\\
 \{0,1\}&5&1&(15-s)/50&(10-2s)/25\\
 \{0,2\}&5&1&(15+s)/50&(10+2s)/25\\
 \{0,1,2\}&5&0&(5-s)/50&(-10+6s)/25\\
 \{0,1,3\}&5&0&(5+s)/50&(-10-6s)/25\\
 \{0,1,2,3\}&5&1&2/5&4/5\\
 E&1&2&1&-2
\end{array}
\]
For completeness, the leading latent set at $\varepsilon=t=0$ is
$J_0=\{2,3,4\}$. The leading singleton contributions are its three
singletons, giving $3/5$. The leading pair contributions are
$\{2,3\},\{2,4\},\{3,4\}$, whose squared minors sum to
$(15\mp s)/50$. The leading triple contribution is $J_0$ itself. The two
leading four-point sets add either 0 or 1 to $J_0$, giving $2/5$.
The empty and full probabilities at $t=0$ are
$\varepsilon^3(1-\varepsilon)^2$ and
$\varepsilon^2(1-\varepsilon)^3$. These facts verify $m_S,c_S$.

To check $d_S$ directly, the only nonzero values of
$\partial_t^2q_J(\lambda_\varepsilon(t))$ at $\varepsilon=t=0$ are
\[
\begin{array}{c|r@{\qquad}c|r}
 J&q_J''&J&q_J''\\\hline
 \{3\}&-2&\{2,3\}&2\\
 \{3,4\}&2&\{0,2,3\}&2\\
 \{1,2,3\}&-2&\{0,3,4\}&-2\\
 \{1,3,4\}&2&\{2,3,4\}&-4\\
 \{0,2,3,4\}&2&\{1,2,3,4\}&2\\
 E&-2&&
\end{array}
\]
These are obtained by differentiating the five-factor products defining
$q_J$. Multiplication by the squared Fourier minors and summation gives
the displayed $d_S$ values. Polynomial dependence supplies all stated
error terms.

At every positive $\varepsilon$, all probabilities are positive, so entropy
is smooth. Evenness gives $p_S'(\varepsilon,0)=0$, and normalization gives
$\sum_Sp_S''=0$. Therefore
\[
 H_\varepsilon''(0)=-\sum_Sp_S''(\varepsilon,0)\log p_S(\varepsilon,0).
\]
The potential $\log\varepsilon$ terms cancel, because
$\sum_Sm_Sd_S=-4+4+4-4=0$; all errors are
$O(\varepsilon\log\varepsilon)$ or smaller and vanish. Put
$a=(5-s)/50$, $b=(5+s)/50$, $c=(15-s)/50$, $d=(15+s)/50$. The finite limit is
\begin{align*}
 C={}&2\log(3/5)-4\log(2/5)\\
 &-\tfrac25\bigl[(5-s)\log c+(5+s)\log d\bigr]
 +\tfrac25\bigl[(5-3s)\log a+(5+3s)\log b\bigr]\\
 ={}&2\log(15/44)+\tfrac2s\log\bigl((147+65s)/22\bigr),
\end{align*}
using $ab=1/125$, $cd=11/125$, and
$(c/d)(b/a)^3=(147+65s)/22$. Since
$15/44>1/3$, $(147+65\sqrt5)/22>13$, and $2/\sqrt5>8/9$,
\[
 C>\tfrac89\log13-2\log3
 =\tfrac29\log(28561/19683)>0.
\]
The second and third inequalities follow from $11/5<\sqrt5<9/4$.
Thus positive curvature occurs at interior kernels for every sufficiently
small positive $\varepsilon$. No boundary derivative of entropy is used.
\end{proof}

\begin{remark}[Scope]
The finite witness refutes the source's midpoint inequality itself, with
its original hypotheses and quantifiers intact. It also refutes full
concavity, even on a commuting affine family. It does not establish the
least possible dimension or settle the real-symmetric restriction.
It concerns finite exact-set Shannon entropy; it does not refute concavity
of particle-count entropy, spectral entropy, or any statement about entropy
rates of infinite stationary processes.

As a consequence, the auxiliary balanced beam-splitter inequality from the
discovery discussion also fails for this pair. For
\[
 W=\frac1{\sqrt2}\begin{pmatrix}I&I\\-I&I\end{pmatrix},\qquad
 Q=W(K_+\oplus K_-)W^*,\qquad \bar K=(K_++K_-)/2,
\]
both output coordinate marginals have kernel $\bar K$. Subadditivity yields
$H(Q)\le2H(\bar K)<H(K_+)+H(K_-)$, with output-minus-input gap strictly
less than $-1/2{,}500{,}000{,}000$. This is a corollary, not a second
provenance claim or an attribution of that auxiliary statement to Lyons.
\end{remark}
\end{cxrefutation}
```

```python file=verify.py
#!/usr/bin/env python3
"""Certify a commuting five-dimensional counterexample to DPP entropy concavity.

All calculations that establish the refutation use integers, Fraction, or
the exact field Q(sqrt(5)). Logarithms have rigorous rational enclosures.
There are no third-party dependencies.

The unitary is U[a,b] = exp(2*pi*i*a*b/5)/sqrt(5), with indices 0,...,4.
For K(t) = U diag(SPECTRUM + t*DIRECTION) U*, its exact occupation law is

  p_S(t) = sum_{|J|=|S|} |det U[S,J]|^2
             product_{j in J} lambda_j(t)
             product_{j not in J} (1-lambda_j(t)).

This is the spectral DPP sampling identity, obtained by Cauchy--Binet.
The squared Fourier minors are computed exactly below. Thus no approximate
matrix entries or approximate determinants enter this certificate.
"""

from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction as F
from math import isqrt
import json
import pathlib


# Explicit witness inputs. These are deliberately exposed for mutation tests.
SPECTRUM = (F(1, 1000), F(1, 1000), F(999, 1000),
            F(999, 1000), F(999, 1000))
DIRECTION = (F(1), F(-1), F(1), F(0), F(-1))
STEP = F(1, 10000)
CASE_ID = "lyons-dpp-entropy-concavity"

DIMENSION = 5
STATES = tuple(tuple(i for i in range(DIMENSION) if mask & (1 << i))
               for mask in range(1 << DIMENSION))
ROUND_DENOMINATOR = 10 ** 32
ROOT_DENOMINATOR = 10 ** 40
LOG_TERMS = 40


@dataclass(frozen=True)
class Quadratic:
    """The exact algebraic number a + b*sqrt(5)."""

    a: F = F(0)
    b: F = F(0)

    def __add__(self, other: Quadratic) -> Quadratic:
        return Quadratic(self.a + other.a, self.b + other.b)

    def scale(self, scalar: F) -> Quadratic:
        return Quadratic(self.a * scalar, self.b * scalar)

    def is_zero(self) -> bool:
        return self.a == 0 and self.b == 0

    def as_strings(self) -> list[str]:
        return [str(self.a), str(self.b)]


Interval = tuple[F, F]


def enclose(lower: F, upper: F) -> Interval:
    """Round outward to a fixed rational grid, never inward."""
    assert lower <= upper
    denominator = ROUND_DENOMINATOR
    lower_integer = (lower.numerator * denominator) // lower.denominator
    upper_integer = -((-upper.numerator * denominator) // upper.denominator)
    return F(lower_integer, denominator), F(upper_integer, denominator)


def interval_add(x: Interval, y: Interval) -> Interval:
    return enclose(x[0] + y[0], x[1] + y[1])


def interval_negate(x: Interval) -> Interval:
    return -x[1], -x[0]


def interval_multiply(x: Interval, y: Interval) -> Interval:
    products = tuple(a * b for a in x for b in y)
    return enclose(min(products), max(products))


def quadratic_interval(x: Quadratic, root_interval: Interval) -> Interval:
    lo, hi = root_interval
    if x.b < 0:
        lo, hi = hi, lo
    return enclose(x.a + x.b * lo, x.a + x.b * hi)


def unit_log(x: F) -> Interval:
    """Enclose log(x) for 1 <= x <= 2 using an explicit positive tail.

    Put z=(x-1)/(x+1), so 0 <= z <= 1/3. The identity

      log(x) = 2 sum_{k>=0} z^(2k+1)/(2k+1)

    follows by integrating the geometric series for 2/(1-z*z).
    After LOG_TERMS terms the omitted positive tail is at most

      2*z^(2*LOG_TERMS+1) / ((2*LOG_TERMS+1)*(1-z*z)),

    because every omitted denominator is at least 2*LOG_TERMS+1.
    Both the partial sum and this bound are exact rational numbers.
    """
    assert F(1) <= x <= F(2)
    z = (x - 1) / (x + 1)
    total = F(0)
    power = z
    for k in range(LOG_TERMS):
        total += power / (2 * k + 1)
        power *= z * z
    tail = 2 * power / ((2 * LOG_TERMS + 1) * (1 - z * z))
    return enclose(2 * total, 2 * total + tail)


def rational_log(x: F, log_two: Interval) -> Interval:
    """Enclose log(x) by exact power-of-two range reduction."""
    assert x > 0
    y, exponent = x, 0
    while y < 1:
        y *= 2
        exponent -= 1
    while y > 2:
        y /= 2
        exponent += 1
    shift = interval_multiply((F(exponent), F(exponent)), log_two)
    return interval_add(unit_log(y), shift)


def interval_log(x: Interval, log_two: Interval) -> Interval:
    assert x[0] > 0
    # The logarithm is increasing, so endpoint enclosures suffice.
    lower = rational_log(x[0], log_two)[0]
    upper = rational_log(x[1], log_two)[1]
    return enclose(lower, upper)


def fourier_channel(observed: tuple[int, ...],
                    spectral: tuple[int, ...]) -> Quadratic:
    """Compute |det U[observed,spectral]|^2 exactly in Q(sqrt(5)).

    Empty and full minors have squared modulus 1; single-entry minors have
    squared modulus 1/5. Complementary-minor identities for a unitary give
    the sizes four and three from sizes one and two. For two-element sets,
    with d equal to the product of their index differences modulo five,

      |det U[S,J]|^2 = (2 - 2*cos(2*pi*d/5))/25
                    = (5 - sqrt(5))/50, if d = 1 or 4,
                    = (5 + sqrt(5))/50, if d = 2 or 3.
    """
    size = len(observed)
    if size != len(spectral):
        return Quadratic()
    if size in (0, 5):
        return Quadratic(F(1))
    if size in (1, 4):
        return Quadratic(F(1, 5))
    if size == 3:
        observed = tuple(i for i in range(5) if i not in observed)
        spectral = tuple(i for i in range(5) if i not in spectral)
    difference = ((observed[1] - observed[0])
                  * (spectral[1] - spectral[0])) % 5
    assert difference in (1, 2, 3, 4)
    sign = -1 if difference in (1, 4) else 1
    return Quadratic(F(1, 10), F(sign, 50))


def polynomial_multiply(p: list[F], q: list[F]) -> list[F]:
    result = [F(0)] * (len(p) + len(q) - 1)
    for i, a in enumerate(p):
        for j, b in enumerate(q):
            result[i + j] += a * b
    return result


def probability_polynomials() -> list[list[Quadratic]]:
    spectral_weights = []
    for spectral in STATES:
        weight = [F(1)]
        for i, (eigenvalue, velocity) in enumerate(zip(SPECTRUM, DIRECTION)):
            factor = ([eigenvalue, velocity] if i in spectral
                      else [1 - eigenvalue, -velocity])
            weight = polynomial_multiply(weight, factor)
        spectral_weights.append(weight)

    channel = [[fourier_channel(s, j) for j in STATES] for s in STATES]
    # Independently check exact normalization of the Fourier channel.
    for row in channel:
        assert sum(row, Quadratic()) == Quadratic(F(1))
    for column in zip(*channel):
        assert sum(column, Quadratic()) == Quadratic(F(1))

    result = []
    for row in channel:
        coefficients = [Quadratic() for _ in range(DIMENSION + 1)]
        for transition, weight in zip(row, spectral_weights):
            for degree, coefficient in enumerate(weight):
                coefficients[degree] = (coefficients[degree]
                                        + transition.scale(coefficient))
        result.append(coefficients)
    return result


def evaluate(polynomial: list[Quadratic], t: F) -> Quadratic:
    result = Quadratic()
    for coefficient in reversed(polynomial):
        result = result.scale(t) + coefficient
    return result


def entropy(polynomials: list[list[Quadratic]], t: F,
            root_interval: Interval, log_two: Interval) -> Interval:
    result = (F(0), F(0))
    for polynomial in polynomials:
        probability = quadratic_interval(evaluate(polynomial, t), root_interval)
        assert 0 < probability[0] <= probability[1] < 1
        term = interval_multiply(probability, interval_log(probability, log_two))
        result = interval_add(result, interval_negate(term))
    return result


def interval_strings(interval: Interval) -> dict[str, str]:
    return {"lower": str(interval[0]), "upper": str(interval[1])}


def verify() -> dict:
    """Raise AssertionError on failure; return an exact machine-readable witness."""
    assert len(SPECTRUM) == len(DIRECTION) == DIMENSION
    assert STEP > 0
    spectra = tuple(tuple(a + t * b for a, b in zip(SPECTRUM, DIRECTION))
                    for t in (-STEP, F(0), STEP))
    assert all(0 < eigenvalue < 1 for spectrum in spectra for eigenvalue in spectrum)
    assert all((spectra[0][i] + spectra[2][i]) / 2 == spectra[1][i]
               for i in range(DIMENSION))
    # The three kernels have these spectra in the SAME Fourier basis;
    # hence they are Hermitian, strictly between zero and I, and commute.

    root_integer = isqrt(5 * ROOT_DENOMINATOR * ROOT_DENOMINATOR)
    root_interval = (F(root_integer, ROOT_DENOMINATOR),
                     F(root_integer + 1, ROOT_DENOMINATOR))
    assert root_interval[0] ** 2 < 5 < root_interval[1] ** 2
    log_two = unit_log(F(2))
    polynomials = probability_polynomials()

    # Check total mass as a polynomial, and evenness coefficient by coefficient.
    for degree in range(DIMENSION + 1):
        total = sum((p[degree] for p in polynomials), Quadratic())
        assert total == Quadratic(F(1 if degree == 0 else 0))
    assert all(p[degree].is_zero() for p in polynomials for degree in (1, 3, 5))
    assert all(evaluate(p, STEP) == evaluate(p, -STEP) for p in polynomials)

    h_minus = entropy(polynomials, -STEP, root_interval, log_two)
    h_midpoint = entropy(polynomials, F(0), root_interval, log_two)
    h_plus = entropy(polynomials, STEP, root_interval, log_two)
    assert h_minus == h_plus
    gap = interval_add(h_plus, interval_negate(h_midpoint))
    # This strictly positive exact bound refutes midpoint concavity itself.
    assert gap[0] > F(1, 5000000000)

    # Independent local certificate: p'_S(0)=0, so H''=-sum p''_S log(p_S).
    curvature = (F(0), F(0))
    orbit_classes: dict[tuple[F, F, F, F], int] = {}
    for polynomial in polynomials:
        p_zero = quadratic_interval(polynomial[0], root_interval)
        p_second_exact = polynomial[2].scale(F(2))
        p_second = quadratic_interval(p_second_exact, root_interval)
        term = interval_multiply(p_second, interval_log(p_zero, log_two))
        curvature = interval_add(curvature, interval_negate(term))
        key = (polynomial[0].a, polynomial[0].b,
               p_second_exact.a, p_second_exact.b)
        orbit_classes[key] = orbit_classes.get(key, 0) + 1
    assert F(271, 5000) < curvature[0] <= curvature[1] < F(543, 10000)

    witness = {
        "dimension": DIMENSION,
        "unitary": "U[a,b]=exp(2*pi*i*a*b/5)/sqrt(5), indices a,b=0,...,4",
        "spectrum_at_midpoint": [str(x) for x in SPECTRUM],
        "direction": [str(x) for x in DIRECTION],
        "step": str(STEP),
        "spectrum_minus": [str(x) for x in spectra[0]],
        "spectrum_plus": [str(x) for x in spectra[2]],
        "strict_positive_contractions": True,
        "common_eigenbasis_and_commuting": True,
        "exact_probability_normalization": True,
        "exact_even_probability_polynomials": True,
        "entropy_minus_equals_entropy_plus": True,
        "entropy_midpoint_interval": interval_strings(h_midpoint),
        "entropy_endpoint_interval": interval_strings(h_plus),
        "endpoint_minus_midpoint_interval": interval_strings(gap),
        "strict_gap_lower_bound": "1/5000000000",
        "curvature_interval": interval_strings(curvature),
        "simpler_curvature_bounds": ["271/5000", "543/10000"],
        "sqrt_five_interval": interval_strings(root_interval),
        "log_series_terms": LOG_TERMS,
        "outward_rounding_denominator": str(ROUND_DENOMINATOR),
        "probability_orbit_classes": [
            {"multiplicity": count,
             "p_at_zero_as_a_plus_b_sqrt_five": [str(key[0]), str(key[1])],
             "p_second_as_a_plus_b_sqrt_five": [str(key[2]), str(key[3])]}
            for key, count in orbit_classes.items()
        ],
    }
    return {
        "id": CASE_ID,
        "ok": True,
        "summary": ("Commuting strict positive contractions of dimension 5 have "
                    "endpoint entropy minus midpoint entropy > 1/5000000000; "
                    "all bounds are exact rational enclosures."),
        "witness": witness,
    }


if __name__ == "__main__":
    out = verify()
    artifacts = pathlib.Path(__file__).resolve().parent / "artifacts"
    artifacts.mkdir(exist_ok=True)
    (artifacts / "certificate.json").write_text(
        json.dumps(out["witness"], indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )
    print(f"PASS {out['id']}: {out['summary']}")
```

```markdown file=README.md
# Commuting counterexamples to determinantal entropy concavity

**Status:** refuted
**Certificate level:** computer-assisted

## Statement

Russell Lyons, "Determinantal probability: basic properties and conjectures," Proceedings of the International Congress of Mathematicians 2014, volume IV, pages 137–161, Conjecture 2.6, equation (2.14), section 2.3, page 141, conjectures midpoint concavity of exact-set Shannon entropy for positive-contraction determinantal kernels. The source explicitly permits complex Hilbert spaces. Consulted source: https://rdlyons.pages.iu.edu/pdf/icm-pub.pdf (retrieved 2026-10-30).

## Counterexample

Use the five-point unitary Fourier matrix, indexed 0 through 4, as a common eigenbasis. The two exact spectra are (11,9,9991,9990,9989)/10000 and (9,11,9989,9990,9991)/10000. The commuting kernels are strictly between zero and identity. Their occupation distributions are identical, but each endpoint entropy exceeds the midpoint entropy by more than 1/5000000000. The proof in case.tex also establishes an analytic positive-curvature limit, without computation.

## How to verify

Run `python verify.py`; it raises on any failed check, prints a PASS line, and writes `artifacts/certificate.json`. Python's standard library suffices. All probability arithmetic is exact over the rational numbers with the square root of five adjoined. Logarithms use rigorous rational series bounds and outward rounding. No floating-point comparison establishes the result.

The verifier checks strict admissibility, exact normalization, evenness, the finite entropy gap, and positive curvature. The required negative-control test was performed on a separate copy: changing the first direction entry from 1 to 2 raises AssertionError. The original verifier was left unchanged. The bundle was also unpacked and the extracted verifier was run independently of its working-directory original.

The source statement, nearby hypotheses, bibliography, and scope were checked independently. An additional isolated LaTeX compilation check was attempted but could not run: this environment has a TeX executable without its format files or LaTeX packages. No successful typesetting or repository-wide build is claimed.

## Artifacts

- `artifacts/certificate.json` — exact spectra, square-root bounds, outward rational entropy and curvature intervals, and exact occupation-probability coefficients.

## Attribution and scope

The session identifies the agents as Codex based on GPT-6; the exact model identifier is TODO. The contributor name is TODO. Discovery and agent audits occurred in October 2026. No external human audit or literature priority is claimed. A 2012 prior-work title appeared in a publicly indexed listing, but neither the listing nor the underlying work could be retrieved directly; assessing that lead is TODO, with details in case.tex. The separate beam-splitter consequence is not registered as a second published conjecture. No repository-wide CI or full-paper build is claimed by this submission bundle.
```

```bibtex file=references.bib.add
@inproceedings{Lyons2014DPP,
  author    = {Lyons, Russell},
  title     = {Determinantal probability: basic properties and conjectures},
  booktitle = {Proceedings of the International Congress of Mathematicians---Seoul 2014},
  volume    = {IV},
  pages     = {137--161},
  year      = {2014},
  url       = {https://rdlyons.pages.iu.edu/pdf/icm-pub.pdf}
}
```
