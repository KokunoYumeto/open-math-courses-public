# Reproduce the convergence diagrams

The lesson proves strong local norm convergence and two upper-limit statements for distributionally convergent subharmonic functions. The complete proof is in subharmonic-convergence-formal.md; the learner exposition, exercises and solutions are in subharmonic-convergence-learner.md.

Run with Python, NumPy and Matplotlib:

    python make_figures118.py

The script writes two PNG/SVG pairs and figures/geometry.json. No TeX engine or network resource is used. The first figure shows the continuous cap of the three-dimensional Newtonian kernel, its exact radial error density and three norm-error rates. The second shows the finite grid blocks of moving logarithmic wells, rational nearest-point coordinates and two incompatible subsequences at one observation point. Finite plotted samples illustrate the full arguments in SC4 and SC9.

Kernel convention: Delta E_n=delta_0, E3(r)=-1/(4*pi*r) and E2(r)=log(r)/(2*pi). At level m, N_m=ceil(exp(m)); every one of the (N_m+1)^2 centers is included in the sequence, with coefficient 1/m.

Original exposition, examples, solutions, diagram code and diagram content: CC0-1.0. Written by GPT-6.1 Sol (OpenAI), Ultra reasoning effort, October 2026. Classical source: Hörmander, The Analysis of Linear Partial Differential Operators II, Proposition 16.1.2, printed pages 304–305, first edition 1983, second printing 1990, reprint 2005. See LICENSE.txt and DejaVu-font-license.txt.
