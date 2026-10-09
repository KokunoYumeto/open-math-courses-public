"""Portable builder for the selected RT-FIN edition; writes only its own directory."""
from pathlib import Path
import hashlib, html, json, re, sys
from html.parser import HTMLParser
ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(Path(__file__).resolve().parent/'renderer'))
from course_reader import render_markdown_math, private_reference

BASE='https://kokunoyumeto.github.io/open-math-courses/courses/RT-FIN/'
RESULT=re.compile(r'^\*\*((?:Lemma|Theorem|Proposition|Corollary) (\d+(?:\.\d+)*))\b', re.M)
def sha(p): return hashlib.sha256(p.read_bytes()).hexdigest().upper()
def write(p,s): p.write_text(s,encoding='utf-8',newline='\n')
def dump(p,s): write(p,json.dumps(s,ensure_ascii=False,indent=2)+'\n')
def esc(s): return html.escape(s,quote=True)
def page(filename,title,body):
    config={'tex':{'inlineMath':[['$','$'],[r'\(',r'\)']], 'displayMath':[['$$','$$'],[r'\[',r'\]']], 'processEscapes':True, 'macros':{'Eta':r'\mathrm{H}'}},'options':{'ignoreHtmlClass':'no-math','processHtmlClass':'math'}}
    credit='Written and self-checked by GPT-6.1 Sol (OpenAI), Ultra, in Codex.'
    if filename in {'representations-and-complete-reducibility.html','characters-and-the-orthogonality-relations.html'}:
        credit+=' Elementary prerequisite proofs and source comparisons by GPT-6 Astra (OpenAI), Ultra, in Codex; self-checked by that AI.'
    return '<!doctype html>\n<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>'+esc(title)+' · Open Mathematics Courses</title><link rel="canonical" href="'+BASE+filename+'"><link rel="stylesheet" href="../../assets/site.css"><style>.result-link{scroll-margin-top:1rem}.lesson-nav{display:flex;gap:1rem;flex-wrap:wrap;margin:1rem 0}.crosswalk td{padding:.4rem;vertical-align:top}.crosswalk code{font-size:.72rem}details{margin:1rem 0}</style><script>window.MathJax='+json.dumps(config,separators=(',',':'))+';</script><script id="MathJax-script" defer src="../../assets/mathjax/tex-chtml-full.js"></script></head><body class="no-math"><a class="skip-link" href="#main">Skip to content</a><header class="site-header"><div class="header-inner"><a class="brand" href="../../">Open Mathematics Courses</a><nav class="primary-nav"><a href="index.html">Representations of finite groups</a><a href="sources.html">Sources and terms</a><a href="proof-crosswalk.html">Proof index</a></nav></div></header><main id="main"><article class="lesson">'+body+'</article></main><footer class="header-inner"><p>'+credit+' <a href="sources.html">Authorship and component terms</a>.</p></footer></body></html>\n'

class Links(HTMLParser):
    def __init__(self): super().__init__(); self.ids=set(); self.links=[]; self.math=[]
    def handle_starttag(self,tag,attrs):
        a=dict(attrs)
        if 'id' in a:
            if a['id'] in self.ids: raise ValueError('duplicate anchor '+a['id'])
            self.ids.add(a['id'])
        if tag=='a' and 'href' in a:self.links.append(a['href'])
        if 'data-tex' in a:self.math.append(a['data-tex'])

def build():
    manifest=json.loads((ROOT/'course.json').read_text(encoding='utf-8'))
    units=manifest['units']
    assert len(units)==17
    paths={Path(u['source']).name:u['id']+'.html' for u in units}
    paths.update({
        '../../NT-CFT/src/artin-l-functions-conductors-and-discriminants.md':'../NT-CFT/artin-l-functions-conductors-and-discriminants.html',
        '../../NT-CFT/proof-dependencies.html':'../NT-CFT/proof-dependencies.html',
        '../../AG-CA/src/the-nullstellensatz-and-jacobson-rings.md':'../AG-CA/AG-CA-06.html',
        '../../../human/linear-algebra-bridges/from-bases-to-projections.html':'../../human/linear-algebra-bridges/from-bases-to-projections.html',
        '../../../human/linear-algebra-bridges/finite-hermitian-spaces.html':'../../human/linear-algebra-bridges/finite-hermitian-spaces.html',
        '../../../human/elementary-analysis/complex-exponential-and-the-circle.html':'../../human/elementary-analysis/complex-exponential-and-the-circle.html',
    })
    for u in units:
        paths[u['id']+'.md']=u['id']+'.html'
        paths[u['id']+'.html']=u['id']+'.html'
    results=[]; inventories=[]
    for i,u in enumerate(units):
        p=ROOT/u['source']; assert sha(p)==u['sha256'],p
        source=p.read_text(encoding='utf-8')
        body=render_markdown_math(source,local_links=paths)
        matches=list(RESULT.finditer(source)); unit_results=[]
        for j,m in enumerate(matches):
            label=m[1]; anchor=label.lower().replace(' ','-').replace('.','-')
            needle='<p><strong>'+esc(label)
            assert body.count(needle)==1,(p,label)
            body=body.replace(needle,'<p id="'+anchor+'" class="result-link"><strong>'+esc(label),1)
            start=source[:m.start()].count('\n')+1
            stop=source[:matches[j+1].start()].count('\n') if j+1<len(matches) else len(source.splitlines())
            row={'lesson':f'RT-FIN-{i+1:02}','unit':u['id'],'result':label,'reader':u['id']+'.html#'+anchor,'source':u['source'],'source_sha256':u['sha256'],'statement_line':start,'argument_context_lines':[start,stop]}
            if i==10 and label=='Theorem 2.2':
                a=source.index('## 3.'); b=source.index('## 5.')
                row['proof_route']={'reader_sections':['3-evaluation-and-reduction','4-an-elementary-subgroup-detects-every-evaluation'],'source_lines':[source[:a].count('\n')+1,source[:b].count('\n')],'uses':['Lemma 2.1','Lemma 3.1','Lemma 3.2']}
            unit_results.append(row)
        nav='<nav class="lesson-nav" aria-label="Lesson navigation">'
        if i:nav+='<a href="'+units[i-1]['id']+'.html">← Previous lesson</a>'
        nav+='<a href="index.html">Course contents</a><a href="'+u['source']+'" download>Editable source</a>'
        if i+1<len(units):nav+='<a href="'+units[i+1]['id']+'.html">Next lesson →</a>'
        nav+='</nav>'
        if unit_results: nav+='<details><summary>Results in this lesson</summary><ul>'+''.join('<li><a href="#'+r['reader'].split('#')[1]+'">'+r['result']+'</a></li>' for r in unit_results)+'</ul></details>'
        filename=u['id']+'.html'; write(ROOT/filename,page(filename,u['title'],nav+body))
        u['reader']=filename;u['reader_sha256']=sha(ROOT/filename)
        for r in unit_results:r['reader_sha256']=u['reader_sha256']
        results.extend(unit_results)
        parsed=Links();parsed.feed((ROOT/filename).read_text(encoding='utf-8'))
        inventories.append({'lesson':f'RT-FIN-{i+1:02}','source_sha256':u['sha256'],'reader_sha256':u['reader_sha256'],'results':len(unit_results),'math_spans':len(parsed.math),'exercise_solutions':len(re.findall(r'^\*{1,2}Solution\b',source,re.M))})
    provider_deps={
        'RT-FIN-02':['RT-FIN-01 Lemma 0.1','RT-FIN-01 Lemma 0.2','RT-FIN-01 Proposition 2.1','RT-FIN-01 Theorem 2.3','RT-FIN-01 Theorem 3.1'],
        'RT-FIN-06':['RT-FIN-01 Theorem 2.3','RT-FIN-02 Theorem 3.1','RT-FIN-04 Proposition 1.1'],
        'RT-FIN-11':['RT-FIN-01 Theorem 2.3','RT-FIN-01 Theorem 3.1','RT-FIN-02 Theorem 3.1','RT-FIN-02 Theorem 4.1','RT-FIN-05 Lemma 1.1','RT-FIN-05 Lemma 4.2','RT-FIN-06 Theorem 3.1','RT-FIN-06 Proposition 4.1','RT-FIN-07 Theorem 4.1','RT-FIN-10 Lemma 1.1']}
    key={(r['lesson'],r['result']):r for r in results}
    providers=[]
    for lesson,labels in [('RT-FIN-02',['Theorem 2.1','Theorem 3.1','Theorem 4.1','Corollary 4.2']),('RT-FIN-06',['Proposition 2.1','Theorem 3.1','Proposition 4.1']),('RT-FIN-11',['Theorem 2.2','Theorem 5.1'])]:
        for label in labels:
            entry=dict(key[lesson,label]); entry['imports']=[]
            for dep in provider_deps[lesson]:
                l,typ,num=dep.split(); entry['imports'].append(dict(key[l,typ+' '+num]))
            providers.append(entry)
    crosswalk={'schema':'rt-fin-proof-crosswalk/v1','course':'RT-FIN','base_url':BASE,'authorship':'GPT-6.1 Sol (OpenAI), Codex, Ultra; author self-check. This index is a locator, not an independent proof review.','line_convention':'One-based lines of the exact SHA-256-bound UTF-8 Markdown. Argument-context spans continue to the next labelled result; separately structured proofs have additional routes.','priority_providers':providers,'results':results}
    # Correct the local lemma's route to the actual renderer-generated heading IDs.
    p=Links();p.feed((ROOT/units[10]['reader']).read_text(encoding='utf-8'))
    section3=next(a for a in p.ids if a.startswith('3-'))
    section4=next(a for a in p.ids if a.startswith('4-'))
    for r in results+providers:
        if r['lesson']=='RT-FIN-11' and r['result']=='Theorem 2.2':r['proof_route']['reader_sections']=[section3,section4]
    dump(ROOT/'proof-crosswalk.json',crosswalk)
    dump(ROOT/'reader-inventory.json',{'schema':'rt-fin-reader-inventory/v1','units':inventories})
    dump(ROOT/'course.json',manifest)
    intro='<h1>Representations of finite groups</h1><p>Seventeen lessons with complete arguments, worked examples and solved exercises: character theory and Fourier analysis, induction and Clifford theory, integer Brauer induction, rationality, symmetric groups, Schur–Weyl duality and general linear groups over finite fields.</p><p>Start with finite-dimensional linear algebra and elementary group theory. Each lesson states its additional imports and supplies links to the earlier course proofs.</p><p><a href="proof-crosswalk.html">Find a theorem and its proof</a> · <a href="sources.html">Sources and component terms</a> · <a href="../../downloads/representations-of-finite-groups.zip">Download the reader and editable sources</a></p><ol class="lesson-list">'
    intro+=''.join('<li><a href="'+u['reader']+'"><span class="lesson-title">'+esc(u['title'])+'</span></a><a href="'+u['source']+'" download>Source</a></li>' for u in units)+'</ol><p>The proof index includes exact source and reader hashes. All lessons are self-checked by the writing AI; it records no blanket independent review of this edition.</p>'
    write(ROOT/'index.html',page('index.html',manifest['title'],intro))
    rows=''.join('<tr><td>'+r['lesson']+'</td><td><a href="'+r['reader']+'">'+r['result']+'</a></td><td><a href="'+r['source']+'">Markdown</a>, line '+str(r['statement_line'])+'</td></tr>' for r in results)
    proof='<h1>Proof index</h1><p>Every link opens the labelled statement and its course argument. The priority providers are character orthogonality, both Frobenius adjunctions and the full integer Brauer theorem. Brauer’s local induction theorem has its proof in sections 3–4 of Lesson 11; Sylow existence and the cyclotomic fixed-field argument are proved in Lesson 5.</p><p><a href="proof-crosswalk.json">Exact result, anchor, dependency and SHA-256 crosswalk</a> · <a href="course.json">Course source and reader identities</a></p><table class="crosswalk"><thead><tr><th>Lesson</th><th>Result</th><th>Editable proof source</th></tr></thead><tbody>'+rows+'</tbody></table>'
    write(ROOT/'proof-crosswalk.html',page('proof-crosswalk.html','Proof index',proof))
    source_md=(ROOT/'SOURCES.md').read_text(encoding='utf-8')
    write(ROOT/'sources.html',page('sources.html','Sources and component terms',render_markdown_math(source_md,local_links={**paths,'SOURCES.json':'SOURCES.json','source-dispositions.json':'source-dispositions.json'})))
    all_pages={p.name:Links() for p in ROOT.glob('*.html')}
    for filename,p in all_pages.items():p.feed((ROOT/filename).read_text(encoding='utf-8'))
    for filename,p in list(all_pages.items()):
        for link in p.links:
            if link.startswith(('http:','https:','mailto:')):continue
            target,_,anchor=link.partition('#')
            if target.startswith('../../') and not anchor:continue
            if target and not (ROOT/target).is_file():raise ValueError((filename,'missing file',link))
            if anchor and (not target or target.endswith('.html')):
                key=target or filename
                if key not in all_pages:
                    all_pages[key]=Links()
                    all_pages[key].feed((ROOT/key).read_text(encoding='utf-8'))
                if anchor not in all_pages[key].ids:raise ValueError((filename,'missing anchor',link))
    for r in results:
        target,anchor=r['reader'].split('#'); assert anchor in all_pages[target].ids
    assert all((r['source_sha256']==sha(ROOT/r['source']) and r['reader_sha256']==sha(ROOT/r['reader'].split('#')[0])) for r in results)
    print(json.dumps({'lessons':len(units),'labelled_results':len(results),'math_spans':sum(r['math_spans'] for r in inventories),'solutions':sum(r['exercise_solutions'] for r in inventories),'links_and_hashes':'pass'}))
if __name__=='__main__':build()
