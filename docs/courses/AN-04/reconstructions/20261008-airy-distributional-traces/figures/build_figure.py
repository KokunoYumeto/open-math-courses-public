"""Original smooth partition and exact affine Airy transition layers. CC0-1.0."""
from pathlib import Path
import json,hashlib
import numpy as np
import mpmath as mp
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
P=Path(__file__).resolve().parent;mp.mp.dps=30
plt.rcParams.update({'font.size':12,'svg.fonttype':'path','svg.hashsalt':'AN04-ADT-20261008'})
def chi(a):
 if a<=-2:return 0.
 if a>=-1:return 1.
 u=a+2;a0=np.exp(-1/u);a1=np.exp(-1/(1-u));return a0/(a0+a1)
def F(t):return mp.airyai(t)-1j*mp.airybi(t)
f0=F(0)
fig,ax=plt.subplots(1,2,figsize=(13,4.6));fig.patch.set_facecolor('#f3f6f8')
a=np.linspace(-3,1,401);c=np.array([chi(t) for t in a])
ax[0].plot(a,c,label=r'$\chi_0(a)$: transition / positive',color='#146575',lw=2)
ax[0].plot(a,1-c,label=r'$\chi_1(a)$: oscillatory',color='#b26632',lw=2)
for t in [-2,-1]:ax[0].axvline(t,color='gray',linestyle=':',alpha=.5)
ax[0].set(xlabel=r'Airy argument $a$',ylabel='Partition coefficient',ylim=(-.04,1.08),title='The exact split in DT12')
ax[0].legend(loc='center right',fontsize=10);ax[0].grid(alpha=.2)
colors=['#146575','#b26632','#74569c']
for lam,rho,col in zip([8,64,512],[4,16,64],colors):
 q=np.linspace(0,.55,700)
 vals=[chi(-rho*t)*float(abs(F(-rho*t)/f0)) if rho*t<2 else 0. for t in q]
 ax[1].plot(q,vals,label=fr'$\lambda={lam}$',color=col,lw=2)
 ax[1].axvline(2/rho,color=col,linestyle=':',alpha=.35)
ax[1].set(xlabel=r'Physical normal coordinate $q$',ylabel=r'$|A_\lambda(q)|$',ylim=(-.04,1.08),title=r'Affine layer: $\mu=0$')
ax[1].legend();ax[1].grid(alpha=.2)
fig.suptitle('Normalized Airy transition layers',fontsize=16);fig.tight_layout()
out=P/'airy-distributional-layer.svg';fig.savefig(out,bbox_inches='tight',metadata={'Date':None});plt.close(fig)
record={'svg':'figures/'+out.name,'svg_sha256':hashlib.sha256(out.read_bytes()).hexdigest(),'generator_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),'coordinates':'Left: smooth step chi0, zero a<=-2 and one a>=-1. Right: |chi0(-q*lambda^(2/3)) F(-q*lambda^(2/3))/F(0)|, mu=0, lambda=8,64,512, q in [0,0.55].','actually_inspected':False,'exact_coordinate_review_complete':False}
(P.parent/'figure-check.json').write_text(json.dumps(record,indent=2)+'\n','utf-8');print(json.dumps(record))
