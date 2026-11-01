```json file=case.json
{
  "id": "sra-reciprocal-permanent-lorentzian",
  "title": "An inverse M-matrix with a non-Lorentzian reciprocal-permanent polynomial",
  "status": "refuted",
  "prose": "case.tex",
  "bib_keys": [
    "Sra2026",
    "BrandenHuh2020"
  ],
  "results": [
    {
      "id": "sra-reciprocal-permanent-lorentzian",
      "uid": null,
      "class": "external formal problem",
      "certificate_level": "exact",
      "theorem_label": "thm:sra-reciprocal-permanent-lorentzian",
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
\cxtitle{An inverse M-matrix with a non-Lorentzian reciprocal-permanent polynomial}
\begin{cxcredits}
\posedby{Suvrit Sra \citeyearpar{Sra2026}}
\foundby{trureturing orchestration system}{2026-10}
\formalizedby{trureturing project (commit 9ef54496935, 28 October 2026)}
\auditedby{Codex, exact Python certificate rerun on 1 November 2026; no fresh Lean execution}
\contributedby{Haobo Ma and Wenlin Zhang}
\end{cxcredits}

\begin{cxcontext}
For an entrywise nonnegative invertible matrix $A$, write $A_S=A[S,S]$,
$\operatorname{per}(A_\varnothing)=1$, and
$f_A(x_0,x)=\sum_{S\subseteq[n]}\operatorname{per}(A_S)^{-1}x_0^{n-|S|}\prod_{i\in S}x_i$.
An inverse $M$-matrix has $(A^{-1})_{ij}\leq0$ for $i\ne j$.
Lorentzian polynomials are coefficient limits of strictly Lorentzian
homogeneous polynomials. Every order-$(d-2)$ coordinate derivative of a
degree-$d$ Lorentzian polynomial has a Hessian with at most one positive
eigenvalue, by the recursive definition and continuity of eigenvalues
\cite[Definition 2.1]{BrandenHuh2020}.
\end{cxcontext}

\begin{cxsource}{sra-reciprocal-permanent-lorentzian}
Sra \cite[Section 4(d), p. 6]{Sra2026} asks: ``Is $f_A$ Lorentzian for every inverse $M$-matrix $A$?\'\'
Sra \cite[Section 4(d), p. 6]{Sra2026} poses the universal Lorentzianity
question. His Theorem 1.2 and Section 3.1 already give the matrix, its inverse,
and the four permanents used below. Ma and Zhang's additional conclusion
is non-Lorentzianity, written in a note dated 29 October 2026 and in the
linked expository note and Lean source. No discovery priority for Sra's matrix
is claimed. This yes/no question is recorded here through its affirmative
assertion, not as a refutation of a request to characterize a class.
\end{cxsource}

\begin{cxstatement}{sra-reciprocal-permanent-lorentzian}
For every inverse $M$-matrix $A$, the polynomial $f_A$ defined above is Lorentzian.
\end{cxstatement}

\begin{cxsummary}{sra-reciprocal-permanent-lorentzian}
The reciprocal-permanent polynomial of an inverse $M$-matrix is Lorentzian.
\end{cxsummary}

\begin{cxcertificate}{sra-reciprocal-permanent-lorentzian}
Exact $5\times5$ positive inverse $M$-matrix; a derivative Hessian is positive
definite on a two-dimensional plane, with determinant $1/20783363328$.
\end{cxcertificate}

\begin{cxrefutation}
The witness is Sra's existing matrix \cite[Theorem 1.2]{Sra2026}.
\begin{theorem}[\statusfalse: universal reciprocal-permanent Lorentzianity]\label{thm:sra-reciprocal-permanent-lorentzian}
There is a strictly entrywise positive inverse $M$-matrix $A$ for which $f_A$ is not Lorentzian.
\end{theorem}
\begin{proof}
Take
\[
A=\begin{pmatrix}13&1&7&7&7\\1&13&7&7&7\\1&1&7&7&7\\1&1&1&7&7\\1&1&1&1&7\end{pmatrix},\quad
A^{-1}=\frac1{84}\begin{pmatrix}7&0&-7&0&0\\0&7&-7&0&0\\0&0&14&-14&0\\0&0&0&14&-14\\-1&-1&0&0&14\end{pmatrix}.
\]
Multiplication gives $AA^{-1}=I$, and the inverse has the required signs.
With one-based indices $R=\{3,4,5\}$, $S=R\cup\{1\}$ and $T=R\cup\{2\}$,
the principal permanents of $R,S,T,[5]$ are $546,9996,9996,182784$.
Consequently
\[
q=\partial_3\partial_4\partial_5 f_A
=\frac{x_0^2}{546}+\frac{x_0(x_1+x_2)}{9996}+\frac{x_1x_2}{182784}.
\]
The Hessian restricted to the plane with basis $(e_0,e_1+e_2)$ is
\[
Q=\begin{pmatrix}1/273&1/4998\\1/4998&1/91392\end{pmatrix},\quad
Q_{11}>0,\quad\det Q=\frac1{20783363328}>0.
\]
Thus the Hessian has at least two positive eigenvalues. If $f_A$ were a
coefficient limit of strictly Lorentzian quintics, their threefold
derivatives would have Hessians with at most one positive eigenvalue.
Their restrictions would converge to the positive definite $Q$ and be
positive definite eventually, a contradiction.
\end{proof}
\begin{remark}[Scope]
This answers Section 4(d) negatively for general inverse $M$-matrices.
The example is not symmetrizable: its inverse has a non-symmetric zero
pattern, unchanged by positive diagonal similarity. It does not refute
Lorentzianity in the symmetrizable subclass or Sra's Theorem 1.1.
The exact Python certificate checks the finite premises; the preceding
analytic argument connects them to the Lorentzian definition. The linked
Lean development is supplied without claiming a new kernel or dependency audit.
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

MATRIX = [[13, 1, 7, 7, 7], [1, 13, 7, 7, 7], [1, 1, 7, 7, 7], [1, 1, 1, 7, 7], [1, 1, 1, 1, 7]]


def verify():
    inverse_numerator = [[7, 0, -7, 0, 0], [0, 7, -7, 0, 0], [0, 0, 14, -14, 0], [0, 0, 0, 14, -14], [-1, -1, 0, 0, 14]]
    inverse = [[Fraction(entry, 84) for entry in row] for row in inverse_numerator]
    check_inverse(MATRIX, inverse)
    subsets = [(2, 3, 4), (0, 2, 3, 4), (1, 2, 3, 4), (0, 1, 2, 3, 4)]
    permanents = [sum(coefficients(MATRIX, indices)) for indices in subsets]
    assert permanents == [546, 9996, 9996, 182784]
    first = 2 / permanents[0]
    mixed = 1 / permanents[1] + 1 / permanents[2]
    last = 2 / permanents[3]
    determinant = first * last - mixed**2
    assert first == Fraction(1, 273) and mixed == Fraction(1, 4998) and last == Fraction(1, 91392)
    assert determinant == Fraction(1, 20783363328) and first > 0
    assert inverse[0][2] < 0 and inverse[2][0] == 0
    witness = {'matrix': MATRIX, 'inverse': [[str(entry) for entry in row] for row in inverse],
               'principal_permanents_R_S_T_U': [str(value) for value in permanents],
               'restricted_hessian': [[str(first), str(mixed)], [str(mixed), str(last)]],
               'restricted_hessian_determinant': str(determinant)}
    return {'id': 'sra-reciprocal-permanent-lorentzian', 'ok': True,
            'summary': 'Positive inverse M witness; restricted Hessian determinant 1/20783363328 > 0.',
            'witness': witness}


if __name__ == '__main__':
    result = verify()
    artifacts = Path(__file__).resolve().parent / 'artifacts'
    artifacts.mkdir(exist_ok=True)
    (artifacts / 'certificate.json').write_text(json.dumps(result['witness'], indent=2, sort_keys=True) + '\n')
    print(f"PASS {result['id']}: {result['summary']}")
```

```markdown file=README.md
# An inverse M-matrix with a non-Lorentzian reciprocal-permanent polynomial

**Status:** refuted
**Certificate level:** exact

## Statement
The affirmative assertion of Sra, Section 4(d), is paraphrased in case.tex, with its original hypotheses and quantifiers. Source: https://arxiv.org/abs/2609.39979v1.

## Counterexample
Sra's own five-by-five matrix has a threefold derivative with a Hessian positive definite on a two-dimensional plane.
The full witness, inverse, argument and limits of the conclusion are in case.tex.

## How to verify
Run `python3 verify.py`; it raises on any failed check and writes the exact certificate.
Use standard-library Python 3. No floating-point computation or external packages are used.

## Artifacts
- `artifacts/certificate.json`: exact matrix, inverse and decisive values.

## Notes and formal source
- [Public expository note (repository blueprint)](https://github.com/the-omega-institute/trureturing/blob/67b4fae085cf19003a33f8027410c383b49e5046/Blueprint/D5/S3/Combinatorics/Permanental/SraReciprocalPermanentLorentzianRefutation.md).
- [Direct Lean source at the same verified commit](https://github.com/the-omega-institute/trureturing/blob/67b4fae085cf19003a33f8027410c383b49e5046/D5/S3/Combinatorics/Permanental/SraReciprocalPermanentLorentzianRefutation.lean).
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
@article{BrandenHuh2020,
  author = {Petter Br{\"a}nd{\'e}n and June Huh},
  title = {Lorentzian polynomials},
  journal = {Annals of Mathematics},
  volume = {192},
  number = {3},
  pages = {821--891},
  year = {2020},
  doi = {10.4007/annals.2020.192.3.4},
  url = {https://doi.org/10.4007/annals.2020.192.3.4}
}
```
