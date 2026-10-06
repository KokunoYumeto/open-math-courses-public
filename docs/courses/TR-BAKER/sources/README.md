# Linear forms in logarithms: editable course

Each `TR-BAKER-NN.tex` contains the complete corresponding lesson, including its proofs, examples, exercises, solutions and references. Its figures are in `../figures/`; no further files are required.

To compile a lesson, change into this `sources` directory and run `pdflatex TR-BAKER-NN.tex` twice. Use a current TeX distribution with the packages named in the file. Pandoc 3.9.0.2 generated the editable LaTeX from the Markdown in `../src/`. The LaTeX itself does not require Pandoc.

The course download preserves the `docs/courses/TR-BAKER` and `docs/assets` directories. It contains every current lesson, the complete LaTeX files, original figures and their programs, verification programs, the course renderer, CSS, MathJax and their licence notices. From the extracted root, run:

```text
python -m pip install markdown-it-py
python docs/courses/TR-BAKER/build_reader.py --readers
python docs/courses/TR-BAKER/build_reader.py --tex --pandoc pandoc
python -m http.server 8000 --directory docs
```

Read the course at `http://localhost:8000/courses/TR-BAKER/`. Proof links to earlier programme courses refer to those courses in the full repository; they are not duplicated in this course download. The included readers can be read offline, with local mathematics rendering. To regenerate the ZIP, run `build_reader.py --archive` with the intended destination filename. Some older figure and symbolic programs need Matplotlib, NumPy or SymPy; `verification/padic_examples.py` uses only Python's standard library.

The lessons link freely accessible human sources. No cited source files are included. Original exposition, solutions, figures and course code are CC0. Cited works and bundled software and font glyphs retain their own licences and notices. AI author: GPT-6.1 Sol (OpenAI), Ultra, October 2026.
