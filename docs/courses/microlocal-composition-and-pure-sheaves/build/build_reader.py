"""Build the attributed readers with Python 3 and Pandoc.

Use --download for immutable external source links, and --only to select
reader filenames. Source links are rewritten only by the explicit link map.
"""
from pathlib import Path
import argparse
import json
import re
import subprocess
from reader_math_scrollers import scroll_math
from reader_empty_sets import repair_empty_set_glyphs

TABLE_STYLE = """<style>
.table-scroll { max-width: 100%; overflow-x: auto; margin: 1rem 0 1.5rem; }
.table-scroll table { border-collapse: collapse; width: 100%; min-width: 38rem; }
.table-scroll th, .table-scroll td { border: 1px solid #cbd5d5; padding: .65rem .8rem; text-align: left; vertical-align: top; }
.table-scroll th { background: #edf2ee; }
.table-scroll:focus-visible { outline: 2px solid #15526f; outline-offset: 3px; }
</style>
"""

def rewrite_links(source, links):
    """Replace complete Markdown hrefs; never strip path prefixes globally."""
    return re.sub(r'(\]\()([^\s)]+)(\))',
                  lambda m: m[1] + links.get(m[2], m[2]) + m[3], source)

def build(root, download=False, only=None):
    entries = json.loads((root / 'readings.json').read_text(encoding='utf-8'))['readings']
    config = json.loads((root / 'build/reader-links.json').read_text(encoding='utf-8'))
    links = config['download' if download else 'native']
    known = {entry['reader'] for entry in entries}
    if only and not set(only) <= known:
        raise ValueError('Unknown reader: ' + ', '.join(sorted(set(only) - known)))
    for entry in entries:
        if only and entry['reader'] not in only:
            continue
        source = (root / entry['source']).read_text(encoding='utf-8')
        normalized = rewrite_links(source, links)
        normalized = re.sub(r'\\tag\{([^}]+)\}',
                            lambda m: r'\qquad\text{(' + m[1] + ')}', normalized)
        run = subprocess.run(
            ['pandoc', '--from=markdown+tex_math_single_backslash', '--to=html5',
             '--mathml', '--template', str(root / 'build/reader-template.html'),
             '--metadata', 'title=' + entry['title']],
            input=normalized, capture_output=True, text=True, encoding='utf-8')
        if run.returncode or run.stderr.strip():
            raise RuntimeError(run.stderr)
        html = scroll_math(repair_empty_set_glyphs(run.stdout))
        if '<table' in html:
            html = html.replace('</head>', TABLE_STYLE + '</head>')
            html = re.sub(r'(<table\b.*?</table>)',
                          r'<div class="table-scroll" role="region" aria-label="Prerequisite statements and their roles" tabindex="0">\1</div>',
                          html, flags=re.S)
        # Keep one explicit newline convention across platforms.
        html = html.replace('\r\n', '\n').replace('\n', '\r\n')
        (root / entry['reader']).write_bytes(html.encode('utf-8'))

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--download', action='store_true',
                        help='link external prerequisites to immutable programme sources')
    parser.add_argument('--only', nargs='+', metavar='READER.html',
                        help='build only these reader filenames')
    args = parser.parse_args()
    build(Path(__file__).resolve().parents[1], args.download, args.only)
