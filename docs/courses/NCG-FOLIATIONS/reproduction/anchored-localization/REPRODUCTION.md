# Reproduce anchored proper-source localization

Section 11AA of *K-theory of the leaf space* supplies the original-anchor technical/product foundations, supported averaging, finite-action slices and induction reciprocity, explicit open Mayer–Vietoris extension, anchored source telescope with its Milnor term, and the actual proper-source Dirac lift. Exercises 169–176 have complete solutions for 96 points.

Use Python with Pillow 12.3.0 and the unchanged supplied DejaVu font and FONT-NOTICE.txt. Run `python -B render_localization.py --output OUTPUT` from this directory. It regenerates anchored-localization.png, anchored-localization.svg and figure-data.json. Compare those bytes with the included figure and exact data. The complete Pillow and Python notices accompany requirements.txt.

The figure shows the exact scalar Mayer–Vietoris homotopy at the explicitly labelled sample parameter 1/4; the clopen coefficient-coset diagonal in the induction triangle; the norm error of a continuous telescope in c0(N) with entries 2^(-k); and the whole-base lift through the actual quotient with original coefficients. These finite rational samples supplement the complete proofs. They do not establish the infinite KK identities. Proof locators: MV.1–MV.7, SR.4–SR.9, AT.1–AT.4 and PL.1–PL.7.
