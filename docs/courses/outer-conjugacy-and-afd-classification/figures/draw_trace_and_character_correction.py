from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch
matplotlib.rcParams.update({'font.size':17,'svg.hashsalt':'oa-classify-trace-character-v1','font.family':'DejaVu Sans'})
fig,ax=plt.subplots(figsize=(6.5,9));ax.set(xlim=(0,6.5),ylim=(0,9));ax.axis('off')
ax.text(.3,8.55,'Two commuting corrections',fontsize=22,weight='bold')
ax.text(.3,7.9,r'$M=K\,\overline{\otimes}\,R_\infty$',fontsize=25)
for y,title,formula,detail,color in [(4.65,'Inner phases: on K',r'$D_{\chi^{-1}}(U_n)=\chi(n)^{-1}U_n$','Trace multiplier: 1\nCommutes with invariant isotropy action.','#e5f2ef'),(1.55,'Trace: on the second factor',r'$B_s=\mathrm{id}_K\otimes b_s$','s = log(c / r)\nTrace multiplier: exp(−s) = r / c.','#e9edf8')]:
 ax.add_patch(FancyBboxPatch((.25,y),6,2.7,boxstyle='round,pad=.04',facecolor=color,edgecolor='#465b70',linewidth=1.2))
 ax.text(.5,y+2.15,title,fontsize=20,weight='bold');ax.text(.5,y+1.35,formula,fontsize=22)
 ax.text(.5,y+.45,detail,fontsize=16,linespacing=1.6)
ax.text(.3,.85,r'$F=D_{\chi^{-1}}B_s,\quad\Theta=F\theta$',fontsize=22)
ax.text(.3,.22,'Exact normalization: Theorem 1.1 and (5.1).',fontsize=15)
fig.subplots_adjust(left=0,right=1,bottom=0,top=1);base=Path(__file__).with_name('trace-and-character-correction')
fig.savefig(base.with_suffix('.svg'),metadata={'Date':None,'Creator':'OA-CLASSIFY mathematical figure source'})
fig.savefig(base.with_suffix('.png'),dpi=160,metadata={'Software':'OA-CLASSIFY mathematical figure source'});plt.close(fig)
