from pathlib import Path
import json,re,subprocess,sys
from bs4 import BeautifulSoup
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'build'))
from reader_math_scrollers import scroll_math
root=Path(__file__).resolve().parents[1]
template=(root/'build/reader-template.html').read_text(encoding='utf-8').replace('href="reader.css"','href="../reader.css"').replace('href="index.html"','href="../index.html"')
temp=root/'providers/template.html'
temp.write_text(template,encoding='utf-8')
names={'characteristic-estimates.md':'SH02-CHE.html','asymptotic-estimates.md':'SH02-AE.html'}
for filename,output in names.items():
 source=(root/'providers/src'/filename).read_text(encoding='utf-8')
 original=source.splitlines()[0].removeprefix('# ')
 title=original+' — prerequisite reader edition'
 notice='# '+title+'\n\n*Reader edition by GPT-6.1 Sol (OpenAI), Ultra; published by Open Math Courses, 4 October 2026. Original SH02 exposition and diagram arrangements: CC0 1.0 Universal. Separate human and font notices are retained.*\n\n[Exact editable source](src/'+filename+') · [Component notices](LICENSE.md) · [CC0 1.0](https://creativecommons.org/publicdomain/zero/1.0/) · [Edition history](PROVENANCE.json)\n\n'
 # Keep the exact prerequisite routes visible in generated readers.
 provider_routes = {'asymptotic-estimates.md': 'SH02-AE.html', 'characteristic-estimates.md': 'SH02-CHE.html', 'cohomological-biduality.md': '../../sheaf-proof-readings/SH02-cohomological-biduality.html', 'microlocal-categories.md': '../../sheaf-proof-readings/SH02-microlocal-categories.html', 'microlocal-hom.md': '../../sheaf-proof-readings/SH02-microlocal-hom.html', 'microlocalization.md': '../../sheaf-proof-readings/SH02-microlocalization.html', 'microsupport-operations.md': '../../sheaf-proof-readings/SH02-microsupport-operations.html', 'microsupport-tests.md': '../../sheaf-proof-readings/SH02-microsupport-tests.html', 'normal-geometry.md': '../../sheaf-proof-readings/SH02-normal-geometry.html', 'specialization.md': '../../sheaf-proof-readings/SH02-specialization.html', 'unbounded-characteristic-estimates.md': '../../sheaf-proof-readings/SH02-unbounded-characteristic-estimates.html'}
 def link(m):
  path,sep,anchor=m[2].partition('#')
  if m[2].startswith(('https://','http://')) or not path:return m[0]
  if path not in provider_routes:
   raise ValueError('Unmapped prerequisite link: '+m[2])
  return '['+m[1]+']('+provider_routes[path]+(sep+anchor if sep else '')+')'
 source=re.sub(r'\[([^\]]+)\]\(([^)]+)\)',link,source)
 source=notice+source.replace('# '+original,'## Original document: '+original,1)
 source=re.sub(r'\\tag\{([^}]+)\}',lambda m:r'\qquad\text{('+m[1]+')}',source)
 source=source.replace(r'\varprojlim',r'\underset{\leftarrow}{\lim}')
 target=root/'providers'/output
 run=subprocess.run(['pandoc','--from=markdown+tex_math_single_backslash','--to=html5','--mathml','--template',str(temp),'--metadata','title='+title,'--output',str(target)],input=source,capture_output=True,text=True,encoding='utf-8')
 assert run.returncode==0 and not run.stderr.strip(),run.stderr
 html=target.read_text(encoding='utf-8').replace(r'\underset{\leftarrow}{\lim}',r'\varprojlim')
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
