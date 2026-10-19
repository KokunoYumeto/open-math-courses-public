# Course renderer

The CC0 modules `course_reader.py`, `course_assets.py` and `output_safety.py`
render CommonMark with TeX mathematics as HTML. MathJax typesets the formulas.

The catalogue names every lesson source and its SHA-256 identity. TeX is
protected before Markdown parsing, and inter-lesson links and anchors are
resolved against the catalogue. Linked SVG and other supporting files are
listed with their sizes and SHA-256 identities in `linked_files`.

Each PNG figure has an explicit identifier, source path, hash, dimensions,
alternative text, authorship credit and source attribution. The renderer
validates the PNG format and size and rejects machine-local paths in content.

`build_release.py` supplies the course page layout. From the course directory,
`sync_lessons.py` regenerates the selected lesson readers. The TeX expression
is available in each formula's `data-tex` attribute.

Renderer authorship: OpenAI. CC0 1.0. Dependency notices accompany the code.
