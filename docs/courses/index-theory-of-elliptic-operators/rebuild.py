"""Rebuild this selected-lesson edition from its Markdown sources. CC0 1.0.

Packaging code by GPT-6 Astra (OpenAI), Ultra, October 2026.
The lesson's mathematical authorship and historical checking are unchanged.
Install the two dependencies in requirements.txt, then run python rebuild.py.
"""
from pathlib import Path
import hashlib
import html
import json
import re
from markdown_it import MarkdownIt
from bs4 import BeautifulSoup

ROOT = Path(__file__).resolve().parent


def read(name):
    return json.loads((ROOT / name).read_text(encoding='utf-8'))


def render(source, config):
    md = MarkdownIt('commonmark', {'html': False})
    delimiters = ((r'\[', r'\]'), (r'\(', r'\)'), ('$$', '$$'), ('$', '$'))

    def inline(state, silent):
        for opening, closing in delimiters:
            if not state.src.startswith(opening, state.pos):
                continue
            end = state.src.find(closing, state.pos + len(opening))
            while end > 0 and state.src[end - 1] == '\\':
                end = state.src.find(closing, end + len(closing))
            if end < 0:
                return False
            if not silent:
                token = state.push('lesson_math', '', 0)
                token.content = state.src[state.pos:end + len(closing)]
            state.pos = end + len(closing)
            return True
        return False

    def block(state, start, end, silent):
        if state.sCount[start] - state.blkIndent >= 4:
            return False
        first = state.src[state.bMarks[start] + state.tShift[start]:state.eMarks[start]]
        for opening, closing in ((r'\[', r'\]'), ('$$', '$$')):
            if not first.startswith(opening):
                continue
            raw, stop = first, start
            while raw.find(closing, len(opening)) < 0:
                stop += 1
                if stop >= end:
                    return False
                raw += '\n' + state.src[state.bMarks[stop] + state.tShift[stop]:state.eMarks[stop]]
            at = raw.find(closing, len(opening))
            if raw[at + len(closing):].strip():
                return False
            if silent:
                return True
            token = state.push('lesson_math', '', 0)
            token.content, token.block, token.map = raw, True, [start, stop + 1]
            state.line = stop + 1
            return True
        return False

    def formula(tokens, index, options, env):
        raw = tokens[index].content
        display = ' math-display' if raw.startswith((r'\[', '$$')) else ''
        return '<span class="math' + display + '" data-tex="' + html.escape(raw, quote=True) + '">' + html.escape(raw) + '</span>' + ('\n' if tokens[index].block else '')

    md.inline.ruler.before('escape', 'lesson_math', inline)
    md.block.ruler.after('fence', 'lesson_math', block, {'alt': ['paragraph', 'reference', 'blockquote', 'list']})
    md.renderer.rules['lesson_math'] = formula
    tokens = md.parse(source)
    heading_ids = {row['line']: row['ids'] for row in config['heading_anchors']}
    aliases = {}
    for i, token in enumerate(tokens):
        if token.type == 'heading_open':
            slug = re.sub(r'[^\w-]+', '-', tokens[i + 1].content.lower()).strip('-')
            ids = heading_ids.get(token.map[0] + 1, [])
            token.attrSet('id', ids[0] if ids else slug)
            aliases[i] = sorted(set([slug] + [a for value in ids for a in (value, value.lower())]) - {ids[0] if ids else slug})

    def heading(tokens, index, options, env):
        return md.renderer.renderToken(tokens, index, options, env) + ''.join('<span id="' + html.escape(value, quote=True) + '"></span>' for value in aliases.get(index, []))

    md.renderer.rules['heading_open'] = heading
    soup = BeautifulSoup(md.renderer.render(tokens, md.options, {}), 'html.parser')
    for link in soup.select('a[href]'):
        value = link['href']
        base, separator, fragment = value.partition('#')
        if base in config.get('unavailable_downstream', []):
            link.name = 'span'
            link.attrs = {'class': 'unavailable-reading', 'title': 'Onward reading — not yet published in this edition'}
            continue
        if base in config['link_projection']:
            link['href'] = config['link_projection'][base] + (separator + fragment if separator else '')
    return str(soup)


def page(title, content, config):
    return '''<!doctype html>
<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>''' + html.escape(title) + ''' · Open Mathematics Courses</title>
<meta name="description" content="''' + html.escape(config['scope'], quote=True) + '''">
<link rel="stylesheet" href="assets/site.css">
<style>.lesson{max-width:76rem}.math-display{display:block;max-width:100%;overflow-x:auto;margin:1rem 0}mjx-container[display="true"]{max-width:100%;overflow-x:auto;overflow-y:hidden}pre{overflow:auto}a{overflow-wrap:anywhere}.course-note{max-width:76rem;margin:1rem auto;padding:0 1rem}.toc{columns:2;column-gap:2rem;list-style:none;padding:0}.toc li{break-inside:avoid;margin:.5rem 0}.unavailable-reading{text-decoration:underline dotted;text-underline-offset:3px}@media(max-width:650px){.toc{columns:1}}</style>
<script>window.MathJax={tex:{inlineMath:[['\\\\(','\\\\)']],displayMath:[['\\\\[','\\\\]']],processEscapes:true,macros:{Eta:'\\\\mathrm{H}'}},options:{ignoreHtmlClass:'no-math',processHtmlClass:'math'}};</script>
<script defer src="assets/mathjax/tex-chtml-full.js"></script></head>
<body class="no-math"><a class="skip-link" href="#main">Skip to content</a>
<header class="site-header"><div class="header-inner"><a class="brand" href="''' + config['site'] + '''">Open Mathematics Courses</a><nav class="primary-nav" aria-label="Course"><a href="index.html">Selected lessons</a><a href="prerequisites.html">Prerequisites</a><a href="LICENSING.html">Attribution and terms</a><a href="''' + config['download_url'] + '''">Download reader and sources</a></nav></div></header>
<main id="main">''' + content + '''</main><footer class="course-note"><a href="index.html">''' + html.escape(config['title']) + '''</a> · <a href="provenance.json">Sources and authorship</a> · <a href="dependencies.json">Exact prerequisites</a></footer></body></html>
'''


def main():
    config = read('render-config.json')
    contents = []
    for lesson in config['lessons'] + config.get('supporting_readings', []):
        source = (ROOT / lesson['source']).read_bytes()
        if hashlib.sha256(source).hexdigest() != lesson['source_sha256']:
            raise ValueError('Source differs from the recorded edition: ' + lesson['source'])
        body = render(source.decode('utf-8-sig'), lesson)
        intro = '<aside class="course-note">' + lesson.get('reader_note_html', '') + '</aside>'
        content = intro + '<article class="lesson">' + body + '</article><p class="course-note"><a href="' + lesson['source'] + '">Editable Markdown source</a></p>'
        (ROOT / lesson['reader']).write_text(page(lesson['title'], content, config), encoding='utf-8', newline='\n')
        headings = BeautifulSoup(body, 'html.parser').select('h2')
        contents.append('<h2><a href="' + lesson['reader'] + '">' + html.escape(lesson['title']) + '</a></h2><ul class="toc">' + ''.join('<li><a href="' + lesson['reader'] + '#' + h['id'] + '">' + html.escape(h.get_text(' ', strip=True)) + '</a></li>' for h in headings) + '</ul>')
    introduction = '<article class="lesson"><h1>' + html.escape(config['title']) + '</h1><p>' + html.escape(config['scope']) + '</p><p>This edition contains ' + str(len(config['lessons'])) + ' complete selected lesson' + ('s' if len(config['lessons']) > 1 else '') + '; it is not the complete parent course.</p><p>' + html.escape(config['authorship']) + '</p><p><a href="prerequisites.html">Prerequisites and supporting reading</a> · <a href="' + config['download_url'] + '">Download the reader and editable sources</a></p>' + ''.join(contents) + '<h2>Sources and terms</h2><p>English · original exposition under CC0 1.0 · human sources retain their credit and terms.</p><p><a href="LICENSING.html">Attribution and component terms</a></p></article>'
    (ROOT / 'index.html').write_text(page(config['title'], introduction, config), encoding='utf-8', newline='\n')
    for name, title, content in [('LICENSING.html', 'Attribution and component terms', config['licensing_html']), ('prerequisites.html', 'Prerequisites and supporting reading', config['prerequisites_html'])]:
        (ROOT / name).write_text(page(title, '<article class="lesson"><h1>' + title + '</h1>' + content + '</article>', config), encoding='utf-8', newline='\n')


if __name__ == '__main__':
    main()

