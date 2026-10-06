"""Exact transport formulas for U002 Theorem6.2 / Solution7.2. CC0.

Original figure by GPT-6.1 Sol (OpenAI), Ultra. No external image is used.
Unit forcing on [0,2], D_t=-i d/dt, unitary Fourier transform, energy 0.
All curves are finite samples; the analytic limits are proved in the lesson.
"""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

HERE=Path(__file__).resolve().parent
plt.rcParams.update({'font.family':'DejaVu Sans','font.size':12,
                    'svg.hashsalt':'AN06-endpoint-tail-v1'})
EPS=[.5,.2,.05];COLORS=['#b25318','#167f72','#7750a4']
def boundary(t):return np.where(t<0,0,np.minimum(t,2))
def nonreal(t,e):
    t=np.asarray(t,dtype=float);c=-np.expm1(-2*e)/e
    return np.where(t<0,0,np.where(t<=2,-np.expm1(-e*np.maximum(t,0))/e,c*np.exp(-e*np.maximum(t-2,0))))
def primitive_boundary(r):
    r=np.asarray(r,dtype=float);b=np.minimum(r,2)
    return b**3/3+4*np.maximum(r-2,0)
def primitive_nonreal(r,e):
    r=np.asarray(r,dtype=float);b=np.minimum(r,2);l=np.maximum(r-2,0);c=-np.expm1(-2*e)/e
    return (b+2*np.expm1(-e*b)/e-np.expm1(-2*e*b)/(2*e))/e**2+c*c*(-np.expm1(-2*e*l))/(2*e)
def primitive_error(r,e):
    r=np.asarray(r,dtype=float);b=np.minimum(r,2);l=np.maximum(r-2,0);c=-np.expm1(-2*e)/e
    interior=b**3/3-b*b/e+b/e**2-2*b*np.exp(-e*b)/e**2-np.expm1(-2*e*b)/(2*e**3)
    return interior+4*l+4*c*np.expm1(-e*l)/e-c*c*np.expm1(-2*e*l)/(2*e)

fig,axes=plt.subplots(3,1,figsize=(11.5,11),constrained_layout=True)
fig.suptitle('A real-energy transport wave keeps its tail mass',fontsize=19,fontweight='bold')
t=np.linspace(-2,45,1400);r=np.geomspace(4,2**14,700);j=np.arange(1,15);rj=2.**j
axes[0].plot(t,boundary(t),color='#192f50',lw=2.8,label=r'Boundary $\operatorname{Im}u_+(t)$')
for e,c in zip(EPS,COLORS):
    axes[0].plot(t,nonreal(t,e),color=c,lw=2,label=rf'$\operatorname{{Im}}R_0(i\varepsilon)f$, $\varepsilon={e:g}$')
    axes[1].plot(r,primitive_nonreal(r,e)/r,color=c,lw=2,label=rf'$\varepsilon={e:g}$; limit $0$')
    shell=(primitive_error(rj,e)-primitive_error(rj/2,e))/rj
    axes[2].plot(j,shell,'o-',color=c,lw=2,ms=4,label=rf'$\varepsilon={e:g}$')
axes[0].axvspan(0,2,color='#cbd9ec',alpha=.35)
axes[0].set(xlabel=r'Position $t$',ylabel='Imaginary amplitude',title=r'1. Exact solutions for $f=1_{[0,2]}$, $\lambda=0$')
axes[0].legend(fontsize=10,loc='upper right',ncol=2)
axes[1].plot(r,primitive_boundary(r)/r,color='#192f50',lw=2.8,label='Boundary; limit 4')
axes[1].axhline(4,color='#192f50',ls=':',lw=1.4)
axes[1].set(xscale='log',xlabel=r'Ball radius $R$',ylabel=r'$R^{-1}\int_{-R}^{R}|u|^2$',title='2. Taking the radius to infinity distinguishes the solutions')
axes[1].legend(fontsize=10,ncol=2)
axes[2].axhline(2,color='#192f50',ls=':',lw=1.7,label='Exact squared-error limit 2')
axes[2].set(xlabel=r'Shell index $j$, with $R_j=2^j$',ylabel=r'$R_j^{-1}\|R_0(i\varepsilon)f-u_+\|_{L^2(A_j)}^2$',
            title=r'3. Every nonreal solution has a norm error at least $\sqrt{2}$')
axes[2].legend(fontsize=10,loc='lower right',ncol=2)
for ax in axes:
    ax.grid(True,alpha=.2);ax.spines[['top','right']].set_visible(False)
    ax.set_ylim(bottom=0)
fig.savefig(HERE/'endpoint-tail-and-boundary.png',dpi=150,metadata={'Software':'Matplotlib; original CC0 mathematical figure'})
fig.savefig(HERE/'endpoint-tail-and-boundary.svg',metadata={'Date':None,'Creator':'GPT-6.1 Sol (OpenAI), Ultra; CC0'})
print('Exact formula figure saved; analytic limits 4, 0, 2 and norm obstruction sqrt(2).')
