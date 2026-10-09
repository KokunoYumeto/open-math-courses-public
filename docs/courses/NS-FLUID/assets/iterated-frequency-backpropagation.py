"""Exact interval geometry and the finite sum mechanism in IB8–IB12."""
from pathlib import Path
from fractions import Fraction as F
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle
ROOT=Path(__file__).resolve().parent
plt.rcParams.update({'font.family':'DejaVu Sans','font.size':11})
fig,(ax,bx)=plt.subplots(1,2,figsize=(14,7),layout='constrained',gridspec_kw={'width_ratios':[1.25,1]})
N=[8,4,4,2];times=[F(1)]
for n in N:times.append(times[-1]-F(2,n*n))
S=F(1,4);threshold=1-S;m=2
ax.axvspan(float(threshold),1,color='#e7f0f4',zorder=0)
ax.axvline(float(threshold),ls='--',color='#b54d43',lw=1.5)
ax.text(float(threshold)-.013,3.45,r'$t_0-S=3/4$',ha='right',color='#983c33')
for j in range(3):
 y=3-j
 ax.plot([float(times[j+1]),float(times[j])],[y,y],lw=3,color='#8b979d')
 ax.scatter([float(times[j])],[y],s=28,color='#263d49',zorder=3)
 ax.annotate(r'$t_%d=%s$'%(j,str(times[j])),(float(times[j]),y),xytext=(0,13),textcoords='offset points',ha='center',fontsize=10)
 if j<m:
  left=times[j]-F(1,2*N[j]**2)
  ax.broken_barh([(float(left),float(times[j]-left))],(y-.10,.20),facecolors='#cc944d',zorder=4)
  ax.annotate(r'$J_%d,\ |J_%d|=1/%d$'%(j,j,2*N[j]**2),(float(left),y),xytext=(-8,-25),textcoords='offset points',ha='right',fontsize=10,color='#8b561c')
ax.scatter([float(times[3])],[1],color='#b54d43',s=35,zorder=4)
ax.annotate(r'$t_3=23/32<t_0-S$',(float(times[3]),1),xytext=(8,-28),textcoords='offset points',ha='left',fontsize=10,color='#983c33',bbox={'facecolor':'white','edgecolor':'none','alpha':.95})
ax.set(xlim=(.64,1.045),ylim=(-.65,3.85),yticks=[],xlabel='Original physical time',title='The retained persistence intervals are disjoint')
ax.text(.655,-.5,'Geometry example: d = 1, D = 4; frequencies 8, 4, 4, 2.\nSteps have length 2/N²; analytic PDE constants are not evaluated.',fontsize=9,bbox={'facecolor':'white','edgecolor':'none','alpha':.95})
ax.grid(axis='x',alpha=.2)
rs=[F(1,n) for n in N[:m+1]];total=sum(rs);largest=max(rs)
bx.add_patch(Rectangle((0,0),float(total),float(largest),facecolor='#e7f0f4',edgecolor='#406e87',ls='--',lw=1.5))
left=F(0)
for j,r in enumerate(rs):
 bx.add_patch(Rectangle((float(left),0),float(r),float(r),facecolor='#3b7b9b',edgecolor='white',lw=1.5))
 bx.text(float(left+r/2),float(r/2),r'$r_%d^2$'%j,ha='center',va='center',color='white',fontsize=13)
 bx.text(float(left+r/2),-.028,r'$r_%d=%s$'%(j,str(r)),ha='center',fontsize=10)
 left+=r
bx.text(float(total)/2,.282,r'$\sum r_j^2\leq(\max r_j)\sum r_j$',ha='center',fontsize=14)
bx.text(.012,.36,r'$r_j=N_j^{-1}$, with $j=0,1,2$',fontsize=12)
bx.text(.012,.325,r'Exact areas: $9/64\leq(1/4)(5/8)=5/32$',fontsize=11)
bx.text(.012,-.085,'Crossing supplies the lower bound on the blue area.\nTotal speed bounds the complete horizontal width.\nTogether they force an earlier reciprocal frequency.',fontsize=10)
bx.set(xlim=(-.02,.665),ylim=(-.11,.41),xticks=[],yticks=[0,.125,.25],ylabel='Reciprocal frequency',title='The finite sum forces an earlier scale')
fig.suptitle('From disjoint time intervals to an earlier frequency',fontsize=16)
fig.savefig(ROOT/'iterated-frequency-backpropagation.png',dpi=170)
fig.savefig(ROOT/'iterated-frequency-backpropagation.svg')
print('Saved exact interval and finite-sum geometry.')
