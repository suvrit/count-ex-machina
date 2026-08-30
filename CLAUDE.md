# CLAUDE.md

**Read [AGENTS.md](AGENTS.md).** It is the full brief for agents working in
this repository, and this file exists only so that Claude Code loads a pointer
to it automatically. Nested briefs: `counterexamples/AGENTS.md` (authoring a
case), `tex/AGENTS.md` (the paper), `tools/AGENTS.md` (the build).

If you read nothing else:

1. This archive's only claim is that **every counterexample recomputes** —
   exact arithmetic or rigorous intervals, never floating point. Do not weaken
   a check to make it pass.
2. **Never invent attribution or provenance.** Which model found a witness, in
   which month, and where a statement was posed are facts about the world.
   Leave the `TODO` and report it.
3. `tex/generated/`, `registry.json`, and the `README.md` case table are
   **generated**. Edit `case.json` or a `.tex` sidecar, then `make regen`.
   Everything else in `tex/` is the maintainer's prose. **You may draft
   anything; once a human has edited it, it is theirs — do not regenerate,
   reformat, or "resync" it unless asked in that session.** Report drift
   instead of fixing it. See "Who owns which file" in AGENTS.md.
4. `make check` and `make verify` **both pass** on a clean tree and must stay
   passing: any error either prints after your change is yours. CI runs the
   same two commands plus `git diff --exit-code`.
