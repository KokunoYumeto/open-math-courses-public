# Signature and cone source coefficients

This original illustration accompanies Quadratic boundary kernels and signature phases, Theorem4.1 and Example7.2. Every signature with n=p+q between3 and8 is included. The entries are the exact integers sin(pi*p/2) for the positive sign cone and -sin(pi*q/2) for the negative sign cone. Multiply by 4*pi^((n-2)/2)*abs(det(A))^(-1/2) to recover the source coefficient. The highlighted(2,2)signature has zero source for both cone layers;the chapter separately proves nonzero boundary-value fundamental solutions. These are coefficient tables,not pointwise kernel plots. Exact data are in signature-coefficients.json.

Reproduce the PNG, editable SVG and data with Matplotlib:

    python -B make_signature_figure.py

Original illustration, code, data and text by GPT-6.1 Sol (OpenAI), October2026. CC0 1.0: https://creativecommons.org/publicdomain/zero/1.0/
