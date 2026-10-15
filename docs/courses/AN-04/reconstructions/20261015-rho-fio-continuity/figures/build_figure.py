"""Original exact-scale illustration. All fonts remain SVG text."""
from pathlib import Path
import hashlib,json
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle
ROOT=Path(__file__).resolve().parents[1]
plt.rcParams.update({'svg.fonttype':'none','font.family':'DejaVu Sans','font.size':11})
fig,axes=plt.subplots(1,3,figsize=(13.2,4.5),layout='constrained')
ax=axes[0];ax.add_patch(Rectangle((-.5,-8),1,16,facecolor='#c8e7e6',edgecolor='#17736f',lw=2))
ax.axhline(0,color='#697a88',lw=.7);ax.axvline(0,color='#697a88',lw=.7)
ax.set(xlim=(-.85,.85),ylim=(-12,12),xlabel='base offset x − x₀',ylabel='frequency offset η − η₀',
       title='Normalized metric box\nρ = 3/4, r = 16')
ax.set_xticks([-.5,0,.5],['−1/2','0','1/2']);ax.set_yticks([-8,0,8])
ax.text(0,9.2,'half-widths: 1/2 and 8',ha='center',fontsize=10)
ax=axes[1];k=np.arange(7);m=-k/4
ax.fill_between(k,-2,m,color='#dbeedd');ax.plot(k,m,'o-',color='#216c48',lw=2)
ax.set(xlim=(0,6),ylim=(-2,.2),xlabel='corank k',ylabel='operator order m',title='Sufficient L² range\nm ≤ −k/4')
ax.set_xticks(k);ax.grid(alpha=.2);ax.text(2,-1.65,'radial exclusion assumed',ha='center',fontsize=10)
ax=axes[2];N=np.arange(129);error=1/np.log(2+np.sqrt(1+(N+1)**2))
ax.plot(N,error,color='#8253a3',lw=2)
ax.set(xlabel='Fourier cutoff N',ylabel='exact operator norm error',title='Compact approximation\n1 / log(2 + √(1+(N+1)²))')
ax.set_xlim(0,128);ax.set_ylim(0,1);ax.grid(alpha=.2)
fig.suptitle('Continuity follows the normalized scales',fontsize=15)
p=ROOT/'figures/continuity-scales.svg';fig.savefig(p,metadata={'Date':None});plt.close(fig)
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
(ROOT/'figure-check.json').write_text(json.dumps({'svg':'figures/continuity-scales.svg',
 'svg_sha256':sha(p),'generator_sha256':sha(Path(__file__)),'actually_inspected':False,
 'data':'GC3 and GC14 at rho=3/4,r=16; GC25 at integer k=0..6; exact GC28 for N=0..128.',
 'schematic':'First panel is a normalized metric box, not a canonical relation; second is a sufficient range only.',
 'embedded_fonts':False,'original_expression_licence':'CC0-1.0'},indent=2)+'\n','utf-8')
print(json.dumps({'svg_bytes':p.stat().st_size}))
