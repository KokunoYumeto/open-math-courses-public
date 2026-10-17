# Reader sources

This package renders **Artin’s axioms** and **Moduli stacks are algebraic** from their complete editable Markdown and TeX sources. The course archive also contains all twelve lessons, the component and licence records, and the genus-two figure data and drawing sources.

Use Python 3.11 or later. Install the build dependencies and choose a fresh output directory:

```sh
python -m pip install -r reader-source/requirements-build.txt
python reader-source/build_reader.py --output reader-output
```

Run these commands from the course directory containing `course.json`. The two HTML readers appear under `reader-output/courses/AG-AS/`. The build checks its explicit input catalogue, TeX payloads, heading aliases, mathematical passage hashes and writing credits. Its output must match the reader identities recorded in the catalogue. Source edits require corresponding updates to the source and heading catalogues; the pinned edition check deliberately rejects changed inputs.

For browser validation, install the additional dependencies and a Playwright Chromium browser:

```sh
python -m pip install -r reader-source/requirements-check.txt
python -m playwright install chromium
python reader-source/validate_reader.py --site reader-output --report reader-check
```

An installed Microsoft Edge browser can be selected with `--channel msedge`. Validation splits each complete reader into ordered heading fragments whose concatenation is exactly the original lesson body. It checks every formula, font loading, browser errors, mobile page width and horizontal access to wide equations. Exact cached fragment checks retain their asset and policy identities and are reported separately from fresh rendering. Temporary HTML fragments are removed after each check. These checks establish reproducibility and rendering behaviour; they do not establish mathematical correctness or independent scholarly review.

The source archive includes the exact MathJax runtime, fonts and notices. A repository checkout can instead use the same hash-bound shared files in `docs/assets/`. Course CSS and JavaScript accompany the sources. Cross-course theorem links require the corresponding companion courses in the collection for offline navigation.

The renderer is original Open Mathematics Courses programme code, drawn from the course renderer accompanying *Cohomology of quasi-coherent sheaves*. The course builder and browser validator were written by GPT-6.1 Sol (OpenAI), Codex, Ultra. Mathematical exposition and supplementary arguments retain their separate credits in `components.json` and the lessons. MathJax retains Apache-2.0 and the font terms in its accompanying notices; the mathematical text’s licence does not replace dependency terms.
