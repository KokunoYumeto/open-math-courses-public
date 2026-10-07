"""Original exact one-base embedding diagram, GPT-6.1 Sol, Ultra. CC0."""
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch

plt.rcParams.update({'font.family':'DejaVu Sans','font.size':20,'mathtext.fontset':'dejavusans'})
fig=plt.figure(figsize=(15.5,7.5),facecolor='white')
fig.text(.5,.955,'One base becomes two independent rational bases',ha='center',fontsize=25,weight='bold')
fig.text(.5,.88,r'Example: $a=8,\quad p=3,\quad c\in\{2,3,5\}$',ha='center',fontsize=23)
ax=fig.add_axes([0,0,1,1]);ax.set(xlim=(0,1),ylim=(0,1));ax.axis('off')
for x,prime,reason,color in [(.045,'2',r'Dependent: $8=2^3$','#fff1f2'),(.375,'3',r'Excluded: $c=p$','#fff1f2'),(.705,'5','Independent and a unit','#eff6ff')]:
    ax.add_patch(FancyBboxPatch((x,.66),.25,.15,boxstyle='round,pad=0.008',facecolor=color,edgecolor='#94a3b8',linewidth=1.4))
    ax.text(x+.125,.755,'$c='+prime+'$',ha='center',fontsize=24)
    ax.text(x+.125,.695,reason,ha='center',fontsize=20)
ax.annotate('',xy=(.69,.54),xytext=(.83,.65),arrowprops={'arrowstyle':'->','lw':2,'color':'#1d4ed8'})
ax.text(.5,.575,r'$(\alpha_1,\alpha_2)=\left(\frac{a}{c},\frac{1}{c}\right)$',ha='center',fontsize=27)
ax.text(.5,.485,r'$\alpha_1^u\alpha_2^v=a^u c^{-u-v},\qquad (u,v)\mapsto(u,-u-v)$',ha='center',fontsize=25)
ax.text(.5,.405,r'$h(\alpha_1)\leq\ln(5a),\qquad h(\alpha_2)\leq\ln5$',ha='center',fontsize=24)
ax.add_patch(FancyBboxPatch((.08,.185),.84,.18,boxstyle='round,pad=0.012',facecolor='#f8fafc',edgecolor='#94a3b8'))
ax.text(.5,.295,r'$\alpha_1^{p-1}-\alpha_2^{p-1}=c^{-(p-1)}(a^{p-1}-1)$',ha='center',fontsize=26)
ax.text(.5,.235,r'$\left(\frac{8}{5}\right)^2-\left(\frac{1}{5}\right)^2=\frac{63}{25},\qquad v_3=2$',ha='center',fontsize=24)
fig.text(.5,.12,'At most one candidate is dependent; at most one equals p. One always remains.',ha='center',fontsize=21,color='#334155')
fig.text(.5,.055,'Corollaries 10.9–10.10: the same 250000 constant, now also when b = 1.',ha='center',fontsize=20,color='#475569')
folder=Path(__file__).resolve().parent
destination=folder.parent/'figures/one-base-embedding.png' if folder.name=='figure_sources' else folder/'one-base-embedding.png'
destination.parent.mkdir(exist_ok=True)
fig.savefig(destination,dpi=180,bbox_inches='tight')
print(destination)
