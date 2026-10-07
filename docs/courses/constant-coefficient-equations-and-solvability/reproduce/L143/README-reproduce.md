# Reproduce the local compactness diagrams

The complete original argument is [psh-local-compactness-formal.md](psh-local-compactness-formal.md). The learner explanation and complete exercise solutions are in [psh-local-compactness-learner.md](psh-local-compactness-learner.md).

Run with Python, NumPy and Matplotlib:

    python make_figures142.py

The script uses the Agg backend and built-in math text. It writes two PNG/SVG pairs and [figure-geometry.json](figure-geometry.json), with exact rational coordinates, domains, function formulas and proof locators. No TeX engine or network resource is used.

[Figure 1 SVG](figures/mean-propagation-and-components.svg) and [PNG](figures/mean-propagation-and-components.png) show the mean-ball inclusions, a finite compact cover inside a connected domain, and the actual disconnected counterexample. The middle drawing illustrates finite covering; it is not a claim that overlapping balls alone supply one numerical bound on the whole domain.

[Figure 2 SVG](figures/truncated-logs-and-hartogs.svg) and [PNG](figures/truncated-logs-and-hartogs.png) plot the truncated logarithms, the exact integral error and the compact suprema for two different compact sets. Profiles use positive radii; minus-infinite and finite point values at zero are stated separately. The error graph evaluates the proved closed formula.

Original proofs, exposition, examples, solutions, diagrams and code use CC0 1.0. The SVGs preserve editable text. The DejaVu font retains the terms in [DejaVu-font-license.txt](DejaVu-font-license.txt).

Classical source credit: Lars Hörmander, *The Analysis of Linear Partial Differential Operators I: Distribution Theory and Fourier Analysis*, Theorem 4.1.9; first edition 1983, second edition 1990, reprint 2003.
