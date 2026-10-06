# Building the matrix-extension reading

The `src/`, `tex/`, `pdf/` and `figures/` directories contain the exact editable lesson files and their rendered outputs. The complete three-lesson reader uses native MathML and needs no network connection for its mathematics or figures. Links to further lessons in the Open Mathematics Courses collection and external scholarly readings need an internet connection.

To rebuild the HTML readers, install Python 3 with Beautiful Soup 4 and Pandoc, then run from this directory:

```text
python build/build_reader.py --pandoc pandoc
```

To rebuild a PDF, use a current LuaLaTeX distribution with the packages named in the corresponding TeX file. Run from `tex/`, so the original relative figure paths remain correct:

```text
lualatex -interaction=nonstopmode -halt-on-error matrix-extension.tex
lualatex -interaction=nonstopmode -halt-on-error matrix-extension.tex
lualatex -interaction=nonstopmode -halt-on-error stable-prerequisite-bridges.tex
lualatex -interaction=nonstopmode -halt-on-error metric-foundation-bridges.tex
```

Move the rebuilt PDFs from `tex/` into `pdf/`. PDF metadata and byte hashes may vary with the engine and build date; the distributed PDF bytes are identified by `checksums.sha256`. The source files and figure assets preserve the released mathematical content exactly.

To regenerate the two map figures, install Matplotlib and run each Python file in `figures/`. Both PNG and editable SVG outputs are produced beside the figure source.

The reader builder preserves every original TeX formula in its MathML annotation. Visible equation labels use MathML text while retaining the original label. The build converts legacy fraction/font syntax only for the HTML renderer and keeps the original source and annotated formula intact. The combined lessons retain GFDL 1.2 only; notices and the complete license are in `component-notices/`.
