"""Exact cell geometry and literal complex-leaf obstruction for L043.
CC0; GPT-6.1 Sol (OpenAI), Ultra reasoning effort, October 2026.
The M4,B8 diagram is cell geometry only; no full operator is assigned to it.
The second example is the fully specified constant model F=-rho,G1.
"""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle

plt.rcParams.update({'font.family':'DejaVu Sans','font.size':14,
    'axes.titlesize':17,'axes.labelsize':15,'figure.facecolor':'#fffdfa',
    'axes.facecolor':'#fffdfa','savefig.facecolor':'#fffdfa'})
fig=plt.figure(figsize=(14,10.8),dpi=150)
gs=fig.add_gridspec(2,2,top=.83,bottom=.12,left=.09,right=.96,
    hspace=.60,wspace=.38,height_ratios=[1,1])
fig.text(.06,.947,'Scale the cell and test the exact bracket leaf',fontsize=24,weight='bold',color='#172d44')
fig.text(.06,.898,'Exact coordinate maps, cell masses and a constant-coefficient source test',fontsize=17,color='#414b57')
colors={'core':'#4773a0','outer':'#8a5637','complex':'#ae422e','real':'#177467'}
ax=fig.add_subplot(gs[0,0]);ax.set_title('Normalized cell: two fixed radii')
for a,color,style in [(.5,colors['core'],'-'),(.75,colors['outer'],'--'),(1,'#929ba5',':')]:
    ax.add_patch(Rectangle((-a,-a),2*a,2*a,fill=False,lw=2.5,ec=color,ls=style))
ax.text(0,.25,r'$Q_{1/2}$',ha='center',color=colors['core'],fontsize=19)
ax.text(0,.64,r'$Q_{3/4}$',ha='center',color=colors['outer'],fontsize=18)
ax.set(xlim=(-1.08,1.08),ylim=(-1.08,1.08),xlabel=r'$X=M(t-y_t)$',ylabel=r'$Z=B(z-y_z)$')
ax.set_aspect('equal');ax.set_xticks([-1,-.5,0,.5,1]);ax.set_yticks([-1,-.5,0,.5,1]);ax.grid(alpha=.15)
ax=fig.add_subplot(gs[0,1]);ax.set_title(r'Exact cell geometry only: $M=4,\ B=8$')
for a,color,style in [(.5,colors['core'],'-'),(.75,colors['outer'],'--'),(1,'#929ba5',':')]:
    ax.add_patch(Rectangle((-a/4,-a/8),a/2,a/4,fill=False,lw=2.5,ec=color,ls=style))
ax.set(xlim=(-.28,.28),ylim=(-.14,.14),xlabel=r'$t-y_t=X/4$',ylabel=r'$z-y_z=Z/8$')
ax.set_aspect('equal');ax.set_xticks([-.25,-.125,0,.125,.25],['−1/4','−1/8','0','1/8','1/4'])
ax.set_yticks([-.125,-.0625,0,.0625,.125],['−1/8','−1/16','0','1/16','1/8']);ax.grid(alpha=.15)
ax.text(0,.025,r'$E_{1/2}(y)$',ha='center',color=colors['core'],fontsize=19)
ax.text(.5,-.34,r'$dX\,dZ=32\,dt\,dz$',ha='center',transform=ax.transAxes,fontsize=17)

ax=fig.add_subplot(gs[1,0]);ax.set_title(r'Constant model: $F=-\rho,\ G=1$')
ax.axhline(0,color=colors['real'],lw=2.6,label=r'Real leaf $(-\rho+\eta)/\rho$')
ax.axvline(-1,color=colors['complex'],lw=2.6,label=r'Complex leaf $(-\rho+i\eta)/\rho$')
ax.plot([-1,0],[0,0],color='#183a55',lw=4,ls='--')
ax.scatter([-1,0,-1],[0,0,1],s=55,color=['#183a55',colors['real'],colors['complex']],zorder=5)
ax.text(-.83,.12,r'$\min|\widetilde L_2|/\rho=1$',fontsize=13,color='#183a55')
ax.annotate(r'$\eta=\rho$: real leaf is zero',(0,0),xytext=(-.35,-.43),fontsize=11.5,
    arrowprops={'arrowstyle':'->','color':colors['real']},color=colors['real'])
ax.annotate(r'At $\eta=\rho$: $-1+i$',(-1,1),xytext=(-.7,1.26),fontsize=12,
    arrowprops={'arrowstyle':'->','color':colors['complex']},color=colors['complex'])
ax.set(xlim=(-1.5,1.3),ylim=(-1.25,1.65),xlabel=r'$\operatorname{Re}L_2/\rho$',ylabel=r'$\operatorname{Im}L_2/\rho$')
ax.set_aspect('equal');ax.grid(alpha=.15)
ax.legend(loc='lower left',fontsize=10.5,framealpha=.98)

ax=fig.add_subplot(gs[1,1]);ax.axis('off')
ax.text(0,.98,'Integrate cell centers\nto restore the full norm',fontsize=16,weight='bold',color='#172d44',va='top')
ax.text(0,.67,r'$\int_R 1_{E_a(y)}(x)\,M(y)B(y)\,dy\asymp1$',fontsize=16,color='#172d44')
ax.text(0,.57,'For the geometric illustration above:',fontsize=12,color='#414b57')
ax.text(0,.48,r'$M^3B=512,\quad MB=32$',fontsize=17,color=colors['core'])
ax.text(0,.34,'Literal complex leaf:\nthe equation norm stays bounded',fontsize=14,weight='bold',color=colors['complex'],va='top')
ax.text(0,.10,r'$u_\rho=e^{i\rho z}\phi,\qquad\|u_\rho\|=1$',fontsize=17,color='#172d44')
ax.text(0,-.06,r'$Pu_\rho=e^{i\rho z}(D_t+iD_z)\phi$',fontsize=17,color='#172d44')
ax.text(0,-.18,'All brackets with two or more leaves vanish.',fontsize=12,color='#414b57')
fig.text(.06,.058,'Cell geometry: (3.1), (5.1)–(5.5), (6.1)–(6.3). Constant-model test: (7.1)–(7.3). The two examples are separate.',fontsize=12,color='#414b57')
fig.text(.06,.023,'Hörmander IV, Proposition 27.5.1, printed p.202: literal complex leaf versus the real leaf in the normalized proof. Original diagram; CC0.',fontsize=11.4,color='#414b57')
target=Path(__file__).with_name('rooted-cells-and-complex-leaf.png')
fig.savefig(target,dpi=150,metadata={'Software':'AN05-L043 reproducible mathematical illustration; CC0'})
plt.close(fig);print(target.name)
