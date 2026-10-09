# Reproducing the causal support illustrations and checks

The chapters contain the full proofs and complete exercise solutions. With Python, Matplotlib, NumPy and mpmath available, run:

    python -B -X utf8 make_figures246.py
    python -B -X utf8 check_numerics246.py

The first program writes two PNG/SVG pairs and an exact coordinate-and-formula description. Its temporary Matplotlib configuration is removed at completion. The cone diagram uses the actual shifted coordinates, contribution starts, positive clock and compact cutoff of the differential-and-delay example. The curve diagram shows the continuous feedback powers and the exact regular inverse density; its delta term is specified separately.

The checker uses exact fractions for recursively constructed delay coefficients, the clock inequality and the curved support example. At 65 decimal digits it independently integrates the causal Green convolutions, tests the full distributional differential-and-delay equation against compact time bumps with complex spatial oscillations, and checks the continuous-feedback identity by a separate convolution integral. It also verifies the finite-regularity error signs, local norm bounds and factorial tail estimates. Its local report is supplementary evidence and does not replace any proof.

Original exposition, solutions, programs and figures are public domain under CC0. The DejaVu font retains the licence provided alongside these sources.
