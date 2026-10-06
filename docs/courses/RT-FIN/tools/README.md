# Rebuilding the finite-group course

Install the requirements in a Python environment, then run `python tools/build.py` from this course directory. The builder checks every Markdown SHA-256 against `course.json`, renders only these 17 lessons, binds every labelled result to a stable anchor, writes the source/reader crosswalk, and checks local links and anchors. After deliberately editing a source, update its hash in the manifest before rebuilding. Source hashes are uppercase hexadecimal SHA-256 of the exact bytes.

The renderer modules are the selected CC0 mathematical Markdown renderer from the Open Research Courses R5C reader (21 September 2026), as subsequently extended for this course collection; `tools/renderer/PROVENANCE.md` describes the parser and its changes. This edition invokes only its Markdown/TeX rendering entry point. The RT-FIN wrapper, result-anchor projection, proof index and source/reader crosswalk are written for this edition by GPT-6.1 Sol (OpenAI), Ultra, in Codex.

The reader expects the shared site stylesheet and vendored MathJax under `../../assets/`. The downloadable reader/source archive preserves those paths and third-party notices. Serve its `docs/` directory with any static HTTP server and open `courses/RT-FIN/index.html`.
