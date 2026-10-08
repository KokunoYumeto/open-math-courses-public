"""Invariant quadratic/cubic tensors for S3, Figure 133.1. CC0-1.0 code.
Run with Python, numpy and matplotlib. Outputs are next to this script.
"""
from pathlib import Path
import json
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

OUT=Path(__file__).resolve().parent
plt.rcParams.update({'font.family':'DejaVu Sans','mathtext.fontset':'dejavusans','font.size':12,'svg.fonttype':'path','svg.hashsalt':'OA-FLOW-compact-tannaka-v1'})
fig,(ax,curve)=plt.subplots(1,2,figsize=(12,5.7),layout='constrained',gridspec_kw={'width_ratios':[1,1.25]})
t=np.linspace(0,2*np.pi,721)
ax.plot(np.cos(t),np.sin(t),color='#a4adb7',lw=1.3)
angles=np.arange(4)*2*np.pi/3
ax.plot(np.cos(angles),np.sin(angles),'-o',color='#15805c',lw=2.5,ms=8,label=r'$p=1$')
ax.plot(np.cos(angles+np.pi/3),np.sin(angles+np.pi/3),'--o',color='#b63737',lw=2,ms=6,label=r'rotate by $\pi/3$: $p=-1$')
for a in np.arange(3)*2*np.pi/3:
    ax.plot([0,np.cos(a)],[0,np.sin(a)],':',color='#15805c',alpha=.6)
ax.annotate(r'$e_1$',xy=(1,0),xytext=(1.14,.12),fontsize=14)
ax.annotate(r'$R_{\pi/3}e_1$',xy=(.5,np.sqrt(3)/2),xytext=(.55,1.17),fontsize=14)
ax.set(xlim=(-1.35,1.6),ylim=(-1.4,1.45),aspect='equal',xticks=[],yticks=[])
ax.spines[['top','right','left','bottom']].set_visible(False)
ax.set_title('The cubic selects a triangle',fontsize=16)
ax.legend(loc='lower center',frameon=False,bbox_to_anchor=(.5,-.08))
curve.plot(t,np.cos(3*t),color='#1268b3',lw=2.5)
curve.axhline(0,color='#a4adb7',lw=.8)
curve.scatter(np.arange(3)*2*np.pi/3,np.ones(3),c='#15805c',s=60,zorder=3)
curve.scatter((np.arange(3)*2+1)*np.pi/3,-np.ones(3),c='#b63737',s=50,zorder=3)
curve.set(xlim=(-.12,2*np.pi+.12),ylim=(-1.22,1.25),yticks=[-1,0,1],xticks=np.arange(7)*np.pi/3,
          xticklabels=['0',r'$\pi/3$',r'$2\pi/3$',r'$\pi$',r'$4\pi/3$',r'$5\pi/3$',r'$2\pi$'])
curve.set_xlabel(r'Angle $\theta$ on the unit circle')
curve.set_title(r'$p(\cos\theta,\sin\theta)=\cos(3\theta)$',fontsize=16)
curve.spines[['top','right']].set_visible(False)
curve.grid(axis='x',color='#e4e8ec',lw=.8)
fig.suptitle('Invariant tensors recover the six symmetries of $S_3$\n'+r'Quadratic: $O(2)$     +     cubic: $x^3-3xy^2$',fontsize=19)
fig.savefig(OUT/'invariant-tensors.png',dpi=160,facecolor='white')
fig.savefig(OUT/'invariant-tensors.svg',facecolor='white',metadata={'Date':None})
(OUT/'data.json').write_text(json.dumps({'polynomial':'x^3-3*x*y^2','circle_restriction':'cos(3*theta)','maxima_angles':['0','2*pi/3','4*pi/3'],'counterexample_angle':'pi/3','counterexample_values':[1,-1]},indent=2),encoding='utf-8')
plt.close(fig)
