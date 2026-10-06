# Operator algebras: representations, derivations and core traces

The eight lesson sources are in `src/`. The reader preserves every complete TeX formula and the stable result anchors listed in `results.json`.

Use Python 3.10 or later:

```console
python -m pip install -r requirements.txt
python build_reader.py
python -m http.server 8000
```

Open `http://localhost:8000/`. The bundled MathJax renderer needs no external scripts or fonts. The prerequisite links lead to the current online companion readings; those readings are not included in this eight-lesson archive.

To create the portable archive, choose a destination outside this directory:

```console
python build_reader.py --archive ../group-representations-and-covariance.zip
```

The ZIP sorts its files, fixes timestamps and permissions, and contains the lesson sources, reader, build script, mathematical result index, references and component notices. With identical inputs and Python compression runtime its bytes are reproducible.

Original lesson authorship and the actual human references are recorded in the lessons and `provenance.json`. Author self-check does not assert human review or formal verification.

The cyclic matrix illustration is supplied as PNG, editable SVG and an original reproduction program under `assets/`. The SVG is reproducible with Python alone; PNG rasterization additionally uses Playwright and Edge and may differ with fonts or browser versions.

The logarithmic-product proof diagram is supplied as PNG, SVG and `assets/render-prescribed-product-mechanism.py`. Run its reproduction program from this directory with Matplotlib installed; exact raster bytes also depend on the recorded font and library versions. The diagram illustrates the proof, not numerical evidence for its infinite-dimensional claims.

The power-strip illustration is supplied as PNG, SVG and `assets/render-power-strip-poisson.py`. Its exact kernels and boundary masses illustrate the proved continuity mechanism. Run its reproduction program in its containing directory with NumPy and Matplotlib installed; exact rendered bytes depend on the installed fonts and library versions.

The spectral-tail figure retains its included GFDL/MIT component terms. The faithful-state core figure is supplied as PNG, SVG and assets/render-core-construction.py; run the program in its containing directory. Both figures preserve exact mathematical coordinates and proof locators.

Builds default to a private review draft. The `--release` option requires complete review records bound to the exact current lesson sources, verified free research materials, and complete programme proof dependencies. The records are currently incomplete. Rendering, link checks and formula preservation do not establish that mathematical review.
