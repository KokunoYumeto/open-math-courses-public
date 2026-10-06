"""Rebuild this course's reader, editable TeX and portable sources only."""
from pathlib import Path
import hashlib, html, json, re, shutil, subprocess, sys, zipfile
root=Path(__file__).resolve().parent
sys.path.insert(0,str(root/'renderer'))
from course_reader import read_catalog,render_markdown_math
from course_assets import asset_output_path
load=lambda p:json.loads(p.read_text(encoding='utf-8'))
save=lambda p,x:p.write_text(json.dumps(x,ensure_ascii=False,indent=2)+'\n',encoding='utf-8',newline='\n')
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest().upper()
h=lambda x:html.escape(str(x),quote=True)
catalog=load(root/'catalogue.json');course=catalog['courses'][0]
for u in course['units']:u['source_sha256']=sha(root/u['source'])
save(root/'catalogue.json',catalog)
payload,sources=read_catalog(root/'catalogue.json')
solution_count=sum(len(re.findall(r'^\*\*Solution\.',(root/u['source']).read_text(encoding='utf-8'),re.M)) for u in course['units'])
if solution_count!=108:raise ValueError('The requested 108 exercise solutions must be preserved')
css='''body{margin:0;background:#f6f7f3;color:#172b28;font:18px/1.65 Georgia,serif}header,footer{background:#173e37;color:white;padding:1.1rem max(1.2rem,calc((100vw - 960px)/2))}header a,footer a{color:white}main{max-width:960px;margin:2rem auto;padding:0 1.3rem 3rem}h1,h2,h3,nav{font-family:system-ui,sans-serif}h1{font-size:2.1rem;line-height:1.2}h2{font-size:1.5rem;margin-top:2.2rem}a{color:#006459;text-underline-offset:3px}nav{font-size:1rem;display:flex;gap:.9rem;flex-wrap:wrap}li{margin:.5rem 0}img{max-width:100%;height:auto}table{display:block;max-width:100%;overflow:auto;border-collapse:collapse}th,td{padding:.4rem;border:1px solid #bac8c0}mjx-container[display=true],.math-display{display:block;max-width:100%;overflow-x:auto;overflow-y:hidden;padding:.4rem 0}pre{overflow:auto;background:#edf0ea;padding:1rem}code{font-size:.85em;overflow-wrap:anywhere}figure{margin:2rem 0}figcaption{font-size:1rem}@media(max-width:600px){body{font-size:17px}main{padding:0 1rem 2rem}h1{font-size:1.7rem}}'''
(root/'assets/reader.css').write_text(css,encoding='utf-8')
def page(title,body,nav=''):
    return '<!doctype html>\n<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>'+h(title)+' · Cohomology of quasi-coherent sheaves</title><link rel="stylesheet" href="assets/reader.css"><script>window.MathJax={tex:{inlineMath:[["\\\\(","\\\\)"],["$","$"]],displayMath:[["\\\\[","\\\\]"],["$$","$$"]],processEscapes:true},options:{skipHtmlTags:["script","noscript","style","textarea","pre","code"]}};</script><script defer src="assets/mathjax/tex-chtml-full.js"></script></head><body><header><nav><a href="../../">Open Mathematics Courses</a><a href="index.html">Cohomology of quasi-coherent sheaves</a><a href="prerequisites.html">Prerequisites and proofs</a></nav></header><main>'+nav+body+'</main><footer><nav><a href="sources.html">Human sources</a><a href="licensing.html">Authorship and component terms</a><a href="complete-source.zip">Editable source archive</a></nav><p>Written and self-checked by GPT-6.1 Sol (OpenAI), Codex, Ultra, October 2026. English edition.</p></footer></body></html>\n'
providers=load(root/'PROVIDER_HANDOFF.json') if (root/'PROVIDER_HANDOFF.json').exists() else {'providers':[]}
for i,u in enumerate(course['units']):
    slug=u['id'];body=sources[('AG-QC',slug)]['html']
    # Stable aliases identify course lessons and exact consumed theorem proofs.
    body='<span id="AG-QC-'+str(i+1).zfill(2)+'"></span>'+body
    for row in providers['providers']:
        if row['source']!=u['source']:continue
        label=row['proof_label'];pattern=r'<p><strong>'+re.escape(label)+r'(?=[. (])'
        anchors=''.join('<span id="'+h(alias)+'"></span>' for alias in row.get('aliases',[]))
        body,count=re.subn(pattern,anchors+'<p><strong>'+label,body,count=1)
        if count!=1:raise ValueError('Missing actual proof label '+label)
    links=['<a href="src/'+slug+'.md">Markdown</a>','<a href="files/'+slug+'.tex">LaTeX</a>']
    if i:links.insert(0,'<a href="'+course['units'][i-1]['id']+'.html">Previous</a>')
    if i+1<len(course['units']):links.append('<a href="'+course['units'][i+1]['id']+'.html">Next</a>')
    (root/(slug+'.html')).write_text(page(u['title'],body,'<nav>'+''.join(links)+'</nav>'),encoding='utf-8',newline='\n')
    # Stable numeric aliases also serve downstream records using course IDs.
    alias='AG-QC-'+str(i+1).zfill(2)+'.html'
    (root/alias).write_text(page(u['title'],body,'<nav>'+''.join(links)+'</nav>'),encoding='utf-8',newline='\n')
    for a in u.get('assets',[]):
        target=root/asset_output_path('AG-QC',slug,a).split('/',2)[2]
        target.parent.mkdir(parents=True,exist_ok=True);shutil.copyfile(root/a['source'],target)
    tex=root/'files'/(slug+'.tex')
    subprocess.run(['pandoc',str(root/u['source']),'--from=markdown+tex_math_single_backslash','--to=latex','--standalone','--pdf-engine=pdflatex','--template',str(root/'latex-template.tex'),'-o',str(tex)],check=True)
def normalize(p):
    s=p.read_text(encoding='utf-8').replace(r'{\def\LTcaptype{none} % do not increment counter','{')
    s=re.sub(r'\\includegraphics\[keepaspectratio,alt=\{[^{}]*\}\]',r'\\includegraphics[width=0.95\\linewidth,keepaspectratio]',s)
    # Pandoc drops a numeric prefix when deriving TeX heading identifiers.
    # Resolve only against a label actually emitted in this TeX document.
    labels=set(re.findall(r'\\label\{([^}]+)\}',s))
    def local_reference(match):
        target=match.group(1)
        shorter=re.sub(r'^\d+-','',target)
        if target not in labels and shorter in labels:
            return r'\hyperref['+shorter+']'
        return match.group(0)
    s=re.sub(r'\\hyperref\[([^]]+)\]',local_reference,s)
    if p.name in {'the-theorem-on-formal-functions.tex','zariski-connectedness-and-stein-factorization.tex','the-right-adjoint-of-derived-pushforward.tex','course.tex'}:
        notice = (r'\clearpage\section*{Copyright and licence of Stacks adaptations}' + '\n'
            + 'The identified Stacks proof adaptations retain the authorship of the Stacks project authors and AI Integrated Stacks Project contributors. '
            + 'Adaptations and added exposition by GPT-6.1 Sol (OpenAI), Codex, Ultra, 5 October 2026. '
            + 'Permission is granted to copy, distribute and/or modify these identified components under the GNU Free Documentation License, Version 1.2 or any later version published by the Free Software Foundation; '
            + 'with no Invariant Sections, no Front-Cover Texts, and no Back-Cover Texts. Independently authored portions retain their stated CC0 terms. '
            + 'A copy of the licence follows.\n\n'
            + r'\begingroup\footnotesize'+'\n'+r'\begin{verbatim}'+'\n'
            + (root/'COPYING-GFDL-1.2.txt').read_text(encoding='utf-8')+'\n'
            + r'\end{verbatim}\endgroup'+'\n')
        s=s.replace(r'\end{document}',notice+r'\end{document}')
    p.write_text(s,encoding='utf-8',newline='\n')
for p in (root/'files').glob('*.tex'):normalize(p)
body=render_markdown_math((root/'course-introduction.md').read_text(encoding='utf-8'),local_links={'prerequisites.html':'prerequisites.html',**{route:route for route in course.get('programme_links',[])}})
body+='<h2>Lessons</h2><ol>'+''.join('<li><a href="'+u['id']+'.html">'+h(u['title'])+'</a></li>' for u in course['units'])+'</ol><h2>Editable sources</h2><p><a href="complete-source.zip">Complete reader and source archive</a> · <a href="files/course.tex">Complete LaTeX</a> · <a href="PROVIDER_HANDOFF.json">Exact proof providers</a></p>'
(root/'index.html').write_text(page(course['title'],body),encoding='utf-8',newline='\n')
refs=['<h1>Human sources</h1>']
for s in load(root/'SOURCES.json')['sources']:
    refs.append('<section><h2>'+h(s.get('title',s.get('key','Source')))+'</h2><p>'+h(s.get('authors',s.get('author','')))+'. '+h(s.get('version',s.get('commit','')))+'.</p>')
    url=s.get('url',s.get('reading_url'))
    if url:refs.append('<p><a href="'+h(url)+'">Read the source</a></p>')
    refs.append('</section>')
refs.append('<p><a href="SOURCES.json">Source editions</a> · <a href="COMPONENTS.json">Component terms</a></p>')
(root/'sources.html').write_text(page('Human sources',''.join(refs)),encoding='utf-8',newline='\n')
licence='<h1>Authorship and component terms</h1><p>The independently authored teaching, examples, exercise solutions and original figures by GPT-6.1 Sol (OpenAI), Codex, Ultra, use <a href="https://creativecommons.org/publicdomain/zero/1.0/">CC0 1.0</a>. The writing AI performed its self-check; independent review is not claimed.</p><h2>Demailly and Siegel: preparation and division</h2><p>The full germ-level preparation-and-division proof in <a href="complex-analytic-spaces-and-analytification.html#2-local-analytic-algebra">Complex analytic spaces and analytification</a> adapts Jean-Pierre Demailly’s <i>Complex Analytic and Differential Geometry</i>, 21 June 2012, II, Theorems2.1 and2.3, pp79–81. Demailly credits C. L. Siegel’s contour argument. It retains the author’s <a href="https://www-fourier.univ-grenoble-alpes.fr/~demailly/documents.html">custom OpenContent permission</a> to distribute and modify on the web while retaining authorship; this component is outside CC0. GPT-6.1 Sol reorganized the germ proof and made the unit case, root multiplicities, joint holomorphicity and uniqueness explicit. The additional uniform norm estimates are not included.</p><h2>Stacks proof adaptations</h2><p>The conductor and strong-transcendence appendix in <a href="the-theorem-on-formal-functions.html#appendix-z-conductor-coefficients-and-strong-transcendence">The theorem on formal functions</a>, the approximation appendix in <a href="zariski-connectedness-and-stein-factorization.html#appendix-a-approximation-and-connectedness-over-an-arbitrary-base">Zariski connectedness and Stein factorization</a>, and the adapted compact-generation, denominator, Brown, supported-factorization and duality constructions in <a href="the-right-adjoint-of-derived-pushforward.html">The right adjoint of derived pushforward</a>, retain the authorship of the Stacks project authors and the AI Integrated Stacks Project edition contributors. GPT-6.1 Sol (OpenAI), Codex, Ultra, wrote the adaptations and added arguments on 5 October 2026. These identified components are licensed under GFDL version 1.2 or any later version, with no Invariant Sections, no Front-Cover Texts and no Back-Cover Texts. A verbatim <a href="COPYING-GFDL-1.2.txt">copy of the GNU Free Documentation License 1.2</a> accompanies the reader and editable archive. Independently authored portions retain their stated CC0 terms.</p><h2>References and software</h2><p>Linked AI Integrated Stacks Project texts retain GFDL1.2 and their authorship. MIT OpenCourseWare supplementary reading retains CC BY-NC-SA4.0. Other scholarly reading retains its own rights. <a href="COMPONENTS.json">Component record</a> · <a href="assets/mathjax/LICENSE">MathJax Apache2.0</a> · <a href="assets/mathjax/FONT-LICENSES.txt">Font notices</a>.</p>'
(root/'licensing.html').write_text(page('Authorship and component terms',licence),encoding='utf-8',newline='\n')
if (root/'PREREQUISITES.md').exists():
    guide=(root/'PREREQUISITES.md').read_text(encoding='utf-8')
    links={u['id']+'.html':u['id']+'.html' for u in course['units']}
    links.update({u['source']:u['source'] for u in course['units']})
    links.update({name:name for name in ['prerequisites.json','PROVIDER_HANDOFF.json','RESULTS.json']})
    links.update({route:route for route in course.get('programme_links',[])})
    (root/'prerequisites.html').write_text(page('Prerequisites and proof providers',render_markdown_math(guide,local_links=links)),encoding='utf-8',newline='\n')
subprocess.run(['pandoc',str(root/'course-introduction.md'),*[str(root/u['source']) for u in course['units']],'--from=markdown+tex_math_single_backslash','--to=latex','--standalone','--pdf-engine=pdflatex','--template',str(root/'latex-template.tex'),'-o',str(root/'files/course.tex')],check=True)
normalize(root/'files/course.tex')
save(root/'course.json',{'id':'AG-QC','title':course['title'],'language':'en','lessons':[{'id':f'AG-QC-{i+1:02}','slug':u['id'],'title':u['title'],'source':u['source'],'source_sha256':u['source_sha256'],'reader':u['id']+'.html','latex':'files/'+u['id']+'.tex'} for i,u in enumerate(course['units'])],'exercise_solutions':solution_count,'components':'COMPONENTS.json','proof_providers':'PROVIDER_HANDOFF.json','prerequisites':'prerequisites.json'})
with zipfile.ZipFile(root/'complete-source.zip','w',zipfile.ZIP_DEFLATED,compresslevel=9) as archive:
    for p in sorted(root.rglob('*')):
        if p.is_file() and p.suffix!='.zip' and '__pycache__' not in p.parts:
            info=zipfile.ZipInfo('AG-QC/'+p.relative_to(root).as_posix(),(1980,1,1,0,0,0));info.compress_type=zipfile.ZIP_DEFLATED;archive.writestr(info,p.read_bytes())
print(json.dumps({'lessons':len(course['units']),'reader':'complete','tex_sources':19,'source_zip_bytes':(root/'complete-source.zip').stat().st_size}))
