# Reproduce the general reduced-graph diagrams

The mathematical expression, diagrams and generator are original CC0. Matplotlib, NumPy and installed fonts retain their own terms. No external artwork or source PDF is included.

Run `python generate.py` with NumPy and Matplotlib installed. The default destination is the course's `figures` directory. PNG and SVG outputs are deterministic with a fixed library and font installation; SVG retains editable text and does not embed font files. The generator verifies each sampled curve against its stated proved bound. Samples illustrate the proofs; they do not replace them.

- **metric-fibre-shear:** The concrete polynomial germ, its actual second-jet tangent shear, Frobenius-normalized cotangent coefficient, and MB.16 uniform bound. Proofs: MB.12–MB.17; full oriented cancellation MB.21.
- **normalized-cone-pairings:** Exact specified-class obstruction, disk-invisible corrections, attainable integral subgroup and actual commutative mapping-cylinder tests. Proofs: FCD.8–FCD.14 and OFD.1–OFD.4.
- **joint-covariant-rank-seam:** Original degree-three finite suspension, retained rank seams, exact averaged coefficient and noninvariant transport ratios. Proofs: JCN.20–JCN.29 and JCR.1–JCR.7. The omitted endpoints are shown as open circles.

Read [the lesson](../../k-theory-of-the-leaf-space.html) for the complete arguments and the limitations of each construction.
