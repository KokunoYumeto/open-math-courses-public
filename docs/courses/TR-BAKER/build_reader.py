"""Rebuild this course's editable LaTeX, HTML readers and source download. CC0."""
from pathlib import Path
import argparse
import hashlib
import html
import json
import posixpath
import re
import shutil
import subprocess
import sys
import tempfile
import unicodedata
from urllib.parse import urlsplit
import zipfile

COURSE = Path(__file__).resolve().parent
sys.dont_write_bytecode = True
sys.path.insert(0, str(COURSE / 'reader_engine'))
from course_reader import render_markdown_math
from course_assets import read_unit_assets, asset_output_path


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest().upper()


def bind_figures(tex):
    """Keep an authored Figure paragraph with its image, including mathematics."""
    pattern = re.compile(r'\\begin\{figure\}\n[\s\S]*?\\end\{figure\}\n\s*\\emph\{')
    position = 0
    parts = []
    for match in pattern.finditer(tex):
        if match.start() < position:
            continue
        brace = match.end() - 1
        depth, end = 1, brace + 1
        while depth:
            if end >= len(tex):
                raise ValueError('Unclosed figure explanation')
            if tex[end] in '{}':
                escapes, before = 0, end - 1
                while before >= 0 and tex[before] == '\\':
                    escapes += 1
                    before -= 1
                if escapes % 2 == 0:
                    depth += 1 if tex[end] == '{' else -1
            end += 1
        figure = tex[match.start():brace]
        graphic = next(line for line in figure.splitlines() if '\\pandocbounded{' in line)
        explanation = tex[brace + 1:end - 1]
        parts += [tex[position:match.start()],
                  '\\begin{minipage}[t]{\\linewidth}\n\\centering\n' + graphic +
                  '\n\\par\\smallskip\n\\begin{flushleft}\\small\n\\emph{' +
                  explanation + '}\n\\end{flushleft}\n\\end{minipage}\\par\\medskip\n']
        position = end
    return ''.join(parts) + tex[position:]


def write_tex(unit, pandoc):
    source = COURSE / unit['source']
    text = source.read_text(encoding='utf-8')
    destination = COURSE / 'sources' / (unit['internal_id'] + '.tex')
    destination.parent.mkdir(exist_ok=True)
    with tempfile.TemporaryDirectory(prefix='tr-baker-pandoc-') as temporary:
        input_file = Path(temporary) / 'lesson.md'
        output_file = Path(temporary) / 'lesson.tex'
        input_file.write_text('\n'.join(text.splitlines()[1:]) + '\n', encoding='utf-8')
        command = [pandoc, str(input_file), '--from=markdown+tex_math_single_backslash',
                   '--to=latex', '--standalone', '--metadata=title:' + unit['title'],
                   '--metadata=author:GPT-6.1 Sol (OpenAI), Ultra',
                   '--metadata=date:October 2026', '--variable=papersize:a4',
                   '--variable=fontsize:11pt', '--variable=geometry:margin=22mm',
                   '--resource-path=' + str(source.parent), '--output=' + str(output_file)]
        result = subprocess.run(command, capture_output=True, text=True, encoding='utf-8', errors='replace')
        if result.returncode:
            raise RuntimeError(result.stderr)
        tex = bind_figures(output_file.read_text(encoding='utf-8'))
    # amsmath requires the outer display, rather than aligned/gathered, to own a tag.
    def move_tag(match):
        inner = match.group(0)
        tags = re.findall(r'\\tag\{([^}]+)\}', inner)
        if not tags:
            return inner
        if len(tags) != 1:
            raise ValueError('Multiple tags in one aligned/gathered environment')
        return re.sub(r'\s*\\tag\{[^}]+\}', '', inner) + ' \\tag{' + tags[0] + '}'
    tex = re.sub(r'\\begin\{(aligned|gathered)\}[\s\S]*?\\end\{\1\}', move_tag, tex)
    tex = tex.replace('\\begin{document}', '\\providecommand{\\Eta}{\\mathrm{H}}\n\\begin{document}', 1)
    if unit['internal_id'] == 'TR-BAKER-07':
        # Retain the checked table widths of the previous editable edition.
        for old, new in [('0.1429', '0.14285'), ('0.0968', '0.1168'),
                         ('0.1290', '0.1261'), ('0.1579', '0.2299'), ('0.2105', '0.1925')]:
            tex = tex.replace('\\real{' + old + '}', '\\real{' + new + '}')
    source_tags = re.findall(r'\\tag\{([^}]+)\}', text)
    assert re.findall(r'\\tag\{([^}]+)\}', tex) == source_tags
    # The complete lesson is inline; figures remain relative to sources/.
    assert '\\input{' not in tex and '\\include{' not in tex
    # Preserve an unchanged checkout's bytes and timestamp, including CRLF.
    if not destination.exists() or destination.read_text(encoding='utf-8') != tex:
        destination.write_text(tex, encoding='utf-8', newline='\n')


def slug(text):
    text = unicodedata.normalize('NFKD', text).encode('ascii', 'ignore').decode('ascii').lower()
    return re.sub(r'[^a-z0-9]+', '-', text).strip('-')


def render_unit(unit, template, number, total, units):
    uid = unit['internal_id']
    source = COURSE / unit['source']
    text = source.read_text(encoding='utf-8')
    # Git may check text out with CRLF on Windows; catalogue hashes bind LF text.
    assert hashlib.sha256(text.encode('utf-8')).hexdigest().upper() == unit['sha256']
    anchors = unit.get('heading_anchors')
    if anchors is None:
        anchors = [{'line': n, 'ids': [slug(re.sub(r'^#{1,6} ', '', line))]}
                   for n, line in enumerate(text.splitlines(), 1) if re.match(r'^#{1,6} ', line)]
        unit['heading_anchors'] = anchors
    assets = read_unit_assets(COURSE, 'TR-BAKER',
                              {'id': uid, 'source': unit['source'], 'assets': unit.get('assets', [])})
    links = {}
    for href in re.findall(r'\]\(([^)]+)\)', text):
        parsed = urlsplit(href)
        if not parsed.scheme and parsed.path and not href.startswith('#'):
            links[parsed.path] = posixpath.normpath(posixpath.join('src', parsed.path))
    body = render_markdown_math(text, local_links=links, heading_anchors=anchors, assets=assets)
    if uid == 'TR-BAKER-08':
        safe = 'the-baker-wustholz-dependence-on-the-number-of-logarithms'
        alias = 'the-baker-wüstholz-dependence-on-the-number-of-logarithms'
        body = body.replace('id="' + safe + '">', 'id="' + safe + '"><span id="' + alias + '"></span>', 1)
    for row in unit.get('assets', []):
        generated = asset_output_path('TR-BAKER', uid, row).split('/', 2)[2]
        body = body.replace('src="' + generated + '"', 'src="' + row['source'] + '"')
    direct = '<p class="small source-link"><a href="sources/' + uid + '.tex" download>Editable LaTeX source of this lesson</a> · <a href="src/' + uid + '.md" download>Markdown source</a></p>'
    document = re.sub(r'(<article class="lesson">).*?(</article>)',
                      lambda m: m.group(1) + '\n' + body + '\n' + m.group(2), template, count=1, flags=re.S)
    document = re.sub(r'<title>.*?</title>', '<title>' + html.escape(unit['title']) + ' · Linear forms in logarithms and their applications</title>', document, count=1)
    document = re.sub(r'(<link rel="canonical" href=")[^"]*',
                      r'\1https://kokunoyumeto.github.io/open-math-courses/courses/TR-BAKER/' + uid + '.html', document, count=1)
    document = re.sub(r'Lesson \d+ of \d+', f'Lesson {number} of {total}', document)
    previous = '<span></span>' if number == 1 else '<a rel="prev" href="' + units[number - 2]['internal_id'] + '.html">← ' + html.escape(units[number - 2]['title']) + '</a>'
    following = '<span></span>' if number == total else '<span class="pager-next"><a rel="next" href="' + units[number]['internal_id'] + '.html">' + html.escape(units[number]['title']) + ' →</a></span>'
    pager = '<nav class="pager" aria-label="Lessons">' + previous + '<a href="./">Course contents</a>' + following + '</nav>'
    document = re.sub(r'<nav class="pager".*?</nav>', lambda m: pager, document, count=1, flags=re.S)
    document = re.sub(r'<p class="small source-link">.*?</p>', lambda m: direct, document, count=1, flags=re.S)
    (COURSE / (uid + '.html')).write_text(document, encoding='utf-8', newline='\n')


def source_archive(destination):
    """Include the exact course, offline reader assets and their licence notices."""
    docs = COURSE.parent.parent
    members = []
    for path in COURSE.rglob('*'):
        if path.is_file() and '__pycache__' not in path.parts and path.suffix not in {'.aux', '.log', '.out', '.zip', '.pdf'}:
            members.append((path, 'docs/courses/TR-BAKER/' + path.relative_to(COURSE).as_posix()))
    for name in ['site.css', 'mathjax']:
        path = docs / 'assets' / name
        files = list(path.rglob('*')) if path.is_dir() else [path]
        for asset in files:
            if asset.is_file():
                members.append((asset, 'docs/assets/' + asset.relative_to(docs / 'assets').as_posix()))
    destination.parent.mkdir(parents=True, exist_ok=True)
    def archive_bytes(path):
        data = path.read_bytes()
        if path.suffix.lower() in {'.md', '.json', '.py', '.html', '.css', '.js', '.tex', '.txt'}:
            data = data.replace(b'\r\n', b'\n')
        return data
    with zipfile.ZipFile(destination, 'w', zipfile.ZIP_DEFLATED) as archive:
        for path, name in sorted(members, key=lambda pair: pair[1]):
            archive.writestr(name, archive_bytes(path))
    with zipfile.ZipFile(destination) as archive:
        assert archive.testzip() is None
        assert len(archive.namelist()) == len(set(archive.namelist()))
        for path, name in members:
            assert archive.read(name) == archive_bytes(path)
    print('Source archive:', len(members), 'exact files')


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--tex', action='store_true', help='Generate complete standalone LaTeX with Pandoc')
    parser.add_argument('--pandoc', default='pandoc')
    parser.add_argument('--readers', action='store_true')
    parser.add_argument('--archive', type=Path)
    args = parser.parse_args()
    metadata = json.loads((COURSE / 'course.json').read_text(encoding='utf-8'))
    units = metadata['units']
    if args.tex:
        for unit in units:
            write_tex(unit, args.pandoc)
            print('LaTeX:', unit['internal_id'])
    if args.readers:
        template = (COURSE / 'TR-BAKER-08.html').read_text(encoding='utf-8')
        for number, unit in enumerate(units, 1):
            path = COURSE / (unit['internal_id'] + '.html')
            existing = path.read_text(encoding='utf-8') if path.exists() else template
            render_unit(unit, existing, number, len(units), units)
        (COURSE / 'course.json').write_text(json.dumps(metadata, ensure_ascii=False, indent=2) + '\n', encoding='utf-8', newline='\n')
    if args.archive:
        source_archive(args.archive)


if __name__ == '__main__':
    main()
