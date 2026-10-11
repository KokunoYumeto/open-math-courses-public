"""Exact bound diagrams for the original cascade; no sampled nonlinear trajectory."""
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch
R=Path(__file__).resolve().parent
plt.rcParams.update({'font.family':'DejaVu Sans','font.size':13,'mathtext.fontset':'dejavusans'})
blue='#173b59';teal='#087f8c';orange='#a45423';gray='#546979'
def canvas(title):
 fig=plt.figure(figsize=(15,12),facecolor='#f6f8fb')
 fig.text(.055,.955,title,fontsize=22,weight='bold',color=blue)
 axes=[fig.add_axes([.06,.68,.88,.22]),fig.add_axes([.06,.36,.88,.23]),fig.add_axes([.06,.075,.88,.22])]
 for ax in axes:ax.set_xlim(0,1);ax.set_ylim(0,1);ax.axis('off')
 return fig,axes
fig,axs=canvas('The actual remaining time controls growth between checkpoints')
ax=axs[0]
ax.text(0,1.10,'1   The entire future sum retains the actual amplitudes',fontsize=17,weight='bold',color=blue)
ax.annotate('',xy=(.98,.71),xytext=(.02,.71),arrowprops={'arrowstyle':'->','lw':2,'color':blue})
for pos,label in [(.06,r'$t_n$'),(.31,r'$t$'),(.62,r'$t_{n+1}$'),(.92,r'$T_*$')]:
 ax.plot(pos,.71,'o',color=teal);ax.text(pos,.86,label,ha='center',fontsize=17)
ax.annotate('',xy=(.92,.49),xytext=(.31,.49),arrowprops={'arrowstyle':'<->','color':orange,'lw':2})
ax.text(.615,.28,r'$\tau(t)=T_*-t$',ha='center',fontsize=20,color=orange)
ax.text(.015,.01,r'$r_-e_n\leq e_{n+1}\leq r_+e_n,\quad r_-=1-41K^{-39},\quad r_+=1+3K^{-20}$',fontsize=19)
ax=axs[1]
ax.text(0,1.10,'2   Exact physical time and frequency bounds',fontsize=17,weight='bold',color=blue)
ax.text(.015,.77,r'$\frac{l}{q^{5n/2}e_n}\leq T_*-t\leq\frac{U}{q^{5n/2}e_n}$',fontsize=24,color=teal)
ax.text(.015,.44,r'$l=\frac{1}{2(q^{5/2}r_+-1)},\qquad U=\frac{2}{1-q^{-5/2}r_-^{-1}}$',fontsize=21)
ax.text(.015,.09,r'$a_K=-\frac{\log(1-41K^{-39})}{\log q}<\frac{1}{100},\qquad q^{-a_K(n-n_0)}\leq e_n\leq1$',fontsize=20)
ax=axs[2]
ax.text(0,1.12,'3   The complete critical norm has a matching rate',fontsize=17,weight='bold',color=blue)
ax.text(.5,.76,r'$\frac{A_{\rm low}}{T_*-t}\leq\|u(t)\|_{H^{5/2}}\leq\frac{A_{\rm high}}{T_*-t}$',ha='center',fontsize=28,color=teal)
ax.text(.5,.43,r'$A_{\rm low}=\sqrt{1-40K^{-39}}\,(4\pi^2)^{5/4}l,\qquad A_{\rm high}=D_{5/2}U$',ha='center',fontsize=19)
ax.text(.5,.14,'The full Sobolev constant D is given in EX22; every original band contributes.',ha='center',fontsize=14,color=gray)
fig.text(.06,.02,'Schematic time spacing. Exact bounds EX1–EX25 hold for UI1–UI4 and t at or after the first checkpoint.',fontsize=11,color=gray)
for ext in ['png','svg']:fig.savefig(R/('original-cascade-lifetime-and-growth.'+ext),dpi=150,facecolor=fig.get_facecolor())
plt.close(fig)

fig,axs=canvas('Every Fourier band enters the full Sobolev estimate')
ax=axs[0]
ax.text(0,1.10,'1   The original field is an orthogonal sum of complete band fields',fontsize=17,weight='bold',color=blue)
xs=[.08,.24,.40,.57,.75,.92]
labels=[r'$n_0$',r'$\cdots$',r'$n-1$',r'$n$',r'$n+1$',r'$n+2,\ldots$']
for x,label in zip(xs,labels):
 color=teal if label in [r'$n$',r'$n+1$'] else gray
 ax.add_patch(FancyBboxPatch((x-.055,.42),.11,.27,boxstyle='round,pad=.007',facecolor='white',edgecolor=color,lw=2))
 ax.text(x,.55,label,ha='center',va='center',fontsize=16,color=color)
ax.text(.5,.14,r'$\|u(t)\|_{H^\sigma}^2\leq 2\sum_{m=n_0}^{\infty}(1+\chi q^{2m})^\sigma E_m(t)$',ha='center',fontsize=23,color=blue)
ax=axs[1]
ax.text(0,1.10,'2   The full band bounds retain the physical index and tail weight',fontsize=17,weight='bold',color=blue)
ax.text(.015,.77,r'$E_{n+1-j}\leq K^{-40}q^{j/10}e_n^2,\qquad 2\leq j\leq n-n_0+1$',fontsize=20,color=gray)
ax.text(.015,.43,r'$E_n+E_{n+1}\leq e_n^2$',fontsize=22,color=teal)
ax.text(.015,.08,r'$2\sum_{m\geq n+2}q^{20(m-n-2)}E_m\leq C^2e_n^2K^{-78}$',fontsize=22,color=gray)
ax=axs[2]
ax.text(0,1.12,'3   The exact finite coarse sum has a visible threshold',fontsize=17,weight='bold',color=blue)
ax.text(.015,.80,r'$\sum_{j=2}^{H+1}q^{(1/10-2\sigma)j},\qquad H=n-n_0$',fontsize=23)
ax.text(.015,.50,r'$\sigma>1/20:\ \mathrm{bounded};\qquad \sigma=1/20:\ H$',fontsize=21,color=orange)
ax.text(.015,.19,r'$1/20<\sigma\leq10:\quad \|u(t)\|_{H^\sigma}\leq D_\sigma e_nq^{\sigma n}$',fontsize=22,color=teal)
fig.text(.06,.02,'Schematic band boxes, not spectral data. Full constants and complete finite sum: EX17–EX24; lower packet map: EX11.',fontsize=11,color=gray)
for ext in ['png','svg']:fig.savefig(R/('original-cascade-sobolev-sums.'+ext),dpi=150,facecolor=fig.get_facecolor())
plt.close(fig)

