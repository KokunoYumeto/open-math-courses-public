"""Exact smooth observation geometry and the explicit six-layer derivative bound."""
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import Circle,Rectangle
import numpy as np
R=Path(__file__).resolve().parent
plt.rcParams.update({'font.family':'DejaVu Sans','mathtext.fontset':'dejavusans','font.size':12})
fig=plt.figure(figsize=(14.5,7.8),layout='constrained');g=fig.add_gridspec(2,2,height_ratios=[1,0.28])
a=fig.add_subplot(g[0,0]);b=fig.add_subplot(g[0,1]);cap=fig.add_subplot(g[1,:])
A=1.5;B=1.6;p=np.array([0.6,0.85]);delta=0.12
samples=np.array([(x,y) for x in [-1.2,0,1.2] for y in [0,0.4,1.5]])
dist=np.linalg.norm(samples-p,axis=1).min();assert delta<min(p[0],p[1],A-p[0],B-p[1],dist)/4
a.add_patch(Rectangle((-A,0),2*A,B,facecolor='#eef3f7',edgecolor='#3d5368'))
a.scatter(samples[:,0],samples[:,1],marker='x',s=55,color='#2b3b4c',label='the finite samples')
for sign,color in [(1,'#af482b'),(-1,'#246a94')]:
    pp=p*np.array([sign,1]);a.add_patch(Circle(pp,delta,fc=color,alpha=0.3,ec=color,lw=2));a.plot(*pp,'o',color=color)
    a.text(pp[0]+sign*0.17,pp[1]+0.12,r'$p$' if sign==1 else r'$\rho p$',ha='left' if sign==1 else 'right',color=color,fontsize=14)
a.text(-1.4,1.35,r'$p=(0.6,0.85),\quad\delta=0.12$',fontsize=11)
a.text(-1.4,0.62,'Every sampled jet is unchanged.',fontsize=11)
a.text(-1.4,-0.19,r'$f_1^{[m]}(p)=f_1(p)+\varepsilon m$',fontsize=14)
a.set(xlim=(-1.75,1.75),ylim=(-0.32,1.82),xlabel=r'$y_1$',ylabel=r'$y_2$',title='Smooth perturbations away from the samples')
a.set_aspect('equal',adjustable='box');a.spines[['top','right']].set_visible(False)
ell=np.arange(7);C2=4/(3*np.sqrt(3));bounds=2*ell+1.5*C2*C2*ell*(ell-1)
b.plot(ell,bounds,'o-',lw=2,color='#2a6b91',label=r'proved global bound $C_\ell$')
b.plot(ell,2*ell,'s--',lw=1.8,color='#ad4c2b',label=r'exact $|q_\ell^{\prime\prime\prime}(0)|=2\ell$')
b.annotate(r'$116/3$',(6,bounds[-1]),(-55,8),textcoords='offset points',fontsize=14,color='#2a6b91')
b.annotate(r'$12$',(6,12),(-26,10),textcoords='offset points',fontsize=14,color='#ad4c2b')
b.set(xlim=(-0.15,6.3),ylim=(-1,44),xticks=ell,xlabel='number of active tanh layers',ylabel='absolute third derivative bound',title='A fully specified six-layer network')
b.text(0.2,39,r'$q_\ell=\tanh^{\circ\ell}(z_1)$',fontsize=14)
b.legend(loc='upper left',bbox_to_anchor=(0,-0.16),frameon=False,fontsize=11);b.spines[['top','right']].set_visible(False)
cap.axis('off')
rows=[
 'Left: the two compact supports avoid every sample, the wall and the rectangle boundary; NB1–NB7 retain the exact parity and residual maps.',
 'Right: one active channel in each of six 30-unit hidden layers. Every other weight and bias is zero; the output weight is one.',
 r'$C_\ell=2\ell+\frac{3}{2}\left(\frac{4}{3\sqrt{3}}\right)^2\ell(\ell-1).$ The graph evaluates this proved bound and the exact origin derivative.',
 'Proof: NB1–NB18. Human architecture source: Wang, Lai, Gómez-Serrano and Buckmaster, arXiv:2201.06780v3, main169–203.'
]
for yy,txt in zip([0.95,0.68,0.42,0.12],rows):cap.text(0,yy,txt,va='top',fontsize=11)
for ext in ['png','svg']:fig.savefig(R/f'profile-samples-network-bounds.{ext}',dpi=180,facecolor='white')
print(str(R/'profile-samples-network-bounds.png'))
