# Original formula-based figures

These five original figures and their reproducible code and data are dedicated to CC0-1.0 to the extent of the author's rights. The diagrams display the maps, periods, kernels and exact finite data from the two accompanying lessons.

Run `python build_figures.py`, then `python validate_models.py` in this directory. The first command creates PNG and SVG versions, exact parameter descriptions, floating samples, and SHA-256 hashes. The second checks integer carry identities exactly with rational numbers, finite-support Floquet translation signs numerically, the Fourier normalization, local references and equation delimiters. The written proofs supply the infinite-dimensional assertions.

| Figure | Exact proof locator | Scope of the picture |
|---|---|---|
| `characteristic-square` | `../../src/OA-FLOW-NSQ.md`, CS1–CS5 | Nine groups, all twelve internal arrows, all six surjective kernels; nonfactor top-left group retained. |
| `cocycle-topology` | `../../src/OA-FLOW-NSQ.md`, CS14–CS16 | Abstract Polish-group example. R = 1. The compact-time supremum of the tail occurs at t = 1 because each sine term is increasing on this interval. The tail beyond K = 10000 has squared norm at most 1/K; the dashed global bound is 1/sqrt(N). Floating sums illustrate these proved estimates. |
| `dominance-boundary` | `../../src/OA-FLOW-NSQ.md`, CS24–CS26 | Five labels represent an excerpt from all real atomic eigenvalue labels. The diffuse density is amplified to the same Hilbert dimension in the proof. The jump is exactly sqrt(2) at every nonzero frequency and zero at zero. |
| `periodic-monodromy` | `../../src/OA-FLOW-PSQ.md`, PS5–PS7, PS20–PS23 | Distinct center and modular circles, with P = 2, T = pi, lambda = exp(-2), and PT = 2pi. Arrows show negative phase motion. |
| `periodic-obstruction` | `../../src/OA-FLOW-PSQ.md`, PS30–PS36 | Exact integer carry and relative splitting requirement. The lower torsion panel is conditional on the stated modulus element, not an asserted factor realization. |

Human source context: Masamichi Takesaki, *Theory of Operator Algebras II*, XII.6.12–6.15, printed pp.449–453, and Exercise XII.6.1–2, printed pp.455–456. These are ordinary mathematical citations; the figures are independently designed from the displayed proof formulas. The nonseparable dominance boundary tests extrapolation beyond the standing separability assumption on p.403 and is not labeled a source error.

The PNG files provide ready-to-view figures; their SVG counterparts are editable vector sources. `HASHES.json` supports regeneration comparison.

Install both lesson readers before running the validator. Its document and anchor checks use the NSQ and PSQ source and reader routes. `VALIDATION.json` records the finite-model checks; the written proofs establish the general results.
