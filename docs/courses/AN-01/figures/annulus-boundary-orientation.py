"""Outward-first annulus boundary orientation. GPT-6 Astra; CC0."""
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import Wedge, FancyArrowPatch
import numpy as np
plt.rcParams['svg.hashsalt']='AN01-annulus-boundary-orientation'
out=Path(__file__).parent
fig,ax=plt.subplots(figsize=(7.8,6.4),layout='constrained')
fig.patch.set_facecolor('#f8fafc');ax.set_facecolor('#f8fafc')
ax.add_patch(Wedge((0,0),2,0,360,width=1,facecolor='#dcecf3',edgecolor='none'))
t=np.linspace(0,2*np.pi,401)
for radius in [1,2]:
    ax.plot(radius*np.cos(t),radius*np.sin(t),color='#176689',lw=2)
    for theta in [.45*np.pi,1.2*np.pi]:
        start=theta-.11 if radius==2 else theta+.11
        end=theta+.11 if radius==2 else theta-.11
        ax.add_patch(FancyArrowPatch((radius*np.cos(start),radius*np.sin(start)),
                                    (radius*np.cos(end),radius*np.sin(end)),
                                    arrowstyle='-|>',mutation_scale=19,lw=2,color='#176689',
                                    connectionstyle='arc3,rad='+('-.1' if radius==2 else '.1')))
    theta=-.2*np.pi
    p=radius*np.array([np.cos(theta),np.sin(theta)])
    q=p+(.42 if radius==2 else -.42)*np.array([np.cos(theta),np.sin(theta)])
    ax.annotate('',xy=q,xytext=p,arrowprops=dict(arrowstyle='->',lw=2,color='#b45025'))
ax.text(2.25,.65,r'outer: $+2\pi$',fontsize=13,color='#176689',ha='left')
ax.annotate('',xy=(1.85,.72),xytext=(2.2,.7),arrowprops=dict(arrowstyle='-',color='#176689'))
ax.text(-.1,.03,r'inner: $-2\pi$',fontsize=13,color='#176689',ha='center')
ax.text(1.55,-1.7,'outward normals',fontsize=11,color='#b45025',ha='left')
ax.text(-2.5,-2.55,r'$\det(n_{\rm out},v_{\rm boundary})>0$',fontsize=14)
ax.set(xlim=(-2.8,4),ylim=(-2.85,2.55),aspect='equal',xlabel='x',ylabel='y')
ax.set_title(r'$M=\{1<x^2+y^2<4\}$, orientation $dx\wedge dy$'+'\n'+
             r'$\alpha=(-y\,dx+x\,dy)/(x^2+y^2),\quad d\alpha=0$',fontsize=14,pad=13)
ax.spines[['top','right']].set_visible(False);ax.grid(alpha=.14);ax.set_axisbelow(True)
for ext in ['png','svg']:
    fig.savefig(out/('annulus-boundary-orientation.'+ext),dpi=175,
                metadata={'Date':'2026-10-20'} if ext=='svg' else None)
svg=out/'annulus-boundary-orientation.svg'
svg.write_text('\n'.join(line.rstrip() for line in svg.read_text(encoding='utf-8').splitlines())+'\n',encoding='utf-8')
plt.close(fig)
