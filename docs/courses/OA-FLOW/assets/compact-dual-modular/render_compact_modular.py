"""Original CC0-1.0 mathematical figure. Reproduce using --output-dir."""
from pathlib import Path
from fractions import Fraction
import argparse,json
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

HERE=Path(__file__).resolve().parent
p=argparse.ArgumentParser();p.add_argument('--output-dir',type=Path,default=HERE/'assets')
args=p.parse_args();args.output_dir.mkdir(parents=True,exist_ok=True)
plt.rcParams.update({'font.family':'DejaVu Sans','font.size':14,
                     'svg.hashsalt':'compact-dual-modular-20261004',
                     'axes.titlesize':18,'axes.labelsize':15})
INK='#183449';BLUE='#236c9c';TEAL='#138477';GOLD='#bb7b20';GRAY='#75848a'
fig=plt.figure(figsize=(14,8.5),dpi=200,facecolor='white')
fig.suptitle('The modular generator and the exact trace normalization',
             fontsize=21,color=INK,y=.98)
fig.text(.5,.905,r'Two exact examples; $\kappa=\log 2$, $P=2\pi/\log 2$, $\beta(e_n)=e_{n-1}$',
         ha='center',fontsize=15,color=INK)
grid=fig.add_gridspec(1,2,left=.075,right=.96,bottom=.33,top=.78,wspace=.28)
ax=fig.add_subplot(grid[0,0]);ax.set_title('A. Matrix coefficient: the exact operator orbit',loc='left',pad=18,color=INK)
phase=np.linspace(0,-2*np.pi,600)
ax.plot(np.cos(phase),np.sin(phase),color=BLUE,lw=2)
ax.axhline(0,color=GRAY,lw=.8,alpha=.4);ax.axvline(0,color=GRAY,lw=.8,alpha=.4)
quarter=[(0,1,0),(1,-0,-1),(2,-1,0),(3,0,1)]
for j,x,y in quarter:ax.scatter([x],[y],s=55,color=BLUE,zorder=3)
ax.annotate(r'$t/P=0,1$',xy=(1,0),xytext=(1.10,.17),fontsize=15,color=INK)
ax.annotate(r'$t/P=\frac{1}{4}$',xy=(0,-1),xytext=(.11,-1.27),fontsize=15,color=INK)
ax.annotate(r'$t/P=\frac{1}{2}$',xy=(-1,0),xytext=(-1.57,-.30),fontsize=15,color=INK)
ax.annotate(r'$t/P=\frac{3}{4}$',xy=(0,1),xytext=(-.05,1.18),fontsize=15,color=INK)
for start,end in [(-.15,-.40),(-1.75,-2.00),(-3.30,-3.55),(-4.9,-5.15)]:
 ax.annotate('',xy=(np.cos(end),np.sin(end)),xytext=(np.cos(start),np.sin(start)),
             arrowprops={'arrowstyle':'->','color':TEAL,'lw':2.5,'connectionstyle':'arc3,rad=-.1'})
ax.set_aspect('equal');ax.set_xlim(-1.65,1.72);ax.set_ylim(-1.42,1.44)
ax.set_xticks([-1,0,1]);ax.set_yticks([-1,0,1]);ax.set_xlabel('Real part');ax.set_ylabel('Imaginary part')
ax.text(0,0,r'$e^{-i\kappa t}$',ha='center',va='center',fontsize=21,color=INK,
        bbox={'fc':'white','ec':'none','alpha':.95})
ax.text(.5,-.22,r'$M=M_2(\mathbb{C}),\ d=\mathrm{diag}(1,2),\ \varphi(a)=\mathrm{Tr}(da)$',
        transform=ax.transAxes,ha='center',fontsize=13.5,color=INK)
ax.text(.5,-.32,r'$\sigma_t^\omega(\Pi(E_{12}))=e^{-i\kappa t}\Pi(E_{12})$; $\ell(s)$ is fixed.  CD33–34',
        transform=ax.transAxes,ha='center',fontsize=13,color=INK)

ax=fig.add_subplot(grid[0,1]);ax.set_title('B. Scalar example: the masses fix the scale',loc='left',pad=18,color=INK)
ns=list(range(-3,4));masses=[Fraction(2)**n for n in ns];shifted=[x/2 for x in masses]
ax.plot(ns,[float(x) for x in masses],'o-',lw=2,ms=7,color=BLUE,label=r'$\tau(e_n)=2^n$')
ax.plot(ns,[float(x) for x in shifted],'s--',lw=2,ms=6,color=TEAL,label=r'$\tau(\beta e_n)=2^{n-1}$')
ax.plot(ns,[1]*len(ns),':',lw=2.2,color=GOLD,label=r'$\omega(e_n)=1$')
ax.set_yscale('log',base=2);ax.set_xticks(ns);ax.set_xlabel('Fourier index n');ax.set_ylabel('Exact trace mass')
ax.set_yticks([1/16,1/4,1,4,8]);ax.set_yticklabels(['1/16','1/4','1','4','8'])
ax.grid(True,alpha=.18);ax.legend(loc='upper left',fontsize=12,framealpha=.96)
ax.text(.5,-.22,r'$M=\mathbb{C},\ B=\ell^\infty(\mathbb{Z}),\ \omega(b)=\sum_n b_n,\ \tau(b)=\sum_n2^n b_n$',
        transform=ax.transAxes,ha='center',fontsize=13.5,color=INK)
ax.text(.5,-.32,r'$\tau\circ\beta=\frac{1}{2}\tau$ on the entire positive cone.  CD35–36',
        transform=ax.transAxes,ha='center',fontsize=13,color=INK)

fig.text(.5,.115,r'Canonical GNS: $\Delta_\omega^{it}=\pi_\omega(\ell(t))J_\omega\pi_\omega(\ell(t))J_\omega$ on all $H_\omega$.  CD27',
         ha='center',fontsize=17,color=INK)
fig.text(.5,.066,'In the scalar example, both modular groups are trivial and canonical Δω = I; the regular clock H₀ is unbounded.',
         ha='center',fontsize=12.5,color=INK)
fig.text(.5,.028,'Discrete mass samples are exact; connecting segments are guides. Given periods do not supply a type classification.',
         ha='center',fontsize=12,color=INK)
fig.savefig(args.output_dir/'compact-dual-modular.png',dpi=200,
            metadata={'Software':'CC0 original matplotlib source 2026-10-04'})
fig.savefig(args.output_dir/'compact-dual-modular.svg',
            metadata={'Date':None,'Creator':'CC0 original matplotlib source 2026-10-04'})
plt.close(fig)
data={'scope':'Two distinct exact examples, neither a type-III classification.',
      'kappa':'log(2)','P':'2*pi/log(2)','lambda':'1/2',
      'matrix_example':{'M':'M2(C)','d':[1,2],'weight':'Tr(d a)',
                        'orbit':'sigma_t^omega(Pi(E12))=exp(-i*kappa*t)Pi(E12)',
                        'quarter_period_samples':[{'t_over_P':str(Fraction(j,4)),
                          'phase_real':x,'phase_imag':y} for j,x,y in quarter],
                        'not_a_GNS_vector_claim':True},
      'scalar_example':{'M':'C','B':'l-infinity(Z)','beta_b_n':'b_(n+1)',
                        'indices':ns,'tau_e_n_rational':[str(x) for x in masses],
                        'tau_beta_e_n_rational':[str(x) for x in shifted],
                        'omega_e_n':[1]*len(ns),
                        'full_cone_scale':'tau beta = tau/2, including infinity',
                        'canonical_Delta':'I','regular_H0_n':'2^(-n)'},
      'no_finite_window_limit_inference':True,'proof_locators':['CD27','CD33–CD36'],
      'licence':'CC0-1.0 to extent of rights held'}
(args.output_dir/'compact-dual-modular-data.json').write_text(json.dumps(data,indent=2)+'\n',encoding='utf-8')
print('Rendered original PNG/SVG and exact data in',args.output_dir)
