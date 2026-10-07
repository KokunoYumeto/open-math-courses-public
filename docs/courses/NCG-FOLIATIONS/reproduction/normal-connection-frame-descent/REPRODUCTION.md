# Normal connections and compact-frame descent

*K-theory of the leaf space*, Section 11AG, proves the local affine connection, its global patching through flat zero-weight strata, and its compact-frame descent to the original units. The pointwise averaged weight can have noncompact inverse; the figure does not assert a completed physical graph operator.

Use Python 3.13.9, Matplotlib 3.10.9, NumPy 2.4.4 and Pillow 12.2.0. The unchanged fonts, full font terms, complete software notices and full CC0 dedication are in the adjacent labelled-geometric-kernel folder. No private inputs are read.

Run `python -B reproduce.py --output-dir out`. Compare the PNG and SVG with the copies in `../../figures/`, and the two JSON files with those in this folder. The optional `--resources` selects another copy of the shared font resources. Set MPLCONFIGDIR to a temporary cache directory if desired. The pinned public inputs reproduce all four outputs byte for byte.

The affine chart example has transition 3, weights 2/3 and 1/3, origins -2 and 1, and zero identity displacement. Panel C samples the proved conditional inequalities with L=J=H=1 and K0=100; the exact endpoint is 23/400. It does not choose a foliation metric realizing those illustrative constants. Panel E uses the exact Fourier orthonormal family and fixed auxiliary eigenvalue 2 to explain the infinite compactness obstruction. The six finite-check families cover rational origin corrections, scalar resolvent inequalities, conditional bounds, a pinned two-point toy frame marginal, positive averaging, and the Fourier Gram identities; the infinite proofs are in the lesson.
