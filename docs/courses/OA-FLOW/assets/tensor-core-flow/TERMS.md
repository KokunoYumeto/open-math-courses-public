# Tensor-flow figure: terms and reproduction

The original Python renderer, mathematical data and diagram in this directory are dedicated to CC0 1.0 Universal. Source publications and third-party fonts retain their own terms. No personal attribution is required for the original material.

## Mathematical content

The diagram illustrates two circles of length \(1\), represented by the square \([0,1]^2\) with its opposite edges identified. It uses the coordinate convention \((\theta_s f)(q)=f(q+s)\) and the exact quotient
\[
Q(q_1,q_2)=q_1+q_2\pmod1.
\]
The orange displacement \((1/4,-1/4)\) takes \(A=(1/4,1/2)\) to \(B=(1/2,1/4)\) and fixes the quotient coordinate \(3/4\). The blue displacement \((1/4,0)\) takes \(A\) to \(C=(1/2,1/2)\), moving the quotient coordinate from \(3/4\) to \(0\). On the drawn circle \(r\) is represented by \((\sin(2\pi r),\cos(2\pi r))\), so positive coordinate time is clockwise.

The dashed segments are exact pieces of constant-\(Q\) fibers before the edge identifications. The highlighted fiber \(Q=3/4\) includes both segments \(q_1+q_2=3/4\) and \(q_1+q_2=7/4\). The figure displays selected orbit segments, rather than all orbits.

The residual action has parameter \(s\). The same-time diagonal acts with parameter \(2s\), and the half-time diagonal restores parameter \(s\). For these unit circles the residual period group is \(\mathbb Z\), whereas the same-time diagonal has period group \(\tfrac12\mathbb Z\).

The complete normal-algebra proof is [Tensor products and the normalized flow of weights, TF31–TF34](../../OA-FLOW-TF.html#tf-models), particularly the equal-circle specialization of TF32–TF33 and the normalization in TF34. The human-source antecedent is M. Takesaki, *Theory of Operator Algebras II*, Exercise XII.4.2, printed p.420. Its XII.4 standing separability convention is on printed p.403. The diagram follows the independently proved single-time residual normalization. It is independently drawn and does not reproduce the source's graphical expression.

## Files and fonts

- `render.py`: independently authored Python/Matplotlib drawing program.
- `data.json`: exact rational model, coordinates, normalization, caption and source identities.
- `tensor-flow.svg`: vector output with glyph outlines.
- `tensor-flow.png`: 2880 × 1800 raster output.
- `FONT_LICENSE_DEJAVU.txt` and `FONT_LICENSE_STIX.txt`: complete font license notices copied byte-for-byte from the installed Matplotlib distribution.

The renderer uses DejaVu Sans, its bold and oblique forms, and STIXGeneral Italic for the mathematical fallback glyphs. SVG text is converted to paths. No font binaries are included. The original-material CC0 dedication does not replace the font notices.

## Reproduction

Run in a Python environment with Matplotlib and NumPy:

```text
python render.py
```

The program reads `data.json` beside itself, checks the coordinates and quotient values with exact rational arithmetic, and writes the two outputs beside itself.

The verified runtime is Python 3.13.9, Matplotlib 3.10.9, NumPy 2.4.4 and FreeType 2.6.1. SVG identifiers use a fixed hash salt, creation timestamps are omitted, and all samples and styles are deterministic. Byte-identical SVG and PNG reproduction was checked in separate Python processes on this runtime; another rendering-library version may produce different bytes while retaining the same exact mathematics.
