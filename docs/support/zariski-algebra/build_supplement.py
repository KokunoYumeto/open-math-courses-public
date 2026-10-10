"""Rebuild the definitions/comparison reader and its exact result bindings.

Uses the programme's existing markdown-it-py renderer. Run in the repository,
or in a download containing courses/AG-QC/renderer and the cited providers.
No network access, source import or publication is performed.
"""
from pathlib import Path
from urllib.parse import urlsplit
import hashlib
import json
import re
import sys

HERE = Path(__file__).resolve().parent
DOCS = HERE.parents[1]
sys.path.insert(0, str(DOCS / 'courses/AG-QC/renderer'))
from course_reader import render_markdown_math


def main():
    source = (HERE / 'src/definitions-and-dimension.md').read_text(encoding='utf-8')
    links = {urlsplit(h).path: urlsplit(h).path
             for h in re.findall(r'\]\(([^)]+)\)', source) if not urlsplit(h).scheme}
    body = render_markdown_math(source, local_links=links)
    template = (HERE / 'index.html').read_text(encoding='utf-8')
    page = re.sub(r'<title>.*?</title>', '<title>Finite presentations and dimension under a quotient</title>', template, count=1)
    page = re.sub(r'<nav>.*?</nav>', '<nav><a href="index.html">Algebra proof collection</a> · <a href="src/definitions-and-dimension.md">Editable source</a> · <a href="CC0-1.0.txt">CC0 dedication</a></nav>', page, count=1, flags=re.S)
    page, count = re.subn(r'(<article class="lesson">).*?(</article>)', lambda m: m[1] + body + m[2], page, count=1, flags=re.S)
    assert count == 1
    (HERE / 'definitions-and-dimension.html').write_text(page, encoding='utf-8', newline='\n')
    for name, key in [('result-routes.json', 'units'), ('providers.json', 'providers')]:
        path = HERE / name
        data = json.loads(path.read_text(encoding='utf-8'))
        for row in data[key]:
            for role in ('source', 'reader'):
                relative = row[role]
                assert relative.startswith('docs/') and '..' not in Path(relative).parts
                payload = (DOCS / relative.removeprefix('docs/')).read_bytes()
                row[role + '_sha256'] = hashlib.sha256(payload).hexdigest()
        path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + '\n', encoding='utf-8', newline='\n')


if __name__ == '__main__':
    main()
