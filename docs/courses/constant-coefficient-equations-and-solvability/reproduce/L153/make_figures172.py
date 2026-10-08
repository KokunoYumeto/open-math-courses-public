"""Original scientific plots with the exact topology, contour and curvature data."""
from pathlib import Path
import json
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
HERE=Path(__file__).resolve().parent;OUT=HERE/'figures';OUT.mkdir(exist_ok=True)
plt.rcParams.update({'font.family':'DejaVu Sans','font.size':11,
 'axes.titlesize':13,'svg.hashsalt':'AN02-smooth-topology-172','savefig.facecolor':'white'})
def save(fig,name):
 fig.savefig(OUT/(name+'.png'),dpi=180,bbox_inches='tight')
 fig.savefig(OUT/(name+'.svg'),bbox_inches='tight',metadata={'Date':None})
 plt.close(fig)
def bump(x):
 out=np.zeros_like(x);inside=np.abs(x)<.25
 out[inside]=np.exp(1-1/(1-16*x[inside]**2));return out
x=np.linspace(.6,6.3,1800);colors=['#176b91','#ad542c','#534594']
fig,ax=plt.subplots(2,1,figsize=(12.6,7),layout='constrained',sharex=True)
for j,color in zip([1,3,5],colors):
 center=j+.5
 ax[0].plot(x,2**(-j)*bump(x-center),color=color,lw=2.3,label='j='+str(j)+', amplitude '+str(2**(-j)))
 ax[1].plot(x,bump(x-center),color=color,lw=2.3,label='j='+str(j)+', q(v_j)=1')
ax[0].set(ylabel='Actual bump amplitude',title='Escaping supports with every fixed derivative supremum tending to zero',ylim=(-.025,.56))
ax[1].set(xlabel='Real physical coordinate x',ylabel='Locally weighted amplitude',
 title=r'Exact products $\rho_0v_j=b(x-j-1/2)$',ylim=(-.05,1.14))
for a in ax:a.grid(alpha=.2);a.legend(loc='upper right',fontsize=10)
save(fig,'moving-bumps-and-local-test-weight')

xi=np.linspace(-4,4,600)
fig,ax=plt.subplots(1,2,figsize=(13.2,5.7),layout='constrained')
for R,color in zip([.3,.7,1.3],colors):
 ax[0].plot(xi,R*np.log(2+xi*xi),lw=2.3,color=color,label='R='+str(R))
 ax[0].plot(0,R*np.log(2),'o',color=color,ms=4)
ax[0].set(xlabel=r'Real coordinate $\xi$',ylabel=r'Imaginary height $\operatorname{Im}z_R$',
 title='Exact logarithmic Fourier contours\n'+r'$z_R=\xi+iR\log(2+\xi^2)$')
ax[0].legend(loc='upper center',fontsize=10)
r=np.geomspace(.006,40,600);q=1/(1+r*r);a=2;t=4096
radial=(q**.75+.25-.75*q)/4
actual=radial-(a/np.sqrt(t))*q**1.25
ax[1].semilogx(r,radial,lw=2.1,ls='--',color='#ad542c',label='Radial correction alone')
ax[1].semilogx(r,actual,lw=2.3,color='#176b91',label='Full corrected seed at '+r'$\xi=0$')
ax[1].axhline(1/32,color='.4',ls=':',label='Proved lower bound: 1/32')
ax[1].set(xlabel=r'$|\eta|/t$ (off the support-function corner)',
 ylabel=r'Levi curvature multiplied by $(t^2+\eta^2)^{3/4}$',
 title='Exact seed curvature: a=2, t=4096',ylim=(.02,.138))
ax[1].legend(loc='upper right',fontsize=9)
for z in ax:z.grid(alpha=.2)
save(fig,'logarithmic-contour-and-strict-curvature')
geometry=dict(bump='exp(1-1/(1-16*x^2)) for |x|<1/4, zero otherwise',
 moving_profiles=[dict(j=j,center=j+.5,amplitude=2**(-j),weighted_supremum=1) for j in [1,3,5]],
 coefficient='rho_0=sum_j>=1 2^j chi(x-j-1/2); chi=1 on [-1/4,1/4], support(-2/5,2/5)',
 selected_profiles_do_not_replace_infinite_locally_finite_family=True,
 contour=dict(z='xi+i*R*log(2+xi^2)',complex_jacobian='1+i*2*R*xi/(2+xi^2)',
  R_values=[.3,.7,1.3],height_at_zero='R*log(2)',integration_uses_complex_differential_not_arc_length=True),
 seed=dict(a=a,t=t,support_interval=[-1,1],s='t^2+eta^2',q='t^2/s',
  correction='sqrt(t^2+eta^2)/sqrt(t)-(t^2+eta^2)^(1/4)',
  exact_normalized_Levi='(q^(3/4)+1/4-3*q/4)/4-(a/sqrt(t))*q^(5/4)',
  lower_bound='1/32',classical_part_off_eta_zero=True,
  support_corner_contributes_positive_distributional_measure=True),
 exact_proof_locators=['TP11-TP16','TP26-TP31','L153.1-L153.9'],
 human_source='Lars Hormander, Analysis of Linear Partial Differential Operators II, Theorems15.4.1-15.4.3',
 original_sources=True,blender_useful=False,
 blender_reason='These exact one-dimensional profiles, complex contours and scalar curvature bounds are fully displayed by scientific plots.')
(OUT/'geometry.json').write_text(json.dumps(geometry,indent=2)+'\n',encoding='utf-8')
print(json.dumps({'figure_pairs':2,'geometry':str(OUT/'geometry.json')}))
