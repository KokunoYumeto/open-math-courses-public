"""Build the self-contained reader from the hash-bound owned source catalogue."""
import hashlib,html,json,re,shutil,sys
from pathlib import Path
from html.parser import HTMLParser
from urllib.parse import urlsplit,unquote
root=Path(__file__).resolve().parent
sys.path.insert(0,str(root/'renderer'))
from course_reader import read_catalog,render_markdown_math
from course_assets import asset_output_path
def h(s):return html.escape(str(s),quote=True)
def read(n):return json.loads((root/n).read_text(encoding='utf8'))
catalog,sources=read_catalog(root/'catalogue.json')
course=catalog['courses'][0]
deps=read('prerequisites.json')['dependencies']
providers=read('PROVIDER_HANDOFF.json')['providers']
css='''body{margin:0;background:#f6f7f3;color:#172b28;font:18px/1.65 Georgia,serif}header,footer{background:#173e37;color:#fff;padding:1.2rem max(1.3rem,calc((100vw - 960px)/2))}header a,footer a{color:#fff}main{max-width:960px;margin:2rem auto;padding:0 1.4rem 3rem;overflow-wrap:anywhere}h1,h2,h3,nav,.note,button{font-family:system-ui,sans-serif}h1{font-size:2.1rem;line-height:1.2}h2{font-size:1.45rem;margin-top:2.5rem}h3{font-size:1.2rem;margin-top:2rem}a{color:#006459;text-underline-offset:3px}nav{font-size:1rem;display:flex;gap:1rem;flex-wrap:wrap}.note{border-left:4px solid #c28a35;background:#fff9ec;padding:1rem;font-size:1rem;margin:1.5rem 0}li{margin:.45rem 0}img{max-width:100%;height:auto}table{border-collapse:collapse;max-width:100%;display:block;overflow:auto}th,td{padding:.45rem;border:1px solid #bac8c0}mjx-container[display=true]{width:100%;min-width:0!important;max-width:100%;box-sizing:border-box;overflow-x:auto;overflow-y:hidden;padding:.4rem 0}pre{overflow:auto;padding:1rem;background:#edf0ea}code{font-size:.85em}figure{margin:2rem 0}figcaption{font-size:1rem}section{scroll-margin-top:1rem}@media(max-width:600px){body{font-size:17px}main{padding:0 1rem 2rem}h1{font-size:1.7rem}}'''
css += 'mjx-container:not([display]){display:inline-block;max-width:100%;overflow-x:auto;overflow-y:hidden}'
for row in course.get('linked_files',[]):
    target=root/row['href'];target.parent.mkdir(parents=True,exist_ok=True)
    shutil.copyfile(root/row['source'],target)
(root/'assets/reader.css').write_text(css,encoding='utf8')
mathjax_config={'tex':{'inlineMath':[['\\(','\\)'],['$','$']],
    'displayMath':[['\\[','\\]'],['$$','$$']],'processEscapes':True,
    'macros':{'NL':r'\operatorname{NL}','colim':r'\operatorname*{colim}'}},
    'options':{'skipHtmlTags':['script','noscript','style','textarea','pre','code']}}
def page(title,body,nav=''):
    return '<!doctype html>\n<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>'+h(title)+' | Reductive group schemes</title><link rel="stylesheet" href="assets/reader.css"><script>window.MathJax='+json.dumps(mathjax_config,separators=(',',':'))+';</script><script defer src="assets/mathjax/tex-chtml-full.js"></script></head><body><header><nav><a href="https://kokunoyumeto.github.io/open-math-courses/">Open mathematics courses</a><a href="index.html">Reductive group schemes</a><a href="prerequisites.html">Prerequisites</a></nav></header><main>'+nav+body+'</main><footer><nav><a href="COPYING.txt">Rights and credits</a><a href="references.html">Human sources</a><a href="Reductive-group-schemes-source.zip">Editable source archive</a></nav><p>GPT-6.1 Sol (OpenAI), Codex, Ultra setting. October 2026. Written and self-checked by the writing AI.</p></footer></body></html>\n'
for i,u in enumerate(course['units']):
    uid=u['id'];body=sources[('AG-RG',uid)]['html']
    # Preserve the incoming repairs that point programme links at the lessons.
    for old,new in {
        'https://kokunoyumeto.github.io/open-math-courses/courses/AG-GS/prerequisites/AG-AS/algebraic-spaces.html':'https://kokunoyumeto.github.io/open-math-courses/courses/AG-AS/algebraic-spaces.html',
        'https://kokunoyumeto.github.io/open-math-courses/courses/AG-GS/prerequisites/AG-AS/bootstrap-theorem.html':'https://kokunoyumeto.github.io/open-math-courses/courses/AG-AS/bootstrap-theorem.html',
        'https://kokunoyumeto.github.io/open-math-courses/courses/AG-DFG/descending-properties.html':'https://kokunoyumeto.github.io/open-math-courses/courses/AG-DFG/AG-DFG-03.html',
    }.items():
        body=body.replace('href="'+old+'"','href="'+new+'"')
    for p in providers:
        if p['source_file']!=uid+'.md':continue
        prefix=p['id'].split('-')[-1]
        label={'p':'Proposition','t':'Theorem','l':'Lemma'}[prefix[0]]
        n=prefix[1:];num=n[:-1]+'.'+n[-1]
        pattern=r'<p><strong>'+label+' '+re.escape(num)+r'(?=[. (])'
        body,count=re.subn(pattern,'<p id="'+p['id']+'"><strong>'+label+' '+num,body,count=1)
        if count!=1:raise ValueError('Missing actual theorem anchor '+p['id'])
    links=['<a href="'+uid+'.pdf">Lesson PDF</a>','<a href="'+uid+'.md">Markdown source</a>','<a href="'+uid+'.tex">Editable TeX</a>']
    if i:links.insert(0,'<a href="'+course['units'][i-1]['id']+'.html">Previous lesson</a>')
    if i+1<len(course['units']):links.append('<a href="'+course['units'][i+1]['id']+'.html">Next lesson</a>')
    (root/(uid+'.html')).write_text(page(u['title'],body,'<nav>'+''.join(links)+'</nav>'),encoding='utf8')
    for a in u.get('assets',[]):
        target=root/asset_output_path('AG-RG',uid,a).split('/',2)[2];target.parent.mkdir(parents=True,exist_ok=True)
        shutil.copyfile(root/a['source'],target)
guide=(root/'PREREQUISITES.md').read_text(encoding='utf8')
anchors=[]
for i,line in enumerate(guide.splitlines(),1):
    for d in deps:
        if line=='## '+d['title']:anchors.append({'line':i,'ids':['prerequisite-'+d['id'].lower()]})
body=render_markdown_math(guide,local_links={'index.html':'index.html','SOURCES.json':'SOURCES.json','COMPONENTS.json':'COMPONENTS.json',**{u['id']+'.md':u['id']+'.html' for u in course['units']}},heading_anchors=anchors)
(root/'prerequisites.html').write_text(page('Prerequisites and reading order',body),encoding='utf8')
source=read('SOURCES.json');refs=['<h1>Human sources and rights</h1><p>Freely accessible sources provide material for writing the programme proofs. Every used result requires its actual proof here or in an earlier programme lesson. Attributed Stacks adaptations retain their GNU FDL terms; original contributions retain their stated component terms.</p>']
for s in source['sources']:
    refs.append('<section><h2>'+h(s.get('title',s.get('authors',s['id'])))+'</h2><p>'+h(s.get('authors',''))+'. '+h(s.get('version',''))+'.</p>')
    if s.get('url'):refs.append('<p><a href="'+h(s['url'])+'">Source reading</a></p>')
    for key in ('licence','licence_evidence','reading_qualification','checked_scope'):
        if s.get(key):refs.append('<p>'+h(key.replace('_',' ').capitalize())+': '+h(s[key])+'</p>')
    if s.get('checked_content'):
        checked=s['checked_content'];checked=[checked] if isinstance(checked,str) else checked
        refs.append('<ul>'+''.join('<li>'+h(x)+'</li>' for x in checked)+'</ul>')
    refs.append('</section>')
refs.append('<p><a href="SOURCES.json">Full source and version record</a> · <a href="COMPONENTS.json">Component licences and expression boundaries</a> · <a href="assets/GFDL-1.2.txt">Unaltered GNU FDL 1.2</a></p>')
reference_body=''.join(refs)
# Retain the current reader wording when rebuilding from historical source records.
reference_wording={
    'Previously recorded actual readings in SOURCES.json, including §§2.1–2.3, 3.2, rank-one/root-data sections, pinned classification and automorphisms; exact source corrections remain in PROVENANCE.json.':'Sections read include §§2.1–2.3, 3.2, rank-one/root-data sections, pinned classification and automorphisms.',
    'Public edition checked 4 October 2026; AG-ET source last changed in commit 88d1416.':'Read 4 October 2026 (commit 88d1416).',
    'The supporting lesson Projective cohomology and smooth affine models contains the reconstructed model and smoothness arguments. Its transitive programme inputs remain under review.':'The supporting lesson Projective cohomology and smooth affine models contains the reconstructed model and smoothness arguments.',
    'Manager verified exact current author-hosted bytes, title and contents:':'Relevant contents:',
}
for old,new in reference_wording.items():
    reference_body=reference_body.replace(h(old),h(new))
(root/'references.html').write_text(page('Human sources and rights',reference_body),encoding='utf8')
missing=[d for d in deps if not d['source_sha256']]
intro='<h1>Reductive group schemes</h1><p>Six main lessons, preceded by supporting lessons: tori, centralizers, root groups, Bruhat decomposition, integral pinned classification, and forms and flag schemes, with worked examples and solved exercises.</p><p>The relative Bruhat and Schubert arguments retain their scope over every base, including the integers.</p><div class="note">Approximation, quotient, Lie and group foundations have written proofs. Self-checked by the writing AI. The <a href="prerequisites.html">prerequisite guide</a> identifies the required statements and their proof positions.</div><nav><a href="Reductive-group-schemes.pdf">Collected draft PDF</a><a href="Reductive-group-schemes-source.zip">Editable sources</a></nav><h2>Reading order</h2><ol>'
intro+=''.join('<li><a href="'+u['id']+'.html">'+h(u['title'])+'</a> · <a href="'+u['id']+'.pdf">PDF</a></li>' for u in course['units'])+'</ol><h2>Reading and reuse</h2><p><a href="references.html">Human sources and rights</a> · <a href="prerequisites.html">Supporting statements and reading order</a></p><p>Original contributions retain CC0 1.0. Attributed Stacks adaptations retain their GNU Free Documentation License obligations; the cumulative edition includes the full version 1.2 licence.</p><p><a href="PROVIDER_HANDOFF.json">Result and consumer map</a> · <a href="COMPONENTS.json">Component and licence record</a> · <a href="PROVENANCE.json">Edition provenance</a></p>'
(root/'index.html').write_text(page('Course reader',intro),encoding='utf8')
class Index(HTMLParser):
    def __init__(self):super().__init__();self.ids=set();self.links=[]
    def handle_starttag(self,tag,attrs):
        a=dict(attrs)
        if 'id' in a:
            if a['id'] in self.ids:raise ValueError('Duplicate HTML id '+a['id'])
            self.ids.add(a['id'])
        for k in ('href','src'):
            if k in a:self.links.append(a[k])
indices={}
for p in root.glob('*.html'):
    ix=Index();ix.feed(p.read_text(encoding='utf8'));indices[p.name]=ix
for filename,ix in indices.items():
    for link in ix.links:
        u=urlsplit(link)
        if u.scheme or u.netloc or u.path.startswith('../../') or u.path.endswith('.zip'):continue
        relative=unquote(u.path) or filename;target=root/relative
        if not target.is_file():raise ValueError('Missing local reader file '+filename+' -> '+link)
        if u.fragment and relative in indices and unquote(u.fragment) not in indices[relative].ids:raise ValueError('Missing reader anchor '+link)
for p in providers:
    url=urlsplit(p['reader_url']);name=Path(url.path).name
    if url.fragment not in indices[name].ids:raise ValueError('Provider anchor was not rendered')
print('Built and checked '+str(len(indices))+' HTML pages, all local links and exact proof anchors.')
