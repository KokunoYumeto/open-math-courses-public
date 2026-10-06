# Reproduce the rational-period diagrams

The complete lesson contains the full learner and full PR1–PR31 formal proof, including all twelve sections, three examples and six complete solutions in each original. It preserves ordinary/integral/field conventions, dimensional endpoints and the conditional general receiver.

## Download the unchanged original files

The eleven original files below are byte-identical to the owner-admitted PR036 inputs. LICENSE.txt identifies the original-work dedication and retained component terms. The proof and learner downloads are full Markdown documents.

- [geometry.json](../reproduce/L121/figures/geometry.json) — 2481 bytes; SHA-256 `0DE6E8D9A59DAE9470B5DD648E6217907FBEC6CA3E39BCDF8AABBA5A495E21FE`.
- [normal-tube-phase-map.png](../reproduce/L121/figures/normal-tube-phase-map.png) — 79655 bytes; SHA-256 `D1A96575118FAEBAA542ED1CBE7D26AD143A5F123B3E57868F0D7B1B3641B72D`.
- [normal-tube-phase-map.svg](../reproduce/L121/figures/normal-tube-phase-map.svg) — 55365 bytes; SHA-256 `278EB3E172E1419FFEA4000D3C9ECB806BCDC27B8031E7ADFA477494C7F373AD`.
- [period-basis-and-tube.png](../reproduce/L121/figures/period-basis-and-tube.png) — 87673 bytes; SHA-256 `A9A57AD43E236F837CC3FE6F68155E826D7EBF261449C5B27D4A48101B411B1F`.
- [period-basis-and-tube.svg](../reproduce/L121/figures/period-basis-and-tube.svg) — 67642 bytes; SHA-256 `4C2111D54A34FC4F2CACA3BDE96E91860B9D56F9615348999A09789BC8B1C542`.
- [punctured-plane-cover.png](../reproduce/L121/figures/punctured-plane-cover.png) — 104910 bytes; SHA-256 `F61781F8E37EAAE7BCC8568E3922F2E522836EBE52B409DA60611590C9316524`.
- [punctured-plane-cover.svg](../reproduce/L121/figures/punctured-plane-cover.svg) — 70997 bytes; SHA-256 `CCF13AC430ECA29D7DD273E3C6E36334ADC0ACACC844176DF308E45BEEB7A450`.
- [make_figures.py](../reproduce/L121/make_figures.py) — 8984 bytes; SHA-256 `36E8159FFCDB54ED6B021345E73069E0CFA3FC546889AFA15D2C559E3ECC4771`.
- projective-rational-periods-learner.md — 43141 bytes; SHA-256 `D70634480BC947E33D5DD7F9E1B63C9AD68F9BAF760CDDE078BA27FD493EB7CF`.
- [projective-rational-periods-working-proof.md](../reproduce/L121/projective-rational-periods-working-proof.md) — 38481 bytes; SHA-256 `6D5AF96EE82B097A8BDF1A1A167BAE39C1C9A023096BAC4CE0778794254E4B06`.
- [README-reproduce.md](../reproduce/L121/README-reproduce.md) — 1298 bytes; SHA-256 `7ADA00D0AB96319F3D895868E626EAB182CFD8225C65B7BADDC0E52D226A7B52`.
- [LICENSE.txt](../reproduce/L121/LICENSE.txt) — 390 bytes; SHA-256 `747209EC407251B30C50DA5809DBF1C3CB25E50774FFEAEA98D575D4F3FC8FFA`.
- CURRENT-SCOPE.txt — 1083 bytes; SHA-256 `52199F3D8AF3B2078D54CD6DC03209AB8914D28709D214C86B580F843216937B`.

## Run the portable renderer

Keep make_figures.py at the root of a fresh scratch directory and run:

```text
python -X utf8 make_figures.py
```

The unchanged program creates figures/ and writes three PNG diagrams, three SVG files and geometry.json. Alternatively use --output-dir replay. A current fresh run with Python 3.13.9, NumPy 2.4.4 and Matplotlib 3.10.9, using its bundled DejaVu Sans font, matched all seven supplied files byte for byte and every decoded PNG RGBA pixel. No SVG date or identifier normalization was performed. Byte identity is qualified by that observed software/font environment; other versions may change rendering bytes. The geometry JSON records the mathematical objects independently.

## Exact figures, proof locators and credits

Figure 1 is a window of the exact slit-plane cover for S={-1,1}, delta=0.65 and circle radius 0.45. It includes the actual integral intersection map of PR12, with left/right components and the positive-circle kernel vectors; PR2–PR3 and PR11–PR15 prove the chain statements. Figure 2 is the d=2 unwrapped phase map modulo 2pi, with actual columns (-1,-1) and (1,0), determinant +1, and normal circle first; PR21–PR24 specify every coordinate. Figure 3 is the complete normalized diagonal period matrix and separate primitive tube vector for Example 2; PR6, PR17, PR25–PR26 establish its entries. Full original captions remain in the learner and assembled reader. Each native PNG has an explicit full-size route.

The diagrams, geometry and renderer are original GPT-6.1 Sol (OpenAI), Ultra work, October 2026, CC0. Historical mathematical credits are Atiyah, Bott, Gårding, Grothendieck and Hatcher, with free primary source links and precise comparison limits retained in the full learner. The admitted smooth comparison is CD034. The general algebraic/Stein/duality route remains an explicit prerequisite, not a claimed new proof. Existing MathJax, Matplotlib and font/software terms remain included and unchanged. No book scans or source media are distributed.
