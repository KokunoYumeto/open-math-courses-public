"""Build the owned private NOE-IDL reader after canonical corrections are integrated.

Requires Python 3.10+, Pandoc, canonical NOE-IDL and AG-CA source trees, the
existing MathJax runtime, and the owner's pending-programme scope record.
No shared registry, shared site builder, network access, Git command, PDF
generation or TeX compilation is used. All writes are confined to the three
explicitly selected owned destinations. Original source bodies are copied
byte-for-byte; only rendered link targets are changed.

Workspace invocation:
  python work/build_private_corrected_reader.py --scope-record PATH

Portable invocations can override --source-course, --prerequisite-course,
--mathjax, --output, --repository and --pandoc. The source ZIP includes this
script and the input layout needed to rebuild independently.

Original build script: GPT-6.1 Sol (OpenAI), Ultra. CC0 1.0 Universal.
"""
from __future__ import annotations

import argparse
import copy
import hashlib
import html
import json
import os
from pathlib import Path, PurePosixPath
import posixpath
import re
import shutil
import subprocess
import tempfile
from html.parser import HTMLParser
from urllib.parse import unquote, urlsplit, urlunsplit
import zipfile


OWN_IDS = tuple(f"NOE-IDL-{number:02d}" for number in range(1, 6))
PAPERS = {
    19: ("Ideal Theory in Ring Domains", "Emmy Noether"),
    22: ("On the Theory of Polynomial Ideals and Resultants", "Kurt Hentzelt, edited by Emmy Noether"),
    24: ("Elimination Theory and General Ideal Theory", "Emmy Noether"),
}
MD_FORMAT = "markdown+tex_math_single_backslash"
PAID_NAMES = re.compile(
    r"Cox\s*[,–—-]\s*Little|Cox[^\n]{0,80}O['’]Shea|"
    r"Ideals,?\s+Varieties,?\s+and\s+Algorithms|"
    r"(?:Atiyah|Matsumura|Bourbaki)[^\n]{0,90}(?:Press|Springer|edition)|"
    r"Springer(?:[- ]Verlag)?|Cambridge University Press|Oxford University Press",
    re.I,
)
PAID_HOSTS = {"link.springer.com", "www.springer.com", "shop.elsevier.com", "www.sciencedirect.com"}
FREE_HOSTS = {
    "arxiv.org", "zenodo.org", "github.com", "raw.githubusercontent.com",
    "stacks.math.columbia.edu", "www.jmilne.org", "jmilne.org",
    "creativecommons.org", "gdz.sub.uni-goettingen.de", "eudml.org",
}
CSS = """
:root{color-scheme:light dark;--paper:#f9f7f1;--ink:#252b2b;--muted:#5f6865;--link:#176b63;--line:#d7ddd5}
*{box-sizing:border-box}body{margin:0;background:var(--paper);color:var(--ink);font:18px/1.7 Georgia,serif}
main{max-width:980px;margin:auto;padding:2rem 1.5rem 4rem}a{color:var(--link);text-underline-offset:.17em}
header,nav,footer,.notice{font-family:system-ui,sans-serif}nav{display:flex;flex-wrap:wrap;gap:.9rem;font-size:.9rem}
h1{font-size:clamp(2rem,5vw,3.25rem);line-height:1.16;margin:1.5rem 0}h2{margin-top:2.4rem;line-height:1.25}
h3{line-height:1.3}.notice{padding:1rem 1.2rem;border:1px solid var(--line);border-left:4px solid var(--link);font-size:.92rem}
article img{max-width:100%;height:auto;display:block;margin:1.5rem auto}pre{overflow:auto;padding:1rem;border:1px solid var(--line)}
article{min-width:0;overflow-wrap:anywhere}
.math.inline{display:inline-block;max-width:100%;overflow-x:auto;overflow-y:hidden;vertical-align:middle;padding:.2rem 0}
code{font-size:.86em}table{border-collapse:collapse;display:block;overflow-x:auto}td,th{padding:.5rem .8rem;border:1px solid var(--line)}
.math.display,mjx-container[display="true"]{display:block;overflow-x:auto;overflow-y:hidden;padding:.2rem 0}
.cards{display:grid;grid-template-columns:repeat(auto-fit,minmax(260px,1fr));gap:1rem;list-style:none;padding:0}
.cards li{padding:1rem;border:1px solid var(--line);border-radius:.35rem}.cards a{font-size:1.1rem;font-weight:600}
footer{margin-top:3rem;padding-top:1rem;border-top:1px solid var(--line);font-size:.85rem;color:var(--muted)}
.skip{position:absolute;left:-9999px}.skip:focus{left:1rem;top:1rem;background:var(--paper);padding:1rem}
@media(prefers-color-scheme:dark){:root{--paper:#17201e;--ink:#ecede8;--muted:#b6c0b8;--link:#80d6c0;--line:#40504b}}
@media(max-width:600px){body{font-size:17px}main{padding:1rem .9rem 3rem}.cards{grid-template-columns:1fr}}
"""


def sha_bytes(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def is_link(path: Path) -> bool:
    return path.is_symlink() or (hasattr(path, "is_junction") and path.is_junction())


def contained(root: Path, relative: str) -> Path:
    rel = PurePosixPath(relative.replace("\\", "/"))
    if rel.is_absolute() or ".." in rel.parts or not rel.parts:
        raise ValueError(f"Unsafe relative package path: {relative}")
    result = root.joinpath(*rel.parts)
    if not result.resolve().is_relative_to(root.resolve()):
        raise ValueError(f"Package path leaves its selected root: {relative}")
    return result


def read_tree(root: Path) -> dict[str, bytes]:
    if not root.is_dir() or is_link(root):
        raise ValueError(f"Missing ordinary input directory: {root}")
    result = {}
    for path in sorted(root.rglob("*")):
        if is_link(path):
            raise ValueError(f"Input contains a symbolic link or junction: {path}")
        if path.is_file():
            data = path.read_bytes()
            if path.suffix.lower() in {".txt", ".tex", ".md", ".html", ".json", ".py", ".svg", ".js", ".css"} or path.name in {"LICENSE", "FONT-LICENSES.txt"}:
                data = data.replace(b"\r\n", b"\n")
            result[path.relative_to(root).as_posix()] = data
    return result


def json_bytes(value: object) -> bytes:
    return (json.dumps(value, ensure_ascii=False, indent=2) + "\n").encode("utf-8")


def find_pandoc(explicit: str | None) -> str:
    candidates = [explicit, shutil.which("pandoc")]
    local = os.environ.get("LOCALAPPDATA")
    if local:
        candidates.append(str(Path(local) / "Pandoc" / "pandoc.exe"))
    candidates += [str(Path.home() / ".local/bin/pandoc"), "/usr/local/bin/pandoc", "/usr/bin/pandoc"]
    for candidate in candidates:
        if candidate and Path(candidate).is_file():
            return str(Path(candidate).resolve())
    raise ValueError("Installed Pandoc was not found; supply --pandoc with its executable path.")


def pandoc(executable: str, data: bytes, *arguments: str) -> bytes:
    process = subprocess.run(
        [executable, *arguments], input=data, stdout=subprocess.PIPE,
        stderr=subprocess.PIPE, check=False,
    )
    if process.returncode:
        raise RuntimeError("Pandoc failed: " + process.stderr.decode("utf-8", errors="replace"))
    # Keep diagnostics in the private receipt, never append them to reader text.
    if process.stderr:
        PANDOC_DIAGNOSTICS.append(process.stderr.decode("utf-8", errors="replace"))
    return process.stdout


PANDOC_DIAGNOSTICS: list[str] = []


class Document:
    def __init__(self, cid: str, unit: dict, root: Path, executable: str):
        self.cid = cid
        self.uid = unit["id"]
        self.title = unit["title"]
        self.source = unit["source"]
        self.declared_license = unit.get("license")
        self.path = contained(root, self.source).resolve()
        self.data = self.path.read_bytes()
        self.ast = json.loads(pandoc(executable, self.data, "-f", MD_FORMAT, "-t", "json"))
        self.output = f"{self.uid}.html" if cid == "NOE-IDL" else f"prerequisites/AG-CA/{self.uid}.html"


def targets(value: object):
    if isinstance(value, dict):
        if value.get("t") in {"Link", "Image"}:
            yield value["t"], value["c"][-1][0]
        for child in value.values():
            yield from targets(child)
    elif isinstance(value, list):
        for child in value:
            yield from targets(child)


def relative_url(destination: str, page: str, query: str = "", fragment: str = "") -> str:
    relative = posixpath.relpath(destination, posixpath.dirname(page) or ".")
    return urlunsplit(("", "", relative, query, fragment))


def private_ref(url: str, document: Document, by_path: dict, by_uid: dict) -> Document | None:
    parts = urlsplit(url)
    path = unquote(parts.path)
    if parts.scheme in {"http", "https"} or parts.netloc:
        match = re.search(r"/(NOE-IDL|AG-CA)/(?:src/)?([^/]+)$", path)
        if match:
            cid, filename = match.groups()
            stem = Path(filename).stem
            return by_uid.get(stem) or next(
                (doc for doc in by_uid.values() if doc.cid == cid and Path(doc.source).stem == stem), None
            )
        return None
    if parts.scheme or not path or not path.endswith((".md", ".html")):
        return None
    resolved = (document.path.parent / path).resolve()
    if resolved in by_path:
        return by_path[resolved]
    stem = Path(path).stem
    if stem in by_uid:
        return by_uid[stem]
    cid = "AG-CA" if "AG-CA" in PurePosixPath(path).parts else document.cid
    return next((doc for doc in by_uid.values() if doc.cid == cid and Path(doc.source).stem == stem), None)


def validate_owned_citations(document: Document, extra_free: set[str]) -> None:
    source = document.data.decode("utf-8")
    if PAID_NAMES.search(source):
        raise ValueError(f"Paid-reference wording remains in {document.uid}; integrate the corrected lesson first.")
    for kind, target in targets(document.ast):
        parts = urlsplit(target)
        if parts.scheme not in {"http", "https"} and not parts.netloc:
            continue
        host = (parts.hostname or "").lower()
        if host in PAID_HOSTS or (host == "doi.org" and parts.path.lower().startswith("/10.1007/")):
            raise ValueError(f"Paid publication endpoint remains in {document.uid}: {target}")
        if target in extra_free:
            continue
        if host in FREE_HOSTS:
            continue
        if host == "doi.org" and parts.path.lower().startswith(("/10.5281/zenodo.", "/10.48550/arxiv.")):
            continue
        if host == "kokunoyumeto.github.io" and (
            "/stacks-zh-hans-cn/" in parts.path or "/courses/AG-CA/" in parts.path or "/courses/NOE-IDL/" in parts.path
        ):
            continue
        raise ValueError(
            f"Unverified external reference in {document.uid}: {target}. "
            "Use an actual free edition, or add the verified exact URL to the owner's scope record free_reference_urls."
        )
    if any(kind == "Image" and (urlsplit(target).scheme or urlsplit(target).netloc) for kind, target in targets(document.ast)):
        raise ValueError(f"Remote image would make {document.uid} incomplete offline.")


def map_ast(document: Document, selected: dict, by_path: dict, roots: dict, *, tex: bool = False) -> dict:
    ast = copy.deepcopy(document.ast)
    page = "downloads/ideal-theory-in-rings.tex" if tex else document.output

    def mapped(url: str, kind: str) -> str:
        parts = urlsplit(url)
        target_doc = private_ref(url, document, by_path, selected)
        if target_doc:
            if target_doc.uid not in selected:
                raise ValueError(f"Prerequisite closure missing {target_doc.uid}")
            fragment = parts.fragment
            header_ids = {block["c"][1][0] for block in target_doc.ast["blocks"] if block.get("t") == "Header"}
            plain_fragment = re.sub(r"^\d+-", "", fragment)
            if fragment not in header_ids and plain_fragment in header_ids:
                fragment = plain_fragment
            return relative_url(target_doc.output, page, parts.query, fragment)
        if parts.scheme or parts.netloc or not parts.path:
            return url
        if document.cid == "AG-CA" and PurePosixPath(parts.path).name in {"CC0-1.0.txt", "COPYING-GFDL-1.2.txt"}:
            return relative_url("prerequisites/AG-CA/" + PurePosixPath(parts.path).name, page, parts.query, parts.fragment)
        source_target = (document.path.parent / unquote(parts.path)).resolve()
        asset_root = roots[document.cid] / "assets"
        if source_target.is_relative_to(asset_root.resolve()):
            prefix = "assets" if document.cid == "NOE-IDL" else "prerequisites/AG-CA/assets"
            tail = source_target.relative_to(asset_root.resolve()).as_posix()
            destination = f"downloads/assets/{tail}" if tex and document.cid == "NOE-IDL" else f"{prefix}/{tail}"
            return relative_url(destination, page, parts.query, parts.fragment)
        if document.cid == "NOE-IDL" and "downloads" in PurePosixPath(parts.path).parts:
            filename = PurePosixPath(parts.path).name
            permitted = {"ideal-theory-in-rings.tex", "ideal-theory-in-rings-source.zip", *(uid + ".tex" for uid in OWN_IDS)}
            if filename not in permitted:
                raise ValueError(f"Unsupported owned download link: {url}")
            return relative_url("downloads/" + filename, page, parts.query, parts.fragment)
        if source_target.is_relative_to((roots["NOE-IDL"] / "historical").resolve()):
            tail = source_target.relative_to((roots["NOE-IDL"] / "historical").resolve()).as_posix()
            return relative_url("historical/" + tail, page, parts.query, parts.fragment)
        raise ValueError(f"Unmapped local link in {document.uid}: {url}")

    def visit(value: object):
        if isinstance(value, dict):
            if value.get("t") in {"Link", "Image"}:
                value["c"][-1][0] = mapped(value["c"][-1][0], value["t"])
            for child in value.values():
                visit(child)
        elif isinstance(value, list):
            for child in value:
                visit(child)
    visit(ast)
    return ast


def wrapper(title: str, body: str, page: str, *, navigation: str = "", notice: str = "") -> bytes:
    runtime = relative_url("runtime/mathjax/tex-chtml-full.js", page)
    runtime_directory = relative_url("runtime/mathjax", page)
    fonts = relative_url("runtime/mathjax/output/chtml/fonts/woff-v2", page)
    home = relative_url("index.html", page)
    notices = relative_url("NOTICES.txt", page)
    config = {
        "loader": {"paths": {"mathjax": runtime_directory}},
        "tex": {"inlineMath": [["\\(", "\\)"], ["$", "$"]], "displayMath": [["\\[", "\\]"], ["$$", "$$"]], "processEscapes": True, "macros": {"Eta": "\\mathrm{H}"}},
        "chtml": {"fontURL": fonts},
        "options": {"ignoreHtmlClass": "no-math", "processHtmlClass": "math"},
    }
    browser_title = title if title == "Ideal theory in rings" else title + " · Ideal theory in rings"
    document = f"""<!doctype html>
<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>{html.escape(browser_title)}</title><meta name="robots" content="noindex,nofollow">
<style>{CSS}</style><script>window.MathJax={json.dumps(config, ensure_ascii=False)};</script>
<script id="MathJax-script" defer src="{html.escape(runtime, quote=True)}"></script></head>
<body class="no-math"><a class="skip" href="#main">Skip to content</a><main id="main">
<header><nav aria-label="Course navigation"><a href="{html.escape(home, quote=True)}">Ideal theory in rings</a>{navigation}</nav></header>
{('<aside class="notice">' + notice + '</aside>') if notice else ''}
<article class="math">{body}</article>
<footer>Original course contributions: CC0 1.0. Historical readings, prerequisite snapshots, rendering software and fonts retain their own notices. <a href="{html.escape(notices, quote=True)}">Component notices</a>.</footer>
</main></body></html>"""
    return document.encode("utf-8")


class LocalLinks(HTMLParser):
    def __init__(self):
        super().__init__()
        self.links = []
        self.ids = set()

    def handle_starttag(self, tag, attrs):
        attributes = dict(attrs)
        if "id" in attributes:
            self.ids.add(attributes["id"])
        for key in ("href", "src"):
            if key in attributes:
                self.links.append(attributes[key])


def validate_bundle(files: dict[str, bytes]) -> int:
    pages = {}
    for name, data in files.items():
        if name.endswith(".html") and not name.startswith("source-course/"):
            parser = LocalLinks()
            parser.feed(data.decode("utf-8"))
            pages[name] = parser
    total = 0
    for name, page in pages.items():
        for url in page.links:
            parts = urlsplit(url)
            if parts.scheme or parts.netloc:
                continue
            destination = posixpath.normpath(posixpath.join(posixpath.dirname(name), unquote(parts.path))) if parts.path else name
            if destination not in files:
                raise ValueError(f"Broken local reader link: {name} -> {url}")
            if parts.fragment and destination in pages and unquote(parts.fragment) not in pages[destination].ids:
                raise ValueError(f"Broken reader anchor: {name} -> {url}")
            total += 1
    return total


def publish_files(root: Path, files: dict[str, bytes]) -> None:
    """Copy only explicitly owned files; never delete or traverse unrelated data."""
    if is_link(root):
        raise ValueError(f"Output root is a symbolic link or junction: {root}")
    root.mkdir(parents=True, exist_ok=True)
    for relative, data in sorted(files.items()):
        target = contained(root, relative)
        target.parent.mkdir(parents=True, exist_ok=True)
        if not target.exists() or target.read_bytes() != data:
            target.write_bytes(data)


def parser() -> argparse.ArgumentParser:
    here = Path(__file__).resolve().parent
    workspace_layout = (here / "site/courses/NOE-IDL/course.json").is_file()
    source = here / "site/courses/NOE-IDL" if workspace_layout else here / "source-course"
    if not source.is_dir() and (here / "src").is_dir():
        source = here
    prerequisites = here / "agca-source-repair/reconciled" if workspace_layout else here / "prerequisites/AG-CA"
    runtime = here / "site/docs/assets/mathjax" if workspace_layout else here / "runtime/mathjax"
    course_root_layout = source == here
    portable_output = here.parent / (here.name + "-reader") if course_root_layout else here / "reader"
    portable_repository = here.parent / (here.name + "-private-repo") if course_root_layout else here / "private-repo"
    result = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    result.add_argument("--source-course", type=Path, default=source)
    result.add_argument("--prerequisite-course", type=Path, default=prerequisites)
    result.add_argument("--mathjax", type=Path, default=runtime)
    result.add_argument("--scope-record", type=Path, default=here / "private-scope.json")
    result.add_argument("--output", type=Path, default=here.parent / "outputs/private-course" if workspace_layout else portable_output)
    result.add_argument("--repository", type=Path, default=here / "current-repo" if workspace_layout else portable_repository)
    result.add_argument("--pandoc")
    return result


def main() -> None:
    args = parser().parse_args()
    source, preq, runtime = (path.resolve() for path in (args.source_course, args.prerequisite_course, args.mathjax))
    scope_path = args.scope_record.resolve()
    if not scope_path.is_file():
        raise ValueError("Supply --scope-record PATH with the owner's exact pending-programme scope record.")
    scope_bytes = scope_path.read_bytes()
    scope = json.loads(scope_bytes)
    if not isinstance(scope, dict):
        raise ValueError("The owner scope record must be a JSON object; it is preserved without granting public clearance.")
    executable = find_pandoc(args.pandoc)
    source_meta_bytes = (source / "course.json").read_bytes().replace(b"\r\n", b"\n")
    source_meta = json.loads(source_meta_bytes)
    preq_meta_bytes = (preq / "course.json").read_bytes()
    preq_meta = json.loads(preq_meta_bytes)
    if source_meta.get("id") != "NOE-IDL" or preq_meta.get("id") != "AG-CA":
        raise ValueError("Input course identities must be NOE-IDL and AG-CA.")
    own = {row["id"]: Document("NOE-IDL", row, source, executable) for row in source_meta["units"]}
    preq_units = preq_meta.get("units", preq_meta.get("lessons", []))
    earlier = {row["id"]: Document("AG-CA", row, preq, executable) for row in preq_units if contained(preq, row["source"]).is_file()}
    if set(own) != set(OWN_IDS):
        raise ValueError("The corrected owned course must contain exactly NOE-IDL-01 through NOE-IDL-05.")
    all_docs = {**own, **earlier}
    by_path = {doc.path: doc for doc in all_docs.values()}
    selected = dict(own)
    todo = list(own.values())
    while todo:
        doc = todo.pop()
        for _, url in targets(doc.ast):
            linked = private_ref(url, doc, by_path, all_docs)
            if linked and linked.uid not in selected:
                selected[linked.uid] = linked
                todo.append(linked)
            if urlsplit(url).scheme in {"http", "https"} and "/courses/AG-CA/" in url and not linked:
                raise ValueError(f"Actual local AG-CA snapshot is missing for {doc.uid}: {url}")
    for doc in own.values():
        validate_owned_citations(doc, set(scope.get("free_reference_urls", [])))
    for doc in selected.values():
        if doc.cid != "AG-CA":
            continue
        text = doc.data.decode("utf-8")
        if re.search(r"Alg[èe]bre\s+locale|Serre[^\n]{0,100}Local\s+Algebra", text, re.I):
            raise ValueError(f"Stale unapproved Serre book citation remains in {doc.uid}.")
        if doc.declared_license not in {"CC0-1.0", "GFDL-1.2-or-later"}:
            raise ValueError(f"Exact per-lesson component terms are missing for {doc.uid}.")
        if doc.declared_license == "GFDL-1.2-or-later" and "GNU Free Documentation License" not in text:
            raise ValueError(f"Incorporated-source component notice is missing for {doc.uid}.")
    roots = {"NOE-IDL": source, "AG-CA": preq}
    runtime_files = read_tree(runtime)
    for required in ("tex-chtml-full.js", "LICENSE", "FONT-LICENSES.txt"):
        if required not in runtime_files:
            raise ValueError(f"Local MathJax runtime or its notice is incomplete: {required}")
    if not any(name.endswith(".woff") for name in runtime_files):
        raise ValueError("The local MathJax runtime is missing its offline fonts.")
    owned_assets = read_tree(source / "assets")
    earlier_assets = read_tree(preq / "assets") if (preq / "assets").is_dir() else {}
    historical = read_tree(source / "historical")
    for number in PAPERS:
        for suffix in ("html", "tex"):
            if f"paper-{number}-english.{suffix}" not in historical:
                raise ValueError(f"Historical source is missing: paper-{number}-english.{suffix}")
    for name in ("LICENSE-English.txt", "provenance.json"):
        if name not in historical:
            raise ValueError(f"Historical rights/provenance input is missing: {name}")
    files: dict[str, bytes] = {}
    for name, data in runtime_files.items():
        files["runtime/mathjax/" + name] = data
    for name, data in owned_assets.items():
        files["assets/" + name] = data
        files["downloads/assets/" + name] = data
        files["source-course/assets/" + name] = data
    for name, data in earlier_assets.items():
        files["prerequisites/AG-CA/assets/" + name] = data
    for name, data in historical.items():
        # Never import old PDFs or archives into this source-only build.
        if Path(name).suffix.lower() not in {".pdf", ".zip"}:
            files["source-course/historical/" + name] = data
    files["source-course/course-source-metadata.json"] = source_meta_bytes
    files["prerequisites/AG-CA/course-source-metadata.json"] = preq_meta_bytes
    for name in ("CC0-1.0.txt", "COPYING-GFDL-1.2.txt"):
        notice_path = preq / name
        if notice_path.is_file():
            files["prerequisites/AG-CA/" + name] = notice_path.read_bytes()
    files["private-scope.json"] = scope_bytes
    files["build_private_corrected_reader.py"] = Path(__file__).read_bytes()
    unit_rows = []
    prerequisite_rows = []
    latex_bodies = []
    for uid in OWN_IDS:
        doc = own[uid]
        files["source-course/" + doc.source] = doc.data
        ast = map_ast(doc, selected, by_path, roots)
        fragment = pandoc(executable, json_bytes(ast), "-f", "json", "-t", "html5", "--mathjax").decode("utf-8")
        number = OWN_IDS.index(uid)
        links = []
        if number:
            links.append(f'<a href="{OWN_IDS[number-1]}.html">Previous lesson</a>')
        if number + 1 < len(OWN_IDS):
            links.append(f'<a href="{OWN_IDS[number+1]}.html">Next lesson</a>')
        links += [f'<a href="source-course/{html.escape(doc.source, quote=True)}">Markdown source</a>', f'<a href="downloads/{uid}.tex">LaTeX source</a>']
        files[doc.output] = wrapper(doc.title, fragment, doc.output, navigation="".join(links))
        tex_ast = map_ast(doc, selected, by_path, roots, tex=True)
        tex_json = json_bytes(tex_ast)
        latex = pandoc(executable, tex_json, "-f", "json", "-t", "latex", "--standalone", "-V", "geometry:margin=25mm", "-V", "colorlinks:true")
        files[f"downloads/{uid}.tex"] = latex
        latex_bodies += tex_ast["blocks"]
        unit_rows.append({"id": uid, "title": doc.title, "source": doc.source, "source_sha256": sha_bytes(doc.data), "reader": doc.output, "license": "CC0-1.0", "public_release_clearance": False})
    combined = copy.deepcopy(own[OWN_IDS[0]].ast)
    combined["blocks"] = latex_bodies
    combined["meta"] = {"title": {"t": "MetaString", "c": source_meta.get("title", "Ideal theory in rings")}}
    files["downloads/ideal-theory-in-rings.tex"] = pandoc(executable, json_bytes(combined), "-f", "json", "-t", "latex", "--standalone", "--toc", "-V", "geometry:margin=25mm", "-V", "colorlinks:true")
    for uid, doc in sorted(selected.items()):
        if doc.cid != "AG-CA":
            continue
        files["prerequisites/AG-CA/" + doc.source] = doc.data
        fragment = pandoc(executable, json_bytes(map_ast(doc, selected, by_path, roots)), "-f", "json", "-t", "html5", "--mathjax").decode("utf-8")
        source_link = relative_url("prerequisites/AG-CA/" + doc.source, doc.output)
        terms = doc.declared_license or preq_meta.get("license")
        licence_name = "COPYING-GFDL-1.2.txt" if terms == "GFDL-1.2-or-later" else "CC0-1.0.txt"
        licence_url = relative_url("prerequisites/AG-CA/" + licence_name, doc.output)
        notice = f'Private prerequisite snapshot. Component terms: <a href="{html.escape(licence_url, quote=True)}">{html.escape(terms)}</a>. The complete source body and attribution are retained. This snapshot has not been cleared for public release.'
        files[doc.output] = wrapper(doc.title, fragment, doc.output, navigation=f'<a href="{html.escape(source_link, quote=True)}">Original Markdown snapshot</a>', notice=notice)
        prerequisite_rows.append({"id": uid, "title": doc.title, "source": "prerequisites/AG-CA/" + doc.source, "source_sha256": sha_bytes(doc.data), "reader": doc.output, "reader_sha256": sha_bytes(files[doc.output]), "declared_source_license": doc.declared_license or preq_meta.get("license"), "source_body_preserved": True, "attribution_preserved": True, "public_release_clearance": False})
    for number, (title, author) in PAPERS.items():
        page = f"historical/paper-{number}-english.html"
        fragment = historical[f"paper-{number}-english.html"].decode("utf-8")
        if re.search(r"<(?:script|iframe|object)\b", fragment, re.I):
            raise ValueError(f"Unexpected active content in historical source paper {number}")
        notice = f"Historical reading by {html.escape(author)}. Working English translation from the <a href=\"https://zenodo.org/records/21923146\">free source edition</a>. The translation layer and original work retain their separate rights."
        files[page] = wrapper(title, fragment, page, navigation=f'<a href="../source-course/historical/paper-{number}-english.tex">Historical TeX source</a>', notice=notice)
    cards = "".join(f'<li><a href="{row["reader"]}">{html.escape(row["title"])}</a><br>Lesson {i} of 5</li>' for i, row in enumerate(unit_rows, 1))
    readings = "".join(f'<li><a href="historical/paper-{number}-english.html">{html.escape(title)}</a></li>' for number, (title, _) in PAPERS.items())
    proof_links = "".join(f'<li><a href="{row["reader"]}">{html.escape(row["title"])}</a></li>' for row in prerequisite_rows)
    body = f'<h1>{html.escape(source_meta.get("title", "Ideal theory in rings"))}</h1><p>{html.escape(source_meta.get("description", ""))}</p><ul class="cards">{cards}</ul><h2>Historical readings</h2><ul>{readings}</ul><h2>Prerequisite readings</h2><p>The linked source snapshots are supplied privately with their attribution and component notices. They have not been cleared for public release.</p><ul>{proof_links}</ul><h2>Editable sources</h2><p><a href="downloads/ideal-theory-in-rings.tex">Complete LaTeX source</a> · <a href="downloads/ideal-theory-in-rings-source.zip">Complete source archive</a></p>'
    files["index.html"] = wrapper("Ideal theory in rings", body, "index.html")
    proof_body = (
        '<h1>Proof readings and scope</h1>'
        '<p>The five lessons supply the decomposition, counting, field-extension '
        'and elimination arguments. Their exact earlier commutative-algebra '
        'readings are linked below with preserved source bodies and attribution.</p>'
        '<h2>Several-variable analysis</h2><p>The module lesson proves its '
        'symbol-algebra theorem for finite-dimensional quotients of '
        'the complex polynomial ring on every connected open set. '
        'The full smooth-system fundamental principle on general convex open '
        'sets remains an unfinished analytic programme obligation; its density '
        'and integral-representation proof is not supplied in this bundle.</p>'
        '<h2>Earlier commutative algebra</h2><ul>' + proof_links + '</ul>'
        '<p><a href="course.json">Exact source identities and component terms</a></p>'
    )
    files["proof-index.html"] = wrapper("Proof readings and scope", proof_body, "proof-index.html")
    notices = (
        "Original NOE-IDL lesson text, original figures and this build script: CC0 1.0 Universal.\n"
        "https://creativecommons.org/publicdomain/zero/1.0/legalcode\n\n"
        "Prerequisite source bodies and attribution are preserved as private snapshots; no public clearance or global proof closure is asserted.\n"
        "Their declared source notices remain in each source body. Linked external works are not incorporated or relicensed.\n\n"
        "AG-CA prerequisite components use the per-lesson terms in course.json: independently authored CC0 text and genuine incorporated Stacks text under GFDL 1.2 or later.\n"
        "Full component terms: prerequisites/AG-CA/CC0-1.0.txt and prerequisites/AG-CA/COPYING-GFDL-1.2.txt.\n\n"
        "Historical English readings: source-course/historical/LICENSE-English.txt and provenance.json. Original works and third-party materials are not relicensed.\n\n"
        "MathJax rendering software: Apache 2.0, runtime/mathjax/LICENSE. MathJax fonts retain their own terms in runtime/mathjax/FONT-LICENSES.txt.\n"
        "Rendered DejaVu glyphs retain the notice in assets/LICENSE_DEJAVU.txt.\n"
    )
    files["NOTICES.txt"] = notices.encode("utf-8")
    metadata = {"schema": "private-mathematics-course/v1", "id": "NOE-IDL", "title": source_meta.get("title", "Ideal theory in rings"), "description": source_meta.get("description", ""), "language": "en", "distribution": "private", "public_release_clearance": False, "global_proof_closure": "not_claimed", "pending_programme_scope_record": "private-scope.json", "pending_programme_scope_sha256": sha_bytes(scope_bytes), "original_contributions_license": "CC0-1.0", "component_notices": "NOTICES.txt", "author": {"model": "gpt-6.1-sol", "reasoning_effort": "ultra", "platform": "Codex"}, "independent_review_claimed": False, "units": unit_rows, "private_prerequisite_snapshots": prerequisite_rows, "owned_lesson_paid_citation_scan": "passed_known_paid_patterns_and_free_url_policy", "pdf_generation": False, "tex_compilation": False}
    files["course.json"] = json_bytes(metadata)
    files["source-course/course.json"] = json_bytes({**metadata, "units": [{**row, "sha256": row["source_sha256"]} for row in unit_rows]})
    files["source-course/LICENSE"] = files["NOTICES.txt"]
    private_preq_units = []
    for row in prerequisite_rows:
        doc = selected[row["id"]]
        private_preq_units.append({"id": doc.uid, "title": doc.title, "source": doc.source, "sha256": sha_bytes(doc.data), "reader": PurePosixPath(doc.output).name, "reader_sha256": sha_bytes(files[doc.output]), "license": doc.declared_license or preq_meta.get("license"), "status": "private_snapshot", "public_release_clearance": False})
    files["prerequisites/AG-CA/course.json"] = json_bytes({"schema": "private-programme-snapshot/v1", "id": "AG-CA", "title": preq_meta.get("title"), "licence_rule": "Per-lesson terms; no blanket relicensing. Incorporated source expression retains its component notice.", "source_metadata_snapshot": "course-source-metadata.json", "source_metadata_sha256": sha_bytes(preq_meta_bytes), "distribution": "private", "public_release_clearance": False, "global_proof_closure": "not_claimed", "units": private_preq_units})
    # Explicit source archive: no private workspace, old downloads or unrelated courses.
    archive_names = sorted(name for name in files if name.startswith(("source-course/", "prerequisites/AG-CA/src/", "prerequisites/AG-CA/assets/", "runtime/mathjax/", "downloads/assets/")) or name in {"build_private_corrected_reader.py", "private-scope.json", "course.json", "NOTICES.txt", "prerequisites/AG-CA/course.json", "prerequisites/AG-CA/course-source-metadata.json", "prerequisites/AG-CA/CC0-1.0.txt", "prerequisites/AG-CA/COPYING-GFDL-1.2.txt"} or (name.startswith("downloads/") and name.endswith(".tex")))
    manifest = {name: {"bytes": len(files[name]), "sha256": sha_bytes(files[name])} for name in archive_names}
    archive_manifest = json_bytes({"schema": "explicit-private-course-source-manifest/v1", "entries": manifest, "public_release_clearance": False, "global_proof_closure": "not_claimed"})
    files["source-archive-manifest.json"] = archive_manifest
    with tempfile.TemporaryFile() as temporary:
        with zipfile.ZipFile(temporary, "w", zipfile.ZIP_DEFLATED) as archive:
            for name in archive_names:
                info = zipfile.ZipInfo(name, (1980, 1, 1, 0, 0, 0))
                info.compress_type = zipfile.ZIP_DEFLATED
                info.external_attr = 0o100644 << 16
                archive.writestr(info, files[name])
            archive.writestr("source-archive-manifest.json", archive_manifest)
        temporary.seek(0)
        files["downloads/ideal-theory-in-rings-source.zip"] = temporary.read()
    checked_links = validate_bundle(files)
    receipt = {"schema": "private-reader-build-receipt/v1", "lessons": 5, "historical_pages": 3, "private_prerequisite_pages": len(prerequisite_rows), "local_links_verified": checked_links, "source_bodies_preserved": True, "source_zip_sha256": sha_bytes(files["downloads/ideal-theory-in-rings-source.zip"]), "explicit_source_archive_entries": len(archive_names) + 1, "pandoc_diagnostics": PANDOC_DIAGNOSTICS, "canonical_inputs_edited": False, "shared_registry_or_readme_edited": False, "git_commands_used": False, "public_release_clearance": False, "global_proof_closure": "not_claimed", "pdf_generation": False, "tex_compilation": False}
    files["build-receipt.json"] = json_bytes(receipt)
    output = args.output.resolve()
    reader_target = args.repository.resolve() / "docs/courses/ideal-theory-in-rings"
    course_target = args.repository.resolve() / "courses/NOE-IDL"
    for destination in (output, reader_target, course_target):
        for original in (source, preq, runtime):
            if destination == original or destination.is_relative_to(original) or original.is_relative_to(destination):
                raise ValueError("An output destination would modify the canonical input tree.")
    publish_files(output, files)
    publish_files(reader_target, files)
    course_files = {name[len("source-course/"):]: data for name, data in files.items() if name.startswith("source-course/")}
    for name, data in files.items():
        if name.startswith(("downloads/", "prerequisites/", "runtime/")) or name in {"build_private_corrected_reader.py", "private-scope.json", "NOTICES.txt", "source-archive-manifest.json", "build-receipt.json"}:
            course_files[name] = data
    publish_files(course_target, course_files)
    print(json.dumps(receipt, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    try:
        main()
    except (ValueError, RuntimeError, OSError, KeyError, json.JSONDecodeError) as error:
        raise SystemExit(str(error)) from error
