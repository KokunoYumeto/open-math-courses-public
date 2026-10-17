"""Validate every exact reader fragment with local, hash-bound runtime assets."""
from pathlib import Path
from collections import Counter
from contextlib import nullcontext
import argparse, datetime, hashlib, http.server, importlib.metadata, json, re, threading
from bs4 import BeautifulSoup
import psutil
from playwright.sync_api import sync_playwright

POLICY='AG-AS-exact-fragments-desktop-mobile-v1'
ERRORS=['mathErrors','unparsedControls','errors','failed_requests','failed_responses','literalCodeBlocks','unreachableWideMath']
sha=lambda raw:hashlib.sha256(raw).hexdigest()

class Server(http.server.ThreadingHTTPServer):request_queue_size=128

class Handler(http.server.SimpleHTTPRequestHandler):
    def log_message(self,*args):pass

def validate(site,report,channel,screenshots,no_cache):
    site=site.resolve();report=report.resolve()
    if report==site or site.is_relative_to(report):raise ValueError('Report directory overlaps the site root')
    report.mkdir(parents=True,exist_ok=True)
    cfg=json.loads((site/'courses/AG-AS/reader-source/build-inputs.json').read_bytes())
    assets=[]
    for row in cfg['files']:
        if row['output'].startswith('assets/') or row['output'].endswith(('.css','.js','.woff')):
            raw=(site/row['output']).read_bytes()
            if sha(raw)!=row['sha256']:raise ValueError('Runtime asset hash differs')
            assets.append({'path':row['output'],'sha256':sha(raw)})
    assets=sorted(assets,key=lambda r:r['path'])
    signature=sha(json.dumps(assets,sort_keys=True).encode())
    identity={'policy':POLICY,'asset_signature':signature,'validator_sha256':sha(Path(__file__).read_bytes()),
              'playwright':importlib.metadata.version('playwright'),'browser_choice':channel or 'playwright-chromium'}
    cachefile=report/'fragment-cache.json';cache=json.loads(cachefile.read_bytes()) if cachefile.exists() and not no_cache else {}
    plans=[];readers=[]
    for unit in cfg['units']:
        path=site/'courses/AG-AS'/unit['reader'];raw=path.read_bytes()
        if sha(raw)!=unit['reader_sha256']:raise ValueError('Reader differs from its build catalogue')
        front,rest=raw.decode().split('<article class="lesson">');body,tail=rest.split('</article>',1)
        whole=BeautifulSoup(body,'html.parser')
        if screenshots:
            for target in unit.get('capture_anchors',[]):
                if len(whole.find_all(id=target['anchor']))!=1:
                    raise ValueError('Screenshot anchor is absent or ambiguous')
        pieces=re.split(r'(?=<h[1-6](?:\s|>))',body)
        chunks=[''.join(pieces[i:i+20]) for i in range(0,len(pieces),20)]
        if ''.join(chunks)!=body:raise ValueError('Reader fragment concatenation differs')
        expected=Counter(e['data-tex'] for e in BeautifulSoup(body,'html.parser').select('[data-tex]'))
        actual=Counter()
        for index,chunk in enumerate(chunks):
            dom=BeautifulSoup(chunk,'html.parser');formulas=[e['data-tex'] for e in dom.select('[data-tex]')];actual.update(formulas)
            complete=(front+'<article class="lesson">'+chunk+'</article>'+tail).encode()
            captures=[r for r in unit.get('capture_anchors',[]) if dom.find(id=r['anchor'])] if screenshots else []
            key=sha(complete+json.dumps(identity,sort_keys=True).encode());prior=cache.get(key)
            reusable=bool(prior and prior.get('passed') is True and prior.get('identity')==identity and not captures
                          and prior.get('math')==len(formulas) and prior.get('headings')==len(dom.find_all(re.compile('^h[1-6]$')))
                          and all(prior.get(k)==[] for k in ERRORS) and prior.get('mobilePageOverflow') is False)
            plans.append({'unit':unit['id'],'reader':unit['reader'],'index':index,'raw':complete,'key':key,
                          'captures':captures,'cached':prior if reusable else None,'expected_math':len(formulas)})
        if actual!=expected or sum(expected.values())!=unit['expected_math']:raise ValueError('Complete formula coverage differs')
        readers.append({'id':unit['id'],'reader_sha256':sha(raw),'source_sha256':unit['source_sha256'],
                        'chunks':len(chunks),'formulas':sum(expected.values()),'expected_headings':unit['expected_headings']})
    fresh=any(not row['cached'] for row in plans)
    stop=threading.Event();memory={'peak_bytes':psutil.Process().memory_info().rss,'cap_bytes':5000000000,'cap_exceeded':False}
    def watch():
        while not stop.wait(0.5):
            family=[psutil.Process(),*psutil.Process().children(recursive=True)];total=0
            for process in family:
                try:total+=process.memory_info().rss
                except psutil.Error:pass
            memory['peak_bytes']=max(memory['peak_bytes'],total)
            if total>memory['cap_bytes']:
                memory['cap_exceeded']=True
                for process in family[1:]:
                    try:process.terminate()
                    except psutil.Error:pass
                return
    threading.Thread(target=watch,daemon=True).start()
    factory=lambda *args,**kwargs:Handler(*args,directory=str(site),**kwargs)
    server=Server(('127.0.0.1',0),factory);threading.Thread(target=server.serve_forever,daemon=True).start()
    rows=[];temporary=[];removed=[];browser=None
    try:
        with (sync_playwright() if fresh else nullcontext(None)) as p:
            if fresh:
                browser=p.chromium.launch(headless=True,**({'channel':channel} if channel else {}))
            try:
                for plan in plans:
                    if plan['cached']:
                        row=dict(plan['cached'],cache_reused=True)
                    else:
                        if memory['cap_exceeded']:raise MemoryError('Reader validation exceeded its memory cap')
                        filename='__reader_check_'+plan['unit']+'_'+str(plan['index']).zfill(3)+'.html'
                        path=site/'courses/AG-AS'/filename
                        if path.exists():raise ValueError('A reader-check temporary file already exists')
                        with path.open('xb') as f:f.write(plan['raw'])
                        temporary.append(path)
                        page=browser.new_page(viewport={'width':1280,'height':960});page.set_default_timeout(60000)
                        errors=[];failed=[];bad=[]
                        page.on('pageerror',lambda e:errors.append(str(e)))
                        page.on('requestfailed',lambda r:failed.append({'url':r.url.split('/courses/',1)[-1],'failure':r.failure}))
                        page.on('response',lambda r:bad.append({'status':r.status,'path':r.url.split('/courses/',1)[-1]}) if r.status>=400 else None)
                        response=page.goto('http://127.0.0.1:'+str(server.server_port)+'/courses/AG-AS/'+filename,wait_until='domcontentloaded')
                        page.wait_for_function('typeof MathJax!=="undefined" && !!MathJax.startup && !!MathJax.startup.promise')
                        page.evaluate('async()=>{await MathJax.startup.promise;await document.fonts.ready;}')
                        row=page.evaluate(r'''()=>({math:document.querySelectorAll('article mjx-container').length,headings:document.querySelectorAll('article h1,article h2,article h3,article h4,article h5,article h6').length,mathErrors:[...document.querySelectorAll('mjx-merror')].map(e=>({text:e.textContent,tex:e.closest('.math')?.dataset.tex})),unparsedControls:[...document.querySelectorAll('mjx-container')].filter(e=>/\\[A-Za-z]+/.test(e.textContent)).map(e=>e.textContent),literalCodeBlocks:[...document.querySelectorAll('article pre')].map(e=>e.textContent)})''')
                        shots=[];overflow=False;wide=[]
                        for mode,width,height in [('desktop',1280,960),('mobile',390,844)]:
                            page.set_viewport_size({'width':width,'height':height})
                            page.evaluate('async()=>{await document.fonts.ready;await new Promise(r=>requestAnimationFrame(()=>requestAnimationFrame(r)));}')
                            overflow|=page.evaluate('document.documentElement.scrollWidth>innerWidth+4')
                            for target in plan['captures']:
                                locator=page.locator('[id="'+target['anchor']+'"]')
                                if locator.count()!=1:raise ValueError('Screenshot anchor does not occur exactly once')
                                locator.evaluate('(e)=>{e.scrollIntoView({block:"start"});window.scrollBy(0,-24);}');page.evaluate('()=>new Promise(r=>requestAnimationFrame(()=>requestAnimationFrame(r)))')
                                name=plan['unit']+'-'+target['name']+'-'+mode+'.png';page.screenshot(path=str(report/name))
                                shots.append({'file':name,'sha256':sha((report/name).read_bytes())})
                            if mode=='mobile':
                                wide=page.evaluate('''()=>[...document.querySelectorAll('article .math')].filter(e=>e.scrollWidth>e.clientWidth+4).map(e=>{e.scrollLeft=e.scrollWidth;const ok=e.scrollLeft>0;e.scrollLeft=0;return {scrollsToEnd:ok,tex:e.dataset.tex}}).filter(e=>!e.scrollsToEnd)''')
                        row.update(identity=identity,html_sha256=sha(plan['raw']),unit=plan['unit'],chunk=plan['index'],mobilePageOverflow=overflow,
                                   unreachableWideMath=wide,errors=errors,failed_requests=failed,failed_responses=bad,
                                   http_status=response.status,screenshots=shots,browser_version=browser.version,cache_reused=False)
                        row['passed']=response.status==200 and row['math']==plan['expected_math'] and not overflow and all(not row[k] for k in ERRORS)
                        page.close();path.unlink();temporary.remove(path);removed.append({'file':filename,'sha256':sha(plan['raw'])})
                    rows.append(row)
                    (report/'fragment-results.json').write_text(json.dumps(rows,indent=2)+'\n',encoding='utf-8')
                    if not row['passed']:raise ValueError('Reader fragment failed: '+plan['unit']+' '+str(plan['index']))
                    cache[plan['key']]=row
                    cachefile.write_text(json.dumps(cache,indent=2)+'\n',encoding='utf-8')
                    if len(rows)%10==0:print(json.dumps({'checked_fragments':len(rows),'total_fragments':len(plans),'memory_peak_bytes':memory['peak_bytes']}),flush=True)
            finally:
                if browser is not None:browser.close()
    finally:
        server.shutdown();server.server_close();stop.set()
        for path in temporary:
            if not path.resolve().is_relative_to((site/'courses/AG-AS').resolve()):raise ValueError('Temporary path escaped its scope')
            if path.exists():path.unlink();removed.append({'file':path.name,'removed_after_failure':True})
        (report/'temporary-cleanup.json').write_text(json.dumps({'files_removed':removed,'temporary_files_remaining':[]},indent=2)+'\n',encoding='utf-8')
    for unit in readers:
        selected=[r for r in rows if r['unit']==unit['id']]
        if sum(r['math'] for r in selected)!=unit['formulas'] or sum(r['headings'] for r in selected)!=unit['expected_headings']:
            raise ValueError('Whole-reader totals differ')
    result={'schema':'AG-AS-reader-browser-check/v1','observed_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),
            'readers':readers,'identity':identity,'runtime_assets':assets,'browser_launched':fresh,
            'cached_exact_fragments':sum(bool(p['cached']) for p in plans),'freshly_rendered_fragments':sum(not p['cached'] for p in plans),
            'all_fragments_passed':True,'memory':memory,'temporary_files_removed':len(removed),
            'screenshots':[s for row in rows for s in row.get('screenshots',[]) if not row['cache_reused']],
            'human_or_independent_scholarly_review_claimed':False}
    if memory['cap_exceeded']:raise MemoryError('Reader memory cap exceeded')
    (report/'results.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
    return result

if __name__=='__main__':
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--site',type=Path,required=True);parser.add_argument('--report',type=Path,required=True)
    parser.add_argument('--channel',default='');parser.add_argument('--screenshots',action='store_true');parser.add_argument('--no-cache',action='store_true')
    args=parser.parse_args();result=validate(args.site,args.report,args.channel,args.screenshots,args.no_cache)
    print(json.dumps({'all_fragments_passed':result['all_fragments_passed'],'fresh':result['freshly_rendered_fragments'],'cached':result['cached_exact_fragments'],'readers':result['readers']}))
