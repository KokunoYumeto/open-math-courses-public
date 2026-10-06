"""Exact coefficient illustration for lesson L042, (3.2) and (8.1).
CC0; GPT-6.1 Sol (OpenAI), Ultra reasoning effort, October 2026.
Run this file with Python, NumPy and Matplotlib to reproduce the adjoining PNG.
This illustrates G alone; it does not assert a full two-operator model.
"""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.gridspec import GridSpec

p=10000
e=1/(10*p)
a=0.5
c=1/(2*(1-e))
def curves(X):
    t=a+np.sqrt(e)*X
    original=c*X**2*(1+e*t)
    taylor=c*((1-e)*X**2-0.75*np.sqrt(e)*X-0.125)
    return original,taylor,taylor+1

plt.rcParams.update({'font.family':'DejaVu Sans','font.size':15,
    'axes.titlesize':18,'axes.labelsize':16,'figure.facecolor':'#fffdfa',
    'axes.facecolor':'#fffdfa','savefig.facecolor':'#fffdfa',
    'svg.hashsalt':'AN05-L042'})
fig=plt.figure(figsize=(14,9.2),dpi=150)
gs=GridSpec(2,2,figure=fig,height_ratios=[4,1.15],width_ratios=[1.3,1],
    top=.77,bottom=.07,left=.07,right=.97,hspace=.47,wspace=.3)
fig.text(.07,.94,'A positive coefficient needs a positive polynomial model',
    fontsize=23,weight='bold',color='#172d44')
fig.text(.07,.887,r'$p=10^4,\quad e=(10p)^{-1},\quad a=1/2,\quad c=[2(1-e)]^{-1}$',fontsize=17)
fig.text(.07,.844,r'Exact coordinates: $X=(t-a)/\sqrt{e}$ and $Y=G/e$; the vertical scale is amplified.',fontsize=15)
colors=['#177467','#b54530','#3a61aa']
labels=[r'$G(t)/e$: nonnegative smooth coefficient',
        r'$G_0(t)/e$: quadratic Taylor polynomial',
        r'$(G_0(t)+e)/e$: positive correction']
for panel,xspan,ylim,title in [(0,(-2.15,2.15),(-.18,3.6),'The exact Taylor error can change the sign'),
                              (1,(-.5,.5),(-.085,.14),'A closer view near the smooth zero')]:
    ax=fig.add_subplot(gs[0,panel]);X=np.linspace(*xspan,1201)
    for y,color,label in zip(curves(X),colors,labels):
        if panel==1 and color==colors[2]:continue
        ax.plot(X,y,color=color,lw=2.7,label=label)
    ax.axhline(0,color='#4b5664',lw=1);ax.axvline(0,color='#aeb5bd',lw=1,ls=':')
    ax.set(xlim=xspan,ylim=ylim,xlabel=r'$X=(t-a)/\sqrt{e}$',ylabel='Scaled coefficient value',title=title)
    ax.grid(alpha=.18)
    if panel==0:ax.legend(loc='upper left',fontsize=11.5,framealpha=.96)
    else:
        ax.scatter([0,0],[0,-c/8],color=colors[:2],s=42,zorder=4)
        ax.annotate(r'$G(a)=0$',(0,0),xytext=(-.45,.09),
            arrowprops={'arrowstyle':'->','color':colors[0]},color=colors[0])
        ax.annotate(r'$G_0(a)/e=-c/8<0$',(0,-c/8),xytext=(-.46,-.077),fontsize=13,
            arrowprops={'arrowstyle':'->','color':colors[1]},color=colors[1])
ax=fig.add_subplot(gs[1,:]);ax.axis('off')
ax.text(0,1.03,'Repair the pair together to preserve the residual intercept',fontsize=18,weight='bold',color='#172d44')
ax.text(0,.51,r'$G_*=G_0+\kappa/p,\qquad F_*=F_0+(\kappa/p)H_0$',fontsize=22,color='#3a61aa')
ax.text(0,-.02,r'$F_*-G_*H_0=F_0-G_0H_0=R$',fontsize=22,color='#172d44')
fig.text(.07,.019,'Coefficient example: Exercise 2, (8.1). Paired correction: Section 3, (3.2)–(3.3). No full intercept is specified in the plot.',fontsize=11.5,color='#414b57')
target=Path(__file__).with_name('smooth-positive-approximation.png')
fig.savefig(target,dpi=150,metadata={'Software':'AN05-L042 reproducible mathematical illustration; CC0'})
plt.close(fig)
print(target.name)
