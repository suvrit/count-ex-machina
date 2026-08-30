#!/usr/bin/env python3
"""Flatten the paper into arxiv/ for an arXiv upload: `make arxiv`.

arXiv wants few files and no build system, so tex/ is folded into three:

  arxiv/main.tex      tex/main.tex with generated/metadata, 01, 02, ledger,
                      cases (and every case.tex it \\inputs) and 07 inlined,
                      the bibliography spliced in as a thebibliography, and
                      the appendix \\inputs replaced by one \\input{appendix}
  arxiv/appendix.tex  the appendix files in main.tex's order, with their
                      case.tex's and generated/appendix-brief inlined
  arxiv/cxcase.sty    a verbatim copy

The source becomes public on arXiv, so whole-line comments are dropped,
trailing comment text is cut back to a bare % (which still eats the newline,
so TeX sees the same tokens), and \\iffalse ... \\fi blocks are removed.  Blank
lines are never inserted -- a blank line inside the ledger's longtable would
be a \\par -- and runs of them are collapsed to two.

arxiv/ is regenerated wholesale every run: edit tex/, not arxiv/.  The
bibliography comes from a bibtex run here, so tex/main.bbl is never trusted;
the folder is then compiled once more from its three files alone, and the run
fails if that build has an undefined reference or citation.  main.pdf is
left behind for inspection (gitignored); the aux files are cleaned.

Stdlib only.
"""
from __future__ import annotations

import re
import shutil
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
TEX = ROOT / "tex"
OUT = ROOT / "arxiv"

# The appendix \input's of tex/main.tex, in its order.  Kept in step with
# main.tex by check, not by trust: an \input there that is not listed here is
# inlined into main.tex, and a name listed here that main.tex does not \input
# is an error.
APPENDIX = [
    "09-additional",
    "03-proof-details",
    "04-aim36-pencil",
    "05-macdonald-omega",
    "06-quantum-coupon-trace",
    "08-lorentzian-audit",
]

INPUT_RE = re.compile(r"^\s*\\input\{([^}]+)\}\s*(%.*)?$")
IF_RE = re.compile(r"\\if(?!f\b)[a-zA-Z@]*")  # every \if... except the math \iff
FI_RE = re.compile(r"\\fi\b")
PAGES_RE = re.compile(r"Output written on main\.pdf \((\d+) pages")


def resolve(arg: str) -> Path:
    p = TEX / arg
    if p.suffix != ".tex":
        p = p.with_suffix(".tex")
    return p.resolve()


def rel(p: Path) -> str:
    return p.relative_to(ROOT).as_posix()


def comment_index(line: str) -> int:
    """Index of the first unescaped %, or -1."""
    i = 0
    while i < len(line):
        if line[i] == "\\":
            i += 2
            continue
        if line[i] == "%":
            return i
        i += 1
    return -1


def code(line: str) -> str:
    k = comment_index(line)
    return line if k < 0 else line[:k]


def clean(lines: list[str], where: str) -> list[str]:
    """Drop whole-line comments, trailing comment text and \\iffalse blocks."""
    out: list[str] = []
    i = 0
    while i < len(lines):
        line = lines[i]
        if code(line).lstrip().startswith(r"\iffalse"):
            depth, j = 0, i
            while True:
                depth += len(IF_RE.findall(code(lines[j]))) - len(FI_RE.findall(code(lines[j])))
                if depth <= 0:
                    break
                j += 1
                if j == len(lines):
                    sys.exit(f"error: unclosed \\iffalse at {where}:{i + 1}")
            print(f"  dropped \\iffalse block {where}:{i + 1}-{j + 1}")
            i = j + 1
            continue
        k = comment_index(line)
        if k >= 0:
            if not line[:k].strip():
                i += 1
                continue  # whole-line comment
            line = line[:k] + "%"  # trailing comment: keep the bare %
        else:
            line = line.rstrip()
        out.append(line)
        i += 1
    return out


def flatten(path: Path, inlined: list[str]) -> list[str]:
    if not path.exists():
        sys.exit(f"error: {rel(path)} does not exist")
    inlined.append(rel(path))
    out: list[str] = []
    for line in clean(path.read_text().splitlines(), rel(path)):
        m = INPUT_RE.match(line)
        if m:
            target = resolve(m.group(1))
            out.append(f"% ==== {rel(target)} ====")
            out.extend(flatten(target, inlined))
            out.append(f"% ==== end {rel(target)} ====")
        else:
            out.append(line)
    return out


def collapse(lines: list[str]) -> list[str]:
    out: list[str] = []
    blanks = 0
    for line in lines:
        blanks = blanks + 1 if not line.strip() else 0
        if blanks <= 2:
            out.append(line)
    return out


def header(what: str) -> list[str]:
    proc = subprocess.run(
        ["git", "describe", "--always", "--dirty"], cwd=ROOT, capture_output=True, text=True
    )
    commit = proc.stdout.strip() or "unknown"
    return [
        f"% arXiv snapshot: {what}, flattened from tex/ at commit {commit}",
        "% by tools/flatten_arxiv.py (`make arxiv`).  Every \\input is inlined;",
        "% comments and disabled blocks are removed.  Edit tex/, not this file.",
        "",
    ]


def build_main(inlined: list[str]) -> list[str]:
    out = header("tex/main.tex")
    seen_appendix: list[str] = []
    for line in clean((TEX / "main.tex").read_text().splitlines(), "tex/main.tex"):
        m = INPUT_RE.match(line)
        if not m:
            out.append(line)
            continue
        name = m.group(1)
        if name in APPENDIX:
            if not seen_appendix:
                out.append(r"\input{appendix}")
            seen_appendix.append(name)
            continue
        target = resolve(name)
        out.append(f"% ==== {rel(target)} ====")
        out.extend(flatten(target, inlined))
        out.append(f"% ==== end {rel(target)} ====")
    if seen_appendix != APPENDIX:
        sys.exit(
            "error: the appendix \\input's of tex/main.tex are "
            f"{seen_appendix}, but APPENDIX in tools/flatten_arxiv.py says {APPENDIX}; "
            "update the list"
        )
    return collapse(out)


def build_appendix(inlined: list[str]) -> list[str]:
    out = header("the appendices of tex/main.tex")
    for name in APPENDIX:
        target = resolve(name)
        out.append(f"% ==== {rel(target)} ====")
        out.extend(flatten(target, inlined))
        out.append(f"% ==== end {rel(target)} ====")
        out.append("")
    return collapse(out)


def splice_bbl(main_lines: list[str], bbl: str) -> list[str]:
    """Replace \\bibliographystyle + \\bibliography with the .bbl's contents."""
    out: list[str] = []
    style = biblio = 0
    for line in main_lines:
        if line.startswith(r"\bibliographystyle{"):
            style += 1
            continue
        if line.startswith(r"\bibliography{"):
            biblio += 1
            out.extend(bbl.rstrip("\n").splitlines())
            continue
        out.append(line)
    if (style, biblio) != (1, 1):
        sys.exit(
            f"error: expected one \\bibliographystyle and one \\bibliography in "
            f"tex/main.tex, found {style} and {biblio}"
        )
    return out


def latexmk(*args: str) -> subprocess.CompletedProcess:
    try:
        return subprocess.run(
            ["latexmk", *args], cwd=OUT, capture_output=True, text=True
        )
    except FileNotFoundError:
        sys.exit("error: latexmk not found on PATH")


def compile_pdf(what: str) -> None:
    proc = latexmk("-pdf", "-interaction=nonstopmode", "main")
    if proc.returncode != 0:
        (OUT / "flatten-arxiv.log").write_text(proc.stdout + proc.stderr)
        sys.exit(
            f"error: {what} failed; see arxiv/main.log and arxiv/flatten-arxiv.log "
            "(arxiv/ is left as it was for inspection)"
        )


def report(log: str) -> int:
    """Print what the standalone build's log says; return the number of errors."""
    pages = PAGES_RE.search(log)
    print(f"  pages: {pages.group(1) if pages else '?'}")
    print(f"  overfull boxes: {log.count('Overfull')}")
    warnings = [
        ln.rstrip()
        for ln in log.splitlines()
        if ("Warning" in ln or "undefined" in ln) and "Overfull" not in ln
    ]
    for w in warnings:
        print(f"  {w}")
    fatal = [w for w in warnings if "undefined" in w or "Citation" in w or "Reference" in w]
    return len(fatal)


def main() -> int:
    OUT.mkdir(exist_ok=True)
    inlined: list[str] = []
    print("flattening")
    main_lines = build_main(inlined)
    appendix_lines = build_appendix(inlined)
    (OUT / "main.tex").write_text("\n".join(main_lines) + "\n")
    (OUT / "appendix.tex").write_text("\n".join(appendix_lines) + "\n")
    shutil.copyfile(TEX / "cxcase.sty", OUT / "cxcase.sty")
    print("inlined, in order:")
    for p in inlined:
        print(f"  {p}")

    print("bibtex run (with tex/references.bib copied in)")
    bib = OUT / "references.bib"
    shutil.copyfile(TEX / "references.bib", bib)
    latexmk("-C")
    compile_pdf("the bibtex build")
    bbl = (OUT / "main.bbl").read_text()
    print(f"  {bbl.count(chr(92) + 'bibitem')} entries folded into arxiv/main.tex")
    (OUT / "main.tex").write_text("\n".join(splice_bbl(main_lines, bbl)) + "\n")
    bib.unlink()
    latexmk("-C")
    (OUT / "main.bbl").unlink(missing_ok=True)

    print("standalone build (main.tex, appendix.tex, cxcase.sty only)")
    compile_pdf("the standalone build")
    fatal = report((OUT / "main.log").read_text())
    latexmk("-c")
    (OUT / "main.synctex.gz").unlink(missing_ok=True)
    if fatal:
        print(f"error: {fatal} undefined reference/citation warning(s) in the standalone build")
        return 1
    print("wrote arxiv/main.tex, arxiv/appendix.tex, arxiv/cxcase.sty (and arxiv/main.pdf to look at)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
