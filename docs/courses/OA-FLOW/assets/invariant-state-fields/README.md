# Invariant-state field diagrams

The two diagrams illustrate the exact examples proved in [L40](../../src/OA-FLOW-L40.md#oa-flow.istate.examples).

The column diagram depicts formulas (E1)–(E7). Each vertical arrow acts inside one of two fixed fibres. The masses are exactly 1/2 and 1/2. The orange factors are complex phases, while the measure derivative is exactly one. Both fibre unitaries fix their indicated cyclic vectors.

The boundary diagram depicts (E13)–(E15). The compact spectrum is [0,1], the ideal consists of continuous functions vanishing at zero, and its exact full-norm restriction locus is (0,1]. Lebesgue measure gives the omitted endpoint zero mass. The stated group action is trivial.

## Reproduction

Run Python on render_column_phases.py with matplotlib and numpy installed. The script reads exact-data.json, verifies the integer phase identities and rational masses, checks sample complex matrices, and writes both SVG and PNG pairs. Figure coordinates are diagram coordinates, not numerical samples of the mathematical base. The interval endpoints and open/closed markers have their exact usual set-theoretic meanings.

The checked runtime used Python with matplotlib 3.10.9 and numpy 2.4.4. The SVG files contain font outlines and do not need a network font service. The associated PNGs are convenient inspection copies.

## Component terms

The original mathematical exposition, diagram geometry, labels, exact data and reproduction code are dedicated to the public domain under CC0 1.0 Universal.

The figures use DejaVu Sans supplied with matplotlib. Its separate font terms are retained verbatim in FONT_LICENSE_DEJAVU.txt and continue to apply to that font component. No third-party figure or photograph is used.

Self-checked by the writing AI.
