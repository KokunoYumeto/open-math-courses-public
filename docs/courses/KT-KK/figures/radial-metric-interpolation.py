"""Exact hyperbolic-plane model for the radial metric estimates in Lemma 11.2.

Independent course figure. Public domain (CC0).
For curvature -1: A_t(r)=(1-t)sinh(r)^2+t r^2 in polar coordinates.
The angular eigenvalue of Hess(r^2/2) is r A_t'(r)/(2 A_t(r)).
The values at r=0 are the continuous limits, all equal to one.
"""
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np

directory=Path(__file__).resolve().parent
matplotlib.rcParams.update({
    'font.family':'DejaVu Serif','font.size':12,
    'mathtext.fontset':'dejavuserif','svg.hashsalt':'kt-kk-radial-metric-v1',
    'axes.spines.top':False,'axes.spines.right':False,
})
r=np.linspace(0,4,801)
radial=np.divide(r,np.tanh(r),out=np.ones_like(r),where=r>0)
angular_hyperbolic=np.sinh(r)**2
angular_flat=r*r
fig,ax=plt.subplots(figsize=(5.3,4.7),layout='constrained')
fig.set_facecolor('#fffdf8');ax.set_facecolor('#fffdf8')
ax.fill_between(r,1,1+r,color='#e6ece5',label=r'Proved range $1\leq\lambda_t\leq1+r$')
for t,color,label in [
    (0,'#246b50',r'$t=0$ (hyperbolic)'),
    (.5,'#bc6531',r'$t=1/2$'),
    (1,'#335b8e',r'$t=1$ (flat)'),
]:
    denominator=(1-t)*angular_hyperbolic+t*angular_flat
    numerator=(1-t)*angular_hyperbolic*radial+t*angular_flat
    value=np.divide(numerator,denominator,out=np.ones_like(r),where=denominator>0)
    ax.plot(r,value,color=color,lw=2.3,label=label)
ax.plot(r,1+r,color='#747b72',ls='--',lw=1.2)
ax.set(xlim=(0,4),ylim=(.75,5.15),
       xlabel=r'Radius $r=|z|$',
       ylabel=r'Angular Hessian eigenvalue $\lambda_t$',
       title=r'Radial Hessian of $r^2/2$')
ax.set_xticks(range(5));ax.set_yticks(range(1,6))
ax.grid(alpha=.18)
ax.legend(loc='upper left',frameon=True,facecolor='#fffdf8',edgecolor='#d7dbd0',fontsize=10.5)
base=directory/'radial-metric-interpolation'
fig.savefig(base.with_suffix('.svg'),metadata={
    'Title':'Radial metric interpolation on the hyperbolic plane',
    'Description':'Angular Hessian eigenvalues for curvature -1, with the proved radial bounds from Lemma 11.2 of Descent and the K-theory of crossed products.',
    'Creator':'GPT-6.1 Sol (OpenAI) in Codex, Ultra setting',
    'Rights':'Public domain (CC0)',
    'Date':'2026-10-02',
})
fig.savefig(base.with_suffix('.png'),dpi=180,metadata={
    'Title':'Radial metric interpolation on the hyperbolic plane',
    'Author':'GPT-6.1 Sol (OpenAI) in Codex, Ultra setting',
    'Copyright':'Public domain (CC0)',
})
plt.close(fig)
print('Created radial-metric-interpolation.svg and .png')
