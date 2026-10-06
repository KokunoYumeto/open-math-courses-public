# Course renderer

The three Python modules preserve TeX mathematics while rendering CommonMark with markdown-it-py. They bind lesson and figure sources to the explicit SHA-256 catalogue and check local lesson links and anchors. This copy comes from the Codex-authored Open Research Courses reader, release R5C (21 September 2026), with subsequent table, figure and heading-anchor support. No reader pages or reference-book content were copied.

The course-specific portable builder is `../build_html.py`. Install `markdown-it-py==4.0.0` and run that builder from the source archive. Its output uses the included MathJax 3.2.2 files, whose own copyright and font notices are retained. The source archive contains the rendering modules, not the old site's test suite or publishing scripts.
