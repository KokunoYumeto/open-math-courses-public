"""Sharp atomic index mass of the actual physical return. CC0 1.0."""
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
P=Path(__file__).resolve().with_suffix('')
fig=plt.figure(figsize=(12,10),facecolor='#fafcff');ink='#182a3a';blue='#164b7a';green='#126856'
ax=fig.add_axes([.04,.67,.92,.29]);ax.axis('off')
ax.text(.5,.94,'Sharp central normal minorant',ha='center',fontsize=21,weight='bold',color=ink)
ax.text(.5,.73,r'$t E_U^\tau\leq_{\rm cp} E_N^\tau\quad\Longleftrightarrow\quad 0\leq t\leq t_*$',ha='center',fontsize=16,color=blue)
ax.text(.5,.51,r'$t_*=\sum_i\frac{p_i}{d_i}z_i,\qquad p_i=\tau(z_i),\quad d_i=[Uz_i:Nz_i]$',ha='center',fontsize=17,color=ink)
ax.text(.5,.28,r'$h=t_*,\qquad \tau(h)=\sum_i p_i^2/d_i,\qquad 1/\infty=0$',ha='center',fontsize=17,color=green)
ax.text(.5,.08,'PH.16–PH.18: original physical expectations and whole supported returns',ha='center',fontsize=12,color=ink)
b=fig.add_axes([.10,.40,.80,.19],facecolor='white')
x=np.arange(3);p=np.array([.5,1/3,1/6]);d=np.array([1,2,3]);a=p/d
b.bar(x-.16,p,.30,label=r'$p_i$',color='#9ab9d3')
b.bar(x+.16,a,.30,label=r'$a_i=p_i/d_i$',color=green)
b.set_xticks(x,labels=['atom 1: d = 1','atom 2: d = 2','atom 3: d = 3']);b.set_ylim(0,.61);b.set_ylabel('Physical central coefficient');b.legend(frameon=False);b.grid(axis='y',alpha=.15)
b.set_title('Exercise data only: exact total mass = 17/54',fontsize=12,color=ink)
c=fig.add_axes([.10,.10,.80,.21],facecolor='white')
c.axvspan(1,2,color='#eadbdc',alpha=.75,label='1 < r < 2 excluded')
r=np.linspace(2,8,200);c.plot(r,1/r,color=blue,lw=2,label='1/r at an actual factor index')
c.scatter([1,2,4],[1,.5,.25],color=green,zorder=4)
c.annotate('r = 1: mass 1',xy=(1,1),xytext=(1.5,.87),arrowprops=dict(arrowstyle='->',color=ink),fontsize=10)
c.annotate('proper factor: mass ≤ 1/2',xy=(2,.5),xytext=(3.0,.61),arrowprops=dict(arrowstyle='->',color=ink),fontsize=11)
c.set_xlim(.8,8);c.set_ylim(0,1.08);c.set_xlabel('Extended factor index r (finite part shown)');c.set_ylabel('Limit mass');c.grid(alpha=.15);c.legend(loc='upper right',frameon=True,facecolor='white')
fig.text(.5,.035,'At r = ∞ the mass is 0. The curve does not assert realization of every real index.',ha='center',fontsize=11,color=ink)
fig.savefig(P.with_suffix('.png'),dpi=160,facecolor=fig.get_facecolor());fig.savefig(P.with_suffix('.svg'),facecolor=fig.get_facecolor());plt.close(fig)
svg=P.with_suffix('.svg');svg.write_bytes(b'\n'.join(x.rstrip() for x in svg.read_bytes().splitlines())+b'\n')
