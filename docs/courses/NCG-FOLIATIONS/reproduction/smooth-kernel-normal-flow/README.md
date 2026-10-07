# Smooth labelled kernel and normal flow

*K-theory of the leaf space*, Section 11AE, proves the smooth approximation SK.1–SK.5 and the complete irrational-rotation counterexample CK.1–CK.9. Exercises 195–196 have checked solutions (28 points). Smooth coarse control alone does not imply normal norm continuity or the naive bounded-phase compactness condition. The example does not exclude a different suitable geometric graph operator.

Use Python 3.13.9, Matplotlib 3.10.9, NumPy 2.4.4 and Pillow 12.2.0. The pinned [requirements](../labelled-geometric-kernel/requirements.txt), unchanged [fonts and complete notice](../labelled-geometric-kernel/FONT-NOTICE.txt), and complete software notices in `../labelled-geometric-kernel/software-notices/` are shared with the preceding labelled-kernel diagram. No private inputs are required.

Run `python -B finite_checks.py --out finite-checks.json`, then `python -B draw_normal_flow.py`. The drawing command writes PNG, SVG and figure-data.json in figures/. Its default resources directory is the adjacent labelled-geometric-kernel folder. Optional `--out OUTPUT` and `--resources RESOURCES` select another output or resource directory. Set MPLCONFIGDIR to a temporary cache directory if desired.

Six exact finite checks cover 99 quarter-circle distances, rational angle and margin bounds, 64 Gaussian-rational Fourier polynomials, one zero-sum Gram sample and the phase margin. The infinite conclusions are proved in the lesson. The plotted traces are numerical samples; the labelled map at x=1/4, coarse bounds, derivative coefficients, Fourier coefficient i/8, flow margin 17/64 and phase margin 1/16 are exact. The pinned inputs reproduce the supplied PNG, SVG and figure-data.json byte for byte.
