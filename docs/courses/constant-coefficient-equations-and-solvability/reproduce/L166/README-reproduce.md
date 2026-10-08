# Reproducing the directional surface figures

Run Python with NumPy and Matplotlib:

    python -B make_figures213.py

This creates two PNG/SVG figure pairs and geometry213.json. The geometry records the exact sphere convention, integer multiples of pi, ellipse center and semiaxes, inverse-normal formula, unit normal arrows and equal physical coordinate scales. The sphere plot uses the exact identity for integer-pi centers and omits their zero value at the real center.

Run the supplementary checks with mpmath and SciPy:

    python -B check_numerics213.py

The checks compare direct sphere surface-height integration with the entire sine quotient, direct physical ellipse integration with the Bessel transform, and independently calculated normals, curvature and stationary-phase coefficients. They also verify the profile identity and recession constant. The formal lesson proves the general statements; finite probes serve only as supplementary checks.

The original lesson, proofs, examples, solutions, geometry and figure scripts are dedicated to the public domain under CC0 1.0. DejaVu Sans is used under its separately retained font license. The scripts use the installed mathematical libraries without incorporating their code into the lesson.
