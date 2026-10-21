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
from urllib.parse import urljoin, urlsplit
import zipfile

COURSE = Path(__file__).resolve().parent
sys.dont_write_bytecode = True
sys.path.insert(0, str(COURSE / 'reader_engine'))
from course_reader import render_markdown_math
from course_assets import read_unit_assets, asset_output_path


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest().upper()


def validate_metadata(metadata):
    """Keep the course catalogue limited to reader information and attribution."""
    if 'status' in metadata or any('status' in u for u in metadata['units']):
        raise ValueError('Course status belongs outside publication metadata')
    for unit in metadata['units']:
        for scope in unit.get('authorship_scope', {}).values():
            if re.search(r'(?i)self[- ]check|review pending|author review', scope):
                raise ValueError('Review commentary belongs outside publication metadata')


def current_pdf(unit):
    """Expose a compiled edition only when its source and bytes are current."""
    edition = unit.get('compiled_pdf')
    if not edition or edition['source_sha256'].upper() != unit['sha256'].upper():
        return None
    path = COURSE / edition['path']
    if path.parent != COURSE or path.suffix != '.pdf':
        raise ValueError('Unexpected compiled PDF path')
    if digest(path) != edition['sha256'].upper() or path.stat().st_size != edition['bytes']:
        raise ValueError('Compiled PDF identity mismatch')
    return path


def bind_figures(tex):
    """Keep an authored Figure paragraph with its image, including mathematics."""
    pattern = re.compile(
        r'\\begin\{figure\}\n(?:(?!\\end\{figure\})[\s\S])*'
        r'\\end\{figure\}\n\s*\\emph\{')
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
                   '--metadata=author:' + unit.get('written_by', 'GPT-6.1 Sol (OpenAI), Ultra'),
                   '--metadata=date:October 2026', '--variable=papersize:a4',
                   '--variable=fontsize:11pt', '--variable=geometry:margin=22mm',
                   '--resource-path=' + str(source.parent), '--output=' + str(output_file)]
        result = subprocess.run(command, capture_output=True, text=True, encoding='utf-8', errors='replace')
        if result.returncode:
            raise RuntimeError(result.stderr)
        tex = bind_figures(output_file.read_text(encoding='utf-8'))
    # A downloaded PDF must use web links rather than local-file launch actions.
    def pdf_link(match):
        href = match.group(1)
        parsed = urlsplit(href)
        if parsed.scheme or parsed.netloc or not parsed.path:
            return match.group(0)
        path = posixpath.normpath(posixpath.join('src', parsed.path))
        target = path + ('?' + parsed.query if parsed.query else '')
        target += ('#' + parsed.fragment if parsed.fragment else '')
        target = urljoin('https://kokunoyumeto.github.io/open-math-courses-public/courses/TR-BAKER/', target)
        return '\\href{' + target + '}'
    tex = re.sub(r'\\href\{([^}]+)\}', pdf_link, tex)
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
    if '\\mathscr' in tex:
        tex = tex.replace('\\begin{document}', '\\usepackage{mathrsfs}\n\\begin{document}', 1)
    tex = tex.replace('\\begin{document}', '\\providecommand{\\Eta}{\\mathrm{H}}\n\\begin{document}', 1)
    if unit['internal_id'] == 'TR-BAKER-07':
        # Column widths for the tables in Lesson 7.
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


def render_unit(unit, template, number, total, units, *, write=True):
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
    downloads = []
    edition = current_pdf(unit)
    if edition is not None:
        downloads.append('<a href="' + edition.name + '" download>PDF of this lesson</a>')
    downloads += ['<a href="sources/' + uid + '.tex" download>Editable LaTeX source of this lesson</a>',
                  '<a href="../../downloads/TR-BAKER-source.zip" download>Complete course source package</a>',
                  '<a href="src/' + uid + '.md" download>Markdown source</a>']
    direct = '<p class="small source-link">' + ' · '.join(downloads) + '</p>'
    document = re.sub(r'(<article class="lesson">).*?(</article>)',
                      lambda m: m.group(1) + '\n' + body + '\n' + m.group(2), template, count=1, flags=re.S)
    document = re.sub(r'<p class="lesson-status">.*?</p>\s*', '', document, flags=re.S)
    document = re.sub(r'<title>.*?</title>', '<title>' + html.escape(unit['title']) + ' · Linear forms in logarithms and their applications</title>', document, count=1)
    document = re.sub(r'(<link rel="canonical" href=")[^"]*',
                      r'\1https://kokunoyumeto.github.io/open-math-courses-public/courses/TR-BAKER/' + uid + '.html', document, count=1)
    document = re.sub(r'https://github\.com/KokunoYumeto/open-math-courses(?:-public)*(?=/|["#?]|$)',
                      'https://github.com/KokunoYumeto/open-math-courses-public', document)
    document = re.sub(r'Lesson \d+ of \d+', f'Lesson {number} of {total}', document)
    previous = '<span></span>' if number == 1 else '<a rel="prev" href="' + units[number - 2]['internal_id'] + '.html">← ' + html.escape(units[number - 2]['title']) + '</a>'
    following = '<span></span>' if number == total else '<span class="pager-next"><a rel="next" href="' + units[number]['internal_id'] + '.html">' + html.escape(units[number]['title']) + ' →</a></span>'
    pager = '<nav class="pager" aria-label="Lessons">' + previous + '<a href="./">Course contents</a>' + following + '</nav>'
    document = re.sub(r'<nav class="pager".*?</nav>', lambda m: pager, document, count=1, flags=re.S)
    document = re.sub(r'<p class="small source-link">.*?</p>', lambda m: direct, document, count=1, flags=re.S)
    document = document.replace('<span class="unlinked">Course sources</span>',
                                '<a href="../../downloads/TR-BAKER-source.zip">Course sources</a>')
    if write:
        (COURSE / (uid + '.html')).write_text(document, encoding='utf-8', newline='\n')
    return document


def source_archive(destination):
    """Include the exact course, offline reader assets and their licence notices."""
    docs = COURSE.parent.parent
    repository = docs.parent
    members = []
    metadata = json.loads((COURSE / 'course.json').read_text(encoding='utf-8'))
    validate_metadata(metadata)
    allowed = json.loads((COURSE / 'source-package-files.json').read_text(encoding='utf-8'))['members']
    if len(allowed) != len(set(allowed)):
        raise ValueError('Duplicate source-package member')
    current_editions = {path.resolve() for unit in metadata['units']
                        if (path := current_pdf(unit)) is not None}
    for name in allowed:
        if not (name.startswith('docs/courses/TR-BAKER/') or
                name.startswith('docs/assets/mathjax/') or name == 'docs/assets/site.css'):
            raise ValueError('Source-package member outside its allowed scope')
        path = repository / name
        if path.resolve().relative_to(repository.resolve()).as_posix() != name:
            raise ValueError('Source-package member has an indirect path')
        if '__pycache__' in path.parts or path.suffix in {'.aux', '.log', '.out', '.zip', '.pyc'}:
            raise ValueError('Unexpected source-package member')
        if not path.is_file():
            raise ValueError('Missing source-package member: ' + name)
        if path.suffix == '.pdf' and path.resolve() not in current_editions:
            continue
        members.append((path, name))
    required = {'docs/courses/TR-BAKER/' + unit['source'] for unit in metadata['units']}
    required.update('docs/courses/TR-BAKER/sources/' + unit['internal_id'] + '.tex'
                    for unit in metadata['units'])
    if not required <= {name for _, name in members}:
        raise ValueError('Incomplete editable source package')
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
    validate_metadata(metadata)
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
