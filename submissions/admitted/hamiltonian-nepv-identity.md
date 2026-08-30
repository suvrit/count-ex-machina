```json file=case.json
{
  "id": "hamiltonian-nepv-identity",
  "title": "Failure of the proposed Hamiltonian NEPv Rayleigh identity",
  "status": "refuted",
  "prose": "case.tex",
  "bib_keys": ["AmselEtAl2026"],
  "results": [
    {
      "id": "hamiltonian-nepv-identity",
      "uid": null,
      "class": "published theorem",
      "certificate_level": "exact",
      "theorem_label": "thm:hamiltonian-nepv-identity",
      "provenance": {
        "url": "https://arxiv.org/abs/2602.05394v2",
        "retrieved": "2026-08-04",
        "fidelity": "verbatim"
      }
    }
  ],
  "verify": { "python": "verify.py", "sage": [], "requires": [] },
  "artifacts": [
    {
      "file": "artifacts/certificate.json",
      "description": "Exact rational Hermitian matrices and vector, with the two unequal Rayleigh quotients"
    }
  ]
}
```

```latex file=case.tex
\cxtitle{Failure of the proposed Hamiltonian NEPv Rayleigh identity}

\begin{cxcredits}
\posedby{Elias Jarlebring \citeyearpar{AmselEtAl2026}}
\foundby{OpenAI Codex}{2026-08}
\formalizedby{OpenAI Codex}
\auditedby{OpenAI Codex}
\contributedby{Suvrit Sra}
\end{cxcredits}

\begin{cxcontext}
Section~6.2 considers $n,d\in\mathbb N$, nonzero vectors
$x_1,\ldots,x_d\in\mathbb C^n$, and matrices
$F_i,G_{i,j},K_{i,j}\in\mathbb C^{n\times n}$ that are Hermitian and have
norm at most one.  It defines
\[
H=\sum_{i=1}^{d}\left(F_i^{\langle i\rangle}
 +\sum_{j=1}^{d}G_{i,j}^{\langle i\rangle}
 K_{i,j}^{\langle j\rangle}\right)
\]
and the product-state Rayleigh quotient
\[
f(x_1,\ldots,x_d)=
\frac{(x_1\otimes\cdots\otimes x_d)^H
H(x_1\otimes\cdots\otimes x_d)}
{\prod_{j=1}^{d}x_j^Hx_j}.
\]
The proposed block diagonal matrix $A$ has blocks
\[
A_i=\left(\frac{\sum_{j=1}^{d}x_j^Hx_j}{x_i^Hx_i}\right)
\left(F_i+\sum_{j=1}^{d}G_{i,j}
\frac{x_j^HK_{i,j}x_j}{x_j^Hx_j}\right).
\]
The displayed source statement writes the stack through $x_n$, although $A$
has $d$ blocks and the surrounding text declares the NEPv dimension to be
$nd$.  The only dimensionally consistent reading is the stack through $x_d$;
the counterexample below uses $d=1$, so that $z=x_1$.
\end{cxcontext}

\begin{cxsource}{hamiltonian-nepv-identity}
The assertion appears immediately after equation~(20) in Section~6.2 of
\cite{AmselEtAl2026}.  The section is scribed by Edgar Solomonik and records
discussion with Elias Jarlebring, Florian Schafer, Maryam Dehghan, Tamara
Kolda, and Chris Cama\~no; it says the question is based on a pre-workshop
question of Elias Jarlebring.
\end{cxsource}

\begin{cxstatement}{hamiltonian-nepv-identity}
Then, we have that with
\[
z=\begin{bmatrix}x_{1}\\
\vdots\\
x_{n}\end{bmatrix},\quad
\frac{z^{H}A(z)z}{z^{H}z}=f(x_{1},\ldots,x_{d}).
\]
\end{cxstatement}

\begin{cxsummary}{hamiltonian-nepv-identity}
The proposed NEPv matrix does not reproduce the product-state Rayleigh
quotient when the Hamiltonian sum includes a same-site term with $i=j$.
\end{cxsummary}

\begin{cxcertificate}{hamiltonian-nepv-identity}
The certificate consists of exact $2\times2$ integer matrices and the integer
vector $(1,2)^T$, for which the two assertedly equal values are $0$ and
$-4/25$.
\end{cxcertificate}

\begin{cxrefutation}
The construction in Section~6.2 of \cite{AmselEtAl2026} replaces a same-site
expectation of a product by the product of two expectations.  Those
quantities need not agree.

\begin{theorem}[\statusfalse: proposed NEPv Rayleigh identity]
\label{thm:hamiltonian-nepv-identity}
The displayed Rayleigh-quotient identity following equation~(20) is false for
the stated matrix formulas.  This refutes an assertion in the setup of
Problem~6.2, not the problem's request for an efficient algorithm.
\end{theorem}
\begin{proof}
Set $n=2$ and $d=1$, and take
\[
F_1=\begin{pmatrix}0&0\\0&0\end{pmatrix},\qquad
G_{1,1}=\begin{pmatrix}1&0\\0&0\end{pmatrix},\qquad
K_{1,1}=\begin{pmatrix}0&0\\0&-1\end{pmatrix},\qquad
x_1=\begin{pmatrix}1\\2\end{pmatrix}.
\]
All three matrices are Hermitian and have norm at most one.  Moreover,
$G_{1,1}$ and $K_{1,1}$ commute, so the matrix $H$ below is Hermitian.  Since
$d=1$, equation~(18) gives
\[
H=G_{1,1}K_{1,1}
=\begin{pmatrix}0&0\\0&0\end{pmatrix}.
\]
Therefore the objective in equation~(19) is
\[
f(x_1)=\frac{x_1^HHx_1}{x_1^Hx_1}=\frac{0}{5}=0.
\]
On the other hand, the scalar prefactor in equation~(20) is one and
\[
\frac{x_1^HK_{1,1}x_1}{x_1^Hx_1}=-\frac45,
\qquad
A(x_1)=-\frac45G_{1,1}.
\]
It follows that
\[
\frac{x_1^HA(x_1)x_1}{x_1^Hx_1}
=-\frac45\frac{1}{5}=-\frac{4}{25}\ne0=f(x_1).
\]
The failed step is specific and algebraic: for $i=j$, equation~(18) contains
\[
\frac{x_i^HG_{i,i}K_{i,i}x_i}{x_i^Hx_i},
\]
whereas equation~(20) produces
\[
\left(\frac{x_i^HG_{i,i}x_i}{x_i^Hx_i}\right)
\left(\frac{x_i^HK_{i,i}x_i}{x_i^Hx_i}\right).
\]
Hermiticity of the two factors does not make these expressions equal; the
counterexample uses commuting factors and even has $H=0$.
\end{proof}
\end{cxrefutation}
```

```python file=verify.py
#!/usr/bin/env python3
"""Certify the exact failure of the Rayleigh identity following equation (20)."""
from __future__ import annotations

import json
import pathlib
from fractions import Fraction


Scalar = Fraction
Matrix2 = tuple[tuple[Scalar, Scalar], tuple[Scalar, Scalar]]
Vector2 = tuple[Scalar, Scalar]


def transpose(matrix: Matrix2) -> Matrix2:
    return (
        (matrix[0][0], matrix[1][0]),
        (matrix[0][1], matrix[1][1]),
    )


def matmul(left: Matrix2, right: Matrix2) -> Matrix2:
    return tuple(
        tuple(
            sum((left[i][k] * right[k][j] for k in range(2)), Fraction(0))
            for j in range(2)
        )
        for i in range(2)
    )  # type: ignore[return-value]


def scale(scalar: Scalar, matrix: Matrix2) -> Matrix2:
    return tuple(
        tuple(scalar * entry for entry in row) for row in matrix
    )  # type: ignore[return-value]


def quadratic(vector: Vector2, matrix: Matrix2) -> Scalar:
    product = (
        matrix[0][0] * vector[0] + matrix[0][1] * vector[1],
        matrix[1][0] * vector[0] + matrix[1][1] * vector[1],
    )
    return vector[0] * product[0] + vector[1] * product[1]


def matrix_strings(matrix: Matrix2) -> list[list[str]]:
    return [[str(entry) for entry in row] for row in matrix]


def verify() -> dict:
    """Raise AssertionError if any check fails; return a machine-readable summary."""
    zero: Matrix2 = (
        (Fraction(0), Fraction(0)),
        (Fraction(0), Fraction(0)),
    )
    g: Matrix2 = (
        (Fraction(1), Fraction(0)),
        (Fraction(0), Fraction(0)),
    )
    k: Matrix2 = (
        (Fraction(0), Fraction(0)),
        (Fraction(0), Fraction(-1)),
    )
    x: Vector2 = (Fraction(1), Fraction(2))

    # These are the explicit assumptions on the three local factors.
    assert transpose(zero) == zero
    assert transpose(g) == g
    assert transpose(k) == k
    # G is an orthogonal projection and -K is one too, certifying norm one.
    assert matmul(g, g) == g
    assert matmul(k, k) == scale(Fraction(-1), k)
    assert matmul(g, k) == matmul(k, g)

    norm_squared = quadratic(x, (
        (Fraction(1), Fraction(0)),
        (Fraction(0), Fraction(1)),
    ))
    assert norm_squared == 5

    # Equations (18)--(19), with d=1 and F_1=0.
    h = matmul(g, k)
    assert h == zero
    objective = quadratic(x, h) / norm_squared

    # Equation (20), whose outer scalar prefactor is 1 when d=1.
    k_rayleigh = quadratic(x, k) / norm_squared
    a = scale(k_rayleigh, g)
    proposed_rayleigh = quadratic(x, a) / norm_squared

    assert objective == 0
    assert k_rayleigh == Fraction(-4, 5)
    assert proposed_rayleigh == Fraction(-4, 25)
    assert proposed_rayleigh != objective

    exact_witness = {
        "n": 2,
        "d": 1,
        "F_1": matrix_strings(zero),
        "G_1_1": matrix_strings(g),
        "K_1_1": matrix_strings(k),
        "x_1": [str(entry) for entry in x],
        "x_norm_squared": str(norm_squared),
        "objective_from_equations_18_19": str(objective),
        "rayleigh_from_equation_20": str(proposed_rayleigh),
    }
    return {
        "id": "hamiltonian-nepv-identity",
        "ok": True,
        "summary": "the exact values asserted equal are 0 and -4/25",
        "witness": exact_witness,
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
# Failure of the proposed Hamiltonian NEPv Rayleigh identity

**Status:** refuted
**Certificate level:** exact

## Statement

Immediately after equation (20), Section 6.2 of Amsel et al. asserts that its
block diagonal NEPv matrix has Rayleigh quotient equal to the product-state
objective in equation (19).

## Counterexample

With `n=2`, `d=1`, exact Hermitian norm-one matrices, and `x=(1,2)`, the
objective from equations (18)--(19) is exactly zero, while the proposed NEPv
Rayleigh quotient is exactly `-4/25`. The discrepancy occurs because an
`i=j` interaction is an expectation of a matrix product, not the product of
the two separate expectations.

## How to verify

Run `python verify.py`; it uses only exact rational arithmetic, raises on any
failed check, and writes the certificate artifact. As a mutation test, change
the upper-left entry of `K_1_1` from `0` to `1`; the exact-value assertions
fail.

## Artifacts

- `artifacts/certificate.json` — the exact matrices, vector, and unequal
  Rayleigh quotients.
```

```bibtex file=references.bib.add
@misc{AmselEtAl2026,
  author        = {Noah Amsel and Yves Baumann and Paul Beckman and Peter B\"urgisser and Chris Cama\~no and Tyler Chen and Edmond Chow and Anil Damle and Michal Derezinski and Mark Embree and Ethan N. Epperly and Robert Falgout and Mark Fornace and Anne Greenbaum and Chen Greif and Diana Halikias and Zhen Huang and Elias Jarlebring and Yiannis Koutis and Daniel Kressner and Rasmus Kyng and J\"org Liesen and Jackie Lok and Raphael A. Meyer and Yuji Nakatsukasa and Kate Pearce and Richard Peng and David Persson and Eliza Rebrova and Ryan Schneider and Rikhav Shah and Edgar Solomonik and Nikhil Srivastava and Alex Townsend and Robert J. Webber and Jess Williams},
  title         = {Linear Systems and Eigenvalue Problems: Open Questions from a Simons Workshop},
  year          = {2026},
  eprint        = {2602.05394},
  archivePrefix = {arXiv},
  primaryClass  = {math.NA},
  note          = {Version 2}
}
```
