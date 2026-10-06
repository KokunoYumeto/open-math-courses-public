"""Exact portions of the forbidden kappa rays in equation (5.3).

Written by GPT-6.1 Sol (OpenAI), Ultra reasoning effort, September 2026.
Public domain (CC0). Self-checked; no independent review.
Theorem 1.1 and equations (5.1)–(5.3) of Quadratic coercivity when some
directions have zero energy. References: Sjostrand (1974); Melin (1971).
Run with Python and matplotlib; the PNG is saved beside this source.
"""
from fractions import Fraction as F
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

plt.rcParams.update({'font.family':'DejaVu Sans','font.size':13})
fig,ax=plt.subplots(figsize=(11,7),dpi=150)
fig.patch.set_facecolor('#fafaf7');ax.set_facecolor('#fafaf7')
colors=['#136c82','#a24e25','#66518e']
def point(a,r):
 return float(-(2*a+1)-F(6,5)*r),float(-F(2*a+1,2)+F(13,30)*r)
for a,color in enumerate(colors):
 pts=[point(a,r) for r in range(5)]
 ax.plot([p[0] for p in pts],[p[1] for p in pts],color=color,lw=2.2)
 ax.scatter([p[0] for p in pts],[p[1] for p in pts],color=color,s=55,zorder=3)
 ax.annotate('',point(a,F(9,2)),point(a,4),arrowprops={'arrowstyle':'->','lw':2.2,'color':color})
 ax.annotate(rf'$\alpha={a}$',pts[0],xytext=(8,-12),textcoords='offset points',color=color,fontsize=15)
 if a==0:
  for r in [0,1,4]:ax.annotate(rf'$r={r}$',pts[r],xytext=(3,13),textcoords='offset points',fontsize=12,color=color)
ax.scatter([0],[0],marker='x',s=90,lw=2,color='#293c45')
ax.annotate(r'$\kappa=0$ satisfies the criterion',(0,0),xytext=(-4.8,-3.25),textcoords='data',
 arrowprops={'arrowstyle':'-','color':'#364d59'},fontsize=13)
ax.set(xlim=(-11,.9),ylim=(-3.65,2.25),xlabel=r'Real part of $\kappa$',ylabel=r'Imaginary part of $\kappa$')
ax.set_aspect('equal',adjustable='box');ax.grid(alpha=.18)
ax.set_title('An oscillator plus a zero direction forbids entire rays',fontsize=18,pad=18)
fig.text(.5,.065,r'$\kappa=-(2\alpha+1)(1+i/2)-(6/5-13i/30)r$, $r=t^2\geq0$',ha='center',fontsize=15)
fig.text(.5,.02,'Shown: occupations 0, 1, 2; dots at r = 0, 1, 2, 3, 4. Every ray continues beyond its arrow.',ha='center',fontsize=11.5)
fig.subplots_adjust(left=.1,right=.97,bottom=.2,top=.88)
fig.savefig(Path(__file__).with_name('quadratic-forbidden-rays.png'),metadata={'Software':'Matplotlib; original CC0 mathematical figure'})
plt.close(fig)
