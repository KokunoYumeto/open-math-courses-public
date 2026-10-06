"""Exact finite C5 example of the Bernoulli tower formula; original CC0."""
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle
plt.rcParams.update({'font.family':'DejaVu Sans','font.size':17,'svg.hashsalt':'oa-classify-bernoulli-tower-v1'})
out=Path(__file__).resolve().parent
fig=plt.figure(figsize=(6.5,10.5));fig.patch.set_facecolor('#fffdf8')
ax=fig.add_axes([.06,.04,.88,.92]);ax.set_xlim(0,1);ax.set_ylim(0,1);ax.axis('off')
blue='#176a8a';orange='#e3aa63';green='#74b298';ink='#183744'
ax.text(.5,.98,'A matrix model on a tower',ha='center',va='top',fontsize=22,color=ink,weight='bold')
ax.text(.5,.925,r'$Q=C_5,\quad R=\{0,1,2\},\quad g=1$',ha='center',color=ink)
ax.text(.5,.88,r'$B_{C_5}=(M_2)^{\otimes5}=M_{32}$',ha='center',color=ink)
ax.text(.02,.83,'Each block has trace 1/5.',color=ink)
for s in range(5):
 x=.02+s*.197
 ax.add_patch(Rectangle((x,.70),.173,.087,facecolor=blue if s in [0,1,2] else orange,edgecolor=ink))
 ax.text(x+.0865,.765,str(s),ha='center',color='white' if s<3 else ink,fontsize=20)
 ax.text(x+.0865,.72,r'$\delta_{%d}(x)$'%(-s) if s<3 else r'$x$',ha='center',color='white' if s<3 else ink,fontsize=17)
ax.text(.5,.657,'Upper row: the blocks of Θ(x).',ha='center',color=ink)
ax.annotate('',xy=(.91,.58),xytext=(.09,.58),arrowprops={'arrowstyle':'->','lw':2,'color':blue})
ax.text(.5,.60,'γ₁ shifts blocks one step, cyclically.',ha='center',fontsize=17,color=ink)
for t in range(5):
 x=.02+t*.197;good=t in [1,2]
 ax.add_patch(Rectangle((x,.455),.173,.072,facecolor=green if good else orange,edgecolor=ink))
 ax.text(x+.0865,.488,str(t),ha='center',fontsize=20,color=ink)
ax.text(.5,.417,r'$C_1=E_1+E_2$',ha='center',color=ink)
ax.text(.5,.376,'Green blocks agree exactly:',ha='center',color=ink)
ax.text(.5,.335,r'$\gamma_1\Theta(x)=\Theta\delta_1(x)$',ha='center',color=ink)
ax.text(.5,.291,r'on $C_1$, for $x$ in the tested matrix algebra.',ha='center',fontsize=16,color=ink)
ax.text(.5,.24,'Orange is the common error support.',ha='center',color=ink)
ax.text(.5,.20,r'$\tau(1-C_1)=\frac{2}{5}+\frac{1}{5}=\frac{3}{5}$',ha='center',color=ink,fontsize=21)
ax.text(.5,.137,r'$\|\gamma_1\Theta(x)-\Theta\delta_1(x)\|_2$',ha='center',color=ink,fontsize=19)
ax.text(.5,.09,r'$\leq2\|x\|\sqrt{3/5}$',ha='center',color=ink,fontsize=21)
ax.text(.5,.023,'Exact finite example; no infinite absorption claim.',ha='center',fontsize=14,color=ink)
fig.savefig(out/'bernoulli-tower-model.svg',metadata={'Date':None,'Creator':'OA-CLASSIFY Writing AI; GPT-6.1 Sol Ultra; original CC0'})
fig.savefig(out/'bernoulli-tower-model.png',dpi=160,metadata={'Software':'OA-CLASSIFY Writing AI; GPT-6.1 Sol Ultra; original CC0'})
plt.close(fig)
