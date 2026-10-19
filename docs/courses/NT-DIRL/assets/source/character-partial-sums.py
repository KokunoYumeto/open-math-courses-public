"""Original CC0 exact Legendre partial-sum plot; no source figure copied."""
from pathlib import Path
import math
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
out=Path(__file__).resolve().parents[1]
plt.rcParams.update({'font.family':'DejaVu Sans','font.size':20,'axes.labelsize':20,'axes.titlesize':24,'xtick.labelsize':17,'ytick.labelsize':18,'svg.fonttype':'none'})
fig,axes=plt.subplots(3,1,figsize=(10,10.7),constrained_layout=True)
for ax,p,color in zip(axes,[7,11,23],['#126b91','#8c4c12','#5a428d']):
 values=[0]+[0 if n%p==0 else (1 if pow(n,(p-1)//2,p)==1 else -1) for n in range(1,p+1)]
 sums=np.cumsum(values)
 ax.step(range(p+1),sums,where='post',color=color,linewidth=2.8)
 ax.scatter(range(p+1),sums,color=color,s=42,zorder=3)
 ax.axhline(0,color='#777777',linewidth=1)
 ax.set(xlim=(-.2,p+.2),ylim=(-.25,max(sums)+.9),xlabel=r'Integer endpoint $n$',ylabel=r'$S(n)$')
 ax.set_xticks(range(0,p+1,1 if p<12 else 2))
 ax.set_yticks(range(max(sums)+1))
 ax.grid(axis='y',alpha=.2)
 first=next(n for n in range(1,p) if values[n]==-1)
 ax.set_title(rf'$p={p}$: maximum $S(n)={max(sums)}$, least nonresidue $={first}$',loc='left',pad=12)
 ax.text(.98,.97,rf'$\sqrt{{p}}\log p\approx {math.sqrt(p)*math.log(p):.3f}$',ha='right',va='top',transform=ax.transAxes,fontsize=19,bbox={'facecolor':'white','edgecolor':'none','alpha':.9})
 ax.spines[['top','right']].set_visible(False)
fig.savefig(out/'character-partial-sums.png',dpi=160,metadata={'Author':'GPT-6.1 Sol (OpenAI), Codex, Ultra','Description':'Original CC0 exact Legendre partial-sum diagram for Character sums, equation (3.3).'})
fig.savefig(out/'character-partial-sums.svg',metadata={'Creator':'GPT-6.1 Sol (OpenAI), Codex, Ultra','Description':'Original CC0 diagram; rendered DejaVu glyphs retain their font licence.'})
plt.close(fig)
print('Generated exact character partial-sum PNG and SVG.')
