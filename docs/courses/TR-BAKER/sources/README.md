# Linear forms in logarithms: editable course

This edition contains Lessons 1–9, the available sections of Lesson 10, and Lessons 11–21 on powers of two and three, S-unit gaps, 3x+1 cycles, the many-to-two logarithm reduction, the effective unit equation, Thue equations, effective irrationality bounds, binomial families, S-unit and primitive Thue–Mahler equations, superelliptic and hyperelliptic equations, affine curves of genus one, Mordell bounds, the Ramanujan–Nagell equation, primitive divisors, effective Catalan finiteness, fixed-variable Pillai equations, quadratic forms and class numbers, products of Dirichlet L-functions and their explicit limit formula, the complete class-number-one argument and the genus-character reduction for class number two, the Stewart–Tijdeman construction for abc triples and effective bounds in terms of their radicals, the Stewart–Yu one-third bound and its least-greatest-prime refinement, and complete equation resolutions by continued fractions and certified lattice reduction. Each `TR-BAKER-NN.tex` contains the full current text of the corresponding lesson, including its proofs, examples, exercises, solutions and references. The full course has 22 lessons. Its figures are in `../figures/`; no further files are required.

To compile a lesson, change into this `sources` directory and run `pdflatex -output-directory=.. TR-BAKER-NN.tex` twice. This places the PDF beside its online reader. Use a current TeX distribution with the packages named in the file. Pandoc 3.9.0.2 generated the editable LaTeX from the Markdown in `../src/`. The LaTeX itself does not require Pandoc.

The course download preserves the `docs/courses/TR-BAKER` and `docs/assets` directories. It contains every current lesson, the complete LaTeX files, original figures and their programs, verification programs, the course renderer, CSS, MathJax and their licence notices. From the extracted root, run:

```text
python -m pip install markdown-it-py
python docs/courses/TR-BAKER/build_reader.py --readers
python docs/courses/TR-BAKER/build_reader.py --tex --pandoc pandoc
python -m http.server 8000 --directory docs
```

Read the course at `http://localhost:8000/courses/TR-BAKER/`. Proof links to earlier programme courses refer to those courses in the full repository; they are not duplicated in this course download. The included readers can be read offline, with local mathematics rendering. To regenerate the ZIP, run `build_reader.py --archive` with the intended destination filename. Some figure and symbolic programs need Matplotlib, NumPy, SymPy or mpmath; the class-number Fourier certificate uses mpmath interval arithmetic, and its figure program runs that certificate; `verification/padic_examples.py` uses only Python's standard library.

The lessons link freely accessible human sources. No cited source files are included. Original exposition, solutions, figures and course code are CC0. Cited works and bundled software and font glyphs retain their own licences and notices. AI authors and self-checkers: GPT-6.1 Sol and GPT-6 Astra (OpenAI), Ultra. The course manifest specifies their contributions.
