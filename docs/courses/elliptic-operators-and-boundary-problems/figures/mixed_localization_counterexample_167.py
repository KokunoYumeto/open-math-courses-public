"""Exact compact bump supports and the complete ML1--ML5 cancellation."""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrowPatch, Rectangle
out=Path(__file__).resolve().parent
plt.rcParams.update({'font.size':12,'mathtext.fontset':'dejavusans'})
fig=plt.figure(figsize=(13,9),layout='constrained')
gs=fig.add_gridspec(2,2,height_ratios=[1,1.2])
ax=fig.add_subplot(gs[0,0])
y=np.linspace(-5,5,3001)
def bump(center):
 z=(y-center)/.8
 v=np.zeros_like(y);mask=np.abs(z)<1
 v[mask]=np.exp(-1/(1-z[mask]**2))
 return v
for c,name,color in [(-3,'f','#176b90'),(0,'g','#b55718'),(3,'h','#754baa')]:
 ax.plot(y,bump(c),color=color,lw=2.4,label=name)
ax.add_patch(Rectangle((-4.1,0),2.2,.43,color='#176b90',alpha=.09))
ax.set(xlim=(-5,5),ylim=(0,.45),xlabel='Original circle coordinate y (one chart)',ylabel='Actual bump value',title='A. Three disjoint original supports')
ax.text(-3,.405,r'$\eta_y=\chi_y=1$ on supp f',ha='center',fontsize=10)
ax.text(1.5,.405,r'$\eta_y=0$ on supp g and h',ha='center',fontsize=10)
for c,name,color in [(-3,'f','#176b90'),(0,'g','#b55718'),(3,'h','#754baa')]:
 ax.text(c-.58,.32,name,color=color,fontsize=15)
ax=fig.add_subplot(gs[0,1]);ax.axis('off')
ax.set_title('B. The separated kernel keeps its normal singularity')
ax.text(.5,.88,r'$K_S(y,z)\,D_r\delta(r-s)$',ha='center',fontsize=20)
for xy,label,c in [((.22,.52),'input z in supp g or h','#b55718'),((.78,.52),'output y in supp f','#176b90')]:
 ax.text(*xy,label,ha='center',bbox=dict(boxstyle='round',fc=c+'18',ec=c),fontsize=11)
ax.add_patch(FancyArrowPatch((.37,.52),(.61,.52),arrowstyle='->',mutation_scale=20,lw=2,color='#176b90'))
ax.text(.5,.30,'Tangential points are separated; r = s is retained.',ha='center',fontsize=12)
ax.text(.5,.12,'Smooth in y and z does not give a smooth full kernel.\nExact density and both S denominators are in ML1.',ha='center',fontsize=11)
ax=fig.add_subplot(gs[1,:]);ax.axis('off')
ax.set_title('C. Every component of the oscillatory input is retained')
ax.text(.5,.88,r'$u_n=\psi(r)e^{inr}\left(f-n g-n^{-1}h\right)$',ha='center',fontsize=21)
ax.text(.5,.72,r'On supp $\eta$: all positive derivatives of $\psi$ vanish; $D_r e^{inr}=n e^{inr}$.',ha='center',fontsize=12)
xs=[.13,.37,.63,.87]
labels=[r'$f\ \mathrm{component}:\quad n^2f$',r'$L_y f:\quad L_yf$',r'$g\ \mathrm{component}:\quad -n^2f$',r'$h\ \mathrm{component}:\quad -L_yf$']
for x,label in zip(xs,labels):
 ax.text(x,.54,label,ha='center',fontsize=14,bbox=dict(boxstyle='round',fc='#edf3f6',ec='#47758b'))
ax.text(.5,.33,r'$\eta P u_n=\eta_r e^{inr}(n^2f+L_yf-n^2f-L_yf)=0$',ha='center',fontsize=19)
ax.text(.5,.14,r'$\|\chi u_n\|_{H^2}\geq c n^2,\qquad \|\eta u_n\|_{H^1}\leq C(n+1)$',ha='center',fontsize=20)
ax.text(.5,.015,'ML1–ML5 proves the contradiction. ML8 retains the full lower input norm, including both distant components.',ha='center',fontsize=11)
fig.suptitle('Why the cutoff-only mixed elliptic estimate fails',fontsize=22)
fig.savefig(out/'mixed_localization_counterexample_167.png',dpi=150)
fig.savefig(out/'mixed_localization_counterexample_167.svg')
plt.close(fig)
print('Rendered the full exact support and cancellation diagram.')
