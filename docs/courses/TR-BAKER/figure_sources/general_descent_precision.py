"""Reproduce TR-BAKER-10 Figure10.24 from its exact proved formulas; CC0."""
from pathlib import Path
from fractions import Fraction as Q
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

HERE=Path(__file__).resolve().parent
if HERE.name=='figure_sources':OUT=HERE.parent/'figures/general-descent-precision.png'
else:OUT=HERE/'general-descent-precision.png'
ranks=list(range(2,13))
C=[Q(r*10+1,10*(r+1))+Q(17*(r-1),24*(r+1)**2) for r in ranks]
eps=[(Q(3)+Q(14,r+1))/(7*Q(7200,29)*14**(r-2)) for r in ranks]
plt.rcParams.update({'font.size':12,'axes.spines.top':False,'axes.spines.right':False})
fig,ax=plt.subplots(1,3,figsize=(16,5.2),layout='constrained')
for u in range(7):
 for h in range(7-u):
  zero=u>2
  ax[0].scatter(u,h,s=65,color='#9ca3af' if zero else '#146c94',marker='x' if zero else 'o')
ax[0].plot([2,2],[0,6],color='#d97706',ls='--',label='Illustrative degree 2')
ax[0].scatter([2],[2],color='#c02655',marker='*',s=230,zorder=5,label='Mean (2, 2)')
ax[0].set(xlim=(-.4,6.5),ylim=(-.4,6.5),xlabel='Additive order u',ylabel='Euler order h',title='Rank 2: 28 full simplex rows')
ax[0].text(3.1,4.8,'u + h ≤ 6\nSlack = 6 − u − h\n×: zero rows',fontsize=11)
ax[0].set_aspect('equal');ax[0].legend(loc='upper right',fontsize=9)
ax[1].plot(ranks,list(map(float,C)),marker='o',color='#146c94',label='Proved Cᵣ')
ax[1].axhline(1,color='#c02655',ls='--',label='Strict upper bound 1')
ax[1].set(xlabel='Rank r',ylabel='Mean clearing + Euler coefficient',ylim=(.7,1.035),title='Exact all-rank mean bound')
ax[1].text(3.2,.73,'1 − Cᵣ = (23r + 193) / [120(r + 1)²]',fontsize=10)
ax[1].text(3.2,1.005,'Strict upper bound 1',fontsize=10,color='#c02655')
ax[1].text(9.6,.925,'Proved Cᵣ',fontsize=10,color='#146c94')
ax[2].semilogy(ranks,list(map(float,eps)),marker='o',color='#146c94',label='Proved εᵣ')
ax[2].set(xlabel='Rank r',ylabel='Upper bound for ln(N d_E) / Z',title='General coefficient-count budget')
ax[2].text(.05,.08,'$Z=S\\mathcal{D}/d$\nεᵣ < 14²⁻ʳ / 225',transform=ax[2].transAxes,fontsize=11)
ax[2].legend(fontsize=10)
for a in ax:a.grid(alpha=.2)
fig.savefig(OUT,dpi=180,facecolor='white');plt.close(fig)
print(OUT)
