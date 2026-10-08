# Reproduce the four-condition complex weight lesson

This original AN02-L149 packet proves the full variable-scale regularization
of Hörmander II Lemma 15.2.3 and the complete seminorm-domination weight of
Theorem 15.2.1. It includes the compact-support partition topology, local
reflected dual identification and subsequent weak representation.

Read complex-psh-weight-formal.md for VS1–VS20, PW1–PW35 and PW3a. Read
complex-psh-weight-learner.md for four worked examples and ten exercises with
complete solutions. The exact source curvature is
c*(1+|Im z|^2)^(-3/4); the regularization has M^(-3/2)/18. Both powers and the
Fourier reflections are retained.

Run from this folder with Python, NumPy, SciPy, mpmath and Matplotlib:

    python -B -X utf8 check_examples160.py
    python -B -X utf8 make_figures160.py

No external TeX engine is used. The plots show exact scalar functions and real
support geometry, for which a three-dimensional Blender scene adds no clarity.
The editable parameters and formulas are in figures/geometry.json.

The first figure shows the exact k=1 radial correction and the 1/16 curvature
margin, the 1/144 loss budget and the retained 1/18 bound. Its second panel is a
three-branch finite maximum with exactly stated interval radii, t and G. The
strip |eta|<=5 is analytically stabilized; the switching positions are numerical
roots of the exact seed functions. The finite illustration does not stand in
for the full infinite exhaustion proved in the formal text.

The second figure shows K=[-1,1], C=[2,3], gap one and the positive separating
direction. Its exact exterior-box plane energy can grow even while the
coefficient exp(-2 eta) becomes small. The seminorm induction uses an enlarging
imaginary integration domain, not a claim that the entire transform decays.

The 128 independent checks evaluate defining integrals in two coordinates,
smooth-kernel derivatives and the unsmoothed logarithm's distributional corner,
high-precision physical radial/tangential Hessians, finite-stage inactivity and
interfaces, actual exterior-interval transforms and physical squared norms,
support functions and the large-parameter margin. Numerical checks supplement
the analytic proofs; they do not establish general statements by sampling.

All original prose, scripts, solutions and figures use CC0 1.0. The DejaVu font
retains its own license. Ordinary scholarly attribution appears in the formal
proof. No protected source pages, extracted book text or book media are included.
