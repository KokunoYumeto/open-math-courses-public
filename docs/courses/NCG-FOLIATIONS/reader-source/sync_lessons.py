"""Regenerate selected NCG lesson pages from the sources on the current branch.

This deliberately does not assemble an archive or publish a site. Existing
section/result anchors and inherited component terms are retained.
"""
from __future__ import annotations

import argparse
from collections import Counter
import hashlib
import html
from html.parser import HTMLParser
import json
from pathlib import Path
import re
import sys
from urllib.parse import unquote, urlsplit


class PageIndex(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.ids = []
        self.math = []
        self.references = []
        self.headings = []
        self._heading = None

    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        if a.get('id'):
            self.ids.append(a['id'])
        if a.get('data-tex'):
            self.math.append(a['data-tex'])
        for key in ('href', 'src'):
            if key in a:
                self.references.append(a[key])
        if re.fullmatch('h[1-6]', tag):
            self._heading = {'tag': tag, 'ids': [], 'text': ''}
        if self._heading is not None and a.get('id'):
            self._heading['ids'].append(a['id'])

    def handle_data(self, data):
        if self._heading is not None:
            self._heading['text'] += data

    def handle_endtag(self, tag):
        if self._heading is not None and tag == self._heading['tag']:
            self.headings.append(self._heading)
            self._heading = None


def index(text):
    i = PageIndex()
    i.feed(text)
    return i


def sha(data):
    return hashlib.sha256(data).hexdigest().upper()


def normalized(text):
    return re.sub(r'\s+', ' ', text).strip()


def write_json(path, value):
    path.write_text(json.dumps(value, ensure_ascii=False, indent=2) + '\n', encoding='utf-8', newline='\n')


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument('--course', type=Path, default=Path(__file__).resolve().parent.parent)
    p.add_argument('--companions', action='store_true')
    p.add_argument('--companion-ids', nargs='*', default=[], help='Regenerate only the named companion lessons')
    p.add_argument('--kernel', action='store_true')
    p.add_argument('--lessons', nargs='*', default=[])
    p.add_argument('--report', type=Path)
    args = p.parse_args()
    course = args.course.resolve()
    adapter_dir = course / 'reader-source'
    sys.path[:0] = [str(adapter_dir), str(adapter_dir / 'vendor'), str(adapter_dir / 'reader')]
    from build_release import page, rebind_html
    from course_reader import render_markdown_math
    from course_assets import read_unit_assets

    metadata = json.loads((course / 'course.json').read_text(encoding='utf-8'))
    mf_path = adapter_dir / 'companion-inputs/manifest.json'
    manifest = json.loads(mf_path.read_text(encoding='utf-8'))
    entries = manifest['proof_files']
    aliases = {}
    rewrites = dict(manifest.get('projection_rewrites', {}))
    for row in entries:
        filename = Path(row['frozen_file']).name
        aliases[filename] = row['id'] + '.html'
        aliases[row['id'] + '.md'] = row['id'] + '.html'
        for url in row.get('replaces_retired_urls', []):
            rewrites[url] = row['id'] + '.html'
            rewrites[url.replace('open-mathematics-courses', 'open-math-courses')] = row['id'] + '.html'
    aliases['effros-borel-structure.md'] = 'the-effros-borel-structure.html'
    aliases['polish-spaces-and-standard-borel-spaces-the-full-appendix-of-vol-i.md'] = 'polish-spaces-and-standard-borel-spaces.html'
    aliases.update({
        'decomposable-operators-diagonal-algebra.md': '../../OA-FOUND-REMAINDER/reader/supplements/decomposable-operators-diagonal-algebra.html',
        'spatial-tensor-products.md': '../../OA-FOUND-REMAINDER/reader/supplements/spatial-tensor-products.html',
        'stone-weierstrass-c0.md': '../../function-algebras-and-approximation/the-stone-weierstrass-theorem-for-functions-vanishing-at-infinity.html',
    })
    aliases.update(manifest.get('local_link_aliases', {}))
    for u in metadata['units']:
        aliases[Path(u['source']).name] = '../' + u['id'] + '.html'

    # Preserve stable aliases attached to headings on the actual current page.
    # Bind by heading text instead of stale line numbers after proof additions.
    def heading_bindings(text, previous, fallback, explicit=None):
        old = {normalized(h['text']): h['ids'] for h in index(previous).headings}
        fallback_by_line = {r['line']: r['ids'] for r in fallback}
        result, used = [], set()
        additions = {r['line']: r['ids'] for r in explicit or []}
        for line, value in enumerate(text.splitlines(), 1):
            m = re.match(r'^#{1,6}\s+(.+)$', value)
            if not m:
                continue
            heading = index(render_markdown_math('# ' + m[1])).headings[0]['text']
            ids = list(old.get(normalized(heading), fallback_by_line.get(line, []) if not previous else []))
            ids.extend(additions.get(line, []))
            # Newly inserted numbered sections get the same readable aliases
            # used by existing title links in the course.
            section = re.match(r'^(\d+[A-Z]?)[.\s]', m[1])
            if section and m[1].startswith(section[1] + '.'):
                candidate = 'section-' + section[1].lower()
                if candidate not in ids and candidate not in used:
                    ids.insert(0, candidate)
            native = re.sub(r'[^\w-]+', '-', m[1].lower()).strip('-')
            if native and re.fullmatch(r'[A-Za-z0-9][A-Za-z0-9_.-]{0,100}', native) and native not in ids:
                ids.append(native)
            by_case = {}
            for a in ids:
                if a.lower() in used or not re.fullmatch(r'[A-Za-z0-9][A-Za-z0-9_.-]{0,100}', a):
                    continue
                if a.lower() not in by_case or a != a.lower():
                    by_case[a.lower()] = a
            ids = list(by_case.values())
            if ids:
                result.append({'line': line, 'ids': ids})
                used.update(a.lower() for a in ids)
        return result

    def current_links(rendered, output):
        # Every programme link resolves against this checkout, so changes of
        # repository spelling never resurrect retired URLs.
        def replace(m):
            value = html.unescape(m[1]).replace('open-mathematics-courses', 'open-math-courses')
            parts = urlsplit(value)
            root = 'https://kokunoyumeto.github.io/open-math-courses/'
            if value.startswith(root):
                local = course.parents[1] / unquote(parts.path.split('/open-math-courses/', 1)[1])
                if local.is_file():
                    import os
                    value = Path(os.path.relpath(local, output.parent)).as_posix()
                    if parts.fragment:
                        value += '#' + parts.fragment
            return 'href="' + html.escape(value, quote=True) + '"'
        return re.sub(r'href="([^"]*)"', replace, rendered)

    def local_routes(text, output, initial):
        routes = dict(initial)
        for reference in re.findall(r'(?<!!)\]\(([^)\s]+)\)', text):
            base = reference.split('#', 1)[0]
            if base and not urlsplit(base).scheme and (output.parent / unquote(base)).is_file():
                routes[base] = base
        return routes

    report = []
    public = json.loads((course / 'companions/manifest.json').read_text(encoding='utf-8'))
    if args.companions or args.companion_ids:
        unknown = set(args.companion_ids) - {row['id'] for row in entries}
        if unknown:
            raise ValueError('unknown companion ids: ' + ', '.join(sorted(unknown)))
        for row in entries:
            if args.companion_ids and row['id'] not in args.companion_ids:
                continue
            source = adapter_dir / 'companion-inputs' / row['frozen_file']
            data = source.read_bytes()
            source_name = source.name
            text = data.decode('utf-8')
            copied = course / 'companions/src' / source_name
            if copied.read_bytes() != data:
                raise ValueError('companion copies differ: ' + source_name)
            output = course / 'companions' / (row['id'] + '.html')
            previous = output.read_text(encoding='utf-8') if output.exists() else ''
            # All existing stable section anchors are recovered by heading.
            fallback = []
            if not previous:
                fallback = [{'line': r['line'], 'ids': [r['stable_section_anchor']]} for r in row['heading_anchor_map'] if r.get('stable_section_anchor')]
            anchors = heading_bindings(text, previous, fallback, row.get('heading_anchor_aliases'))
            png_rows = [r for r in manifest.get('figure_assets', []) if r.get('bound_source') == source_name and r['frozen_file'].endswith('.png')]
            assets = None
            if png_rows:
                import struct
                asset_rows = []
                for a in png_rows:
                    image = adapter_dir / 'companion-inputs' / a['frozen_file']
                    width, height = struct.unpack('>II', image.read_bytes()[16:24])
                    pub = a['suggested_companion_path']
                    asset_rows.append({'id': Path(pub).stem, 'path': a.get('markdown_path', pub), 'source': a['frozen_file'], 'source_sha256': a['sha256'], 'media_type': 'image/png', 'bytes': a['bytes'], 'width': width, 'height': height, 'authorship': {'kind': 'original', 'credit': 'Original course illustration', 'statement': 'Original illustration dedicated to CC0-1.0; component terms retained.'}, 'source_attribution': [row['source_title']]})
                assets = read_unit_assets(adapter_dir / 'companion-inputs', 'ncg-proof-companions', {'id': row['id'], 'source': row['frozen_file'], 'assets': asset_rows})
            routes = local_routes(text, output, aliases)
            outside = set()
            unresolved_bases = []
            for reference in re.findall(r'(?<!!)\]\(([^)\s]+)\)', text):
                base = reference.split('#', 1)[0]
                if base and not urlsplit(base).scheme and base not in routes and re.search(r'\.(?:md|html|py|svg|png|pdf)$', base, re.I):
                    marker = 'ancillary/' + sha(base.encode())[:16]
                    routes[base] = marker
                    outside.add(marker)
                    unresolved_bases.append(base)
            if outside:
                raise ValueError('unresolved prerequisite routes in ' + row['id'] + ': ' + repr(unresolved_bases))
            try:
                rendered = render_markdown_math(text, local_links=routes, heading_anchors=anchors, assets=assets)
            except ValueError as error:
                raise ValueError(row['id'] + ': ' + str(error)) from error
            def ancillary(match):
                return '<span>' + match[2] + '</span>' if html.unescape(match[1]).split('#', 1)[0] in outside else match[0]
            rendered = re.sub(r'<a href="([^"]*)">(.*?)</a>', ancillary, rendered, flags=re.S)
            # A historical title slug may exceed the renderer's finite bound
            # for authored IDs. Retain that harmless HTML alias as well.
            for binding in row.get('heading_anchor_aliases', []):
                extra = [a for a in binding['ids'] if len(a) > 101 and re.fullmatch(r'[A-Za-z0-9_.-]+', a)]
                anchor = next((a for a in anchors if a['line'] == binding['line']), None)
                if extra and anchor:
                    marker = '<span id="' + html.escape(anchor['ids'][0], quote=True) + '"></span>'
                    aliases_html = ''.join('<span id="' + html.escape(a, quote=True) + '"></span>' for a in extra)
                    rendered = re.sub(r'(<h[1-6] id="' + re.escape(anchor['ids'][0]) + r'">)', lambda m: m[1] + aliases_html, rendered, count=1)
            if assets is not None:
                rendered, _ = rebind_html(rendered, assets, rewrites)
            else:
                class EmptyAssets:
                    records = []
                rendered, _ = rebind_html(rendered, EmptyAssets(), rewrites)
            rendered = current_links(rendered, output)
            nav = '<nav><a href="../index.html">Course contents</a><a href="index.html">Companion readings</a><a href="src/' + source_name + '" download>Markdown source</a></nav>'
            rights = ''
            if row['licence'] == 'GFDL-1.2-only':
                rights = '<p>GNU Free Documentation License, Version 1.2 only; no Invariant Sections or Cover Texts. <a href="AN-03/RIGHTS.md">Rights</a> · <a href="AN-03/TITLE_PAGE.md">Title page</a> · <a href="AN-03/HISTORY.md">History</a> · <a href="AN-03/COPYING">Complete licence</a> · <a href="AN-03/HTML-PROJECTION.md">HTML adaptation notice</a>.</p>'
            footer = html.escape(row['licence']) + '. Source credits and component terms are retained. <a href="index.html">Companion readings and terms</a>.'
            if row.get('additional_projection_credit'):
                footer += ' ' + html.escape(row['additional_projection_credit'])
            output.write_text(page(row['source_title'], nav + rights + rendered, math=True, depth='../', footer=footer, mathtools=r'\begin{psmallmatrix}' in text), encoding='utf-8', newline='\n')
            # Retain existing result aliases supplied by main; result bindings
            # can be transferred by their immediately following paragraph.
            new_index = index(output.read_text(encoding='utf-8'))
            missing = set(index(previous).ids) - set(new_index.ids)
            report.append({'id': row['id'], 'math_spans': len(new_index.math), 'missing_old_ids': sorted(missing)})
            row.update(sha256=sha(data), bytes=len(data))
            headings = []
            for line, value in enumerate(text.splitlines(), 1):
                if re.match(r'^#{1,6}\s+', value):
                    stable = next((a for b in anchors if b['line'] == line for a in b['ids'] if a.startswith('section-')), None)
                    headings.append({'line': line, 'heading': re.sub(r'^#{1,6}\s+', '', value), 'stable_section_anchor': stable})
            row['heading_anchor_map'] = headings
            public.setdefault('published_source_files', {})['src/' + source_name] = {'sha256': sha(data), 'bytes': len(data)}
            public.setdefault('rendered_math', {})[row['id']] = {'formulas': len(new_index.math), 'math_tex_sha256': sha(json.dumps(new_index.math, ensure_ascii=False).encode()), 'source_sha256': sha(data), 'heading_bindings': anchors}
        public['proof_files'] = entries
        write_json(mf_path, manifest)
        write_json(course / 'companions/manifest.json', public)
        rows = []
        for row in entries:
            title = render_markdown_math(row['source_title']).removeprefix('<p>').removesuffix('</p>\n')
            rows.append('<li><a href="' + row['id'] + '.html">' + title + '</a> · <a href="src/' + Path(row['frozen_file']).name + '" download>Markdown source</a><br>' + html.escape(row['licence']) + '</li>')
        for row in manifest.get('additional_readings', []):
            rows.append('<li><a href="' + html.escape(row['reader'], quote=True) + '">' + html.escape(row['title']) + '</a> · <a href="' + html.escape(row['source'], quote=True) + '" download>Markdown source</a><br>' + html.escape(row['licence']) + '</li>')
        body = '<nav><a href="../index.html">Course contents</a><a href="../sources.html">Sources and terms</a></nav><h1>Companion readings</h1><p>These lessons provide the algebra, topology, analysis and measure theory used in the foliation course. Each reading retains its own source credits and licence.</p><ol>' + ''.join(rows) + '</ol><p>Applicable component notices are linked from the readings that use them.</p>'
        (course / 'companions/index.html').write_text(page('Companion readings', body, math=True, depth='../', footer='Consult each reading for its references, attribution and component terms.'), encoding='utf-8', newline='\n')

    for slug in args.lessons:
        unit = next(u for u in metadata['units'] if u['id'] == slug)
        text = (course / unit['source']).read_text(encoding='utf-8')
        output = course / (slug + '.html')
        previous = output.read_text(encoding='utf-8')
        anchors = heading_bindings(text, previous, unit['heading_anchors'])
        unit['heading_anchors'] = anchors
        assets = read_unit_assets(course, metadata['id'], unit)
        local = {Path(u['source']).name: u['id'] + '.html' for u in metadata['units']}
        local.update({'../' + a['href']: a['href'] for a in metadata.get('linked_files', [])})
        local = local_routes(text, output, local)
        core_rewrites = {key: ('companions/' + value if not value.startswith('../') else value[3:]) for key, value in rewrites.items()}
        rendered = render_markdown_math(text, local_links=local, heading_anchors=anchors, assets=assets)
        rendered, _ = rebind_html(rendered, assets, core_rewrites)
        rendered = current_links(rendered, output)
        nav = '<nav><a href="../../index.html">Open Mathematics Courses</a><a href="index.html">Course contents</a><a href="' + unit['source'] + '" download>Markdown source</a><a href="sources.html">Sources and terms</a></nav>'
        output.write_text(page(unit.get('title', slug), nav + rendered, math=True, mathtools=r'\begin{psmallmatrix}' in text), encoding='utf-8', newline='\n')
        data = (course / unit['source']).read_bytes()
        unit['sha256'] = sha(data)
        new_index = index(output.read_text(encoding='utf-8'))
        report.append({'id': slug, 'math_spans': len(new_index.math), 'missing_old_ids': sorted(set(index(previous).ids) - set(new_index.ids))})
    if args.lessons:
        write_json(course / 'course.json', metadata)
    if args.kernel:
        import struct
        folder = course / 'finite-kernel-prerequisite'
        text = (folder / 'READING.md').read_text(encoding='utf-8')
        output = folder / 'index.html'
        previous = output.read_text(encoding='utf-8') if output.exists() else ''
        asset_rows = []
        for name in ('density-refinement', 'positive-interchange', 'probability-codes'):
            source = 'figures/' + name + '.png'
            data = (folder / source).read_bytes()
            width, height = struct.unpack('>II', data[16:24])
            asset_rows.append({'id': name, 'path': source, 'source': source, 'source_sha256': sha(data), 'media_type': 'image/png', 'bytes': len(data), 'width': width, 'height': height, 'authorship': {'kind': 'original', 'credit': 'Original course illustration', 'statement': 'Original CC0 illustration; font/software terms retained in COMPONENT-TERMS.md.'}, 'source_attribution': ['Finite conditional expectations, measurable densities, and positive kernel integrals, ' + ('K.4A.' if name == 'probability-codes' else 'K.3 and K.4.')]})
        assets = read_unit_assets(folder, 'ncg-kernel', {'id': 'finite-kernel-prerequisite', 'source': 'READING.md', 'assets': asset_rows})
        fallback = [{'line': line, 'ids': ['k-' + m[1].lower()]} for line, value in enumerate(text.splitlines(), 1) if (m := re.match(r'^## K\.(\d+[A-Z]?) ', value))]
        rendered = render_markdown_math(text, local_links=local_routes(text, output, {'reproduce.py': 'reproduce.py'}), heading_anchors=heading_bindings(text, previous, fallback, fallback), assets=assets)
        rendered, _ = rebind_html(rendered, assets, {})
        nav = '<nav><a href="../index.html">Course contents</a><a href="../companions/index.html">Companion readings</a><a href="READING.md" download>Markdown source</a></nav>'
        footer = 'Original text and illustrations: <a href="LICENSE">CC0 1.0</a>. <a href="COMPONENT-TERMS.md">Font and software component terms</a> · <a href="README.md">Figure reproduction</a>.'
        output.write_text(page('Finite conditional expectations, measurable densities, and positive kernel integrals', nav + rendered, math=True, depth='../', footer=footer), encoding='utf-8', newline='\n')
        parsed = index(output.read_text(encoding='utf-8'))
        report.append({'id': 'finite-kernel-prerequisite', 'math_spans': len(parsed.math), 'missing_old_ids': sorted(set(index(previous).ids) - set(parsed.ids))})
    if args.report:
        write_json(args.report, report)
    print(json.dumps({'rendered': len(report), 'missing_old_ids': sum(len(r['missing_old_ids']) for r in report)}, ensure_ascii=False))


if __name__ == '__main__':
    main()
