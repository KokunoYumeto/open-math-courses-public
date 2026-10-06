"""Exact finite extension model; outputs are deterministic and locally editable."""
from pathlib import Path
from fractions import Fraction as F
import json,hashlib
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrowPatch,Rectangle

P=Path(__file__).resolve().parent;O=P/'assets';O.mkdir(exist_ok=True)
plt.rcParams.update({'font.family':'DejaVu Sans','font.size':15,'svg.hashsalt':'l118-exact-extension-rectangle','axes.spines.top':False,'axes.spines.right':False,'text.color':'#172b40','axes.labelcolor':'#172b40','xtick.color':'#172b40','ytick.color':'#172b40'})
weights=[F(1,6),F(1,6),F(1,3),F(1,3)];h=[1,-1,0,0]
plus=[w*(1+x) for w,x in zip(weights,h)];minus=[w*(1-x) for w,x in zip(weights,h)]
assert plus==[F(1,3),0,F(1,3),F(1,3)] and minus==[0,F(1,3),F(1,3),F(1,3)]
assert sum(weights)==sum(plus)==sum(minus)==1
assert sum(w*x*x for w,x in zip(weights,h))==F(1,3)
assert sum((p-m)*x for p,m,x in zip(plus,minus,h))==F(2,3)
for z in [weights,plus,minus]:assert sum(z[:2])==F(1,3) and sum(z[2:])==F(2,3)
for u in [F(0),F(1,3)]:
 for v in [F(0),F(2,3)]:assert sum(x>0 for x in [u,F(1,3)-u,v,F(2,3)-v])==2
blue='#2279ac';orange='#cb6c32';green='#278571';gray='#53687c'
fig=plt.figure(figsize=(15,13),dpi=200,facecolor='#fcfdff')
fig.text(.05,.963,'An extreme extension keeps the original operators',fontsize=25,weight='bold')
fig.text(.05,.924,'Two fixed marginal masses give a rectangle of state extensions; only its vertices collapse the full GNS algebra.',fontsize=13.5)
gs=fig.add_gridspec(2,2,left=.07,right=.95,bottom=.23,top=.85,wspace=.27,hspace=.60)
ax=fig.add_subplot(gs[0,0]);ax.set_axis_off();ax.set_xlim(0,1);ax.set_ylim(0,1)
ax.text(0,1.04,'1  The open surjection and its marginals',fontsize=17,weight='bold')
for yi,xcol,col,lab,mass in [(1,.24,blue,'1',r'$1/3$'),(2,.77,orange,'2',r'$2/3$')]:
 ax.scatter([xcol],[.23],s=650,color=col,zorder=4);ax.text(xcol,.23,'$y_'+lab+'$',ha='center',va='center',color='white',fontsize=17,zorder=6)
 ax.text(xcol,.04,'mass '+mass,ha='center',fontsize=15)
 for j,dx in [(1,-.1),(2,.1)]:
  x=xcol+dx;ax.scatter([x],[.74],s=510,facecolor='white',edgecolor=col,lw=2.5,zorder=4);ax.text(x,.74,'$x_{'+lab+str(j)+'}$',ha='center',va='center',fontsize=14,zorder=6)
  ax.add_patch(FancyArrowPatch((x,.67),(xcol,.31),arrowstyle='-|>',mutation_scale=17,lw=1.6,color=col))
ax.text(.5,.51,'$q$',ha='center',fontsize=19)
ax.text(.5,-.10,r'$C(Y)=\mathbb{C}^2\ \hookrightarrow\ C(X)=\mathbb{C}^4$',ha='center',fontsize=17)
ax=fig.add_subplot(gs[0,1]);ax.set_title('2  The complete state-extension fibre',loc='left',fontsize=17,weight='bold',pad=18)
ax.add_patch(Rectangle((0,0),1/3,2/3,facecolor='#eaf2fa',edgecolor=gray,lw=2))
corners=[(0,0),(1/3,0),(0,2/3),(1/3,2/3)];ax.scatter(*zip(*corners),s=110,color=green,zorder=5)
ax.scatter([1/6],[1/3],s=100,color='#7540a5',zorder=5)
ax.scatter([0,1/3],[1/3,1/3],s=78,color='#7540a5',zorder=5)
ax.annotate('',xy=(1/3,1/3),xytext=(0,1/3),arrowprops={'arrowstyle':'<->','color':'#7540a5','lw':2.3})
ax.text(1/6,1/3+.066,r'balanced $\psi$',ha='center',fontsize=13)
ax.text(0,1/3-.077,r'$\psi_-$',ha='center',fontsize=14);ax.text(1/3,1/3-.077,r'$\psi_+$',ha='center',fontsize=14)
ax.set_xlim(-.035,.37);ax.set_ylim(-.065,.74);ax.set_xticks([0,1/6,1/3],['0','$1/6$','$1/3$']);ax.set_yticks([0,1/3,2/3],['0','$1/3$','$2/3$']);ax.set_xlabel('$u$ = mass at $x_{11}$');ax.set_ylabel('$v$ = mass at $x_{21}$')
ax.text(.5,-.34,'Four vertices: own GNS dimension 2, '+r'$\mathcal{A}=\mathcal{B}=\mathbb{C}^2$',transform=ax.transAxes,ha='center',fontsize=13,color=green)
ax=fig.add_subplot(gs[1,0]);ax.set_title('3  A marginal-preserving kernel direction',loc='left',fontsize=17,weight='bold',pad=18)
x=np.arange(4);width=.24
for off,z,col,lab in [(-width,weights,'#7540a5',r'$\psi$'),(0,plus,blue,r'$\psi_+$'),(width,minus,orange,r'$\psi_-$')]:ax.bar(x+off,[float(v) for v in z],width,color=col,label=lab)
ax.set_xticks(x,[r'$x_{11}$',r'$x_{12}$',r'$x_{21}$',r'$x_{22}$']);ax.set_ylim(0,.43);ax.set_yticks([0,1/6,1/3],['0','$1/6$','$1/3$']);ax.set_ylabel('state mass');ax.legend(loc='upper right',ncol=3,fontsize=13,frameon=False)
ax.text(.5,-.20,r'$h=(1,-1,0,0),\quad P(h)=0,\quad \psi_\pm=(1\pm h)\psi$',transform=ax.transAxes,ha='center',fontsize=14)
ax.text(.5,-.34,r'$\psi=(\psi_++\psi_-)/2,\qquad(\psi_+-\psi_-)(h)=2/3$',transform=ax.transAxes,ha='center',fontsize=14)
ax=fig.add_subplot(gs[1,1]);ax.set_axis_off();ax.set_title('4  Distinguish the GNS representations',loc='left',fontsize=17,weight='bold',pad=18)
rows=[('Vertex','2 positive masses',r'$\dim H=2$',r'$\mathcal{A}=\mathcal{B}=\mathbb{C}^2$',green),('Balanced interior','4 positive masses',r'$\dim H=4$',r'$\mathcal{A}=\mathbb{C}^4,\ \mathcal{B}=\mathbb{C}^2$','#7540a5'),(r'Boundary $\psi_\pm$','3 positive masses',r'$\dim H=3$',r'$\mathcal{A}=\mathbb{C}^3,\ \mathcal{B}=\mathbb{C}^2$',gray)]
for y,(lab,n,dim,alg,col) in zip([.86,.54,.22],rows):
 ax.text(0,y,lab,fontsize=16,weight='bold',color=col);ax.text(0,y-.105,n+'; '+dim,fontsize=13.5);ax.text(0,y-.215,alg,fontsize=16)
ax.text(0,-.13,'The interior has a two-dimensional '+r'$\mathcal{B}$'+'-cyclic subspace.\nAn extreme vertex gives the extension on the original space.',fontsize=13,linespacing=1.45)
fig.text(.05,.070,'Exact finite model: (AE11)–(AE12).  General collapse: (AE1)–(AE6); compact and support assembly: (E5)–(E24).',fontsize=12.5)
fig.text(.05,.038,'The finite rectangle illustrates extremality; it is not a measurable-selection construction for arbitrary spaces.',fontsize=12.5,color=gray)
png=O/'extension-rectangle.png';svg=O/'extension-rectangle.svg'
fig.savefig(png,dpi=200,metadata={'Software':'Original L118 programme illustration'})
fig.savefig(svg,metadata={'Date':None,'Creator':'Original L118 programme illustration'})
# Portable source normalization, without changing the vector geometry.
svg.write_text('\n'.join(line.rstrip() for line in svg.read_text(encoding='utf-8').splitlines())+'\n',encoding='utf-8',newline='\n')
plt.close(fig)
data={'model':'finite four-point state-extension fibre','native_dimensions':[3000,2600],'marginals':['1/3','2/3'],'balanced_weights':[str(x) for x in weights],'kernel_h':h,'plus_weights':[str(x) for x in plus],'minus_weights':[str(x) for x in minus],'difference_on_h':'2/3','vertices':[['0','0'],['1/3','0'],['0','2/3'],['1/3','2/3']],'GNS_dimensions':{'vertex':2,'balanced':4,'horizontal_boundary_states':3},'smaller_cyclic_dimension':2,'no_general_selection_claim':True,'rights':'CC0-1.0 for original expression to extent of rights held; DejaVu font under separate recorded terms'}
(O/'extension-rectangle-data.json').write_text(json.dumps(data,indent=2)+'\n',encoding='utf-8',newline='\n')
print(json.dumps({'files':{p.name:hashlib.sha256(p.read_bytes()).hexdigest() for p in [png,svg,O/'extension-rectangle-data.json']},'exact_checks_passed':True}))
