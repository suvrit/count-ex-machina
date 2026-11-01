```json file=case.json
{
  "id": "sra-symmetric-alpha-permanent",
  "title": "A symmetric inverse M-matrix with non-log-supermodular principal alpha-permanents",
  "status": "refuted",
  "prose": "case.tex",
  "bib_keys": [
    "Sra2026"
  ],
  "results": [
    {
      "id": "sra-symmetric-alpha-permanent",
      "uid": null,
      "class": "external formal problem",
      "certificate_level": "exact",
      "theorem_label": "thm:sra-symmetric-alpha-permanent",
      "provenance": {
        "url": "https://arxiv.org/abs/2609.39979v1",
        "retrieved": "2026-11-01",
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
      "description": "Exact witness, inverse and decisive certificate values."
    }
  ]
}
```

```latex file=case.tex
\cxtitle{A symmetric inverse M-matrix with non-log-supermodular principal alpha-permanents}
\begin{cxcredits}
\posedby{Suvrit Sra \citeyearpar{Sra2026}}
\foundby{trureturing orchestration system}{2026-10}
\formalizedby{trureturing project (commit 9ef54496935, 28 October 2026)}
\auditedby{Codex, exact Python certificate rerun on 1 November 2026; no fresh Lean execution}
\contributedby{Haobo Ma and Wenlin Zhang}
\end{cxcredits}

\begin{cxcontext}
For a matrix $H$ indexed by $V$ and $\alpha>0$, use
$\operatorname{per}_\alpha(H)=\sum_{\pi\in\mathfrak S(V)}\alpha^{c(\pi)}\prod_{i\in V}H_{i,\pi(i)}$,
where fixed points count as cycles, and set the empty value to $1$.
An inverse $M$-matrix is nonnegative and invertible with nonpositive
off-diagonal inverse entries; it is symmetrizable when $DAD^{-1}$ is
symmetric for some positive diagonal $D$. A positive set function $f$ is
log-supermodular when $f(S\cup T)f(S\cap T)\geq f(S)f(T)$ for all $S,T$.
\end{cxcontext}

\begin{cxsource}{sra-symmetric-alpha-permanent}
Sra \cite[Section 4(b), p. 6]{Sra2026} asks: ``For symmetrizable inverse $M$-matrices and $\alpha\notin\{\tfrac12,1\}$, decide whether $S\mapsto\operatorname{per}_\alpha(A_S)$ is log-supermodular.\'\'
Sra \cite[Section 4(b), p. 6; equation (3.1)]{Sra2026} poses a yes/no question
for symmetrizable inverse $M$-matrices at positive orders other than $1/2$ and $1$.
The statement below is the universal affirmative assertion, faithfully
paraphrased with those exclusions. The witness disproves that assertion,
not a request for a complete characterization. Ma and Zhang's note dated
29 October 2026 and linked expository note and Lean source already record
this witness; no new discovery or priority is claimed for this packaging.
\end{cxsource}

\begin{cxstatement}{sra-symmetric-alpha-permanent}
For every symmetrizable inverse $M$-matrix $A$ and every
$\alpha>0$ with $\alpha\notin\{1/2,1\}$, the function
$S\mapsto\operatorname{per}_\alpha(A_S)$ is log-supermodular.
\end{cxstatement}

\begin{cxsummary}{sra-symmetric-alpha-permanent}
All positive orders other than $1/2$ and $1$ preserve principal
alpha-permanent log-supermodularity for symmetrizable inverse $M$-matrices.
\end{cxsummary}

\begin{cxcertificate}{sra-symmetric-alpha-permanent}
Exact symmetric $4\times4$ integer witness; gap
$\alpha^2(\alpha+1)(2401\alpha^2+1617\alpha-16)<0$ for $0<\alpha\leq1/200$.
\end{cxcertificate}

\begin{cxrefutation}
The affirmative extension of \cite[Section 4(b)]{Sra2026} fails even for a symmetric matrix.
\begin{theorem}[\statusfalse: all-order symmetric alpha-permanent extension]\label{thm:sra-symmetric-alpha-permanent}
There is a strictly entrywise positive symmetric inverse $M$-matrix whose
principal $\alpha$-permanents are not log-supermodular for every $0<\alpha\leq1/200$.
\end{theorem}
\begin{proof}
Use zero-based indices and take
\[
B=\begin{pmatrix}7&2&1&2\\2&7&2&1\\1&2&7&2\\2&1&2&7\end{pmatrix},\quad
B^{-1}=\frac1{24}\begin{pmatrix}4&-1&0&-1\\-1&4&-1&0\\0&-1&4&-1\\-1&0&-1&4\end{pmatrix}.
\]
The identity follows by multiplication; symmetry, positivity and inverse
off-diagonal signs give all hypotheses, with symmetrizing diagonal $I$.
Put $S=\{0,1,2\}$, $T=\{0,2,3\}$, $R=\{0,2\}$, and $U=\{0,1,2,3\}$.
For $f(V)=\operatorname{per}_\alpha(B_V)$, grouping by cycle count gives
\begin{align*}
f(R)&=\alpha+49\alpha^2,\\
f(S)=f(T)&=8\alpha+63\alpha^2+343\alpha^3,\\
f(U)&=48\alpha+257\alpha^2+882\alpha^3+2401\alpha^4.
\end{align*}
For $U$, four-cycles contribute $48$, a three-cycle and a fixed point
contribute $224$, two transpositions contribute $33$, one transposition
and two fixed points contribute $882$, and the identity contributes $2401$.
Multiplication gives
\[
f(U)f(R)-f(S)f(T)=\alpha^2(\alpha+1)(2401\alpha^2+1617\alpha-16).
\]
For $0<\alpha\leq1/200$, the last factor is at most
$2401/40000+1617/200-16=-314199/40000<0$.
At $\alpha=1/200$ the gap is $-63153999/320000000000$.
\end{proof}
\begin{remark}[Scope]
This disproves the all-order affirmative assertion, not the positive cases
$\alpha=1/2$, $\alpha=1$, or inverse tree graphs in Sra's Theorem 1.1 and
Remark 3.1. The inverse graph here is $C_4$. For this pair the gap is negative
exactly for $0<\alpha<(\sqrt{1153}-33)/98$. No classification of all
symmetrizable matrices at the remaining orders is claimed. The companion
four-cycle note proves the complete criterion for the uniform resolvent
family, a separate strengthening beyond this certificate. The linked Lean
source proves the specified refutation; no fresh Lean execution is asserted.
\end{remark}
\end{cxrefutation}
```

```python file=verify.py
from fractions import Fraction
from itertools import permutations
import json
from pathlib import Path


def cycle_count(permutation):
    visited = set()
    count = 0
    for start in range(len(permutation)):
        if start not in visited:
            count += 1
            current = start
            while current not in visited:
                visited.add(current)
                current = permutation[current]
    return count


def coefficients(matrix, indices):
    result = [Fraction(0)] * (len(indices) + 1)
    for permutation in permutations(range(len(indices))):
        product = Fraction(1)
        for row, column in enumerate(permutation):
            product *= matrix[indices[row]][indices[column]]
        result[cycle_count(permutation)] += product
    return result


def check_inverse(matrix, inverse):
    size = len(matrix)
    assert all(entry > 0 for row in matrix for entry in row)
    for row in range(size):
        for column in range(size):
            assert sum(matrix[row][inner] * inverse[inner][column] for inner in range(size)) == int(row == column)
            if row != column:
                assert inverse[row][column] <= 0


def convolution(first, second):
    result = [Fraction(0)] * (len(first) + len(second) - 1)
    for first_degree, first_coefficient in enumerate(first):
        for second_degree, second_coefficient in enumerate(second):
            result[first_degree + second_degree] += first_coefficient * second_coefficient
    return result


def evaluate(polynomial, argument):
    return sum(coefficient * argument**degree for degree, coefficient in enumerate(polynomial))

MATRIX = [[7, 2, 1, 2], [2, 7, 2, 1], [1, 2, 7, 2], [2, 1, 2, 7]]


def verify():
    inverse_numerator = [[4, -1, 0, -1], [-1, 4, -1, 0], [0, -1, 4, -1], [-1, 0, -1, 4]]
    inverse = [[Fraction(entry, 24) for entry in row] for row in inverse_numerator]
    check_inverse(MATRIX, inverse)
    assert all(MATRIX[row][column] == MATRIX[column][row] for row in range(4) for column in range(4))
    subsets = [(0, 2), (0, 1, 2), (0, 2, 3), (0, 1, 2, 3)]
    polynomials = [coefficients(MATRIX, indices) for indices in subsets]
    assert polynomials == [[0, 1, 49], [0, 8, 63, 343], [0, 8, 63, 343], [0, 48, 257, 882, 2401]]
    positive = convolution(polynomials[3], polynomials[0])
    negative = convolution(polynomials[1], polynomials[2])
    gap = [left - right for left, right in zip(positive, negative)]
    assert gap == convolution([0, 0, 1, 1], [-16, 1617, 2401]) + [Fraction(0)]
    alpha = Fraction(1, 200)
    quadratic_bound = 2401 * alpha**2 + 1617 * alpha - 16
    assert quadratic_bound == Fraction(-314199, 40000) < 0
    assert evaluate(gap, alpha) == Fraction(-63153999, 320000000000) < 0
    witness = {'matrix': MATRIX, 'inverse': [[str(entry) for entry in row] for row in inverse],
               'principal_polynomials_R_S_T_U': [[str(value) for value in polynomial] for polynomial in polynomials],
               'gap_coefficients_ascending': [str(value) for value in gap],
               'alpha': str(alpha), 'gap_at_alpha': str(evaluate(gap, alpha)),
               'quadratic_upper_bound_for_0_lt_alpha_le_1_over_200': str(quadratic_bound)}
    return {'id': 'sra-symmetric-alpha-permanent', 'ok': True,
            'summary': 'Symmetric positive inverse M witness; gap at alpha=1/200 is -63153999/320000000000.',
            'witness': witness}


if __name__ == '__main__':
    result = verify()
    artifacts = Path(__file__).resolve().parent / 'artifacts'
    artifacts.mkdir(exist_ok=True)
    (artifacts / 'certificate.json').write_text(json.dumps(result['witness'], indent=2, sort_keys=True) + '\n')
    print(f"PASS {result['id']}: {result['summary']}")
```

```markdown file=README.md
# A symmetric inverse M-matrix with non-log-supermodular principal alpha-permanents

**Status:** refuted
**Certificate level:** exact

## Statement
The affirmative assertion of Sra, Section 4(b), is paraphrased in case.tex, with its original hypotheses and quantifiers. Source: https://arxiv.org/abs/2609.39979v1.

## Counterexample
The symmetric four-by-four integer matrix B has a negative principal alpha-permanent gap at alpha=1/200, and throughout 0<alpha<=1/200.
The full witness, inverse, argument and limits of the conclusion are in case.tex.

## How to verify
Run `python3 verify.py`; it raises on any failed check and writes the exact certificate.
Use standard-library Python 3. No floating-point computation or external packages are used.

## Artifacts
- `artifacts/certificate.json`: exact matrix, inverse and decisive values.

## Notes and formal source
- [Public expository note (repository blueprint)](https://github.com/the-omega-institute/trureturing/blob/67b4fae085cf19003a33f8027410c383b49e5046/Blueprint/D5/S3/Combinatorics/Permanental/SraSymmetricAlphaPermanentRefutation.md).
- [Direct Lean source at the same verified commit](https://github.com/the-omega-institute/trureturing/blob/67b4fae085cf19003a33f8027410c383b49e5046/D5/S3/Combinatorics/Permanental/SraSymmetricAlphaPermanentRefutation.lean).
- Original two-page note: Ma and Zhang, 29 October 2026, correspondence note.

## Attribution and provenance facts still unavailable
The authors on the supplied notes are Haobo Ma then Wenlin Zhang. The witness was found by the trureturing orchestration system in October 2026 and formalized in the
trureturing project (commit 9ef54496935, 28 October 2026).
The current Python rerun certifies the finite arithmetic, not a new Lean build or a global novelty claim.

No issue or pull request has been opened by this preparation.
```

```bibtex file=references.bib.add
@misc{Sra2026,
  author = {Suvrit Sra},
  title = {A Koteljanskii inequality for permanents},
  year = {2026},
  eprint = {2609.39979},
  archivePrefix = {arXiv},
  url = {https://arxiv.org/abs/2609.39979v1},
  note = {Version 1, 30 September 2026}
}
```
