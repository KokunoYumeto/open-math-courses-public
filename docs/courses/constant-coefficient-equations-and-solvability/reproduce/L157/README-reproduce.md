# Reproduce the joint logarithmic-frequency examples

The original proofs, learner explanations, complete solutions and figure programs use CC0 1.0. The accompanying DejaVu font license retains its own terms.

Run the two Python programs with Python 3 and NumPy, Matplotlib and mpmath:

    python -B make_figures185.py
    python -B check_examples185.py

The first program writes the two PNG/SVG pairs and their exact geometric specifications. The second directly evaluates entire Fourier pairs, phase cancellation, derivative errors and recession limits, and the real frequency-coordinate inequalities at 75 decimal digits. These numerical checks supplement the written proofs; they do not prove PSH compactness or ultrafilter existence.

The two-atom curve is undefined at its exact Fourier zero. The program records that value as missing on the finite plot and labels it minus infinite. The crossed-distribution diagram presents three exact frequency routes and a forbidden pair; it does not classify every possible proper component.

The complete proof provides the compactness bound, smooth invariance on the same sequence, coordinate lifting, countable extraction, the compact metric space of exponentiated profiles and the arbitrary-family ultrafilter construction. The learner text supplies four worked examples and ten complete exercise solutions. The illustrations use equal Euclidean scales where appropriate, the Fourier sign stated in the lesson, and exact symbolic support functions.
