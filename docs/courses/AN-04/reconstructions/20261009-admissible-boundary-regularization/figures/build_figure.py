"""Exact finite source-test tree and Sobolev indices; CC0-1.0."""
from pathlib import Path
import hashlib,json,html
p=Path(__file__).resolve();root=p.parents[1]
out=['<svg xmlns="http://www.w3.org/2000/svg" width="1040" height="600" viewBox="0 0 1040 600">',
'<rect width="1040" height="600" fill="#f8fafc"/>',
'<style>text{font-family:Arial,sans-serif;fill:#172b40}.title{font-size:23px;font-weight:bold}.label{font-size:18px}.small{font-size:16px}.node{fill:#197d8d;stroke:white;stroke-width:2}.edge{stroke:#92b4c2;stroke-width:1.7}</style>']
def txt(x,y,s,cls='label',anchor='start'):
 out.append(f'<text x="{x}" y="{y}" class="{cls}" text-anchor="{anchor}">{html.escape(s)}</text>')
txt(28,40,'A finite admissible test tree: N = 1, d = 1','title')
txt(28,73,'Source nodes retain the entire kernel, including residual terms.','small')
levels=[]
for count,y in [(1,145),(4,230),(16,315)]:
 xs=[65+(i+.5)*540/count for i in range(count)]
 levels.append([(x,y) for x in xs])
for j in range(1,3):
 for i,(x,y) in enumerate(levels[j]):
  xp,yp=levels[j-1][i//4];out.append(f'<line class="edge" x1="{xp}" y1="{yp}" x2="{x}" y2="{y}"/>')
for j,level in enumerate(levels):
 for x,y in level:out.append(f'<circle class="node" cx="{x}" cy="{y}" r="7"/>')
 txt(30,level[0][1]+5,str(len(level)),'label')
 txt(665,level[0][1]+5,f'maximal source order = {[-6,-4,-2][j]}')
txt(30,360,'1 + 4 + 16 = 21 source tests before simplification','label')
out.append('<line x1="28" y1="388" x2="1012" y2="388" stroke="#c4d1d9"/>')
txt(28,425,'Ordinary Sobolev gains; every source target is at most L²','title')
for i,label in enumerate(['H⁻¹','H⁰','H¹','H²']):
 x=110+260*i
 out.append(f'<rect x="{x-55}" y="450" width="110" height="54" rx="8" fill="#ddecf1"/>')
 txt(x,485,label,'title','middle')
 if i<3:
  out.append(f'<path d="M{x+65} 477 H{x+185} l-10 -6 m10 6 l-10 6" stroke="#197d8d" stroke-width="3" fill="none"/>')
  txt(x+130,541,['source H⁻²','source H⁻¹','source L²'][i],'small','middle')
txt(28,580,'Arrows are analytic recovery steps, not geometric rays. Orders are upper bounds.','small')
out.append('</svg>')
dest=p.parent/'admissible-test-tree.svg';dest.write_text('\n'.join(out)+'\n','utf-8')
check={'svg':'figures/'+dest.name,'svg_sha256':hashlib.sha256(dest.read_bytes()).hexdigest(),
       'generator_sha256':hashlib.sha256(p.read_bytes()).hexdigest(),'actually_inspected':False,
       'exact_tree_node_counts':[1,4,16],'maximal_source_orders':[-6,-4,-2],
       'ordinary_solution_exponents':[-1,0,1,2],'ordinary_source_exponents':[-2,-1,0],
       'meaning':'Exact analytic dependency tree and recovery indices for Exercise 1; not a ray diagram.'}
(root/'figure-check.json').write_text(json.dumps(check,indent=2)+'\n','utf-8')
print(json.dumps({'figure':str(dest),'nodes':21,'passed':True}))
