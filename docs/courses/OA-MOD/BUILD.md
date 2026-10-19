# Build the course readers

Python 3.10 or later is required. The editable lesson sources are in `src/`, supporting texts in `notes/`, and illustrations and their reproducible sources in `assets/` and `figures/`.

From the repository root, install `courses/OA-MOD/publication/requirements.txt` and run `python courses/OA-MOD/publication/build_readers.py --course` to render the registered lessons. The renderer preserves their existing navigation, result anchors, figures and reading links. Use `--reading OA-MOD-SF` to select one lesson, or a comma-separated list of lesson identifiers. The mathematical expressions are retained in `data-tex` attributes.

Run `python courses/OA-MOD/publication/build_catalogue.py` to render the course entrance and topic routes from `course.json`.

For the separately declared supporting pages, install this directory's `requirements.txt` and run `python build_reader.py --reading sources.html`. Omitting `--reading` builds the declared supporting pages while preserving the course catalogue and canonical lesson redirects. Their stylesheet is `support-reader.css`; it does not replace the lesson stylesheet.

The web readers use the repository's MathJax files under `docs/assets/mathjax`. An offline copy needs those scripts, fonts and their licence notices. Links to other courses and research papers can require network access. The prerequisite guide distinguishes results proved in these lessons from results used from other programme texts.
