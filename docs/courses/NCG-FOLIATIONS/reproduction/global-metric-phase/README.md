# Global metric phase and reduced receiving routes

This generator and the diagram are original mathematical expression dedicated under CC0 1.0 to the extent of rights held. No external artwork is incorporated.

Run `python -B draw.py` with Python, NumPy and Matplotlib. It produces `global-metric-reduced-routes.svg` and `.png` in the course figures directory. Select another output directory with `--output PATH`. SVG hash salt and metadata are fixed; outputs are reproducible byte for byte with the recorded runtime.

The left panel evaluates exactly the scalar defect from MB.13–MB.14 on a 201 by 201 radial magnitude grid: each displayed magnitude is 10**t - 1 with 0 <= t <= 4. The colour is log10 of the defect, clipped by the displayed scale. This finite plot is a sample, not the proof of the bound on all rays. MB.14 supplies that bound, while MGP.1–MGP.10 prove the operator norm, compactness and nonlinear coordinate comparison.

The right panel is a schematic of the actual maximal cycle and two sufficient reduced receiving scopes MGP.11–MGP.13 and MRP.1–MRP.13. Both preserve the whole metric and tree carriers, original q, full inverse lift and graded Clifford order; the whole graph and original positive disk are retained. It does not assert arbitrary-holonomy reduced continuity or make a sufficient receiving certificate universally necessary.

Software and fonts retain their applicable component terms, including `../FONT-NOTICE.txt` for DejaVu outlines. The CC0 dedication covers the mathematical expression and diagram, not third-party software.
