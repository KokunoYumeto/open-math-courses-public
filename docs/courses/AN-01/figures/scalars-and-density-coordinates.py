"""Coordinate change y=3 exp(x) and density 1/y. GPT-6 Astra; CC0."""
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
plt.rcParams['svg.hashsalt']='AN01-scalars-and-density-coordinates'
out=Path(__file__).parent if __file__.endswith('scalars-and-density-coordinates.py') else Path(__file__).parent/'advanced-U179-20261020/new'
out.mkdir(exist_ok=True,parents=True)
fig,axes=plt.subplots(1,2,figsize=(10.4,4.5),layout='constrained')
fig.patch.set_facecolor('#f8fafc')
x=np.linspace(-1,1,400);y=3*np.exp(x)
axes[0].plot(x,y,color='#176689',lw=2.6)
axes[0].scatter([0],[3],s=45,color='#b24b21',zorder=3)
axes[0].annotate('(0, 3)',(0,3),xytext=(.17,2.2),fontsize=12)
axes[0].set(title='The coordinate map',xlabel='x',ylabel='y = 3 exp(x)',xlim=(-1.12,1.12),ylim=(0,9))
axes[0].set_xticks([-1,0,1])
axes[0].text(-.96,7.5,r'$dy/dx=3e^x$',fontsize=15)
axes[1].plot(y,1/y,color='#176689',lw=2.6)
axes[1].fill_between(y,0,1/y,color='#dceaf3')
axes[1].scatter([3],[1/3],s=45,color='#b24b21',zorder=3)
axes[1].annotate('(3, 1/3)',(3,1/3),xytext=(4,.45),fontsize=12)
axes[1].set(title='The density coefficient',xlabel='y',ylabel='dx/dy = 1/y',xlim=(.7,8.6),ylim=(0,1.04))
axes[1].text(3.8,.82,r'$\int_{3/e}^{3e}dy/y=2$',fontsize=15)
axes[1].set_xticks([3/np.e,3,3*np.e],['3/e','3','3e'])
for ax in axes:
    ax.set_facecolor('#f8fafc');ax.spines[['top','right']].set_visible(False)
    ax.grid(alpha=.17);ax.set_axisbelow(True)
for ext in ['png','svg']:
    fig.savefig(out/('scalars-and-density-coordinates.'+ext),dpi=175,
                metadata={'Date':'2026-10-20'} if ext=='svg' else None)
svg=out/'scalars-and-density-coordinates.svg'
svg.write_text('\n'.join(line.rstrip() for line in svg.read_text(encoding='utf-8').splitlines())+'\n',encoding='utf-8')
plt.close(fig)
