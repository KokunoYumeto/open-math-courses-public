"""Exact symbolic schematics for the newly reconstructed L34; no external TeX."""
from pathlib import Path
import json, matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
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
 fig.savefig(OUT/(name+'.svg'),bbox_inches='tight',facecolor='white')
 fig.savefig(OUT/(name+'.png'),bbox_inches='tight',facecolor='white',dpi=150)
 plt.close(fig)
fig,ax=plt.subplots(figsize=(12,6.4));ax.set_xlim(0,1);ax.set_ylim(0,1);ax.axis('off')
ax.text(.5,.975,'Automatic boundedness: compression contradicts a nonzero graph limit',ha='center',va='top',fontsize=16)
box(ax,.025,.57,.245,.26,[r'$x_n=x_n^*\longrightarrow0$',r'$d x_n\longrightarrow a=a^*$',r'$\|a\|=1,\quad 1\in\sigma(a)$'])
box(ax,.365,.57,.285,.26,[r'$h=\max(0,2a-1)$',r'$p_n=h(x_n+3\varepsilon_n1)h$',r'$z_n=p_n/(4\varepsilon_n)$'])
box(ax,.745,.57,.23,.26,[r'$h^2/2\leq z_n\leq h^2$',r'$\|z_n\|\geq1/2$',r'$\varphi_n(z_n)=\|z_n\|$'])
arrow(ax,(.28,.70),(.35,.70),r'$\varepsilon_n=\|x_n\|>0$',dy=.16)
arrow(ax,(.66,.70),(.735,.70),'choose a norming state',dy=.16)
box(ax,.06,.15,.395,.23,[r'$d p_n\longrightarrow hah$',r'$\varphi_n(d p_n)=0$',r'$|\varphi_n(hah)|<1/8$'],'#ffedec')
box(ax,.55,.15,.395,.23,[r'$hah\geq h^2/2\geq z_n/2$',r'$\varphi_n(hah)\geq\|z_n\|/2$',r'$\varphi_n(hah)\geq1/4$'],'#e9f5ed')
arrow(ax,(.51,.55),(.29,.405),'product rule and norm error')
arrow(ax,(.865,.55),(.755,.405),'positivity and order')
ax.text(.5,.077,'Both bounds concern the same state and the same fixed positive element.',ha='center',fontsize=12)
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
data={'compression':{'epsilon':'norm(x_n)>0','h_function':'max(0,2t-1)','normalized_bounds':['h^2/2 <= z_n','z_n <= h^2','norm(z_n)>=1/2'],'same_state_conflict':['abs(phi_n(hah))<1/8','phi_n(hah)>=1/4'],'proof':'Theorem 4.3'},
 'corner':{'index_set':'arbitrary J, including uncountable sets','initial_projections':'e_i=v_i^*v_i<=e; may overlap','range_projections':'q_i=v_i v_i^*, pairwise orthogonal; join=1','final_projections':'gamma(q_i), pairwise orthogonal; join=1','unitary':'strong finite-subset sum gamma(v_i)v_i^*','coefficient':'v_i^*xv_j in eMe, fixed pointwise','proof':'Theorem 9.1'},
 'caption_scope':'Symbolic schematics, not finite-dimensional reductions; complete arguments remain in lesson.'}
(OUT/'exact-figure-data.json').write_text(json.dumps(data,indent=2)+'\n',encoding='utf-8')
print('Wrote two reproducible SVG/PNG pairs and exact figure data.')
