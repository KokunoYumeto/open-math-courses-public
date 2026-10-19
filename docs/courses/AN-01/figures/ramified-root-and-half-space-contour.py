"""Ramified root and oriented characteristic contour; AN01-U088 Lemmas 1,4. CC0."""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import Circle, Rectangle
plt.rcParams.update({'font.family':'DejaVu Sans','font.size':12,'svg.fonttype':'none'})
fig,axs=plt.subplots(1,2,figsize=(13,6),layout='constrained')
fig.set_facecolor('#f8fafc')
ax=axs[0];ax.set_aspect('equal')
ax.axhline(0,color='#bec8d0',lw=.8);ax.axvline(0,color='#bec8d0',lw=.8)
colors=['#215f7a','#b25d31','#744a85']
for k in range(3):
 t=np.linspace(k*2*np.pi/3,(k+1)*2*np.pi/3,180)
 ax.plot(np.cos(t),np.sin(t),color=colors[k],lw=3)
 mid=(k+.5)*2*np.pi/3
 ax.annotate('',xy=(np.cos(mid+.12),np.sin(mid+.12)),xytext=(np.cos(mid-.12),np.sin(mid-.12)),arrowprops={'arrowstyle':'->','lw':3,'color':colors[k]})
 t0=k*2*np.pi/3
 ax.plot(np.cos(t0),np.sin(t0),'o',color=colors[k],ms=7)
ax.text(1.08,-.04,'0 / 3 turns',ha='left',va='center')
ax.text(-.65,1.02,'1 turn',ha='center',color=colors[1])
ax.text(-.65,-1.12,'2 turns',ha='center',color=colors[2])
ax.text(-1.47,1.35,r'$w^3=z,\quad z=e^{i\theta},\quad w=e^{i\theta/3}$')
ax.set(xlim=(-1.6,2.25),ylim=(-1.6,1.6),xlabel=r'$\operatorname{Re}w$',ylabel=r'$\operatorname{Im}w$')
ax.set_title('Three turns of z return one root',fontweight='bold',pad=15)
ax=axs[1];ax.set_aspect('equal')
R=2;tau=3
ax.add_patch(Rectangle((-R,-4.1),2*R,4.1,color='#e2e8ee',zorder=0))
ax.add_patch(Circle((0,0),R,color='#e2e8ee',zorder=0))
ax.axhline(0,color='#bec8d0',lw=.8);ax.axvline(0,color='#bec8d0',lw=.8)
ax.plot([0,0],[-4.05,0],ls='--',color='#9b6875',lw=1.6)
ax.text(.15,-3.45,'branch cut',fontsize=10,color='#814357')
tt=np.linspace(np.pi,0,240);col='#215f7a'
ax.plot(R*np.cos(tt),R*np.sin(tt),color=col,lw=2.8)
ax.plot([-R,-R],[-4,0],color=col,lw=2.8);ax.plot([R,R],[0,-4],color=col,lw=2.8)
for p,q in [((-R,-2.9),(-R,-1.9)),((R,-1.9),(R,-2.9)),((-.45,1.9487),(.45,1.9487))]:
 ax.annotate('',xy=q,xytext=p,arrowprops={'arrowstyle':'->','color':col,'lw':2.8})
ax.plot([-4,4],[tau,tau],color='#b25d31',lw=2.5)
ax.annotate('',xy=(3.15,tau),xytext=(1.9,tau),arrowprops={'arrowstyle':'->','lw':2.5,'color':'#b25d31'})
ax.text(-3.95,3.3,r'$\mathbb{R}+i\tau,\ \tau=3$',color='#9a4d28',fontsize=11)
ax.text(2.2,-.6,r'$\Gamma_R$',fontsize=15,color=col)
ax.text(-.6,.65,r'$R=2$',fontsize=11)
ax.set(xlim=(-4.35,4.35),ylim=(-4.2,4.2),xlabel=r'$\operatorname{Re}s$',ylabel=r'$\operatorname{Im}s$')
ax.set_title('Contour for the negative half-space',fontweight='bold',pad=15)
fig.suptitle('Ramification supplies the curve; contour decay locates its solution',fontsize=16,fontweight='bold')
fig.supxlabel('Left: exact root continuation, labels count turns of z. Right: arrows give integration direction; shaded region is excluded.',fontsize=10)
out=Path(__file__).with_suffix('')
fig.savefig(out.with_suffix('.png'),dpi=190);fig.savefig(out.with_suffix('.svg'))
svg=out.with_suffix('.svg');svg.write_text('\n'.join(l.rstrip() for l in svg.read_text().splitlines())+'\n')
