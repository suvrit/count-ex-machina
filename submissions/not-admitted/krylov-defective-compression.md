```json file=case.json
{
  "id": "krylov-defective-compression",
  "title": "A defective full Krylov compression in Problem 3.5",
  "status": "refuted",
  "prose": "case.tex",
  "bib_keys": ["AmselEtAl2026"],
  "results": [
    {
      "id": "krylov-defective-compression",
      "uid": null,
      "class": "external formal problem",
      "certificate_level": "exact",
      "theorem_label": "thm:krylov-defective-compression",
      "provenance": {
        "url": "https://arxiv.org/abs/2602.05394v2",
        "retrieved": "2026-08-04",
        "fidelity": "verbatim"
      }
    }
  ],
  "verify": { "python": "verify.py", "sage": [], "requires": [] },
  "artifacts": [
    { "file": "artifacts/certificate.json", "description": "Exact integer data certifying cyclicity and defectiveness of the two-dimensional witness." }
  ]
}
```

```latex file=case.tex
\cxtitle{A defective full Krylov compression in Problem 3.5}

\begin{cxcredits}
\posedby{Rikhav Shah and Mark Embree \citeyearpar{AmselEtAl2026}}
\foundby{OpenAI Codex}{2026-08}
\formalizedby{OpenAI Codex}
\auditedby{OpenAI Codex}
\contributedby{Suvrit Sra}
\end{cxcredits}

\begin{cxcontext}
For a matrix $A$ and starting vector $b$, write
$\mathcal K_k(A,b)=\operatorname{span}\{b,Ab,\ldots,A^{k-1}b\}$.
If the compressed matrix $Q^*AQ$ has no eigenvector basis, we use the usual
extended-value convention $\kappa_V(Q^*AQ)=\infty$, the same convention used
in the discussion immediately following Problem~3.5.  The formal statement of
Problem~3.5 places no restriction $k<n$ on the dimension of the Krylov space,
although the subsequent motivating example does impose $k<n$.  The certificate
therefore tests the question exactly as written by taking the full Krylov space
in dimension two.  A ``random starting vector'' is taken in its standard sense,
for example a complex Gaussian vector; the argument applies to every
absolutely continuous distribution and also to the uniform distribution on the
unit sphere.
\end{cxcontext}

\begin{cxsource}{krylov-defective-compression}
Rikhav Shah and Mark Embree posed the question in
Problem~3.5 of \cite{AmselEtAl2026}, in the section on Ritz values and
approximate invariant subspaces.
\end{cxsource}

\begin{cxstatement}{krylov-defective-compression}
``Let $Q$ be an orthonormal basis for a Krylov space for arbitrary
$A\in\mathbb{C}^{n\times n}$ with random starting vector $b$. Is
$\kappa_V(Q^*AQ)$ bounded (by a polynomial in $n$) with high probability? Or
is $\mathbb{E}[\operatorname*{area}\Lambda_{\varepsilon}(Q^*AQ)]$ (the
expected value of the area in $\mathbb{C}$ of the $\varepsilon$-pseudospectrum)
bounded by $\mathrm{poly}(n)\varepsilon^{\beta}$ for $\beta$ close to 2? (This
problem is open even when $A$ is a circulant shift matrix.)''
\end{cxstatement}

\begin{cxsummary}{krylov-defective-compression}
The proposed high-probability polynomial bound on $\kappa_V(Q^*AQ)$ fails when
the unrestricted Krylov space is the full space.
\end{cxsummary}

\begin{cxcertificate}{krylov-defective-compression}
The certificate is the exact integer matrix $J_2$ and the polynomial identity
$\det[b,J_2b]=-v^2$ for $b=(u,v)^{\mathsf T}$.
\end{cxcertificate}

\begin{cxrefutation}
Problem~3.5 of \cite{AmselEtAl2026} asks, without restricting the Krylov
dimension, whether randomization of the starting vector makes the eigenvector
condition number of a Krylov compression polynomially bounded with high
probability.

\begin{theorem}[\statusfalse: polynomial conditioning of an unrestricted Krylov compression]\label{thm:krylov-defective-compression}
The first boundedness question in Problem~3.5 is false as posed: there is a
$2\times2$ matrix for which a standard random starting vector produces a full
Krylov compression with infinite eigenvector condition number almost surely.
\end{theorem}
\begin{proof}
Take
\[
A=J_2=\begin{bmatrix}0&1\\0&0\end{bmatrix},
\qquad b=\begin{bmatrix}u\\v\end{bmatrix}.
\]
Then
\[
Ab=\begin{bmatrix}v\\0\end{bmatrix},
\qquad
\det\begin{bmatrix}b&Ab\end{bmatrix}
=\det\begin{bmatrix}u&v\\v&0\end{bmatrix}=-v^2.
\]
For a complex Gaussian starting vector, and more generally for any
absolutely continuous random vector, $v\ne0$ almost surely.  The same holds for
a vector chosen uniformly from the unit sphere.  Hence
$\mathcal K_2(A,b)=\mathbb C^2$ almost surely.

Let $Q$ be any orthonormal basis for this Krylov space.  It is a square unitary
matrix, so $H=Q^*AQ$ is unitarily similar to $A$.  Exact multiplication gives
$A^2=0$ and $A\ne0$, and therefore $H^2=0$ and $H\ne0$.  A diagonalizable
nilpotent matrix is zero, so $H$ is defective.  Consequently
$\kappa_V(H)=\infty$ almost surely.  In particular it cannot be bounded by any
polynomial in $n=2$ with high probability.
\end{proof}
\end{cxrefutation}
```

```python file=verify.py
#!/usr/bin/env python3
"""Certify the exact cyclicity and defectiveness identities for the J2 witness."""
from __future__ import annotations
import json
import pathlib


Monomial = tuple[int, int]
Polynomial = dict[Monomial, int]


def add(p: Polynomial, q: Polynomial) -> Polynomial:
    """Add integer polynomials in the formal variables u and v."""
    out = dict(p)
    for monomial, coefficient in q.items():
        out[monomial] = out.get(monomial, 0) + coefficient
        if out[monomial] == 0:
            del out[monomial]
    return out


def neg(p: Polynomial) -> Polynomial:
    return {monomial: -coefficient for monomial, coefficient in p.items()}


def mul(p: Polynomial, q: Polynomial) -> Polynomial:
    """Multiply integer polynomials in the formal variables u and v."""
    out: Polynomial = {}
    for (pu, pv), pc in p.items():
        for (qu, qv), qc in q.items():
            monomial = (pu + qu, pv + qv)
            out[monomial] = out.get(monomial, 0) + pc * qc
    return {monomial: coefficient for monomial, coefficient in out.items() if coefficient}


def matmul(a: list[list[int]], b: list[list[int]]) -> list[list[int]]:
    return [
        [sum(a[i][k] * b[k][j] for k in range(len(b))) for j in range(len(b[0]))]
        for i in range(len(a))
    ]


def matvec_poly(a: list[list[int]], x: list[Polynomial]) -> list[Polynomial]:
    out: list[Polynomial] = []
    for row in a:
        value: Polynomial = {}
        for coefficient, polynomial in zip(row, x):
            value = add(value, {monomial: coefficient * c for monomial, c in polynomial.items()})
        out.append(value)
    return out


def verify() -> dict:
    """Raise AssertionError if any exact identity fails; return a certificate summary."""
    zero: Polynomial = {}
    u: Polynomial = {(1, 0): 1}
    v: Polynomial = {(0, 1): 1}
    a = [[0, 1], [0, 0]]

    ab = matvec_poly(a, [u, v])
    assert ab == [v, zero]

    # The two Krylov columns are b=(u,v)^T and Ab=(v,0)^T.
    determinant = add(mul(u, ab[1]), neg(mul(ab[0], v)))
    assert determinant == {(0, 2): -1}

    a_squared = matmul(a, a)
    assert a_squared == [[0, 0], [0, 0]]
    assert a != [[0, 0], [0, 0]]

    trace = a[0][0] + a[1][1]
    matrix_determinant = a[0][0] * a[1][1] - a[0][1] * a[1][0]
    assert trace == 0 and matrix_determinant == 0

    witness = {
        "matrix": [["0", "1"], ["0", "0"]],
        "starting_vector": ["u", "v"],
        "image_vector": ["v", "0"],
        "krylov_determinant": "-v^2",
        "exceptional_set": "v=0",
        "matrix_square": [["0", "0"], ["0", "0"]],
        "matrix_is_nonzero": True,
        "characteristic_polynomial": "lambda^2",
        "conclusion": "full Krylov compression is defective almost surely; kappa_V is infinite",
    }
    return {
        "id": "krylov-defective-compression",
        "ok": True,
        "summary": "det[b,Ab] = -v^2 and A is nonzero with A^2 = 0",
        "witness": witness,
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
# A defective full Krylov compression in Problem 3.5

**Status:** refuted
**Certificate level:** exact

## Statement
Problem 3.5 of Amsel et al. asks whether the eigenvector condition number of a
Krylov compression with a random starting vector is polynomially bounded with
high probability. The formal question does not restrict the Krylov space to
have dimension strictly smaller than the ambient dimension.

## Counterexample
Take the two-dimensional nilpotent Jordan block and its full Krylov space. For
a random starting vector with second coordinate nonzero, which occurs almost
surely under standard continuous distributions, the two Krylov vectors span
the full space. The compression is therefore unitarily similar to the defective
Jordan block and has infinite eigenvector condition number.

## How to verify
Run `python verify.py`; it raises on any failed exact identity and writes the
artifact.

## Artifacts
- `artifacts/certificate.json` — the exact matrix, polynomial determinant, and
  nilpotence certificate.
```

```bibtex file=references.bib.add
@article{AmselEtAl2026,
  author        = {Noah Amsel and others},
  title         = {Linear Systems and Eigenvalue Problems: Open Questions from a Simons Workshop},
  journal       = {arXiv preprint arXiv:2602.05394},
  year          = {2026},
  eprint        = {2602.05394},
  archivePrefix = {arXiv},
  primaryClass  = {math.NA}
}
```
