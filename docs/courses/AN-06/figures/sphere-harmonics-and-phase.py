"""Exact local round-sphere spectrum diagram; U028 Section 6. CC0."""
from pathlib import Path
from math import comb, factorial, ceil
from fractions import Fraction
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch

matplotlib.rcParams.update({'font.family':'DejaVu Sans','font.size':17,'svg.hashsalt':'AN06-sphere-harmonics-v1'})
out=Path(__file__).resolve().parent
def multiplicity(n,l):
    a=comb(l+n,n)-(comb(l+n-2,n) if l>=2 else 0)
    prod=1
    for r in range(1,n-1):prod*=l+r
    assert Fraction((2*l+n-1)*prod,factorial(n-1))==a
    return a
for n in range(2,12):
    for l in range(20):multiplicity(n,l)
fig=plt.figure(figsize=(8,12),facecolor='white')
gs=fig.add_gridspec(4,1,height_ratios=[2.8,2.0,2.4,2.4],hspace=.28,left=.08,right=.96,top=.92,bottom=.075)
fig.suptitle('The complete spectrum of the unit round sphere',fontsize=21,y=.977)
fig.text(.5,.943,r'$n\geq2$: exact local harmonic model',ha='center',fontsize=15)
ax=fig.add_subplot(gs[0]);ax.set_axis_off()
ax.add_patch(FancyBboxPatch((.01,.03),.98,.93,boxstyle='round,pad=.015',transform=ax.transAxes,facecolor='#edf4fa',edgecolor='#9bb2c6'))
for y,t in [(.85,r'$\Delta(r^{2j+2}H_m)=c_{j,m,n}\,r^{2j}H_m$'),
            (.64,r'$c_{j,m,n}=2(j+1)(2m+2j+n+1)>0$'),
            (.42,r'$\Delta:r^2\mathcal{P}_{\ell-2}\ \longrightarrow\ \mathcal{P}_{\ell-2}$'),
            (.25,'is an isomorphism in each degree'),
            (.10,r'$\mathcal{P}_{\ell}=\mathcal{H}_{\ell}\oplus r^2\mathcal{P}_{\ell-2}$')]:
    ax.text(.5,y,t,ha='center',va='center',transform=ax.transAxes,fontsize=17)
ax=fig.add_subplot(gs[1]);ax.set_axis_off()
for y,t in [(.87,'Injective restriction to the sphere'),
            (.60,'Orthogonality + polynomial density + closure'),
            (.31,r'$L^2(S^n)=\widehat{\bigoplus}_{\ell\geq0}\mathcal{H}_{\ell}|_{S^n}$'),
            (.04,r'$-\Delta_{S^n}|_{\mathcal{H}_{\ell}}=\ell(\ell+n-1)$')]:
    ax.text(.5,y,t,ha='center',va='center',transform=ax.transAxes,fontsize=18)
ax=fig.add_subplot(gs[2]);ax.set_axis_off()
ax.add_patch(FancyBboxPatch((.01,.01),.98,.94,boxstyle='round,pad=.015',transform=ax.transAxes,facecolor='#edf4fa',edgecolor='#9bb2c6'))
ax.text(.5,.83,'Exact harmonic multiplicities',ha='center',transform=ax.transAxes,fontsize=19)
xs=[.12,.36,.52,.68,.84]
for x,t in zip(xs,['sphere',r'$\ell=0$',r'$\ell=1$',r'$\ell=2$',r'$\ell=3$']):ax.text(x,.68,t,ha='center',transform=ax.transAxes,fontsize=16)
for y,n in zip([.51,.36,.21,.06],range(2,6)):
    for x,t in zip(xs,[f'$S^{n}$',*[str(multiplicity(n,l)) for l in range(4)]]):ax.text(x,y,t,ha='center',transform=ax.transAxes,fontsize=17)
ax=fig.add_subplot(gs[3]);ax.set_axis_off()
ax.add_patch(FancyBboxPatch((.01,.01),.98,.94,boxstyle='round,pad=.015',transform=ax.transAxes,facecolor='#fff3e9',edgecolor='#c7ab92'))
ax.text(.5,.83,r'$\alpha=(n-1)/2,\quad\beta=\lceil\alpha\rceil-\alpha$',ha='center',transform=ax.transAxes,fontsize=18)
xs=[.10,.27,.43,.63,.86]
for x,t in zip(xs,['$n$',r'$\alpha$',r'$\beta$',r'$e^{-2\pi iA}$',r'$\min\sigma(L_n)$']):ax.text(x,.67,t,ha='center',transform=ax.transAxes,fontsize=14)
for y,n in zip([.51,.36,.21,.06],range(2,6)):
    alpha=Fraction(n-1,2);beta=ceil(alpha)-alpha;phase=(-1)**(n-1)
    vals=[str(n),str(alpha),str(beta),'$-I$' if phase<0 else '$I$',str(ceil(alpha))]
    assert beta in [0,Fraction(1,2)] and phase*((-1) if beta else 1)==1
    for x,t in zip(xs,vals):ax.text(x,y,t,ha='center',transform=ax.transAxes,fontsize=17)
fig.text(.5,.025,r'$A=(-\Delta_{S^n}+\alpha^2)^{1/2},\quad L_n=A+\beta,\quad e^{-2\pi iL_n}=I$'+'\nU028 Section 6: harmonic decomposition, density and operator spectrum. CC0.',ha='center',fontsize=14)
fig.savefig(out/'sphere-harmonics-and-phase.png',dpi=180,metadata={'Software':'Matplotlib; independently authored exact AN06 proof diagram'})
fig.savefig(out/'sphere-harmonics-and-phase.svg',metadata={'Date':None,'Creator':'GPT-6.1 Sol (OpenAI), Ultra','Description':'Exact harmonic dimensions and unchanged round-sphere square roots and phases; local proof in U028.'})
plt.close(fig)
