"""Original CC0 exact Gaussian, retained-shape and recurrence diagram.

The integer labels are wrapped in four rows for legibility. This arrangement
is schematic; group addition remains addition of the printed integers.
Proof locators: Sections 2–4, equations (6.5), (6.7), Exercise 9.7.
"""
from pathlib import Path
import math
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Rectangle
matplotlib.rcParams['svg.hashsalt']='oa-classify-amenable-gaussian-towers-learner-v1'
fig=plt.figure(figsize=(6.5,16.1),facecolor='#faf8f4')
fig.text(.5,.981,'From independent copies\nto amenable towers',ha='center',va='top',fontsize=21,weight='bold')
fig.text(.5,.924,'Bounded independent-copy exponentials',ha='center',fontsize=19)
fig.text(.5,.893,r'$\tau(\prod_j U_N(a_j,t_j))\ \longrightarrow\ e^{-\|\sum_jt_ja_j\|_2^2/2}$',ha='center',fontsize=18)
fig.text(.5,.859,r'Normal Gaussian model $A\subset P^\prime\cap F$',ha='center',fontsize=19)
fig.text(.5,.837,r'$J\alpha_g=\gamma_gJ$',ha='center',fontsize=19)
fig.text(.5,.805,'Gaussian movement has no zero atom',ha='center',fontsize=20,weight='bold')
ax=fig.add_axes([.17,.681,.72,.1],facecolor='#faf8f4')
t=np.linspace(-7,7,701);density=np.exp(-t*t/8)/(2*math.sqrt(2*math.pi))
ax.plot(t,density,color='#11647d',lw=2.4);ax.axvline(0,color='#af5e15',ls='--',lw=1.6)
ax.set_xlim(-7,7);ax.set_ylim(0,.22);ax.set_xticks([-6,-3,0,3,6]);ax.set_yticks([0,.1,.2]);ax.tick_params(labelsize=16)
ax.set_xlabel(r'$\delta=G(-f)-G(f),\quad\|f\|=1$',fontsize=18);ax.set_ylabel('Density',fontsize=18)
fig.text(.5,.628,r'$\operatorname{Var}(\delta)=4,\quad\mu(\{\delta=0\})=0$',ha='center',fontsize=20)
fig.text(.5,.596,'Retain labels and control boundaries',ha='center',fontsize=19,weight='bold')
fig.text(.5,.575,'Integer labels, wrapped in four rows',ha='center',fontsize=17)
levels=fig.add_axes([.12,.402,.77,.156]);levels.set_xlim(-.55,4.6);levels.set_ylim(-.65,4.1);levels.axis('off')
holes={7,12};outgoing={6,11,19};incoming={0,8,13}
for s in range(20):
 col=s%5;row=s//5;y=3.2-row
 levels.add_patch(Rectangle((col-.32,y),.64,.55,facecolor='#eee' if s in holes else '#dce7ea',edgecolor='#777' if s in holes else '#344d5a',hatch='//' if s in holes else None))
 levels.text(col,y+.275,str(s),ha='center',va='center',fontsize=18)
 if s in outgoing:levels.plot(col,y+.77,'v',color='#11647d',markersize=10)
 if s in incoming:levels.plot(col,y-.15,'^',color='#af5e15',markersize=10)
fig.text(.27,.388,'Blue ▼: outgoing',ha='center',fontsize=17,color='#11647d')
fig.text(.73,.388,'Orange ▲: incoming',ha='center',fontsize=17,color='#af5e15')
fig.text(.5,.358,r'$S=\{0,\ldots,19\},\quad R=S\setminus\{7,12\}$',ha='center',fontsize=18)
fig.text(.5,.331,'Outgoing: 6, 11, 19.   Incoming: 0, 8, 13.',ha='center',fontsize=17)
fig.text(.5,.304,r'$|R|=18,\quad B^{\mathrm{L}}/\mu(RB)=B^{\mathrm{R}}/\mu(RB)=1/6$',ha='center',fontsize=17)
fig.text(.5,.267,'Descending bound on uncovered mass',ha='center',fontsize=20,weight='bold')
ax=fig.add_axes([.18,.119,.71,.119],facecolor='#faf8f4')
L=np.arange(21);bound=(.75)**L+.01*(1-(.75)**L)
ax.semilogy(L,bound,'o-',color='#11647d',lw=2,ms=4);ax.axhline(.01,color='#af5e15',ls='--',lw=1.4)
ax.set_xlim(0,20);ax.set_ylim(.008,1.15);ax.set_xticks([0,5,10,15,20]);ax.set_yticks([1,.1,.01]);ax.set_yticklabels(['1','0.1','0.01']);ax.tick_params(labelsize=16)
ax.set_xlabel(r'Number of packing stages $L$',fontsize=17);ax.set_ylabel('Proved upper bound',fontsize=17)
fig.text(.5,.063,r'$a=1/4,\quad d=3/1600$',ha='center',fontsize=18)
fig.text(.5,.039,r'$h_L\leq(3/4)^L+0.01[1-(3/4)^L]$',ha='center',fontsize=18)
fig.text(.5,.015,r'$h_{20}<0.01318$: bound on measured coverage.',ha='center',fontsize=17)
out=Path(__file__).resolve().parent
fig.savefig(out/'amenable-gaussian-towers.svg',metadata={'Date':None},facecolor=fig.get_facecolor())
fig.savefig(out/'amenable-gaussian-towers.png',dpi=120,metadata={'Software':'OA-CLASSIFY original plotting source'},facecolor=fig.get_facecolor())
plt.close(fig)
