"""Reproduce the exact scale exponents at e=1/4."""
from pathlib import Path
import hashlib, json
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

HERE = Path(__file__).resolve().parent
e = .25
x = np.linspace(0, .5, 401)
H = np.maximum(e, .5-x)
h = 2*H-1
square = 2*x+4*H-2
bracket = np.where(x <= .5-e, -.5+e, np.minimum(x-1+2*e, e-x))
plt.rcParams.update({'font.size': 12, 'svg.fonttype': 'none', 'font.family': 'DejaVu Sans'})
fig, ax = plt.subplots(2, 1, figsize=(11, 8), constrained_layout=True)
fig.suptitle('Complex cutoff: the square error and the sharp commutator scale', fontsize=16)
ax[0].plot(x,H,label='H exponent',color='#206b9a',lw=2.5)
ax[0].plot(x,h,label='Planck h exponent',color='#b26822',lw=2.5)
ax[0].plot(x,square,label='Square-error exponent',color='#20815f',lw=3)
ax[0].axhline(0,color='#333333',lw=1)
ax[0].set(title='A = R^α,  e = 1/4: the square error is uniformly bounded',ylabel='Power of R')
ax[0].legend(loc='lower right',ncol=3,fontsize=10)
ax[1].plot(x,bracket,color='#59378b',lw=3,label='Leading commutator bound, relative to s')
ax[1].axhline(-.5+1.5*e,color='#ae4052',lw=2,ls='--',label='Allowed β − s = −1/8')
ax[1].scatter([.375],[-.125],color='#59378b',zorder=3,s=45)
ax[1].annotate('Maximum at α = 3/8',(.375,-.125),xytext=(.20,-.16),arrowprops={'arrowstyle':'->','color':'#59378b'},fontsize=11)
ax[1].set(title='The two derivative regimes meet at the required weak order',ylabel='Power of R, after subtracting s',ylim=(-.31,-.08))
ax[1].legend(loc='lower left',fontsize=10)
for a in ax:
    a.set_xlim(0,.5); a.set_xlabel('α = log_R A'); a.grid(alpha=.2)
    a.set_xticks([0,.125,.25,.375,.5],['0','1/8','1/4','3/8','1/2'])
file=HERE/'adaptive-root-scales.svg'
fig.savefig(file,metadata={'Date':None,'Creator':'AN-04 original reproducible figure'})
plt.close(fig)
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
(HERE.parent/'figure-check.json').write_text(json.dumps({'svg':'figures/adaptive-root-scales.svg','svg_sha256':sha(file),'generator_sha256':sha(Path(__file__)),'actual_formulas':['H=max(e,1/2-alpha)','h=2H-1','square=2alpha+4H-2','bracket=-1/2+e for alpha<=1/2-e; otherwise min(alpha-1+2e,e-alpha)'],'e':'1/4','scope':'Exact exponent bounds, not operator norm equalities.'                           },indent=2)+'\n','utf-8')
print(json.dumps({'figure':str(file),'sha256':sha(file)}))
