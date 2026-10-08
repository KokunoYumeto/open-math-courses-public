"""Exact singular-carrier separation, logarithmic strip and triangular profiles."""
from pathlib import Path
import json
import numpy as np
from scipy.optimize import brentq
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import Circle
HERE=Path(__file__).resolve().parent;OUT=HERE/'figures';OUT.mkdir(exist_ok=True)
plt.rcParams.update({'font.family':'DejaVu Sans','font.size':11,'axes.titlesize':13,
 'svg.hashsalt':'singular-support-hull188','savefig.facecolor':'white'})
def save(fig,name):
 fig.savefig(OUT/(name+'.png'),dpi=180,bbox_inches='tight')
 fig.savefig(OUT/(name+'.svg'),bbox_inches='tight',metadata={'Date':None})
 plt.close(fig)
fig,axes=plt.subplots(1,2,figsize=(13.7,6),layout='constrained')
ax=axes[0];ax.plot([0,0],[-1,1],color='#a54f35',lw=5,label=r'$K=\{0\}\times[-1,1]$')
ax.plot([0,0],[-1,1],'o',color='#a54f35');ax.plot(0,0,'o',color='#222222')
ax.add_patch(Circle((2,0),.5,facecolor='#226c9a',edgecolor='#226c9a',alpha=.13))
ax.add_patch(Circle((2,0),.5,fill=False,edgecolor='#226c9a',ls='--',lw=1.7))
ax.plot(2,0,'o',color='#226c9a')
ax.annotate('',xy=(2,0),xytext=(0,0),arrowprops={'arrowstyle':'->','color':'#226c9a','lw':1.8})
ax.text(.75,.13,r'$\theta=(1,0)$',fontsize=11)
ax.text(1.54,.66,r'$x_0=(2,0)$, radius $1/2$',fontsize=10)
ax.text(-.35,-.18,r'$p=(0,0)$',fontsize=10)
ax.plot([1.5,1.5],[-1.15,.65],color='#34725b',ls=':',lw=1.5)
ax.annotate('',xy=(1.5,-.9),xytext=(0,-.9),arrowprops={'arrowstyle':'<->','color':'#34725b'})
ax.text(.25,-1.13,r'Gap on $U$: at least $3/2$',fontsize=10,color='#34725b')
ax.set_aspect('equal',adjustable='box');ax.set(xlim=(-.6,2.95),ylim=(-1.45,1.45),
 xlabel=r'Spatial coordinate $x_1$',ylabel=r'Spatial coordinate $x_2$',title='A direction separating the whole neighborhood')
ax.legend(loc='upper left',fontsize=10)
xi=np.linspace(-4,4,601);R=2.;m=4.
height=R*np.log(2+xi*xi)
boundary=np.array([brentq(lambda y:y-m*np.log1p(np.hypot(x,y)),1e-8,100)for x in xi])
ax=axes[1];ax.fill_between(xi,0,boundary,color='#34725b',alpha=.10,label=r'Upper part of the actual $m=4$ strip')
ax.plot(xi,boundary,color='#34725b',ls='--',lw=1.7)
ax.plot(xi,height,color='#226c9a',lw=2.6,label=r'Contour height $2\log(2+\xi_1^2)$')
ax.axhline(0,color='#555555',lw=1)
for x in [-3,0,3]:
 h=R*np.log(2+x*x);ax.annotate('',xy=(x,h),xytext=(x,0),arrowprops={'arrowstyle':'->','color':'#226c9a','alpha':.65})
ax.set(xlabel=r'Real frequency $\xi_1=\operatorname{Re}\zeta_1$',ylabel=r'Imaginary frequency $\eta=\operatorname{Im}\zeta_1$',
 title=r'Exact complex slice: $\xi_2=0$, $\zeta_2=0$, $R=2$',ylim=(-.3,11.3))
ax.grid(alpha=.18);ax.legend(loc='upper right',fontsize=9)
fig.suptitle('Spatial separation turns logarithmic contour displacement into decay',fontsize=16)
save(fig,'separation-and-logarithmic-strip')

fig=plt.figure(figsize=(13.8,7),layout='constrained')
gs=fig.add_gridspec(2,2,width_ratios=[1,1.55],height_ratios=[1,1])
a=fig.add_subplot(gs[0,0]);b=fig.add_subplot(gs[1,0],sharex=a);c=fig.add_subplot(gs[:,1])
x=np.linspace(-1.6,1.6,801);a.plot(x,np.maximum(1-np.abs(x),0),color='#226c9a',lw=2.5)
a.plot([-1,0,1],[0,1,0],'o',color='#a54f35',ms=6)
a.axvspan(-1,1,color='#34725b',alpha=.07)
a.set(ylabel='Function value',title=r'The actual function $u(x)=(1-|x|)_+$',ylim=(-.15,1.25))
a.grid(alpha=.18)
b.axhline(0,color='#555555',lw=1)
for position,weight,label in [(-1,-1,r'$-\delta_{-1}$'),(0,2,r'$2\delta_0$'),(1,-1,r'$-\delta_1$')]:
 b.annotate('',xy=(position,weight),xytext=(position,0),arrowprops={'arrowstyle':'->','color':'#a54f35','lw':2.4})
 b.text(position,weight+(.17 if weight>0 else -.40),label,ha='center',fontsize=11)
b.set(xlim=(-1.6,1.6),ylim=(-1.7,2.7),xlabel=r'Physical location $x$',
 ylabel='Point-mass coefficient',title=r'The distribution $D^2u$: three signed masses')
b.grid(alpha=.18)
eta=np.linspace(-3,3,2001);nz=eta!=0
indices=[1,10,100];colors=['#226c9a','#b36829','#7356a5']
for j,color in zip(indices,colors):
 Rj=2*np.pi*j;s=np.log(Rj);v=np.full(eta.shape,np.nan)
 v[nz]=(np.log(4)+2*np.log(np.abs(np.sinh(s*eta[nz]/2)))-np.log(Rj*Rj+s*s*eta[nz]**2))/s
 c.plot(eta,v,color=color,lw=1.9,label=f'Exact Fourier profile, j={j}')
c.plot(eta,np.abs(eta)-2,color='#222222',lw=2.5,ls='--',label=r'Proper limit $|\eta|-2$')
c.plot(0,-2,'o',color='#222222',ms=5)
c.annotate(r'At $\eta=0$: $-\infty$',xy=(0,-8.1),xytext=(-2.65,-6.1),
 arrowprops={'arrowstyle':'->','color':'#444444'},fontsize=10)
c.set(xlabel=r'Imaginary observation coordinate $\eta$, $z=i\eta$',ylabel='Normalized Fourier logarithm',
 title=r'Centers $R_j=2\pi j$; recession support function $|\eta|$',ylim=(-8.3,1.4))
c.grid(alpha=.18);c.legend(loc='upper right',fontsize=9)
fig.suptitle('Three singular corners retain the hull; the profile constant records decay',fontsize=16)
save(fig,'triangular-corners-and-singular-hull')
geometry=dict(schema='original-singular-hull-geometry/v1',fourier_convention='F_u(z)=<u,exp(-i x dot z)>;D=(1/i)partial',
 first_figure=dict(spatial_dimension=2,carrier='K={0}x[-1,1]',observation_point=[2,0],
  closest_point=[0,0],open_neighborhood_radius=.5,unit_separator=[1,0],uniform_gap=1.5,equal_spatial_axes=True,
  complex_contour_dimension=2,displayed_slice='xi2=0,zeta2=0; real xi1 in[-4,4]',R=2,m=4,
  contour_height='2log(2+xi1^2)',strip_upper_boundary='positive root of eta=4log(1+sqrt(xi1^2+eta^2))',
  shaded_set='Upper eta>=0 part of the actual implicit strip,not a bound using real frequency alone',
  root_solver='brentq on[1e-8,100];601 horizontal samples',full_proof_uses_all_real_frequency_coordinates=True,
  proof_locators=['Theorem1.1,sufficiency;equations3.1–3.8','Exercise5']),
 second_figure=dict(function='(1-abs(x))_+',singular_points=[-1,0,1],singular_hull=[-1,1],
  operator='D^2=-partial_x^2',point_mass_weights=[-1,2,-1],weights_are_distributional_coefficients=True,
  entire_transform='2(1-cos z)/z^2 with value1 at0',
  real_centers='R_j=2pi j',indices=indices,eta_range=[-3,3],
  exact_profile='[log4+2log(abs(sinh(eta logR/2)))-log(R^2+(eta logR)^2)]/logR',
  eta0='exact minus-infinite value excluded from finite curves',proper_limit='abs(eta)-2',
  recession='abs(eta)',proof_locators=['Theorems4.1,5.1','Worked example4;equations9.2–9.3','Exercise10']),
 human_sources=['Terence Tao,Some connections with the Fourier transform,2021',
  'Lars Hormander,The Analysis of Linear Partial Differential Operators I and II'],
 authorship='GPT-6.1 Sol(OpenAI),Ultra;original CC0 1.0')
(OUT/'geometry.json').write_text(json.dumps(geometry,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print(json.dumps(dict(figures=2,formats=['PNG','SVG'],exact_geometry=True)))
