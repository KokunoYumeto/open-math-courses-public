"""Exact interval microsupport models; independently written programme source, CC0."""
from pathlib import Path
import sys
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrowPatch

plt.rcParams.update({'svg.fonttype':'path','svg.hashsalt':'SH03-v140-rays','font.family':'DejaVu Sans','font.size':11})
out=Path(sys.argv[1]) if len(sys.argv)>1 else Path(__file__).resolve().parent
out.mkdir(parents=True,exist_ok=True)
fig, axes=plt.subplots(2,2,figsize=(10,8))
fig.subplots_adjust(left=.07,right=.95,bottom=.15,top=.78,wspace=.28,hspace=.60)
fig.suptitle('Two restriction maps determine the cotangent rays',fontsize=17,fontweight='bold',y=.97)
fig.text(.5,.925,r'$L\ \longleftarrow\ A\ \longrightarrow\ R$',ha='center',fontsize=16)
fig.text(.5,.882,r'positive $\xi$: left map fails to be an isomorphism   |   negative $\xi$: right map fails',ha='center',fontsize=11)
blue='#216b92';orange='#bd4d2d';dark='#203542'
cases=[
 ('Constant on the interval','k  ←¹  k  →¹  k',(-1,1),False,False),
 ('Closed right half interval','0  ←  k  →¹  k',(0,1),True,False),
 ('Open right half interval',r'$0\ \longleftarrow\ 0\ \longrightarrow\ k$',(0,1),False,True),
 ('Supported at the point',r'$0\ \longleftarrow\ k\ \longrightarrow\ 0$',None,True,True)]
def ray(ax,end,color):
 ax.add_patch(FancyArrowPatch((0,0),end,arrowstyle='-|>',mutation_scale=15,lw=3,color=color,zorder=4))
for ax,(title,diagram,base,up,down) in zip(axes.flat,cases):
 ax.set_xlim(-.575,.575);ax.set_ylim(-1.15,1.15);ax.set_aspect(.5)
 ax.axhline(0,color='#adbbc2',lw=.8,zorder=0);ax.axvline(0,color='#adbbc2',lw=.8,zorder=0)
 ax.set_xticks([-.5,0,.5]);ax.set_yticks([-1,0,1]);ax.grid(alpha=.17)
 for s in ax.spines.values():s.set_visible(False)
 ax.set_title(title+'\n'+diagram,fontsize=12,pad=10,color=dark)
 ax.set_xlabel(r'base $x$',labelpad=1);ax.set_ylabel(r'covector $\xi$',labelpad=1)
 if base:
  if base[0]<0:ray(ax,(-.54,0),blue)
  ray(ax,(.54,0),blue)
 if up:ray(ax,(0,1.08),orange)
 if down:ray(ax,(0,-1.08),orange)
 ax.plot(0,0,'o',color=dark,markersize=5,zorder=5)
 if title=='Open right half interval':ax.text(.07,-.63,r'test in degree $1$',fontsize=10,color=orange)
 if title=='Closed right half interval':ax.text(.07,.57,r'test in degree $0$',fontsize=10,color=orange)
fig.text(.5,.075,'Exact supports in a finite coordinate window; arrows indicate continuation.',ha='center',fontsize=11)
fig.text(.5,.042,'Filled origin included in every case. Proof: interval model (G1)–(G4).',ha='center',fontsize=11)
for ext in ['svg','png']:
 kwargs={'metadata':{'Date':None}} if ext=='svg' else {'dpi':160,'metadata':{'Software':'Open Math Courses'}}
 fig.savefig(out/('constructibility-rays.'+ext),facecolor='white',**kwargs)
plt.close(fig)
