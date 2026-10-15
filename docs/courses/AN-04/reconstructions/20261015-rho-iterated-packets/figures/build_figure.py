"""Original Fourier-packet and exact order-gap figure; no embedded fonts."""
from pathlib import Path
import json,hashlib
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
ROOT=Path(__file__).resolve().parents[1]
plt.rcParams.update({'svg.fonttype':'none','font.family':'DejaVu Sans','font.size':10.5})
fig,axes=plt.subplots(1,3,figsize=(13.2,4.4),layout='constrained')
ax=axes[0];z=np.linspace(-18,18,6001);profile=np.zeros_like(z);inside=np.abs(z)<1
profile[inside]=np.exp(1-1/(1-z[inside]**2))
ax.plot(z,profile,color='#186f80',lw=2)
ax.axvline(-16,color='#89959e',ls='--');ax.axvline(16,color='#89959e',ls='--')
ax.set(xlim=(-18,18),ylim=(0,1.2),xlabel='normalized frequency offset z',ylabel='unit-height Fourier profile',
 title='A packet inside a much wider shell\nρ = 3/4, R = 65536')
ax.set_xticks([-16,0,16],['−16','0','16'])
ax.text(0,1.08,'width R^ρ = 4096; height multiplier R^a',ha='center',fontsize=9)
ax.text(0,.4,'shell-distance scale R^(1−ρ) = 16',ha='center',fontsize=9)
ax=axes[1];r=np.linspace(.5,1,201)
ax.plot(r,(1-r)/2,label='n = 1',color='#84589e',lw=2)
ax.plot(r,1-r,label='n = 2',color='#23774e',lw=2)
ax.set(xlim=(.5,1),ylim=(0,.53),xlabel='ρ',ylabel='order difference δn/2',
 title='The exact height/order gap\n(1−ρ)n/2')
ax.plot([.5,.5],[.25,.5],'o',mfc='white',mec='#71808d',ms=6)
ax.legend(frameon=False);ax.grid(alpha=.2)
ax=axes[2];ax.bar([0,1],[.5,.25],color=['#186f80','#23774e'],width=.55)
ax.hlines(.25,-.35,1.35,color='#71808d',ls='--',lw=1)
ax.annotate('gap = 1/4',xy=(.65,.5),xytext=(.65,.25),ha='center',va='bottom',
 arrowprops={'arrowstyle':'<->','color':'#84589e'},color='#84589e',fontsize=10)
ax.set(xticks=[0,1],xticklabels=['actual / fixed\nendpoint','exact cell\nallowance'],ylim=(0,.62),
 ylabel='power of R in the L² norm',title='X1: n = 2, ρ = 3/4, m = 0')
ax.text(0,.53,'M = 1/2',ha='center');ax.text(1,.28,'q + ρn/2 = 1/4',ha='center',fontsize=9)
fig.suptitle('Annular size does not fix the height of a narrow packet',fontsize=14)
p=ROOT/'figures/iterated-packet-scales.svg';fig.savefig(p,metadata={'Date':None});plt.close(fig)
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
(ROOT/'figure-check.json').write_text(json.dumps({'svg':'figures/iterated-packet-scales.svg',
 'svg_sha256':sha(p),'generator_sha256':sha(Path(__file__)),'actually_inspected':False,
 'data':'IP18–IP20 with rho=3/4,R=65536, exact bump profile; exact gap delta*n/2; X1 powers 1/2 and 1/4.',
 'qualification':'First panel uses normalized Fourier offsets and unit height; remaining panels plot exact exponents, not a numerical proof.',
 'embedded_fonts':False,'original_expression_licence':'CC0-1.0'},indent=2)+'\n','utf-8')
print(json.dumps({'svg_bytes':p.stat().st_size}))
