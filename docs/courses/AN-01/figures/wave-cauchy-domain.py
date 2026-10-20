"""Backward wave dependence, c=2, T=1. Original figure: GPT-6 Astra; CC0."""
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
plt.rcParams['svg.hashsalt']='AN01-wave-cauchy-domain'
out=Path(__file__).parent if __file__.endswith('wave-cauchy-domain.py') else Path(__file__).parent/'advanced-U178-20261020/new'
out.mkdir(exist_ok=True,parents=True)
fig,ax=plt.subplots(figsize=(8.4,5.1),layout='constrained')
fig.patch.set_facecolor('#f8fafc');ax.set_facecolor('#f8fafc')
s=np.linspace(0,1,300);r=2*(1-s)
ax.fill_betweenx(s,-r,r,color='#dceaf3')
ax.plot(-r,s,color='#196485',lw=2);ax.plot(r,s,color='#196485',lw=2)
ax.plot([-2,2],[0,0],color='#ac4e22',lw=4,label='initial-data region')
ax.plot([-.8,.8],[.6,.6],color='#196485',lw=3)
ax.scatter([0],[1],color='#14364b',s=50,zorder=4)
ax.annotate('observation (1, 0)',(0,1),xytext=(.35,1.12),fontsize=12)
ax.text(0,.67,r'$|y|\leq 2(1-s)$',ha='center',fontsize=15)
ax.text(0,.51,r'$s=0.6:\quad -0.8\leq y\leq0.8$',ha='center',fontsize=12)
ax.text(0,.23,'possible forcing dependence',ha='center',fontsize=13,color='#196485')
ax.text(0,-.13,r'initial data: $-2\leq y\leq2$',ha='center',fontsize=13,color='#943d17')
ax.set(xlim=(-2.55,2.55),ylim=(-.23,1.27),xlabel='spatial coordinate y',ylabel='source time s')
ax.set_title('A compact backward cone',loc='left',fontsize=18,pad=15)
ax.set_xticks([-2,-1,0,1,2]);ax.set_yticks([0,.6,1])
ax.spines[['top','right']].set_visible(False)
ax.grid(alpha=.17);ax.set_axisbelow(True)
for ext in ['png','svg']:
    fig.savefig(out/('wave-cauchy-domain.'+ext),dpi=175,
                metadata={'Date':'2026-10-20'} if ext=='svg' else None)
svg=out/'wave-cauchy-domain.svg'
svg.write_text('\n'.join(line.rstrip() for line in svg.read_text(encoding='utf-8').splitlines())+'\n',encoding='utf-8')
plt.close(fig)
