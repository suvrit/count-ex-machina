```json file=case.json
{
  "id": "odonnell-matrix-conjecture",
  "title": "No dimension-free constant in O'Donnell's matrix conjecture",
  "status": "refuted",
  "prose": "case.tex",
  "bib_keys": ["Wright2015Proposal"],
  "results": [
    {
      "id": "odonnell-matrix-conjecture",
      "uid": null,
      "class": "external conjecture",
      "certificate_level": "exact",
      "theorem_label": "thm:odonnell-matrix-conjecture",
      "provenance": {
        "url": "https://www.cs.cmu.edu/~jswright/proposal.pdf",
        "retrieved": "2026-08-04",
        "fidelity": "verbatim"
      }
    }
  ],
  "verify": { "python": "verify.py", "sage": [], "requires": [] },
  "artifacts": [
    { "file": "artifacts/certificate.json", "description": "Exact algebraic family parameters, a symbolic unboundedness certificate, and a finite exact-arithmetic audit." }
  ]
}
```

```latex file=case.tex
\cxtitle{Ryan O'Donnell's matrix conjecture}

\begin{cxcredits}
\posedby{Ryan O'Donnell, recorded by John Wright \citeyearpar{Wright2015Proposal}}
\foundby{GPT-5.6 Pro}{2026-08}
\formalizedby{GPT-5.6 Pro}
\auditedby{GPT-5.6 Pro}
\contributedby{Suvrit Sra}
\end{cxcredits}

\begin{cxcontext}
For a Hermitian matrix $X$, write
\[
  \lVert X\rVert_1=\operatorname{tr}|X|
\]
for its trace norm.  For $R\in\mathbb C^{n\times n}$, let
$D=\operatorname{Diag}(R)=\operatorname{diag}(d_1,\ldots,d_n)$.
We list the eigenvalues as $\lambda_1\geq\cdots\geq\lambda_n$.
The source's displayed conjecture does not separately specify an ordering of
its diagonal entries.  In the family below, both $(\lambda_i)$ and $(d_i)$ are
strictly decreasing in the displayed index order, so the refutation does not
rely on a favorable permutation or matching.
\end{cxcontext}

\begin{cxsource}{odonnell-matrix-conjecture}
Ryan O'Donnell's conjecture is recorded by John Wright in Section~4.3,
Conjecture~4.28, of his Ph.D. thesis proposal \cite{Wright2015Proposal}.
\end{cxsource}

\begin{cxstatement}{odonnell-matrix-conjecture}
Let $R$ be a unit trace psd matrix with eigenvalues $\lambda_i$. Then,
\[
  \lVert R-\operatorname{Diag}(R)\rVert_1^2
  =\lVert R-D\rVert_1^2
  \leq c\sum_i |\lambda_i-d_{ii}|,
\]
for some absolute constant independent of $n$?
\end{cxstatement}

\begin{cxsummary}{odonnell-matrix-conjecture}
Every absolute $c$ fails: an exact real-symmetric density-matrix family has ratio greater than $(\log_2 n)/32$.
\end{cxsummary}

\begin{cxcertificate}{odonnell-matrix-conjecture}
An exact algebraic Givens-rotation family with a rational dyadic lower bound, accompanied by a standard-library exact-arithmetic verifier.
\end{cxcertificate}

\begin{cxrefutation}
The conjecture asks whether the off-diagonal trace norm of a density matrix can
be controlled, up to an absolute constant, by the $\ell_1$ displacement between
its spectrum and its diagonal \cite{Wright2015Proposal}.  The following exact
family shows logarithmic divergence.

\begin{theorem}[\statusfalse: O'Donnell's matrix conjecture]\label{thm:odonnell-matrix-conjecture}
For every $C>0$ there exist an integer $n$ and a real symmetric positive
semidefinite matrix $R\in\mathbb R^{n\times n}$ with
$\operatorname{tr}R=1$ such that, writing
$D=\operatorname{Diag}(R)=\operatorname{diag}(d_1,\ldots,d_n)$ and listing the
eigenvalues $\lambda_1\geq\cdots\geq\lambda_n$,
\[
  \frac{\lVert R-D\rVert_1^2}
       {\sum_{i=1}^n |\lambda_i-d_i|}>C.
\]
Moreover, both $(\lambda_i)$ and $(d_i)$ are strictly decreasing.
\end{theorem}

\begin{proof}
Fix an integer $m\geq2$ and put
\[
  n=2^m,\qquad q=n,\qquad
  H=H_{n-1}=\sum_{i=1}^{n-1}\frac1i,
\]
\[
  B=1+q^2H,\qquad
  \delta=\frac1{2B},\qquad
  \eta=\frac1{2n}.
\]
Define positive spectral gaps by
\[
  g_1=\delta(1+q^2),
  \qquad
  g_i=\delta\frac{q^2}{i^2}
  \quad (2\leq i\leq n-1),
\]
and set
\[
  \lambda_n=\eta,
  \qquad
  \lambda_i=\eta+\sum_{k=i}^{n-1}g_k
  \quad (1\leq i\leq n-1).
\]
Then $\lambda_1>\cdots>\lambda_n>0$, and
\[
\begin{aligned}
  \sum_{i=1}^n\lambda_i
  &=n\eta+\sum_{i=1}^{n-1}i g_i \\
  &=\frac12+\delta\left(1+q^2+q^2\sum_{i=2}^{n-1}\frac1i\right)
    =\frac12+\delta B=1.
\end{aligned}
\]
Thus $\Lambda=\operatorname{diag}(\lambda_1,\ldots,\lambda_n)$ is a density
matrix.

For $1\leq i\leq n-1$, put
\[
  r_i=\frac qi,
  \qquad
  c_i=\frac{q}{\sqrt{q^2+i^2}},
  \qquad
  s_i=\frac{i}{\sqrt{q^2+i^2}}.
\]
Hence $c_i^2+s_i^2=1$ and $c_i/s_i=r_i$.  Let $G_i$ be the identity except
for the following orthogonal block in coordinates $i,i+1$:
\[
  \begin{pmatrix}
    c_i&-s_i\\
    s_i& c_i
  \end{pmatrix}.
\]
Starting from $R^{(0)}=\Lambda$, define successively
\[
  R^{(i)}=G_iR^{(i-1)}G_i^{\mathsf T},
  \qquad 1\leq i\leq n-1,
\]
and let $R=R^{(n-1)}$.  This is an exact algebraic matrix.  Since it is
orthogonally similar to $\Lambda$, it is real symmetric, positive semidefinite,
has trace one, and has eigenvalues $(\lambda_i)$.

We next compute its diagonal exactly.  Before the first rotation, the active
diagonal gap is
\[
  \lambda_1-\lambda_2=g_1=\delta(1+r_1^2).
\]
Before rotation $G_i$ for $i\geq2$, coordinate $i$ has diagonal entry
$\lambda_i+\delta$, coordinate $i+1$ has diagonal entry $\lambda_{i+1}$,
and coordinate $i+1$ has not previously been touched.  Thus the active
$2\times2$ principal block is diagonal and its diagonal gap is
\[
  (\lambda_i+\delta)-\lambda_{i+1}
  =g_i+\delta
  =\delta(1+r_i^2).
\]
In both cases,
\[
  s_i^2\,\delta(1+r_i^2)=\delta.
\]
Consequently, $G_i$ transfers exactly $\delta$ from diagonal position $i$ to
position $i+1$.  Induction gives
\[
  d_1=\lambda_1-\delta,
  \qquad
  d_i=\lambda_i\quad(2\leq i\leq n-1),
  \qquad
  d_n=\lambda_n+\delta.
\]
These entries are strictly decreasing: at the first edge the remaining gap is
$g_1-\delta=\delta q^2>0$, at every interior edge it is $g_i>0$, and at the
last edge it is
\[
  g_{n-1}-\delta
  =\delta\left(\frac{q^2}{(n-1)^2}-1\right)>0
\]
because $q=n$.  Therefore
\[
  \sum_{i=1}^n|\lambda_i-d_i|=2\delta.
\]

The same rotation calculation gives useful exact off-diagonal entries.  At
step $i$, the newly created $(i,i+1)$ entry has magnitude
\[
  c_is_i\,\delta(1+r_i^2)=\delta r_i.
\]
For $i\leq n-2$, the next rotation multiplies this entry by $c_{i+1}$; all
later rotations leave it unchanged.  Hence
\[
  |R_{i,i+1}|=
  \begin{cases}
    \delta r_i c_{i+1},&1\leq i\leq n-2,\\
    \delta r_{n-1},&i=n-1.
  \end{cases}
\]
Let $A=R-D$.  Pinch $A$ to the disjoint coordinate blocks
$(1,2),(3,4),\ldots,(n-1,n)$.  Trace norm is contractive under pinching, and
each retained zero-diagonal $2\times2$ block has trace norm twice the magnitude
of its off-diagonal entry.  If
\[
  O=\sum_{\substack{1\leq i\leq n-1\\ i\ \mathrm{odd}}}\frac1i,
\]
then $q=n$ implies
\[
  c_j^2=\frac{q^2}{q^2+j^2}>\frac12
  \qquad(1\leq j\leq n-1).
\]
Using the multiplier $1>1/\sqrt2$ for the final edge as well, we obtain
\[
  \lVert A\rVert_1
  \geq 2\sum_{\substack{1\leq i\leq n-1\\ i\ \mathrm{odd}}}|R_{i,i+1}|
  >\sqrt2\,\delta q O.
\]
It follows that
\[
\begin{aligned}
  \frac{\lVert R-D\rVert_1^2}
       {\sum_i|\lambda_i-d_i|}
  &>\frac{2\delta^2q^2O^2}{2\delta}
    =\delta q^2O^2
    =\frac{q^2O^2}{2(1+q^2H)}\\
  &>\frac{O^2}{2(H+1)}.
\end{aligned}
\]

It remains only to estimate the two harmonic sums.  In each dyadic block
$[2^k,2^{k+1})$, for $1\leq k\leq m-1$, there are $2^{k-1}$ odd integers,
each contributing more than $2^{-(k+1)}$.  Therefore
\[
  O>1+\frac{m-1}{4}=\frac{m+3}{4}.
\]
Also
\[
  H_{n-1}<1+\log(n-1)<m+1.
\]
Consequently,
\[
  \frac{\lVert R-D\rVert_1^2}
       {\sum_i|\lambda_i-d_i|}
  >\frac{(m+3)^2}{32(m+2)}
  >\frac{m}{32}.
\]
Given any real $C>0$, choose an integer $m>32C$.  The resulting exact matrix
has ratio greater than $C$, proving that no dimension-independent constant can
exist.
\end{proof}
\end{cxrefutation}
```

```python file=verify.py
#!/usr/bin/env python3
"""Certify the exact Givens-rotation family refuting O'Donnell's matrix conjecture."""
from __future__ import annotations

import json
import pathlib
from fractions import Fraction
from typing import Iterable


CASE_ID = "odonnell-matrix-conjecture"


def _fraction_text(value: Fraction) -> str:
    """Return a lossless plain-text representation of a Fraction."""
    if value.denominator == 1:
        return str(value.numerator)
    return f"{value.numerator}/{value.denominator}"


def _sum_fractions(values: Iterable[Fraction]) -> Fraction:
    return sum(values, Fraction(0, 1))


def _poly_add(left: list[int], right: list[int]) -> list[int]:
    size = max(len(left), len(right))
    out = [0] * size
    for index in range(size):
        out[index] = (
            (left[index] if index < len(left) else 0)
            + (right[index] if index < len(right) else 0)
        )
    while len(out) > 1 and out[-1] == 0:
        out.pop()
    return out


def _poly_scale(poly: list[int], scalar: int) -> list[int]:
    return [scalar * coefficient for coefficient in poly]


def _poly_mul(left: list[int], right: list[int]) -> list[int]:
    out = [0] * (len(left) + len(right) - 1)
    for i, a in enumerate(left):
        for j, b in enumerate(right):
            out[i + j] += a * b
    while len(out) > 1 and out[-1] == 0:
        out.pop()
    return out


def _symbolic_unboundedness_audit() -> dict:
    """Check the polynomial certificate valid for every integer target C >= 0."""
    # Choose m = 32*C + 1.  The proof gives
    # ratio > (m+3)^2 / (32*(m+2)).
    # Cross-multiplication against C leaves 160*C + 16 > 0.
    c_poly = [0, 1]
    m_poly = [1, 32]
    m_plus_three = _poly_add(m_poly, [3])
    m_plus_two = _poly_add(m_poly, [2])
    gap = _poly_add(
        _poly_mul(m_plus_three, m_plus_three),
        _poly_scale(_poly_mul(c_poly, m_plus_two), -32),
    )
    assert gap == [16, 160]
    assert all(coefficient > 0 for coefficient in gap)

    for target in (0, 1, 2, 10, 1000):
        m = 32 * target + 1
        lower = Fraction((m + 3) * (m + 3), 32 * (m + 2))
        assert lower > target

    return {
        "target": "any integer C >= 0",
        "choice_of_m": "32*C+1",
        "dimension": "2^(32*C+1)",
        "ratio_lower_bound": "(m+3)^2/(32*(m+2))",
        "cross_multiplied_gap": "160*C+16",
    }


def _finite_exact_audit(n: int = 512) -> dict:
    """Audit all scalar identities for one exact finite member of the family."""
    assert n >= 4
    assert n & (n - 1) == 0
    assert n % 2 == 0

    q = n
    harmonic = _sum_fractions(Fraction(1, i) for i in range(1, n))
    odd_harmonic = _sum_fractions(Fraction(1, i) for i in range(1, n, 2))
    b_value = Fraction(1, 1) + q * q * harmonic
    delta = Fraction(1, 2) / b_value
    eta = Fraction(1, 2 * n)

    gaps = [delta * (1 + q * q)]
    gaps.extend(delta * q * q / (i * i) for i in range(2, n))
    assert len(gaps) == n - 1
    assert all(gap > 0 for gap in gaps)

    eigenvalues = [Fraction(0, 1)] * n
    eigenvalues[-1] = eta
    for index in range(n - 2, -1, -1):
        eigenvalues[index] = eigenvalues[index + 1] + gaps[index]

    assert all(eigenvalues[i] > eigenvalues[i + 1] for i in range(n - 1))
    assert _sum_fractions(eigenvalues) == 1
    assert n * eta + _sum_fractions(
        Fraction(i, 1) * gaps[i - 1] for i in range(1, n)
    ) == 1

    diagonal = list(eigenvalues)
    diagonal[0] -= delta
    diagonal[-1] += delta
    assert all(diagonal[i] > diagonal[i + 1] for i in range(n - 1))

    spectral_diagonal_distance = _sum_fractions(
        abs(eigenvalues[i] - diagonal[i]) for i in range(n)
    )
    assert spectral_diagonal_distance == 2 * delta

    for i in range(1, n):
        c_squared = Fraction(q * q, q * q + i * i)
        s_squared = Fraction(i * i, q * q + i * i)
        r_squared = Fraction(q * q, i * i)
        assert c_squared + s_squared == 1
        assert c_squared == r_squared * s_squared

        active_gap = gaps[i - 1] if i == 1 else gaps[i - 1] + delta
        assert active_gap == delta * (1 + r_squared)
        assert active_gap * s_squared == delta

        created_edge_squared = active_gap * active_gap * c_squared * s_squared
        assert created_edge_squared == delta * delta * r_squared

        next_c_squared = (
            Fraction(1, 1)
            if i == n - 1
            else Fraction(q * q, q * q + (i + 1) * (i + 1))
        )
        final_edge_squared = created_edge_squared * next_c_squared
        assert next_c_squared > Fraction(1, 2)
        assert final_edge_squared > delta * delta * r_squared / 2

    pinching_ratio_lower_bound = (
        Fraction(q * q, 1) * odd_harmonic * odd_harmonic / (2 * b_value)
    )
    assert pinching_ratio_lower_bound > 1

    # Built-in mutation test: changing the first gap by delta must break the
    # exact transfer identity checked above.
    first_s_squared = Fraction(1, q * q + 1)
    perturbed_first_gap = gaps[0] + delta
    assert perturbed_first_gap * first_s_squared != delta

    return {
        "n": n,
        "q": q,
        "H_n_minus_1": _fraction_text(harmonic),
        "odd_harmonic_sum": _fraction_text(odd_harmonic),
        "B": _fraction_text(b_value),
        "delta": _fraction_text(delta),
        "spectral_diagonal_distance": _fraction_text(spectral_diagonal_distance),
        "pinching_ratio_lower_bound": _fraction_text(pinching_ratio_lower_bound),
        "comparison": "pinching_ratio_lower_bound > 1",
        "mutation_test": "replacing g_1 by g_1+delta is rejected",
    }


def verify() -> dict:
    """Raise AssertionError if any check fails; return a machine-readable summary."""
    family = _symbolic_unboundedness_audit()
    finite = _finite_exact_audit()
    return {
        "id": CASE_ID,
        "ok": True,
        "summary": (
            "the family has ratio > (log_2 n)/32; "
            "the generic gap is 160*C+16 and the n=512 exact audit exceeds 1"
        ),
        "witness": {
            "family": family,
            "finite_exact_audit": finite,
        },
    }


if __name__ == "__main__":
    out = verify()
    art = pathlib.Path(__file__).resolve().parent / "artifacts"
    art.mkdir(exist_ok=True)
    (art / "certificate.json").write_text(
        json.dumps(out["witness"], indent=2, sort_keys=True) + "\n"
    )
    print(f"PASS {out['id']}: {out['summary']}")
```

```markdown file=README.md
# No dimension-free constant in O'Donnell's matrix conjecture

**Status:** refuted
**Certificate level:** exact

## Statement
Conjecture 4.28 in Section 4.3 of John Wright's 2015 Ph.D. thesis proposal, attributed there to Ryan O'Donnell, asks whether the squared trace norm of the off-diagonal part of every unit-trace positive semidefinite matrix is bounded by an absolute constant times the entrywise-matched distance between its spectrum and diagonal.

## Counterexample
For every integer m at least 2, the package defines an exact algebraic density matrix of dimension n = 2^m by conjugating a rational diagonal spectrum with a sequence of exact Givens rotations. Its spectrum and diagonal are both strictly decreasing, their l1 distance is exactly 2 delta, and pinching the off-diagonal part gives a ratio greater than m/32. Hence the ratio is unbounded.

## How to verify
Run `python verify.py`; it raises on any failed check and writes the artifact. The verifier uses only integer and Fraction arithmetic, checks the scalar identities behind the Givens construction, proves the generic target gap 160*C+16, audits a finite n = 512 member, and includes a deliberate mutation test.

## Artifacts
- `artifacts/certificate.json` — exact family formulas, the symbolic unboundedness certificate, and exact rational data for the finite audit.
```

```bibtex file=references.bib.add
@misc{Wright2015Proposal,
  author       = {John Wright},
  title        = {How to Learn a Quantum State},
  howpublished = {Ph.D. thesis proposal, Carnegie Mellon University},
  year         = {2015},
  note         = {Section 4.3, Conjecture 4.28},
  url          = {https://www.cs.cmu.edu/~jswright/proposal.pdf}
}
```
