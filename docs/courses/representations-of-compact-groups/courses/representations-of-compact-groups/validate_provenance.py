"""Stdlib-only offline validation. Copy beside the portable course.json."""
import json,re,hashlib
from pathlib import Path
from html.parser import HTMLParser
HERE=Path(__file__).resolve().parent
COURSE=HERE if (HERE/'course.json').exists() else HERE/'frozen/courses/representations-of-compact-groups'
PACK=COURSE.parent.parent;DOCS=PACK/'reader/courses/representations-of-compact-groups'
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def read(name):return [json.loads(x) for x in (COURSE/name).read_text(encoding='utf-8').splitlines() if x]
def unique(rows,key):
 d={r[key]:r for r in rows};assert len(d)==len(rows),(key,'duplicate identity');assert len({k.casefold() for k in d})==len(d),(key,'case collision');return d
class Ids(HTMLParser):
 def __init__(self):super().__init__();self.ids=set()
 def handle_starttag(self,tag,attrs):
  d=dict(attrs)
  if 'id' in d:assert d['id'] not in self.ids,('duplicate DOM id',d['id']);self.ids.add(d['id'])
sources=unique(read('sources.jsonl'),'source_key');results=unique(read('results.jsonl'),'id');uses=unique(read('source-use.jsonl'),'id');contributions=unique(read('contributions.jsonl'),'id')
index=json.loads((COURSE/'provenance-index.json').read_text(encoding='utf-8'));course=json.loads((COURSE/'course.json').read_text(encoding='utf-8'))
assert len(course['units'])==13 and len(contributions)==37
assert sum(r['kind']=='proved result' for r in results.values())==90
assert sum(r['kind']=='exercise with solution' for r in results.values())==52
for n,u in enumerate(course['units'],1):
 key=f'RT-CPT-{n:02d}';p=COURSE/u['source'];rev=sha(p);s=p.read_text(encoding='utf-8');assert rev.upper()==u['sha256'].upper()
 side=json.loads((COURSE/'src'/(key+'.provenance.json')).read_text(encoding='utf-8'));assert side['source_sha256']==rev and side['unit_id']==u['id']
 assert sha(DOCS/'src'/(key+'.provenance.json'))==sha(COURSE/'src'/(key+'.provenance.json'))
 assert '../sources.jsonl'==side['source_registry'] and (DOCS/'src'/side['source_registry']).is_file()
 doc=Ids();doc.feed((DOCS/(u['id']+'.html')).read_text(encoding='utf-8'))
 for r in (r for r in results.values() if r['lesson']==key):
  assert r['lesson_sha256']==rev and r['global_tag'] is None and r['original_research'] is False
  page,anchor=r['route'].split('#');assert page==u['id']+'.html' and anchor in doc.ids,(r['id'],'missing result route',anchor)
  body=r.get('proof',r.get('solution'));assert body and body['text'] in s and hashlib.sha256(body['text'].encode()).hexdigest()==body['sha256']
  assert index['result_to_sources'][r['id']]==r['source_use_ids']
  for edge in r['source_use_ids']:assert edge in uses and uses[edge]['result_id']==r['id']
  env=r.get('programme_dependencies',{})
  for skey in env.get('exact_external_prerequisite_environment',[]):assert skey in sources
  for prev in env.get('earlier_same_lesson_results',[]):assert prev['id'] in results and prev['lesson_sha256']==rev
  for prev in env.get('earlier_own_lessons',[]):
   other=index['lessons'][int(prev['lesson'][-2:])-1];assert other['source_sha256']==prev['sha256']
 history=next(x for x in index['source_revision_history'] if x['lesson']==key)
 assert history['current_revision']==rev and history==side['source_revision_history']
 for c in (c for c in contributions.values() if c['lesson']==key):
  assert any(v['sha256']==c['output_revision'] and c['id'] in v['contribution_ids'] for v in history['revisions'])
  assert (c['date'],c['model'],c['provider'],c['reasoning_effort']) in {('2026-10-03','GPT-6.1 Sol','OpenAI','Ultra'),('2026-10-05','Claude Opus 5.5','Anthropic','max')} and c['independent_review'] is False
 assert any(c['lesson']==key and c['output_revision']==rev for c in contributions.values())
 assert side['contributions']==[c for c in contributions.values() if c['lesson']==key]
for e in uses.values():
 assert e['source_key'] in sources,(e['id'],'unknown source',e['source_key'])
 if e['result_id'] is not None:assert e['result_id'] in results
 assert e['id'] in index['source_to_uses'][e['source_key']]
for key,rows in index['source_to_uses'].items():assert key in sources and set(rows)=={e['id'] for e in uses.values() if e['source_key']==key}
for name in ['sources.jsonl','results.jsonl','source-use.jsonl','contributions.jsonl','provenance-index.json']:
 text=(COURSE/name).read_text(encoding='utf-8');assert not re.search(r'[A-Za-z]:[/\\](?:Users|user|Documents|home|tmp)|file://|127\.0\.0\.1|localhost',text),('private path',name)
 assert sha(COURSE/name)==sha(DOCS/name)
receipt=dict(check='PASS',course='representations-of-compact-groups',lessons=13,sources=len(sources),result_records=len(results),labelled_proved_results=90,exercises_with_solutions=52,source_use_edges=len(uses),contributions=len(contributions),unique_identities=True,full_source_revision_bindings=True,historical_contributions_revision_bound=True,all_result_routes_resolve=True,bidirectional_source_navigation=True,no_private_absolute_paths=True,new_global_tags_allocated=0,independent_review_claimed=False,network_check=False)
out=HERE/'PROVENANCE_VALIDATION.json';out.write_text(json.dumps(receipt,indent=2)+'\n',encoding='utf-8');print(json.dumps(receipt))
