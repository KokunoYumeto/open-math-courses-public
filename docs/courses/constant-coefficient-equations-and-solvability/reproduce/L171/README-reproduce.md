# Reproducing the illustrations and supplementary checks

The formal and learner chapters contain the mathematical proofs. The numerical checks supplement the worked examples and do not prove the general duality or solvability theorems.

Run these commands from this directory with Python, Matplotlib, NumPy, SciPy and mpmath installed:

    python -B -X utf8 make_figures228.py
    python -B -X utf8 check_numerics228.py

The first command writes two PNG/SVG figure pairs and their exact formula descriptions in the figures directory. Its private temporary Matplotlib configuration is removed automatically when the command finishes. The first illustration distinguishes actual finite harmonic inverse norms from a proved upper bound on the image error. The second samples the normalized smooth bump and its compact negative primitive; its exact support, mass, sign and plateau identities are proved in the learner chapter.

The second command checks harmonic bounds, geometric tails, bilinear shifts, smooth translated forcing, antiderivatives, slow-decrease windows, resonant difference equations, the Fourier weight integral and exact rational support margins at 65 decimal digits where appropriate. It writes a supplementary report. That report is a local check log rather than part of the mathematical reading edition.

The original chapters, programs and mathematical illustrations are public domain under CC0. The DejaVu font retains its separate font licence. SVG text remains editable.
