# Reproduce the completed restriction-duality and boundary figure

The complete proof is Proposition 6.8h, equations QB.1–QB.15, in *The index theorem for measured foliations*. Exercises 31–33 have complete solutions with 32 rubric points. Figure 6.8e shows the exact completed quotient/Dirichlet anti-dual isometry, physical support enclosures on one fixed ordinary interval, and the proved local upper, global lower and ratio lower bounds. Each support row is a separate operator. Profile heights are normalized coordinate schematics, not the scaled output amplitudes. The curves are proved bounds, not computed norms or spectra.

From this directory, install the versions in [requirements.txt](requirements.txt) and run:

```text
python draw_negative_output_boundary.py
```

The complete portable generator registers all thirteen exact bundled DejaVu/STIX font binaries in `fonts/`; eleven are opened in the reference rendering. It writes `../../figures/kt-plaque-negative-output-boundary.png`, `../../figures/kt-plaque-negative-output-boundary.svg` and [figure-and-bounds.json](figure-and-bounds.json). The SVG uses glyph outlines and embeds the full [font notice](FONT-NOTICE.txt). Individual full notices remain in fonts/LICENSE_DEJAVU.txt and fonts/LICENSE_STIX.txt. Use the full-size figures to read fine labels on small screens.

The reference runtime is Python 3.13.9, Matplotlib 3.10.9, NumPy 2.4.4 and Pillow 12.2.0. Reproduction is byte exact in that recorded runtime; another environment may produce different bytes with the same mathematics. Libraries and a Python runtime are not bundled.

The original expression is CC0 1.0. Fonts, glyphs and external software retain their separate terms in [COMPONENT-TERMS.md](COMPONENT-TERMS.md) and the complete accompanying notices. The result concerns the explicitly defined restriction quotient and Dirichlet anti-dual; the inherited supported norm, unrestricted regional dual and common compact interior-buffer requirement remain distinct. It does not identify the historical local plaque norm.
