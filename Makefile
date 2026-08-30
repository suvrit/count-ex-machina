# One-command entry points.  `make check` is the gate every pull request must
# pass, and it is the same pair of commands CI runs.
#
# Override the interpreter if you are not using the repo venv:
#     make check PY=python3

PY ?= .venv/bin/python

.DEFAULT_GOAL := help
.PHONY: help venv new unpack check verify regen paper preview arxiv all clean

help:
	@echo "make venv    create .venv and install the pinned dependencies"
	@echo "make new     scaffold a new counterexample (interactive)"
	@echo "make unpack BUNDLE=submissions/x.md   unpack a SUBMIT.md bundle"
	@echo "make check   validate metadata + verify every certificate  <- the PR gate"
	@echo "make verify  run every counterexample's verify.py only"
	@echo "make regen   regenerate the case metadata, registry, README table"
	@echo "make paper   build tex/main.pdf"
	@echo "make preview CASE=<id>   compile one case on its own"
	@echo "make arxiv   flatten tex/ into arxiv/ for an arXiv upload"
	@echo "make all     check, then build the paper"
	@echo "make clean   remove LaTeX build artifacts"

venv:
	python3 -m venv .venv
	.venv/bin/pip install --no-deps -r requirements.txt

new:
	@$(PY) tools/new_case.py

# Maintainer side of SUBMIT.md: one contributed markdown bundle -> a case dir.
unpack:
	@$(PY) tools/unpack_submission.py $(BUNDLE)

# build.py --check fails if any metadata is incomplete or any generated file is
# stale; verify_all.py recomputes every certificate from scratch.
check:
	$(PY) tools/build.py --check
	$(PY) tools/verify_all.py

verify:
	$(PY) tools/verify_all.py

regen:
	$(PY) tools/build.py

paper:
	cd tex && latexmk -pdf main

# One case, typeset on its own while it is being written.  Metadata (heading
# level, verbatim vs paraphrase) is not applied; see tools/preview_case.py.
preview:
	@$(PY) tools/preview_case.py $(CASE)

# arXiv upload: tex/ flattened into arxiv/{main.tex,appendix.tex,cxcase.sty},
# bibliography folded in, then compiled once to prove it stands alone.
arxiv:
	@$(PY) tools/flatten_arxiv.py

all: check paper

clean:
	cd tex && latexmk -C
