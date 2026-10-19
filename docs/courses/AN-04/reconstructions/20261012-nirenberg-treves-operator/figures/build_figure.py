"""Explicit matrix commutator scale and the time-window constants."""
from pathlib import Path
import hashlib,json
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
HERE=Path(__file__).resolve().parent
plt.rcParams.update({'font.size':11,'svg.fonttype':'none','svg.hashsalt':'an04-nirenberg-treves-operator','font.family':'DejaVu Sans'})
fig,axes=plt.subplots(1,3,figsize=(11,4.5),constrained_layout=True)
r=np.linspace(0,1,501);m=20*(1+r)**.25*r**.75
axes[0].plot(r,r,lw=2.5,label='Actual norm r',color='#247248')
axes[0].plot(r,m/3,lw=2.5,label='Proved bound M(r)/3',color='#236b94')
axes[0].set(title='Double-root commutator',xlabel='Off-diagonal entry r',ylabel='Operator norm',xlim=(0,1),ylim=(0,8.3));axes[0].legend(fontsize=9)
rr=np.geomspace(.001,1,501);mm=20*(1+rr)**.25*rr**.75
axes[1].loglog(rr,1/(2*mm),lw=2.5,color='#a36521')
axes[1].set(title='Strict upper time threshold',xlabel='r > 0 (log scale)',ylabel='1 / (2 M(r))',xlim=(.001,1))
theta=np.linspace(0,.48,401)
axes[2].plot(theta,4/(1-2*theta),lw=2.5,color='#673a87')
axes[2].axvline(.5,color='#a36521',ls='--')
axes[2].set(title='Norm constant divided by T',xlabel='θ = TM',ylabel='4 / (1 − 2θ)',xlim=(0,.51),ylim=(0,105))
for ax in axes:ax.grid(alpha=.2)
fig.suptitle('Exact formulas for B = diag(−1,1), A = [[1,r],[r,1]]',fontsize=14)
out=HERE/'operator-commutators-and-time-window.svg';fig.savefig(out,metadata={'Date':None,'Creator':'AN-04 original reproducible figure'});plt.close(fig)
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
(HERE.parent/'figure-check.json').write_text(json.dumps({'svg':'figures/operator-commutators-and-time-window.svg','svg_sha256':sha(out),'generator_sha256':sha(Path(__file__)),'actual_formulas':['double square-root commutator norm = r','M(r)=20(1+r)^(1/4)r^(3/4)','time threshold = 1/(2M(r)) for r>0','solution norm constant / T = 4/(1-2 theta), theta=TM<1/2'],'scope':'Exact formulas sampled for illustration. Infinite-dimensional bounds and every constant are proved analytically in the lesson.'                           },indent=2)+'\n','utf-8')
print(json.dumps({'figure':str(out),'sha256':sha(out)}))
