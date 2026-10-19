"""Reproducible samples of the exact adaptive example AP37."""
from pathlib import Path
import hashlib,json
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
matplotlib.rcParams['svg.fonttype']='none'
MOD=Path(__file__).resolve().parents[1]
z=np.linspace(-np.pi,np.pi,1801)
y=np.abs(np.sin(z))
floor=np.full_like(z,.64);value=y;gradient=np.cos(z)**2
alpha=1/(10*np.sqrt(np.maximum.reduce([floor,value,gradient])))
fig,axes=plt.subplots(2,1,figsize=(11,7.2),sharex=True,layout='constrained')
axes[0].plot(z,floor,color='#475569',label='floor: p^2 / 100 = 0.64')
axes[0].plot(z,value,color='#b45309',label='value: |sin z|')
axes[0].plot(z,gradient,color='#146b87',label='gradient squared: cos^2 z')
axes[0].set(ylabel='Maximum terms / 100',title='The three exact competing quantities')
axes[0].legend(loc='lower left',ncol=1)
colors={'bounded':'#a3aab7','gradient':'#53a5c2','positive value':'#e8a04c','negative value':'#ae76b8'}
regions=np.where(y<.6,'gradient',np.where(y<=.64,'bounded',np.where(np.sin(z)>0,'positive value','negative value')))
for key,col in colors.items():
 axes[1].fill_between(z,.095,.13,where=regions==key,color=col,alpha=.25,label=key)
axes[1].plot(z,alpha,color='#182a3b',linewidth=2.2,label='alpha = 1 / s')
axes[1].set(ylabel='Reciprocal scale alpha',xlabel='z = x / 10',ylim=(.095,.13),title='Case regions and the resulting reciprocal scale')
axes[1].legend(loc='upper center',ncol=3,fontsize=9)
for ax in axes:
 ax.grid(alpha=.2)
 ax.set_xlim(-np.pi,np.pi)
for root in [np.arcsin(.6),np.arcsin(.64)]:
 for pos in [root,np.pi-root,-root,-np.pi+root]:
  axes[1].axvline(pos,color='#64748b',linewidth=.5,alpha=.55)
axes[1].set_xticks([-np.pi,-np.pi/2,0,np.pi/2,np.pi],['-pi','-pi/2','0','pi/2','pi'])
p=MOD/'figures/adaptive-trichotomy.svg'
fig.savefig(p);plt.close(fig)
sha=lambda q:hashlib.sha256(q.read_bytes()).hexdigest()
record={'svg':'figures/adaptive-trichotomy.svg','svg_sha256':sha(p),'generator_sha256':sha(Path(__file__)),
 'numerical_samples_of_exact_formula':True,'arbitrary_symbol_estimate_inferred_from_plot':False,
 'exact_formula':'s^2=max(64,100|sin z|,100cos^2 z); alpha=1/s; z=x/10',
 'exact_transition_levels':['3/5','16/25'],'source_locator':'**F0. Exact competing quantities and their scale.**',
 'scope':'The recorded calculations and diagrams concern the stated examples. The general analytic assertions use the written arguments.'}
(MOD/'figure-check.json').write_text(json.dumps(record,indent=2)+'\n','utf-8')
print(json.dumps({'figure_bytes':p.stat().st_size,'sha256':sha(p)}))
