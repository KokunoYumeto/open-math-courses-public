#!/usr/bin/env python3
"""Render this course without invoking the site's destructive global writer.

Run from a repository or unpacked source tree: python courses/NT-CFT/build_course.py
Use --register to merge this course's metadata; --global-index to update its
registration on the existing home page and catalogue. No other course is written.
Original code: OpenAI GPT-6.1 Sol, Codex, Ultra effort. CC0 1.0.
"""
from pathlib import Path
import argparse, hashlib, html, importlib.util, json, re, shutil, sys

HERE=Path(__file__).resolve().parent
ROOT=HERE.parents[1]
COURSES=ROOT/'courses'
DOCS=ROOT/'docs'
CID='NT-CFT'
def load(p): return json.loads(p.read_text(encoding='utf-8-sig'))
def merge_entry(path,row):
    # Splice only this entry: preserve every other entry's bytes and newlines.
    data=path.read_bytes()
    bom=b'\xef\xbb\xbf' if data.startswith(b'\xef\xbb\xbf') else b''
    raw=data[len(bom):].decode('utf-8')
    match=re.search(r'"courses"\s*:\s*\[',raw)
    if not match: raise ValueError('courses array missing')
    dec=json.JSONDecoder(); pos=match.end(); count=0; own=None
    while True:
        while pos<len(raw) and raw[pos].isspace(): pos+=1
        if raw[pos]==']': end=pos; break
        start=pos; value,pos=dec.raw_decode(raw,pos); count+=1
        if value.get('id')==CID:
            if own is not None: raise ValueError('duplicate course entry')
            own=(start,pos)
        while raw[pos].isspace(): pos+=1
        if raw[pos]==',': pos+=1
        elif raw[pos]!=']': raise ValueError('invalid array delimiter')
    encoded=json.dumps(row,ensure_ascii=False,indent=2)
    if own: out=raw[:own[0]]+encoded+raw[own[1]:]
    else: out=raw[:end]+(',' if count else '')+'\n'+encoded+'\n'+raw[end:]
    parsed=json.loads(out)
    assert sum(x['id']==CID for x in parsed['courses'])==1
    before=[x for x in json.loads(raw)['courses'] if x['id']!=CID]
    after=[x for x in parsed['courses'] if x['id']!=CID]
    assert before==after
    path.write_bytes(bom+out.encode('utf-8'))

def render(global_index=False):
    sys.path.insert(0,str(ROOT/'scripts/reader'))
    spec=importlib.util.spec_from_file_location('course_site_builder',ROOT/'scripts/build_site.py')
    mod=importlib.util.module_from_spec(spec); spec.loader.exec_module(mod)
    entry=load(HERE/'catalog-entry.json')
    # Validate exactly the owned sources, hashes, links, mathematics and figures.
    temp=COURSES/'.NT-CFT-reader-catalog.json'
    temp.write_text(json.dumps({'schema':'stacks-course-catalog/v1','snapshot':'Class field theory, October 2026','courses':[entry]},ensure_ascii=False),encoding='utf-8')
    # The shared catalogue validates unit routes only. Bind the guide note to
    # each lesson's actual References anchor during that validation, then route
    # that exact labelled link to the separately generated owned guide below.
    # Final cross-file validation covers the guide together with all 24 units.
    render_globals=mod.read_catalog.__globals__
    original_render=render_globals['render_markdown_math']
    def render_with_guide(text,local_links=None,**kwargs):
        links=dict(local_links or {})
        links['../FREE_PROOFS.md']='#references'
        return original_render(text,local_links=links,**kwargs)
    render_globals['render_markdown_math']=render_with_guide
    try: payload,sources=mod.read_catalog(temp)
    finally:
        render_globals['render_markdown_math']=original_render
        temp.unlink()
    catalog=load(COURSES/'catalog.json')
    class ScopedSite(mod.Site):
        def title_html(self,cid,unit):
            if (cid,unit['id']) not in self.sources:
                return mod.with_math(mod.unescape_markdown(mod.clean_title(unit['title'])))
            return super().title_html(cid,unit)
        def courses_json(self):
            # Project only the owned row. Other courses can have independently
            # managed editions without a source field in the shared metadata.
            reg=self.reg[CID]
            row={
                'id':CID,'title':reg['title'],'subject':reg['subject'],
                'summary':reg['summary'],'href':f'courses/{CID}/',
                'content_language':reg['content_language'],'translations':reg['translations'],
                'take_first':reg['take_first'],'courses_here_to_take_first':self.chain(CID),
                'status':'draft','status_note':self.status_of(CID),'written_by':self.writer(CID),
                'licence':{'spdx':reg['licence']['spdx'],'scope':reg['licence']['scope'],
                           'exceptions':reg['licence'].get('exceptions',[])},
                'lessons':[{'id':u['id'],'title':self.title_text(u),
                            'href':f"courses/{CID}/{u['id']}.html",
                            'markdown':'courses/'+u['source']}
                           for u in self.courses[CID]['units']]
            }
            data={'schema':'open-mathematics-courses/catalogue/2','snapshot':self.registry['snapshot'],
                  'label':self.site['group_label'],'base_url':self.base,'courses':[row]}
            self.out['courses.json']=(json.dumps(data,ensure_ascii=False,indent=1)+'\n').encode('utf-8')
    obj=ScopedSite.__new__(ScopedSite)
    obj.registry=load(COURSES/'registry.json'); obj.site=obj.registry['site']; obj.base=obj.site['base_url']
    obj.core=obj.registry['core_courses']; obj.subjects={r['id']:r['label'] for r in obj.registry['subjects']}
    obj.writers=obj.registry['writers']; obj.status=obj.registry['status_wording']
    obj.payload=catalog; obj.courses={c['id']:c for c in catalog['courses']}
    obj.courses[CID]=payload['courses'][0]
    raw_units={u['id']:u for u in entry['units']}
    for unit in obj.courses[CID]['units']: unit['source']=raw_units[unit['id']]['source']
    obj.sources=sources
    registered={r['id']:r for r in obj.registry['courses']}
    obj.reg={c:obj.defaults(r) for c,r in registered.items() if c in obj.courses}
    obj.planned=sorted(set(registered)-set(obj.courses)); obj.former={}; obj.results={'groups':[],'references':[]}
    obj.out={}; obj.copies={}; obj.unit_index={}; obj.item_index={}
    for cid,course in obj.courses.items():
        for unit in course['units']:
            obj.unit_index[unit['id']]=(cid,unit)
            for item in unit.get('mathematical_item_ids',[]): obj.item_index.setdefault(item,(cid,unit['id']))
    obj.check_take_first()
    obj.courses[CID]['units']=obj.dependency_order(obj.courses[CID])
    obj.course_page(CID)
    for n in range(len(obj.courses[CID]['units'])): obj.lesson_page(CID,n)
    plan=load(HERE/'release-plan.json')
    learning=load(HERE/'learning-structure.json')
    aliases=load(HERE/'anchor-aliases.json')['lessons']
    # Old bookmarks remain valid after a section's teaching role changes.
    for slug,mapping in aliases.items():
        key=f'courses/{CID}/{slug}.html'
        doc=obj.out[key].decode('utf-8')
        ids=re.findall(r'\bid="([^"]+)"',doc)
        for old,new in mapping.items():
            if old in ids or new not in ids: raise ValueError(f'invalid anchor alias {slug}: {old} -> {new}')
            if not re.fullmatch(r'[\w-]+',old): raise ValueError('unsafe anchor alias')
            pattern=r'(<h[1-6]\b[^>]*\bid="'+re.escape(new)+r'"[^>]*>)'
            doc,n=re.subn(pattern,lambda m:f'<span id="{html.escape(old,quote=True)}" aria-hidden="true"></span>'+m.group(1),doc,count=1)
            if n!=1: raise ValueError('anchor target is not a heading')
            ids.append(old)
        obj.out[key]=doc.encode('utf-8')
    paths='<section aria-labelledby="paths-title"><h2 id="paths-title">Reading paths</h2><p>Lesson numbers remain stable. These paths select the sections needed for a particular question. <a href="study-guide.html">Read the full study guide</a> and the <a href="free-proofs.html">proofs and freely readable references</a>.</p>'
    for route in learning['reading_paths']:
        paths+='<h3>'+html.escape(route['title'])+'</h3><p>'+html.escape(route['purpose'])+'</p><ol>'
        for step in route['steps']:
            i=step['lesson'];slug=plan['lesson_slugs'][i-1]
            paths+=f'<li><a href="{slug}.html">Lesson {i}</a>: '+html.escape(step['sections'])+'</li>'
        paths+='</ol>'
    paths+='</section>'
    from markdown_it import MarkdownIt
    guide=(HERE/'STUDY_GUIDE.md').read_text(encoding='utf-8')
    for slug in plan['lesson_slugs']:guide=guide.replace(f'](src/{slug}.md)',f']({slug}.html)')
    guide_body=MarkdownIt('commonmark',{'html':False}).render(guide)
    obj.page(f'courses/{CID}/study-guide.html','Studying class field theory','Section-level paths through the local and global proofs.',f'<nav class="crumbs"><a href="./">Class field theory</a></nav><article class="lesson-content">{guide_body}</article>')
    free_guide=(HERE/'FREE_PROOFS.md').read_text(encoding='utf-8').replace('](STUDY_GUIDE.md)','](study-guide.html)')
    for slug in plan['lesson_slugs']:free_guide=free_guide.replace(f'](src/{slug}.md)',f']({slug}.html)')
    free_body=MarkdownIt('commonmark',{'html':False}).render(free_guide)
    obj.page(f'courses/{CID}/free-proofs.html','Proofs and freely readable references','External comparisons alongside the course arguments.',f'<nav class="crumbs"><a href="./">Class field theory</a></nav><article class="lesson-content">{free_body}</article>')
    prerequisite_text=(HERE/'PROOF_DEPENDENCIES.md').read_text(encoding='utf-8')
    prerequisite_body=MarkdownIt('commonmark',{'html':False}).render(prerequisite_text)
    for row in load(HERE/'proof-dependencies.json')['records']:
        prerequisite_body=prerequisite_body.replace('<h2>'+row['id']+':','<h2 id="'+row['id']+'">'+row['id']+':')
    for number in range(1,25):
        prerequisite_body=prerequisite_body.replace('<h2>Lesson '+str(number)+'</h2>','<h2 id="lesson-'+str(number)+'">Lesson '+str(number)+'</h2>')
    obj.page(f'courses/{CID}/proof-dependencies.html','Prerequisite proofs and availability','Exact programme proof providers and remaining dependencies.',f'<nav class="crumbs"><a href="./">Class field theory</a></nav><article class="lesson-content">{prerequisite_body}</article>')
    links=['<li><a download href="files/class-field-theory.tex">Complete LaTeX edition</a></li>',
           '<li><a download href="files/class-field-theory-source.zip">Complete editable source ZIP</a></li>']
    downloads=f'<section aria-labelledby="downloads-title"><h2 id="downloads-title">Read and edit</h2><p>This HTML edition contains all {len(plan["lesson_slugs"])} lessons. The complete LaTeX file contains all their text; the ZIP supplies the figures, original lesson files and reproduction instructions.</p><ol>'+''.join(links)+'</ol></section>\n'
    index=f'courses/{CID}/index.html'
    obj.out[index]=obj.out[index].decode('utf-8').replace('<section class="lessons"',paths+'<section class="lessons"',1).replace('<section class="provenance"',downloads+'<section class="provenance"',1).encode('utf-8')
    for slug in plan['lesson_slugs']:
        key=f'courses/{CID}/{slug}.html'
        doc=obj.out[key].decode('utf-8')
        reading_base='https://kokunoyumeto.github.io/open-math-courses/'
        for provider in load(HERE/'proof-dependencies.json')['records']:
            old='../'+provider['course']+'/'+provider['lesson']+'.html'
            target=(reading_base+provider['programme_reader_path'] if provider['reader_available_in_this_edition'] and provider['course']!='LG-GAL' else reading_base+'courses/NT-CFT/proof-dependencies.html#'+provider['id'])
            doc=doc.replace(old,target)
        doc=doc.replace('href="#references">freely readable proof guide</a>','href="free-proofs.html">freely readable proof guide</a>')
        doc=doc.replace('href="#references">proof guide</a>','href="free-proofs.html">proof guide</a>')
        doc=re.sub(r'href="https://github\.com/[^" ]+/blob/main/courses/NT-CFT/src/'+re.escape(slug)+r'\.md"',f'href="files/{slug}.md"',doc)
        doc=doc.replace('Markdown source of this lesson</a></p>',f'Markdown source of this lesson</a> · <a download href="files/{slug}.tex">Complete LaTeX source</a> · <a download href="files/class-field-theory-source.zip">Editable source ZIP</a></p>')
        obj.out[key]=doc.encode('utf-8')
    doc=obj.out[index].decode('utf-8')
    doc=re.sub(r'href="https://github\.com/[^" ]+/tree/main/courses/NT-CFT"', 'href="files/class-field-theory-source.zip"',doc)
    doc=doc.replace('GitHub repository</a>', 'editable source ZIP</a>')
    obj.out[index]=doc.encode('utf-8')
    if global_index:
        # Preserve customized/public pages and every other catalogue row bytewise.
        obj.courses_json()
        ownrow=next(r for r in json.loads(obj.out.pop('courses.json'))['courses'] if r['id']==CID)
        merge_entry(DOCS/'courses.json',ownrow)
        obj.out['courses.json']=(DOCS/'courses.json').read_bytes()
        home=(DOCS/'index.html').read_bytes().decode('utf-8')
        pattern=r'<article class="course-card" id="course-NT-CFT"[^>]*>.*?</article>'
        card=obj.card(CID)
        if re.search(pattern,home,flags=re.S):
            home=re.sub(pattern,lambda _:card,home,count=1,flags=re.S)
        else:
            shelf=r'(<section class="shelf" id="shelf-number-theory"[^>]*>.*?<div class="card-grid">\s*)'
            home,n=re.subn(shelf,lambda m:m.group(1)+card+'\n',home,count=1,flags=re.S)
            if n!=1: raise ValueError('number theory shelf missing')
            for subject in ['all','number-theory']:
                chip=r'(<a class="chip"[^>]*data-subject="'+subject+r'"[^>]*>[^<]*<span class="count">)(\d+)(</span>)'
                home,n=re.subn(chip,lambda m:m.group(1)+str(int(m.group(2))+1)+m.group(3),home,count=1)
                if n!=1: raise ValueError('catalogue count missing')
            count=r'(<h3 id="shelf-number-theory-title">.*?<span class="shelf-count">)(\d+)( courses</span>)'
            home,n=re.subn(count,lambda m:m.group(1)+str(int(m.group(2))+1)+m.group(3),home,count=1,flags=re.S)
            if n!=1: raise ValueError('shelf count missing')
        obj.out['index.html']=home.encode('utf-8')
    allowed={index,f'courses/{CID}/study-guide.html',f'courses/{CID}/free-proofs.html',f'courses/{CID}/proof-dependencies.html',*[f'courses/{CID}/{s}.html' for s in plan['lesson_slugs']]}
    if global_index: allowed|={'index.html','courses.json'}
    if set(obj.out)!=allowed: raise ValueError('unexpected output outside owned render scope')
    for rel,data in obj.out.items():
        target=DOCS/rel; target.parent.mkdir(parents=True,exist_ok=True); target.write_bytes(data)
    from course_assets import asset_output_path
    for unit in obj.courses[CID]['units']:
        bound=sources[(CID,unit['id'])]['assets']
        for row in bound.records:
            source=bound.frozen_root/row['source']; data=source.read_bytes()
            if hashlib.sha256(data).hexdigest().upper()!=row['source_sha256'] or len(data)!=row['bytes']:
                raise ValueError('figure changed since validation')
            target=DOCS/asset_output_path(CID,unit['id'],row)
            if not target.resolve().is_relative_to((DOCS/'courses'/CID).resolve()):
                raise ValueError('figure target escapes owned course')
            target.parent.mkdir(parents=True,exist_ok=True); target.write_bytes(data)
    files=DOCS/'courses'/CID/'files'; files.mkdir(parents=True,exist_ok=True)
    for name in plan['direct_latex']: shutil.copyfile(HERE/'latex'/name,files/name)
    for slug in plan['lesson_slugs']:shutil.copyfile(HERE/'src'/f'{slug}.md',files/f'{slug}.md')
    for name in ['FREE_PROOFS.md','free-proofs.json']:shutil.copyfile(HERE/name,files/name)
    # Direct LaTeX downloads resolve their image dependency from this folder.
    assets=files/'assets'; assets.mkdir(exist_ok=True)
    for unit in load(HERE/'course.json')['units']:
        for row in unit.get('assets',[]):
            shutil.copyfile(HERE/row['source'],assets/Path(row['source']).name)
    zip_source=HERE/'downloads'/plan['source_zip']
    if zip_source.exists(): shutil.copyfile(zip_source,files/zip_source.name)
    return {'course':CID,'lessons':len(plan['lesson_slugs']),'pages':len(obj.out),'other_courses_written':0}

if __name__=='__main__':
    p=argparse.ArgumentParser(); p.add_argument('--register',action='store_true'); p.add_argument('--global-index',action='store_true'); args=p.parse_args()
    if args.register:
        merge_entry(COURSES/'catalog.json',load(HERE/'catalog-entry.json'))
        merge_entry(COURSES/'registry.json',load(HERE/'registry-entry.json'))
    print(json.dumps(render(args.global_index)))
