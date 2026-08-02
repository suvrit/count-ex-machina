# Submission inbox

Drop a single bundle file here — `<case-id>.md`, in the format
[SUBMIT.md](../SUBMIT.md) specifies — and open a pull request.

Nothing in this directory is read by `tools/build.py` or run by CI, so a
submission cannot break the archive while it is being reviewed. A maintainer
unpacks it into `counterexamples/<case-id>/`, which is where the admission
checks apply.

If you have not cloned the repository, you do not need to: paste the bundle
into an issue instead, using the *Submit a counterexample* template.
