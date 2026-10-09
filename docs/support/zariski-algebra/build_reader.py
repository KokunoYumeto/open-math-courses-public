"""Render the editable mathematical source using the programme's CC0 renderer.

Run with Python plus markdown-it-py from this repository checkout.
"""
from pathlib import Path
from urllib.parse import urlsplit
import hashlib
import json
import re
import sys

HERE = Path(__file__).resolve().parent
DOCS = HERE.parents[1]
REPO = DOCS.parent
sys.path.insert(0, str(DOCS/'courses/AG-QC/renderer'))
from course_reader import render_markdown_math

ALIASES = {
    'Integral closure and localization': ['algebra-lemma-integral-closure-localize'],
    'Coefficients in the radical of a conductor': ['algebra-lemma-all-coefficients-in-J'],
    'Strong transcendence and quasi-finite points': ['algebra-lemma-reduced-strongly-transcendental-not-quasi-finite'],
    'Finite presentation across a finite algebra': ['algebra-lemma-finite-finitely-presented-extension', 'finite-presentation-under-finite-algebra'],
    'Dimension near a point after extension of the ground field': ['algebra-lemma-dimension-at-a-point-preserved-field-extension', 'dimension-under-field-extension'],
}

def digest(path):
    return hashlib.sha256(path.read_bytes().replace(b'\r\n', b'\n')).hexdigest()

def main():
    source = (HERE/'src/zariski-algebra.md').read_text(encoding='utf-8')
    bindings = [{'line':number, 'ids':ALIASES[re.sub(r'^#+\s+', '', line)]}
                for number, line in enumerate(source.splitlines(), 1)
                if line.startswith('#') and re.sub(r'^#+\s+', '', line) in ALIASES]
    links = {urlsplit(href).path:urlsplit(href).path
             for href in re.findall(r'\]\(([^)]+)\)', source)
             if not urlsplit(href).scheme and urlsplit(href).path}
    body = render_markdown_math(source, local_links=links, heading_anchors=bindings)
    reader = HERE/'index.html'
    previous = reader.read_text(encoding='utf-8')
    rendered, count = re.subn(r'(<article class="lesson">).*?(</article>)',
                             lambda match:match[1]+body+match[2], previous, flags=re.S)
    assert count == 1
    reader.write_text(rendered, encoding='utf-8', newline='\n')
    manifest = HERE/'providers.json'
    routes = json.loads(manifest.read_text(encoding='utf-8'))
    for row in routes['providers']:
        row['source_sha256'] = digest(REPO/row['source'])
        row['reader_sha256'] = digest(REPO/row['reader'])
    manifest.write_text(json.dumps(routes,indent=2,ensure_ascii=False)+'\n',encoding='utf-8',newline='\n')

if __name__ == '__main__':
    main()
