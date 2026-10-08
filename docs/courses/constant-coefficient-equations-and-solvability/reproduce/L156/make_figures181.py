"""Exact Levi signs and holomorphic pullback coefficients for the chapter notes."""
from pathlib import Path
import json
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
HERE=Path(__file__).resolve().parent;OUT=HERE/'figures';OUT.mkdir(exist_ok=True)
plt.rcParams.update({'font.family':'DejaVu Sans','font.size':11,'axes.titlesize':13,
 'svg.hashsalt':'AN02-chapter15-notes-181','savefig.facecolor':'white'})
def save(fig,name):
 fig.savefig(OUT/(name+'.png'),dpi=180,bbox_inches='tight')
 fig.savefig(OUT/(name+'.svg'),bbox_inches='tight',metadata={'Date':None})
 plt.close(fig)

eta=np.linspace(.1,4,700);q=np.linspace(.02,4,700);t=4096.;a=2.
fig,ax=plt.subplots(1,2,figsize=(13.4,5.7),layout='constrained')
ax[0].plot(eta,-1/(eta*(1+eta)**2),lw=2.4,color='#ad542c')
ax[0].axhline(0,color='#333333',lw=1)
ax[0].set(xlabel=r'Imaginary coordinate $\eta>0$, real coordinate $\xi=0$',
 ylabel='Actual Levi coefficient (negative)',
 title=r'Naive weight: $R|\eta|-4\log(1+|z|)$')
ratio=1/(1+q*q)
strict=(1+q*q)**(-.75)/4*(ratio**.75+.25-.75*ratio)-a/np.sqrt(t)*(1+q*q)**(-2)
bound=(1+q*q)**(-.75)/32
ax[1].plot(q,strict,lw=2.4,color='#176b91',label='Exact strict-seed coefficient')
ax[1].plot(q,bound,lw=2,ls='--',color='#534594',label='Proved positive lower bound')
ax[1].set(xlabel=r'Scaled imaginary coordinate $q=\eta/t>0$, $\xi=0$',
 ylabel=r'Levi coefficient multiplied by $t^{3/2}$',
 title=r'Strict seed: $t=4096$, $a=2$, $\sqrt{t}=32a$')
ax[1].legend(fontsize=10)
for axis in ax:axis.grid(alpha=.2)
fig.suptitle('The logarithmic decay needs curvature away from the real axis',fontsize=16)
save(fig,'negative-naive-and-positive-strict-curvature')

r=np.linspace(0,1.5,700);epsilon=.4
fig,ax=plt.subplots(1,2,figsize=(13.4,5.7),layout='constrained')
ax[0].plot(r,r*r,lw=2.4,color='#176b91',label=r'Target radius $|h(z)|=r^2$')
ax[0].plot(r,2*r,lw=2.1,ls='--',color='#ad542c',label=r'Derivative norm $|h^\prime(z)|=2r$')
ax[0].set(xlabel=r'Source radius $r=|z|$',ylabel='Exact radius or derivative norm',
 title=r'Holomorphic map $h(z)=z^2$')
ax[0].legend(loc='upper left',fontsize=10)
ax[1].axvspan(epsilon,1.5,color='#176b91',alpha=.08)
ax[1].plot(r,np.ones_like(r),lw=2,color='#534594',label=r'Target Levi coefficient: $1$')
ax[1].plot(r,4*r*r,lw=2.4,color='#176b91',label=r'Pullback Levi coefficient: $4r^2$')
ax[1].plot(r[r>=epsilon],np.full(np.count_nonzero(r>=epsilon),4*epsilon**2),
 lw=1.8,ls='--',color='#ad542c',label=r'On $r\geq0.4$: lower bound $0.64$')
ax[1].plot(0,0,'o',color='#176b91')
ax[1].annotate('Critical point: strictness lost',(0,0),xytext=(.08,3.2),
 textcoords='data',fontsize=10,arrowprops={'arrowstyle':'->','color':'#444444'})
ax[1].set(xlabel=r'Source radius $r=|z|$',ylabel='Exact Levi coefficient',
 title=r'$\varphi(w)=|w|^2$, pullback $\varphi(h(z))=|z|^4$')
ax[1].legend(loc='upper left',fontsize=9)
for axis in ax:axis.grid(alpha=.2)
fig.suptitle('Coordinate covariance preserves positivity; critical maps can lose strictness',fontsize=16)
save(fig,'holomorphic-pullback-and-loss-of-strictness')
geometry=dict(schema='AN02-L156-geometry181/v1',
 coordinate_conventions='z=xi+i*eta; Euclidean complex coordinates; Levi coefficient isDelta/4 in dimension1; Hermitian forms use w*Lw.',
 first_figure=dict(proof_locators=['formalNW1-NW3,NW5-NW8','learnerexamples1-2,L156.1-L156.6'],
  naive_carrier='K=[-R,R],R>0; displayed smooth half-plane has zero support-term Levi',
  naive_parameters=dict(kappa=4,xi=0,eta_interval=[.1,4],samples=700),
  naive_coefficient='-1/[eta*(1+eta)^2]',
  strict_parameters=dict(a=2,t=4096,xi=0,q_interval=[.02,4],samples=700),
  strict_carriers='K=[-1/128,1/128],L=[-3/128,3/128],X=(-1/32,1/32)',
  strict_display='q=eta/t; plotted values are t^(3/2) times the actual Levi coefficient; support function is affine at every displayed point',
  strict_coefficient='s^(-3/4)/4*(q0^(3/4)+1/4-3*q0/4)-a*t^2/(t^2+xi^2+eta^2)^2; s=t^2+eta^2,q0=t^2/s',
  bound='s^(-3/4)/32; no ordinary smooth coefficient claimed on the nonsmooth support ridge'),
 second_figure=dict(proof_locators=['formalNW10-NW11','learnerexample3,L156.7,solutions8-9'],
  map='h(z)=z^2',target='varphi(w)=|w|^2',pullback='|z|^4',
  radius_interval=[0,1.5],samples=700,
  target_radius='r^2',derivative_norm='2r',
  target_Levi=1,pullback_Levi='4r^2',critical_point='z=0',
  displayed_compact_annulus=dict(epsilon=.4,outer_radius=1.5,strict_lower_bound=.64),
  qualifications='Radial values in actual complex coordinates; chosen inverse charts are local away from0. No global chart, systems theorem or global manifold estimate is depicted.'),
 authorship='GPT-6.1 Sol (OpenAI), Ultra; original exact scientific plots; CC0 1.0',
 human_source='Lars Hormander, The Analysis of Linear Partial Differential Operators II, Notes on printedp300-301.',
 Blender_assessment='Exact one-dimensional curvature profiles and coordinate radii fully display these findings. A3D embedding would add no mathematical information.',
 protected_source_body_or_images_used=False)
(OUT/'geometry.json').write_text(json.dumps(geometry,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print(json.dumps({'figure_pairs':2,'geometry':str(OUT/'geometry.json')}))
