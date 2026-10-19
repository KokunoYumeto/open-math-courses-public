"""Reproducible diagrams for jumps, point jets and smooth division.
Original figure by GPT-6 Astra (OpenAI), 2026. CC0.
Exact formulas: Theorems 2 and 5 and Exercise 6 of the accompanying lesson.
"""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
matplotlib.rcParams.update({'font.size':12,'axes.titlesize':15,'svg.hashsalt':'AN01-U121','font.family':'DejaVu Sans'})
root=Path(__file__).resolve().parent
fig,axes=plt.subplots(1,3,figsize=(16,5.5),layout='constrained')
navy='#153b5b';orange='#bd5b21';teal='#087e8b'
ax=axes[0]
x=np.linspace(-3,3,601)
ax.plot(x,np.exp(-np.abs(x)),color=navy,lw=2.4,label=r'$f(x)=e^{-|x|}$')
left=np.linspace(-3,-0.002,300);right=-left[::-1]
ax.plot(left,np.exp(left),color=orange,lw=2,label=r'ordinary $f^\prime$')
ax.plot(right,-np.exp(-right),color=orange,lw=2)
ax.scatter([0,0],[1,-1],s=60,edgecolors=orange,facecolors='white',zorder=4)
ax.annotate('',xy=(0,-0.97),xytext=(0,0.97),arrowprops={'arrowstyle':'->','color':orange,'lw':2})
ax.text(.18,.05,r'jump $=-2$',color=orange)
ax.set(title='A jump produces a point mass',xlabel=r'$x$',ylim=(-1.2,1.35))
ax.axhline(0,color='#aeb8c1',lw=.8);ax.legend(loc='upper right',fontsize=11)
ax.text(.5,-.23,r'$D^2f=f-2\delta_0$',transform=ax.transAxes,ha='center',fontsize=15)
ax=axes[1]
ax.axhline(0,color=navy,lw=1.5)
ax.scatter([-1,1],[0,0],s=85,color=[teal,orange],zorder=3)
ax.text(-1,.18,r'$m=2$',ha='center',color=teal,fontsize=15)
ax.text(1,.18,r'$m=3$',ha='center',color=orange,fontsize=15)
ax.text(-1,-.30,r'$\delta_{-1},\ \delta_{-1}^\prime$',ha='center',color=teal,fontsize=16)
ax.text(1,-.30,r'$\delta_1,\ \delta_1^\prime,\ \delta_1^{\prime\prime}$',ha='center',color=orange,fontsize=16)
ax.text(0,.61,r'$F(x)=(x+1)^2(x-1)^3$',ha='center',fontsize=15)
ax.set(title='Multiplicity determines the kernel',xlim=(-2,2),ylim=(-.6,.9),xticks=[-1,0,1],yticks=[],xlabel=r'$x$')
ax.text(.5,-.23,'Point locations and jet bases',transform=ax.transAxes,ha='center',fontsize=12)
ax=axes[2]
x=np.linspace(.2,1,500)
ax.semilogy(x,x**4,color=teal,lw=2.5,label=r'$x^4$: multiplicity $4$')
ax.semilogy(x,np.exp(-1/x**2),color=orange,lw=2.5,label=r'$e^{-1/x^2}$: flat at $0$')
ax.set(title='Finite order versus a flat zero',xlabel=r'$x>0$',ylabel='value (logarithmic scale)',xlim=(.2,1),ylim=(1e-12,2))
ax.legend(loc='lower right',fontsize=11)
ax.text(.5,-.23,r'Both extend with value $0$ at $x=0$',transform=ax.transAxes,ha='center',fontsize=12)
for ax in axes:
 ax.spines[['top','right']].set_visible(False)
 ax.grid(alpha=.16)
fig.suptitle('Jumps, point jets and division by smooth functions',fontsize=19,color=navy)
fig.savefig(root/'jumps-zero-multiplicities-and-flatness.png',dpi=150,facecolor='white')
svg=root/'jumps-zero-multiplicities-and-flatness.svg'
fig.savefig(svg,metadata={'Date':None,'Creator':'GPT-6 Astra (OpenAI)'},facecolor='white')
svg.write_text('\n'.join(line.rstrip() for line in svg.read_text(encoding='utf-8').splitlines())+'\n',encoding='utf-8')
plt.close(fig)
