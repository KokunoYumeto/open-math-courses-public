"""Original CC0-1.0 exact integer Fourier/shear illustration."""
from pathlib import Path
import argparse,json
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
HERE=Path(__file__).resolve().parent
p=argparse.ArgumentParser();p.add_argument('--output-dir',type=Path,default=HERE/'assets')
args=p.parse_args();args.output_dir.mkdir(parents=True,exist_ok=True)
plt.rcParams.update({'font.family':'DejaVu Sans','font.size':14,'svg.hashsalt':'compact-vn-duality-20261004'})
INK='#183449';BLUE='#236c9c';PURPLE='#8f5291';GRAY='#788890'
fig=plt.figure(figsize=(15,9.5),dpi=200,facecolor='white')
fig.suptitle('The Fourier shear and the complete normal double dual',fontsize=23,color=INK,y=.98)
fig.text(.5,.91,r'$\Psi:L^2(\mathbb{T},\,\bigoplus_nH)\ \longrightarrow\ (\bigoplus_rH)\otimes\ell^2(\mathbb{Z})$; $r=n-k$, $dm=dt/(2\pi)$',
         ha='center',color=INK,fontsize=17)
gs=fig.add_gridspec(1,2,left=.08,right=.955,bottom=.40,top=.80,wspace=.28)
left=fig.add_subplot(gs[0,0]);right=fig.add_subplot(gs[0,1])
left.set_title('A. Regular and Fourier coordinates',loc='left',fontsize=18,pad=18,color=INK)
right.set_title('B. The same vectors after the integer shear',loc='left',fontsize=18,pad=18,color=INK)
points=[{'k':k,'n':n,'r':n-k} for k in range(-2,3) for n in range(-2,3)]
cmap=plt.get_cmap('viridis')
for q in points:
 color=cmap((q['r']+4)/8)
 left.scatter(q['k'],q['n'],s=65,color=color,edgecolors='white',linewidths=.8,zorder=3)
 right.scatter(q['k'],q['r'],s=65,color=color,edgecolors='white',linewidths=.8,zorder=3)
for ax in [left,right]:
 ax.set_xticks(range(-2,3));ax.grid(color=GRAY,alpha=.22)
 ax.set_xlabel(r'$k$ (circle Fourier index)',fontsize=15)
 ax.axhline(0,color=GRAY,alpha=.35,lw=1)
 ax.axvline(0,color=GRAY,alpha=.35,lw=1)
 ax.set_xlim(-2.7,2.7)
left.set_ylabel(r'$n$ (discrete regular index)',fontsize=15)
left.set_yticks(range(-2,3));left.set_ylim(-2.7,2.7)
right.set_ylabel(r'$r=n-k$ (multiplicity index)',fontsize=15)
right.set_yticks(range(-4,5));right.set_ylim(-4.7,4.7)
arrows=[
 ('U',(0,0),(1,1),(0,0),(1,0),BLUE),
 ('beta_1',(0,0),(-1,0),(0,0),(-1,1),PURPLE)]
for label,a,b,c,d,color in arrows:
 for ax,start,end in [(left,a,b),(right,c,d)]:
  ax.annotate('',xy=end,xytext=start,arrowprops={'arrowstyle':'->','color':color,'lw':3.2},zorder=5)
left.text(.9,1.48,r'$U=\Pi(u):\ (+1,+1)$',color=BLUE,fontsize=15,ha='center')
left.text(-.8,-.59,r'$\beta_1:\ (-1,0)$',color=PURPLE,fontsize=15,ha='center')
right.text(1.05,-.82,r'$I\otimes S:\ (+1,0)$',color=BLUE,fontsize=15,ha='center')
right.text(-.6,3.45,r'$S_r\otimes S^{-1}:\ (-1,+1)$',color=PURPLE,fontsize=15,ha='center')
fig.text(.5,.318,'Matching colors record r=n−k under Ψ. The 25 points are finite samples of the full integer lattice.',
         ha='center',color=INK,fontsize=15)
fig.text(.5,.265,r'Actual coefficient: $\Psi\Pi(\pi(a))\Psi^*=\sum_k\rho(\alpha^{-k}(a))\otimes E_{kk}$; field $\alpha^{-r-k}(a)$.  VD17',
         ha='center',color=INK,fontsize=16)
fig.text(.5,.209,r'Untwisted coefficient and full matrix units: $\Phi(\iota(a)f_{ij})=a\otimes E_{ij}$.  VD25–29',
         ha='center',color=INK,fontsize=16)
fig.text(.5,.154,r'Negative second dual: $\Phi\beta_m\Phi^{-1}=\alpha^m\overline{\otimes}\operatorname{Ad}(S^{-m})$.  VD30–32',
         ha='center',color=INK,fontsize=16)
fig.text(.5,.099,r'Given $\tau_A\alpha=c\tau_A$: $\mathcal{T}(X)=\sum_k\tau_A(X_{kk})$, $\mathcal{T}\Phi\beta_m\Phi^{-1}=c^m\mathcal{T}$.  VD33–39',
         ha='center',color=INK,fontsize=16)
fig.text(.5,.045,'Type II∞ additionally requires A to be a nonzero factor without minimal projections, with a given faithful n.s.f. trace.',
         ha='center',color=INK,fontsize=14)
stem=args.output_dir/'compact-von-neumann-duality'
fig.savefig(stem.with_suffix('.png'),dpi=200,metadata={'Software':'Original CC0-1.0 reproducible Fourier/shear figure'})
fig.savefig(stem.with_suffix('.svg'),metadata={'Date':None,'Creator':'Original CC0-1.0 reproducible Fourier/shear figure'})
plt.close(fig)
data={'scope':'Exact finite sample of the whole integer-coordinate bijection; coefficient Hilbert space arbitrary',
 'old_coordinate_order':['k','n'],'new_coordinate_order':['k','r'],'shear':'r=n-k','points':points,
 'operator_U':{'old_displacement':[1,1],'new_displacement':[1,0]},
 'negative_second_dual_beta_1':{'old_displacement':[-1,0],'new_displacement':[-1,1]},
 'negative_first_dual':'gamma_z(u)=conjugate(z)u','normalization':'dm=dt/(2*pi), dual counting measure',
 'all_integer_indices_not_finite_cyclic':True,'unbounded_weight_values_not_replaced_by_samples':True}
(stem.parent/(stem.name+'-data.json')).write_text(json.dumps(data,indent=2,sort_keys=True)+'\n',encoding='utf-8')
print('Rendered PNG/SVG/exact data in',args.output_dir)
