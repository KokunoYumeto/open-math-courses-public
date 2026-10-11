"""Reproduce the complete uniform-cascade bound diagram; no numerical trajectory."""
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch
R=Path(__file__).resolve().parent
plt.rcParams.update({'font.family':'DejaVu Sans','font.size':13,'mathtext.fontset':'dejavusans'})
fig=plt.figure(figsize=(15,12),facecolor='#f6f8fb')
axs=[fig.add_axes([.06,.69,.88,.22]),fig.add_axes([.06,.35,.88,.25]),fig.add_axes([.06,.07,.88,.21])]
for ax in axs:ax.set_xlim(0,1);ax.set_ylim(0,1);ax.axis('off')
fig.text(.06,.963,'Every transfer retains the original field and its entire history',fontsize=22,weight='bold',color='#16334c')
ax=axs[0]
ax.text(0,1.07,'1   The same bounds hold at every constructed scale',fontsize=17,weight='bold',color='#16334c')
ax.annotate('',xy=(.99,.68),xytext=(.015,.68),arrowprops={'arrowstyle':'->','lw':2,'color':'#315a78'})
for xx,label in [(.04,r'$0$'),(.29,r'$t_N$'),(.60,r'$t_c$'),(.91,r'$t_{N+1}$')]:
    ax.plot(xx,.68,'o',ms=8,color='#136e83');ax.text(xx,.83,label,ha='center',fontsize=16)
ax.text(.02,.43,r'All moments start at $0$; no heat or memory history is reset.',fontsize=14)
ax.text(.02,.21,r'$A=e_N,\quad k=q^{5N/2},\qquad \frac{1}{2}<kA(t_c-t_N)<\frac{3}{2}$',fontsize=17,color='#136e83')
ax.text(.02,-.02,r'$t_{N+1}=t_c+(kA)^{-1}K^{-1/2},\qquad q^{-1/100}e_N\leq e_{N+1}\leq q^{1/100}e_N$',fontsize=17)
ax=axs[1]
ax.text(0,1.11,'2   Two estimates close the induction without growing constants',fontsize=17,weight='bold',color='#16334c')
for xx,title in [(.01,'Previous band'),(.525,'Full forward tail')]:
    ax.add_patch(FancyBboxPatch((xx,.08),.465,.85,boxstyle='round,pad=.009',facecolor='white',edgecolor='#7892a5',lw=1.4))
    ax.text(xx+.2325,.78,title,ha='center',fontsize=16,weight='bold')
ax.text(.2425,.57,r'$E_{N-1}(t)\leq A^2K^{-59}$',ha='center',fontsize=19,color='#136e83')
ax.text(.2425,.405,r'$(t_c\leq t\leq t_{N+1})$',ha='center',fontsize=12)
ax.text(.2425,.20,r'$\exp(-kK\int_u^v a_N)\leq2$',ha='center',fontsize=18)
ax.text(.7575,.57,r'$Y_N^2=2\sum_{m\geq N+2}q^{20(m-N-2)}E_m$',ha='center',fontsize=16)
ax.text(.7575,.34,r'$Y_N\leq CAK^{-39}$',ha='center',fontsize=19,color='#136e83')
ax.text(.7575,.16,r'$Y_N(t_N)\leq q^{-(10-1/100)}Ce_NK^{-39}$',ha='center',fontsize=13)
ax.text(.01,-.04,'The signed rotor integral controls every forcing interval; the exact tail shift closes its recurrence.',fontsize=13,color='#465b70')
ax=axs[2]
ax.text(0,1.11,'3   The resulting finite endpoint belongs to the averaged equation',fontsize=17,weight='bold',color='#16334c')
ax.text(.02,.79,r'$\epsilon^2e_{N+1}\exp(-K^{10})<c_{N+1}(t_{N+1})\leq10^{-5}\epsilon^2e_{N+1}\exp(-K^{10}/2)$',fontsize=17,color='#8b4b23')
ax.text(.02,.45,r'$T_*=\lim_Nt_N\leq2C_tq^{-5n_0/2}<\infty,\qquad C_t=(1-q^{-(5/2-1/100)})^{-1}$',fontsize=18,color='#136e83')
ax.text(.02,.12,r'$\|u(t_N)\|_{H^{10}}\geq(4\pi^2)^5q^{10N}q^{-(N-n_0)/100}\longrightarrow\infty$',fontsize=18)
fig.text(.06,.02,'Schematic clock, not a numerical solution. Original viscosity and all scale factors are retained. Proof: UI1-UI59.',fontsize=11,color='#465b70')
fig.savefig(R/'uniform-viscous-cascade.png',dpi=150,facecolor=fig.get_facecolor())
fig.savefig(R/'uniform-viscous-cascade.svg',facecolor=fig.get_facecolor())
plt.close(fig)

