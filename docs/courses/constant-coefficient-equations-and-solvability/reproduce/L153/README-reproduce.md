# Reproduce the smooth-test topology lesson

The original proof source proves all four physical-space neighborhood criteria, the infinite Fourier-envelope criterion and all three conditions of the strictly PSH weighted-integral criterion. It includes smooth locally finite derivative majorants, the complete logarithmic-contour homotopy and Jacobian, exterior separation, successive power/coefficient choices, finite whole-strip stabilization and the exact curvature exponent.

The learner source gives four worked examples and ten complete solutions. Run Python with NumPy, mpmath and Matplotlib:

    python -B check_examples172.py
    python -B make_figures172.py

The checks integrate actual compact-bump transforms on the real and logarithmically shifted contours, compare shifted-plane Plancherel integrals, differentiate both sides of the multidimensional homotopy identity, evaluate actual complex determinants and independently differentiate the radial/full seed Hessians. The explicit weighted norm is evaluated through its positive physical-space integral, with its imaginary tail bounded separately. These calculations supplement the full proofs.

Two original PNG/SVG pairs and exact geometry JSON retain the escaping bump supports, weighted response, complex differential, actual contour heights, strict curvature normalization and distributional support corner. These objects are fully shown by scientific plots; a Blender scene would add no useful mathematical geometry. The scripts require no TeX. SVG dates are omitted and a fixed hash salt is used; DejaVu fonts retain their own license.

Human source: Lars Hörmander, The Analysis of Linear Partial Differential Operators II, §15.4, Theorems 15.4.1–15.4.3, printed pp. 296–300. The exact curvature power is -3/4 of 1+|Im z|². The historical summary's weaker -3/2 power is corrected in the current mapping. Approved local source text/pixels remain private and are excluded from the lesson payload.

The chapter's separate embedded representation exercises, notes and every other assigned course target remain in the full goal.
