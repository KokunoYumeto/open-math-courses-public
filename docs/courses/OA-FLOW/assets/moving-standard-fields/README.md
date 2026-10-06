# Moving standard forms: the exact two-summand swap

Run render_moving_fields.py with Python, numpy and matplotlib to reproduce
the SVG, PNG and exact-data.json. The source uses exact fractions for the
probability, density, conditional-mass and normalization identities. It also
checks the weighted unitary, involution, conjugation, covariance and cone
formulas on explicit complex matrices, with the stated numerical tolerance.

The figure depicts OA-FLOW L41, oa-flow.cstd.example, equations (E1)–(E13).
The columns are target fibres. In the left column the source is fibre 1; in
the right column the source is fibre 0. Both fibre maps are identities between
labelled Hilbert–Schmidt copies. The orange factor belongs to the global
weighted Hilbert-space operator. The green division normalizes the resulting
conditional state vector. The lower bars have a common probability scale
and represent central masses, not Hilbert-space dimensions.

The exact data are p=1/3, q=2/3,
rho_0=diag(2/3,1/3), and rho_1=diag(1/4,3/4).
The proof, including all null-set and conditional-vector qualifications,
remains in the lesson.

Original diagram, code and data: CC0-1.0 to the extent of rights held.
DejaVu Sans and DejaVu math lettering retain the terms in
FONT_LICENSE_DEJAVU.txt. The SVG uses glyph paths; this does not replace
the font's terms with CC0.
