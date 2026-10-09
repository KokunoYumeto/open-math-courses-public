"""Exact scalar gauge and continuation-cutoff profiles; original work: CC0."""
from pathlib import Path
import json,hashlib
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
ROOT=Path(__file__).resolve().parents[1]
plt.rcParams.update({'svg.fonttype':'path','svg.hashsalt':'AN04-MEX-20261008',
                    'font.size':12,'axes.spines.top':False,'axes.spines.right':False})
fig,axes=plt.subplots(1,2,figsize=(12,4.7),layout='constrained')
q=np.linspace(0,1.5,501);ax=axes[0]
ax.plot(q,np.cos(q),label=r'$\operatorname{Re}S=\cos q$',color='#166b82',lw=2.2)
ax.plot(q,-np.sin(q),label=r'$\operatorname{Im}S=-\sin q$',color='#b54b28',lw=2.2)
ax.plot(q,np.exp(-q),label=r'$T=e^{-q}$',color='#6b5091',lw=2.2,ls='--')
ax.set(xlabel=r'$q$',ylabel='gauge value',title='Solution gauge and adjoint test gauge',
       xlim=(0,1.5),ylim=(-1.15,1.15))
ax.legend(loc='lower left',frameon=False)
ax=axes[1];t=np.linspace(-.2,1.2,801)
a=np.zeros_like(t);b=np.zeros_like(t)
pos=t>0;a[pos]=np.exp(-1/t[pos])
pos=t<1;b[pos]=np.exp(-1/(1-t[pos]))
chi=b/(a+b);der=np.zeros_like(t)
mid=(t>0)&(t<1)
der[mid]=-a[mid]*b[mid]/(a[mid]+b[mid])**2*(1/t[mid]**2+1/(1-t[mid])**2)
ax.plot(t,chi,label=r'$\chi(t)$',color='#166b82',lw=2.4)
ax.plot(t,der/4,label=r'$\chi^\prime(t)/4$',color='#b54b28',lw=2.4)
ax.axhline(0,color='#afbcc3',lw=.7)
ax.axvline(0,color='#afbcc3',lw=.7,ls=':');ax.axvline(1,color='#afbcc3',lw=.7,ls=':')
ax.set(xlabel=r'$t$',ylabel='profile value',title='A smooth cutoff retains its source error',
       xlim=(-.2,1.2),ylim=(-.7,1.15))
ax.legend(loc='center right',frameon=False)
fig.suptitle('Exact profiles used in the causal construction',fontsize=16)
target=ROOT/'figures/causal-matrix-boundary.svg'
fig.savefig(target,metadata={'Date':None});plt.close(fig)
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
record={'svg':'figures/causal-matrix-boundary.svg','svg_sha256':sha(target),
        'generator_sha256':sha(Path(__file__)),'proof_locators':['MEX:C1','MEX:C7','MEX:X3','MEX:F0'],
        'parameters':{'m':1,'h':1,'q_interval':[0,1.5],'t_interval':['-1/5','6/5'],'derivative_scale':'1/4'},
        'meaning':'Exact scalar slices of distinct gauges and an explicit smooth cutoff; no PDE numerical solution claim.',
        'actually_inspected':False,'exact_coordinate_review_complete':False}
(ROOT/'figure-check.json').write_text(json.dumps(record,indent=2)+'\n','utf-8')
print(json.dumps({'figure':target.name,'bytes':target.stat().st_size}))
