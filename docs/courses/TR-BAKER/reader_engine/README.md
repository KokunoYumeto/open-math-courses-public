# Course renderer

The renderer converts CommonMark lessons with TeX mathematics to HTML. The course's `build_reader.py` uses `course_reader.py`, `course_assets.py` and `output_safety.py` from this directory. MathJax displays the formulas in the browser.

Run the course commands from the extracted package root:

```text
python -m pip install markdown-it-py
python docs/courses/TR-BAKER/build_reader.py --readers
python docs/courses/TR-BAKER/build_reader.py --tex --pandoc pandoc
python -m http.server 8000 --directory docs
```

Open `http://localhost:8000/courses/TR-BAKER/`. The editable LaTeX files can also be compiled directly as described in `../sources/README.md`.

## Mathematics, links and figures

The renderer separates TeX from Markdown before parsing, preserving underscores, asterisks and backslashes inside formulas. Heading identifiers support links to precise sections. The course manifest identifies the lesson sources, figures, dimensions, authorship and content hashes. The source package uses an explicit file list.

Markdown tables are supported. Use `\lvert x\rvert` or `\vert` for a vertical bar inside a table formula, since a literal `|` separates table cells.

Figures use their declared paths and alternative text. CSS, MathJax, software licences and font notices accompany the offline reader. Cross-course mathematical prerequisite links refer to the corresponding courses in the full programme.

## Software provenance

The renderer originates in the Open Research Courses R5C renderer, dated 21 September 2026 and written in Codex. The package contains its rendering utilities and the course adapter. Licence terms are given in `../LICENCE.txt` and the accompanying notices.
