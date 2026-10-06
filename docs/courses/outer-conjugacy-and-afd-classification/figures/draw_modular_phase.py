"""Exact phase geometry for Section 5; no approximation to operator algebras.

p=2, s=L/2, t=P/2, LP=2*pi. Raw phase=-i, correction=i,
untwisted obstruction=1. All plotted marked coordinates are exact.
"""
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import Circle,Arc,FancyArrowPatch

DEST=Path(__file__).resolve().parent
plt.rcParams.update({'font.family':'DejaVu Sans','font.size':20,
                    'svg.fonttype':'path','svg.hashsalt':'modular-phase-correction-v1'})
fig,axes=plt.subplots(2,1,figsize=(6.8,11.6),layout='constrained')
fig.suptitle(r'$p=2,\quad s=L/2,\quad t=P/2,\quad LP=2\pi$',fontsize=20)
raw='#a43c22';corrected='#176b4b'
for ax in axes:
    ax.set_aspect('equal')
    ax.set_xlim(-1.6,1.7);ax.set_ylim(-1.6,1.55)
    ax.axis('off')
    ax.add_patch(Circle((0,0),1,fill=False,edgecolor='#8b9cac',linewidth=2))
    ax.plot([-1.2,1.2],[0,0],color='#c6d0d9',linewidth=1)
    ax.plot([0,0],[-1.2,1.2],color='#c6d0d9',linewidth=1)
    ax.text(0,1.18,r'$i$',ha='center',fontsize=21,color='#455769')
axes[0].set_title('Correct the phase',fontsize=25,pad=12)
axes[0].scatter([0],[ -1],s=120,color=raw,zorder=5)
axes[0].scatter([1],[0],s=120,color=corrected,zorder=5)
axes[0].text(-.15,-1.3,r'$\gamma=-i$',ha='center',color=raw,fontsize=26)
axes[0].text(1.05,.24,r'$\delta=1$',ha='center',color=corrected,fontsize=26)
axes[0].add_patch(Arc((0,0),1.42,1.42,theta1=-90,theta2=0,linewidth=3,color=corrected))
axes[0].add_patch(FancyArrowPatch((.69,-.2),(.71,0),arrowstyle='-|>',mutation_scale=20,linewidth=2,color=corrected))
axes[0].text(.06,-.31,r'$\times i$',color=corrected,fontsize=27)
axes[0].text(0,1.45,r'$\delta=\gamma a^{-it}$',ha='center',fontsize=23)
axes[1].set_title('Compare the squares',fontsize=25,pad=12)
axes[1].scatter([-1],[0],s=120,color=raw,zorder=5)
axes[1].scatter([1],[0],s=120,color=corrected,zorder=5)
axes[1].text(-1,.26,r'$\gamma^2=-1$',ha='center',color=raw,fontsize=24)
axes[1].text(1,-.35,r'$\delta^2=1$',ha='center',color=corrected,fontsize=24)
axes[1].text(0,-1.35,r'$\gamma^p=a^{ipt},\qquad\delta^p=1$',ha='center',fontsize=23)
fig.savefig(DEST/'modular-phase-correction.svg',metadata={'Date':None,'Creator':'Matplotlib','Description':'Exact order-two modular phase correction, Section 5.'})
fig.savefig(DEST/'modular-phase-correction.png',dpi=190,metadata={'Software':'Matplotlib'})
plt.close(fig)
