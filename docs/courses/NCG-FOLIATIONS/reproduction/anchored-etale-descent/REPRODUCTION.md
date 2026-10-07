# Reproduce the anchored étale descent diagram and finite identities

Install the exact package versions in `requirements.txt`. Keep the unchanged
regular and bold fonts in `fonts` and their complete `FONT-NOTICE.txt` beside
the two standalone scripts. From this directory run:

    python finite_checks.py
    python draw_descent.py --output-dir figures

The first command writes `finite-checks.json`; it needs only NumPy and the
script's finite mathematical model. It reads no lesson proof, provider,
coordination record, or private validation input. The second command writes
the PNG, SVG and exact figure-data JSON under `figures`, using only its
embedded drawing data and the supplied fonts/notice. Its runtime cache stays
inside this reproduction directory. SVG dates are omitted and its hash salt
is fixed, so the three figure outputs have deterministic bytes with the
pinned runtime and fonts.

The finite model is the eight-arrow action groupoid of C2 × C2 on two units.
The first factor exchanges units; the second is nontrivial isotropy. Moving
graded frames have dimensions two and three, with actual continuous arrow
unitaries and the correct cocycle. Seed `6100623` fixes 24 trials for each
of 15 matrix/module/tensor/sign checks. The 19 passing checks include actual
composition, core inner-product positivity, full typed tensor balancing and
inner products, reduced source-column intertwining, a degenerate coefficient
representation, rank-one compact extension, connection-kernel equality,
Clifford multiplication/adjoint signs and the positive product anticommutator.
A further 24-trial check uses noncommutative M2(C) coefficients with actual
conjugation transport in the module and tensor formulas.

These finite calculations supplement the complete DS.1–DS.23 proofs. They
do not establish infinite KK claims, product existence, reduced exactness,
or a coefficient-free quotient inverse from samples.

The diagram is a typed schematic. Its drawing coordinates are page-layout
coordinates and assert no groupoid metric or geometric model. The top left
retains `g:x→z`, `h:y→z`, and `h^-1g:x→y`. The top right displays the
source-x regular matrix coefficient acting from `E_x` to `E_x`. The lower
left gives the rank-one compact tensor extension and the resulting positive
Calkin compression. The lower right gives the exact quotient module
identification and its commuting KK square. Complete proof locators and all
domain/codomain data are also in `anchored-etale-descent-data.json`.

Human-source orientation: Alistair Miller,
[*Functors between Kasparov categories from étale groupoid correspondences*](https://arxiv.org/html/2303.02089v2),
Section 2.4. The groupoid descent proof is supplied in the lesson; the
independently supplied KG.1–KG.4 foundation proves the original anchored
equivariant product existence. Neither is replaced by the group-only
descent theorem.
