from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrowPatch,FancyBboxPatch
dest=Path(__file__).resolve().parent
dest.mkdir(parents=True,exist_ok=True)
plt.rcParams.update({'svg.hashsalt':'oa-classify-continuous-return-55','font.family':'DejaVu Sans','font.size':14})
fig,ax=plt.subplots(figsize=(6,8.5));fig.subplots_adjust(left=.03,right=.97,bottom=.03,top=.97)
ax.set_xlim(0,9);ax.set_ylim(0,9);ax.axis('off')
def text(x,y,s,size=14):ax.text(x,y,s,ha='center',va='center',fontsize=size,color='#173647')
def arrow(x,y,a,b):ax.add_patch(FancyArrowPatch((x,y),(a,b),arrowstyle='->',mutation_scale=18,linewidth=1.7,color='#315c71'))
ax.add_patch(FancyBboxPatch((.15,3.3),8.7,4.6,boxstyle='round,pad=.08',facecolor='#edf5fc',edgecolor='#315c71'))
text(4.5,8.6,'An exact return arrow\nretains both group labels',18)
text(1.65,7.15,r'$x=(z,u)$',18);text(7.3,7.15,r'$y=(w,v)$',18)
text(1.65,4.2,r'$j(z)=(z,0)$',18);text(7.3,4.2,r'$j(w)=(w,0)$',18)
arrow(2.8,7.15,6.1,7.15);text(4.5,7.55,r'$g=(m,t)$',17)
arrow(1.65,4.75,1.65,6.6);text(.78,5.7,r'$v_x$',17);text(2.5,5.7,r'$(0,u)$',16)
arrow(7.3,4.75,7.3,6.6);text(8.18,5.7,r'$v_y$',17);text(6.35,5.7,r'$(0,v)$',16)
arrow(2.8,4.2,6.1,4.2);text(4.5,4.65,r'$\bar g=(m,t+u-v)$',16)
text(4.5,3.65,r'$g=v_y\bar g v_x^{-1}$',17)
text(4.5,2.83,'Compare at height zero,\nthen transport to the range',17)
text(4.5,2.23,r'$P_x=\beta_{v_x}p_z\alpha_{v_x}^{-1}$',18)
text(4.5,1.65,r'$W(g,x)=\beta_{v_y}(w_{\bar g})$',18)
text(4.5,.94,r'$\overline{fg}=\bar f\bar g$',17)
text(4.5,.43,r'$W(f,y)\beta_f(W(g,x))=W(fg,x)$',17)
fig.savefig(dest/'continuous-return-reconstruction.svg',metadata={'Date':None})
fig.savefig(dest/'continuous-return-reconstruction.png',dpi=160,metadata={'Software':'OA-CLASSIFY original figure source'})
plt.close(fig)
