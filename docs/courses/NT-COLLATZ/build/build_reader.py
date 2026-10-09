"""Build four lessons and a matching offline download with Pandoc native MathML.
The explicit release list excludes private records. No remote writes.
"""
from pathlib import Path
import hashlib
import html
import json
import re
import subprocess
import sys
import zipfile

ROOT = Path(__file__).resolve().parents[1]


def write(path, text):
    target = ROOT / path
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(text, encoding='utf-8', newline='\n')


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


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
    course = json.loads((ROOT/'COURSE.json').read_text(encoding='utf-8'))
    files = ['index.html', 'reader.css', 'COURSE.json', 'PROVENANCE.json',
             'figures/three-clocks.svg', 'build/build_reader.py',
             'build/check_examples.py', 'build/check_pathway.py',
             'checks/examples.json', 'checks/pathway.json']
    readers = []
    for i, lesson in enumerate(course['lessons']):
        source = (ROOT/lesson['source']).read_text(encoding='utf-8')
        built = subprocess.run(
            ['pandoc', '-f', 'markdown+tex_math_single_backslash-implicit_figures',
             '-t', 'html5', '--mathml'], input=source, text=True,
            encoding='utf-8', capture_output=True, check=True)
        if built.stderr.strip():
            raise RuntimeError(built.stderr)
        body = built.stdout.replace('src="../figures/', 'src="figures/')
        for other in course['lessons']:
            body = body.replace('href="'+other['id']+'.md', 'href="'+other['reader'])
        body = re.sub(r'(<math display="block"[\s\S]*?</math>)',
                      r'<span class="math display">\1</span>', body)
        body = body.replace('<table>', '<div class="table-scroll"><table>').replace('</table>', '</table></div>')
        body = re.sub(r'(<p><img\b[^>]+></p>)', r'<div class="figure-scroll">\1</div>', body)
        if '<merror' in body or '<math' not in body:
            raise ValueError('Mathematical typesetting failed: '+lesson['id'])
        nav = '<a href="index.html">'+html.escape(course['title'])+'</a> · '
        nav += '<a href="'+lesson['source']+'">Lesson source</a>'
        nextlinks = []
        if i:
            p = course['lessons'][i-1]
            nextlinks.append('<a href="'+p['reader']+'">Previous: '+html.escape(p['title'])+'</a>')
        if i+1 < len(course['lessons']):
            n = course['lessons'][i+1]
            nextlinks.append('<a href="'+n['reader']+'">Next: '+html.escape(n['title'])+'</a>')
        body += '<nav aria-label="Lesson sequence"><p>'+'<br>'.join(nextlinks)+'</p></nav>'
        write(lesson['reader'], shell(body, lesson['title'], nav))
        files.extend([lesson['reader'], lesson['source']])
        readers.append({'id':lesson['id'], 'math_expressions':body.count('<math'),
                        'source_words':len(source.split())})
    overview = '''<h1>Discrete dynamics, coding and probability</h1>
<p>A dynamical system can be described by its successive states, by the branches it follows, or by the distributions obtained from many starting points. These descriptions retain different information. This sequence develops the maps between them and proves exactly what each preserves.</p>
<p>The Collatz iteration is a sustained case study, not the endpoint of the course. Its elementary definition makes it possible to see return maps, symbolic coding, congruence counting and probability transport working together. Other examples separate the general mechanisms from the unresolved conjecture.</p>
<h2>Four lessons</h2>
<ol>
<li><a href="NT-COLLATZ-01.html">Return maps and exact changes of clock</a> proves a general return-clock theorem, then reconstructs ordinary, shortcut and odd-return Collatz trajectories. It identifies when deleting states does and does not preserve an orbit minimum.</li>
<li><a href="NT-COLLATZ-02.html">Symbolic itineraries and affine composition</a> derives exact branch coordinates, proves that finite parity words correspond to residue classes, and obtains a finite probability law by counting these classes.</li>
<li><a href="NT-COLLATZ-03.html">Pushforward measures and logarithmic sampling</a> proves composition and contraction of transported measures, then calculates the effect of the odd-part projection on uniform and logarithmic sampling. The density conclusions do not require density limits to exist.</li>
<li><a href="NT-COLLATZ-04.html">First passage and transport across scales</a> constructs entrance maps, identifies their kernels and images, and proves finite-chain and summable-scale bounds for orbit minima.</li>
</ol>
<p>Each lesson contains complete written arguments, worked examples, and four exercises with solutions. The specialised results used later are proved here or linked to a preceding lesson.</p>
<h2>Two ways to read</h2>
<p>For the connected Collatz case study, read all four in order. For the general subjects, begin with return maps; continue to the second lesson for coding and arithmetic, or to the third and fourth for probability transport. These are routes through the same lessons, not separate courses.</p>
<p>The first two lessons assume positive-integer arithmetic, induction, well-ordering and division with remainder. The later lessons also use elementary limits, completeness of the real numbers, logarithms and integration of elementary functions. They develop the needed countable probability and transport arguments explicitly.</p>
<h2>Where the sequence leads</h2>
<p>Induced dynamics, symbolic dynamics, arithmetic density and probability theory provide the broader mathematical homes for these lessons. The last lesson makes clear how mixing and renewal estimates can feed into an orbit-minimum theorem. Those analytic estimates, including the deep estimates in Tao’s work, are further study; this sequence proves the transport mechanism rather than claiming to supply the whole argument or a solution of the conjecture.</p>
<h2>Read, study and reproduce</h2>
<p>The <a href="../../downloads/NT-COLLATZ.zip">offline download</a> contains all four readers, editable lesson sources, the clock diagram and reproducible exact finite checks. After extracting it, open the included index.html. The general results are established by the written proofs, not by a finite computation. The writing AI has self-checked the lessons; no independent review or Lean certification is claimed.</p>
<p><a href="PROVENANCE.json">Authorship and mathematical references</a>.</p>'''
    write('index.html', shell(overview, course['title'], 'Open Mathematics Courses'))
    checks = {}
    for stem in ['examples', 'pathway']:
        checked = subprocess.run([sys.executable, '-X', 'utf8', str(ROOT/'build'/('check_'+stem+'.py'))],
                                 capture_output=True, text=True, encoding='utf-8', check=True)
        checks[stem] = json.loads(checked.stdout)
        assert checks[stem]['passed']
        write('checks/'+stem+'.json', json.dumps(checks[stem], ensure_ascii=False, indent=2)+'\n')
    for name in ['index.html']+[x['reader'] for x in course['lessons']]:
        text = (ROOT/name).read_text(encoding='utf-8')
        for link in re.findall(r'(?:href|src)="([^"]+)"', text):
            if ':' in link or link.startswith('#') or link == course['download']:
                continue
            path = html.unescape(link.split('#')[0])
            assert (ROOT/path).is_file(), (name, path)
    manifest = {'files':[{'path':p,'sha256':digest(ROOT/p)} for p in files],
                'readers':readers, 'reader_engine':'Pandoc native MathML',
                'local_links_checked':True}
    write('checks/artifacts.json', json.dumps(manifest, indent=2)+'\n')
    archive = ROOT/'dist/NT-COLLATZ.zip'
    archive.parent.mkdir(exist_ok=True)
    with zipfile.ZipFile(archive, 'w', compression=zipfile.ZIP_DEFLATED) as z:
        for name in files+['checks/artifacts.json']:
            info = zipfile.ZipInfo('NT-COLLATZ/'+name, date_time=(2026,10,9,0,0,0))
            info.compress_type = zipfile.ZIP_DEFLATED
            z.writestr(info, (ROOT/name).read_bytes())
    with zipfile.ZipFile(archive) as z:
        assert z.testzip() is None
        for name in files+['checks/artifacts.json']:
            assert z.read('NT-COLLATZ/'+name) == (ROOT/name).read_bytes()
    print(json.dumps({'readers':readers, 'finite_checks':checks,
                      'zip_sha256':digest(archive)}, indent=2))


if __name__ == '__main__':
    main()
