```json file=case.json
{
  "id": "sdd-nystrom-diminishing-returns",
  "title": "Strict diagonal dominance does not ensure diminishing Nyström error reductions",
  "status": "refuted",
  "prose": "case.tex",
  "bib_keys": ["AmselEtAl2026", "Colbrook2026"],
  "results": [
    {
      "id": "sdd-nystrom-diminishing-returns",
      "uid": null,
      "class": "external formal problem",
      "certificate_level": "exact",
      "theorem_label": "thm:sdd-nystrom-diminishing-returns",
      "provenance": {
        "url": "https://arxiv.org/html/2602.05394v2",
        "retrieved": "2026-08-04",
        "fidelity": "verbatim"
      }
    }
  ],
  "verify": { "python": "verify.py", "sage": [], "requires": [] },
  "artifacts": [
    { "file": "artifacts/certificate.json", "description": "Exact matrix, diagonal-dominance margins, principal inverse traces, marginal reductions, and positive violation gap" }
  ]
}
```

```latex file=case.tex
\cxtitle{Strict diagonal dominance does not ensure diminishing Nystr\"om error reductions}

\begin{cxcredits}
\posedby{Mark Fornace \citeyearpar{AmselEtAl2026}}
\foundby{OpenAI Codex}{2026-08}
\formalizedby{OpenAI Codex}
\auditedby{OpenAI Codex}
\contributedby{Suvrit Sra}
\end{cxcredits}

\begin{cxcontext}
For a symmetric positive-definite matrix $L$ and $\gamma>0$, put
$K=(L+\gamma I)^{-1}$.  For a nonempty selected index set $\mathcal I$, the
nuclear Nystr\"om error is
\[
 F(\mathcal I)=\left\|K-K_{:,\mathcal I}
 K_{\mathcal I,\mathcal I}^{-1}K_{\mathcal I,:}\right\|_*.
\]
The residual is positive semidefinite, so its nuclear norm equals its trace.
The intended diminishing-error-reduction property is that, for
$S\subseteq T$ and $i\notin T$,
\[
 F(S)-F(S\cup\{i\})\geq F(T)-F(T\cup\{i\}).
\]
This formulation avoids the convention-dependent choice between the words
``submodular'' and ``supermodular'' for a decreasing error function.
Colbrook had already resolved Problem~4.6 in July 2026, proving the SDDM case
and giving exact SDD obstructions \cite{Colbrook2026}.  The matrix below was
found independently in August 2026; no priority over Colbrook is claimed.
\end{cxcontext}

\begin{cxsource}{sdd-nystrom-diminishing-returns}
Problem~4.6 of Amsel et al. \cite{AmselEtAl2026}, posed there by Mark Fornace.
Colbrook \cite{Colbrook2026} subsequently completed the answer before this
independent witness was found.
\end{cxsource}

\begin{cxstatement}{sdd-nystrom-diminishing-returns}
Prove or disprove the submodularity of the nuclear Nystr\"om error~(14) when
$L$ is assumed, in contrast to the above, to be (a) SDDM and positive-definite
or (b) SDD and positive-definite.
\end{cxstatement}

\begin{cxsummary}{sdd-nystrom-diminishing-returns}
A strictly diagonally dominant positive-definite $4\times4$ signed matrix has
a nonempty-base marginal Nystr\"om error reduction that increases after an
additional index is selected.
\end{cxsummary}

\begin{cxcertificate}{sdd-nystrom-diminishing-returns}
An exact integer $4\times4$ matrix, rational shift, four rational principal
inverse traces, and the positive violation gap $2165/14833896$.
\end{cxcertificate}

\begin{cxrefutation}
Problem~4.6 asks whether the nuclear Nystr\"om error retains diminishing
reductions for positive-definite SDDM or SDD matrices \cite{AmselEtAl2026}.
Part~(a) is true, while part~(b) is false \cite{Colbrook2026}.  Here is an
independently found exact witness for part~(b) with a nonempty base set.

\begin{theorem}[\statusfalse: SDD Nystr\"om diminishing returns]
\label{thm:sdd-nystrom-diminishing-returns}
The nuclear Nystr\"om error need not have diminishing error reductions when
$L$ is symmetric diagonally dominant and positive definite, even when $L$ is
strictly diagonally dominant and the comparison uses a nonempty base set.
\end{theorem}
\begin{proof}
Let
\[
 M=\begin{pmatrix}
 11&3&-4&3\\
 3&12&4&-1\\
 -4&4&14&-2\\
 3&-1&-2&11
 \end{pmatrix},\qquad
 \gamma=\frac12,\qquad L=M-\frac12I,
\]
and set $K=(L+\gamma I)^{-1}=M^{-1}$.  The diagonal entries of $L$ minus the
sums of the absolute values of the corresponding off-diagonal entries are
\[
 \frac12,\quad\frac72,\quad\frac72,\quad\frac92.
\]
Thus $L$ is symmetric strictly diagonally dominant with positive diagonal;
Gershgorin's theorem gives $L\succ0$.

For a selected set $\mathcal I$ with complement $J$, the block inverse
identity gives
\[
 K_{J,J}-K_{J,\mathcal I}K_{\mathcal I,\mathcal I}^{-1}
 K_{\mathcal I,J}=(M_{J,J})^{-1}.
\]
All other blocks of the Nystr\"om residual vanish.  Consequently
\[
 F(\mathcal I)=\operatorname{Tr}\bigl((M_{J,J})^{-1}\bigr).
\]

Use one-based indices, take the nonempty base $S=\{2\}$, and compare adding
$i=3$ before and after $j=4$.  Direct exact inversion of the four relevant
principal submatrices gives
\[
 F(\{2\})=\frac{100}{349},\qquad
 F(\{2,3\})=\frac{11}{56},\qquad
 F(\{2,4\})=\frac{25}{138},\qquad
 F(\{2,3,4\})=\frac1{11}.
\]
For example, the complement of $\{2\}$ is indexed by $\{1,3,4\}$; its
$3\times3$ principal submatrix has determinant $1396$ and the sum of its
three diagonal cofactors is $400$, yielding $400/1396=100/349$.

The two marginal error reductions are therefore
\[
 F(\{2\})-F(\{2,3\})=\frac{1761}{19544},\qquad
 F(\{2,4\})-F(\{2,3,4\})=\frac{137}{1518}.
\]
Their difference in the forbidden direction is
\[
 \frac{137}{1518}-\frac{1761}{19544}
 =\frac{2165}{14833896}>0.
\]
Hence selecting index $3$ reduces the error more, not less, after index $4$
has already been selected.  This exactly violates diminishing error
reductions.  Every displayed quantity is an integer or an exact rational.
\end{proof}
\end{cxrefutation}
```

```python file=verify.py
#!/usr/bin/env python3
"""Certify the exact strict-SDD Nyström diminishing-returns obstruction."""
from __future__ import annotations
from fractions import Fraction as F
import json
import pathlib


def identity(n):
    return [[F(int(i == j)) for j in range(n)] for i in range(n)]


def transpose(a):
    return [list(row) for row in zip(*a)]


def matmul(a, b):
    return [
        [sum((a[i][t] * b[t][j] for t in range(len(b))), F(0))
         for j in range(len(b[0]))]
        for i in range(len(a))
    ]


def inverse(a):
    n = len(a)
    aug = [list(a[i]) + identity(n)[i] for i in range(n)]
    for col in range(n):
        pivot = next(row for row in range(col, n) if aug[row][col] != 0)
        aug[col], aug[pivot] = aug[pivot], aug[col]
        scale = aug[col][col]
        aug[col] = [x / scale for x in aug[col]]
        for row in range(n):
            if row != col:
                factor = aug[row][col]
                aug[row] = [aug[row][j] - factor * aug[col][j]
                            for j in range(2 * n)]
    return [row[n:] for row in aug]


def principal(a, indices):
    return [[a[i][j] for j in indices] for i in indices]


def trace(a):
    return sum((a[i][i] for i in range(len(a))), F(0))


def ldl_pivots(a):
    n = len(a)
    lower = identity(n)
    pivots = [F(0) for _ in range(n)]
    for j in range(n):
        pivots[j] = a[j][j] - sum(
            (lower[j][k] * lower[j][k] * pivots[k] for k in range(j)), F(0)
        )
        assert pivots[j] != 0
        for i in range(j + 1, n):
            numerator = a[i][j] - sum(
                (lower[i][k] * lower[j][k] * pivots[k] for k in range(j)), F(0)
            )
            lower[i][j] = numerator / pivots[j]
    return pivots


def nystrom_residual(k, selected):
    n = len(k)
    chosen = sorted(selected)
    kii_inv = inverse(principal(k, chosen))
    k_col = [[k[i][j] for j in chosen] for i in range(n)]
    k_row = [[k[i][j] for j in range(n)] for i in chosen]
    approx = matmul(matmul(k_col, kii_inv), k_row)
    return [[k[i][j] - approx[i][j] for j in range(n)] for i in range(n)]


def s(x):
    return str(x)


def verify() -> dict:
    """Raise AssertionError if any exact check fails; return a summary."""
    m = [
        [F(11), F(3), F(-4), F(3)],
        [F(3), F(12), F(4), F(-1)],
        [F(-4), F(4), F(14), F(-2)],
        [F(3), F(-1), F(-2), F(11)],
    ]
    gamma = F(1, 2)
    l = [[m[i][j] - (gamma if i == j else F(0)) for j in range(4)]
         for i in range(4)]
    assert l == transpose(l)
    margins = [
        l[i][i] - sum((abs(l[i][j]) for j in range(4) if j != i), F(0))
        for i in range(4)
    ]
    assert margins == [F(1, 2), F(7, 2), F(7, 2), F(9, 2)]
    assert all(x > 0 for x in margins)
    assert all(x > 0 for x in ldl_pivots(l))

    k = inverse(m)
    assert matmul(m, k) == identity(4)
    sets = {
        "2": {1},
        "23": {1, 2},
        "24": {1, 3},
        "234": {1, 2, 3},
    }
    expected = {
        "2": F(100, 349),
        "23": F(11, 56),
        "24": F(25, 138),
        "234": F(1, 11),
    }
    errors = {}
    for name, selected in sets.items():
        complement = [i for i in range(4) if i not in selected]
        complement_formula = trace(inverse(principal(m, complement)))
        residual = nystrom_residual(k, selected)
        direct_formula = trace(residual)
        assert complement_formula == direct_formula
        # Exact LDL check on the nonzero principal residual block certifies PSD,
        # so its nuclear norm equals its trace.
        residual_block = principal(residual, complement)
        assert all(x > 0 for x in ldl_pivots(residual_block))
        errors[name] = direct_formula
    assert errors == expected

    first_reduction = errors["2"] - errors["23"]
    later_reduction = errors["24"] - errors["234"]
    gap = later_reduction - first_reduction
    assert first_reduction == F(1761, 19544)
    assert later_reduction == F(137, 1518)
    assert gap == F(2165, 14833896) > 0

    witness = {
        "M": [[s(x) for x in row] for row in m],
        "gamma": s(gamma),
        "strict_diagonal_dominance_margins_of_L": [s(x) for x in margins],
        "errors": {name: s(value) for name, value in errors.items()},
        "first_reduction": s(first_reduction),
        "later_reduction": s(later_reduction),
        "violation_gap": s(gap),
    }
    return {
        "id": "sdd-nystrom-diminishing-returns",
        "ok": True,
        "summary": "strict SDD margins are positive and the exact later-minus-earlier marginal reduction is 2165/14833896",
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
# Strict diagonal dominance does not ensure diminishing Nyström error reductions

**Status:** refuted
**Certificate level:** exact

## Statement
Problem 4.6(b) of Amsel et al., posed there by Mark Fornace, asks whether nuclear Nyström error has diminishing reductions for a positive-definite symmetric diagonally dominant matrix. Colbrook resolved the problem negatively in July 2026; this package records an independently found exact witness and does not claim priority.

## Counterexample
An integer 4 by 4 matrix, shifted by one half of the identity, is strictly SDD and positive definite. On a nonempty selected base, its two exact marginal error reductions differ in the forbidden direction by 2165/14833896.

## How to verify
Run `python verify.py`; it uses only exact rational arithmetic, raises on any failed check, and writes the artifact.

## Artifacts
- `artifacts/certificate.json` — exact matrix, shift, SDD margins, four errors, marginal reductions, and violation gap.
```

```bibtex file=references.bib.add
@article{AmselEtAl2026,
  author  = {Noah Amsel and others},
  title   = {Linear Systems and Eigenvalue Problems: Open Questions from a Simons Workshop},
  journal = {arXiv preprint arXiv:2602.05394},
  year    = {2026},
  url     = {https://arxiv.org/abs/2602.05394}
}

@article{Colbrook2026,
  author  = {Matthew J. Colbrook},
  title   = {Nystr\"om Error Beyond M-Matrices: A Minimal Diagonally Dominant Obstruction},
  journal = {arXiv preprint arXiv:2607.19282},
  year    = {2026},
  url     = {https://arxiv.org/abs/2607.19282}
}
```
