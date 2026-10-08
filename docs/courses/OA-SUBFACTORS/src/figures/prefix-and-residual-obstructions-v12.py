"""CC0. Reproduce exact proof diagrams CF.1--CF.9 and the spin trace obstruction.

Blocks are schematics, not trace-scaled shapes. The plotted polynomial has
m=2,n=2; its argument x is formal, whereas the actual trace parameter p is
transcendental in (1/2,2/3). No harmonic probability is numerically sampled.
"""
from pathlib import Path
import json
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch
import numpy as np

D=Path(__file__).resolve().parent
plt.rcParams.update({'svg.fonttype':'path','font.family':'DejaVu Sans'})
fig=plt.figure(figsize=(14.4,14.3),facecolor='#fafcff')
ax=fig.add_axes([0,.22,1,.78])
ax.set(xlim=(0,14.4),ylim=(0,11.2));ax.axis('off')
def box(x,y,w,h,title,lines,color='#edf5fc'):
    ax.add_patch(FancyBboxPatch((x,y),w,h,boxstyle='round,pad=.12',
                               edgecolor='#4b6b8f',facecolor=color,lw=1.2))
    ax.text(x+.18,y+h-.32,title,fontsize=13,weight='bold',color='#16365a')
    for j,(text,size) in enumerate(lines):
        ax.text(x+.18,y+h-.78-.43*j,text,fontsize=size,color='#173750')
def arrow(x,y,xx,yy,label=None):
    ax.add_patch(FancyArrowPatch((x,y),(xx,yy),arrowstyle='-|>',mutation_scale=15,
                                color='#426687',lw=1.3))
    if label: ax.text((x+xx)/2,(y+yy)/2+.12,label,ha='center',fontsize=10,color='#355775')
ax.text(.5,10.7,'Common-stage and unchanged-residual steps can fail',
        fontsize=18,weight='bold',color='#102c4c')
ax.text(.5,10.28,'Two actual amenable inclusions  |  exact constants, original targets and prescribed prefixes',
        fontsize=11,color='#456079')
box(.55,7.75,5.45,1.9,'Index 25: one unchanged finite prefix',
    [(r'$A_1=D_2^+\subset F=\operatorname{Mat}_{25}$',16),
     (r'$E_{A_1}(z_{\mathcal{T}})=z_1,\quad \|z_{\mathcal{T}}\|\leq1$',14),
     (r'$\operatorname{Var}_\tau(z_1)\geq 4h_+^2/25,\quad h_+>0$',14)])
box(8.0,7.75,5.85,1.9,'Every continuation has the same variance',
    [(r'$x_{\mathcal{T}}=E_F(z_{\mathcal{T}})$',16),
     (r'$\operatorname{Var}_\tau(x_{\mathcal{T}})\geq4h_+^2/25$',15),
     ('625 fixed shift-and-clock unitaries in F.',11)])
arrow(6.17,8.58,7.8,8.58,'CF.2–CF.4')
box(.55,5.25,6.35,1.75,'A common stage must miss a fixed target',
    [(r'$\frac{1}{625}\sum_{u\in Y}\|[u,z_{\mathcal{T}}]\|_2^2\geq8h_+^2/25$',15),
     (r'$\max_{u\in Y}\|u-E_{D_{\mathcal{T},m}}u\|_2\geq\sqrt{2}h_+/5$',15)],
    '#fff2e5')
box(7.7,5.25,6.15,1.75,'A full finite family still exists',
    [(r'$\|u-E_{P_*}u\|_2<h_+/10\quad(u\in Y)$',16),
     ('The same physical blocks cannot share one stage.',12)],
    '#e9f7ef')
arrow(10.3,7.57,10.3,7.17,'CF.5–CF.8')
arrow(7.49,6.06,7.03,6.06,'CF.9')
ax.text(.7,4.76,'Plain amenability gives the family here. Ergodic-core hypotheses still govern the stronger common-stage theorem.',
        fontsize=11,color='#294865')
box(.55,.8,6.15,3.35,'Nonuniform spin: no unchanged-residual cells',
    [(r'$p\in(1/2,2/3)$ transcendental; $q=1-p$',13),
     (r'$H(x)=\sum_r h_r x^{n-r}(1-x)^r,\quad h_r\geq0$',14),
     (r'$m$ disjoint old supports, each of trace $p^n$',13),
     (r'$\tau(f)=1-mp^n>0$',17),
     (r'$\sum_a H_a(p)=1-mp^n\ \Longrightarrow\ \sum_a H_a(1)=1-m<0$',12),
     ('Finite rank polynomials have nonnegative value at 1.',10)],
    '#f0eef9')
plot=fig.add_axes([.525,.22+.78*.085,.41,.78*.235],facecolor='#fafcff')
xx=np.linspace(0,1,301)
plot.plot(xx,1-2*xx**2,color='#794c9f',lw=2.2,label=r'formal remainder $1-2x^2$')
plot.axhline(0,color='#4f657b',lw=1)
plot.axvspan(.5,2/3,color='#c3e5d2',alpha=.6,label=r'actual parameter interval for $p$')
plot.plot([1],[-1],'o',color='#b14c46')
plot.annotate(r'$x=1:\ -1$',(1,-1),(.66,-.82),arrowprops={'arrowstyle':'->','color':'#9c4b43'},
              fontsize=12,color='#943f3c')
plot.set(xlim=(0,1.04),ylim=(-1.15,1.15),xlabel='Formal polynomial variable x',ylabel='Formal remainder')
plot.grid(alpha=.18);plot.legend(loc='upper left',fontsize=9,frameon=True,facecolor='#fafcff',framealpha=1)
ax.text(7.72,3.95,r'Example $m=2,n=2$: the actual remainder is positive on $(1/2,2/3)$.',
        fontsize=10,color='#35506c')
ax.text(7.72,3.65,'With m = floor(p⁻ⁿ), positive residual traces tend to zero.',
        fontsize=10,color='#35506c')
ax.text(.65,.23,'CF.1–CF.9 and RF.1–RF.26  |  schematic block sizes; no area represents a canonical trace',
        fontsize=10,color='#416078')
ax=fig.add_axes([0,0,1,.22])
ax.set(xlim=(0,14.4),ylim=(0,3.2));ax.axis('off')
box(.55,1.1,5.3,1.8,'The corrected finite family cuts old supports',
    [(r"$r_i'\leq r_i,\quad f_*=f+\sum_i(r_i-r_i')$",15),
     (r"$\sum_i\tau(r_i-r_i')=\Delta_J\to0$",15),
     ('The original targets and earlier cups stay fixed.',11)],
    '#e9f7ef')
box(8.15,1.1,5.7,1.8,'Exact finite complement and physical placement',
    [(r'$q_0\in C_J,\quad vq_0v^*=f_*,\quad v\in N_k$',14),
     (r'$m=n=2,\ J=4:\ \tau(f_*)=(1-p^2)^2$',15),
     (r'Physical cut $p^4$; distinct dual cut $q^4$.',12)],
    '#e9f7ef')
arrow(6.07,1.9,7.91,1.9,'RF.16–RF.17')
ax.text(.72,.65,r'Extra physical error $\leq(1+\sqrt{2})R\sqrt{\Delta_J}$; choose a finite J from RF.25.',
        fontsize=15,color='#163955')
ax.text(.72,.17,'RF.12–RF.26  |  a complete correction in this actual model  |  Popa (1994), §4.4  |  CC0',
        fontsize=10,color='#416078')
for ext in ['svg','png']:
    fig.savefig(D/('prefix-and-residual-obstructions-v12.'+ext),dpi=125,facecolor=fig.get_facecolor())
p=D/'prefix-and-residual-obstructions-v12.svg'
p.write_text('\n'.join(line.rstrip() for line in p.read_text(encoding='utf-8').splitlines())+'\n',encoding='utf-8')
plt.close(fig)
(D/'diagram-check.json').write_text(json.dumps(dict(
    actual_matrix_dimension=25,targets=625,proofs=['CF.1–CF.9','SR trace obstruction'],
    plotted_polynomial=dict(m=2,n=2,variable='Formal x; not an assigned physical trace'),
    actual_parameter_interval=[.5,2/3],trace_scaled_shapes=False,
    exact_positive_h_not_numerically_sampled=True),indent=2)+'\n',encoding='utf-8')
