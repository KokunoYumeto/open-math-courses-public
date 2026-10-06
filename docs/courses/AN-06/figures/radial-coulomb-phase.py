"""Exact Coulomb exterior model, independently drawn; CC0."""
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
from scipy.integrate import quad
import json
HERE=Path(__file__).resolve().parent
OUT=HERE if HERE.name=='figures' else HERE.parent/'courses/AN-06/public/figures'
OUT.mkdir(exist_ok=True)
k=1.0;c=.25;r0=2.0
r=np.geomspace(r0,1000,400)
q=np.sqrt(k*k-2*c/r)
def primitive(x):
 w=np.sqrt(k*k-2*c/x)
 return x*w-(2*c/k)*np.arctanh(w/k)
s=k*r0+primitive(r)-primitive(r0)-k*r
reference=-(c/k)*np.log(r/r0)
checks=[]
for x in [2,3,10,100,1000]:
 direct=quad(lambda t:np.sqrt(k*k-2*c/t)-k,r0,x,epsabs=1e-11)[0]
 exact=k*r0+primitive(x)-primitive(r0)-k*x
 assert abs(exact-direct)<2e-10
 checks.append({'radius':x,'phase_correction':float(exact),'quadrature_error':abs(exact-direct)})
plt.rcParams.update({'font.size':14,'axes.labelsize':15,'svg.fonttype':'none','svg.hashsalt':'AN06-radial-20261003'})
fig,ax=plt.subplots(2,1,figsize=(8,8.5),layout='constrained')
fig.suptitle('A small momentum error accumulates in the phase\n'+r'$k=1,\ c=1/4,\ R=2$',fontsize=17)
ax[0].plot(r,q,color='#1261a0',lw=2.5,label=r'$q(r)=\sqrt{1-1/(2r)}$')
ax[0].axhline(1,color='#a34712',ls='--',lw=1.8,label='free momentum: 1')
ax[0].set_xscale('log');ax[0].set_ylim(.84,1.02);ax[0].set_ylabel('outgoing momentum');ax[0].legend(loc='lower right',fontsize=12)
ax[1].plot(r,s,color='#1261a0',lw=2.5,label=r'exact $S(r)-r$')
ax[1].plot(r,reference,color='#a34712',ls='--',lw=1.8,label=r'leading comparison $-\frac{1}{4}\log(r/2)$')
ax[1].set_xscale('log');ax[1].set_ylabel('phase correction');ax[1].set_xlabel('exterior radius r');ax[1].legend(loc='lower left',fontsize=12)
for a in ax:a.grid(alpha=.2);a.set_xlim(r0,1000)
fig.savefig(OUT/'radial-coulomb-phase.png',dpi=150)
fig.savefig(OUT/'radial-coulomb-phase.svg',metadata={'Creator':'GPT-6.1 Sol (OpenAI), Ultra; CC0','Date':'2026-10-03'})
(OUT/'radial-coulomb-phase-check.json').write_text(json.dumps({'model':'Exterior radial Coulomb phase; Proposition8.2 in AN06-U041',
 'k':k,'c':c,'R':r0,'radius_range':[2,1000],'exact_primitive':'r*q-(2*c/k)*atanh(q/k)',
 'plotting_samples_not_a_proof':True,'checks':checks,'source_figure_reproduced':False},indent=2)+'\n',encoding='utf8')
print(json.dumps({'figure':'radial-coulomb-phase.png','direct_integral_checks':len(checks)}))
