"""Normal intertwining proof diagram, with exact maps and implication order; CC0."""
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch
plt.rcParams.update({'font.family':'DejaVu Sans','font.size':17,'svg.hashsalt':'oa-classify-normal-absorption-v1'})
out=Path(__file__).resolve().parent
fig=plt.figure(figsize=(6.5,12.5));fig.patch.set_facecolor('#fffdf8')
ax=fig.add_axes([.06,.035,.88,.93]);ax.set_xlim(0,1);ax.set_ylim(0,1);ax.axis('off')
ink='#183744';blue='#176a8a';green='#dceee2'
ax.text(.5,.98,'Making absorption normal and onto',ha='center',va='top',fontsize=20,weight='bold',color=ink)
ax.text(.5,.925,r'$A=M\,\overline{\otimes}\,B,\quad E=\mathrm{id}\otimes\tau_B$',ha='center',color=ink)
ax.text(.5,.88,r'$W_n=W_{n-1}u_n^*$',ha='center',color=ink,fontsize=22)
ax.text(.13,.808,r'$M$',ha='center',color=ink,fontsize=26)
ax.text(.87,.808,r'$A$',ha='center',color=ink,fontsize=26)
ax.annotate('',xy=(.78,.833),xytext=(.22,.833),arrowprops={'arrowstyle':'->','color':blue,'lw':2.3})
ax.text(.5,.85,r'$\Phi_n=\mathrm{Ad}\,W_n\circ\iota$',ha='center',color=ink)
ax.annotate('',xy=(.22,.795),xytext=(.78,.795),arrowprops={'arrowstyle':'->','color':blue,'lw':2.3})
ax.text(.5,.762,r'$\Psi_n=E\circ\mathrm{Ad}\,W_n^*$',ha='center',color=ink)
ax.text(.5,.715,r'$\Psi_n\Phi_n=\mathrm{id}_M$',ha='center',color=ink,fontsize=22)
boxes=[
 (.57,'1. Normal predual limit',r'$\Psi_n^*\psi\ \longrightarrow\ \Psi^*\psi$','Norm convergence; Ψ is normal and u.c.p.'),
 (.42,'2. Stable preimages\nand vanishing defects',r'$x_{j,n}=\Psi_n(Y_j)\ \longrightarrow\ \Psi(Y_j)$','Strong-star limits make Ψ multiplicative.'),
 (.27,'3. Injective, then onto',r'$\Psi(Z_i)=X_i,\quad Z_i=\lim_n\Phi_n(X_i)$','Factoriality + normal compact unit balls.'),
 (.12,'4. Inverse isomorphism and cocycle',r'$\Phi=\Psi^{-1},\quad c_g=\lim_n W_na_g(W_n^*)$','Summable transported strong-star errors.')]
for y,title,formula,caption in boxes:
 ax.add_patch(FancyBboxPatch((.015,y-.015),.97,.13,boxstyle='round,pad=.012',facecolor=green,edgecolor=blue,lw=1.2))
 ax.text(.5,y+.089,title,ha='center',va='center',fontsize=17,weight='bold',color=ink)
 ax.text(.5,y+.042,formula,ha='center',fontsize=17,color=ink)
 ax.text(.5,y+.003,caption,ha='center',fontsize=16,color=ink)
ax.text(.5,.027,r'$\Phi\alpha_g\Phi^{-1}=\mathrm{Ad}\,c_g\circ a_g$',ha='center',color=ink,fontsize=20)
fig.savefig(out/'normal-absorption-intertwining.svg',metadata={'Date':None,'Creator':'OA-CLASSIFY Writing AI; GPT-6.1 Sol Ultra; original CC0'})
fig.savefig(out/'normal-absorption-intertwining.png',dpi=160,metadata={'Software':'OA-CLASSIFY Writing AI; GPT-6.1 Sol Ultra; original CC0'})
plt.close(fig)
