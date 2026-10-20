"""Exact multiplier formulas; plotted samples illustrate the accompanying proof.

Original figure: GPT-6.1 Sol (OpenAI), CC0-1.0.
"""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

matplotlib.rcParams.update({'svg.fonttype':'none','svg.hashsalt':'AN04-sign-roots',
    'font.size':11,'axes.titlesize':12,'axes.labelsize':11,'axes.unicode_minus':False})
x=np.linspace(-1,1,1601)
fig,axes=plt.subplots(1,2,figsize=(10,3.5),layout='constrained')
for ax in axes:
    ax.axhline(0,color='#64748b',linewidth=.7)
    ax.axvline(0,color='#64748b',linewidth=.7)
    ax.set_xlim(-1,1);ax.set_xticks([-1,-.5,0,.5,1]);ax.set_xlabel('spatial coordinate x')
    ax.grid(alpha=.15)
axes[0].plot(x,x,color='#1d4ed8',linewidth=2.3,label='B0: x')
axes[0].set_ylim(-1.08,1.08);axes[0].set_ylabel('multiplier value')
axes[0].set_title('Smooth order-zero symbol');axes[0].legend(loc='upper left')
axes[1].plot(x,np.sqrt(np.maximum(x,0)),color='#b91c1c',linewidth=2.4,label='S+: sqrt(max(x, 0))')
axes[1].plot(x,np.sqrt(np.maximum(-x,0)),color='#047857',linewidth=2.4,linestyle='--',label='S-: sqrt(max(-x, 0))')
axes[1].scatter([0],[0],color='#0f172a',s=22,zorder=4)
axes[1].set_ylim(-.05,1.08);axes[1].set_ylabel('sign-root multiplier value')
axes[1].set_title('Continuous roots; not differentiable at zero')
axes[1].legend(loc='upper center',fontsize=9)
axes[1].annotate('x = 0',xy=(0,0),xytext=(.18,.16),arrowprops={'arrowstyle':'->','color':'#475569'},color='#334155')
fig.savefig(Path(__file__).resolve().parent/'sign-root-multipliers.svg',
    metadata={'Date':None,'Creator':'GPT-6.1 Sol (OpenAI); original CC0 figure',
              'Title':'Smooth multiplication operator and its nonsmooth sign square roots'})
plt.close(fig)
