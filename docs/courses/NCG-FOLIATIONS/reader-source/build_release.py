"""Build only the explicit public NCG course snapshot; never publish remotely.

The vendored renderer preserves TeX before CommonMark. This adapter changes
page chrome and exact public link destinations, not mathematical source text.
"""
from __future__ import annotations

import argparse
from datetime import datetime, timezone
import hashlib
import html
from html.parser import HTMLParser
import json
from pathlib import Path, PurePosixPath
import re
import shutil
import struct
import sys
import stat
from urllib.parse import unquote, urlsplit
import zipfile

HERE = Path(__file__).resolve().parent
sys.path[:0] = [str(HERE / "vendor"), str(HERE / "reader")]
from course_assets import read_unit_assets, asset_output_path, MAX_ASSETS
from course_reader import render_markdown_math, validate_course_links, ID
from markdown_it import MarkdownIt

ASSIGNMENT = "NCG-FOLIATIONS"
SLUGS = (
    "transverse-measures-of-foliations", "the-c-star-algebra-of-a-foliation",
    "hilbert-modules-and-fields-on-the-leaf-space",
    "the-index-theorem-for-measured-foliations", "k-theory-of-the-leaf-space",
)
PUBLIC_NOTICES = ("LICENSE", "README.md", "STATUS.md", "SOURCE-LICENSES.md")
REPRODUCTION_PATTERN = r"(?:(?:figures|reproduction)/[a-z0-9_-]+\.py|reproduction/graph-dirac/draw_graph_dirac\.py|reproduction/countable\-tree/check_formulas\.py|reproduction/countable\-tree/draw_countable_tree\.py|reproduction/countable\-tree/draw_proper_tree\.py|reproduction/negative\-output\-packing/draw_negative_output\.py|reproduction/negative\-output\-boundary/draw_negative_output_boundary\.py)"
SUPPORTING_SOURCE_PATHS = {
    "reproduction/negative-output-boundary/COMPONENT-TERMS.md",
    "reproduction/negative-output-boundary/FONT-NOTICE.txt",
    "reproduction/negative-output-boundary/MATPLOTLIB-LICENSE.txt",
    "reproduction/negative-output-boundary/NUMPY-LICENSE.txt",
    "reproduction/negative-output-boundary/PILLOW-LICENSE.txt",
    "reproduction/negative-output-boundary/README.md",
    "reproduction/negative-output-boundary/figure-and-bounds.json",
    "reproduction/negative-output-boundary/fonts/DejaVuSans-Bold.ttf",
    "reproduction/negative-output-boundary/fonts/DejaVuSans-Oblique.ttf",
    "reproduction/negative-output-boundary/fonts/DejaVuSans.ttf",
    "reproduction/negative-output-boundary/fonts/DejaVuSansDisplay.ttf",
    "reproduction/negative-output-boundary/fonts/DejaVuSansMono.ttf",
    "reproduction/negative-output-boundary/fonts/LICENSE_DEJAVU.txt",
    "reproduction/negative-output-boundary/fonts/LICENSE_STIX.txt",
    "reproduction/negative-output-boundary/fonts/STIXGeneral.ttf",
    "reproduction/negative-output-boundary/fonts/STIXGeneralItalic.ttf",
    "reproduction/negative-output-boundary/fonts/STIXNonUniIta.ttf",
    "reproduction/negative-output-boundary/fonts/STIXSizFiveSymReg.ttf",
    "reproduction/negative-output-boundary/fonts/STIXSizFourSymReg.ttf",
    "reproduction/negative-output-boundary/fonts/STIXSizOneSymReg.ttf",
    "reproduction/negative-output-boundary/fonts/STIXSizThreeSymReg.ttf",
    "reproduction/negative-output-boundary/fonts/STIXSizTwoSymReg.ttf",
    "reproduction/negative-output-boundary/requirements.txt",
    "reproduction/countable-tree/COMPONENT-TERMS.md",
    "reproduction/countable-tree/COUNTABLE-FIGURE-BOUNDS.json",
    "reproduction/countable-tree/FIGURE-BOUNDS.json",
    "reproduction/countable-tree/FORMULA-CHECKS.json",
    "reproduction/countable-tree/MATPLOTLIB-LICENSE.txt",
    "reproduction/countable-tree/NUMPY-LICENSE.txt",
    "reproduction/countable-tree/PILLOW-LICENSE.txt",
    "reproduction/countable-tree/README.md",
    "reproduction/countable-tree/fonts/DejaVuSans-Bold.ttf",
    "reproduction/countable-tree/fonts/DejaVuSans-Oblique.ttf",
    "reproduction/countable-tree/fonts/DejaVuSans.ttf",
    "reproduction/countable-tree/fonts/DejaVuSansDisplay.ttf",
    "reproduction/countable-tree/fonts/DejaVuSansMono.ttf",
    "reproduction/countable-tree/fonts/LICENSE_DEJAVU.txt",
    "reproduction/countable-tree/fonts/LICENSE_STIX.txt",
    "reproduction/countable-tree/fonts/STIXGeneral.ttf",
    "reproduction/countable-tree/fonts/STIXGeneralItalic.ttf",
    "reproduction/countable-tree/fonts/STIXNonUniIta.ttf",
    "reproduction/countable-tree/fonts/STIXSizFiveSymReg.ttf",
    "reproduction/countable-tree/fonts/STIXSizFourSymReg.ttf",
    "reproduction/countable-tree/fonts/STIXSizOneSymReg.ttf",
    "reproduction/countable-tree/fonts/STIXSizThreeSymReg.ttf",
    "reproduction/countable-tree/fonts/STIXSizTwoSymReg.ttf",
    "reproduction/countable-tree/requirements.txt",
    "reproduction/negative-output-packing/COMPONENT-TERMS.md",
    "reproduction/negative-output-packing/FONT-NOTICE.txt",
    "reproduction/negative-output-packing/MATPLOTLIB-LICENSE.txt",
    "reproduction/negative-output-packing/NUMPY-LICENSE.txt",
    "reproduction/negative-output-packing/PILLOW-LICENSE.txt",
    "reproduction/negative-output-packing/README.md",
    "reproduction/negative-output-packing/figure-and-bounds.json",
    "reproduction/negative-output-packing/fonts/DejaVuSans-Bold.ttf",
    "reproduction/negative-output-packing/fonts/DejaVuSans-Oblique.ttf",
    "reproduction/negative-output-packing/fonts/DejaVuSans.ttf",
    "reproduction/negative-output-packing/fonts/DejaVuSansDisplay.ttf",
    "reproduction/negative-output-packing/fonts/STIXGeneral.ttf",
    "reproduction/negative-output-packing/fonts/STIXNonUniIta.ttf",
    "reproduction/negative-output-packing/fonts/STIXSizFiveSymReg.ttf",
    "reproduction/negative-output-packing/fonts/STIXSizFourSymReg.ttf",
    "reproduction/negative-output-packing/fonts/STIXSizOneSymReg.ttf",
    "reproduction/negative-output-packing/fonts/STIXSizThreeSymReg.ttf",
    "reproduction/negative-output-packing/fonts/STIXSizTwoSymReg.ttf",
    "reproduction/negative-output-packing/requirements.txt",
    "reproduction/graph-dirac/COMPONENT-TERMS.md",
    "reproduction/graph-dirac/MATPLOTLIB-LICENSE.txt",
    "reproduction/graph-dirac/NUMPY-LICENSE.txt",
    "reproduction/graph-dirac/README.md",
    "reproduction/graph-dirac/arithmetic-and-figure.json",
    "reproduction/graph-dirac/fonts/DejaVuSans-Bold.ttf",
    "reproduction/graph-dirac/fonts/DejaVuSans-Oblique.ttf",
    "reproduction/graph-dirac/fonts/DejaVuSans.ttf",
    "reproduction/graph-dirac/fonts/DejaVuSansDisplay.ttf",
    "reproduction/graph-dirac/fonts/LICENSE_DEJAVU.txt",
    "reproduction/graph-dirac/fonts/LICENSE_STIX.txt",
    "reproduction/graph-dirac/fonts/STIXGeneralItalic.ttf",
    "reproduction/graph-dirac/requirements.txt",
    "reproduction/README.md",
    "reproduction/plaque-dirichlet-README.md",
    "reproduction/FONT-NOTICE.txt",
    "reproduction/fonts/DejaVuSans-Bold.ttf",
    "reproduction/fonts/DejaVuSans-Oblique.ttf",
    "reproduction/fonts/DejaVuSans.ttf",
    "reproduction/fonts/DejaVuSansCondensed-Bold.ttf",
    "reproduction/fonts/DejaVuSansCondensed.ttf",
    "reproduction/fonts/LICENSE_DEJAVU.txt",
}
DOWNLOAD_NAME = "ncg-foliations-reader-and-sources.zip"
OLD_READER = "https://kokunoyumeto.github.io/open-mathematics-courses/courses/"
OLD_FIGURES = "https://raw.githubusercontent.com/KokunoYumeto/open-mathematics-courses/main/courses/NCG-FOLIATIONS/figures/"
COURSE_FIGURE_PREFIXES = (OLD_FIGURES,
    "https://raw.githubusercontent.com/KokunoYumeto/open-math-courses/main/docs/courses/NCG-FOLIATIONS/figures/",
    "https://raw.githubusercontent.com/KokunoYumeto/open-math-courses/main/courses/NCG-FOLIATIONS/figures/",
    "https://kokunoyumeto.github.io/open-math-courses/courses/NCG-FOLIATIONS/figures/",
)
REPOSITORY = "https://github.com/KokunoYumeto/open-math-courses"
STYLE = """body{margin:0;background:#f6f8fc;color:#23324b;font:18px/1.7 Georgia,serif;overflow-wrap:anywhere}main{max-width:1040px;margin:28px auto;padding:35px 52px;background:white;border:1px solid #d6deeb;border-radius:10px;min-width:0}h1,h2,h3,nav,.draft{font-family:Arial,sans-serif;line-height:1.25}h1{font-size:36px}h2{font-size:28px;margin-top:2.4em}a{color:#175c96;overflow-wrap:anywhere}nav{font-size:16px;margin-bottom:22px}nav a{display:inline-block;margin:0 .8em .4em 0}.draft{background:#fff3ce;padding:12px 16px;font-size:15px;border-left:4px solid #c78b00}.math-display{display:block;overflow-x:auto;text-align:center;margin:20px 0}mjx-container[display=true]{margin:12px 0!important}.course-figure{display:block;margin:24px auto}li{margin:8px 0}code{font-family:monospace;overflow-wrap:anywhere}footer{margin-top:32px;font-size:14px;color:#5d6d82}table{border-collapse:collapse;width:100%}td,th{padding:8px;border-bottom:1px solid #d6deeb;text-align:left}details{margin:1em 0}summary{cursor:pointer}@media(max-width:800px){main{margin:0;padding:22px 18px;border-radius:0}body{font-size:17px}h1{font-size:29px}h2{font-size:24px}.math:not(.math-display){display:inline-block;max-width:100%;overflow-x:auto;vertical-align:middle}}"""
MATH_CONFIG = r"""window.MathJax={tex:{inlineMath:[['\\(','\\)']],displayMath:[['\\[','\\]']],processEscapes:true},svg:{fontCache:'local'},options:{ignoreHtmlClass:'no-math',processHtmlClass:'math'},startup:{ready:()=>{MathJax.startup.defaultReady();MathJax.startup.promise.then(()=>{if(location.hash){try{const target=document.getElementById(decodeURIComponent(location.hash.slice(1)));if(target)target.scrollIntoView();}catch{}}document.documentElement.dataset.mathReady='true';});}}};"""
STYLE += "\npre{max-width:100%;overflow-x:auto}"
MATHTOOLS_CONFIG = MATH_CONFIG.replace("window.MathJax={tex:{", "window.MathJax={loader:{load:['[tex]/mathtools'],paths:{tex:new URL('../mathjax/input/tex/extensions',document.currentScript.src).href}},tex:{packages:{'[+]':['mathtools']},", 1)
BANNER = '<p class="draft">This course is an incomplete draft. <a href="status.html">Proved scope and remaining questions</a>.</p>'


def sha(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest().upper()


def write_json(path: Path, value) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(value, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def copy_exact(source: Path, destination: Path, expected=None) -> dict:
    if source.is_symlink() or not source.is_file():
        raise ValueError("source must be a regular file: " + source.name)
    data = source.read_bytes()
    digest = sha(data)
    if expected and digest != expected:
        raise ValueError("source hash mismatch: " + source.name)
    destination.parent.mkdir(parents=True, exist_ok=True)
    destination.write_bytes(data)
    return {"sha256": digest, "bytes": len(data)}


def safe_relative(value: str) -> Path:
    if not isinstance(value,str) or not value:
        raise ValueError("noncanonical public allowlist path")
    p = PurePosixPath(value)
    if not p.parts or p.is_absolute() or p.as_posix()!=value or ".." in p.parts or "\\" in value or ":" in value:
        raise ValueError("noncanonical public allowlist path")
    return Path(*p.parts)


def page(title, body, *, math=False, depth="", footer=None, mathtools=False):
    config_name = "mathjax-mathtools-config.js" if mathtools else "mathjax-config.js"
    scripts = ('<script src="' + depth + 'assets/reader/' + config_name + '"></script><script defer src="' + depth + 'assets/mathjax/tex-svg.js"></script>') if math else ""
    if footer is None:
        footer = 'Original lessons and drawings: <a href="' + depth + 'LICENSE">CC0 1.0</a>. K-theory Lemma 7.7 adaptation: CC BY 4.0. <a href="' + depth + 'sources.html">Sources, attribution and component terms</a>. MathJax: Apache License 2.0. This is an incomplete draft.'
    return '<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>' + html.escape(title) + '</title><link rel="stylesheet" href="' + depth + 'assets/reader/reader.css">' + scripts + '</head><body><main>' + body + '<footer>' + footer + '</footer></main></body></html>\n'


def heading_aliases(text, rows, explicit=None):
    """Retain stable sections and exact provider heading aliases."""
    lines = text.splitlines()
    explicit_ids = {value.lower() for row in explicit or [] for value in row["ids"]}
    bindings = {}
    for row in rows:
        ids = [value for value in row["ids"] if value.lower() not in explicit_ids]
        if ids:
            bindings[row["line"]] = ids
    for row in explicit or []:
        bindings.setdefault(row["line"], []).extend(row["ids"])
    result, used = [], set()
    for line, ids in sorted(bindings.items()):
        if not 1 <= line <= len(lines) or not re.match(r"^#{1,6}\s+", lines[line - 1]):
            raise ValueError("heading alias must bind an actual source heading")
        heading = re.sub(r"^#{1,6}\s+", "", lines[line - 1])
        native = re.sub(r"[^\w-]+", "-", heading.lower()).strip("-")
        if ID.fullmatch(native):
            ids.append(native)
        by_case = {}
        for value in ids:
            if not ID.fullmatch(value):
                if re.fullmatch(r"[\w][\w.-]*", value):
                    continue  # retain this safe historical HTML alias below
                raise ValueError("invalid explicit heading alias")
            key = value.lower()
            if key not in used and (key not in by_case or value != key):
                by_case[key] = value
        if by_case:
            result.append({"line":line, "ids":list(by_case.values())})
            used.update(by_case)
    return result


def outside_import_links(rendered, outside):
    """Keep ancillary bibliographic text without a misleading dead proof link."""
    changes = []
    def replace(match):
        original = html.unescape(match[1])
        base = original.split("#", 1)[0]
        if not (base in outside or base.startswith("outside-import/")):
            return match[0]
        label = match[2]
        changes.append({"original_reference":outside.get(base,original), "action":"Unavailable ancillary hyperlink rendered as a plain title outside this import"})
        return '<span class="outside-import">' + label + ' <small>(further reading outside this import)</small></span>'
    return re.sub(r'<a href="([^"]*)">(.*?)</a>', replace, rendered, flags=re.S), changes


def build_companions(dest, core_units):
    folder = HERE / "companion-inputs"
    if not (folder / "manifest.json").exists():
        return {}, None
    manifest = json.loads((folder / "manifest.json").read_text(encoding="utf-8"))
    target = dest / "companions"
    target.mkdir(parents=True, exist_ok=True)
    aliases, root_rewrites = {}, {}
    entries = manifest["proof_files"]
    for row in entries:
        stem = Path(row["frozen_file"]).stem
        name = row["id"] + ".html"
        aliases[stem + ".md"] = name
        aliases[row["id"] + ".md"] = name
        for original in row.get("replaces_retired_urls", []):
            root_rewrites[original] = "companions/" + name
    aliases["effros-borel-structure.md"] = "the-effros-borel-structure.html"
    aliases["polish-spaces-and-standard-borel-spaces-the-full-appendix-of-vol-i.md"] = "polish-spaces-and-standard-borel-spaces.html"
    aliases.update(manifest.get("local_link_aliases", {}))
    malformed = OLD_READER + "the topological K-theory lesson,/topological-k-theory-of-spaces-pairs-and-vector-bundles.html"
    root_rewrites[malformed] = "companions/KT-OPK-12.html"
    root_rewrites[malformed.replace(" ", "%20")] = "companions/KT-OPK-12.html"
    companion_rewrites = {key:value.removeprefix("companions/") for key,value in root_rewrites.items()}
    for slug, unit in core_units.items():
        base = "https://github.com/KokunoYumeto/open-mathematics-courses/blob/main/courses/NCG-FOLIATIONS/src/" + slug + ".md"
        companion_rewrites[base] = "../" + slug + ".html"
        if slug == "hilbert-modules-and-fields-on-the-leaf-space":
            companion_rewrites[base + "#6-sobolev-modules-and-the-analytic-symbol-class"] = "../" + slug + ".html#section-6"
    companion_rewrites.update(manifest.get("projection_rewrites", {}))
    ancillary_records, source_records, parsed_math = [], {}, {}
    png_assets = {}
    published_file_routes = {row["frozen_file"]:row["suggested_path"] for row in manifest["notice_files"]}
    published_file_routes.update({row["frozen_file"]:row["suggested_companion_path"] for row in manifest.get("figure_assets", [])})
    figure_sources = {Path(row["frozen_file"]).name:row for row in entries}
    for row in manifest.get("figure_assets", []):
        frozen = folder / safe_relative(row["frozen_file"])
        published = row["suggested_companion_path"]
        source_records[published] = copy_exact(frozen,target / safe_relative(published),row["sha256"])
        copy_exact(frozen,target / "src" / safe_relative(published),row["sha256"])
        if published.endswith((".png",".svg")):
            alias = "figures/" + Path(row["frozen_file"]).name
            if alias != published:
                source_records[alias] = copy_exact(frozen,target / safe_relative(alias),row["sha256"])
        if published.endswith(".png"):
            width,height = struct.unpack(">II",frozen.read_bytes()[16:24])
            provider = figure_sources[row["bound_source"]]
            asset = {"id":Path(published).stem,"path":row.get("markdown_path",published),"source":row["frozen_file"],"source_sha256":row["sha256"],"media_type":"image/png","bytes":row["bytes"],"width":width,"height":height,"authorship":{"kind":"original","credit":"Original illustration for "+provider["source_title"],"statement":row.get("rights_evidence","Original illustration dedicated to CC0-1.0; component terms retained.")},"source_attribution":[provider["source_title"]]}
            png_assets.setdefault(row["bound_source"], []).append(asset)
    for row in manifest["notice_files"]:
        name = row["suggested_path"]
        source_records[name] = copy_exact(folder / safe_relative(row["frozen_file"]),target / safe_relative(name),row["sha256"])
    for row in entries:
        frozen = folder / safe_relative(row["frozen_file"])
        text = frozen.read_text(encoding="utf-8")
        source_name = Path(row["frozen_file"]).name
        source_records["src/"+source_name] = copy_exact(frozen,target / "src" / source_name,row["sha256"])
        anchors = [{"line":r["line"],"ids":[r["stable_section_anchor"]]} for r in row["heading_anchor_map"] if r["stable_section_anchor"]]
        if row["id"] == "the-effros-borel-structure":
            for anchor in anchors:
                number = int(anchor["ids"][0].split("-")[-1])
                if number <= 10:
                    anchor["ids"].append("oa-fnd-ef-"+str(number).zfill(2))
        native_prefix = {"af-algebras":"oa-fnd-af-", "c-star-algebras-continuous-functional-calculus-automatic-continuity-positive-cones":"oa-fnd-cf-"}.get(row["id"])
        if native_prefix:
            for anchor in anchors:
                number = int(anchor["ids"][0].split("-")[-1])
                anchor["ids"].append(native_prefix+str(number).zfill(2))
        if row["id"] == "polish-spaces-and-standard-borel-spaces":
            # Native provider IDs refer to source subdivisions, not simply
            # the numbered sections. These exact heading lines retain them.
            native_lines = {1:59,2:88,3:121,4:151,5:173,6:277,7:326,8:348,9:396,10:465,11:536,12:49}
            for number,line in native_lines.items():
                existing = next((anchor for anchor in anchors if anchor["line"] == line),None)
                if existing is None:
                    anchors.append({"line":line,"ids":["oa-fnd-pb-"+str(number).zfill(2)]})
                else:
                    existing["ids"].append("oa-fnd-pb-"+str(number).zfill(2))
        local = dict(aliases)
        outside = {}
        for reference in re.findall(r"(?<!!)\]\(([^)]*)\)",text):
            base = reference.split("#",1)[0]
            if base and not urlsplit(base).scheme and base not in local:
                try:
                    declared_source = (frozen.parent / unquote(base)).resolve().relative_to(folder.resolve()).as_posix()
                except ValueError:
                    declared_source = None
                if declared_source in published_file_routes:
                    local[base] = published_file_routes[declared_source]
                elif re.search(r"\.(md|html)$",base):
                    marker = "outside-import/" + sha(base.encode())[:16]
                    local[base] = marker
                    outside[marker] = reference
        unit_assets = png_assets.get(source_name,[])
        unit = {"id":row["id"],"source":row["frozen_file"],"assets":unit_assets}
        assets = read_unit_assets(folder,"ncg-proof-companions",unit)
        heading_bindings = heading_aliases(text,anchors,row.get("heading_anchor_aliases"))
        rendered = render_markdown_math(text,local_links=local,heading_anchors=heading_bindings,assets=assets)
        # Preserve exact safe historical HTML aliases outside authored-ID limits.
        for binding in row.get("heading_anchor_aliases", []):
            extra = [a for a in binding["ids"] if not ID.fullmatch(a) and re.fullmatch(r"[\w][\w.-]*", a)]
            anchor = next((a for a in heading_bindings if a["line"] == binding["line"]), None)
            if extra and anchor:
                aliases_html = "".join('<span id="' + html.escape(a,quote=True) + '"></span>' for a in extra)
                rendered = re.sub(r'(<h[1-6] id="' + re.escape(anchor["ids"][0]) + r'">)',lambda m:m[1]+aliases_html,rendered,count=1)
        for reference in IndexFromHTML(rendered).references:
            base = reference.split("#",1)[0]
            if (base.startswith(OLD_READER) or base.startswith("https://github.com/KokunoYumeto/open-mathematics-courses/")) and base not in companion_rewrites:
                outside[base] = reference
        rendered, link_changes = rebind_html(rendered,assets,companion_rewrites)
        rendered, ancillary = outside_import_links(rendered,outside)
        ancillary_records.extend({"provider":row["id"],**item} for item in ancillary)
        proof_loci = html.escape("; ".join(row["proof_locators"]))
        nav = '<nav><a href="../index.html">Course contents</a><a href="index.html">Companion readings</a><a href="src/' + source_name + '" download>Markdown source</a></nav>'
        note = ""
        licence = html.escape(row["licence"])
        rights = ""
        if row["licence"] == "GFDL-1.2-only":
            rights += '<p>GNU Free Documentation License, Version 1.2 only; no Invariant Sections or Cover Texts. Retain <a href="AN-03/RIGHTS.md">rights notice</a>, <a href="AN-03/TITLE_PAGE.md">original title page</a>, <a href="AN-03/HISTORY.md">original history</a>, <a href="AN-03/COPYING">complete licence</a>, and <a href="AN-03/HTML-PROJECTION.md">this projection notice</a>.</p>'
        footer = licence + '. Source credits and component terms are retained. <a href="index.html">Companion readings and terms</a>.'
        if row.get("additional_projection_credit"):
            footer += " " + html.escape(row["additional_projection_credit"])
        (target / (row["id"]+".html")).write_text(page(row["source_title"],nav+note+rights+rendered,math=True,depth="../",footer=footer,mathtools=r"\begin{psmallmatrix}" in text),encoding="utf-8")
        parsed = IndexFromHTML(rendered)
        parsed_math[row["id"]] = {"formulas":len(parsed.math),"math_tex_sha256":sha(json.dumps(parsed.math,ensure_ascii=False).encode()),"source_sha256":row["sha256"],"heading_bindings":heading_bindings}
    if any(row["licence"] == "GFDL-1.2-only" for row in entries):
        (target / "AN-03/HTML-PROJECTION.md").write_text("# Spectral calculus — NCG supporting source projection\n\nThis is an HTML presentation of the exact admitted spectral-calculus source snapshot identified in the companion manifest. The source Markdown bytes are unchanged. Original AN-03 title, history, rights and complete GFDL 1.2 notices accompany this component. The HTML projection changes navigation, adds hash-bound source and notice downloads, supplies stable section anchors, and labels unavailable ancillary hyperlinks as readings outside this course import.\n\nProjection contributor: GPT-6.1 Sol (OpenAI), Ultra, October 2026. Publisher entity: Open Mathematics Courses collection. This projection retains GNU Free Documentation License, Version 1.2 only, with no Invariant Sections, no Front-Cover Texts and no Back-Cover Texts. New presentation code is CC0 to the extent rights exist; it does not relicense the inherited GFDL work.\n",encoding="utf-8")
    rows = []
    for row in entries:
        title = render_markdown_math(row["source_title"]).removeprefix("<p>").removesuffix("</p>\n")
        rows.append('<li><a href="'+row["id"]+'.html">'+title+'</a> · <a href="src/'+Path(row["frozen_file"]).name+'" download>Markdown source</a><br>'+html.escape(row["licence"])+'</li>')
    body = '<nav><a href="../index.html">Course contents</a><a href="../sources.html">Sources and terms</a></nav><h1>Companion readings</h1><p>These lessons provide the algebra, topology, analysis and measure theory used in the foliation course. Each reading retains its own source credits and licence.</p><ol>'+''.join(rows)+'</ol><p>Applicable component notices are linked from the readings that use them.</p>'
    (target / "index.html").write_text(page("Companion readings",body,math=True,depth="../",footer="Consult each reading for its references, attribution and component terms."),encoding="utf-8")
    public_manifest = {**manifest,"published_source_files":source_records,"rendered_math":parsed_math,"ancillary_link_presentation":ancillary_records,"projection_authorship":{"model":"GPT-6.1 Sol (OpenAI)","reasoning_effort":"Ultra","scope":"Portable HTML projection and link adaptations only; no independent proof review"}}
    write_json(target / "manifest.json",public_manifest)
    return root_rewrites, public_manifest


def IndexFromHTML(rendered):
    index = Index()
    index.feed(rendered)
    return index


def rebind_html(rendered: str, assets, rewrites: dict[str, str]) -> tuple[str, list[dict]]:
    applied = []
    for row in assets.records:
        original = asset_output_path(assets.course_id, assets.unit_id, row).split("/", 2)[2]
        destination = "figures/" + Path(row["source"]).name
        pattern = r'(<img src=")' + re.escape(original) + r'("[^>]*data-asset-id="' + re.escape(row["id"]) + r'"[^>]*>)'
        rendered, count = re.subn(pattern, lambda m: m[1] + destination + m[2], rendered)
        if count != 1:
            raise ValueError("expected exactly one rendered bound figure: " + row["id"])
    def rewrite(match):
        original = html.unescape(match[1])
        parts = urlsplit(original)
        base = original.split("#", 1)[0]
        destination = rewrites.get(original)
        if destination is None and base in rewrites:
            destination = rewrites[base] + ("#" + parts.fragment if parts.fragment else "")
        figure_prefix = next((prefix for prefix in COURSE_FIGURE_PREFIXES if original.startswith(prefix)),None)
        if destination is None and figure_prefix:
            filename = unquote(original[len(figure_prefix):])
            if "/" in filename or not re.fullmatch(r"[a-z0-9_-]+\.(png|svg|py)", filename):
                raise ValueError("unrecognized original figure download")
            destination = "figures/" + filename
        if destination is None:
            return match[0]
        applied.append({"original": original, "reader_destination": destination})
        return 'href="' + html.escape(destination, quote=True) + '"'
    rendered = re.sub(r'href="([^"]*)"', rewrite, rendered)
    for row in assets.records:
        routes = [("figures/"+row["id"]+".png","Full-size PNG"),("figures/"+row["id"]+".svg","Editable SVG")]
        missing = [(href,label) for href,label in routes if 'href="'+href+'"' not in rendered]
        if missing:
            links = '<p class="figure-downloads">' + ' · '.join('<a href="'+href+'" download>'+label+'</a>' for href,label in missing) + '</p>'
            pattern = r'(<img [^>]*data-asset-id="' + re.escape(row["id"]) + r'"[^>]*>)'
            rendered,count = re.subn(pattern,lambda match:match[1]+links,rendered)
            if count != 1:
                raise ValueError("missing exact bound image for source download links")
            applied.append({"kind":"Accessible download routes added for an already bound figure","figure_id":row["id"],"links":[href for href,_ in missing]})
    return rendered, applied


class Index(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.ids, self.references, self.math = set(), [], []

    def handle_starttag(self, tag, attrs):
        row = dict(attrs)
        if "id" in row:
            if row["id"] in self.ids:
                raise ValueError("duplicate public HTML anchor")
            self.ids.add(row["id"])
        if "data-tex" in row:
            self.math.append(row["data-tex"])
        for name in ("href", "src"):
            if name in row:
                self.references.append(row[name])


def validate_site(docs: Path, course: Path) -> dict:
    indices = {}
    for source in course.rglob("*.html"):
        index = Index()
        index.feed(source.read_text(encoding="utf-8"))
        indices[source.resolve()] = index
    external, unresolved = set(), set()
    for source, index in indices.items():
        for reference in index.references:
            parsed = urlsplit(reference)
            if parsed.scheme in {"https", "http", "mailto"}:
                external.add(reference)
                if reference.startswith(OLD_READER):
                    unresolved.add(reference)
                continue
            if parsed.scheme or parsed.netloc:
                raise ValueError("unsupported public URL scheme")
            target = (source.parent / unquote(parsed.path)).resolve() if parsed.path else source
            if not target.is_relative_to(docs.resolve()):
                raise ValueError("reader link escapes docs root")
            # The library landing page is integrated by the release owner.
            if target == docs.resolve() / "index.html":
                continue
            if not target.is_file():
                raise ValueError("missing public link target: " + reference)
            if parsed.fragment and target in indices and unquote(parsed.fragment) not in indices[target].ids:
                raise ValueError("missing public link anchor: " + reference)
    return {"local_links_and_anchors": "passed", "external_urls": sorted(external), "unresolved_retired_programme_urls": sorted(unresolved)}


def build(args):
    source = args.source.resolve()
    output = args.output.resolve()
    if source == output or source.is_relative_to(output) or output.is_relative_to(source):
        raise ValueError("build output must be separate from the public source")
    # Validate the authoritative snapshot before replacing the last staging
    # build. A course owner may be updating figures and metadata together.
    metadata = json.loads((source / "course.json").read_text(encoding="utf-8"))
    figures = json.loads((source / "figures/figures.json").read_text(encoding="utf-8"))
    for row in metadata["units"]:
        if sha((source / safe_relative(row["source"])).read_bytes()) != row["sha256"]:
            raise ValueError("source update is not yet hash-bound: " + row["id"])
    for row in figures["figures"]:
        if sha((source / safe_relative(row["source"])).read_bytes()) != row["source_sha256"]:
            raise ValueError("figure update is not yet hash-bound: " + row["id"])
    editable=figures["editable_sources"]
    if (not isinstance(editable,list) or any(not isinstance(name,str) or not re.fullmatch(r"[a-z0-9_-]+\.svg",name) for name in editable)
            or len(set(editable))!=len(editable)):
        raise ValueError("noncanonical or duplicate editable figure source")
    expected_linked={"figures/"+name for name in editable}
    reproduction={}
    for row in figures.get("reproduction_sources",[]):
        name=row["source"]
        if not re.fullmatch(REPRODUCTION_PATTERN,name) or name in reproduction:
            raise ValueError("noncanonical or duplicate figure reproduction source")
        if "bytes" in row and (type(row["bytes"]) is not int or row["bytes"]<0):
            raise ValueError("invalid reproduction-source size")
        reproduction[name]=row
        expected_linked.add(name)
    supporting={}
    for row in figures.get("supporting_sources",[]):
        name=row["source"]
        if name not in SUPPORTING_SOURCE_PATHS or name in supporting or name in expected_linked:
            raise ValueError("noncanonical or duplicate figure supporting source")
        supporting[name]=row
        expected_linked.add(name)
    declared=metadata.get("linked_files")
    if not isinstance(declared,list):
        raise ValueError("linked figure sources need explicit hash bindings")
    linked={}
    for row in declared:
        if not isinstance(row,dict) or set(row)!={"href","sha256","bytes"}:
            raise ValueError("invalid linked-file integrity record")
        name=row["href"];relative=safe_relative(name)
        if (not re.fullmatch(r"figures/[a-z0-9_-]+\.svg",name)
                and not re.fullmatch(REPRODUCTION_PATTERN,name)
                and name not in SUPPORTING_SOURCE_PATHS) or name in linked:
            raise ValueError("noncanonical or duplicate linked figure source")
        if not isinstance(row["sha256"],str) or not re.fullmatch(r"[0-9A-F]{64}",row["sha256"]) or type(row["bytes"]) is not int or row["bytes"]<0:
            raise ValueError("invalid linked figure hash or size")
        path=source/relative
        if not path.resolve().is_relative_to(source) or path.is_symlink() or not path.is_file():
            raise ValueError("linked figure source must be an in-root regular file")
        for part in [path,*path.parents]:
            if part==source.parent:
                break
            if (part.is_symlink() or getattr(part.lstat(),"st_reparse_tag",0)
                    ==getattr(stat,"IO_REPARSE_TAG_MOUNT_POINT",0xA0000003)):
                raise ValueError("linked figure source has a symlink or junction component")
        data=path.read_bytes()
        if sha(data)!=row["sha256"] or len(data)!=row["bytes"]:
            raise ValueError("linked figure source hash or size mismatch: "+name)
        if name in reproduction and (reproduction[name]["sha256"]!=row["sha256"]
                or ("bytes" in reproduction[name] and reproduction[name]["bytes"]!=row["bytes"])):
            raise ValueError("reproduction-source and linked-file integrity differs")
        if name in supporting and (type(supporting[name].get("bytes")) is not int or supporting[name]["bytes"]<0):
            raise ValueError("invalid supporting-source size")
        if name in supporting and (supporting[name]["sha256"]!=row["sha256"]
                or supporting[name]["bytes"]!=row["bytes"]):
            raise ValueError("supporting-source and linked-file integrity differs")
        linked[name]=row
    if set(linked)!=expected_linked:
        raise ValueError("declared linked files must equal the exact editable figure and reproduction sources")
    output.mkdir(parents=True, exist_ok=True)
    # Clean only files recorded in this adapter's previous manifest.
    prior = output / "build-manifest.json"
    if prior.exists():
        for relative in json.loads(prior.read_text(encoding="utf-8"))["staged_files"]:
            candidate = output / safe_relative(relative)
            if candidate.exists():
                candidate.unlink()
    docs = output / "docs"
    dest = docs / "courses" / ASSIGNMENT
    dest.mkdir(parents=True, exist_ok=True)
    if metadata["status"] != "draft-incomplete" or [u["id"] for u in metadata["units"]] != list(SLUGS):
        raise ValueError("expected the five-unit incomplete public course snapshot")
    bindings = {u["id"]: u for u in metadata["units"]}
    if any(len(u["assets"]) > MAX_ASSETS for u in metadata["units"]):
        raise ValueError("declared lesson assets exceed the owned renderer capacity")
    figure_count = len(figures["figures"])
    k_theory_images = len(bindings[SLUGS[-1]]["assets"])
    companion_rewrites, companion_manifest = build_companions(dest,bindings)
    sources = {}
    source_files = {}
    for name in ("course.json", *PUBLIC_NOTICES, "figures/figures.json"):
        source_files[name] = copy_exact(source / safe_relative(name), dest / safe_relative(name))
    pngs = {row["source"]: row for row in figures["figures"]}
    bound_assets = [a for u in metadata["units"] for a in u["assets"]]
    if (len(pngs) != figure_count or len(bound_assets) != figure_count
            or {a["source"] for a in bound_assets} != set(pngs)
            or set(figures["editable_sources"]) != {Path(a["source"]).stem + ".svg" for a in bound_assets}):
        raise ValueError("every declared PNG/SVG pair must have exactly one lesson binding")
    for name, row in pngs.items():
        source_files[name] = copy_exact(source / safe_relative(name), dest / safe_relative(name), row["source_sha256"])
    for name in figures["editable_sources"]:
        relative = "figures/" + name
        source_files[relative] = copy_exact(source / safe_relative(relative), dest / safe_relative(relative), linked[relative]["sha256"])
    for row in figures.get("reproduction_sources", []):
        relative = row["source"]
        if not re.fullmatch(REPRODUCTION_PATTERN,relative):
            raise ValueError("noncanonical figure reproduction source")
        source_files[relative] = copy_exact(source / safe_relative(relative), dest / safe_relative(relative), row["sha256"])
    for row in figures.get("supporting_sources", []):
        relative = row["source"]
        if relative not in SUPPORTING_SOURCE_PATHS:
            raise ValueError("noncanonical figure supporting source")
        source_files[relative] = copy_exact(source / safe_relative(relative), dest / safe_relative(relative), row["sha256"])
    supplemental_metadata = "figures/supplementary-assets.json"
    if (source / supplemental_metadata).exists():
        source_files[supplemental_metadata] = copy_exact(source / supplemental_metadata, dest / supplemental_metadata)
    rewrites = companion_rewrites
    if args.link_rewrites:
        rewrites.update(json.loads(args.link_rewrites.read_text(encoding="utf-8")))
    applied = []
    local_links = {slug + ".md": slug + ".html" for slug in SLUGS}
    linked_files = metadata["linked_files"]
    local_links.update({"../"+row["href"]:row["href"] for row in linked_files})
    units = []
    for slug in SLUGS:
        unit = bindings[slug]
        relative = unit["source"]
        source_files[relative] = copy_exact(source / safe_relative(relative), dest / safe_relative(relative), unit["sha256"])
        text = (dest / relative).read_text(encoding="utf-8")
        malformed = OLD_READER + "the topological K-theory lesson,/topological-k-theory-of-spaces-pairs-and-vector-bundles.html"
        if malformed in text:
            corrected = OLD_READER + "KT-OPK/topological-k-theory-of-spaces-pairs-and-vector-bundles.html"
            text = text.replace(malformed,corrected)
            applied.append({"lesson":slug,"original":malformed,"reader_destination":"companions/KT-OPK-12.html","kind":"Display-only repair of the malformed Markdown URL before link parsing; source bytes retained"})
        assets = read_unit_assets(source, metadata["id"], unit)
        rendered = render_markdown_math(text, local_links=local_links, heading_anchors=unit["heading_anchors"], assets=assets)
        sources[(metadata["id"], slug)] = {"html": rendered, "assets": assets}
        units.append(unit)
    validate_course_links({"id": metadata["id"], "units": units, "linked_files":linked_files}, sources)
    for number, slug in enumerate(SLUGS):
        unit = bindings[slug]
        rendered, changes = rebind_html(sources[(metadata["id"], slug)]["html"], sources[(metadata["id"], slug)]["assets"], rewrites)
        applied.extend({"lesson": slug, **change} for change in changes)
        nav = '<nav aria-label="Course navigation"><a href="../../index.html">Open Mathematics Courses</a><a href="index.html">Course contents</a><a href="' + html.escape(unit["source"]) + '" download>Markdown source</a><a href="sources.html">Sources and terms</a></nav>'
        next_links = []
        if number:
            next_links.append('<a href="' + SLUGS[number - 1] + '.html">Previous lesson</a>')
        if number + 1 < len(SLUGS):
            next_links.append('<a href="' + SLUGS[number + 1] + '.html">Next lesson</a>')
        (dest / (slug + ".html")).write_text(page(unit["title"], nav + BANNER + rendered + '<nav aria-label="Lesson sequence">' + " ".join(next_links) + '</nav>', math=True), encoding="utf-8")
    assets_dir = dest / "assets"
    for name in ("tex-svg.js", "LICENSE", "input/tex/extensions/mathtools.js"):
        copy_exact(HERE / "assets/mathjax" / name, assets_dir / "mathjax" / name)
    (assets_dir / "reader").mkdir(parents=True, exist_ok=True)
    (assets_dir / "reader/reader.css").write_text(STYLE + "\n", encoding="utf-8")
    (assets_dir / "reader/mathjax-config.js").write_text(MATH_CONFIG + "\n", encoding="utf-8")
    (assets_dir / "reader/mathjax-mathtools-config.js").write_text(MATHTOOLS_CONFIG + "\n", encoding="utf-8")
    for name in ("LICENSE-reader-CC0.txt", "LICENSE-markdown-it-py.txt", "LICENSE-mdurl.txt"):
        copy_exact(HERE / "licenses" / name, dest / "component-licenses" / name)
    # A complete portable build source accompanies this course. State, QA,
    # private source references and local process logs are not copied.
    tool_files = [HERE / "build_release.py", HERE / "README.md"]
    tool_files += [p for folder in ("reader", "vendor", "licenses", "assets", "companion-inputs") for p in (HERE / folder).rglob("*") if p.is_file() and "__pycache__" not in p.parts and p.suffix != ".pyc"]
    for p in sorted(tool_files):
        relative = p.relative_to(HERE)
        copy_exact(p, dest / "reader-source" / relative)
    notice_links = {"LICENSE": "LICENSE", "STATUS.md": "status.html", "SOURCE-LICENSES.md": "sources.html", **{"src/" + s + ".md": s + ".html" for s in SLUGS}}
    status = render_markdown_math((dest / "STATUS.md").read_text(encoding="utf-8"), local_links=notice_links)
    (dest / "status.html").write_text(page("Course status", '<nav><a href="index.html">Course contents</a></nav>' + status, math=True), encoding="utf-8")
    source_notice = render_markdown_math((dest / "SOURCE-LICENSES.md").read_text(encoding="utf-8"), local_links=notice_links)
    rows = ''.join('<li><a href="' + s + '.html">' + html.escape(bindings[s]["title"]) + '</a> · <a href="src/' + s + '.md" download>Markdown</a></li>' for s in SLUGS)
    figure_rows = ''.join('<tr><td>' + html.escape(row["id"]) + '</td><td><a href="' + row["source"] + '" download>PNG</a></td><td><a href="figures/' + row["id"] + '.svg" download>Editable SVG</a></td></tr>' for row in figures["figures"])
    sources_body = '<nav><a href="index.html">Course contents</a></nav>' + source_notice + '<h2>Lesson sources</h2><ol>' + rows + '</ol><p><a href="course.json">Course metadata</a> · <a href="../../downloads/' + DOWNLOAD_NAME + '" download>Download reader and sources</a></p><h2>Companion readings</h2><p><a href="companions/index.html">Algebra, topology, analysis and measure-theory readings</a>. Each retains its own source credits and licence. The GFDL 1.2 reading retains its required notices.</p><h2>Figures</h2><table><thead><tr><th>Figure</th><th>Rendering</th><th>Source</th></tr></thead><tbody>' + figure_rows + '</tbody></table><h2>Reader components</h2><ul><li><a href="component-licenses/LICENSE-reader-CC0.txt">Course renderer and adapter: CC0 1.0</a></li><li><a href="assets/mathjax/LICENSE">MathJax 3.2.2: Apache License 2.0</a></li><li><a href="component-licenses/LICENSE-markdown-it-py.txt">markdown-it-py 3.0.0: MIT</a></li><li><a href="component-licenses/LICENSE-mdurl.txt">mdurl 0.1.2: MIT</a></li></ul><p><a href="reader-source/README.md">Reader regeneration instructions</a> · <a href="reader-source/build_release.py">Build adapter</a></p>'
    (dest / "sources.html").write_text(page("Sources and component terms", sources_body), encoding="utf-8")
    intro = '<nav><a href="../../index.html">Open Mathematics Courses</a></nav>' + BANNER + '<h1>' + html.escape(metadata["title"]) + '</h1><p>' + html.escape(metadata["description"]) + '</p><p>Five lessons in English, with examples, exercises, solutions and ' + str(figure_count) + ' diagrams. Read the lessons in this order:</p><ol>' + rows + '</ol><p><a href="status.html">Proved scope and remaining questions</a> · <a href="sources.html">Sources, figures and component terms</a> · <a href="companions/index.html">Companion readings</a> · <a href="../../downloads/' + DOWNLOAD_NAME + '" download>Download reader and editable sources</a></p>'
    (dest / "index.html").write_text(page(metadata["title"], intro), encoding="utf-8")
    manifests = {p.relative_to(dest).as_posix(): {"sha256": sha(p.read_bytes()), "bytes": p.stat().st_size} for p in sorted(dest.rglob("*")) if p.is_file() and p.name != "release-manifest.json" and "__pycache__" not in p.parts}
    manifest = {"schema": "ncg-portable-release/v1", "assignment_id": ASSIGNMENT, "status": "draft-incomplete", "proof_completion": False, "independent_mathematical_review": False, "public_source_files": source_files, "reader_files": manifests, "source_metadata_sha256": source_files["course.json"]["sha256"], "renderer_capacity": MAX_ASSETS, "supporting_proof_files":len(companion_manifest["proof_files"]) if companion_manifest else 0,"supporting_source_manifest":"companions/manifest.json" if companion_manifest else None, "link_destination_adaptations": applied, "privacy_scope": "Exact public allowlist only; no private notes, source logs or repository history.", "mathjax": {"version": "3.2.2", "source_url": "https://cdn.jsdelivr.net/npm/mathjax@3.2.2/es5/tex-svg.js", "license": "Apache-2.0", "sha256": sha((HERE / "assets/mathjax/tex-svg.js").read_bytes())}}
    write_json(dest / "release-manifest.json", manifest)
    archive = docs / "downloads" / DOWNLOAD_NAME
    archive.parent.mkdir(parents=True, exist_ok=True)
    archive_files = {}
    with zipfile.ZipFile(archive, "w", zipfile.ZIP_DEFLATED, compresslevel=9) as zipped:
        for p in sorted(dest.rglob("*")):
            if p.is_file() and "__pycache__" not in p.parts:
                relative = p.relative_to(docs).as_posix()
                payload = p.read_bytes()
                if p.suffix == ".html":
                    original = 'href="../../downloads/' + DOWNLOAD_NAME + '"'
                    online = 'href="https://kokunoyumeto.github.io/open-math-courses/downloads/' + DOWNLOAD_NAME + '"'
                    payload = payload.decode("utf-8").replace(original,online).encode("utf-8")
                info = zipfile.ZipInfo(relative, date_time=(2026, 10, 3, 0, 0, 0))
                info.compress_type = zipfile.ZIP_DEFLATED
                info.external_attr = 0o644 << 16
                zipped.writestr(info,payload)
                archive_files[relative] = {"sha256":sha(payload),"bytes":len(payload)}
        info = zipfile.ZipInfo("index.html",date_time=(2026,10,3,0,0,0))
        info.compress_type = zipfile.ZIP_DEFLATED
        info.external_attr = 0o644 << 16
        offline_index = '<!doctype html><html lang="en"><meta charset="utf-8"><title>Foliations course draft</title><p><a href="courses/NCG-FOLIATIONS/index.html">Read Foliations and their operator algebras</a></p><p>Serve this folder with a local HTTP server to render the mathematics. All reader scripts, proof sources and diagrams are included. Archive re-download links use the anonymous public site; exact offline file hashes are in offline-manifest.json.</p></html>\n'
        zipped.writestr(info,offline_index)
        archive_files["index.html"] = {"sha256":sha(offline_index.encode()),"bytes":len(offline_index.encode())}
        info = zipfile.ZipInfo("offline-manifest.json",date_time=(2026,10,3,0,0,0))
        info.compress_type = zipfile.ZIP_DEFLATED
        info.external_attr = 0o644 << 16
        zipped.writestr(info,json.dumps({"schema":"ncg-offline-files/v1","files":archive_files,"projection_adaptation":"Only the ZIP re-download links use the anonymous public site; the archive has an offline root navigation page. Source Markdown, figure and runtime bytes are identical to the public staging tree.","proof_completion":False,"independent_mathematical_review":False},ensure_ascii=False,indent=2)+"\n")
    link_report = validate_site(docs, dest)
    # Validate all non-TeX public payloads for machine paths and personal names.
    for p in dest.rglob("*"):
        if p.is_file() and p.suffix in {".html", ".md", ".json", ".svg", ".css"}:
            text = p.read_text(encoding="utf-8")
            if re.search(r"[A-Za-z]:[\\/]Users[\\/]|file://|localhost:[0-9]+|127\.0\.0\.1:[0-9]+", text, re.I):
                raise ValueError("machine-local reference in public output: " + p.name)
    staged = {p.relative_to(output).as_posix(): {"sha256": sha(p.read_bytes()), "bytes": p.stat().st_size} for p in sorted(docs.rglob("*")) if p.is_file() and "__pycache__" not in p.parts}
    write_json(output / "build-manifest.json", {"schema": "ncg-staging-build/v1", "staged_files": staged, "public_source_files": source_files, "lessons": len(SLUGS), "figures": figure_count, "k_theory_images": k_theory_images, "math_source_spans": sum(s["html"].count("data-tex=") for s in sources.values()), "links": link_report, "proof_completion": False, "independent_mathematical_review": False})
    print(json.dumps({"staging": str(output), "files": len(staged), "formulas": sum(s["html"].count("data-tex=") for s in sources.values()), "unresolved_retired_links": len(link_report["unresolved_retired_programme_urls"]), "proof_completion": False}))


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--source", type=Path, required=True, help="Exact public course source directory")
    parser.add_argument("--output", type=Path, required=True, help="Separate staging directory")
    parser.add_argument("--link-rewrites", type=Path, help="Exact public provider URL destinations")
    build(parser.parse_args())
