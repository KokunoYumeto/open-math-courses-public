"""Reproduce Figure22.15 from the exact recurrence and proved tail bound."""
from pathlib import Path
import json
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

root=Path(__file__).parent
data=json.loads((root/'elliptic-canonical-height-check.json').read_text(encoding='utf-8'))['numerical']['telescope'][1:]
r=np.array([d['r'] for d in data])
centers=np.array([float(d['center']) for d in data])
lower=np.array([float(d['lower']) for d in data])
upper=np.array([float(d['upper']) for d in data])
width=np.array([float(d['width']) for d in data])
assert np.all(lower<=centers) and np.all(centers<=upper)
fig,axes=plt.subplots(1,2,figsize=(11.4,4.9),layout='constrained')
axes[0].errorbar(r,centers,yerr=[centers-lower,upper-centers],fmt='o',capsize=5,color='#286f9f',ecolor='#286f9f')
axes[0].set(title='Certified intervals for the canonical height',xlabel=r'Doublings $r$',ylabel=r'Height in the $3O$ normalization',xticks=r)
axes[0].grid(alpha=.2)
axes[1].semilogy(r,width,'o-',color='#b45c28',linewidth=2)
axes[1].set(title='Geometric decay of the interval width',xlabel=r'Doublings $r$',ylabel='Interval width (logarithmic scale)',xticks=r)
axes[1].grid(alpha=.2)
fig.suptitle(r'$P=(3,10)$ on $Y^2=4x^3-8$; exact endpoints defined by (22.578)',fontsize=13)
fig.savefig(root/'elliptic-height-telescope.png',dpi=170,bbox_inches='tight')
plt.close(fig)
print('Figure22.15 saved: elliptic-height-telescope.png')
