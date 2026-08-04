```json file=case.json
{
  "id": "qrcp-orthonormal-greedy",
  "title": "Exact QRCP can miss the orthonormal-row conditioning bound",
  "status": "refuted",
  "prose": "case.tex",
  "bib_keys": ["AmselEtAl2026", "ChenLiuHeDong2026"],
  "results": [
    {
      "id": "qrcp-orthonormal-greedy",
      "uid": null,
      "class": "external formal problem",
      "certificate_level": "exact",
      "theorem_label": "thm:qrcp-orthonormal-greedy",
      "provenance": {
        "url": "https://arxiv.org/html/2602.05394v2",
        "retrieved": "2026-08-04",
        "fidelity": "verbatim"
      }
    }
  ],
  "verify": { "python": "verify.py", "sage": [], "requires": [] },
  "artifacts": [
    { "file": "artifacts/certificate.json", "description": "Exact rational Grassmann-chart witness, projector, QRCP residual table and strict pivot gaps, and a rational Rayleigh certificate for failure of the conditioning bound" }
  ]
}
```

```latex file=case.tex
\cxtitle{Exact QRCP can miss the orthonormal-row conditioning bound}

\begin{cxcredits}
\posedby{Anil Damle and Daniel Kressner \citeyearpar{AmselEtAl2026}}
\foundby{OpenAI Codex}{2026-08}
\formalizedby{OpenAI Codex}
\auditedby{OpenAI Codex}
\contributedby{Suvrit Sra}
\end{cxcredits}

\begin{cxcontext}
Let $Q\in\mathbb R^{n\times k}$ have orthonormal columns.  Exact
Businger--Golub QR with column pivoting (QRCP) applied to $Q^T$ repeatedly
chooses a remaining column with largest squared residual after orthogonal
projection away from the previously chosen columns.  If $P=QQ^T$ and the
previously chosen indices form $S$, the squared residual of index $i$ is the
Schur complement
\[
 \rho_S(i)=P_{ii}-P_{iS}P_{SS}^{-1}P_{Si}.
\]
Thus the exact pivot path depends only on the orthogonal projector $P$.

Chen, Liu, He, and Dong first answered Problem~4.3 negatively by an
asymptotic low-coherence family \cite{ChenLiuHeDong2026}.  Their construction
prescribes a long upper-triangular selected block and then completes the
identity with several blocks of extra columns.  The finite witness below was
found later and independently.  It instead specifies a small rational point
in a Grassmann chart, takes its projector directly, and has only $k=3$ and
$n=8$.  No priority over Chen--Liu--He--Dong is claimed.
\end{cxcontext}

\begin{cxsource}{qrcp-orthonormal-greedy}
Problem~4.3 of Amsel et al. \cite{AmselEtAl2026}, sourced there to Anil Damle
and Daniel Kressner.  Chen, Liu, He, and Dong \cite{ChenLiuHeDong2026} were
the first to publish a negative resolution.
\end{cxsource}

\begin{cxstatement}{qrcp-orthonormal-greedy}
``It is known that there exists $I$ such that
$\|Q(I,:)^{-1}\|_2\leq\sqrt{k(n-k+1)}$ [HP92] and there is a fairly efficient
$O(nk^2)$ algorithm that satisfies this bound [Osi25].''  Problem~4.3 then
asks: ``Does the QRCP algorithm typically used in practice satisfy the above,
or a similar, bound.''
\end{cxstatement}

\begin{cxsummary}{qrcp-orthonormal-greedy}
For an exact rational rank-three projector on eight coordinates, QRCP has
strict pivots $I=(1,2,3)$ but the resulting inverse norm exceeds $\sqrt{18}$.
\end{cxsummary}

\begin{cxcertificate}{qrcp-orthonormal-greedy}
An exact rational $8\times3$ Grassmann-chart matrix, three positive rational
pivot gaps, and the Rayleigh gap $192051/250000$.
\end{cxcertificate}

\begin{cxrefutation}
Problem~4.3 asks whether classical QRCP itself attains the conditioning scale
known to be achievable by a suitable subset-selection algorithm
\cite{AmselEtAl2026}.  The full question was first answered negatively by
Chen, Liu, He, and Dong \cite{ChenLiuHeDong2026}.  Here is a different,
small, exact counterexample to the displayed bound.

\begin{theorem}[\statusfalse: QRCP orthonormal-row bound]
\label{thm:qrcp-orthonormal-greedy}
There are $n=8$, $k=3$, and $Q\in\mathbb R^{8\times3}$ with $Q^TQ=I_3$
such that exact Businger--Golub QRCP applied to $Q^T$ makes three strict
pivot choices $I=(1,2,3)$, while
\[
 \|Q(I,:)^{-1}\|_2>\sqrt{k(n-k+1)}=\sqrt{18}.
\]
\end{theorem}
\begin{proof}
Put $V=\binom{I_3}{W}$, where
\[
 W=\frac1{1000}\begin{pmatrix}
 707&-23&-985\\
 1639&1259&-985\\
 1639&1259&-985\\
 -707&23&985\\
 1639&1259&-985
 \end{pmatrix},
 \qquad H=V^TV=I_3+W^TW,
\]
and define $Q=VH^{-1/2}$ using the positive-definite square root.  Then
$Q^TQ=I_3$, and its projector is the rational matrix
$P=QQ^T=VH^{-1}V^T$.  Hence all QRCP decisions can be certified using
rational arithmetic alone.

For completeness, exact Schur-complement evaluation gives the following
pivot residual and runner-up residual at each step:
\[
\begin{array}{c|c|c|c|c}
 S & \text{pivot} & \rho_S(\text{pivot}) &
 \max_{i\notin S\cup\{\text{pivot}\}}\rho_S(i)&\text{gap}\\ \hline
 \varnothing&1&\dfrac{100874772187}{197275840682}&
 \dfrac{99899751883}{197275840682}&
 \dfrac{487510152}{98637920341}\\[5pt]
 \{1\}&2&\dfrac{4179375000}{14410681741}&
 \dfrac{28781505000}{100874772187}&
 \dfrac{474120000}{100874772187}\\[5pt]
 \{1,2\}&3&\dfrac{8000}{46809}&
 \dfrac{38809}{234045}&
 \dfrac{397}{78015}
\end{array}
\]
Every gap is positive, so tie handling is irrelevant and QRCP selects
$I=(1,2,3)$.

The selected matrix is $Q(I,:)=H^{-1/2}$, so
\[
 \|Q(I,:)^{-1}\|_2^2=\lambda_{\max}(H)
 =1+\lambda_{\max}(W^TW).
\]
For the integer vector $x=(2,1,-1)^T$, direct exact arithmetic gives
\[
 \|Wx\|_2^2-17\|x\|_2^2=\frac{192051}{250000}>0.
\]
Consequently $\lambda_{\max}(W^TW)>17$, whence
$\|Q(I,:)^{-1}\|_2^2>18=k(n-k+1)$.  This is the claimed strict
counterexample.
\end{proof}
\end{cxrefutation}
```

```python file=verify.py
#!/usr/bin/env python3
"""Certify an exact rank-three QRCP counterexample using rational arithmetic."""
from __future__ import annotations

import json
import pathlib
from fractions import Fraction as F


def transpose(a):
    return [list(row) for row in zip(*a)]


def matmul(a, b):
    bt = transpose(b)
    return [[sum((x * y for x, y in zip(row, col)), F(0)) for col in bt]
            for row in a]


def identity(n):
    return [[F(i == j) for j in range(n)] for i in range(n)]


def inverse(a):
    n = len(a)
    aug = [row[:] + identity(n)[i] for i, row in enumerate(a)]
    for col in range(n):
        pivot = next(i for i in range(col, n) if aug[i][col] != 0)
        aug[col], aug[pivot] = aug[pivot], aug[col]
        scale = aug[col][col]
        aug[col] = [x / scale for x in aug[col]]
        for i in range(n):
            if i != col:
                scale = aug[i][col]
                aug[i] = [x - scale * y for x, y in zip(aug[i], aug[col])]
    return [row[n:] for row in aug]


def principal(a, indices):
    return [[a[i][j] for j in indices] for i in indices]


def schur_residuals(p, selected):
    if not selected:
        return [p[i][i] for i in range(len(p))]
    pinv = inverse(principal(p, selected))
    out = []
    for i in range(len(p)):
        u = [p[i][j] for j in selected]
        correction = sum(
            (u[a] * pinv[a][b] * u[b]
             for a in range(len(selected)) for b in range(len(selected))),
            F(0),
        )
        out.append(p[i][i] - correction)
    return out


def fs(x):
    return str(x.numerator) if x.denominator == 1 else f"{x.numerator}/{x.denominator}"


def verify() -> dict:
    """Raise AssertionError if any exact check fails; return a summary."""
    w = [
        [F(707, 1000), F(-23, 1000), F(-985, 1000)],
        [F(1639, 1000), F(1259, 1000), F(-985, 1000)],
        [F(1639, 1000), F(1259, 1000), F(-985, 1000)],
        [F(-707, 1000), F(23, 1000), F(985, 1000)],
        [F(1639, 1000), F(1259, 1000), F(-985, 1000)],
    ]
    v = identity(3) + w
    h = matmul(transpose(v), v)
    assert h == [[identity(3)[i][j] + matmul(transpose(w), w)[i][j]
                  for j in range(3)] for i in range(3)]
    hinv = inverse(h)
    p = matmul(matmul(v, hinv), transpose(v))

    # P is exactly the rank-three orthogonal projector QQ^T.
    assert p == transpose(p)
    assert matmul(p, p) == p
    assert sum((p[i][i] for i in range(8)), F(0)) == 3

    selected = []
    residual_tables = []
    gaps = []
    for _ in range(3):
        residuals = schur_residuals(p, selected)
        remaining = [i for i in range(8) if i not in selected]
        ordered = sorted(remaining, key=lambda i: (-residuals[i], i))
        pivot, runner_up = ordered[0], ordered[1]
        gap = residuals[pivot] - residuals[runner_up]
        assert gap > 0
        residual_tables.append({
            "selected_before": [i + 1 for i in selected],
            "pivot": pivot + 1,
            "pivot_residual": fs(residuals[pivot]),
            "runner_up_residual": fs(residuals[runner_up]),
            "strict_gap": fs(gap),
        })
        gaps.append(gap)
        selected.append(pivot)

    assert selected == [0, 1, 2]
    assert gaps == [
        F(487510152, 98637920341),
        F(474120000, 100874772187),
        F(397, 78015),
    ]

    # Q = V H^(-1/2), so Q({1,2,3},:)^(-1) has squared norm
    # lambda_max(H)=1+lambda_max(W^T W).  A rational Rayleigh vector
    # certifies lambda_max(W^T W)>17 without computing any radicals.
    x = [[F(2)], [F(1)], [F(-1)]]
    wx = matmul(w, x)
    wx_sq = sum((row[0] ** 2 for row in wx), F(0))
    x_sq = sum((row[0] ** 2 for row in x), F(0))
    rayleigh_gap = wx_sq - 17 * x_sq
    assert x_sq == 6
    assert rayleigh_gap == F(192051, 250000) > 0

    witness = {
        "n": 8,
        "k": 3,
        "W": [[fs(x) for x in row] for row in w],
        "V": [[fs(x) for x in row] for row in v],
        "P": [[fs(x) for x in row] for row in p],
        "pivot_sequence_one_based": [i + 1 for i in selected],
        "pivot_steps": residual_tables,
        "rayleigh_vector": ["2", "1", "-1"],
        "rayleigh_gap_over_17": fs(rayleigh_gap),
        "claimed_bound_squared": "18",
    }
    return {
        "id": "qrcp-orthonormal-greedy",
        "ok": True,
        "summary": "strict QRCP pivots are 1,2,3 and the exact Rayleigh gap over the squared bound is 192051/250000",
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
# Exact QRCP can miss the orthonormal-row conditioning bound

**Status:** refuted
**Certificate level:** exact

## Statement
Problem 4.3 of Amsel et al., sourced there to Anil Damle and Daniel Kressner, asks whether practical QRCP attains the displayed bound for selecting rows from a matrix with orthonormal columns. Chen, Liu, He, and Dong first published a negative resolution in June 2026. This package records a later independent witness and claims no priority.

## Counterexample
A rational 8 by 3 Grassmann-chart matrix defines an exact rank-three orthogonal projector. Its three QRCP pivots are strict and select rows 1, 2, 3, but a rational Rayleigh certificate proves that the inverse norm of the selected 3 by 3 matrix is strictly larger than sqrt(18).

## How to verify
Run `python verify.py`; it uses only exact rational arithmetic, raises on any failed check, and writes the artifact.

## Artifacts
- `artifacts/certificate.json` — exact rational chart, projector, pivot residuals and gaps, and the Rayleigh certificate.
```

```bibtex file=references.bib.add
@article{AmselEtAl2026,
  author  = {Noah Amsel and others},
  title   = {Linear Systems and Eigenvalue Problems: Open Questions from a Simons Workshop},
  journal = {arXiv preprint arXiv:2602.05394},
  year    = {2026},
  url     = {https://arxiv.org/abs/2602.05394}
}

@article{ChenLiuHeDong2026,
  author  = {Leheng Chen and Zihao Liu and Wanyi He and Bin Dong},
  title   = {Iteris: Agentic Research Loops for Computational Mathematics},
  journal = {arXiv preprint arXiv:2606.02484},
  year    = {2026},
  url     = {https://arxiv.org/abs/2606.02484}
}
```
