"""Exact scientific plots for polynomial strengths and sharp heat derivative growth."""
from pathlib import Path
import json,math
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
HERE=Path(__file__).resolve().parent;OUT=HERE/'figures';OUT.mkdir(exist_ok=True)
plt.rcParams.update({'font.family':'DejaVu Sans','font.size':11,'axes.titlesize':13,
 'svg.hashsalt':'AN02-exercise-bridges-175','savefig.facecolor':'white'})
def save(fig,name):
 fig.savefig(OUT/(name+'.png'),dpi=180,bbox_inches='tight')
 fig.savefig(OUT/(name+'.svg'),bbox_inches='tight',metadata={'Date':None})
 plt.close(fig)
x=np.linspace(0,8,500);d=np.sqrt(1+x*x);ratio=(d*d+2)/(2*np.sqrt(d*d+1))
fig,ax=plt.subplots(1,2,figsize=(13.2,5.7),layout='constrained')
ax[0].plot(x,ratio,lw=2.4,color='#176b91',label='Full strength ratio '+r'$r_P$')
ax[0].plot(x,d/2,lw=2.1,ls='--',color='#ad542c',label=r'$d/2,\quad d=\sqrt{1+\xi^2}$')
ax[0].plot(x,(1+d)/4,lw=2,ls=':',color='#534594',label=r'Proved lower bound $(1+d)/4$')
ax[0].set(xlabel=r'Real sample $\xi$',ylabel='Exact ratio or bound',
 title=r'Repeated complex root: $P(z)=(z-i)^2$')
ax[0].legend(loc='upper left',fontsize=9)
xx=np.linspace(-3,3,600)
ax[1].plot(xx,(xx*xx+2)/(2*np.sqrt(1+xx*xx)),lw=2.4,color='#176b91',label='Full ratio: ordinary first and second jets')
for part in [xx[xx<0],xx[xx>0]]:
 ax[1].plot(part,np.abs(part)/2,lw=2.1,ls='--',color='#ad542c')
ax[1].plot([],[],lw=2.1,ls='--',color='#ad542c',label=r'Raw $|P|/|P^\prime|$ away from zero')
ax[1].plot(0,0,'o',ms=7,mfc='white',mec='#ad542c',mew=1.6)
ax[1].plot(0,1,'o',ms=5,color='#176b91')
ax[1].text(0,.65,'Raw quotient undefined at 0',ha='center',fontsize=10)
ax[1].set(xlabel=r'Real sample $\xi$',ylabel='Exact ratio',
 title=r'Real collision: $P(z)=z^2$, full ratio at zero = 1',ylim=(-.08,1.93))
ax[1].legend(loc='upper center',fontsize=8.8)
for a in ax:a.grid(alpha=.2)
save(fig,'repeated-roots-strength-and-distance')

t=np.geomspace(.1,20,500);orders=np.arange(1,25)
spatial=np.array([np.sqrt(2)*math.exp(math.lgamma(int(j)+1)/j)/j for j in orders])
temporal=np.array([2*math.exp(math.lgamma(2*int(j)+1)/j)/(j*j) for j in orders])
fig,ax=plt.subplots(1,2,figsize=(13.2,5.7),layout='constrained')
ax[0].loglog(t,np.sqrt(2)*t,lw=2.4,color='#176b91',label=r'$|z_1(t)|=\sqrt{2}\,t$')
ax[0].loglog(t,2*t*t,lw=2.4,color='#ad542c',label=r'$|z_2(t)|=2t^2$')
ax[0].set(xlabel=r'Actual imaginary norm $|\operatorname{Im}z(t)|=t$',
 ylabel='Actual complex coordinate magnitude',
 title='Heat zeros: '+r'$z(t)=((1+i)t,-2t^2)$')
ax[0].legend(loc='upper left',fontsize=10)
ax[1].plot(orders,spatial,'o-',color='#176b91',lw=2,ms=4,
 label=r'Spatial: $|D_1^ju(0,0)|^{1/j}/j$')
ax[1].plot(orders,temporal,'s-',color='#ad542c',lw=2,ms=4,
 label=r'Time: $|D_2^ju(0,0)|^{1/j}/j^2$')
ax[1].set(xlabel='Derivative order j',ylabel='Exact normalized derivative magnitude',
 title='One actual heat solution, exponential parameter a₀=1',ylim=(0,4.35))
ax[1].legend(loc='upper right',fontsize=9)
for a in ax:a.grid(alpha=.2)
save(fig,'heat-zero-geometry-and-derivative-growth')
geometry=dict(complex_polynomial_root='P(z)=(z-i)^2',distance='sqrt(1+xi^2)',
 strength=dict(A='d^2+2',B='2*sqrt(d^2+1)',ratio='(d^2+2)/(2*sqrt(d^2+1))',
  lower_bounds=['d/2','(1+d)/4'],ordinary_derivatives_not_factorial_normalized=True),
 real_collision=dict(P='z^2',A='xi^2+2',B='2*sqrt(1+xi^2)',ratio_at_zero=1,
  raw_ratio='|xi|/2 only for xi!=0',raw_at_zero='undefined; plotted open circle'),
 heat=dict(P='z1^2+i*z2',operator='partial_x2-partial_x1^2',
  actual_complex_curve='((1+i)*s,-2*s^2)',ambient_real_dimension=4,
  real_coordinates='(s,-2*s^2)',imaginary_coordinates='(s,0)',imaginary_norm='s for s>0',
  magnitudes=['sqrt(2)*s','2*s^2'],plots_are_exact_scalar_magnitudes=True,
  solution='integral_0^infty exp(-a0*s+(i-1)*x1*s-2*i*x2*s^2) ds',
  parameter_measure='real Lebesgue ds, not full complex-surface area',
  domain='x1>-a0, x2 real',a0=1,
  spatial_D_derivative='(1+i)^j*j!/a0^(j+1)',
  time_D_derivative='(-2)^j*(2*j)!/a0^(2*j+1)',
  convention='D=-i*partial',plotted_orders=[int(j) for j in orders]),
 exact_proof_locators=['EB1-EB5','EB9-EB16','L154.1-L154.10','L154.13'],
 human_source='Lars Hormander, Analysis of Linear PDE II, two exercises on printed page291; Theorems11.1.7,11.4.1,11.4.8',
 original_sources=True,blender_useful=False,
 blender_reason='Exact scalar strengths, four-dimensional curve coordinates and derivative orders are fully explained by scientific plots.')
(OUT/'geometry.json').write_text(json.dumps(geometry,indent=2)+'\n',encoding='utf-8')
print(json.dumps({'figure_pairs':2,'geometry':str(OUT/'geometry.json')}))
