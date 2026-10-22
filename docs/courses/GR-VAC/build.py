"""Build the two mathematical readers from their editable Markdown sources.

Requires Python 3.10+ and markdown-it-py. Run beside lessons.json.
"""
from pathlib import Path
from html import escape
import json
import re
from markdown_it import MarkdownIt

ROOT = Path(__file__).resolve().parent
META = json.loads((ROOT / 'lessons.json').read_text(encoding='utf8'))
MATH = re.compile(r'\\\[(.*?)\\\]|\\\((.*?)\\\)', re.S)
NS = 'https://github.com/KokunoYumeto/open-math-courses/blob/a5c2b5e6acfc2ebd7a5d6ce63a5adb21071309ff/courses/NS-BLOWUP/README.md'
CSS = '''
:root{color-scheme:light;--ink:#13283a;--muted:#465d6c;--line:#d2e1e8;--link:#096984}
*{box-sizing:border-box}html{font-size:18px;scroll-behavior:smooth}
body{margin:0;background:#f2f6f8;color:var(--ink);font-family:Georgia,'Times New Roman',serif;line-height:1.65}
main{max-width:1050px;margin:0 auto;background:white;padding:42px 56px 70px}
h1,h2,h3,nav,.eyebrow{font-family:system-ui,sans-serif;line-height:1.25}
h1{font-size:2.1rem;letter-spacing:-.025em}h2{margin-top:2.5rem;font-size:1.42rem;border-top:1px solid var(--line);padding-top:1.1rem}
h3{margin-top:1.7rem;font-size:1.12rem}p{margin:.85rem 0}a{color:var(--link);text-underline-offset:3px;overflow-wrap:anywhere}
nav{font-size:.9rem;padding:18px 22px;background:#edf5f8;border-left:4px solid #2588a0;margin:1.6rem 0}
nav ol{margin:.3rem 0;padding-left:1.3rem}nav li{margin:.55rem 0}
.eyebrow{color:var(--muted);font-size:.8rem;letter-spacing:.08em;text-transform:uppercase}
.math.display{display:block;max-width:100%;overflow-x:auto;overflow-y:hidden;padding:.35rem 0}
.math.inline{overflow-wrap:normal}mjx-container[display=true]{margin:.75rem 0!important}
img{display:block;max-width:100%;height:auto;margin:1.5rem auto}
pre{overflow:auto;background:#edf3f6;padding:1rem}code{font-size:.86em}table{border-collapse:collapse;max-width:100%;display:block;overflow:auto}
th,td{border:1px solid var(--line);padding:.4rem .6rem}section.lesson{margin-top:3rem}
footer{margin-top:3rem;border-top:1px solid var(--line);padding-top:1rem;color:var(--muted);font-size:.85rem}
@media(max-width:650px){html{font-size:16px}main{padding:23px 18px 40px}h1{font-size:1.75rem}h2{font-size:1.3rem}.math.display{font-size:.94rem}}
@media(max-width:600px){mjx-container[display="true"],mjx-math[display="true"],mjx-mtable[side="right"]{min-width:0!important}mjx-mtable[side="right"]>mjx-table{margin-left:0!important;margin-right:0!important}mjx-mtable[side="right"]>mjx-labels{position:static!important;display:block!important;width:auto!important;text-align:right;margin-top:.65em}mjx-mtable[side="right"]>mjx-labels>mjx-itable{position:static!important;display:inline-table!important}mjx-mtable[side="right"]>mjx-labels>mjx-itable>mjx-mtr{height:auto!important}}
@media print{body{background:white}main{max-width:none;padding:0}nav{break-inside:avoid}h2,h3{break-after:avoid}img{max-height:70vh}a{color:inherit}.math.display{overflow:visible}}
'''

def render(source, prefix=''):
    text = source.read_text(encoding='utf8')
    maths = []
    def protect(match):
        value = match.group(1) if match.group(1) is not None else match.group(2)
        display = match.group(1) is not None
        token = f'VACUUMMATHTOKEN{len(maths):05d}END'
        maths.append((token, value.strip(), display))
        return token
    protected = MATH.sub(protect, text)
    engine = MarkdownIt('commonmark', {'html': False}).enable('table')
    tokens = engine.parse(protected)
    used = set()
    for i, token in enumerate(tokens):
        if token.type == 'heading_open':
            title = tokens[i+1].content
            slug = re.sub(r'[^a-z0-9]+', '-', title.lower()).strip('-')
            ident = prefix + slug
            if ident in used:
                raise ValueError('Repeated heading: ' + title)
            used.add(ident)
            token.attrSet('id', ident)
    body = engine.renderer.render(tokens, engine.options, {})
    for token, value, display in maths:
        left, right = (r'\[', r'\]') if display else (r'\(', r'\)')
        body = body.replace(token, '<span class="math '+('display' if display else 'inline')+'" data-tex="'+escape(value, quote=True)+'">'+left+escape(value)+right+'</span>')
    body = body.replace('src="../assets/', 'src="assets/').replace('href="../assets/', 'href="assets/')
    body = body.replace('href="../../NS-BLOWUP/README.md"', 'href="'+NS+'"')
    for lesson in META['lessons']:
        stem = Path(lesson['source']).stem
        body = body.replace('href="'+stem+'.md"', 'href="'+stem+'.html"')
    return body, len(maths)

def page(title, body, nav):
    return '''<!doctype html>
<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>'''+escape(title)+'''</title><style>'''+CSS+'''</style>
<script>window.MathJax={tex:{inlineMath:[['\\\\(','\\\\)']],displayMath:[['\\\\[','\\\\]']],tags:'ams',tagSide:'right'},options:{enableMenu:false},chtml:{displayAlign:'center'},startup:{typeset:true}};</script>
<script defer src="assets/mathjax/tex-chtml-full.js"></script></head>
<body><main><p class="eyebrow">Appendix to the forced Navier–Stokes blowup argument</p>'''+nav+body+'''
<footer>Lessons and diagrams written with GPT-6 Astra. Mathematical sources are cited in the lessons. <a href="README.md">Appendix contents and downloads</a>.</footer>
</main></body></html>'''

def main():
    assert (ROOT/'assets/mathjax/tex-chtml-full.js').is_file(), 'The accompanying MathJax runtime is required.'
    navigation = '<nav aria-label="Appendix lessons"><p><a href="'+escape(META['parent_reader'],quote=True)+'">The forced Navier–Stokes blowup argument</a></p><ol>'+''.join('<li><a href="'+Path(l['source']).stem+'.html">'+escape(l.get('label',l['id'])+': '+l['title'])+'</a></li>' for l in META['lessons'])+'</ol><p><a href="reader.html">Read both appendix lessons</a> · <a href="https://github.com/KokunoYumeto/open-math-courses/blob/main/courses/GR-VAC/GR-VAC-reader-and-source.zip">Offline reader and sources</a></p></nav>'
    cumulative = '<h1>'+escape(META['title'])+'</h1><p>'+escape(META['introduction'])+'</p>'+navigation
    stats = []
    for lesson in META['lessons']:
        p = ROOT/lesson['source']
        body, count = render(p)
        dest = ROOT/(p.stem+'.html')
        dest.write_text(page(lesson['title'], body, navigation), encoding='utf8')
        combined, _ = render(p, prefix=lesson['id']+'-')
        cumulative += '<section class="lesson" id="'+lesson['id']+'">'+combined+'</section>'
        stats.append({'id':lesson['id'], 'formulas':count, 'html':dest.name})
    (ROOT/'reader.html').write_text(page(META['title'], cumulative, ''), encoding='utf8')
    (ROOT/'START-HERE.html').write_text('<!doctype html><html lang="en"><meta charset="utf-8"><title>'+escape(META['title'])+'</title><h1>'+escape(META['title'])+'</h1><p>'+escape(META['introduction'])+'</p><p><a href="reader.html">Read both appendix lessons and their ten solved exercises</a>.</p><p><a href="README.md">Contents, sources and rebuilding instructions</a>.</p></html>\n',encoding='utf8')
    print(json.dumps({'lessons':stats, 'formulas':sum(x['formulas'] for x in stats)}))

if __name__ == '__main__':
    main()
