"""Exact examples of the proved distributional solution families.
Original figure by GPT-6 Astra (OpenAI), 2026. CC0.
References: Theorem 4, formula D19, and Theorem 6 in the accompanying lesson.
"""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
matplotlib.rcParams.update({'font.size':12,'axes.titlesize':14,'svg.hashsalt':'AN01-U122','font.family':'DejaVu Sans'})
root=Path(__file__).resolve().parent
fig,axs=plt.subplots(2,2,figsize=(14,9),layout='constrained')
navy='#153b5b';orange='#bd5b21';teal='#087e8b'
neg=np.linspace(-3,-.002,600);pos=-neg[::-1]
ax=axs[0,0]
ax.plot(neg,np.exp(1/neg),lw=2.5,color=teal)
ax.plot([0,3],[0,0],lw=2.5,color=teal)
ax.scatter([0],[0],color=teal,s=35)
ax.set(title=r'$x^2u^\prime+u=0$: one flat branch',xlabel=r'$x$',ylabel=r'$u$',ylim=(-.08,1.15))
ax.text(.4,.8,'The growing positive branch\nhas no distributional extension.',fontsize=11,color=navy)
ax.text(-2.8,.12,r'$u=e^{1/x}$ for $x<0$',color=teal)
ax=axs[0,1]
ax.plot(neg,np.exp(-1/(2*neg**2)),lw=2.5,color=teal,label=r'$C_-=1$')
ax.plot(pos,2*np.exp(-1/(2*pos**2)),lw=2.5,color=orange,label=r'$C_+=2$')
ax.scatter([0],[0],color=navy,s=35)
ax.set(title=r'$x^3u^\prime-u=0$: independent flat branches',xlabel=r'$x$',ylabel=r'$u$',ylim=(-.08,2.2))
ax.legend(loc='upper left')
ax=axs[1,0]
x=np.linspace(.002,3,500)
ax.plot([-2,0],[0,0],lw=2.5,color=navy)
ax.plot(x,np.exp(((x+1)**-2-1)/2),lw=2.5,color=navy)
ax.scatter([0,0],[0,1],s=55,facecolors='white',edgecolors=navy,zorder=4)
ax.axvline(-1,color=orange,ls='--',lw=1.3)
ax.annotate('singular point',xy=(-1,.04),xytext=(-1.9,.55),arrowprops={'arrowstyle':'->','color':orange},color=orange)
ax.annotate('',xy=(0,.97),xytext=(0,.03),arrowprops={'arrowstyle':'->','color':teal,'lw':2})
ax.text(.13,.3,'unit jump',color=teal)
ax.set(title=r'$(x+1)^3u^\prime+u=\delta_0$: outward forcing',xlabel=r'$x$',ylabel=r'$u$',ylim=(-.08,1.2))
ax=axs[1,1]
zeros=np.pi/2+np.arange(-2,3)*np.pi
values=[.5,1.4,.8,1.8]
for j,d in enumerate(values):
 ax.plot(zeros[j:j+2],[d,d],lw=2.5,color=navy)
 ax.scatter(zeros[j:j+2],[d,d],facecolors='white',edgecolors=navy,s=40,zorder=3)
for z in zeros:
 ax.axvline(z,color=teal,ls=':',alpha=.7,lw=1)
ax.set(title=r'$\cos^2x\,u^\prime=0$: free interval constants',xlabel=r'$x$',ylabel=r'$u$',ylim=(-.08,2.1),xticks=zeros,xticklabels=[r'$-3\pi/2$',r'$-\pi/2$',r'$\pi/2$',r'$3\pi/2$',r'$5\pi/2$'])
ax.text(.03,.95,r'Point coefficients $c_j=0$ in this example',transform=ax.transAxes,va='top',color=teal,fontsize=11)
for ax in axs.flat:
 ax.spines[['top','right']].set_visible(False)
 ax.axhline(0,color='#aeb8c1',lw=.7,zorder=0)
 ax.grid(alpha=.15)
fig.suptitle('Distributional equations at zeros of the leading coefficient',fontsize=19,color=navy)
fig.savefig(root/'flat-branches-and-degenerate-equations.png',dpi=150,facecolor='white')
svg=root/'flat-branches-and-degenerate-equations.svg'
fig.savefig(svg,metadata={'Date':None,'Creator':'GPT-6 Astra (OpenAI)'},facecolor='white')
svg.write_text('\n'.join(line.rstrip() for line in svg.read_text(encoding='utf-8').splitlines())+'\n',encoding='utf-8')
plt.close(fig)
