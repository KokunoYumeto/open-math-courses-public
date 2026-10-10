# Reproduce the positive-kernel plaque figure

The complete proof is Proposition 6.8g, equations NP.1–NP.12, in *The index theorem for measured foliations*. Exercises 28–30 include their full solutions. The figure shows the exact physical plaque parameters and the proved local upper and global lower bounds. Its enlarged plaque rows are coordinate schematics; their displayed widths are not physical lengths. Sampled integer values illustrate the all-N proof.

From this directory, install the versions in [requirements.txt](requirements.txt) and run:

```text
python draw_negative_output.py
```

The complete generator uses the eleven exact bundled DejaVu/STIX font files in `fonts/`. It writes `../../figures/kt-plaque-negative-output.png`, `../../figures/kt-plaque-negative-output.svg`, and the exact asset/source report [figure-and-bounds.json](figure-and-bounds.json). The SVG uses outlines and embeds the full font notice. Full-size PNG/SVG views are needed to read the fine figure labels on small screens.

The reference runtime is Python 3.13.9, Matplotlib 3.10.9, NumPy 2.4.4 and Pillow 12.2.0. Exact reference-environment reproduction is checked; other environments can produce different bytes while retaining the same mathematics. Libraries and a Python runtime are not bundled here.

The original expression is CC0 1.0. Fonts, glyphs and external software retain their separately scoped terms in COMPONENT-TERMS.md and the complete accompanying notices. The result concerns three stated negative-output completions; it does not identify an unspecified historical plaque norm.
