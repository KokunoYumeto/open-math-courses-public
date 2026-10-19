"""Exact arrow exchange and ordered unitary products, equations (6.5)–(6.7)."""
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrowPatch
plt.rcParams['svg.hashsalt']='oa-classify-mixed-isotropy-covariance-v1'
out=Path(__file__).resolve().parent
fig,ax=plt.subplots(figsize=(6.5,9.8));fig.patch.set_facecolor('#fbfcff')
ax.set(xlim=(0,6.5),ylim=(0,9.8));ax.axis('off')
def text(x,y,s,size=19):ax.text(x,y,s,ha='center',va='center',fontsize=size,color='#17304b')
def arrow(a,b):ax.add_patch(FancyArrowPatch(a,b,arrowstyle='-|>',mutation_scale=20,color='#476ea1',linewidth=2.4))
text(3.25,9.2,'Exchange isotropy and motion',22)
text(1.1,7.9,r'$y$',26);text(5.4,7.9,r'$x$',26)
text(1.1,5.55,r'$y$',26);text(5.4,5.55,r'$x$',26)
arrow((1.5,7.9),(5,7.9));text(3.25,8.25,r'$k$',24)
arrow((1.5,5.55),(5,5.55));text(3.25,5.2,r'$k$',24)
arrow((1.1,7.5),(1.1,5.95));text(.63,6.73,r'$j$',24)
arrow((5.4,7.5),(5.4,5.95));text(5.94,6.73,r'$m$',24)
text(3.25,6.75,r'$m=kjk^{-1}$',22)
text(3.25,4.28,r'$kj=mk$',24)
text(3.25,3.32,'Ordered products in the fibre at x',17)
text(3.25,2.7,r'$W_k\beta_k(v_j^{\prime})$',25)
text(3.25,2.14,r'$=$',23)
text(3.25,1.58,r'$v_m^{\prime}\beta_m(W_k)$',25)
text(3.25,.6,'Exact mixed covariance: equation (6.5)',16)
fig.subplots_adjust(left=0,right=1,top=1,bottom=0)
fig.savefig(out/'mixed-isotropy-covariance.svg',metadata={'Date':None,'Creator':'OA-CLASSIFY Writing AI; GPT-6.1 Sol Ultra; original CC0'})
fig.savefig(out/'mixed-isotropy-covariance.png',dpi=180,metadata={'Software':'OA-CLASSIFY Writing AI; GPT-6.1 Sol Ultra; original CC0'})
plt.close(fig)
