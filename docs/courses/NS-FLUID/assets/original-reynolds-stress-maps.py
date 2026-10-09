"""Exact residual maps; schematic geometry represents Sobolev orthogonality."""
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrowPatch
out=Path(__file__).resolve().parent
fig=plt.figure(figsize=(14,8.4),layout='constrained')
fig.get_layout_engine().set(rect=(0,.07,1,.91))
gs=fig.add_gridspec(2,2,height_ratios=[1.1,1])
top=fig.add_subplot(gs[0,:]);left=fig.add_subplot(gs[1,0]);right=fig.add_subplot(gs[1,1])
for ax in [top,left,right]:ax.set_axis_off()
fig.suptitle('The original residual, its constant mode, and the least-norm stress',fontsize=18,weight='bold')
top.set(xlim=(0,1),ylim=(0,1))
def box(x,y,text,color):
    top.text(x,y,text,ha='center',va='center',fontsize=14,bbox=dict(boxstyle='round,pad=.6',fc=color,ec='#40545f'))
box(.5,.84,r'$g=\langle g\rangle+(g-\langle g\rangle)$','#e7f0f5')
box(.22,.42,r'$\langle g\rangle=V_L^{-1}\int g\,dx$'+'\nOriginal constant residual','#fff0df')
box(.76,.42,r'$S_0=\mathcal{R}_Lg$'+'\n'+r'$\operatorname{div}S_0=g-\langle g\rangle$','#e3f2e9')
for x in [.22,.76]:
    top.add_patch(FancyArrowPatch((.5,.73),(x,.57),arrowstyle='-|>',mutation_scale=16,color='#40545f'))
top.text(.22,.07,'A periodic divergence has zero mean.\nThe original constant residual stays explicit.',ha='center',fontsize=12)
top.text(.76,.07,'Every tensor component is retained.\n'+r'$S_0^{T}=S_0,\quad \operatorname{tr}S_0=0,\quad \langle S_0\rangle=0$',ha='center',fontsize=12)
left.set(xlim=(-.3,4.7),ylim=(-.85,3.3))
left.plot([0,3.5,3.5,0],[0,0,2.5,0],color='#247f74',lw=2.5)
left.plot([3.23,3.23,3.5],[0,.27,.27],color='#586779',lw=1)
left.text(1.75,-.33,r'$\|\mathcal{R}_Lg\|_{H_L^{s+1}}$',ha='center',fontsize=13)
left.text(3.67,1.25,r'$\|K\|_{H_L^{s+1}}$',ha='left',fontsize=12)
left.text(1.35,1.43,r'$\|S_0+K\|_{H_L^{s+1}}$',rotation=35,ha='center',fontsize=12)
left.text(1.8,3.1,'All other stresses add a divergence-free tensor K',ha='center',fontsize=13,weight='bold')
left.text(1.8,-.62,'Schematic norm triangle; exact orthogonality is RS14.',ha='center',fontsize=11)
right.set(xlim=(0,1),ylim=(0,1))
right.text(.5,.87,'The trace goes into the same pressure',ha='center',fontsize=14,weight='bold')
right.text(.5,.6,r'$\theta=\operatorname{tr}S/n$'+'\n\n'+r'$p^\circ=p-\theta,\qquad S^\circ=S-\theta I_n$',ha='center',fontsize=16)
right.text(.5,.23,r'$(p-\theta)u-(S-\theta I_n)u=pu-Su$',ha='center',fontsize=15)
right.text(.5,.07,'The complete energy flux is preserved (RS25).',ha='center',fontsize=12)
fig.text(.5,.004,r'Proof: RS1–RS14 and RS23–RS25. Original periods $L_j$, volume $V_L$, frequency $2\pi k_j/L_j$ and viscosity $\nu$ remain unchanged.',ha='center',fontsize=11)
fig.savefig(out/'original-reynolds-stress-maps.png',dpi=150)
fig.savefig(out/'original-reynolds-stress-maps.svg')
