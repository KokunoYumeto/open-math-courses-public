"""Exact tangent-plane sections of X1/X2 and the coisotropic dimension bound."""
from pathlib import Path
import hashlib,json
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
ROOT=Path(__file__).resolve().parents[1]
plt.rcParams.update({'svg.fonttype':'none','font.family':'DejaVu Sans','font.size':11})
fig,axes=plt.subplots(1,3,figsize=(13.2,4.4),layout='constrained')
for i,ax in enumerate(axes[:2]):
 ax.axhline(0,color='#a8b4bf',lw=.8);ax.axvline(0,color='#a8b4bf',lw=.8)
 ax.set(xlim=(-.5,1.55),ylim=(-1.5,.5));ax.set_aspect('equal')
 for xy,label,color,where in [((1,0),'H_g','#246f86',(1.05,.10)),((0,-1),'H_f','#8b4f95',(.12,-1.07))]:
  ax.annotate('',xy=xy,xytext=(0,0),arrowprops={'arrowstyle':'->','color':color,'lw':2})
  ax.text(*where,label,color=color,fontsize=12)
 if i==0:
  ax.scatter([0],[0],color='#ad4937',zorder=5);ax.set(xlabel='x₁ offset',ylabel='ξ₁ offset',
   title='X1: transverse plane\nS occupies only the origin')
  ax.text(-.4,.25,'{f,g} = −1',color='#ad4937')
 else:
  ax.set_facecolor('#e5f0e8');ax.set(xlabel='x₂ tangent offset',ylabel='ξ₁ tangent offset',
   title='X2: Lagrangian tangent plane\nboth arrows stay tangent')
  ax.text(-.4,.25,'ω restricted to Λ = 0',color='#286947')
ax=axes[2];n=np.arange(1,5);ax.fill_between(n,n,2*n,color='#dce7ee')
ax.plot(n,n,'o-',color='#286947',label='minimum dim S = n')
ax.plot(n,2*n,'s--',color='#647a89',label='ambient dimension 2n')
ax.set(xticks=n,xlabel='base dimension n',ylabel='dimension',
 title='Coisotropy requires dim S ≥ n',ylim=(0,8.6))
ax.legend(frameon=False,fontsize=9,loc='upper left');ax.grid(alpha=.2)
fig.suptitle('A nonzero Poisson bracket excludes a wavefront point',fontsize=14)
p=ROOT/'figures/poisson-obstruction.svg';fig.savefig(p,metadata={'Date':None});plt.close(fig)
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
(ROOT/'figure-check.json').write_text(json.dumps({'svg':'figures/poisson-obstruction.svg',
 'svg_sha256':sha(p),'generator_sha256':sha(Path(__file__)),'scope':'The recorded calculations and diagrams concern the stated examples. The general analytic assertions use the written arguments.',
 'data':'PO15–PO18: H_g=(1,0), H_f=(0,-1) in the specified transverse/tangent sections; exact PO14 dimension bound.',
 'qualification':'First two panels are labeled two-dimensional linear sections of four-dimensional phase space; third plots a proved dimension bound.',
 'embedded_fonts':False,'original_expression_licence':'CC0-1.0'},indent=2)+'\n','utf-8')
print(json.dumps({'svg_bytes':p.stat().st_size}))
