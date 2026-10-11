"""Reproducible exact signed scale-energy balance, with full viscosity."""
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch
OUT=Path(__file__).resolve().parent
fig=plt.figure(figsize=(16,10),facecolor='white');ax=fig.add_axes([0,0,1,1]);ax.set_axis_off()
teal='#126471';orange='#b85b19'
def txt(x,y,t,size=18,**kw):ax.text(x,y,t,ha='center',va='center',fontsize=size,**kw)
txt(.5,.95,'The complete signed energy current between original scales',25)
txt(.5,.892,r'$q=1+\epsilon_0,\quad 0<\epsilon_0\leq1/1024,\quad \nu\geq0,\quad 0\leq t<T_*$',17)
for x,lab in [(.055,'n-1'),(.39,'n'),(.725,'n+1')]:
    ax.add_patch(FancyBboxPatch((x,.61),.22,.19,boxstyle='round,pad=0.01',facecolor='#f0f6f7',edgecolor=teal,lw=2))
    txt(x+.11,.75,r'$e_{'+lab+r'}=\sum_i E_{i,'+lab+'}$',22,color=teal)
    txt(x+.11,.672,r'$\nu d_{'+lab+r'}=\nu\sum_i\|\nabla u_{i,'+lab+r'}\|_2^2$',15)
for x1,x2,label in [(.278,.38,r'$\mathcal{J}_{n-1/2}$'),(.613,.715,r'$\mathcal{J}_{n+1/2}$')]:
    ax.annotate('',xy=(x2,.712),xytext=(x1,.712),arrowprops=dict(arrowstyle='-|>',lw=2,color=orange))
    txt((x1+x2)/2,.757,label,19,color=orange)
txt(.5,.548,r"$e_n'=-\nu d_n+\mathcal{J}_{n-1/2}-\mathcal{J}_{n+1/2}$",25)
txt(.5,.474,r'$\mathcal{J}_{n+1/2}=q^{5n/2}\sum_{i_1,i_2,i_3=1}^m'
                  r'\alpha_{i_1,i_2,i_3,0,0,1}X_{i_1,n}X_{i_2,n}X_{i_3,n+1}$',21)
txt(.5,.403,'Arrow direction declares the sign convention. The original currents may have either sign.',17)
txt(.5,.334,r"$\mathcal{E}_\chi=\sum_n\chi_ne_n,\qquad"
                  r"\mathcal{E}_\chi'=-\nu\sum_n\chi_nd_n"
                  r"+\sum_n(\chi_{n+1}-\chi_n)\mathcal{J}_{n+1/2}$",22)
txt(.5,.254,r'$\chi\in\ell^\infty(\mathbb{Z};\mathbb{R}),\qquad'
                  r'\chi_n=1_{\{n\leq N\}}:\quad'
                  r'\dfrac{d}{dt}\sum_{n\leq N}e_n=-\nu\sum_{n\leq N}d_n-\mathcal{J}_{N+1/2}$',20)
txt(.5,.168,'The four original shifts and all six cancellation permutations determine these exact balances.',16)
txt(.5,.115,'VD16–VD20 and Exercise 4, EX17–EX21, prove convergence, every boundary term and the full viscosity term.',13)
txt(.5,.072,'Human comparison: Terence Tao, arXiv:1402.0290v3, original navier-blowup.tex840–987.',12)
txt(.5,.035,'The boxes group actual frequency-band energies; their widths are schematic. No singular trajectory is asserted.',12)
for ext in ['png','svg']:fig.savefig(OUT/f'original-cascade-energy-current.{ext}',dpi=160)
plt.close(fig)
