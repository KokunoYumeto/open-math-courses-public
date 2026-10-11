"""Reproduce the exact-function comparison in PSG:X2; sampled curves are labelled."""
from pathlib import Path
import math,hashlib,json
MOD=Path(__file__).resolve().parents[1]
def E(s):return math.exp(-1/(s*s)) if s>0 else 0.0
def h(t):return -E(-t-1)+E(t-1)
parts=['<svg xmlns="http://www.w3.org/2000/svg" width="1100" height="510" viewBox="0 0 1100 510"><rect width="1100" height="510" fill="#fff"/>',
 '<style>text{font-family:Arial,sans-serif;fill:#183146}.title{font-size:22px;font-weight:bold}.label{font-size:18px}.small{font-size:16px}</style>']
def text(x,y,s,cls='label',anchor='start'):
 parts.append(f'<text x="{x}" y="{y}" class="{cls}" text-anchor="{anchor}">{s}</text>')
for j,(left,title,eps) in enumerate([(70,'A persistent flat interval',0),(610,'The interval collapses',1/8)]):
 right=left+425;xx=lambda t:left+(t+2)/4*425;yy=lambda v:270-180*v
 text(left,34,title,'title');text(left,65,'h(t)' if not eps else 'h(t) + t/8','label')
 if not eps:
  parts.append(f'<rect x="{xx(-1)}" y="120" width="{xx(1)-xx(-1)}" height="285" fill="#e4f2f1"/>')
  text(xx(0),111,'all derivatives vanish','small','middle')
 else:
  parts.append(f'<line x1="{xx(0)}" y1="120" x2="{xx(0)}" y2="405" stroke="#879aab" stroke-dasharray="5 5"/>')
  text(xx(0),111,'strict crossing at 0','small','middle')
 parts.append(f'<path d="M {left} 120 V 405 M {left} 270 H {right}" fill="none" stroke="#5a6d7d" stroke-width="1.5"/>')
 for t in [-2,-1,0,1,2]:
  x=xx(t);parts.append(f'<path d="M {x} 266 V 275" stroke="#5a6d7d"/>');text(x,431,str(t),'small','middle')
 for v in [-0.5,0,0.5]:text(left-10,yy(v)+5,str(v),'small','end')
 points=[(xx(-2+k/100),yy(h(-2+k/100)+eps*(-2+k/100))) for k in range(401)]
 d=' '.join(('M' if k==0 else 'L')+f'{x:.4f},{y:.4f}' for k,(x,y) in enumerate(points))
 parts.append(f'<path d="{d}" fill="none" stroke="#166f83" stroke-width="3"/>')
 text(left+30,390,'negative','small');text(right-12,150,'positive','small','end')
 text(xx(0),460,'infimum length = 2' if not eps else 'infimum length = 0','label','middle')
 text(right+9,278,'t','label')
text(550,495,'Exact functions in X2; curves drawn from 401 samples per panel.','small','middle')
parts.append('</svg>')
p=MOD/'figures/flat-transition-and-collapse.svg';p.write_text('\n'.join(parts)+'\n','utf-8')
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
(MOD/'figure-check.json').write_text(json.dumps({'svg':'figures/'+p.name,'svg_sha256':sha(p),'generator_sha256':sha(Path(__file__)),'exact_functions':'h(t)=-E(-t-1)+E(t-1), E(s)=exp(-1/s^2) for s>0 and zero otherwise; second panel h(t)+t/8','domain':[-2,2],'sampling':{'points_per_panel':401,'step':0.01},'coordinates':{'left_plot_x':[70,495],'right_plot_x':[610,1035],'zero_y':270,'value_scale':180},'proof_locators':['PSG:M0','PSG:X2','PSG:V0'],'finite_samples_are_not_proof':True,'actually_inspected':False},indent=2)+'\n','utf-8')
print(json.dumps({'svg_sha256':sha(p),'samples':802}))
