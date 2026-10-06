# Rebuilding the readers and figures

The distributed Markdown, TeX and PDF files preserve the accepted lesson bytes. Native MathML carries every original formula in its TeX annotation, in source order. The principal readers, mathematics and retained supporting collections can be read offline; external scholarly links need a network connection.

Install Python 3, Beautiful Soup 4 and Pandoc, then run:

```text
python build/build_reader.py --pandoc pandoc
```

The retained supporting collections include their own reader builders and templates. Run each builder in its collection directory to regenerate that collection. To reproduce the figures, install Matplotlib and NumPy and run the Python files in `figures/`; each writes its PNG/SVG outputs beside its source. The supporting collections retain their own figure sources.

For a PDF, use LuaLaTeX with the packages named in the distributed TeX file. Work from the relevant `tex/` directory so its original figure paths remain correct, run the named file at least twice, and move the resulting PDF to `pdf/`. Build metadata and PDF bytes may vary with engine and build date. No TeX/compiler execution occurred in this publication preparation. The distributed source and PDF identities are in the checksum manifests.

Keep every document's companion notice, the title and history notices, and its applicable complete license with separate downloads. The two principal lessons are CC0; inherited supporting components retain GFDL 1.2 only.
