"""CC0 diagram of relative freeness and the exact two-point crossed-product example."""
from pathlib import Path
from math import sqrt
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch
matplotlib.rcParams['svg.hashsalt']='oa-classify-relative-free-action-learner-v2'
fig=plt.figure(figsize=(6.5,11.8),facecolor='#faf8f4')
top=fig.add_axes([.035,.64,.93,.335]);top.set_xlim(0,6.5);top.set_ylim(0,4.0);top.axis('off')
top.text(3.25,3.75,'Freeness survives fixed coefficients',ha='center',fontsize=18,weight='bold')
for x,label,color in [(1.6,'Fixed coefficients\n'+r'$A=W^*(P,v)$','#dce7ea'),(4.9,'Independent orbit copy\n'+r'$T(B)\subset A^\prime\cap F$','#f2dfca')]:
 top.add_patch(FancyBboxPatch((x-1.46,2.63),2.92,.83,boxstyle='round,pad=.04',facecolor=color,edgecolor='#344d5a'))
 top.text(x,3.045,label,ha='center',va='center',fontsize=16)
top.text(3.25,2.27,r'$y=T(x),\quad\delta=\gamma_g(y)-y$',ha='center',fontsize=17)
top.text(3.25,1.9,'A proposed intertwiner would give',ha='center',fontsize=16)
top.text(3.25,1.49,r'$v\gamma_g(y)=yv=vy\quad\Longrightarrow\quad v\delta=0$',ha='center',fontsize=17)
top.text(3.25,1.1,'Independent trace gives the contradiction',ha='center',fontsize=16)
top.text(3.25,.67,r'$\|v\delta\|_2^2=\tau(v^*v)\,c>0$',ha='center',fontsize=19,color='#11647d')
top.text(3.25,.18,r'$c=\|\gamma_g(x)-x\|_2^2>0$',ha='center',fontsize=17)
fig.text(.5,.607,'Finite correction: exact phase '+r'$\theta=\pi$',ha='center',fontsize=18,weight='bold')
ax=fig.add_axes([.16,.285,.68,.29],facecolor='#faf8f4');ax.set_aspect('equal')
ax.set_xlim(-1.16,1.16);ax.set_ylim(-1.16,1.16)
ax.axhline(0,color='#bbb',lw=.8);ax.axvline(0,color='#bbb',lw=.8)
ax.set_xticks([-1,0,1]);ax.set_yticks([-1,0,1]);ax.tick_params(labelsize=15)
t=1/sqrt(2)
ax.plot([-1,1],[-1,1],color='#11647d',lw=1.5,alpha=.55)
ax.plot([-1,1],[1,-1],color='#af5e15',lw=1.5,alpha=.55)
ax.annotate('',xy=(t,t),xytext=(0,0),arrowprops={'arrowstyle':'->','lw':2.4,'color':'#11647d'})
ax.annotate('',xy=(-t,t),xytext=(0,0),arrowprops={'arrowstyle':'->','lw':2.4,'color':'#af5e15'})
ax.text(.85,.59,r'$\xi$',fontsize=20,color='#11647d',ha='center')
ax.text(-.85,.59,r'$\eta$',fontsize=20,color='#af5e15',ha='center')
ax.annotate('',xy=(-t,t),xytext=(t,t),arrowprops={'arrowstyle':'->','lw':1.6,'linestyle':'--','color':'#555','connectionstyle':'arc3,rad=.3'})
ax.text(0,1.03,r'$W$',ha='center',fontsize=20)
for spine in ax.spines.values():spine.set_color('#ccc')
lines=[(.231,r'$\xi=(1,1)/\sqrt{2},\quad\eta=(-1,1)/\sqrt{2}$'),
 (.185,r'$D=\mathbb{C}^2,\ H=\mathbb{Z}/2;\quad\gamma_s$ swaps coordinates'),
 (.147,r'$N=D\rtimes H=M_2,\quad W=\operatorname{diag}(-1,1)$'),
 (.109,r'$p=|\xi\rangle\langle\xi|,\quad q=|\eta\rangle\langle\eta|$'),
 (.071,r'$v=Wp,\ v^*v=p,\ vv^*=q,\quad w=2x$')]
for y,label in lines:fig.text(.5,y,label,ha='center',fontsize=17)
fig.text(.5,.024,r'Coordinates are exact; $\tau(p)=\tau(q)=1/2$.',ha='center',fontsize=16)
out=Path(__file__).resolve().parent
meta={'Date':'2026-10-02','Creator':'GPT-6.1 Sol (OpenAI), Ultra; original CC0 mathematical diagram'}
fig.savefig(out/'relative-free-action.svg',metadata=meta)
fig.savefig(out/'relative-free-action.png',dpi=160,metadata={'Creator':meta['Creator']})
