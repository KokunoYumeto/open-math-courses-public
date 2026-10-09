"""Reproduce the exact compressed lifts and physical-time glancing ray; CC0."""
from pathlib import Path
import hashlib,json
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
matplotlib.rcParams.update({'svg.fonttype':'path','svg.hashsalt':'an04-zero-extension-20261009',
                            'font.size':12,'axes.titlesize':14})
root=Path(__file__).resolve().parents[1]
fig,axs=plt.subplots(1,2,figsize=(12,4.8),layout='constrained')
ax=axs[0];u=np.linspace(-2,2,401)
for a,c in [(0,'#586675'),(.25,'#96a944'),(.5,'#ce8238'),(1,'#245889')]:
 ax.plot(u,a*u,color=c,lw=2,label=r'$q/\epsilon='+str(a)+r'$')
ax.set(xlim=(-2.15,2.15),ylim=(-2.2,2.6),
       xlabel=r'Ordinary ratio $\rho/|\theta|$',
       ylabel=r'Compressed ratio $\sigma/(\epsilon|\theta|)$',
       title='Finite normal lifts collapse at the face')
ax.axvline(0,color='#bbc4ca',lw=.8);ax.grid(alpha=.18)
ax.legend(loc='upper left',fontsize=10,framealpha=.96,ncol=2)
ax.text(0,-2.02,r'$\epsilon=10^{-4},\ C=2,\ \delta=1/2$',ha='center',fontsize=11)
ax=axs[1]
for hs,color,label in [(np.linspace(.5,0,301),'#245889','Incoming'),
                       (np.linspace(0,-.5,301),'#be4f35','Outgoing')]:
 ts=-2*hs-2*hs**3/3;qs=hs**2
 ax.plot(ts,qs,color=color,lw=2.8,label=label)
 ax.annotate('',xy=(ts[170],qs[170]),xytext=(ts[135],qs[135]),
             arrowprops={'arrowstyle':'->','color':color,'lw':2})
ax.axhline(0,color='#263645',lw=1.3)
ax.scatter([0],[0],color='#263645',s=25,zorder=4)
ax.text(0,.14,'Glancing: (t, q) = (0, 0)',ha='center',fontsize=11)
ax.text(-1.083,.268,r'$(-13/12,\ 1/4)$',ha='left',fontsize=11)
ax.text(1.083,.268,r'$(13/12,\ 1/4)$',ha='right',fontsize=11)
ax.set(xlim=(-1.22,1.22),ylim=(-.02,.31),xlabel='Physical time t (increases to the right)',
       ylabel='Normal position q',title='One ordinary characteristic, both sides interior')
ax.grid(alpha=.18);ax.legend(loc='upper center',fontsize=10,ncol=2)
fig.suptitle(r'$\sigma=q\rho$ and the ray of $p=\rho^2+\xi^2-(1+q)\tau^2$',fontsize=16)
out=root/'figures/compressed-lifts-and-glancing-ray.svg'
fig.savefig(out,metadata={'Date':None});plt.close(fig)
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
(root/'figure-check.json').write_text(json.dumps({
 'svg':'figures/'+out.name,'svg_sha256':sha(out),'generator_sha256':sha(Path(__file__)),
 'exact_coordinates':'Left: sigma/(epsilon|theta|)=(q/epsilon)(rho/|theta|), epsilon=1/10000, C=2, delta=1/2. Right: q=s^2, t=-2s-2s^3/3, |s|<=1/2; arrows increase t.',
 'source_proof_locators':['Z2 / ZE8','Z3 / ZE11','Exercise 3 / ZE26-ZE27','F0'],
 'actually_inspected':False,'exact_coordinate_review_complete':False},indent=2)+'\n','utf-8')
print(out.name)
