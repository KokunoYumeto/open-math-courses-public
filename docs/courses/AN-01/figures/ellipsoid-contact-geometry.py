"""Exact linear image of the square and its inscribed and outer ellipses."""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

T=np.array([[2.,1.],[0.,1.]])
theta=np.linspace(0,2*np.pi,1001)
circle=np.array([np.cos(theta),np.sin(theta)])
ellipse=T@circle
square=T@np.array([[-1,1,1,-1,-1],[-1,-1,1,1,-1]])
fig,axes=plt.subplots(1,2,figsize=(12.4,5.2),constrained_layout=True)
for ax in axes:
    ax.fill(square[0],square[1],color='#eaf0fa',zorder=0)
    ax.plot(square[0],square[1],color='#18395c',lw=2)
    ax.plot(ellipse[0],ellipse[1],color='#087e8b',lw=2.3)
    ax.axhline(0,color='#b6c0c8',lw=.7,zorder=-1)
    ax.axvline(0,color='#b6c0c8',lw=.7,zorder=-1)
    ax.set_aspect('equal')
    ax.set_xlabel(r'$x_1$');ax.set_ylabel(r'$x_2$')
    ax.grid(alpha=.15)
    ax.spines[['top','right']].set_visible(False)
axes[0].plot(np.sqrt(2)*ellipse[0],np.sqrt(2)*ellipse[1],
             '--',color='#bb5533',lw=1.8,label=r'$\sqrt{2}E$')
axes[0].plot([],[],color='#087e8b',lw=2.3,label=r'$E=TB$')
axes[0].plot([],[],color='#18395c',lw=2,label=r'$K=T[-1,1]^2$')
axes[0].scatter(square[0,:4],square[1,:4],color='#bb5533',s=27,zorder=4)
axes[0].annotate(r'$(3,1)$: $q=\sqrt{2}$',xy=(3,1),xytext=(.9,1.87),
                 arrowprops=dict(arrowstyle='-',color='#555'),
                 bbox=dict(facecolor='white',edgecolor='none',alpha=.95))
axes[0].legend(loc='lower left',fontsize=10)
axes[0].set_xlim(-3.6,3.6);axes[0].set_ylim(-2.1,2.25)
axes[0].set_title('The sharp containment',fontsize=13,pad=14)
contact=T@np.eye(2)
axes[1].scatter([2,-2,1,-1],[0,0,1,-1],color='#087e8b',s=32,zorder=4)
axes[1].annotate(r'$z_1=(2,0)$',xy=(2,0),xytext=(2.05,.32),
                 fontsize=10,bbox=dict(facecolor='white',edgecolor='none',alpha=.95))
axes[1].annotate(r'$z_2=(1,1)$',xy=(1,1),xytext=(1.3,1.55),
                 arrowprops=dict(arrowstyle='-',color='#555'),fontsize=10,
                 bbox=dict(facecolor='white',edgecolor='none',alpha=.95))
for vec in [np.array([.5,-.5]),np.array([0,1.])]:
    axes[1].annotate('',xy=vec,xytext=(0,0),
                     arrowprops=dict(arrowstyle='->',color='#8a377b',lw=2))
axes[1].text(.58,-.70,r'$\eta_1=(1/2,-1/2)$',fontsize=10,
             bbox=dict(facecolor='white',edgecolor='none',alpha=.95))
axes[1].text(-.18,1.18,r'$\eta_2=(0,1)$',ha='right',fontsize=10,
             bbox=dict(facecolor='white',edgecolor='none',alpha=.95))
axes[1].text(-3.3,-1.82,r'$|\eta_1\cdot x|\leq1,\quad|\eta_2\cdot x|\leq1$',
             fontsize=11)
axes[1].set_xlim(-3.6,3.9);axes[1].set_ylim(-2.1,2.25)
axes[1].set_title('Contacts and supporting covectors',fontsize=13,pad=14)
out=Path(__file__).resolve().parent
for ext in ['svg','png']:
    fig.savefig(out/f'ellipsoid-contact-geometry.{ext}',dpi=160,
                metadata={'Creator':'GPT-6 Astra (OpenAI)'} if ext=='svg' else None)
    if ext=='svg':
        svg=out/'ellipsoid-contact-geometry.svg'
        svg.write_text('\n'.join(line.rstrip() for line in svg.read_text(encoding='utf-8').splitlines())+'\n',encoding='utf-8',newline='\n')
