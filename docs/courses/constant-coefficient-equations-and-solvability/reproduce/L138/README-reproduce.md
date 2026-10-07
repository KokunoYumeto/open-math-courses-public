# Reproduce the Carleman-necessity diagrams

The complete original proof is carleman-necessity-formal.md. The learner explanation, worked examples and complete exercise solutions are in carleman-necessity-learner.md.

Run with Python, NumPy and Matplotlib:

    python make_figures132.py

The script writes two PNG/SVG pairs and figures/geometry.json. It uses the Agg backend and built-in math text; no TeX engine or network resource is used.

Figure 1 evaluates the exact frequency budget for thresholds j and j squared, their normalized algebraic envelopes, and exact finite reciprocal sums. All active thresholds occur in the plotted frequency interval. These envelopes are bounds, not asserted Fourier transforms of compact bumps.

Figure 2 shows the local multiplicity-two logarithmic trace, its exact interval error and proved linear upper bound, and the actual compact bump exp(-2/(1-x squared)) on |x|<1. The proof establishes every derivative bound for that bump; finite plotted samples are illustrations.

The geometry file records formulas, rational heights, exact finite sums, support, constants and proof locators. SVG output keeps text editable. Original exposition, examples, solutions, diagrams and code use CC0 1.0; the DejaVu font notice retains its own terms.

Classical source: Lars Hörmander, The Analysis of Linear Partial Differential Operators II, Theorem 16.1.10, printed page314; first edition1983, second revised printing1990, reprint2005.
