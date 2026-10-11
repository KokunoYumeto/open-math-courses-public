"""Exact symbolic schematics for the newly reconstructed L34; no external TeX."""
from pathlib import Path
import json, matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
plt.rcParams["svg.hashsalt"] = "oa-flow-l34-reconstruction-20261009-v1"
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch
HERE=Path(__file__).resolve().parent
OUT=HERE/'figures'; OUT.mkdir(exist_ok=True)
plt.rcParams.update({'font.family':'DejaVu Sans','font.size':12,'svg.fonttype':'none'})
def box(ax,x,y,w,h,lines,color='#ecf2fa'):
 ax.add_patch(FancyBboxPatch((x,y),w,h,boxstyle='round,pad=0.012,rounding_size=0.03',facecolor=color,edgecolor='#314866',linewidth=1.4))
 for j,text in enumerate(lines):
  ax.text(x+w/2,y+h*(len(lines)-j)/(len(lines)+1),text,ha='center',va='center')
def arrow(ax,a,b,label=None,dy=.025):
 ax.add_patch(FancyArrowPatch(a,b,arrowstyle='-|>',mutation_scale=17,color='#314866',linewidth=1.5))
 if label:ax.text((a[0]+b[0])/2,(a[1]+b[1])/2+dy,label,ha='center',va='bottom',fontsize=10)
def finish(fig,name):
 fig.savefig(OUT/(name+'.svg'),bbox_inches='tight',facecolor='white',metadata={'Date': None})
 fig.savefig(OUT/(name+'.png'),bbox_inches='tight',facecolor='white',dpi=150)
 plt.close(fig)
fig,ax=plt.subplots(figsize=(13.4,8.2));ax.set_xlim(0,1);ax.set_ylim(0,1);ax.axis('off')
ax.text(.5,.982,'Automatic boundedness: norming state, cancellation, closed graph',ha='center',va='top',fontsize=16)
ax.text(.5,.900,'Theorem 4.3: unital star derivation, defined on the entire C*-algebra',ha='center',fontsize=12)
box(ax,.020,.625,.275,.24,[r'$x=x^*\ne0,\quad r=\|x\|$',
    r'$\sigma=\pm1,\quad \sigma r\in\mathrm{spec}(x)$',
    r'$p=r1+\sigma x\geq0$',r'$\|p\|=2r$'])
box(ax,.365,.625,.270,.24,[r'$\varphi(p)=2r,\quad\|\varphi\|=1$',
    r'$\varphi(x)=\sigma r$',r'$\varphi(dx)=0$',
    'Lemmas 4.1 and 4.2'])
box(ax,.705,.625,.275,.24,[r'$\|x+t\,dx\|\geq|\varphi(x+t\,dx)|$',
    r'$=\|x\|\qquad(t\in\mathbb{R})$',
    r'$x=0$: also true', 'Norm estimate (4.3a)'],'#e9f5ed')
arrow(ax,(.307,.745),(.353,.745))
arrow(ax,(.647,.745),(.693,.745))
ax.text(.5,.550,r'Graph test: $x_n=x_n^*\to0,\quad dx_n\to a=a^*$; fix real $t\ne0$.',ha='center',fontsize=13)
box(ax,.020,.190,.275,.28,[r'$y_n=a-x_n/t=y_n^*$',
    r'$da\in A$ is fixed',
    r'$\|y_n\|\leq\|y_n+t\,dy_n\|$',
    'Apply (4.3a) to this input'])
box(ax,.365,.190,.270,.28,[r'$y_n+t\,dy_n$',
    r'$=a-x_n/t+t\,da-dx_n$',
    r'$\longrightarrow t\,da$',
    r'$n\to\infty$ with $t$ fixed'])
box(ax,.705,.190,.275,.28,[r'$\|a\|\leq |t|\,\|da\|$',
    r'$t\to0\ \Longrightarrow\ a=0$',
    'Closed graph: Lemma 3.2',
    'The star derivation is bounded'],'#e9f5ed')
arrow(ax,(.307,.330),(.353,.330))
arrow(ax,(.647,.330),(.693,.330))
ax.text(.5,.100,'Then self-adjoint decomposition, the two star parts, and unitization cover every complex derivation.',ha='center',fontsize=12)
ax.text(.5,.045,'Full domain is essential for da. No state compactness or imported dissipativity theorem.',ha='center',fontsize=11)
finish(fig,'compression-contradiction')

fig,ax=plt.subplots(figsize=(12,7));ax.set_xlim(0,1);ax.set_ylim(0,1);ax.axis('off')
ax.text(.5,.97,'Full fixed corner: orthogonal ranges assemble one unitary',ha='center',va='top',fontsize=16)
box(ax,.345,.68,.31,.19,[r'$eH\quad(\gamma|_{eMe}=\mathrm{id})$',r'$e_i=v_i^*v_i\leq e$'])
for x,label in [(.05,'i'),(.39,'j'),(.73,'r')]:
 box(ax,x,.405,.22,.12,[rf'$q_{label}H$'])
 box(ax,x,.135,.22,.12,[rf'$\gamma(q_{label})H$'],'#e9f5ed')
 arrow(ax,(.50,.67),(x+.11,.55),rf'$v_{label}:e_{label}H\to q_{label}H$',dy=.018)
 arrow(ax,(x+.11,.39),(x+.11,.28),rf'$\gamma(v_{label})v_{label}^*$',dy=0)
ax.text(.5,.065,r'$U$ is the strong finite-subset sum of $\gamma(v_i)v_i^*$; $U^*U=UU^*=1$.',ha='center',fontsize=13)
ax.text(.5,.015,r'Arbitrary $J$; sums mean finite-subset nets. Initial subspaces inside $eH$ may overlap.',ha='center',fontsize=11)
ax.text(.5,.915,r'Fixed coefficients: $v_i^*xv_j\in eMe$ force $\gamma(x)=UxU^*$.',ha='center',fontsize=11)
finish(fig,'full-corner-assembly')
data={'graph_estimate': {'scope': 'Unital star derivation on the entire C*-algebra; zero input included.', 'spectral_choice': 'x=x*, r=norm(x)>0; sigma in {-1,1}, sigma*r in spectrum(x)', 'positive_norming_element': 'p=r*1+sigma*x>=0; norm(p)=2*r', 'state_values': ['phi(p)=2*r', 'phi(x)=sigma*r', 'phi(dx)=0', 'norm(phi)=1'], 'norm_estimate': 'norm(x+t*dx)>=norm(x) for every self-adjoint x and real t', 'graph_sequence': 'x_n=x_n*->0, dx_n->a=a* in norm', 'full_domain_use': 'da is a fixed element of A', 'test_input': 'a-x_n/t for each fixed real t!=0', 'exact_cancellation': '(a-x_n/t)+t*d(a-x_n/t)=a-x_n/t+t*da-dx_n', 'ordered_limits': ['n->infinity with t fixed: norm(a)<=abs(t)*norm(da)', 'then t->0: a=0'], 'conclusion': 'Real closed graph; self-adjoint decomposition; star parts; unitization.', 'proof': 'Theorem 4.3, estimates (4.3a)-(4.3b); Lemmas 4.1-4.2, 3.2, 2.1-2.2', 'classical_source': 'https://www.jstage.jst.go.jp/article/tmj1949/12/1/12_1_31/_pdf', 'schematic_only': True}, 'corner': {'index_set': 'arbitrary J, including uncountable sets', 'initial_projections': 'e_i=v_i^*v_i<=e; may overlap', 'range_projections': 'q_i=v_i v_i^*, pairwise orthogonal; join=1', 'final_projections': 'gamma(q_i), pairwise orthogonal; join=1', 'unitary': 'strong finite-subset sum gamma(v_i)v_i^*', 'coefficient': 'v_i^*xv_j in eMe, fixed pointwise', 'proof': 'Theorem 9.1'}, 'caption_scope': 'Symbolic schematics, not finite-dimensional reductions; complete arguments remain in lesson.'}
(OUT/'exact-figure-data.json').write_text(json.dumps(data,indent=2)+'\n',encoding='utf-8')
print('Wrote two reproducible SVG/PNG pairs and exact figure data.')
