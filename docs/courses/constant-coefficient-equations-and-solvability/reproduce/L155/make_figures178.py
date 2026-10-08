"""Exact scientific plots for arbitrary-order distribution representations."""
from pathlib import Path
import json
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

HERE=Path(__file__).resolve().parent;OUT=HERE/'figures';OUT.mkdir(exist_ok=True)
plt.rcParams.update({'font.family':'DejaVu Sans','font.size':11,'axes.titlesize':13,
 'svg.hashsalt':'AN02-distribution-representations-178','savefig.facecolor':'white'})
def save(fig,name):
 fig.savefig(OUT/(name+'.png'),dpi=180,bbox_inches='tight')
 fig.savefig(OUT/(name+'.svg'),bbox_inches='tight',metadata={'Date':None})
 plt.close(fig)

q=np.linspace(-5,5,900);eta=np.linspace(-5,5,900)
fig,ax=plt.subplots(1,2,figsize=(13.4,5.7),layout='constrained')
for r,color in [(0,'#176b91'),(1,'#ad542c'),(3,'#534594')]:
 ax[0].plot(q,q**(2*r)/(1+q*q)**4,lw=2.2,color=color,label=rf'$r={r}$')
ax[0].set(xlabel=r'Scaled real frequency $q=\xi/t$',ylabel='Normalized weighted energy',
 title=r'Exact point-mass energy: $q^{2r}(1+q^2)^{-4}$')
ax[0].legend(title='Order of '+r'$D^r\delta_0$',fontsize=10)
for sigma,color in [(.5,'#176b91'),(1,'#ad542c'),(2,'#534594')]:
 ax[1].plot(eta,np.exp(-(eta/sigma)**2)/(np.sqrt(np.pi)*sigma),
  lw=2.2,color=color,label=rf'$\sigma={sigma}$')
ax[1].set(xlabel=r'Imaginary frequency $\eta$',ylabel=r'Normalized profile $g_\sigma(\eta)$',
 title='Different complex densities, the same distribution')
ax[1].legend(title=r'$\int g_\sigma\,d\eta=1$',fontsize=10)
for a in ax:a.grid(alpha=.2)
fig.suptitle(r'$U_{r,\sigma}(z)=z^r g_\sigma(\operatorname{Im}z)/(2\pi)$ represents $D^r\delta_0$',fontsize=16)
save(fig,'point-mass-complex-density-and-weighted-energy')

x=np.linspace(-1,1,800)
fig,ax=plt.subplots(1,2,figsize=(13.4,5.7),layout='constrained')
for r,color in [(0,'#176b91'),(1,'#ad542c'),(2,'#534594')]:
 ax[0].plot(x,x**r*np.exp(-x),lw=2.2,color=color,label=rf'$x^{r}e^{{-x}}$')
ax[0].set(xlabel=r'Physical coordinate $x$',ylabel='Actual solution kernel',
 title=r'$P(z)=(z-i)^3$: three necessary amplitudes')
ax[0].legend(title=r'Characteristic point $i$; counting measure',fontsize=9)
orders=np.arange(1,8);positions=1-2.**(-orders)
ax[1].scatter(positions,orders,s=58,c='#176b91',zorder=3)
for l,a in zip(orders,positions):
 ax[1].annotate(rf'$l={l}$',(a,l),xytext=(-10,8),textcoords='offset points',ha='right',fontsize=10)
ax[1].axvline(1,color='#ad542c',ls='--',lw=1.8)
ax[1].text(.988,.92,r'$x_2=1$ is outside $X$',rotation=90,va='bottom',ha='right',fontsize=10)
ax[1].set(xlabel=r'Point-mass position $a_l=1-2^{-l}$',ylabel='Local ordinary derivative order',
 title='First seven terms of a locally finite infinite distribution',
 xlim=(.45,1.025),ylim=(.4,8.4))
ax[1].text(.02,.97,r'$u=1_{x_1}\otimes\sum_{l\geq1}2^{-l}\delta_{a_l}^{(l)}$',
 transform=ax[1].transAxes,va='top',fontsize=12)
for a in ax:a.grid(alpha=.2)
fig.suptitle('Multiplicity and increasing local order remain in the full surface theorem',fontsize=16)
save(fig,'repeated-root-jets-and-increasing-local-orders')

geometry={
 'schema':'AN02-L155-geometry178/v1','coordinates_and_metric':'Euclidean complex frequency space; z=xi+i*eta, real volume dxi*deta. Dot products in exponentials are bilinear.',
 'first_figure':{
  'proof_locators':['learner worked example2, equationsL155.5-L155.8','solutions7-8','formalAR1'],
  'actual_density':'U_(r,sigma)(z)=z^r*exp(-eta^2/sigma^2)/(2*pi^(3/2)*sigma)',
  'density_normalization':'g_sigma integrates to1; actual test integral represents D^r delta0, D=-i*d/dx.',
  'explicit_weight':'t=4096,a=2,R=1/64; phi=p_t(eta)-a*log(t^2+xi^2+eta^2)',
  'left_slice':'eta=0, q=xi/t; weighted energy divided by g_sigma(0)^2/(4*pi^2)*t^(2r-8) is q^(2r)/(1+q^2)^4',
  'left_orders':[0,1,3],'q_samples':'900 samples over[-5,5]; exact function plotted',
  'right_profiles':[.5,1,2],'eta_samples':'900 samples over[-5,5]; entire Gaussian profiles exist beyond plotted interval',
  'full_surface_example':'For n=2,P=z1,N={z1=0},parameter z2=xi2+i*eta2, induced dS=dxi2*deta2. U=z2^3*g1(eta2)/(2*pi), producing1_x1 tensor D2^3 delta0.'},
 'second_figure':{
  'proof_locators':['learner examples1,4, equationsL155.3-L155.4,L155.11','formalAR3'],
  'left_domain':'Displayed x in[-1,1]; all three kernels solve(D-i)^3 u=0 globally.',
  'left_characteristic_measure':'N={i}, counting measure, tau=1, amplitudes a=0,1,2',
  'right_domain':'X=(-1,1)^2; only x2 coordinate and derivative order shown.',
  'right_objects':[{'l':int(l),'a_l':float(a),'coefficient':float(2.**(-l))} for l,a in zip(orders,positions)],
  'infinite_scope':'a_l=1-2^(-l), l>=1, locally finite on X; plotted seven terms are numerical samples, not the complete distribution. Boundary1 is outside X.',
  'homogeneous_operator':'P(z)=z1, P(D)=D1, all local orders preserved.'},
 'authorship':'GPT-6.1 Sol (OpenAI), Ultra; original exact scientific plots; CC0 1.0',
 'human_source':'Lars Hormander, The Analysis of Linear Partial Differential Operators II, two unnumbered representation exercises on printedp300.',
 'Blender_assessment':'Exact scalar energy profiles, physical one-dimensional kernels and order-location coordinates are fully described by these plots. A3D embedding would add no mathematical information.',
 'source_body_or_source_images_used':False}
(OUT/'geometry.json').write_text(json.dumps(geometry,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print(json.dumps({'figure_pairs':2,'geometry':str(OUT/'geometry.json')}))
