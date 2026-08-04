```json file=case.json
{
  "id": "osi-sketch-and-solve",
  "title": "An oblivious subspace injection need not give relative-error sketch-and-solve",
  "status": "refuted",
  "prose": "case.tex",
  "bib_keys": ["AmselEtAl2026", "TownsendWang2026"],
  "results": [
    {
      "id": "osi-sketch-and-solve",
      "uid": null,
      "class": "external formal problem",
      "certificate_level": "exact",
      "theorem_label": "thm:osi-sketch-and-solve",
      "provenance": {
        "url": "https://arxiv.org/html/2602.05394v2",
        "retrieved": "2026-08-04",
        "fidelity": "verbatim"
      }
    }
  ],
  "verify": { "python": "verify.py", "sage": [], "requires": [] },
  "artifacts": [
    { "file": "artifacts/certificate.json", "description": "Exact sketch atoms, probabilities, isotropy matrix, least-squares solutions, and residual ratios" }
  ]
}
```

```latex file=case.tex
\cxtitle{An oblivious subspace injection need not give relative-error sketch-and-solve}

\begin{cxcredits}
\posedby{Amsel et al. \citeyearpar{AmselEtAl2026}}
\foundby{OpenAI Codex}{2026-08}
\formalizedby{OpenAI Codex}
\auditedby{OpenAI Codex}
\contributedby{Suvrit Sra}
\end{cxcredits}

\begin{cxcontext}
For a random matrix $\Omega\in\mathbb R^{n\times k}$ and a fixed
$r$-dimensional subspace $\mathcal V\subseteq\mathbb R^n$, the source calls
$\Omega$ a subspace injection with injectivity $\alpha$ on $\mathcal V$ when
$\mathbb E\|\Omega^Tx\|_2^2=\|x\|_2^2$ for every $x\in\mathbb R^n$ and
$\|\Omega^Tx\|_2^2\geq\alpha\|x\|_2^2$ for every $x\in\mathcal V$.
It is oblivious with failure probability $\delta$ if this lower inequality
holds on every fixed $r$-dimensional subspace with probability at least
$1-\delta$.  When no failure probability is displayed, the source fixes a
small constant, specifically $\delta=0.01$ as its example.  The discussion
immediately following Problems~5.1--5.2 asks whether constant OSI failure
probability suffices and then separately asks whether reducing it to
$\operatorname{poly}(\varepsilon)$ rescues the result.  Thus the probabilistic
claim tested here is the natural one in that context: the relative-error event
should hold with at least the OSI success probability.  Townsend and Wang
subsequently gave related counterexamples and resolved the question negatively
\cite{TownsendWang2026}.
\end{cxcontext}

\begin{cxsource}{osi-sketch-and-solve}
Problem~5.1 of Amsel et al. \cite{AmselEtAl2026}.
\end{cxsource}

\begin{cxstatement}{osi-sketch-and-solve}
Let $A\in\mathbb{R}^{n\times d}$ be a full-rank matrix,
$B\in\mathbb{R}^{n\times p}$ be a matrix, and let
$\Omega\in\mathbb{R}^{n\times k}$ be an oblivious subspace injection with
dimension $d$ and injectivity $1-\varepsilon$. Let
$\widetilde{X}=(\Omega^{\top}A)^{+}(\Omega^{\top}B)\in\mathbb{R}^{d\times p}$
be the sketch-and-solve approximation to the ordinary least-squares solution
$X=A^{+}B$. (Here, ${}^{+}$ denotes the Moore--Penrose pseudoinverse.) Prove
or disprove: Does it necessarily hold that
\[
\|A\widetilde{X}-B\|_{\rm F}\leq(1+\mathcal{O}(\varepsilon))
\min_{X\in\mathbb{R}^{d\times p}}\|AX-B\|_{\rm F}?
\]
\end{cxstatement}

\begin{cxsummary}{osi-sketch-and-solve}
A one-dimensional oblivious subspace injection with injectivity $1$ can make
sketch-and-solve incur the fixed factor $\sqrt2$ with probability $1/50$.
\end{cxsummary}

\begin{cxcertificate}{osi-sketch-and-solve}
Three exact rationally weighted $2\times2$ sketch atoms, with exact isotropy,
an exact $99/100$ injection guarantee, and exact squared residual ratios.
\end{cxcertificate}

\begin{cxrefutation}
Problem~5.1 asks whether one-sided injectivity near $1$ yields the usual
relative-error guarantee for sketch-and-solve \cite{AmselEtAl2026}.  The
following three-atom distribution gives a negative answer under the failure
probability convention fixed in the source.

\begin{theorem}[\statusfalse: OSI relative error for sketch-and-solve]
\label{thm:osi-sketch-and-solve}
There is a $(1,1,1/100)$ oblivious subspace injection for which the claimed
relative-error inequality fails with probability $1/50$.  Consequently no
$1+O(\varepsilon)$ factor can hold with the OSI success probability, even
though the injectivity is exactly $1$.
\end{theorem}
\begin{proof}
Put $\rho=1/100$ and define
\[
 I=\begin{pmatrix}1&0\\0&1\end{pmatrix},\qquad
 B_+=\begin{pmatrix}1&0\\1&0\end{pmatrix},\qquad
 B_-=\begin{pmatrix}1&0\\-1&0\end{pmatrix}.
\]
Let $\Omega$ equal $I,B_+,B_-$ with respective probabilities
$1-2\rho,\rho,\rho$.  Its isotropy is exact:
\[
 \mathbb E[\Omega\Omega^T]
 =(1-2\rho)I+\rho
 \begin{pmatrix}1&1\\1&1\end{pmatrix}
 +\rho\begin{pmatrix}1&-1\\-1&1\end{pmatrix}=I.
\]
For $v=(x,y)^T$, the three possible values of
$\|\Omega^Tv\|_2^2$ are
\[
 x^2+y^2,\qquad (x+y)^2,\qquad (x-y)^2.
\]
The identity
$(x+y)^2+(x-y)^2=2(x^2+y^2)$ shows that at least one of the
last two values is at least $x^2+y^2$.  Hence, on every fixed line, the
injectivity-$1$ inequality can fail on at most one of the two atoms $B_+$ and
$B_-$, each of probability $\rho$.  Thus $\Omega$ is a
$(1,1,\rho)$-OSI, and in particular a $(1,1-\varepsilon,\rho)$-OSI for every
$\varepsilon\in(0,1)$.

Now take the single-response problem
\[
 A=\begin{pmatrix}1\\0\end{pmatrix},\qquad
 b=\begin{pmatrix}0\\1\end{pmatrix}.
\]
The unsketched optimum is $x_\star=0$ and its residual norm is $1$.  On the
identity atom, $\widetilde x=0$.  On the other atoms,
\[
 B_+^TA=\begin{pmatrix}1\\0\end{pmatrix},\quad
 B_+^Tb=\begin{pmatrix}1\\0\end{pmatrix},\qquad
 B_-^TA=\begin{pmatrix}1\\0\end{pmatrix},\quad
 B_-^Tb=\begin{pmatrix}-1\\0\end{pmatrix}.
\]
Therefore $\widetilde x=1$ on $B_+$ and $\widetilde x=-1$ on $B_-$, and in
both cases
\[
 \|A\widetilde x-b\|_2^2=\widetilde x^2+1=2.
\]
The fixed loss $\sqrt2$ occurs with total probability $2\rho=1/50$, whereas
the OSI failure probability is only $\rho=1/100$.

Finally, this is genuinely an asymptotic refutation of $1+O(\varepsilon)$.
If a universal constant $C>0$ supplied the hidden constant, choose
$\varepsilon>0$ so small that $C\varepsilon\leq1/4$.  The same sketch still
has injectivity at least $1-\varepsilon$, while on an event of probability
$1/50$ its ratio is $\sqrt2>5/4\geq1+C\varepsilon$.  No rounding or numerical
approximation is used.
\end{proof}
\end{cxrefutation}
```

```python file=verify.py
#!/usr/bin/env python3
"""Certify the exact three-atom OSI and its sketch-and-solve failure."""
from __future__ import annotations
from fractions import Fraction as F
import json
import pathlib


def transpose(a):
    return [list(row) for row in zip(*a)]


def matmul(a, b):
    return [
        [sum((a[i][t] * b[t][j] for t in range(len(b))), F(0))
         for j in range(len(b[0]))]
        for i in range(len(a))
    ]


def add_scaled(acc, scale, a):
    for i in range(len(a)):
        for j in range(len(a[0])):
            acc[i][j] += scale * a[i][j]


def gram(omega):
    return matmul(omega, transpose(omega))


def sketch_inner(omega, u, v):
    g = gram(omega)
    return sum((u[i] * g[i][j] * v[j]
                for i in range(len(u)) for j in range(len(v))), F(0))


def s(x):
    return str(x)


def verify() -> dict:
    """Raise AssertionError if any exact check fails; return a summary."""
    rho = F(1, 100)
    identity = [[F(1), F(0)], [F(0), F(1)]]
    b_plus = [[F(1), F(0)], [F(1), F(0)]]
    b_minus = [[F(1), F(0)], [F(-1), F(0)]]
    atoms = [(F(1) - 2 * rho, identity), (rho, b_plus), (rho, b_minus)]

    expectation = [[F(0), F(0)], [F(0), F(0)]]
    for probability, omega in atoms:
        add_scaled(expectation, probability, gram(omega))
    assert expectation == identity

    # The exact quadratic-form identity proves that, on every fixed line,
    # at least one of the two signed atoms has injectivity one.
    g_plus = gram(b_plus)
    g_minus = gram(b_minus)
    assert [[g_plus[i][j] + g_minus[i][j] for j in range(2)]
            for i in range(2)] == [[F(2), F(0)], [F(0), F(2)]]
    injection_success_lower_bound = F(1) - rho
    assert injection_success_lower_bound == F(99, 100)

    a = [F(1), F(0)]
    b = [F(0), F(1)]
    residuals = []
    bad_probability = F(0)
    for probability, omega in atoms:
        denominator = sketch_inner(omega, a, a)
        assert denominator > 0
        x_tilde = sketch_inner(omega, a, b) / denominator
        residual_squared = x_tilde * x_tilde + F(1)
        residuals.append((probability, x_tilde, residual_squared))
        if residual_squared > 1:
            bad_probability += probability
    assert residuals == [
        (F(49, 50), F(0), F(1)),
        (F(1, 100), F(1), F(2)),
        (F(1, 100), F(-1), F(2)),
    ]
    assert bad_probability == F(1, 50) > rho

    # For any proposed positive hidden constant C, epsilon=1/(4C)
    # makes (1+C epsilon)^2=25/16<2 on the bad atoms.
    assert F(25, 16) < F(2)

    witness = {
        "rho": s(rho),
        "atoms": [
            {"probability": s(p), "matrix": [[s(x) for x in row] for row in o]}
            for p, o in atoms
        ],
        "isotropy": [[s(x) for x in row] for row in expectation],
        "injection_success_probability_at_least": s(injection_success_lower_bound),
        "bad_probability": s(bad_probability),
        "squared_residual_ratios": [s(item[2]) for item in residuals],
    }
    return {
        "id": "osi-sketch-and-solve",
        "ok": True,
        "summary": "isotropy is exact; OSI success is at least 99/100; squared residual ratio 2 occurs with probability 1/50",
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
# An oblivious subspace injection need not give relative-error sketch-and-solve

**Status:** refuted
**Certificate level:** exact

## Statement
Problem 5.1 of Amsel et al. asks whether an oblivious subspace injection with injectivity near one necessarily gives a relative-error sketch-and-solve approximation at the OSI success probability.

## Counterexample
For a one-variable least-squares problem in two dimensions, a three-atom isotropic sketch distribution is injective on every fixed line with probability at least 99/100, yet produces residual ratio square root of two with probability 1/50.

## How to verify
Run `python verify.py`; it uses only exact rational arithmetic, raises on any failed check, and writes the artifact.

## Artifacts
- `artifacts/certificate.json` — exact sketch atoms, probabilities, isotropy, OSI success bound, and residual ratios.
```

```bibtex file=references.bib.add
@article{AmselEtAl2026,
  author  = {Noah Amsel and others},
  title   = {Linear Systems and Eigenvalue Problems: Open Questions from a Simons Workshop},
  journal = {arXiv preprint arXiv:2602.05394},
  year    = {2026},
  url     = {https://arxiv.org/abs/2602.05394}
}

@article{TownsendWang2026,
  author  = {Alex Townsend and Christopher Wang},
  title   = {Oblivious Subspace Injection Is Not Enough for Relative Error},
  journal = {arXiv preprint arXiv:2604.10215},
  year    = {2026},
  url     = {https://arxiv.org/abs/2604.10215}
}
```
