# Reproducing the course draft

The source ZIP is the complete twenty-four-lesson HTML and LaTeX edition of *Class field theory*. Authorship and mathematical self-check: OpenAI GPT-6.1 Sol in Codex, Ultra effort. No independent review is claimed.

Extract the ZIP into an empty directory. It has the same layout as the course repository: `courses/NT-CFT`, `scripts`, and `docs/assets`. The Markdown files and full LaTeX bodies are the authoritative supplied text. The catalogue describes exactly these twenty-four course lessons; the additional public course metadata preserves the surrounding navigation.

To reproduce the HTML pages, install Python 3.11 or later and `markdown-it-py==4.0.0`, then run:

```text
python courses/NT-CFT/build_course.py
```

Serve the `docs` directory with `python -m http.server 8000 --directory docs`, and open `/courses/NT-CFT/`. The source tree includes the MathJax scripts, fonts and notices required for the mathematical rendering. Other courses’ pages are outside this archive’s scope. Their metadata supplies navigation labels; the course coordinator supplies the surrounding programme edition.

The complete standalone sources are in `courses/NT-CFT/latex`. To compile the cumulative file, use XeLaTeX with the standard `article` class, `geometry`, `fontspec`, `amsmath`, `amssymb`, `mathtools`, `graphicx`, `xcolor`, `hyperref`, `bookmark`, and `enumitem`, and the TeX Gyre Pagella font. Run from the course directory so `assets/compatible-residues.png` resolves:

```text
xelatex -interaction=nonstopmode -halt-on-error -output-directory=latex latex/class-field-theory.tex
xelatex -interaction=nonstopmode -halt-on-error -output-directory=latex latex/class-field-theory.tex
```

The individual lesson files are equally complete, with the same preamble and their full text. They do not require hidden lesson inputs. The ZIP preserves these prepared files, so Pandoc is not needed to reproduce them. They were generated from the matching Markdown with Pandoc's `markdown+tex_math_single_backslash+raw_tex` reader and `latex` writer, with an explicit shared preamble and complete bodies. This edition's reading format is HTML; it makes no claim about a compiled PDF.

To regenerate the original diagram, install Node.js and `sharp`, then run `node courses/NT-CFT/figures/draw-compatible-residues.cjs`. It produces the SVG and its PNG export. The coordinates encode reduction modulo 2 and 4; the highlighted branch is the integer 3.

Run `node courses/NT-CFT/figures/draw-quadratic-norms.cjs` to regenerate the norm-subgroup comparison. It projects the two proved quadratic norm groups over the 2-adic rationals onto valuation and odd unit class modulo 4; each painted cell represents an entire class.

The renderer writes only this course's pages and explicitly listed assets. It never deletes other courses. The optional `--register --global-index` arguments are for integrating this course into a complete checkout of the existing programme; normal reproduction does not need them.

The course page displays the reading paths in `learning-structure.json` and the full study guide. `anchor-aliases.json` preserves earlier heading links in the three reorganized lessons. The builder validates every alias target before writing a page.

## Matching editions

The supplied HTML, Markdown and complete LaTeX bodies describe the same course draft. The prerequisite record separates written proofs from missing proofs. External scholarly reading is never an internal proof certificate. `SOURCE_MANIFEST.json` binds every other source-package file. No compiled PDF is supplied.

After rebuilding the reader, regenerate both downloadable archives and their hash manifests from the extracted package root:

```text
python courses/NT-CFT/package_course.py
```

This writes the source ZIP under `docs/courses/NT-CFT/files/` and the self-contained reader ZIP at the package root. It excludes previous ZIP archives and Python bytecode. It performs no TeX compilation.
