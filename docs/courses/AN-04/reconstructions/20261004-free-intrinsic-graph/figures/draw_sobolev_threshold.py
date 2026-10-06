"""Exact samples from S13–S15; no image-generation or fitted data."""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

out=Path(__file__).resolve().parent
j=np.arange(16,197)
height=np.log(j+1)
width=np.exp(-np.sqrt(j))
energy=height**2*width
plt.rcParams.update({'font.family':'DejaVu Sans','font.size':12,'svg.fonttype':'path'})
fig,ax=plt.subplots(3,1,figsize=(5.5,9.2),layout='constrained')
items=[
 (height,r'$h_j=\log(j+1)$','Normalized peak height',False),
 (width,r'$w_j/R_j=e^{-\sqrt{j}}$','Relative support radius',True),
 (energy,r'$h_j^2e^{-\sqrt{j}}$','Energy bound factor, n = 1',True)]
for a,(y,label,title,log) in zip(ax,items):
 a.plot(j,y,color='#12677a',lw=2.4,label=label)
 a.scatter(j[::20],y[::20],color='#ca652b',s=18,zorder=3)
 if log:a.set_yscale('log')
 a.set_title(title,fontsize=12,pad=12)
 a.set_xlabel('Bump index j')
 a.grid(alpha=.22)
 a.legend(loc='best',frameon=False,fontsize=11)
 a.spines[['top','right']].set_visible(False)
fig.suptitle('Growing peaks, summable weighted mass',fontsize=13)
fig.savefig(out/'sobolev-threshold.svg')
fig.savefig(out/'sobolev-threshold.png',dpi=150)
print('Wrote exact sequence samples, j = 16,...,196.')
