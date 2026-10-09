"""Build the independent Collatz lesson and a matching offline source download.

Requires Python 3 and Pandoc. Uses native MathML; no JavaScript/CDN is needed.
No remote writes. The explicit file list excludes private records.
"""
from pathlib import Path
import hashlib
import html
import json
import re
import subprocess
import zipfile

ROOT = Path(__file__).resolve().parents[1]
ID = 'NT-COLLATZ-01'
FILES = [
    'index.html', ID+'.html', 'reader.css', 'COURSE.json', 'PROVENANCE.json',
    'src/'+ID+'.md', 'figures/three-clocks.svg',
    'build/build_reader.py', 'build/check_examples.py', 'checks/examples.json',
]


def write(path, text):
    target = ROOT / path
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(text, encoding='utf-8', newline='\n')


def shell(body, title, nav):
    return ('<!doctype html>\n<html lang="en"><head><meta charset="utf-8">'
            '<meta name="viewport" content="width=device-width,initial-scale=1">'
            '<title>'+html.escape(title)+'</title><link rel="stylesheet" href="reader.css">'
            '</head><body><a class="skip" href="#main">Skip to the lesson</a>'
            '<header>'+nav+'</header><main id="main">'+body+'</main>'
            '<footer>Original mathematical exposition and illustrations: '
            '<a href="https://creativecommons.org/publicdomain/zero/1.0/">CC0 1.0</a>. '
            'References retain their own authorship and terms.</footer></body></html>\n')


def main():
    source = (ROOT/'src'/f'{ID}.md').read_text(encoding='utf-8')
    built = subprocess.run(['pandoc', '-f', 'markdown+tex_math_single_backslash-implicit_figures', '-t', 'html5', '--mathml'],
                           input=source, text=True, encoding='utf-8', capture_output=True, check=True)
    if built.stderr.strip():
        raise RuntimeError(built.stderr)
    body = built.stdout.replace('src="../figures/', 'src="figures/')
    body = re.sub(r'(<math display="block"[\s\S]*?</math>)', r'<span class="math display">\1</span>', body)
    body = body.replace('<table>', '<div class="table-scroll"><table>').replace('</table>', '</table></div>')
    body = re.sub(r'(<p><img\b[^>]+></p>)', r'<div class="figure-scroll">\1</div>', body)
    if '<merror' in body or '<math' not in body:
        raise ValueError('Mathematical typesetting failed')
    write(ID+'.html', shell(body, 'Three clocks for one Collatz orbit',
          '<a href="index.html">Collatz clocks, coding and probability</a> · '
          '<a href="src/'+ID+'.md">Lesson source</a>'))
    overview = '''<h1>Collatz clocks, coding and probability</h1>
<p>The Collatz iteration connects elementary integer arithmetic with questions about coding and probability. These lessons develop exact changes of clock before considering how a distribution of starting integers moves under those changes.</p>
<h2>Read the opening lesson</h2>
<p><a href="NT-COLLATZ-01.html">Three clocks for one Collatz orbit</a> proves the exact time bijections between ordinary, shortcut and Syracuse iteration, reconstructs every omitted state, and proves equality of orbit minima. It includes worked timelines and four exercises with complete solutions.</p>
<p>The prerequisites are positive-integer arithmetic, induction and well-ordering. Every additional divisibility fact used in the lesson is proved there. The written proofs have been self-checked by GPT-6 Astra; the accompanying finite computations are not a formal certification of the general results.</p>
<h2>The planned continuation</h2>
<p>Parity words and affine composition will lead to logarithmic sampling on dyadic fibres, followed by first-passage maps and transport across scales. These three later lessons are not yet included. The elementary opening requires no probability; the planned sampling and transport lessons are at beginning-graduate level.</p>
<h2>Source and checks</h2>
<p>The <a href="../../downloads/NT-COLLATZ.zip">download</a> contains the available lesson, editable source and diagram, and reproducible finite checks. The lesson's proofs and literature citations can be read without running the checks or opening a research workbench.</p>
<p><a href="PROVENANCE.json">Authorship and mathematical references</a>.</p>'''
    write('index.html', shell(overview, 'Collatz clocks, coding and probability', 'Open Mathematics Courses'))
    checked = subprocess.run(['python', '-X', 'utf8', str(ROOT/'build/check_examples.py')],
                             capture_output=True, text=True, encoding='utf-8', check=True)
    result = json.loads(checked.stdout)
    assert result['passed']
    write('checks/examples.json', json.dumps(result, ensure_ascii=False, indent=2)+'\n')
    digest = lambda p: hashlib.sha256(p.read_bytes()).hexdigest()
    manifest = {'files':[{'path':p,'sha256':digest(ROOT/p)} for p in FILES],
                'math_expressions':body.count('<math'), 'reader_engine':'Pandoc native MathML'}
    write('checks/artifacts.json', json.dumps(manifest, indent=2)+'\n')
    archive = ROOT/'dist/NT-COLLATZ.zip'
    archive.parent.mkdir(exist_ok=True)
    with zipfile.ZipFile(archive, 'w', compression=zipfile.ZIP_DEFLATED) as z:
        for name in FILES+['checks/artifacts.json']:
            info = zipfile.ZipInfo('NT-COLLATZ/'+name, date_time=(2026,10,8,0,0,0))
            info.compress_type = zipfile.ZIP_DEFLATED
            z.writestr(info, (ROOT/name).read_bytes())
    with zipfile.ZipFile(archive) as z:
        assert z.testzip() is None
        for name in FILES+['checks/artifacts.json']:
            assert z.read('NT-COLLATZ/'+name) == (ROOT/name).read_bytes()
    print(json.dumps({'lesson':ID, 'math_expressions':manifest['math_expressions'],
                      'finite_checks':result, 'zip_sha256':digest(archive)}, indent=2))


if __name__ == '__main__':
    main()
