"""Rebuild this complete lesson from its unchanged Markdown. CC0 1.0.

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
        if base in config['link_projection']:
            link['href'] = config['link_projection'][base] + (separator + fragment if separator else '')
    return str(soup)


def page(title, content, config):
    return '''<!doctype html>
<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>''' + html.escape(title) + ''' · Open Mathematics Courses</title>
<meta name="description" content="Complete arguments, examples and four solved exercises in function algebras and uniform approximation.">
<link rel="stylesheet" href="assets/site.css">
<style>.lesson{max-width:76rem}.math-display{display:block;max-width:100%;overflow-x:auto;margin:1rem 0}mjx-container[display="true"]{max-width:100%;overflow-x:auto;overflow-y:hidden}pre{overflow:auto}a{overflow-wrap:anywhere}.course-note{max-width:76rem;margin:1rem auto}.toc{columns:2;column-gap:2rem}.toc li{break-inside:avoid;margin:.5rem 0}@media(max-width:650px){.toc{columns:1}}</style>
<script>window.MathJax={tex:{inlineMath:[['\\\\(','\\\\)']],displayMath:[['\\\\[','\\\\]']],processEscapes:true,macros:{Eta:'\\\\mathrm{H}'}},options:{ignoreHtmlClass:'no-math',processHtmlClass:'math'}};</script>
<script defer src="assets/mathjax/tex-chtml-full.js"></script></head>
<body class="no-math"><a class="skip-link" href="#main">Skip to content</a>
<header class="site-header"><div class="header-inner"><a class="brand" href="''' + config['site'] + '''">Open Mathematics Courses</a><nav class="primary-nav" aria-label="Course"><a href="index.html">Course</a><a href="LICENSING.html">Attribution and terms</a><a href="''' + config['download_url'] + '''">Download reader and sources</a></nav></div></header>
<main id="main">''' + content + '''</main><footer class="course-note"><a href="index.html">Function algebras and approximation</a> · <a href="provenance.json">Sources and authorship</a> · <a href="dependencies.json">Exact prerequisites</a></footer></body></html>
'''


def main():
    config = read('render-config.json')
    source = (ROOT / config['source']).read_bytes()
    if hashlib.sha256(source).hexdigest() != config['source_sha256']:
        raise ValueError('The source differs from this edition. Update its edition record before rebuilding.')
    body = render(source.decode('utf-8-sig'), config)
    lesson = '<article class="lesson">' + body + '</article><p class="course-note"><a href="' + config['source'] + '">Editable Markdown source</a></p>'
    (ROOT / config['reader']).write_text(page(config['lesson_title'], lesson, config), encoding='utf-8', newline='\n')
    headings = BeautifulSoup(body, 'html.parser').select('h2')
    toc = '<ol class="toc">' + ''.join('<li><a href="' + config['reader'] + '#' + h['id'] + '">' + html.escape(h.get_text(' ', strip=True)) + '</a></li>' for h in headings) + '</ol>'
    introduction = '<article class="lesson"><h1>Function algebras and approximation</h1><p>A complete lesson on uniform approximation by algebras of functions on locally compact Hausdorff spaces, without countability or metrizability assumptions.</p><p>Includes the real and complex Stone–Weierstrass theorems, compactification, Urysohn’s lemma, lattice approximation, Bernstein polynomials, Korovkin’s theorem, the disc algebra, integer coefficients, and four exercises with solutions.</p><p><a href="' + config['reader'] + '">Read the complete lesson</a> · <a href="' + config['download_url'] + '">Download the reader and editable sources</a></p><h2>Contents</h2>' + toc + '<h2>Authorship and prerequisites</h2><p>' + html.escape(config['authorship']) + '</p><p>The lesson gives exact proof locators in the programme’s hosted <a href="' + config['site'] + 'https://www.jirka.org/ra/">Basic Analysis I &amp; II by Jiří Lebl</a> and the core <a href="https://kokunoyumeto.github.io/program-matematika-indonesia/en/courses/B10/reader/">Discrete Mathematics by Oscar Levin</a>. The terminology remark about holomorphic functions links to the published Cauchy-theorem lesson.</p><p>English · original exposition under CC0 1.0 · historical sources retain their credit and rights.</p><p><a href="LICENSING.html">Attribution and component terms</a></p></article>'
    (ROOT / 'index.html').write_text(page('Function algebras and approximation', introduction, config), encoding='utf-8', newline='\n')
    licence = '<article class="lesson"><h1>Attribution and component terms</h1><p>' + html.escape(config['authorship']) + '</p><p>The original mathematical exposition is dedicated to the public domain under <a href="LICENSE-CC0.txt">CC0 1.0</a>. Human mathematical sources remain credited in the lesson’s full references.</p><p>Jiří Lebl’s <i>Basic Analysis I &amp; II</i> and Oscar Levin’s <i>Discrete Mathematics: An Open Introduction</i> are the texts of the core courses Real Analysis I and II and Proof, Logic, and Discrete Structures, freely available at their authors’ sites. This package links their exact proofs and does not reproduce their text. Historical and comparative citations retain their respective rights; free access is not a redistribution grant.</p><p>The reader was packaged by GPT-6 Astra (OpenAI), Ultra, October 2026. It includes the complete October 2026 lesson, programme links to its prerequisites, navigation and an offline download. Packaging does not constitute an independent mathematical review. New packaging code is CC0 1.0.</p><p>MathJax and its bundled fonts retain their <a href="assets/mathjax/LICENSE">software licence</a> and accompanying notices. The source renderer uses separately installed markdown-it-py (MIT) and Beautiful Soup (MIT); see requirements.txt.</p><p><a href="provenance.json">Detailed source and authorship record</a> · <a href="index.html">Read the course</a></p></article>'
    (ROOT / 'LICENSING.html').write_text(page('Attribution and component terms', licence, config), encoding='utf-8', newline='\n')


if __name__ == '__main__':
    main()
