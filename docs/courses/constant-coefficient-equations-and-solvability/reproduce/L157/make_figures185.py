"""Exact Fourier profiles and common-frequency geometry; original CC0 figures."""
from pathlib import Path
import json
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import Wedge
HERE=Path(__file__).resolve().parent;OUT=HERE/'figures';OUT.mkdir(exist_ok=True)
plt.rcParams.update({'font.family':'DejaVu Sans','font.size':11,'axes.titlesize':13,
 'svg.hashsalt':'joint-logarithmic-frequency-185','savefig.facecolor':'white'})
def save(fig,name):
 fig.savefig(OUT/(name+'.png'),dpi=180,bbox_inches='tight')
 fig.savefig(OUT/(name+'.svg'),bbox_inches='tight',metadata={'Date':None})
 plt.close(fig)
eta=np.linspace(-2,2,1001);indices=[1,10,100];colors=['#226c9a','#b36829','#7356a5']
fig,axes=plt.subplots(1,2,figsize=(13.8,5.9),layout='constrained')
for j,c in zip(indices,colors):
 R=(2*j+1)*np.pi;s=np.log(R);values=np.full(eta.shape,np.nan);nz=eta!=0
 values[nz]=np.log(np.abs(np.expm1(eta[nz]*s)))/s
 axes[0].plot(eta,values,color=c,lw=1.9,label=f'Exact finite profile, j={j}')
 derivative=2+np.log1p((eta*s/R)**2)/s+eta/2
 axes[1].plot(eta,derivative,color=c,lw=1.9,label=f'Exact derivative profile, j={j}')
axes[0].plot(eta,np.maximum(eta,0),color='#222222',lw=2.6,ls='--',label=r'Proper limit $\max(\eta,0)$')
axes[0].plot(0,0,'o',color='#222222',ms=5)
axes[0].annotate(r'At $\eta=0$: $-\infty$'+'\n(no finite value)',xy=(0,-2.25),xytext=(-1.82,-1.30),
 fontsize=10,arrowprops={'arrowstyle':'->','color':'#444444'})
axes[0].set(xlabel=r'Imaginary coordinate $\eta$, observation $z=i\eta$',ylabel='Normalized Fourier logarithm',
 title=r'Two atoms: $\delta_0+\delta_1$, $R_j=(2j+1)\pi$',ylim=(-2.4,2.25))
axes[1].plot(eta,2+eta/2,color='#222222',lw=2.6,ls='--',label=r'Proper limit $2+\eta/2$')
axes[1].plot(eta,eta/2,color='#34725b',lw=2.5,label=r'Recession support function $\eta/2$')
axes[1].set(xlabel=r'Imaginary coordinate $\eta$, observation $z=i\eta$',ylabel='Profile or recession value',
 title=r'Derivative atom: $D^2\delta_{1/2}$',ylim=(-1.2,3.45))
for ax in axes:ax.grid(alpha=.2);ax.legend(loc='upper left',fontsize=8.9)
fig.suptitle('A local integral limit can remove zeros; recession removes constants',fontsize=16)
save(fig,'logarithmic-profiles-and-recession')

fig,axes=plt.subplots(1,2,figsize=(14.1,6.1),layout='constrained',gridspec_kw={'width_ratios':[1,1.25]})
ax=axes[0];blue='#226c9a';orange='#b36829'
for first,last,c in [(-45,45,blue),(45,135,orange),(135,225,blue),(225,315,orange)]:
 ax.add_patch(Wedge((0,0),1,first,last,color=c,alpha=.10))
 theta=np.linspace(np.deg2rad(first),np.deg2rad(last),181)
 ax.plot(np.cos(theta),np.sin(theta),color=c,lw=4)
for angle in [45,135,225,315]:
 t=np.deg2rad(angle);ax.plot(np.cos(t),np.sin(t),'D',color='#7356a5',ms=5)
ax.axhline(0,color='#888888',lw=.8);ax.axvline(0,color='#888888',lw=.8)
for x,y,label in [(1,0,'A'),(0,1,'B'),(2**-.5,2**-.5,'C')]:
 ax.annotate('',xy=(x,y),xytext=(0,0),arrowprops={'arrowstyle':'->','color':'#222222','lw':1.7})
 ax.text(1.12*x+.025,1.12*y+.01,label,fontsize=12)
ax.plot([],[],color=blue,lw=4,label=r'$|\xi_1|\geq R/\sqrt{2}$: first collapses')
ax.plot([],[],color=orange,lw=4,label=r'$|\xi_2|\geq R/\sqrt{2}$: second collapses')
ax.set_aspect('equal',adjustable='box');ax.set(xlim=(-1.32,1.4),ylim=(-1.28,1.35),
 xlabel=r'Normalized real frequency $\xi_1/R$',ylabel=r'Normalized real frequency $\xi_2/R$',
 title='Every direction has a large coordinate')
ax.legend(loc='lower center',bbox_to_anchor=(.5,-.30),fontsize=9,frameon=False)
axes[1].axis('off');axes[1].set_title('Three common routes and one forbidden pair',pad=22)
rows=[
 [r'A: $\xi=(R,0)$',r'$\varnothing$',r'$h_2=|\eta_2|$','Realized'],
 [r'B: $\xi=(0,R)$',r'$h_1=|\eta_1|$',r'$\varnothing$','Realized'],
 [r'C: $\xi=(R/\sqrt{2},R/\sqrt{2})$',r'$\varnothing$',r'$\varnothing$','Realized'],
 ['Separate proper choices',r'$h_1=|\eta_1|$',r'$h_2=|\eta_2|$','Forbidden together']]
table=axes[1].table(cellText=rows,colLabels=['Frequency route','First component','Second component','Joint status'],
 cellLoc='center',colWidths=[.43,.20,.20,.22],bbox=[0,.28,1,.55])
table.auto_set_font_size(False);table.set_fontsize(9.3)
for (r,c),cell in table.get_celld().items():
 cell.set_edgecolor('#c9ced4');cell.set_facecolor('#eef2f5' if r==0 else '#ffffff')
 if r==4:cell.set_facecolor('#fbebe4')
axes[1].text(.5,.16,r'$\varnothing$: collapsed profile, support function $-\infty$',
 ha='center',transform=axes[1].transAxes,fontsize=10)
axes[1].text(.5,.06,'These routes are explicit examples, not a classification\nof every possible proper component.',
 ha='center',transform=axes[1].transAxes,fontsize=10)
fig.suptitle('Crossed compact distributions need one common frequency sequence',fontsize=16)
save(fig,'common-frequencies-and-joint-limits')
geometry=dict(schema='original-joint-frequency-geometry/v1',fourier_convention='F_u(z)=<u,exp(-i x dot z)>; D=(1/i)partial',
 metric='Euclidean on real and complex spaces; observation integrals use 2n-dimensional Lebesgue measure',
 first_figure=dict(real_frequency_centers='R_j=(2j+1)pi',indices=indices,imaginary_coordinate_range=[-2,2],
  atom_profile='log(abs(expm1(eta*log(R))))/log(R)',zero_value_at_eta0='exactly minus infinity; not represented as a finite ordinate',
  proper_atom_limit='max(eta,0)',derivative_order=2,derivative_location=.5,
  derivative_profile='2+log(1+(eta*log(R)/R)^2)/log(R)+eta/2',derivative_limit='2+eta/2',recession='eta/2',
  proof_locators=['Theorem2.1','Worked example2, equation9.2','Worked example3, equation9.3']),
 second_figure=dict(normalized_real_frequency_circle_radius=1,equal_axis_scale=True,
  dominant_coordinate_threshold='1/sqrt(2)',first_profile_collapses_when='abs(xi1)>=R/sqrt(2)',
  second_profile_collapses_when='abs(xi2)>=R/sqrt(2)',intersection='four diagonal boundary directions',
  distributions='u1=phi(x1) tensor delta0(x2); u2=delta0(x1) tensor phi(x2)',
  bump='phi=exp(-1/(1-x^2)) on abs(x)<1, zero otherwise; exact support[-1,1]',
  realized_routes=['(R,0): empty,|eta2|','(0,R): |eta1|,empty','(R/sqrt2,R/sqrt2): empty,empty'],
  forbidden_joint_pair='|eta1|,|eta2|',not_a_classification_of_all_possible_proper_components=True,
  proof_locators=['Worked example4,equation9.4','Exercise7 and its complete solution']),
 sources=['Lars Hormander,The Analysis of Linear Partial Differential Operators II,1983;1990;2005',
  'Exact linked original PSH compactness,smooth complex decay and endpoint-limit proofs'],
 authorship='GPT-6.1 Sol (OpenAI), Ultra; original CC0 1.0 figures')
(OUT/'geometry.json').write_text(json.dumps(geometry,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print(json.dumps(dict(figures=2,formats=['PNG','SVG'],exact_geometry=True)))
