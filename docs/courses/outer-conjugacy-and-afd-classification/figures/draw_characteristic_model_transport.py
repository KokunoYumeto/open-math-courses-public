from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch
matplotlib.rcParams.update({'font.size':17,'svg.hashsalt':'oa-classify-characteristic-model-v1','font.family':'DejaVu Sans'})
fig,ax=plt.subplots(figsize=(6.5,9));ax.set(xlim=(0,6.5),ylim=(0,9));ax.axis('off')
ax.text(.3,8.6,'Transport in the model',fontsize=24,weight='bold')
ax.text(.3,8.05,r'$\gamma=h k_{xy}:y\longrightarrow x$',fontsize=23)
for y,title,formula,detail,color in [(4.8,'Bernoulli sites',r'$(t,j)\longmapsto(h k_{xy}t k_{xy}^{-1},j)$','Left translation by h after conjugation by k.','#e5f2ef'),(1.7,'Inner unitaries',r'$U_n^y\longmapsto\lambda(n,\gamma)U^x_{\gamma n\gamma^{-1}}$','Conjugation of n, with its actual scalar phase.','#e9edf8')]:
 ax.add_patch(FancyBboxPatch((.25,y),6,2.6,boxstyle='round,pad=.04',facecolor=color,edgecolor='#465b70',linewidth=1.2))
 ax.text(.5,y+2.08,title,fontsize=21,weight='bold')
 ax.text(.5,y+1.25,formula,fontsize=21)
 ax.text(.5,y+.45,detail,fontsize=15)
ax.text(.3,.95,'Covariance: the first map sends left n-action\nto left action by γnγ⁻¹.',fontsize=17,linespacing=1.5)
ax.text(.3,.25,'Exact maps: equation (7.3) and Exercise 8.8.',fontsize=15)
fig.subplots_adjust(left=0,right=1,bottom=0,top=1)
base=Path(__file__).with_name('characteristic-model-transport')
fig.savefig(base.with_suffix('.svg'),metadata={'Date':None,'Creator':'OA-CLASSIFY mathematical figure source'})
fig.savefig(base.with_suffix('.png'),dpi=160,metadata={'Software':'OA-CLASSIFY mathematical figure source'})
plt.close(fig)
