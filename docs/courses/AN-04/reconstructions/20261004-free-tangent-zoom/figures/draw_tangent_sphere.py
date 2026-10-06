"""Reproducible exact model for T1, T6 and Exercise 2; original CC0 figure."""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

out=Path(__file__).resolve().parent
plt.rcParams.update({'font.size':12,'axes.titlesize':14,'svg.fonttype':'none'})
fig=plt.figure(figsize=(11,9),layout='constrained',facecolor='#f8fafc')
grid=fig.add_gridspec(2,2,height_ratios=[1.2,1])
a=fig.add_subplot(grid[0,0]);b=fig.add_subplot(grid[0,1]);c=fig.add_subplot(grid[1,:])
theta=np.linspace(-np.pi,np.pi,1001)
a.plot(np.cos(theta),np.sin(theta),color='#16697a',lw=2.5,label='base projection of the graph')
a.axvline(1,color='#263238',ls='--',label='tangent at the selected point')
a.scatter([1],[0],color='#b34827',s=40,zorder=5)
a.annotate('',xy=(2,0),xytext=(1,0),arrowprops={'arrowstyle':'->','color':'#b34827'})
a.text(1.08,.10,r'$\xi_0=(1,0)$',ha='left',va='bottom')
a.text(.95,-.22,r'$x_0=(1,0)$',ha='right')
a.set(xlabel=r'physical coordinate $y_1$',ylabel=r'physical coordinate $y_2$',xlim=(-1.2,2.2),ylim=(-1.25,1.25),title=r'$H(\xi)=|\xi|$ in two dimensions')
a.set_aspect('equal',adjustable='box');a.legend(loc='upper center',bbox_to_anchor=(.5,-.20),fontsize=9)
s=np.linspace(-2.5,2.5,801)
for t,color in [(2,'#b34827'),(8,'#16697a')]:
 b.plot(t*(np.cos(s/t)-1),t*np.sin(s/t),color=color,lw=2.4,label=f't = {t}')
b.axvline(0,color='#263238',ls='--',lw=2,label='limiting support: x₁ = 0')
b.set(xlabel=r'zoom coordinate $x_1$',ylabel=r'zoom coordinate $x_2$',xlim=(-1.5,.25),ylim=(-2.6,2.6),title=r'$x=t(y-x_0)$: the sphere flattens')
b.legend(loc='upper center',bbox_to_anchor=(.5,-.15),fontsize=9,ncol=2)
x=np.linspace(-4,4,1201);phase=x*x/2-np.pi/4
c.plot(x,np.cos(phase),color='#16697a',lw=2,label='real part')
c.plot(x,np.sin(phase),color='#b34827',lw=2,label='imaginary part')
c.axhline(0,color='#aaa',lw=.8)
c.set(xlabel=r'transverse coordinate $x_2$ on the support line',ylabel='coefficient',ylim=(-1.2,1.2),title=r'Coefficient $e^{i(x_2^2/2-\pi/4)}$: unit magnitude, varying phase')
c.legend(loc='upper center',bbox_to_anchor=(.5,-.20),ncol=2,fontsize=10)
for ax in [a,b,c]:
 ax.grid(alpha=.15);ax.spines[['top','right']].set_visible(False)
fig.suptitle(r'$A=\mathrm{diag}(0,1),\quad B=0,\quad U_{A,0}=e^{i(x_2^2/2-\pi/4)}\,\delta_0(x_1)$',fontsize=17)
fig.savefig(out/'tangent-sphere.svg',metadata={'Creator':'GPT-6 Astra (OpenAI), Ultra; original CC0 figure','Title':'Tangent sphere and singular quadratic model'})
fig.savefig(out/'tangent-sphere.png',dpi=170)
print('Wrote tangent-sphere.svg and tangent-sphere.png')
