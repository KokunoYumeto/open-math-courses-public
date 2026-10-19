"""Exact characteristic slice and derivative data, AN01-U087 Exercise 6. CC0."""
from pathlib import Path
import math
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import Circle
plt.rcParams.update({'font.family':'DejaVu Sans','font.size':12,'svg.fonttype':'none'})
fig,axs=plt.subplots(1,2,figsize=(13,6),layout='constrained')
fig.set_facecolor('#f8fafc')
ax=axs[0];ax.set_aspect('equal')
for r in [.4,.8,1.2]:
 ax.add_patch(Circle((0,0),r,fill=False,edgecolor='#bac8d0',ls=':',lw=1.5))
ax.axhline(0,color='#b2bdc5',lw=.8);ax.axvline(0,color='#b2bdc5',lw=.8)
ax.plot(0,0,'o',color='#172334',ms=8)
ax.annotate('',xy=(.65,0),xytext=(0,0),arrowprops={'arrowstyle':'->','color':'#a23b47','lw':3})
ax.annotate('',xy=(0,-.65),xytext=(0,0),arrowprops={'arrowstyle':'->','color':'#286274','lw':3})
ax.text(.28,.14,r'$H_{\xi_x}=\partial_x$',color='#a23b47')
ax.text(.12,-.75,r'$H_x=-\partial_{\xi_x}$',color='#286274')
ax.text(-1.13,1.06,r'$\{\xi_x,x\}=1$',fontsize=16)
ax.text(-1.18,-1.14,r'$p=x^2+\xi_x^2,\quad \xi_y=1,\ \xi_z=0$',fontsize=12)
ax.set(xlim=(-1.4,1.4),ylim=(-1.4,1.4),xlabel=r'$x$',ylabel=r'$\xi_x$')
ax.set_title('A nonzero bracket at a characteristic point',pad=14,fontweight='bold')
ax=axs[1]
k=np.arange(1,19,dtype=int)
values=np.array([math.exp((math.lgamma(2*int(j)+1)-(2*int(j)+1)*math.log(2)-math.lgamma(int(j)+1))/int(j)) for j in k])
ax.plot(k,values,'o-',lw=2.5,ms=5,color='#286274',label=r'$R_k=((2k)!/(2^{2k+1}k!))^{1/k}$')
ax.plot(k,k/8,'--',color='#a23b47',lw=2,label=r'Proved lower bound $k/8$')
ax.set(xlim=(.5,18.5),ylim=(0,max(values)*1.16),xlabel='Derivative order k',ylabel=r'Required analytic base $R_k$')
ax.set_xticks([1,4,8,12,16,18]);ax.grid(alpha=.2)
ax.legend(loc='upper left',fontsize=11)
ax.set_title('Smooth solutions can fail analytic bounds',pad=14,fontweight='bold')
fig.suptitle('Support uniqueness and analytic regularity are different conclusions',fontsize=17,fontweight='bold')
fig.supxlabel('Left: fixed cotangent slice, arrows scaled by 0.65; dotted circles are levels of p. Right: exact derivative formula, numerical samples.',fontsize=10)
out=Path(__file__).with_suffix('')
fig.savefig(out.with_suffix('.png'),dpi=190);fig.savefig(out.with_suffix('.svg'))
svg=out.with_suffix('.svg');svg.write_text('\n'.join(l.rstrip() for l in svg.read_text().splitlines())+'\n')
