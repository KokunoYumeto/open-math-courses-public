"""Exact domain geometry for AN01-U089 Exercises 1 and 7. CC0."""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import Polygon,Rectangle
plt.rcParams.update({'font.family':'DejaVu Sans','font.size':12,'svg.fonttype':'none'})
fig,axs=plt.subplots(1,2,figsize=(13,6),layout='constrained');fig.set_facecolor('#f8fafc')
ax=axs[0];ax.set_aspect('equal')
ax.add_patch(Polygon([(0,2),(2,0),(0,-2),(-2,0)],facecolor='#f5e6d7',edgecolor='#b25d31',lw=2))
ax.add_patch(Rectangle((-1,-1),2,2,facecolor='#d9e8ef',edgecolor='#215f7a',lw=2))
ax.axhline(0,color='#bec8d0',lw=.8);ax.axvline(0,color='#bec8d0',lw=.8)
x=np.linspace(-2,2,800)
for t in [x+1.4,-x-1.2]:
 ok=np.abs(x)+np.abs(t)<=2
 ax.plot(x[ok],t[ok],'--',color='#744a85',lw=1.6)
ax.text(-.73,.15,r'$X_1$',fontsize=18,color='#215f7a')
ax.text(1.25,.08,r'$X_2$',fontsize=18,color='#9a4d28')
ax.text(-2.3,2.17,r'$X_1:\ \max(|x|,|t|)<1$',fontsize=11,color='#215f7a')
ax.text(-2.3,-2.38,r'$X_2:\ |x|+|t|<2$',fontsize=11,color='#9a4d28')
ax.set(xlim=(-2.45,2.45),ylim=(-2.5,2.5),xlabel=r'$x$',ylabel=r'$t$')
ax.set_title('Wave equation: square determines diamond',fontweight='bold',fontsize=13,pad=14)
ax=axs[1];ax.set_aspect('equal')
ax.add_patch(Polygon([(-2.4,2.4),(0,0),(2.4,2.4)],facecolor='#e4edf1',edgecolor='none'))
ax.add_patch(Polygon([(-1,1),(0,0),(1,1)],facecolor='#e9cbb9',edgecolor='none'))
ax.plot([-2.4,0,2.4],[2.4,0,2.4],color='#215f7a',lw=2.5)
ax.axhline(0,color='#9b4d52',ls='--',lw=1.5)
ax.plot([-1,1],[1,1],color='#9b4d52',lw=2)
ax.axvline(0,color='#bec8d0',lw=.8)
ax.text(-.5,1.83,r'$C:\ t>|x|$',fontsize=15,color='#215f7a')
ax.text(-.55,.67,r'$\operatorname{supp}_C u$',fontsize=12,color='#814357')
ax.text(1.15,1.03,r'$t=1$',fontsize=12,color='#814357')
ax.text(-2.35,-.24,r'$t=0:\ \overline{C}\cap\{t=0\}=\{0\}$',fontsize=11,color='#814357')
ax.text(-2.35,2.75,r'$u(x,t)=e^{-1/(1-t)}\ (t<1),\quad u=0\ (t\geq1)$',fontsize=10)
ax.set(xlim=(-2.5,2.5),ylim=(-.5,3),xlabel=r'$x$',ylabel=r'$t$')
ax.set_title('Transport equation: a bounded cone cap',fontweight='bold',fontsize=13,pad=14)
fig.suptitle('Characteristic planes decide where a zero solution continues',fontsize=16,fontweight='bold')
fig.supxlabel('Left: dashed lines are characteristic, t − x = 1.4 and t + x = −1.2. Right: Dₓu = 0; the cone extends beyond the viewing window.',fontsize=10)
out=Path(__file__).with_suffix('')
fig.savefig(out.with_suffix('.png'),dpi=190);fig.savefig(out.with_suffix('.svg'))
svg=out.with_suffix('.svg');svg.write_text('\n'.join(l.rstrip() for l in svg.read_text().splitlines())+'\n')
