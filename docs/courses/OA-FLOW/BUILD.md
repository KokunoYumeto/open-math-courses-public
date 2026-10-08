# Reading and rebuilding OA-FLOW

The current edition is listed in `docs/courses/OA-FLOW/course.json`. Each entry identifies its Markdown source, HTML reader and current file hashes. Mathematical records and exact source ranges are in `results.json`; the lesson count comes from the registry rather than a fixed selection.

## Read the course locally

From the repository root, with Python 3.10 or later:

```console
python -m http.server 8000 --directory docs
```

Open [the course index](http://localhost:8000/courses/OA-FLOW/). Serving the entire `docs` directory preserves links to the other programme courses. The course's MathJax scripts and fonts are bundled locally; links to human reference works may require internet access. The checked-in HTML can be read without rebuilding.

## Validate the checked-in edition

Run these commands from the repository root:

```console
python -m pip install -r courses/OA-FLOW/reader-records/requirements.txt
python -B courses/OA-FLOW/reader-records/validate_current_lessons.py
```

The validator is read-only. It checks every registered source/reader hash, complete recorded source range, source/reader TeX sequence, local link and asset route, result anchor, and declared internal prerequisite's lesson order. It reports its counts and errors as JSON and exits unsuccessfully on a failed check. To check selected lessons, append their IDs:

```console
python -B courses/OA-FLOW/reader-records/validate_current_lessons.py OA-FLOW-CSAS OA-FLOW-CAPP
```

These are file and record checks. They do not establish mathematical correctness, the adequacy of implicit prerequisites, same-lesson proof availability, external-source access or browser layout.

## Check reader reproduction without writing files

```console
python -B courses/OA-FLOW/reader-records/build_current_lessons.py --check
```

This renders every registered lesson in memory and compares the resulting bytes with the checked-in readers and their supporting indexes and registries. It writes no readers or temporary copies, reports any differing paths, and exits unsuccessfully if a difference remains. Append lesson IDs after `--check` for a selected check. The input files are the programme Markdown, complete proof records, renderer code and `reader-presentation.json`; external source books and papers are not inputs. This is a reproduction check, not a mathematical or licensing audit.

## Rebuild selected readers

After updating a lesson source and its complete records in `results.json`, name the lessons explicitly:

```console
python -B courses/OA-FLOW/reader-records/build_current_lessons.py OA-FLOW-CSAS OA-FLOW-CAPP
python -B courses/OA-FLOW/reader-records/validate_current_lessons.py
```

The builder updates the named HTML readers, their immediate navigation neighbours, course index, prerequisite index and registered source/reader hashes. Source image paths are adjusted for the readers' location one directory above `src/`. It preserves complete TeX expressions in `data-tex` attributes. It requires the recorded proof bodies to be present in the source; it does not write proofs or infer new dependency records. If source edits change a cited proof, update its exact ranges and dependent identity bindings before rebuilding.

Current opening notices, retained heading aliases, HTML serialization and prerequisite-index selections are explicit in `courses/OA-FLOW/reader-records/reader-presentation.json`. Keep that file with the renderer. These presentation settings preserve the published reader independently of historical authorship records.

The current builder is `courses/OA-FLOW/reader-records/build_current_lessons.py`. The older `build_reader.py` supplies rendering functions; its command-line selection/archive workflow describes a historical edition and is not a cumulative exporter for this one. There is no current whole-course archive command or portable-download claim in these instructions.

## Reproduce illustrations and retain component terms

Original illustration programs and mathematical data accompany the assets under `docs/courses/OA-FLOW/assets/`. Consult each program's instructions and nearby component notice for its working directory and dependencies. Some use Python alone; others use Matplotlib, NumPy or browser rasterization. Raster bytes can depend on the recorded font, library and browser versions. Keep the exact data and proof locators alongside regenerated figures.

Lesson authorship and human references are recorded in the individual lessons. Retain `LICENSE.txt`, `LICENSE.md` and the asset notices. Historical binding records that quote the former CV-4 adaptation retain its CC BY 4.0 attribution and change notice; the current CV-4 replacement has its own stated terms. Fonts and software retain their respective terms. Source books and papers are not build inputs and are not bundled with the course.
