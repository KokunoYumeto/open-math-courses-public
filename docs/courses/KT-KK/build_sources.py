from pathlib import Path
import subprocess
import json
import tempfile
import re
import posixpath
from urllib.parse import urlsplit, urlunsplit

r = Path(__file__).resolve().parent
course = json.loads((r / 'course.json').read_text(encoding='utf-8'))
lessons = [r / u['source'] for u in course['units'] + course.get('supplements', [])]
assert len(lessons) == len(set(lessons)), 'Duplicate source'
args = ['pandoc', '--eol=lf', '--from=markdown+tex_math_single_backslash-implicit_figures', '--to=latex', '--standalone', '--variable=geometry:margin=25mm', '--variable=fontsize:11pt']

def normalize_print_links(path):
    text = path.read_text(encoding='utf-8')
    labels = set(re.findall(r'\\label\{([^}]+)\}', text))
    def resolve(match):
        target = match.group(1)
        converted = re.sub(r'^\d+-', '', target)
        if target not in labels and converted in labels:
            return r'\hyperref[' + converted + ']'
        return match.group(0)
    text = re.sub(r'\\hyperref\[([^]]+)\]', resolve, text)
    path.write_text(text, encoding='utf-8', newline='\n')

def combined_source(source):
    body = source.read_text(encoding='utf-8')
    parent = source.parent.relative_to(r).as_posix()
    def rebase(route):
        parts = urlsplit(route)
        if parts.scheme or parts.netloc or not parts.path:
            return route
        path = posixpath.normpath(posixpath.join(parent, parts.path))
        return urlunsplit(('', '', path, parts.query, parts.fragment))
    def prose(part):
        part = re.sub(r'(\[[^\]]*\]\()([^\s)]+)(\))',
                      lambda m: m[1] + rebase(m[2]) + m[3], part)
        return re.sub(r'(\b(?:href|src)\s*=\s*["\'])([^"\']+)(["\'])',
                      lambda m: m[1] + rebase(m[2]) + m[3], part)
    parts = re.split(r'(\\\(.*?\\\)|\\\[.*?\\\])', body, flags=re.S)
    return ''.join(part if part.startswith((r'\(', r'\[')) else prose(part) for part in parts)

for p in lessons:
    subprocess.run(args + [p.relative_to(r).as_posix(), '-o', p.with_suffix('.tex').relative_to(r).as_posix()], cwd=r, check=True)
    normalize_print_links(p.with_suffix('.tex'))
with tempfile.TemporaryDirectory() as temporary:
    combined = Path(temporary) / 'course.md'
    combined.write_text('\n\n\\newpage\n\n'.join(combined_source(p) for p in lessons), encoding='utf-8', newline='\n')
    subprocess.run(args + ['--toc', '--metadata=title:Kasparov’s KK-theory', f'--metadata=subtitle:{len(course["units"])} lessons and {len(course.get("supplements", []))} proof companions', str(combined), '-o', 'KT-KK.tex'], cwd=r, check=True)
    normalize_print_links(r / 'KT-KK.tex')
