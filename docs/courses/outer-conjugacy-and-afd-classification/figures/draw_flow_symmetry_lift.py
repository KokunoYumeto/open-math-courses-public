"""Exact derivative square for the flow-symmetry lift; algebraic arrows."""
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
matplotlib.rcParams.update({'svg.fonttype':'path','svg.hashsalt':'flow-symmetry-lift-v1','font.family':'DejaVu Sans'})
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch
here=Path(__file__).resolve().parent
fig=plt.figure(figsize=(5.8,10),facecolor='white')
fig.text(.5,.958,'Lift a flow symmetry',ha='center',fontsize=23,color='#114e67')
fig.text(.5,.917,r'$hT_t=T_th$',ha='center',fontsize=21)
ax=fig.add_axes([.05,.675,.90,.205])
ax.set_xlim(0,1);ax.set_ylim(0,1);ax.axis('off')
for x,y,label in [(.12,.85,r'$x$'),(.88,.85,r'$T_tx$'),(.12,.14,r'$hx$'),(.88,.14,r'$hT_tx=T_thx$')]:
    ax.text(x,y,label,ha='center',va='center',fontsize=19,color='#202020')
for start,end,label,pos in [((.22,.85),(.76,.85),r'$T_t$',(.5,.98)),((.12,.70),(.12,.29),r'$h$',(.03,.5)),((.88,.70),(.88,.29),r'$h$',(.98,.5)),((.22,.14),(.64,.14),r'$T_t$',(.43,.015))]:
    ax.annotate('',xy=end,xytext=start,arrowprops={'arrowstyle':'->','color':'#155f78','lw':2})
    ax.text(*pos,label,ha='center',va='center',fontsize=18,color='#155f78')
def box(y,height,fill):
    fig.patches.append(FancyBboxPatch((.055,y),.89,height,boxstyle='round,pad=.008',facecolor=fill,edgecolor='#155f78',linewidth=1.2,transform=fig.transFigure))
box(.507,.133,'#edf7fa')
fig.text(.5,.612,'Top, then right: fibre parameter',ha='center',fontsize=14,color='#155f78')
fig.text(.5,.574,r'$t+\log D_{T_t}(x)$',ha='center',fontsize=19)
fig.text(.5,.536,r'$+\log D_h(T_tx)$',ha='center',fontsize=19)
box(.337,.133,'#edf7fa')
fig.text(.5,.443,'Left, then bottom: fibre parameter',ha='center',fontsize=14,color='#155f78')
fig.text(.5,.406,r'$\log D_h(x)+t$',ha='center',fontsize=19)
fig.text(.5,.367,r'$+\log D_{T_t}(hx)$',ha='center',fontsize=19)
fig.text(.5,.291,r'$D_h(T_tx)D_{T_t}(x)$',ha='center',fontsize=18)
fig.text(.5,.254,r'$=D_{T_t}(hx)D_h(x)$',ha='center',fontsize=18)
fig.text(.5,.204,'The derivative chain rule makes them equal.',ha='center',fontsize=12,color='#155f78')
fig.text(.5,.16,r'$D_h(x)e^{-\log D_h(x)}=1$',ha='center',fontsize=19)
fig.text(.5,.116,r'$s_X(h)|_Q=A_h,\qquad s_X(h)(U_t)=U_t$',ha='center',fontsize=16)
fig.text(.5,.079,r'$\operatorname{mod}(s_X(h))=h$',ha='center',fontsize=18)
fig.text(.5,.045,'Proposition 2.1; Lemma 3.1, (3.4); Proposition 5.1.',ha='center',fontsize=9)
fig.text(.5,.023,'Algebraic base arrows; no metric or mass is depicted.',ha='center',fontsize=9,color='#555555')
fig.savefig(here/'flow-symmetry-lift.svg',metadata={'Date':None})
fig.savefig(here/'flow-symmetry-lift.png',dpi=150,metadata={'Software':'matplotlib'})
plt.close(fig)
