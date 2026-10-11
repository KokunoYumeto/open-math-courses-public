"""Reproduce the original-coordinate first-transfer mechanism diagram."""
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch
R=Path(__file__).resolve().parent
plt.rcParams.update({'font.family':'DejaVu Sans','font.size':13,'mathtext.fontset':'dejavusans'})
fig=plt.figure(figsize=(15,11),facecolor='#f6f8fb')
axs=[fig.add_axes([.065,.69,.87,.23]),fig.add_axes([.065,.37,.87,.25]),fig.add_axes([.065,.06,.87,.24])]
for ax in axs: ax.set_xlim(0,1);ax.set_ylim(0,1);ax.axis('off')
fig.text(.065,.965,'The first transfer in the original viscous cascade',fontsize=23,weight='bold',color='#16334c')
ax=axs[0]
ax.text(0,1.02,'1   Construct the times before using them',fontsize=17,weight='bold',color='#16334c')
ax.annotate('',xy=(.97,.55),xytext=(.035,.55),arrowprops={'arrowstyle':'->','lw':2,'color':'#315a78'})
xs=[.05,.29,.49,.69,.91]
labels=[r'$0$',r'$t_c$',r'$s_0=t_c+\kappa^{-1}K^{-9}$',r'$t_1=t_c+\kappa^{-1}K^{-1}$',r'$t_2=t_c+\kappa^{-1}K^{-1/2}$']
for x,label in zip(xs,labels):
 ax.plot(x,.55,'o',color='#136e83',ms=8)
 ax.text(x,.76,label,ha='center',fontsize=12)
ax.text(.05,.27,r'$u(0)=\psi_{1,n_0}$',ha='center',fontsize=12)
ax.text(.29,.27,r'$c=\epsilon^2K^{-10}$',ha='center',fontsize=12)
ax.text(.49,.27,r'$\epsilon^{-2}c\geq K^{100}$',ha='center',fontsize=12)
ax.text(.69,.27,r'$a_{n_0+1}>1/10$',ha='center',fontsize=12)
ax.text(.91,.27,r'$a_{n_0+1}\geq1-7K^{-80}$',ha='center',fontsize=12)
ax.text(0,-.02,r'Physical time: $\kappa=q^{5n_0/2}$. Spacing is schematic. All marked times lie below $T_0<T_*$.',fontsize=12,color='#465b70')
ax=axs[1]
ax.text(0,1.01,'2   Retain every band, viscosity and the entire forward tail',fontsize=17,weight='bold',color='#16334c')
for x,w,title,content in [
 (.01,.28,r'Current scale $n_0$',r'$a,\ b,\ c,\ d$'+'\n'+r'$v_{i,n_0}=\nu\langle\Delta u_{i,n_0},\psi_{i,n_0}\rangle$'),
 (.37,.27,r'Receiver $n_0+1$',r'$z=a_{n_0+1}$'+'\n'+r'$z^\prime=\kappa q^{5/2}Kd^2+r_z$'),
 (.73,.26,r'All scales $m\geq n_0+2$',r'$Y^2=2\sum_m q^{20(m-n_0-2)}E_m$'+'\n'+r'$Y\leq65K^{-39}$')]:
 ax.add_patch(FancyBboxPatch((x,.2),w,.59,boxstyle='round,pad=.008',facecolor='white',edgecolor='#7892a5',lw=1.4))
 ax.text(x+w/2,.68,title,ha='center',fontsize=13,weight='bold')
 ax.text(x+w/2,.41,content,ha='center',va='center',fontsize=11,linespacing=2)
for lo,hi in [(.30,.355),(.655,.715)]:
 ax.annotate('',xy=(hi,.49),xytext=(lo,.49),arrowprops={'arrowstyle':'->','lw':2,'color':'#136e83'})
ax.text(.5,.03,r'Full weighted energy gives $H^{10}$ continuation before activation is invoked (FT53–FT58).',ha='center',fontsize=12,color='#465b70')
ax=axs[2]
ax.text(0,1.03,'3   Energy transfers; the printed next-drive bound needs correction',fontsize=17,weight='bold',color='#16334c')
ax.text(.02,.75,r'$\|u(t_2)-a_{n_0+1}(t_2)\psi_{1,n_0+1}\|_2^2\leq7K^{-80}$',fontsize=19,color='#136e83')
ax.text(.02,.45,r'$\epsilon^2e^{-K^{10}}<c_{n_0+1}(t_2)\leq10^{-5}\epsilon^2e^{-K^{10}/2}a_{n_0+1}(t_2)$',fontsize=18,color='#8b4b23')
ax.text(.02,.15,'The first checkpoint is proved. The complete uniform proof UI1–UI59 propagates the corrected drive range.',fontsize=12,color='#465b70')
fig.savefig(R/'original-viscous-first-transfer.png',dpi=150,facecolor=fig.get_facecolor())
fig.savefig(R/'original-viscous-first-transfer.svg',facecolor=fig.get_facecolor())
plt.close(fig)
