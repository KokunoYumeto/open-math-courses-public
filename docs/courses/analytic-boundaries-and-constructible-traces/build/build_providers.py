from pathlib import Path
import json,re,subprocess,sys
from bs4 import BeautifulSoup
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'build'))
from reader_math_scrollers import scroll_math
root=Path(__file__).resolve().parents[1]
template=(root/'build/reader-template.html').read_text(encoding='utf-8').replace('href="reader.css"','href="../reader.css"').replace('href="index.html"','href="../index.html"')
temp=root/'providers/template.html'
temp.write_text(template,encoding='utf-8')
names={'cohomological-biduality.md':'SH02-CB.html','exceptional-operations.md':'SH02-EX.html'}
for filename,output in names.items():
 source=(root/'providers/src'/filename).read_text(encoding='utf-8')
 original=source.splitlines()[0].removeprefix('# ')
 title=original+' — prerequisite reader edition'
 notice='# '+title+'\n\n*Reader edition by GPT-6.1 Sol (OpenAI), Ultra; published by Open Math Courses, 4 October 2026. Original SH02 exposition is dedicated under CC0 1.0 Universal; human and font notices are retained. Source-account repair: 5 October 2026.*\n\n[Exact editable source](src/'+filename+') · [Reuse and source notice](LICENSE.md) · [Retained GFDL reference text](licenses/GFDL-1.2.txt) · [Edition history](PROVENANCE.json)\n\n'
 # Keep the exact prerequisite routes visible in generated readers.
 provider_routes = {'cohomological-biduality.md': 'SH02-CB.html', 'convex-acyclicity.md': '../../sheaf-proof-readings/SH02-convex-acyclicity.html', 'exceptional-operations.md': 'SH02-EX.html', 'formal-system-bridge.md': '../../sheaf-proof-readings/SH02-formal-system-bridge.html', 'manifold-duality.md': '../../sheaf-proof-readings/SH02-manifold-duality.html', 'open-prerequisites.md': '../../sheaf-proof-readings/SH02-open-prerequisites.html'}
 def link(m):
  path,sep,anchor=m[2].partition('#')
  if m[2].startswith(('https://','http://')) or not path:return m[0]
  if path not in provider_routes:
   raise ValueError('Unmapped prerequisite link: '+m[2])
  return '['+m[1]+']('+provider_routes[path]+(sep+anchor if sep else '')+')'
 source=re.sub(r'\[([^\]]+)\]\(([^)]+)\)',link,source)
 source=notice+source.replace('# '+original,'## Original document: '+original,1)
 source=re.sub(r'\\tag\{([^}]+)\}',lambda m:r'\qquad\text{('+m[1]+')}',source)
 source=source.replace(r'\varprojlim',r'\underset{\leftarrow}{\lim}').replace(r'\varinjlim',r'\underset{\rightarrow}{\lim}')
 target=root/'providers'/output
 run=subprocess.run(['pandoc','--from=markdown+tex_math_single_backslash','--to=html5','--mathml','--template',str(temp),'--metadata','title='+title,'--output',str(target)],input=source,capture_output=True,text=True,encoding='utf-8')
 assert run.returncode==0 and not run.stderr.strip(),run.stderr
 html=target.read_text(encoding='utf-8').replace(r'\underset{\leftarrow}{\lim}',r'\varprojlim').replace(r'\underset{\rightarrow}{\lim}',r'\varinjlim')
 soup=BeautifulSoup(scroll_math(html),'html.parser')
 for h in soup.find_all(re.compile(r'^h[1-6]$')):
  match=re.match(r'(SH02-[A-Z0-9-]+)',h.get_text())
  if match:h['id']=match[1]
 for table in soup.find_all('table'):
  wrapper=soup.new_tag('div',attrs={'class':'provider-table','style':'max-width:100%;overflow-x:auto'})
  table.wrap(wrapper)
 assert not soup.find('merror')
 target.write_text(str(soup),encoding='utf-8')
temp.unlink()
