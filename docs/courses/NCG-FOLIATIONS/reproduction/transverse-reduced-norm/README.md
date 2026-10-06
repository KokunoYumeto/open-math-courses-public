# Reproducing the transverse norm diagram

Run python draw_norm.py --output-dir OUTPUT with the bundled fonts folder and FONT-NOTICE.txt next to the script. It writes transverse-reduced-norm.png, transverse-reduced-norm.svg and data.json.

The recorded renderer is Python 3.13.9, Matplotlib 3.10.9, NumPy 2.4.4 and Pillow 12.2.0. Using those versions and the bundled font and generator bytes permits comparison against the included PNG, SVG and data.json outputs. Other compatible versions may change layout or file bytes without changing the exact mathematical data.

The metric-bundle panel is a coordinate schematic. The norm bars are exact proved values, the forty integer samples are the exact Rayleigh formula (RN.12), and the last panel records the two exact equivariant index pairs (RN.13). The mathematical proof, rather than the finite plot, establishes the limit and norm.

See COMPONENT-TERMS.md, FONT-NOTICE.txt and the four complete software notices. The reproduction bundle includes the generator, bundled fonts, figure outputs and exact data needed to recreate the diagram.
