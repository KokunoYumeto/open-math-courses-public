"""Exact Kummer component spans and distinct local valuations. CC0."""
from pathlib import Path
import json
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from fractional_value_certificate import certificate

data=certificate();plt.rcParams.update({'font.family':'DejaVu Sans','font.size':11})
fig,axes=plt.subplots(1,4,figsize=(15,4.8),gridspec_kw={'width_ratios':[1,1,1,1.7]})
names=[r'$U_1U_2$',r'$1+U_1$',r'$2-U_1-U_2$']
for ax,example,name in zip(axes[:3],data['examples'],names):
    ax.scatter([0,1,0,1],[0,0,1,1],s=60,color='#d6dee6',zorder=1)
    points=example['vectors'];ax.scatter([p[0] for p in points],[p[1] for p in points],s=130,color='#267ca1',zorder=3)
    for a,b in [(0,0),(1,0),(0,1),(1,1)]:ax.text(a,b+.13,f'({a},{b})',ha='center',fontsize=10)
    ax.set(xlim=(-.3,1.3),ylim=(-.35,1.45),xticks=[],yticks=[])
    ax.set_title(name+'\n'+f"span rank {example['rank']}; degree {example['degree']}")
    for spine in ax.spines.values():spine.set_visible(False)
    ax.text(.5,-.23,r'Residues in $\mathbb{F}_2^2$',ha='center',fontsize=10)
ax=axes[3];values=data['valuations'];positions=list(range(4))
ax.bar(positions,values,color=['#c37d2d','#267ca1','#267ca1','#267ca1'],width=.6)
for i,v in enumerate(values):ax.text(i,v+.035,str(v),ha='center')
ax.set(xticks=positions,xticklabels=['(+,+)','(-,+)','(+,-)','(-,-)'],ylim=(0,1.38),yticks=[0,1],ylabel=r'$v_{73}(2-U_1-U_2)$',xlabel='Signs of the two roots')
ax.set_title('Four embeddings; exact valuations')
ax.annotate('Selected principal roots',xy=(0,1),xytext=(.45,1.25),arrowprops={'arrowstyle':'->','color':'#c37d2d'},fontsize=9)
for spine in ['top','right']:ax.spines[spine].set_visible(False)
fig.suptitle('The surviving components determine the arithmetic field',fontsize=17,fontweight='bold')
fig.text(.5,.025,r'$U_1^2=74,\ U_2^2=147,\ U_1\equiv U_2\equiv1\ (\mathrm{mod}\ 73)$'+'\nNorm = 3577 = 49 × 73; sum of the four valuations = 1.',ha='center',fontsize=11)
fig.subplots_adjust(top=.72,bottom=.28,wspace=.34,left=.02,right=.98)
out=Path(__file__).resolve().parent/'fractional-value-components.png';fig.savefig(out,dpi=150,bbox_inches='tight');plt.close(fig)
print(json.dumps({'figure':str(out),'state':'exact_figure_written'}))
