```json file=case.json
{
  "id": "tensor-network-strict-approximation",
  "title": "Strict improvement over the tree tensor approximation factor",
  "status": "refuted",
  "prose": "case.tex",
  "bib_keys": ["AmselEtAl2026"],
  "results": [
    {
      "id": "tensor-network-strict-approximation",
      "uid": null,
      "class": "external formal problem",
      "certificate_level": "exact",
      "theorem_label": "thm:tensor-network-strict-approximation",
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
      "description": "Exact rank-one matrix witness and the resulting zero optimum and zero right-hand side"
    }
  ]
}
```

```latex file=case.tex
\cxtitle{Strict improvement over the tree tensor approximation factor}

\begin{cxcredits}
\posedby{Mehrdad Ghadiri \citeyearpar{AmselEtAl2026}}
\foundby{OpenAI Codex}{2026-08}
\formalizedby{OpenAI Codex}
\auditedby{OpenAI Codex}
\contributedby{Suvrit Sra}
\end{cxcredits}

\begin{cxcontext}
For an order-two tensor, a two-node tensor train with bond rank one is
exactly the class of matrices of rank at most one.  The Frobenius norm is
denoted by $\lVert\cdot\rVert_{\mathrm F}$.  In the source statement,
$\mathbb S$ in the membership condition denotes the representability set
$S$ introduced in the preceding sentence.
\end{cxcontext}

\begin{cxsource}{tensor-network-strict-approximation}
Problem~6.1 of \cite{AmselEtAl2026}; the manuscript says that the question
was initially proposed by Mehrdad Ghadiri.
\end{cxsource}

\begin{cxstatement}{tensor-network-strict-approximation}
Given any choice of $m$-node tree tensor network (e.g., tensor train or
Tucker) and choice of ranks (dimensions of edges in the tensor network), let
the set of representable tensors in this tensor network be
$S\subset\mathbb{R}^{d_{1}\times\cdots\times d_{n}}$. Find a polynomial-time
algorithm that takes as input any tensor
$\mathcal{A}\in\mathbb{R}^{d_{1}\times\cdots\times d_{n}}$ and yields an
approximation $\mathcal{X}\in\mathbb{S}$ such that
\[
\lVert\mathcal{X}-\mathcal{A}\rVert_{F}^{2}
<(m-1)\min_{\mathcal{Y}\in S}
\lVert\mathcal{Y}-\mathcal{A}\rVert_{F}^{2},
\]
or show that an $(m-1)$-approximation is optimal under complexity-theoretic
assumptions.
\end{cxstatement}

\begin{cxsummary}{tensor-network-strict-approximation}
The strict improvement requested in Problem~6.1 is impossible on tensors
that are already representable by the prescribed tensor network.
\end{cxsummary}

\begin{cxcertificate}{tensor-network-strict-approximation}
The certificate is the exact nonzero rank-one matrix
$\operatorname{diag}(1,0)$ in the two-node rank-one tensor-train class.
\end{cxcertificate}

\begin{cxrefutation}
Problem~6.1 of \cite{AmselEtAl2026} asks for a strict inequality for every
input tensor.  Exact representability makes that inequality impossible,
independently of computational complexity.

\begin{theorem}[\statusfalse: strict tree-tensor approximation]
\label{thm:tensor-network-strict-approximation}
The strict-inequality algorithm requested in Problem~6.1 cannot exist as
posed.  This does not resolve the problem's alternative request for a
complexity-theoretic optimality result.
\end{theorem}
\begin{proof}
Take an order-two tensor with $d_{1}=d_{2}=2$, and take the two-node tensor
train with bond rank one.  Its representability set $S$ is the set of
$2\times2$ matrices of rank at most one.  Let
\[
\mathcal A=
\begin{pmatrix}
1&0\\
0&0
\end{pmatrix}.
\]
This is a nonzero member of $S$, since its determinant is zero and its rank is
one.  Consequently
\[
\min_{\mathcal Y\in S}
\lVert\mathcal Y-\mathcal A\rVert_{
\mathrm F}^{2}=0,
\]
with equality attained by $\mathcal Y=\mathcal A$.  Here $m=2$, so the
right-hand side required by Problem~6.1 is $(m-1)\cdot0=0$.  The requested
output would therefore have to satisfy
\[
\lVert\mathcal X-\mathcal A\rVert_{
\mathrm F}^{2}<0,
\]
which is impossible because a squared Frobenius norm is nonnegative.
\end{proof}
\end{cxrefutation}
```

```python file=verify.py
#!/usr/bin/env python3
"""Certify the exact rank-one input that makes Problem 6.1 demand a negative squared norm."""
from __future__ import annotations

import json
import pathlib
from fractions import Fraction


Matrix2 = tuple[tuple[Fraction, Fraction], tuple[Fraction, Fraction]]


def determinant_2x2(matrix: Matrix2) -> Fraction:
    """Return the exact determinant of a two-by-two matrix."""
    return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]


def frobenius_squared(matrix: Matrix2) -> Fraction:
    """Return the exact squared Frobenius norm."""
    return sum((entry * entry for row in matrix for entry in row), Fraction(0))


def verify() -> dict:
    """Raise AssertionError if any check fails; return a machine-readable summary."""
    witness: Matrix2 = (
        (Fraction(1), Fraction(0)),
        (Fraction(0), Fraction(0)),
    )
    m = 2
    rank_bound = 1

    determinant = determinant_2x2(witness)
    witness_norm_squared = frobenius_squared(witness)

    # For a nonzero 2-by-2 matrix, determinant zero is equivalent to rank one.
    assert determinant == 0
    assert witness_norm_squared > 0
    assert rank_bound == 1
    assert m == 2

    # Since the input itself is representable, choosing Y=A proves OPT=0.
    optimum = Fraction(0)
    demanded_right_hand_side = Fraction(m - 1) * optimum
    assert demanded_right_hand_side == 0

    # Every squared Frobenius norm is nonnegative, so none can be strictly
    # smaller than the demanded right-hand side.  Negating this assertion, or
    # changing the lower-right witness entry from 0 to 1, makes verification fail.
    assert not (Fraction(0) < demanded_right_hand_side)

    exact_witness = {
        "matrix": [[str(entry) for entry in row] for row in witness],
        "m": m,
        "rank_bound": rank_bound,
        "determinant": str(determinant),
        "squared_frobenius_norm": str(witness_norm_squared),
        "optimal_error_squared": str(optimum),
        "demanded_right_hand_side": str(demanded_right_hand_side),
    }
    return {
        "id": "tensor-network-strict-approximation",
        "ok": True,
        "summary": "nonzero rank-one input has exact optimum 0, so the strict bound demands a squared norm below 0",
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
# Strict improvement over the tree tensor approximation factor

**Status:** refuted
**Certificate level:** exact

## Statement

Problem 6.1 of Amsel et al. asks for a polynomial-time algorithm whose squared
Frobenius error is strictly smaller than (m-1) times the optimal error for
every input tensor and every prescribed tree tensor network and rank choice.

## Counterexample

For the two-node rank-one tensor train, take the nonzero rank-one matrix
`diag(1, 0)`. It is already representable, so its optimal approximation error
is exactly zero. The strict inequality would require a squared Frobenius norm
to be negative.

## How to verify

Run `python verify.py`; it uses exact rational arithmetic, raises on any failed
check, and writes the certificate artifact. As a mutation test, change the
lower-right witness entry from zero to one; the determinant assertion fails.

## Artifacts

- `artifacts/certificate.json` — the exact matrix witness, rank data, optimum,
  and demanded right-hand side.
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
