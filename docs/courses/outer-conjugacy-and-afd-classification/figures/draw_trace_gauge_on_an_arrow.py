from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch
matplotlib.rcParams.update({'font.size':17,'svg.hashsalt':'oa-classify-trace-arrow-v1','font.family':'DejaVu Sans'})
fig,ax=plt.subplots(figsize=(6.5,8.6));ax.set(xlim=(0,6.5),ylim=(0,8.6));ax.axis('off')
ax.text(.3,8.15,'Trace gauge on an arrow',fontsize=23,weight='bold')
ax.text(.3,7.5,r'$\gamma:y\longrightarrow x$',fontsize=25)
for y,title,formula,color in [(5.0,'Source: inverse comparison',r'$\tau\Theta_y^{-1}=r_y^{-1}\tau$','#e9edf8'),(2.7,'Range: comparison',r'$\tau\Theta_x=r_x\tau$','#e5f2ef')]:
 ax.add_patch(FancyBboxPatch((.25,y),6,1.8,boxstyle='round,pad=.04',facecolor=color,edgecolor='#465b70',linewidth=1.2))
 ax.text(.5,y+1.23,title,fontsize=20,weight='bold');ax.text(.5,y+.55,formula,fontsize=24)
ax.text(.3,2.0,r'$\tau(\Theta_x\alpha_\gamma\Theta_y^{-1})$',fontsize=23)
ax.text(.3,1.25,r'$=\frac{r_x}{r_y}\,d^\alpha_\gamma\,\tau$',fontsize=24)
ax.text(.3,.47,'Example: rₓ = 6, rᵧ = 1, original multiplier = 1.\nCorrected multiplier = 6. Equation (6.4).',fontsize=16,linespacing=1.6)
fig.subplots_adjust(left=0,right=1,bottom=0,top=1);base=Path(__file__).with_name('trace-gauge-on-an-arrow')
fig.savefig(base.with_suffix('.svg'),metadata={'Date':None,'Creator':'OA-CLASSIFY mathematical figure source'})
fig.savefig(base.with_suffix('.png'),dpi=160,metadata={'Software':'OA-CLASSIFY mathematical figure source'});plt.close(fig)
