"""Reproducible Airy energy-weight illustration. Independent code: CC0-1.0."""
from pathlib import Path
import hashlib,json,importlib.util
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import mpmath as mp
HERE=Path(__file__).resolve().parent;ROOT=HERE.parent
# Reuse the checked exact endpoint primitives without running the check suite.
text=(ROOT/'check_models.py').read_text('utf-8')
start=text.index('def vals(');stop=text.index('eigen_records=')
ns={'mp':mp};exec(compile(text[start:stop],'checked-energy-primitives','exec'),ns)
mp.mp.dps=45
plt.rcParams.update({'svg.fonttype':'path','svg.hashsalt':'AN04-airy-energy-20261008','font.size':10})
fig,axes=plt.subplots(1,2,figsize=(12.5,4.6),layout='constrained')
lam=1e6;b=np.linspace(-4,6,700);psi=2/3*np.maximum(b,0)**1.5
first=(1+b*b)**.25*np.exp(-2*psi)
second=lam**(-1/3)*(1+b*b)**(-.25)
ax=axes[0]
ax.semilogy(b,first,color='#006d83',label='Oscillating collar term')
ax.semilogy(b,second,color='#bd5e21',label='Boundary layer term')
ax.semilogy(b,first+second,color='#7650a0',linestyle='--',label='Sum')
root=float(mp.findroot(lambda x:mp.mpf(4)/3*x**mp.mpf('1.5')-mp.log(1+x*x)/2-mp.log(10**6)/3,3))
ax.axvline(root,color='#666666',linestyle=':',linewidth=1)
ax.set(xlabel=r'Boundary Airy argument $b$',ylabel=r'Weight divided by $\lambda^{5/3}$',
       title=r'Single-mode energy: $\lambda=10^6$',ylim=(1e-4,4))
ax.text(root+.12,1.6,'AE18: equal terms',fontsize=9)
ax.legend(loc='lower left',fontsize=9)
ax.grid(alpha=.2)
ax=axes[1];records=[]
for lam,color in [(64,'#006d83'),(512,'#bd5e21')]:
 vlist=np.linspace(-.1,.1,81);lo=[];hi=[]
 for v in vlist:
  lm=mp.mpf(lam);bv=mp.mpf(float(v))*lm**(mp.mpf(2)/3)
  ev=ns['eigenvalues'](lm,bv);lo.append(float(ev[0]));hi.append(float(ev[1]))
 ax.plot(vlist,lo,color=color,label=rf'$\lambda={lam}$: smaller')
 ax.plot(vlist,hi,color=color,linestyle='--',label=rf'$\lambda={lam}$: larger')
 records.append({'lambda':lam,'smallest_sampled_eigenvalue':min(lo),'largest_sampled_eigenvalue':max(hi)})
ax.set(xlabel=r'Normalized boundary parameter $b/k$',ylabel='Normalized Gram eigenvalue',
       title=r'Two-mode energy: $Q=1,\ \delta=0.1$')
ax.grid(alpha=.2);ax.legend(fontsize=9)
fig.suptitle('Airy energy weights: the collar and the boundary layer',fontsize=14)
target=HERE/'airy-energy-weights.svg';fig.savefig(target,metadata={'Date':None})
plt.close(fig)
result={'svg':'figures/'+target.name,'svg_sha256':hashlib.sha256(target.read_bytes()).hexdigest(),
 'generator_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
 'coordinates':{'left_lambda':1000000,'left_b_interval':[-4,6],'equal_terms_b':root,
 'right_Q':1,'right_delta':.1,'right_b_over_k_interval':[-.1,.1],'samples_per_lambda':81,'eigenvalue_samples':records},
 'exact_coordinate_review_complete':False,'actually_inspected':False,
 'scope':'Numerical illustration of AE17/AE18 and the exact AE36 Gram matrix; uniform bounds are analytic.'}
(ROOT/'figure-check.json').write_text(json.dumps(result,indent=2)+'\n','utf-8')
print(json.dumps(result['coordinates']))
