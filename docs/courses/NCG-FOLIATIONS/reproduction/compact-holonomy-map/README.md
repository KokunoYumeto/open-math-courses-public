# Reproduce the compact holonomy figure

Use Python 3.11 or newer and the packages in [requirements.txt](requirements.txt):

```text
python -m pip install -r requirements.txt
python draw_compact_map.py
```

All glyphs come from the bundled unmodified font. The generator selects the bundled font explicitly and writes PNG and editable SVG to the course figures directory. Use --output-dir to choose another destination. The SVG contains the complete font notice. See [component terms](COMPONENT-TERMS.md).
