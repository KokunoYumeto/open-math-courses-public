# Reproduce Rational compact cohomology and the normal-circle connecting map

Read the complete lesson. The proof, three worked examples and six solutions below use the stated coefficient, orientation, right-cap, excision and finite-chain Thom hypotheses. It constructs the actual rational-to-real compact coefficient map and the normalized rational connecting map, proves its square with the specific real CO17 transport and descends exactness faithfully.  The canonical comparison is proved separately in L129; it is not supplied by this argument.

## Exact original files and terms

The downloads provide the proof, figures, exact coordinates and reproducible renderer. The original text and diagrams are dedicated under CC0. MathJax and the supplied fonts retain their component licence notices. Human references and proof locators accompany the mathematical text.

Read the complete supplied proof in its current reader presentation. This complete supplied source contains both its formal argument and all learner examples and solutions. The original downloads below remain exact.

- [README.md](../reproduce/L128/README.md) — 1700 bytes; SHA256 `40109AC7E5A9853CDB8FC6D6058CF9E57C6DC7A57DED60F35D068D41B8FDF9B8`.
- [LICENSE.txt](../reproduce/L128/LICENSE.txt) — 480 bytes; SHA256 `7D2670EA1B721A811F785E54F1EBAC2F7D2791429BB0639DC8A449960DF52903`.
- rational-compact-coefficient-bridge.md — 30907 bytes; SHA256 `B59AC202380DB1395B0EBAAB77EB1325B72E29B6E546755CE0F61338277F3006`.
- [make_figures.py](../reproduce/L128/make_figures.py) — 5886 bytes; SHA256 `E71DDB32B85132D69166BCBAF84B783EE7D6F884F98BFFE6E2D398FD0ECF40A9`.
- [figures/geometry.json](../reproduce/L128/figures/geometry.json) — 1311 bytes; SHA256 `55A405CC987F4DC737F55095983836BD2956B914F5DA99D89898900B54B32EA2`.
- [figures/coefficient-and-right-cap-square.png](../reproduce/L128/figures/coefficient-and-right-cap-square.png) — 148613 bytes; SHA256 `457B32E4CC0D340E4DBF019C8497E66E3310EEFD4CE8CF7A4CFEDC10C11CDE2F`.
- [figures/coefficient-and-right-cap-square.svg](../reproduce/L128/figures/coefficient-and-right-cap-square.svg) — 58474 bytes; SHA256 `D2B9E45FDE3D67F1E8DFDCEF7043642CF14F18AE51E5481768C6E85914733734`.
- [figures/rational-normal-circle-and-descent.png](../reproduce/L128/figures/rational-normal-circle-and-descent.png) — 184769 bytes; SHA256 `5B1E92DC42B252AE5DD2B73DCC1BFCBF968ED61ED2B0AA9D48AEB25C73E126CC`.
- [figures/rational-normal-circle-and-descent.svg](../reproduce/L128/figures/rational-normal-circle-and-descent.svg) — 86914 bytes; SHA256 `55F074A41FC2F09349D06C20B388262E24592737D70A0BF7B9AFF2F948F09CF3`.

## Fresh native reproduction

Keep make_figures.py in a fresh directory and run:

```text
python -B -X utf8 make_figures.py --output fresh-figures
```

The renderer writes native PNG, SVG and exact geometry records. Check the complete original captions, coordinates, conventions and proof locators. The schematic and sampled figures explain the written proof. Different software or font versions may change rendering bytes.

The statements use the specified orientation, Thom and comparison hypotheses. Integral descent, rational-form spanning, the particular affine C8 representative, coefficient conventions and component constancy require their additional arguments. Exposition: GPT-6.1 Sol (OpenAI), Ultra, October 2026; CC0-1.0. [L124](../AN02-L124.html) gives the projective-exhaustion context; [L125](../AN02-L125.html) proves the geometric finite-chain H statement.
