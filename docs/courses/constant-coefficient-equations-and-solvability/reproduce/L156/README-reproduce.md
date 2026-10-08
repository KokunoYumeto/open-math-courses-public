# Reproduce the complex-weight notes

Use Python with NumPy, Matplotlib and mpmath:

    python -B -X utf8 check_examples181.py
    python -B -X utf8 make_figures181.py

The check program independently differentiates the defining real weight functions, integrates actual circle means, differentiates scalar and multivariate holomorphic pullbacks, and checks real radial integrability and the exact carrier enlargement. These are supplements to the full original proofs and do not prove topology equivalence or import a broader-domain or systems theorem.

The figure program writes two PNG/SVG pairs and their exact geometry. SVG dates are omitted and the identifier salt is fixed. The naive curvature is sampled strictly away from the nonsmooth axis. The strict coefficient is displayed with its stated positive scaling. The coordinate plot displays actual radial map and Levi values, with its critical point and compact-chart lower bound explicitly identified.

Original sources, examples, solutions, scripts and geometry use CC0 1.0. The retained DejaVu font license keeps its own terms. The human source is Lars Hörmander, The Analysis of Linear Partial Differential Operators II, Notes on printed pages300–301. No protected source text or page image is part of this packet.

No TeX compilation, network access or book file is needed to reproduce these original calculations and figures.
