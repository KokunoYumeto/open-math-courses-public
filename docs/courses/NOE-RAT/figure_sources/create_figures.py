"""Original course diagrams. Reproduce from the course root with Python + matplotlib."""
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import Polygon, FancyBboxPatch
import numpy as np

root=Path(__file__).resolve().parents[1]/'outputs'/'NOE-RAT'
# The packaged copy lives in figure_sources/, with assets/ beside it.
if not root.exists():
    root=Path(__file__).resolve().parents[1]
assets=root/'assets'
assets.mkdir(parents=True,exist_ok=True)
plt.rcParams.update({'font.family':'DejaVu Sans','mathtext.fontset':'dejavusans','font.size':12,'svg.fonttype':'path'})
blue='#12567e'; orange='#a84d15'; green='#287c62'; gray='#6b7480'

def save(fig,name):
    fig.savefig(assets/(name+'.png'),dpi=175,bbox_inches='tight',facecolor='white',metadata={'Software':'Original NOE-RAT course diagram'})
    fig.savefig(assets/(name+'.svg'),bbox_inches='tight',facecolor='white',metadata={'Creator':'GPT-6.1 Sol (OpenAI), Codex, Ultra; original course diagram','Date':None})
    plt.close(fig)

fig,ax=plt.subplots(figsize=(9,5.7))
ax.set(xlim=(-2.5,5.2),ylim=(-2.5,4.2),aspect='equal',xlabel=r'exponent $a$ of $x$',ylabel=r'exponent $b$ of $y$')
for a in range(-2,6):
    for b in range(-2,5):
        inside=(a-b)%3==0
        ax.scatter(a,b,s=44,facecolor=blue if inside else 'white',edgecolor=blue if inside else '#b5bec4',zorder=3)
ax.add_patch(Polygon([[0,0],[3,0],[4,1],[1,1]],closed=True,facecolor='#b9dfd8',edgecolor=green,alpha=.6,zorder=1))
for end,label,pos in [((3,0),r'$(3,0)\ \mapsto\ x^3$',(2.1,-.65)),((1,1),r'$(1,1)\ \mapsto\ xy$',(.35,1.65))]:
    ax.annotate('',xy=end,xytext=(0,0),arrowprops={'arrowstyle':'->','color':green,'lw':2.7},zorder=4)
    ax.text(*pos,label,color=green,fontsize=13,bbox={'facecolor':'white','edgecolor':'none','alpha':.85})
ax.axhline(0,color=gray,lw=.6); ax.axvline(0,color=gray,lw=.6)
ax.set_xticks(range(-2,6));ax.set_yticks(range(-2,5));ax.grid(color='#e5eaed',lw=.7)
ax.set_title(r'Invariant exponents: $a-b\equiv0\;(\mathrm{mod}\;3)$',pad=15,color=blue)
fig.text(.54,.06,'Basis parallelogram: area 3 = lattice index',ha='center',color=green,fontsize=11)
fig.subplots_adjust(bottom=.18)
save(fig,'invariant-lattice')

fig,ax=plt.subplots(figsize=(10,6.5));ax.axis('off');ax.set_xlim(0,10);ax.set_ylim(0,6.5)
def box(x,y,w,h,text,color=blue,size=13):
    ax.add_patch(FancyBboxPatch((x,y),w,h,boxstyle='round,pad=0.08',fc='#f5f8fa',ec=color,lw=1.6))
    ax.text(x+w/2,y+h/2,text,ha='center',va='center',color=color,fontsize=size,linespacing=1.5)
def arrow(start,end,label=None):
    ax.annotate('',xy=end,xytext=start,arrowprops={'arrowstyle':'->','lw':1.8,'color':gray})
    if label:
        ax.text((start[0]+end[0])/2+.14,(start[1]+end[1])/2,label,va='center',color=gray,fontsize=11)
box(.5,4.65,9,1,r'Coefficient space $S=\mathbf{P}(H_d)$'+'\n'+'one point = one degree-d form, up to scalar')
box(.5,2.65,4.1,1.2,r'Factor incidence $Z_e$'+'\n'+r'$[F]=[G H],\quad \deg G=e$'+'\n'+r'$([G],[H])\in\mathbf{P}(H_e)\times\mathbf{P}(H_{d-e})$',size=11)
box(5.4,2.65,4.1,1.2,r'Closed factor locus $R_e$'+'\n'+'projective elimination'+'\n'+'removes the factor variables',size=12)
arrow((4.68,3.25),(5.3,3.25))
arrow((7.45,3.92),(7.45,4.55),'image in S')
box(.5,.3,4.1,1.35,r'$R=\bigcup_{1\leq e<d}R_e$'+'\n'+'reducible forms'+'\n'+'all Noether forms vanish',orange)
box(5.4,.3,4.1,1.35,r'$S\setminus R$'+'\n'+'absolutely irreducible forms'+'\n'+'some Noether form is nonzero',green)
arrow((7.45,2.57),(3.7,1.75),'finite union')
arrow((4.68,.98),(5.3,.98))
ax.text(5,.03,'right-hand locus = complement in S',ha='center',color=gray,fontsize=10)
ax.text(5,6.35,'Why coefficient tests exist',ha='center',va='top',fontsize=18,color=blue)
save(fig,'factor-elimination')

fig,axs=plt.subplots(1,2,figsize=(10,4.6))
for ax in axs:
    ax.axis('off');ax.set_xlim(0,1);ax.set_ylim(0,1)
for ax,title,formula,poles in [(axs[0],'Polynomial generator',r'$u=t^3+t^2$',[r'$\infty$']), (axs[1],'Rational generator',r'$u=t+t^{-1}$',[r'$0$',r'$\infty$'])]:
    ax.set_title(title,color=blue,fontsize=15)
    ax.text(.5,.83,formula,ha='center',fontsize=20,color=blue)
    ax.plot([.12,.88],[.56,.56],color=gray,lw=2)
    ax.text(.5,.63,r'source $\mathbf{P}^1_t$',ha='center',color=gray)
    for x,label in zip([.85] if len(poles)==1 else [.25,.85],poles):
        ax.scatter(x,.56,s=75,color=orange,zorder=3)
        ax.text(x,.46,label,ha='center',color=orange,fontsize=15)
    ax.text(.5,.32,'Poles: '+('infinity only' if len(poles)==1 else 'zero and infinity'),ha='center',color=orange)
    ax.text(.5,.16,r'$k(u)\cap k[t]=k[u]$' if len(poles)==1 else r'$k(u)\cap k[t]=k$',ha='center',fontsize=18,color=green)
fig.text(.5,.025,'The marked line is a schematic of the projective source, not a real-function plot.',ha='center',color=gray,fontsize=10)
fig.subplots_adjust(bottom=.12,wspace=.3)
save(fig,'poles-and-subrings')
print('Created three original PNG/SVG diagrams.')
