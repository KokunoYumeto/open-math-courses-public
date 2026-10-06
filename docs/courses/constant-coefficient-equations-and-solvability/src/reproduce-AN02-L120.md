# Reproduce the polynomial-averaging figure

The complete averaging lesson contains the entire learner, all three examples, six complete solutions and the full PA1–PA16 proof.

## Download the unchanged original files

The seven original files below are unchanged, including both complete Markdown sources and CREDITS.txt. CURRENT-SCOPE.txt records the current qualified status. LICENSE.txt identifies the original-work dedication and retained component terms.

- [polynomial-averaging-working-proof.md](../reproduce/L120/polynomial-averaging-working-proof.md) — 10314 bytes; SHA-256 `4A6075023A7C4AABE773575575EBDFEC9E06C8E74B27C9BCD37BBEFCB0A739FE`.
- [polynomial-averaging-learner.md](../reproduce/L120/polynomial-averaging-learner.md) — 15886 bytes; SHA-256 `10F9FA7A9F534EE74F089A49E3A4E6B306D9939EE881AF325F273AE28CB2D8FB`.
- [make_figures.py](../reproduce/L120/make_figures.py) — 5316 bytes; SHA-256 `D32C98136C6C6B2D5DA58116DBDC74DD512FB1CD338C69762C91BB405903F675`.
- [polynomial-averaging-annulus.png](../reproduce/L120/figures/polynomial-averaging-annulus.png) — 196470 bytes; SHA-256 `2B199B9986D6A9C2E070597DFB570B973E98967A314D1DB1C789285406E992A1`.
- [polynomial-averaging-annulus.svg](../reproduce/L120/figures/polynomial-averaging-annulus.svg) — 96720 bytes; SHA-256 `6F24F68629AAB720C21F1C564D6C790BB08521A0B38244F414CCD5DA2C8E365A`.
- [polynomial-averaging.geometry.json](../reproduce/L120/figures/polynomial-averaging.geometry.json) — 825 bytes; SHA-256 `1D0B8D15247125FDDB25F28D8E235AE050E9103CEE639E19FF8C83A6B3C82588`.
- CREDITS.txt — 638 bytes; SHA-256 `8370EBF024CCE76A28AA9C58544F681B84B3D2EC1DC734048223D7AAA7A430F7`.
- [LICENSE.txt](../reproduce/L120/LICENSE.txt) — 393 bytes; SHA-256 `D7603F058784D1874463FEA43C8DEEB48863E630214DA069CF5563E562B45CF0`.
- CURRENT-SCOPE.txt — 928 bytes; SHA-256 `516054B983CDFEF4797F770DF6DE6C7935704E7A0B8F2437000902683C0A65EE`.

## Run the portable renderer

Keep `make_figures.py` at the root of a fresh scratch directory. Keep the figure and geometry downloads in `figures/`; both Markdown sources and text notices remain at the root and are downloads, not renderer outputs. Run:

```text
python -X utf8 make_figures.py
```

The program creates figures/ and writes the PNG, SVG and geometry JSON. A fresh run with Python 3.13.9, NumPy 2.4.4 and Matplotlib 3.10.9 using its bundled DejaVu Sans font matched all three supplied outputs byte for byte and the full decoded PNG RGBA pixels. No SVG date or identifier normalization was performed. This byte identity is qualified by that observed environment; other software/font versions can change rendered bytes. The exact geometry JSON specifies the objects independently.

## Exact diagram, proof locators and credits

The left panel shows the annulus 1/3 ≤ |z| ≤ 5/12, roots ±1/4, phase circle |z|=3/8 and unit-radius boundary for q(z)=z²−1/16. Shading is an available support region; the actual smooth density has compact support strictly inside the open annulus. The right panel is its exact phase-circle image, centred at −1/16 with radius 9/64, traversed twice, and separated from zero by 5/64. The annular lower bound is 7/144 and the normalized coefficient bound is 7/(9√1025). The full native caption, learner section 5/exercise 4 and PA036-3–4 locate every bound; samples do not prove nonvanishing. Original diagram and reproducible geometry/renderer are GPT-6.1 Sol (OpenAI), Ultra work, October 2026, CC0.

Historical mathematical credit remains Lars Hörmander, Bernard Malgrange and Leon Ehrenpreis; the primary archive and precise comparison limits are retained in the full proof/learner and CREDITS.txt. Original proof pages and exact original lemma numbers have not been compared. The independently written argument requires no unavailable source proof. All declared scalar prerequisites, the n=0 exception and broader incomplete scopes remain explicit.
