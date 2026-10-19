"""Exact illustrative coordinates for AN01-U083, equation (24), Exercises 2–3.
CC0. GPT-6 Astra (OpenAI), Ultra. Arrows are Euclidean displays of covectors.
"""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

out=Path(__file__).resolve().parent
plt.rcParams.update({'font.size':11,'font.family':'DejaVu Sans','svg.fonttype':'none'})
fig,axes=plt.subplots(1,2,figsize=(11.6,4.7),layout='constrained')
s=np.linspace(-1.35,1.35,361)
ax=axes[0]
ax.plot(s,s*s,color='#173e66',lw=2.2,label=r'$t=s^2$')
for q in [-1,-.5,0,.5,1]:
    for sign in [-1,1]:
        v=.22*sign*np.array([-2*q,1.])
        ax.annotate('',xy=(q+v[0],q*q+v[1]),xytext=(q,q*q),
                    arrowprops=dict(arrowstyle='->',color='#a5392b',lw=1.4))
    ax.plot(q,q*q,'o',color='#173e66',ms=3)
ax.text(-1.58,2.05,r'$(-2s,1)\cdot(1,2s)=0$',fontsize=12)
ax.text(-1.58,-.55,r'Arrow displacements: $\pm\,0.22(-2s,1)$',fontsize=10)
ax.set(xlim=(-1.65,1.65),ylim=(-.7,2.3),xlabel=r'$s$',ylabel=r'$t$',
       title='A level set and its conormals')
ax.set_aspect('equal',adjustable='box')
ax=axes[1]
ax.plot(s,s*s,color='#173e66',lw=2.2,label=r'$j(r)=(r,r^2)$')
ax.axvline(0,color='#797d86',lw=1.4,ls='--',label=r'$\operatorname{supp}\delta_0(y_1)$')
ax.annotate('',xy=(1,0),xytext=(0,0),arrowprops=dict(arrowstyle='->',color='#a5392b',lw=2.2))
ax.annotate('',xy=(0,1),xytext=(0,0),arrowprops=dict(arrowstyle='->',color='#22776f',lw=2.2))
ax.text(.42,-.2,r'$\eta=(1,0)$',color='#a5392b')
ax.text(.08,.75,r'$(0,1)\in\ker Dj(0)^T$',color='#22776f',fontsize=10)
ax.text(-1.58,2.05,r'$Dj(0)^T(\eta_1,\eta_2)=\eta_1$',fontsize=12)
ax.text(-1.58,-.55,r'Singular covector: $(1,0)\mapsto 1$',fontsize=10)
ax.plot(0,0,'o',color='#173e66',ms=4)
ax.set(xlim=(-1.65,1.65),ylim=(-.7,2.3),xlabel=r'$y_1$',ylabel=r'$y_2$',
       title='A transverse restriction at the origin')
ax.set_aspect('equal',adjustable='box')
for ax in axes:
    ax.grid(alpha=.18)
    ax.spines[['top','right']].set_visible(False)
    ax.legend(loc='upper center',bbox_to_anchor=(.5,-.21),frameon=False,fontsize=10)
fig.savefig(out/'analytic-pullback-covectors.png',dpi=230)
fig.savefig(out/'analytic-pullback-covectors.svg')
p=out/'analytic-pullback-covectors.svg'
p.write_text('\n'.join(line.rstrip() for line in p.read_text().splitlines())+'\n',encoding='utf-8')
