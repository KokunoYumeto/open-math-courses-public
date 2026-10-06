"""Original CC0-1.0 figure. Run with --output-dir to reproduce elsewhere."""
from pathlib import Path
from fractions import Fraction
import argparse
import json
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch

HERE=Path(__file__).resolve().parent
parser=argparse.ArgumentParser()
parser.add_argument('--output-dir',type=Path,default=HERE/'assets')
args=parser.parse_args()
args.output_dir.mkdir(parents=True,exist_ok=True)
plt.rcParams.update({'font.family':'DejaVu Sans','font.size':14,
                     'svg.hashsalt':'compact-counting-average-20261004',
                     'axes.titlesize':19,'axes.labelsize':15})
INK='#183449'; BLUE='#236c9c'; TEAL='#138477'; GOLD='#c38324'; LIGHT='#ecf4f8'
fig=plt.figure(figsize=(14,9),dpi=200,facecolor='white')
grid=fig.add_gridspec(2,2,left=.055,right=.965,bottom=.16,top=.83,wspace=.17,hspace=.35)
fig.suptitle('Compact counting: Fourier shift, fixed algebra, finite values',
             fontsize=21,color=INK,y=.975)
fig.text(.5,.905,r'Given $\sigma_P^\varphi=\mathrm{id}$; $\kappa=2\pi/P$; normalized Haar measure $ds/P$',
         ha='center',fontsize=16,color=INK)

ax=fig.add_subplot(grid[0,0]); ax.set_axis_off(); ax.set_xlim(-3.7,3.7); ax.set_ylim(-.1,3.1)
ax.set_title('A. Negative character shifts left',loc='left',color=INK,pad=10)
ax.text(0,2.65,r'$f_n(s)=e^{i\kappa ns},\quad \beta=\mathrm{Ad}(W^*),\quad WI_n=I_{n+1}$',
        ha='center',fontsize=14,color=INK)
for n in range(-3,4):
 ax.add_patch(FancyBboxPatch((n-.31,1.42),.62,.55,boxstyle='round,pad=.03',
                            facecolor=LIGHT,edgecolor=BLUE,linewidth=1.5))
 ax.text(n,1.69,r'$e_{%d}$'%n,ha='center',va='center',fontsize=18,color=INK)
for n in range(-2,4):
 ax.annotate('',xy=(n-1,1.03),xytext=(n,1.03),
             arrowprops={'arrowstyle':'->','color':TEAL,'lw':2.2})
ax.text(0,.56,r'$\beta(e_n)=e_{n-1}\quad\text{for every }n\in\mathbb{Z}$',ha='center',fontsize=18,color=TEAL)
ax.text(0,.05,'Finite window only; no wrap-around.  CC15–CC18',ha='center',fontsize=12,color=INK)

ax=fig.add_subplot(grid[0,1]); ax.set_axis_off(); ax.set_xlim(0,1); ax.set_ylim(0,1)
ax.set_title('B. The full counting sum',loc='left',color=INK,pad=10)
rows=[(.78,r'$e_0$',r'$E(e_0)=\sum_{k\in\mathbb{Z}}e_{-k}=I$'),
      (.49,r'$q_J=\sum_{n=-2}^{2}e_n$',r'$E(q_J)=5I$'),
      (.20,r'$I$',r'$E(I)=\infty I$')]
for y,left,right in rows:
 ax.text(.01,y,left,ha='left',va='center',fontsize=17,color=INK)
 ax.annotate('',xy=(.48,y),xytext=(.36,y),arrowprops={'arrowstyle':'->','color':BLUE,'lw':2})
 ax.text(.51,y,right,ha='left',va='center',fontsize=16,color=TEAL if y>.25 else GOLD)
ax.text(.5,.00,'All integer translates are summed, including infinite values.  CC22–CC32',
        ha='center',fontsize=11.5,color=INK)

ax=fig.add_subplot(grid[1,0]); ax.set_axis_off(); ax.set_xlim(0,1); ax.set_ylim(0,1)
ax.set_title('C. Why the fixed algebra is exactly Π(M)',loc='left',color=INK,pad=10)
ax.text(.5,.92,r'$X\in B,\ \beta(X)=X;\quad Y=TXT^*$',ha='center',fontsize=17,color=INK)
# A displayed finite Fourier corner, with operator entries on arbitrary H.
for i in range(3):
 for j in range(3):
  x=.02+j*.12; y=.40+(2-i)*.12
  ax.add_patch(FancyBboxPatch((x,y),.105,.105,boxstyle='round,pad=.005',
                            facecolor=LIGHT if i==j else 'white',edgecolor='#9aafb9'))
  ax.text(x+.0525,y+.0525,'a' if i==j else '0',ha='center',va='center',fontsize=18,color=BLUE)
ax.text(.20,.31,'Sample Fourier corner',ha='center',fontsize=12,color=INK)
ax.text(.47,.72,r'$[Y,R_t]=0\ \Rightarrow\ Y_{nj}=0\ (n\ne j)$',fontsize=13.5,color=INK)
ax.text(.47,.54,r'$[Y,W]=0\ \Rightarrow\ Y_{nn}=a\ \text{for all }n$',fontsize=13.5,color=INK)
ax.text(.47,.36,r'$[X,M^{\prime}]=0\ \Rightarrow\ a\in M$',fontsize=13.5,color=INK)
ax.text(.5,.12,r'$Y=a\otimes I\quad\Longrightarrow\quad X=\Pi(a)$',ha='center',fontsize=19,color=TEAL)
ax.text(.5,.00,'Complete Fourier blocks and continuous commutator test.  CC19–CC21',
        ha='center',fontsize=11.5,color=INK)

ax=fig.add_subplot(grid[1,1]); ax.set_title('D. Exact clock sample: κ = log 2',loc='left',color=INK,pad=10)
indices=list(range(-3,4))
values=[Fraction(2)**(-n) for n in indices]
shifted=[v/2 for v in values]
ax.plot(indices,[float(v) for v in values],'o-',color=BLUE,lw=2,ms=7,label=r'$H_0:e_n\mapsto 2^{-n}$')
ax.plot(indices,[float(v) for v in shifted],'s--',color=TEAL,lw=2,ms=6,label=r'$\beta(H_0):e_n\mapsto 2^{-(n+1)}$')
ax.set_yscale('log',base=2); ax.set_xticks(indices); ax.set_xlabel('Fourier index n')
ax.set_yticks([1/16,1/4,1,4,8]); ax.set_yticklabels(['1/16','1/4','1','4','8'])
ax.set_ylabel('Spectral multiplier'); ax.grid(True,alpha=.18)
ax.legend(loc='upper right',fontsize=12,framealpha=.95)
ax.text(.02,.055,r'$H_0^{it}=\ell(t),\quad\beta(H_0)=\frac{1}{2}H_0$',
        transform=ax.transAxes,fontsize=17,color=INK,
        bbox={'boxstyle':'round,pad=.3','fc':'white','ec':'none','alpha':.95})
ax.text(.5,-.285,'Discrete samples; connecting segments are guides.  CC35–CC38',
        transform=ax.transAxes,ha='center',fontsize=11.5,color=INK)
fig.text(.5,.027,'The spectral clock alone does not identify the modular group of ω.  No descent or classification is asserted.',
         ha='center',fontsize=12.5,color=INK)

fig.savefig(args.output_dir/'compact-counting-average.png',dpi=200,
            metadata={'Software':'CC0 original matplotlib source 2026-10-04'})
fig.savefig(args.output_dir/'compact-counting-average.svg',
            metadata={'Date':None,'Creator':'CC0 original matplotlib source 2026-10-04'})
plt.close(fig)
data={'scope':'Exact finite samples of the complete integer-indexed theorem, not finite cyclic projections.',
      'haar':'ds/P, total mass one','fourier_basis':'exp(+i*kappa*n*s)',
      'negative_generator':'beta=Ad(W*)','projection_shift':'beta(e_n)=e_(n-1)',
      'counting':'sum over all finite subsets of Z; E(e_n)=I; E(q_J)=|J|I; E(I)=infinity I when B is nonzero',
      'sample_J':list(range(-2,3)),'sample_cardinality':5,
      'clock_sample':{'kappa':'log(2)','P':'2*pi/log(2)','lambda':'1/2',
                      'indices':indices,'H0_rational':[str(v) for v in values],
                      'beta_H0_rational':[str(v) for v in shifted]},
      'plot_segments':'visual guides between discrete samples; no interpolation theorem',
      'not_asserted':['sigma^omega=Ad(H0^it)','H0 affiliated with omega centralizer','classification','invariant-weight descent'],
      'proof_locators':['CC15–CC18','CC19–CC21','CC22–CC32','CC35–CC38']}
(args.output_dir/'compact-counting-average-data.json').write_text(json.dumps(data,indent=2)+'\n',encoding='utf-8')
print('Rendered PNG, SVG and exact rational data in',args.output_dir)
