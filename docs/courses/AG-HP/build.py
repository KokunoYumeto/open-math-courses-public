"""Build the Hilbert and Picard course from its editable Markdown and TeX.

Original build software: CC0 1.0 Universal.
"""
from pathlib import Path
from urllib.parse import urlsplit, urlunsplit
import argparse, hashlib, html, json, posixpath, re, shutil, sys
from bs4 import BeautifulSoup

ROOT = Path(__file__).resolve().parent
sys.path.insert(0, str(ROOT / "buildlib"))
from render_math import render_markdown_math

def digest(data):
    return hashlib.sha256(data).hexdigest()

def render_reading(row, course, standalone=False):
    source = (ROOT / row["source"]).read_text(encoding="utf-8")
    raw_links = {urlsplit(m[1]).path for m in re.finditer(r"\]\(([^\s)]+)", source)
                 if not m[1].startswith(("https:", "http:", "mailto:", "#"))}
    own = {r["reader"] for r in course["readings"]}
    links = {}
    for path in raw_links:
        target = row.get("source_link_targets", {}).get(path, path)
        if standalone and target not in own:
            resolved = posixpath.normpath("courses/AG-HP/" + target)
            target = course["programme_url"] + resolved
        links[path] = target
    headings = []
    for binding in row.get("heading_aliases", []):
        text = binding["heading"]
        if source.count(text) != 1:
            raise ValueError("A stable heading must occur exactly once: " + text)
        headings.append({"line": source[:source.index(text)].count("\n") + 1,
                         "ids": binding["ids"]})
    body = render_markdown_math(source, local_links=links, heading_anchors=headings)
    if row.get("label_anchors"):
        parsed = BeautifulSoup(body, "html.parser")
        for binding in row["label_anchors"]:
            matches = [e for e in parsed.select("strong") if e.get_text() == binding["label"]]
            if len(matches) != 1 or matches[0].get("id"):
                raise ValueError("A stable mathematical label is ambiguous: " + binding["label"])
            matches[0]["id"] = binding["id"]
        body = str(parsed)
    return source, body

def page(row, body, course, previous=None, following=None):
    navigation = []
    if previous:
        navigation.append('<a href="' + html.escape(previous["reader"], quote=True) +
                          '">Previous: ' + html.escape(previous["title"]) + "</a>")
    navigation.append('<a href="index.html">Course contents</a>')
    if following:
        navigation.append('<a href="' + html.escape(following["reader"], quote=True) +
                          '">Next: ' + html.escape(following["title"]) + "</a>")
    values = {
        "TITLE": html.escape(row["title"]),
        "COURSE": html.escape(course["title"]),
        "CANONICAL": html.escape(course["programme_url"] + "courses/AG-HP/" + row["reader"], quote=True),
        "POSITION": "Lesson " + str(row["number"]) + " of 12" if row.get("number") else "Supporting reading",
        "SOURCE": html.escape(row["source"], quote=True),
        "BODY": body,
        "NAVIGATION": ' <span aria-hidden="true">·</span> '.join(navigation),
    }
    result = (ROOT / "buildlib/page.html").read_text(encoding="utf-8")
    for key, value in values.items():
        result = result.replace("{{" + key + "}}", value)
    return result

def build(output=None, standalone=False):
    course = json.loads((ROOT / "readings.json").read_text(encoding="utf-8"))
    assert len(course["readings"]) == 13
    numbered = [r for r in course["readings"] if r.get("number")]
    assert [r["number"] for r in numbered] == list(range(1, 13))
    destination = Path(output).resolve() if output else ROOT
    destination.mkdir(parents=True, exist_ok=True)
    records = []
    for row in course["readings"]:
        source, body = render_reading(row, course, standalone=standalone)
        n = row.get("number")
        previous = numbered[n-2] if n and n > 1 else None
        following = numbered[n] if n and n < 12 else None
        content = page(row, body, course, previous, following)
        (destination / row["reader"]).write_text(content, encoding="utf-8", newline="\n")
        records.append({"reader": row["reader"], "source": row["source"],
                        "source_sha256_lf": digest(source.encode()),
                        "reader_sha256_lf": digest(content.encode())})
    if destination != ROOT:
        for path in ["index.html", "licensing.html", "reader.css", "README.md", "LICENSE.md", "readings.json"]:
            shutil.copyfile(ROOT / path, destination / path)
    return records

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", help="Directory for generated readings; defaults to this course directory.")
    parser.add_argument("--standalone", action="store_true",
                        help="Link prerequisites to their online programme readings.")
    args = parser.parse_args()
    records = build(args.output, args.standalone)
    print("Built " + str(len(records)) + " readings.")
