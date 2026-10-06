"""Rebuild this reading's HTML: Python 3.10+ and markdown-it-py 4.0.0.

Run this file without parameters beside readings.json. Mathematics remains
verbatim in data-tex; MathJax and its font files are supplied in the edition.
Reader code: CC0-1.0. No mathematical or third-party component is relicensed.
"""
from pathlib import Path
import hashlib
import html
import json
import re
from html.parser import HTMLParser
from urllib.parse import urlsplit
from markdown_it import MarkdownIt

ROOT = Path(__file__).resolve().parent
CSS = """*{box-sizing:border-box}body{margin:0;background:#fafbf9;color:#172635;font:18px/1.65 system-ui,sans-serif}main{max-width:58rem;margin:2rem auto;padding:0 1.3rem}nav{font-size:.95rem;border-bottom:1px solid #ccd8df;padding-bottom:1rem}a{color:#075c89}h1{font-size:2.1rem;line-height:1.2}h2{font-size:1.5rem;line-height:1.3;margin-top:2.4rem}h3{font-size:1.15rem;margin-top:1.8rem}p,li{overflow-wrap:anywhere}article img{display:block;max-width:100%;height:auto;margin:1.3rem auto}.math{overflow-wrap:normal}.math:not(.math-display){display:inline-block;max-width:100%;overflow-x:auto;overflow-y:hidden;vertical-align:middle}.math-display{display:block;max-width:100%;overflow-x:auto;padding:.25rem 0;margin:1rem 0}mjx-container[display=true]{margin:.5rem 0!important}table{display:block;overflow-x:auto;border-collapse:collapse}th,td{padding:.6rem;border:1px solid #ccd8df}code{font-size:.9em}footer{margin:3rem 0 1rem;border-top:1px solid #ccd8df;padding-top:1rem;font-size:.95rem}@media(max-width:420px){body{font-size:16px}main{padding:0 .85rem}h1{font-size:1.7rem}}"""


def render(source):
    md = MarkdownIt("commonmark", {"html": False}).enable("table")
    delimiters = ((r"\[", r"\]"), (r"\(", r"\)"))

    def inline(state, silent):
        for opening, closing in delimiters:
            if not state.src.startswith(opening, state.pos):
                continue
            end = state.src.find(closing, state.pos + len(opening))
            if end < 0:
                raise ValueError("Unclosed mathematical delimiter")
            if not silent:
                token = state.push("reading_math", "", 0)
                token.content = state.src[state.pos:end + len(closing)]
            state.pos = end + len(closing)
            return True
        return False

    def block(state, start, end, silent):
        begin = state.bMarks[start] + state.tShift[start]
        raw = state.src[begin:state.eMarks[start]]
        if not raw.startswith(r"\["):
            return False
        stop = start
        while r"\]" not in raw[2:]:
            stop += 1
            if stop >= end:
                raise ValueError("Unclosed display")
            raw += "\n" + state.src[state.bMarks[stop] + state.tShift[stop]:state.eMarks[stop]]
        if raw.split(r"\]", 1)[1].strip():
            return False
        if silent:
            return True
        token = state.push("reading_math", "", 0)
        token.content, token.block, token.map = raw, True, [start, stop + 1]
        state.line = stop + 1
        return True

    def operator_star(state, silent):
        at = state.pos
        if (state.src[at:at+1] != "*" or (at and state.src[at-1] == "*")
                or not re.match(r"-[A-Za-z]", state.src[at+1:])):
            return False
        if not silent:
            state.push("text", "", 0).content = "*"
        state.pos += 1
        return True

    def math(tokens, at, options, env):
        raw = next(raw_math)
        assert [line.lstrip(' \t') for line in raw.splitlines()] == [line.lstrip(' \t') for line in tokens[at].content.splitlines()], 'Mathematical token order changed'
        klass = "math math-display" if raw.startswith(r"\[") else "math"
        return '<span class="' + klass + '" data-tex="' + html.escape(raw, quote=True) + '">' + html.escape(raw) + '</span>\n'

    def heading(tokens, at, options, env):
        opening = md.renderer.renderToken(tokens, at, options, env)
        identity = tokens[at].attrGet('id') or ''
        return opening + ('<span id="' + identity.lower() + '"></span>' if identity.startswith('OA-MOD-') else '')

    md.inline.ruler.before("escape", "reading_math", inline)
    md.inline.ruler.before("emphasis", "operator_star", operator_star)
    md.block.ruler.after("fence", "reading_math", block)
    md.renderer.rules["reading_math"] = math
    md.renderer.rules['heading_open'] = heading
    raw_math = iter(re.findall(r'\\\[.*?\\\]|\\\(.*?\\\)', source, re.S))
    tokens = md.parse(source)
    seen = set()
    for at, token in enumerate(tokens):
        if token.type == "heading_open":
            title = tokens[at+1].content
            match = re.match(r"^(OA-MOD-[A-Z]+-\d+)\s+[—–-]\s+(.*)$", title)
            identity = match.group(1) if match else re.sub(r"[^\w-]+", "-", title.lower()).strip("-")
            if identity in seen:
                raise ValueError("Duplicate heading " + identity)
            seen.add(identity)
            token.attrSet("id", identity)
            if match and identity.startswith("OA-MOD-TC-"):
                visible = tokens[at + 1]
                prefix = title[:match.start(2)]
                assert visible.children and visible.children[0].type == "text"
                assert visible.children[0].content.startswith(prefix)
                visible.children[0].content = visible.children[0].content[len(prefix):]
                visible.content = match.group(2)
        for child in token.children or []:
            if child.type == "link_open":
                target = child.attrGet("href") or ""
                parsed = urlsplit(target)
                if not parsed.scheme and parsed.path.endswith(".md") and not parsed.path.startswith("src/"):
                    child.attrSet("href", target.replace(".md", ".html", 1))
    rendered = md.renderer.render(tokens, md.options, {})
    assert next(raw_math, None) is None, 'Unrendered source mathematics'
    return rendered


def build():
    manifest = json.loads((ROOT / "readings.json").read_text(encoding="utf-8"))
    (ROOT / "reader.css").write_text(CSS + "\n", encoding="utf-8", newline="\n")
    records = []
    for entry in manifest["readings"]:
        source = (ROOT / entry["source"]).read_text(encoding="utf-8")
        body = render(source)
        title = html.escape(entry["title"])
        config = {"tex": {"inlineMath": [[r"\(", r"\)"]], "displayMath": [[r"\[", r"\]"]], "processEscapes": True}, "options": {"renderActions": {"addMenu": []}}}
        page = '<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>' + title + ' · Open Mathematics Courses</title><link rel="stylesheet" href="reader.css"><script>window.MathJax=' + json.dumps(config) + ';</script><script defer src="../../assets/mathjax/tex-chtml-full.js"></script></head><body><main><nav aria-label="Reading navigation"><a href="../../index.html">Open Mathematics Courses</a> · <a href="index.html">Reading contents</a> · <a href="dependencies.html">Prerequisite results</a> · <a href="sources.html">Sources and terms</a> · <a href="' + html.escape(entry["source"], quote=True) + '">Editable Markdown</a></nav><article>' + body + '</article><footer>Mathematical exposition: OpenAI Codex (AI), October 2026. <a href="sources.html">Human research sources, AI contributions and component terms</a>.</footer></main></body></html>\n'
        destination = ROOT / entry["reader"]
        destination.write_text(page, encoding="utf-8", newline="\n")
        records.append({"source": entry["source"], "source_sha256": hashlib.sha256(source.encode()).hexdigest(), "reader": entry["reader"], "reader_sha256": hashlib.sha256(page.encode()).hexdigest()})
    print(json.dumps({"status": "PASS", "readings": records}))


if __name__ == "__main__":
    build()
