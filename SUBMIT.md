# Submit a counterexample with your AI agent

The short version: **paste the line below into Claude Code, Codex, Cursor, or
whatever agent you use.** You do not need to clone this repository, install
anything, or learn its layout.

```text
Read https://raw.githubusercontent.com/suvrit/count-ex-machina/main/SUBMIT.md
and follow it exactly to package the counterexample I have.
```

Then send us the one file it produces (see [Sending it](#sending-it)). We take
it from there.

Everything below is written for the agent.

---

## What this archive accepts

The archive is deliberately broad. The statement need not be famous — this is
not a collection of assaults on the great open problems, and catalogues such as
mathconjectures.com already cover those. A lemma stated in passing in a
preprint, a plausible strengthening on a problem list, or a "surely this holds"
from a forum thread is exactly what belongs here. Nor does it matter who the
user is: researcher, student, hobbyist, anyone.

What is not broad is the certificate. A counterexample is admissible only if
**all three** conditions hold. If one fails, say so plainly to the user and
stop — a case that cannot clear this bar wastes their time and ours.

1. **Provenance.** The refuted statement appeared publicly before the
   counterexample was sought — a paper, preprint, problem list, talk, or public
   forum post — or was posed formally and recorded in advance. A statement
   invented in the same session that refutes it does not qualify. Prominence is
   irrelevant; the point is only that the statement was not built to fall.
2. **No quantifier drift.** The original hypotheses and quantifiers are
   preserved exactly. If you tightened a hypothesis, widened a domain, or
   flipped a quantifier to make the witness work, you have refuted a *different*
   statement. Check this explicitly before packaging anything.
3. **Independent checkability.** The witness is verified by exact arithmetic
   (integers, `fractions.Fraction`, exact `sympy`, algebraic identities) or by a
   rigorous outward-rounded interval computation with explicit error control.
   **Floating-point evidence is inadmissible.** `float`, `numpy`, and bare
   `math` do not certify anything here.

Condition 3 is about checkability, not about tooling. Fifty lines of exact
rational Python satisfy it. So does a Lean, Rocq, or Isabelle development,
which is welcome and will be carried with the case — but do not treat one as
required, and do not tell the user their case is weaker without it. The harness
that runs on every push is Python plus optional Sage, so package a `verify.py`
either way.

A witness you found numerically and cannot yet certify is still welcome — but
say so, and send it as an issue rather than a package. Turning numerical
evidence into an exact certificate is much of what this archive is for.

## Rules you must not break

- **Never invent attribution or provenance.** Which model found the witness, in
  which month, who posed the statement, and where — these are facts about the
  world. If you do not know one, write `TODO` and tell the user which fact is
  missing. A plausible-looking guess is the single worst thing you can put in
  this package.
- **Never mark a quote `verbatim` unless you transcribed it from the source's
  own text.** Otherwise it is `paraphrase`, and the paper labels it as such.
- **Never weaken a check to make it pass.** If `verify.py` fails, the witness or
  the mathematics is wrong. Report that; do not adjust a threshold.
- **Do not invent a `uid` or an `order`.** Leave `uid` as `null` and omit
  `order` entirely — the maintainers assign both, and a value you make up will
  collide with a real one.
- **No LaTeX in the JSON, ever.** Every word you write in LaTeX belongs in
  `case.tex`; `case.json` carries ids, enums, dates and urls and nothing else.
  Write `$\mathcal{Y}$`, not `"$\\mathcal{Y}$"`.

## What to produce

**One markdown file**, containing exactly the fenced blocks below. The
`file=` tag in each fence is what tells our unpacker where the content goes, so
reproduce those tags exactly. Emit nothing outside the blocks except short
prose the maintainers should read.

Name it `<case-id>.md`, where `<case-id>` is kebab-case (lowercase letters,
digits, single hyphens) and names the mathematical object or claim — for
example `quantum-coupon-collector`, `rank-two-mixed-norm`.

````markdown
```json file=case.json
{
  "id": "<case-id>",
  "title": "<plain-text title, for the registry>",
  "status": "refuted",
  "prose": "case.tex",
  "bib_keys": ["<keys of the works you cite; the entries go in the bibtex block>"],
  "results": [
    {
      "id": "<usually the same as the case id; one entry per refuted statement>",
      "uid": null,
      "class": "<published theorem | published conjecture | external conjecture | external formal problem | user formal problem>",
      "certificate_level": "<exact | computer-assisted>",
      "theorem_label": "thm:<case-id>",
      "provenance": {
        "url": "<link to the copy you consulted>",
        "retrieved": "<YYYY-MM-DD>",
        "fidelity": "<verbatim | paraphrase>"
      }
    }
  ],
  "verify": { "python": "verify.py", "sage": [], "requires": [] },
  "artifacts": [
    { "file": "artifacts/certificate.json", "description": "<what it contains; plain text>" }
  ]
}
```

**No LaTeX goes in that JSON.** It holds machine facts only — ids, enums,
dates, urls. Every word you write in LaTeX goes in the file below, in regions
our build extracts. A `\begin{cx...}` and its `\end` must each sit alone on a
line, and regions may not nest. The four regions taking a result id repeat once
per refuted statement; most cases have exactly one.

```latex file=case.tex
\cxtitle{The title heading this case's section in the paper}

\begin{cxcredits}
\posedby{who posed the statement, with \citeyearpar{key} after a name}
\foundby{AI model name}{YYYY-MM of the session}
\formalizedby{who wrote the proof}
\auditedby{who checked the certificate}
\contributedby{who is submitting}
\end{cxcredits}

\begin{cxcontext}
Whatever notation and definitions the quoted statement depends on, so a reader
never has to open the source paper.  This is your prose, not the source's.
Delete this region if the statement needs no notation.
\end{cxcontext}

\begin{cxsource}{<result-id>}
Who posed it and where, with \cite{key} and a section or problem number.
\end{cxsource}

\begin{cxstatement}{<result-id>}
The statement exactly as originally posed, hypotheses and quantifiers intact.
Quote it; do not restate it in your own words unless fidelity is "paraphrase".
\end{cxstatement}

\begin{cxsummary}{<result-id>}
One line: the statement, for the ledger table.
\end{cxsummary}

\begin{cxcertificate}{<result-id>}
One line: what the certificate is, e.g. exact rational $3\times3$ witness and a
negative quadratic form.
\end{cxcertificate}

\begin{cxrefutation}
No \section heading and no credit line -- both are generated.

Prose introducing the conjecture, with \cite{key}.

\begin{theorem}[\statusfalse: short name]\label{thm:<case-id>}
  The claim, refuted as posed.
\end{theorem}
\begin{proof}
  The explicit witness with exact values, and how to read any displayed
  decimals -- e.g. "interpret all six-decimal entries as exact rationals of
  denominator $10^6$".
\end{proof}
\end{cxrefutation}
```

```python file=verify.py
#!/usr/bin/env python3
"""One line: what this certifies."""
from __future__ import annotations
import json
import pathlib


def verify() -> dict:
    """Raise AssertionError if any check fails; return a machine-readable summary."""
    # Exact checks only.  Assert the refutation, not a rounded shadow of it.
    return {
        "id": "<case-id>",
        "ok": True,
        "summary": "one line, including the key exact values",
        "witness": {},  # the exact data worth certifying; stringify Fractions
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
# <Title>

**Status:** refuted
**Certificate level:** <exact | computer-assisted>

## Statement
One paragraph, plain language, with the citation.

## Counterexample
One paragraph: what the witness is.

## How to verify
Run `python verify.py`; it raises on any failed check and writes the artifact.

## Artifacts
- `artifacts/certificate.json` — what it contains.
```

```bibtex file=references.bib.add
@article{YourKey2026,
  author  = {...},
  title   = {...},
  journal = {...},
  year    = {2026}
}
```
````

Omit the `bibtex` block if you cite nothing. Omit the `cxcontext` region only if
the statement genuinely needs no notation — that is rare.

If a block's own content contains a fence, open that block with **four**
backticks so the inner one cannot close it early.

## Check it before you send it

Run these yourself. They need nothing but Python 3.

1. `python verify.py` prints a `PASS` line and writes
   `artifacts/certificate.json`.
2. **Break the witness on purpose** — perturb one entry — and confirm
   `verify.py` now raises. A certificate that passes for any input certifies
   nothing, and this is the fastest way to catch one.
3. Search your own `verify.py` for `float(`, `numpy`, `math.`, and `0.1`-style
   decimal literals used in comparisons. Any hit is a defect unless it is
   `mpmath` at a declared precision with a stated error bound.
4. Re-read the quoted statement beside the theorem you refuted, clause by
   clause. Same hypotheses? Same quantifier order? Same domain?
5. Confirm every `\cite{key}` in your blocks has an entry in the bibtex block.

Then tell the user, in plain words: what was refuted, what the witness is, how
it was certified, and **every field you left as `TODO`**.

## Sending it

Either is fine:

- **Open an issue** using the *Submit a counterexample* template and paste the
  file in. Easiest if you have not cloned anything.
- **Open a pull request** adding the file as `submissions/<case-id>.md`. Nothing
  under `submissions/` is built or verified by CI, so a PR there cannot break
  the archive.

A maintainer unpacks the bundle into a case directory, assigns the `uid` and
ledger `order`, runs the certificate, and reviews the mathematics. Expect
questions — the admission bar is the point of this archive, and clearing it is
usually a conversation rather than a merge.

The full contributor documentation, if you want it: [CONTRIBUTING.md](CONTRIBUTING.md)
for the workflow, [AGENTS.md](AGENTS.md) for the repository's own agent brief,
and `tex/02-admission.tex` for the authoritative admission rule.
