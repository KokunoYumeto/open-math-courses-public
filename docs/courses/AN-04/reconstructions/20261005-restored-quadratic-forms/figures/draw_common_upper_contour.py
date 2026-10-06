"""Exact common-circle construction A13, with a labelled magnified region."""
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
HERE=Path(__file__).resolve().parent
plt.rcParams.update({'font.family':'DejaVu Sans','mathtext.fontset':'stix',
                     'svg.fonttype':'path','font.size':13})
M,delta=2.,1.
L=M*M/delta+delta
radius=L-delta/2
theta=np.linspace(0,2*np.pi,1601)
x=np.linspace(-np.sqrt(3),np.sqrt(3),1001)
y=np.sqrt(M*M-x*x)
fig,axes=plt.subplots(1,2,figsize=(12,7),layout='constrained')
for ax in axes:
    ax.axhline(0,color='#777777',lw=.8)
    ax.axvline(0,color='#777777',lw=.8)
    ax.fill_between(x,delta,y,color='#197b87',alpha=.32,label='Allowed upper region')
    ax.fill_between(x,-y,-delta,color='#a55c36',alpha=.28,label='Allowed lower region')
    ax.plot(M*np.cos(theta),M*np.sin(theta),color='#606b75',ls='--',lw=1.2)
    ax.plot(radius*np.cos(theta),L+radius*np.sin(theta),color='#433e84',lw=2.2)
    ax.set_aspect('equal')
    ax.set_xlabel(r'$\operatorname{Re}z$')
    ax.set_ylabel(r'$\operatorname{Im}z$')
    ax.spines[['top','right']].set_visible(False)
axes[0].set(xlim=(-5.2,5.2),ylim=(-2.5,10.2))
axes[0].set_title(r'Common contour: $c=5i,\ R=9/2$')
axes[0].plot([0],[L],'o',color='#433e84',ms=4)
axes[0].annotate(r'$5i$',(0,L),xytext=(10,8),textcoords='offset points')
for a in [.2,2.1,4.6]:
    axes[0].annotate('',xy=(radius*np.cos(a+.15),L+radius*np.sin(a+.15)),
        xytext=(radius*np.cos(a),L+radius*np.sin(a)),
        arrowprops={'arrowstyle':'-|>','color':'#433e84','lw':1.8,'mutation_scale':15})
axes[0].text(.5,-.16,'Counterclockwise orientation\nAll upper spectral values lie inside',
             transform=axes[0].transAxes,ha='center',va='top',fontsize=11)
axes[1].set(xlim=(-2.35,2.35),ylim=(-2.35,2.65))
axes[1].set_title(r'Magnified bound: $|z|\leq2,\ |\operatorname{Im}z|\geq1$')
for yy in [-1,1]:
    axes[1].axhline(yy,color='#777777',ls=':',lw=.9)
axes[1].plot([0],[.5],'o',color='#433e84',ms=4)
axes[1].annotate(r'Lowest contour point: $i/2$',xy=(0,.5),xytext=(-2.1,.15),
                fontsize=11,arrowprops={'arrowstyle':'-','lw':.8})
axes[1].text(.5,-.14,'Shading shows regions, not particular eigenvalues',
             transform=axes[1].transAxes,ha='center',fontsize=11)
axes[1].legend(loc='lower center',bbox_to_anchor=(.5,-.36),frameon=False,fontsize=11)
fig.suptitle('A fixed contour through changes in Jordan structure',fontsize=17)
fig.savefig(HERE/'common-upper-contour.svg',metadata={
    'Creator':'Original AN-04 mathematical drawing','Date':None,
    'Description':'A13 with M=2, delta=1, L=5 and radius 4.5. Exact admissible spectral regions and a magnified view; no eigenvalue sample is asserted.'})
plt.close(fig)
print('Wrote the exact common contour with a separate magnified region.')
