# Reproduce both countable-tree graph-column figures

Use Python 3.13 and the versions in [requirements.txt](requirements.txt), then run:

```console
python draw_proper_tree.py
python draw_countable_tree.py
python check_formulas.py
```

The two complete generators create `../../figures/kt-proper-tree-normal-inverse.png` and `.svg`, and `../../figures/kt-countable-tree-proper-weight.png` and `.svg`. Their bounds reports and [FORMULA-CHECKS.json](FORMULA-CHECKS.json) stay beside these sources. The bundled exact DejaVu/STIX typefaces are loaded locally; outlined SVGs carry the full actual font notices. No private proof, machine path or external font service is needed.

The reference environment is Python 3.13.9, Matplotlib 3.10.9, NumPy 2.4.4 and Pillow 12.2.0. Two reference runs are compared byte for byte. Other software/renderer versions can change bytes without changing the formulas. These numerical checks cover 108,257 finite typed cases and seven exact window counts. They do not prove infinite domains, compact tails, reduced descent or local Bott normalization; the complete arguments are in Section 11D.

Figure 11D.1 shows the exact radius-two F2 window with finite C2 stabilizers and a two-term coset average. Its eigenvalue curves are the exact parameter formula, rather than a computed normal spectrum. Figure 11D.2 marks finitely drawn attached leaves as a schematic of all positive labels, compares exact square-resolvent values and counts the whole infinite tree in each finite proper-weight window. The finite drawings replace no analytic proof. Read the full-size SVG/PNG for fine labels on small screens.

Original exposition, diagram expression and generator source use CC0 1.0; actual font glyphs and external software have separately scoped [component terms](COMPONENT-TERMS.md).
