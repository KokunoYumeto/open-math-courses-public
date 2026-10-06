# Course renderer

The three Python modules preserve TeX mathematics while rendering CommonMark with markdown-it-py. They bind lesson and figure sources to the explicit SHA-256 catalogue and check local lesson links and anchors. This copy comes from the Codex-authored Open Research Courses reader, release R5C (21 September 2026), with subsequent table, figure and heading-anchor support. No reader pages or reference-book content were copied.

The course-specific portable builder is `../build.py`. Install `markdown-it-py==4.0.0` and Pandoc, then run that builder from the source archive. Its output uses the included MathJax 3.2.2 files, whose own copyright and font notices are retained.

The catalogue's `programme_links` array explicitly permits sibling-course reader paths of the form `../course-slug/lesson-slug.html`. The prerequisite record supplies the exact statements, source identities and theorem anchors. These routes keep the programme connected without copying a second edition of each prerequisite into this course. A single-course archive needs the corresponding sibling courses for offline cross-course navigation. Local and remote source paths remain rejected by the renderer.
