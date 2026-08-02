This bundle replaces the stub case `logdet-loewner`, which recorded a
base-pointed variant of the same alternating sum with no source and no
statement.  The statement refuted here was posed publicly on MathOverflow in
March 2017 and stood unanswered for nine years; the provenance block carries
the permalink, and the quoted statement is transcribed from the post itself.

Timeline: the counterexamples were found on 2026-02-16 with the GPT Pro model
then current, whose version is not recorded; the exact matrices from that
session were lost, and the witnesses certified here were re-derived in 2026-08.
`\foundby` therefore names the February session and `\formalizedby` the August
one.

```json file=case.json
{
  "id": "quantum-coupon-collector",
  "title": "Quantum coupon collection: positivity of an alternating sum of inverses",
  "status": "refuted",
  "prose": "case.tex",
  "bib_keys": ["Sra2017QuantumCoupon", "FlajoletGardyThimonier1992", "NiculescuSra2023"],
  "results": [
    {
      "id": "quantum-coupon-collector",
      "uid": null,
      "class": "user formal problem",
      "certificate_level": "exact",
      "theorem_label": "thm:quantum-coupon-collector",
      "provenance": {
        "url": "https://mathoverflow.net/questions/263833/quantum-coupon-collection-positivity-of-an-alternating-sum-of-matrices",
        "retrieved": "2026-08-02",
        "fidelity": "verbatim"
      }
    }
  ],
  "verify": { "python": "verify.py", "sage": [], "requires": [] },
  "artifacts": [
    {
      "file": "artifacts/certificate.json",
      "description": "Exact rational n=6 Loewner witness, exact rational n=10 trace witness, certified sign intervals, and the structural checks (positive definiteness, noncommutativity, general position)"
    }
  ]
}
```

```latex file=case.tex
% Prose for this counterexample.  Every region below is delimited by an
% environment that tools/build.py extracts; machine facts (ids, uid, dates,
% urls, enums) live in case.json.  See counterexamples/AGENTS.md.

\cxtitle{Quantum coupon collection: an alternating sum of inverses}

\begin{cxcredits}
\posedby{S.~Sra \citeyearpar{Sra2017QuantumCoupon}}
\foundby{GPT Pro}{2026-02-16}
\formalizedby{GPT-5.6 Pro, which re-derived the exact witnesses in 2026-08}
\auditedby{GPT-5.6 Pro, using exact rational arithmetic}
\contributedby{S.~Sra}
\end{cxcredits}

\begin{cxcontext}
In the classical coupon collector's problem with sampling probabilities
$x_1,\ldots,x_n>0$, the expected waiting time is the alternating sum
\[
T_n(x_1,\ldots,x_n)=\sum_{k=1}^n(-1)^{k+1}
\sum_{1\le i_1<\cdots<i_k\le n}\frac{1}{x_{i_1}+\cdots+x_{i_k}},
\]
which is positive for a reason having nothing to do with waiting times: $t\mapsto1/t$ is completely monotone on $(0,\infty)$, so the Laplace-transform representation makes the alternating sum an integral of a nonnegative quantity \cite{FlajoletGardyThimonier1992}.  The statement quoted below asks whether the same holds with the positive numbers replaced by positive definite matrices and the reciprocal by the matrix inverse.

Throughout, $\mathbf{S}_{++}^{d}$ is the cone of real symmetric positive definite $d\times d$ matrices, and for a nonempty $S\subseteq[n]$ we abbreviate $X_S:=\sum_{i\in S}X_i$, so that the source's double sum is
\[
Q_n(X_1,\ldots,X_n)=\sum_{\emptyset\ne S\subseteq[n]}(-1)^{|S|-1}X_S^{-1}.
\]
We also write $\Delta_n:=\tr Q_n$ for its scalar trace transform; since a positive definite matrix has positive trace, the conjecture implies $\Delta_n>0$.

The cone-valued form of the scalar mechanism is available: Theorem~7 of Niculescu and Sra \cite{NiculescuSra2023} states that every completely monotone $f$ on a cone $\mathcal C$ satisfies the inclusion--exclusion inequality $\sum_i f(x_i)-\sum_{i<j}f(x_i+x_j)+\cdots\ge0$ for all $x_1,\ldots,x_n\in\mathcal C$.  Applying it to $\mathcal C=\mathbf{S}_{++}^{d}$ and $f_v(X)=v^{\mathsf T}X^{-1}v$ would settle the conjecture for every $v$, and applying it to $X\mapsto\tr(X^{-1})$ would settle the trace form.  The refutation below therefore also shows that neither function is completely monotone on $\mathbf{S}_{++}^{d}$ for $d\ge3$ --- for $d=1$ both reduce to $1/t$, which is.
\end{cxcontext}

% ---------------- result: quantum-coupon-collector ----------------

\begin{cxsource}{quantum-coupon-collector}
S.~Sra, MathOverflow question 263833 \citeyearpar{Sra2017QuantumCoupon}
\end{cxsource}

\begin{cxstatement}{quantum-coupon-collector}
Here we take symmetric positive definite matrices $X_1,\ldots,X_n\in\mathbf{S}_{++}^d$, and consider the sum
\[
Q_n(X_1,\ldots,X_n):=\sum_{k=1}^n(-1)^{k+1}
\sum_{1\le i_1<\cdots<i_k\le n}\left(X_{i_1}+\cdots+X_{i_k}\right)^{-1}.
\]

\textbf{Conjecture.} For $n\ge1$, and $X_1,\ldots,X_n\in\mathbf{S}_{++}^d$, we have $Q_n(X_1,\ldots,X_n)\succ0$.

\emph{Note.} The cases $n=1,2,3$ are trivially true.  I've tried $n=4$ numerically, and it seems to hold.  (Also, by CCP, positivity immediately holds for a tuple of simultaneously diagonalizable matrices.)
\end{cxstatement}

\begin{cxsummary}{quantum-coupon-collector}
The matrix coupon-collector sum $\sum_{\emptyset\ne S}(-1)^{|S|-1}X_S^{-1}$ was conjectured positive definite for every order $n$ and every dimension $d$.
\end{cxsummary}

\begin{cxcertificate}{quantum-coupon-collector}
Exact rational $3\times3$ matrices with $n=6$ and the integer vector $(4,1,3)^{\mathsf T}$ give a quadratic form strictly between $-96$ and $-95$.
\end{cxcertificate}

\begin{cxrefutation}
The conjecture holds for a tuple of simultaneously diagonalizable matrices, where it is the classical identity coordinate by coordinate, and the source records that $n\le3$ is trivial and that $n=4$ was checked numerically.  Lemma~\ref{lem:qcc-facet} and Theorem~\ref{thm:qcc-positive-five} below upgrade that record: the conjecture is a theorem for every $d$ and every $n\le5$.  It fails at $n=6$.

\begin{lemma}[Facet averaging for inversion]\label{lem:qcc-facet}
Let $A_1,\ldots,A_m\in\mathbf{S}_{++}^{d}$, where $m\ge2$, and put $A=\sum_{j=1}^{m}A_j$.  Then
\[
A^{-1}\preceq\frac{m-1}{m^2}\sum_{j=1}^{m}(A-A_j)^{-1}.
\]
\end{lemma}
\begin{proof}
Set $B_j=A-A_j$, which is positive definite because it is a sum of the remaining $A_i$.  Since
\[
\frac1m\sum_{j=1}^{m}B_j=\frac{m-1}{m}A
\]
and the inversion map is operator convex on $\mathbf{S}_{++}^{d}$,
\[
\frac{m}{m-1}A^{-1}
=\Bigl(\frac1m\sum_{j=1}^{m}B_j\Bigr)^{-1}
\preceq\frac1m\sum_{j=1}^{m}B_j^{-1}.
\]
Rearranging gives the claim.
\end{proof}

For fixed $n$, introduce the layer sums
\[
E_k:=\sum_{\substack{S\subseteq[n]\\|S|=k}}X_S^{-1},\qquad1\le k\le n,
\]
each of which is positive definite.  Applying Lemma~\ref{lem:qcc-facet} inside each $(k+1)$-subset $T$, with the $A_j$ taken to be the $X_i$ for $i\in T$, gives $X_T^{-1}\preceq\frac{k}{(k+1)^2}\sum_{i\in T}X_{T\setminus\{i\}}^{-1}$.  Summing over all $T$ of size $k+1$, and noting that each fixed $k$-subset arises as a facet of exactly $n-k$ of them, yields
\begin{equation}\label{eq:qcc-layer}
E_{k+1}\preceq\frac{k(n-k)}{(k+1)^2}E_k,\qquad1\le k<n.
\end{equation}

\begin{theorem}[\statusproved: positivity through five variables]\label{thm:qcc-positive-five}
For every $d\ge1$, every $1\le n\le5$, and every $X_1,\ldots,X_n\in\mathbf{S}_{++}^{d}$, one has $Q_n(X_1,\ldots,X_n)\succ0$, and consequently $\Delta_n(X_1,\ldots,X_n)>0$.
\end{theorem}
\begin{proof}
The case $n=1$ is immediate.  For the rest, write $Q_n=E_1-E_2+E_3-\cdots+(-1)^{n-1}E_n$ and apply \eqref{eq:qcc-layer}:
\[
\begin{array}{rcl}
n=2:&E_2\preceq\frac14E_1,&Q_2\succeq\frac34E_1,\\[0.35em]
n=3:&E_2\preceq\frac12E_1,&Q_3\succeq\frac12E_1+E_3,\\[0.35em]
n=4:&E_2\preceq\frac34E_1,\quad E_4\preceq\frac3{16}E_3,
&Q_4\succeq\frac14E_1+\frac{13}{16}E_3,\\[0.35em]
n=5:&E_2\preceq E_1,\quad E_4\preceq\frac38E_3,
&Q_5\succeq\frac58E_3+E_5.
\end{array}
\]
Each displayed lower bound is a positive combination of layer sums of odd index, hence positive definite.
\end{proof}

\begin{theorem}[\statusfalse: quantum coupon collection]\label{thm:quantum-coupon-collector}
The conjecture is false: there are $d=3$, $n=6$ and $X_1,\ldots,X_6\in\mathbf{S}_{++}^{3}$ with $Q_6(X_1,\ldots,X_6)\not\succeq0$, so in particular $Q_6\succ0$ fails.
\end{theorem}
\begin{proof}
Take $d=3$, $n=6$, $\varepsilon=1/100$, and
\[
X_i=w_iu_iu_i^{\mathsf T}+\varepsilon I_3,
\]
where
\[
\begin{array}{c|c|c}
i&u_i^{\mathsf T}&w_i\\\hline
1&(-1,2,1)&10\\
2&(0,-3,1)&10\\
3&(-3,-2,0)&100\\
4&(2,-2,-2)&100\\
5&(-1,0,2)&100\\
6&(-1,3,0)&100
\end{array}
\]
Each $X_i$ is strictly positive definite because $X_i\succeq\varepsilon I_3\succ0$, so the hypotheses are met exactly as posed.  The example is genuinely noncommutative --- the $(1,2)$ entry of $[X_1,X_2]$ equals $-1500$ --- and therefore lies outside the simultaneously diagonalizable regime in which the classical identity applies.  For $v=(4,1,3)^{\mathsf T}$, exact rational evaluation of the sixty-three nonempty-subset terms gives
\[
-96<v^{\mathsf T}Q_6(X_1,\ldots,X_6)v<-95.
\]
The supplied verifier performs this computation using only \texttt{fractions.Fraction}.  Thus $Q_6$ has a negative quadratic form and is not positive semidefinite, let alone positive definite.
\end{proof}

The failure is not confined to the matrix ordering: the scalar consequence $\Delta_n>0$ fails too, and for a reason one can see in closed form.  Let $u_1,\ldots,u_n\in\R^3$ be such that every pair is linearly independent and every triple spans $\R^3$, and put
\[
X_i(\varepsilon):=u_iu_i^{\mathsf T}+\varepsilon I_3,\qquad\varepsilon>0,
\]
so that $X_S(\varepsilon)=\sum_{i\in S}u_iu_i^{\mathsf T}+k\varepsilon I_3$ for $|S|=k$.  A singleton leaves two regularized null directions, so $\tr X_S(\varepsilon)^{-1}=2/\varepsilon+O(1)$; a pair leaves one, so $\tr X_S(\varepsilon)^{-1}=1/(2\varepsilon)+O(1)$; and for $k\ge3$ the unregularized matrix is already positive definite, so the trace of the inverse is $O(1)$.  Only finitely many subsets occur, so the remainders sum uniformly and
\begin{equation}\label{eq:qcc-asymptotic}
\Delta_n\bigl(X_1(\varepsilon),\ldots,X_n(\varepsilon)\bigr)
=\frac1\varepsilon\Bigl(2n-\tfrac12\binom n2\Bigr)+O(1)
=\frac{n(9-n)}{4\varepsilon}+O(1).
\end{equation}
The coefficient is negative exactly for $n\ge10$, which the next theorem realizes with an exact witness.

\begin{theorem}[\statusfalse: the trace consequence]\label{thm:quantum-coupon-collector-trace}
There are $d=3$, $n=10$ and $X_1,\ldots,X_{10}\in\mathbf{S}_{++}^{3}$ with $\Delta_{10}(X_1,\ldots,X_{10})<0$.  A fortiori $Q_{10}\succ0$ fails.
\end{theorem}
\begin{proof}
Take $d=3$, $n=10$, $\varepsilon=1/10000$, and, for $t=0,1,\ldots,9$,
\[
u_t=(1,t,t^2)^{\mathsf T},\qquad X_{t+1}=u_tu_t^{\mathsf T}+\varepsilon I_3.
\]
Every $X_i$ is strictly positive definite, and every three of the $u_t$ are independent because their determinant is a nonzero Vandermonde product; the matrices are noncommuting, the $(1,2)$ entry of $[X_1,X_2]$ being $1$.  Exact rational evaluation of all $2^{10}-1=1023$ nonempty-subset terms gives
\[
-13901<\Delta_{10}(X_1,\ldots,X_{10})<-13900.
\]
The supplied verifier computes this with exact rational arithmetic and records the full numerator and denominator in \texttt{artifacts/certificate.json}.
\end{proof}

\begin{remark}[Scope]
What is refuted is the conjecture as posed, universally quantified over $n$ and $d$.  The exact record is now: for every $d$, the conjecture is true for $n\le5$ (Theorem~\ref{thm:qcc-positive-five}) and false at $n=6$ (Theorem~\ref{thm:quantum-coupon-collector}).  For the weaker trace form the record is coarser --- true for $n\le5$, false at $n=10$ --- and \eqref{eq:qcc-asymptotic}, whose coefficient vanishes at $n=9$, says nothing about $6\le n\le9$, since that construction is only one family.  Nothing here contradicts the simultaneously diagonalizable case, which remains an identity.
\end{remark}
\end{cxrefutation}
```

```python file=verify.py
#!/usr/bin/env python3
"""Certify exact rational counterexamples to quantum coupon-collector positivity.

Admission standard (see CONTRIBUTING.md): exact arithmetic only.  Every number
below is a `fractions.Fraction` or a Python int; no float is used anywhere.
"""
from __future__ import annotations

from fractions import Fraction
import itertools
import json
import pathlib
import sys
from typing import Sequence

if hasattr(sys, "set_int_max_str_digits"):
    sys.set_int_max_str_digits(0)

Scalar = Fraction
Vector = tuple[int, int, int]
Matrix = list[list[Scalar]]


def zero3() -> Matrix:
    return [[Fraction(0) for _ in range(3)] for _ in range(3)]


def identity3(scale: Scalar = Fraction(1)) -> Matrix:
    out = zero3()
    for i in range(3):
        out[i][i] = scale
    return out


def add3(a: Matrix, b: Matrix) -> Matrix:
    return [[a[i][j] + b[i][j] for j in range(3)] for i in range(3)]


def scale3(c: Scalar, a: Matrix) -> Matrix:
    return [[c * a[i][j] for j in range(3)] for i in range(3)]


def outer3(u: Sequence[int | Scalar]) -> Matrix:
    return [[Fraction(u[i]) * Fraction(u[j]) for j in range(3)] for i in range(3)]


def transpose3(a: Matrix) -> Matrix:
    return [[a[j][i] for j in range(3)] for i in range(3)]


def multiply3(a: Matrix, b: Matrix) -> Matrix:
    return [
        [sum((a[i][k] * b[k][j] for k in range(3)), Fraction(0)) for j in range(3)]
        for i in range(3)
    ]


def subtract3(a: Matrix, b: Matrix) -> Matrix:
    return [[a[i][j] - b[i][j] for j in range(3)] for i in range(3)]


def determinant3(a: Matrix) -> Scalar:
    a00, a01, a02 = a[0]
    a10, a11, a12 = a[1]
    a20, a21, a22 = a[2]
    return (
        a00 * (a11 * a22 - a12 * a21)
        - a01 * (a10 * a22 - a12 * a20)
        + a02 * (a10 * a21 - a11 * a20)
    )


def inverse3(a: Matrix) -> Matrix:
    a00, a01, a02 = a[0]
    a10, a11, a12 = a[1]
    a20, a21, a22 = a[2]
    det = determinant3(a)
    assert det != 0
    return [
        [
            (a11 * a22 - a12 * a21) / det,
            (a02 * a21 - a01 * a22) / det,
            (a01 * a12 - a02 * a11) / det,
        ],
        [
            (a12 * a20 - a10 * a22) / det,
            (a00 * a22 - a02 * a20) / det,
            (a02 * a10 - a00 * a12) / det,
        ],
        [
            (a10 * a21 - a11 * a20) / det,
            (a01 * a20 - a00 * a21) / det,
            (a00 * a11 - a01 * a10) / det,
        ],
    ]


def trace_inverse3(a: Matrix) -> Scalar:
    """tr(A^{-1}) as tr(adj A)/det A, so no full inverse is formed."""
    a00, a01, a02 = a[0]
    a10, a11, a12 = a[1]
    a20, a21, a22 = a[2]
    det = determinant3(a)
    assert det != 0
    trace_adjugate = (
        (a11 * a22 - a12 * a21)
        + (a00 * a22 - a02 * a20)
        + (a00 * a11 - a01 * a10)
    )
    return trace_adjugate / det


def is_symmetric3(a: Matrix) -> bool:
    return a == transpose3(a)


def leading_principal_minors3(a: Matrix) -> tuple[Scalar, Scalar, Scalar]:
    first = a[0][0]
    second = a[0][0] * a[1][1] - a[0][1] * a[1][0]
    third = determinant3(a)
    return first, second, third


def is_spd3(a: Matrix) -> bool:
    return is_symmetric3(a) and all(x > 0 for x in leading_principal_minors3(a))


def quadratic_form3(a: Matrix, v: Sequence[int | Scalar]) -> Scalar:
    return sum(
        (
            Fraction(v[i]) * a[i][j] * Fraction(v[j])
            for i in range(3)
            for j in range(3)
        ),
        Fraction(0),
    )


def coupon_matrix3(matrices: Sequence[Matrix]) -> Matrix:
    """Q_n = sum over nonempty S of (-1)^{|S|-1} (sum_{i in S} X_i)^{-1}."""
    n = len(matrices)
    out = zero3()
    subset_sums: list[Matrix] = [zero3() for _ in range(1 << n)]
    subset_sizes = [0 for _ in range(1 << n)]
    for mask in range(1, 1 << n):
        least_bit = mask & -mask
        index = least_bit.bit_length() - 1
        previous = mask ^ least_bit
        subset_sums[mask] = add3(subset_sums[previous], matrices[index])
        subset_sizes[mask] = subset_sizes[previous] + 1
        sign = Fraction(1 if subset_sizes[mask] % 2 else -1)
        out = add3(out, scale3(sign, inverse3(subset_sums[mask])))
    return out


def coupon_trace3(matrices: Sequence[Matrix]) -> Scalar:
    """Delta_n = tr Q_n, accumulated without forming Q_n."""
    n = len(matrices)
    out = Fraction(0)
    subset_sums: list[Matrix] = [zero3() for _ in range(1 << n)]
    subset_sizes = [0 for _ in range(1 << n)]
    for mask in range(1, 1 << n):
        least_bit = mask & -mask
        index = least_bit.bit_length() - 1
        previous = mask ^ least_bit
        subset_sums[mask] = add3(subset_sums[previous], matrices[index])
        subset_sizes[mask] = subset_sizes[previous] + 1
        sign = Fraction(1 if subset_sizes[mask] % 2 else -1)
        out += sign * trace_inverse3(subset_sums[mask])
    return out


def commutator3(a: Matrix, b: Matrix) -> Matrix:
    return subtract3(multiply3(a, b), multiply3(b, a))


def matrix_is_nonzero3(a: Matrix) -> bool:
    return any(a[i][j] != 0 for i in range(3) for j in range(3))


def rank_one_regularization(u: Vector, weight: int, epsilon: Scalar) -> Matrix:
    return add3(scale3(Fraction(weight), outer3(u)), identity3(epsilon))


def vandermonde_vector(t: int) -> Vector:
    return (1, t, t * t)


def determinant_of_columns(u: Vector, v: Vector, w: Vector) -> Scalar:
    matrix = [
        [Fraction(u[row]), Fraction(v[row]), Fraction(w[row])]
        for row in range(3)
    ]
    return determinant3(matrix)


def fraction_record(x: Scalar) -> dict[str, str]:
    return {"numerator": str(x.numerator), "denominator": str(x.denominator)}


def verify() -> dict:
    """Raise AssertionError if any check fails; return a machine-readable summary."""
    # Theorem thm:quantum-coupon-collector -- the conjecture as posed, at n = 6.
    n6_parameters: tuple[tuple[Vector, int], ...] = (
        ((-1, 2, 1), 10),
        ((0, -3, 1), 10),
        ((-3, -2, 0), 100),
        ((2, -2, -2), 100),
        ((-1, 0, 2), 100),
        ((-1, 3, 0), 100),
    )
    epsilon6 = Fraction(1, 100)
    matrices6 = [rank_one_regularization(u, w, epsilon6) for u, w in n6_parameters]
    assert all(is_spd3(matrix) for matrix in matrices6)
    assert matrix_is_nonzero3(commutator3(matrices6[0], matrices6[1]))

    coupon6 = coupon_matrix3(matrices6)
    test_vector6: Vector = (4, 1, 3)
    negative_quadratic_form6 = quadratic_form3(coupon6, test_vector6)
    assert Fraction(-96) < negative_quadratic_form6 < Fraction(-95)

    # Theorem thm:quantum-coupon-collector-trace -- the scalar consequence, at n = 10.
    epsilon10 = Fraction(1, 10_000)
    vectors10 = [vandermonde_vector(t) for t in range(10)]
    matrices10 = [rank_one_regularization(u, 1, epsilon10) for u in vectors10]
    assert all(is_spd3(matrix) for matrix in matrices10)
    assert matrix_is_nonzero3(commutator3(matrices10[0], matrices10[1]))
    assert all(
        determinant_of_columns(vectors10[i], vectors10[j], vectors10[k]) != 0
        for i, j, k in itertools.combinations(range(10), 3)
    )

    negative_trace10 = coupon_trace3(matrices10)
    assert Fraction(-13_901) < negative_trace10 < Fraction(-13_900)

    return {
        "id": "quantum-coupon-collector",
        "ok": True,
        "summary": (
            "exact n=6 negative quadratic form in (-96,-95); "
            "exact n=10 trace sum in (-13901,-13900)"
        ),
        "witness": {
            "loewner_n6": {
                "dimension": 3,
                "epsilon": "1/100",
                "parameters": [
                    {"u": list(u), "weight": w} for u, w in n6_parameters
                ],
                "test_vector": list(test_vector6),
                "quadratic_form": fraction_record(negative_quadratic_form6),
                "certified_interval": ["-96", "-95"],
                "strictly_positive_definite": True,
                "noncommuting": True,
            },
            "trace_n10": {
                "dimension": 3,
                "epsilon": "1/10000",
                "vectors": [list(u) for u in vectors10],
                "trace_inclusion_exclusion": fraction_record(negative_trace10),
                "certified_interval": ["-13901", "-13900"],
                "all_triples_independent": True,
                "strictly_positive_definite": True,
                "noncommuting": True,
            },
            "positive_range": {"proved_positive_definite_for_n": [1, 2, 3, 4, 5]},
        },
    }


if __name__ == "__main__":
    output = verify()
    artifacts = pathlib.Path(__file__).resolve().parent / "artifacts"
    artifacts.mkdir(exist_ok=True)
    (artifacts / "certificate.json").write_text(
        json.dumps(output["witness"], indent=2, sort_keys=True) + "\n"
    )
    print(f"PASS {output['id']}: {output['summary']}")
```

```markdown file=README.md
# Quantum coupon collection: positivity of an alternating sum of inverses

**Status:** refuted
**Certificate level:** exact

## Statement

For symmetric positive definite $X_1,\ldots,X_n$, let

$$Q_n(X_1,\ldots,X_n)=\sum_{k=1}^n(-1)^{k+1}\sum_{1\le i_1<\cdots<i_k\le n}(X_{i_1}+\cdots+X_{i_k})^{-1},$$

the matrix analogue of the coupon collector's expected waiting time. Sra
conjectured on [MathOverflow](https://mathoverflow.net/questions/263833/quantum-coupon-collection-positivity-of-an-alternating-sum-of-matrices)
in March 2017 that $Q_n \succ 0$ for every $n\ge1$, noting that $n\le3$ is
trivial and that $n=4$ held numerically. The question stood unanswered for
nine years.

## Counterexample

The conjecture is true for every $n\le5$ — proved here by an operator-convexity
facet-averaging argument — and false at $n=6$: six rank-one-plus-$\varepsilon I$
matrices of size three and the integer vector `(4, 1, 3)` give a quadratic form
in `(-96, -95)`.

Even the scalar consequence $\operatorname{tr} Q_n > 0$ fails: ten moment-curve
matrices in dimension three give an exact alternating trace in
`(-13901, -13900)`. The prose derives the asymptotic coefficient
`n(9-n)/(4 epsilon)` that explains why this family turns negative at ten.

## How to verify

`python verify.py` — raises on any failed check and writes the artifact. Only
Python's exact `fractions.Fraction` arithmetic is used; no float appears.

## Artifacts

- `artifacts/certificate.json` — exact witness parameters, exact rational
  numerator/denominator pairs, certified sign intervals, and the structural
  checks (positive definiteness, noncommutativity, general position).

## Provenance

Both counterexamples were found on 16 February 2026, in a session with the GPT
Pro model then current; **which version that was is not recorded**, so the
credit line says `GPT Pro` and claims no more. The exact matrices from that
session were not preserved — see `audit_notes.md` — and were re-derived in
August 2026, which is what `verify.py` certifies. The refuted statement itself
is nine years older than either session.
```

```bibtex file=references.bib.add
@misc{Sra2017QuantumCoupon,
  author       = {Sra, Suvrit},
  title        = {Quantum coupon collection: positivity of an alternating sum of matrices},
  howpublished = {MathOverflow question 263833},
  month        = mar,
  year         = {2017},
  url          = {https://mathoverflow.net/questions/263833/quantum-coupon-collection-positivity-of-an-alternating-sum-of-matrices},
  note         = {Posed 5 March 2017; unanswered as of 2 August 2026}
}

@article{FlajoletGardyThimonier1992,
  author  = {Flajolet, Philippe and Gardy, Dani\`ele and Thimonier, Lo\"ys},
  title   = {Birthday paradox, coupon collectors, caching algorithms and self-organizing search},
  journal = {Discrete Applied Mathematics},
  volume  = {39},
  number  = {3},
  pages   = {207--229},
  year    = {1992},
  doi     = {10.1016/0166-218X(92)90177-C}
}

@article{NiculescuSra2023,
  author  = {Niculescu, Constantin P. and Sra, Suvrit},
  title   = {The {H}ornich--{H}lawka functional inequality for functions with positive differences},
  journal = {arXiv preprint arXiv:2301.08342},
  year    = {2023},
  url     = {https://arxiv.org/abs/2301.08342}
}
```
