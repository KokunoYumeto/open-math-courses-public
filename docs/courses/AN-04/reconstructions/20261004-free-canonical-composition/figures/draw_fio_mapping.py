from pathlib import Path
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch
p=Path(__file__).resolve().parent
fig,ax=plt.subplots(figsize=(12,8)); fig.patch.set_facecolor('#f4f8fb');ax.set(xlim=(0,12),ylim=(0,8));ax.axis('off')
ax.text(.45,7.55,'Canonical rank determines a sufficient Sobolev loss',fontsize=20,weight='bold',color='#172b3c')
boxes=[(.45,4.5,5.3,2.5,'1. Rank at the selected point',r'$R=\operatorname{rank} B,\quad r=R-N$'+'\n'+r'$\operatorname{rank}d\pi_X=n_X+r$'+'\n'+r'$\operatorname{rank}d\pi_Y=n_Y+r$'+'\n'+'Base submersions keep fibre radicals zero.'),
(6.25,4.5,5.3,2.5,'2. Graph slices',r'$x=(x^\prime,a),\quad y=(y^\prime,b)$'+'\n'+r'$\dim x^\prime=\dim y^\prime=r$'+'\n'+r'$c=n_X+n_Y-2r$'+'\n'+'The graph determinant stays nonzero.'),
(.45,1.35,5.3,2.5,'3. Order and parameter integration',r'$m_{a,b}=m+c/4$'+'\n'+r'$m\leq-\delta_k,\quad r\geq k\ \Longrightarrow\ m_{a,b}\leq0$'+'\n'+r'$\|Af\|_2\leq M\sqrt{|E||F|}\,\|f\|_2$'),
(6.25,1.35,5.3,2.5,'4. All real Sobolev orders',r'$\delta_k=(n_X+n_Y-2k)/4$'+'\n'+r'$Q_X^t A P_Y^{-s}\in I^{-\delta_k}$'+'\n'+r'$t=s-m-\delta_k$'+'\n'+r'$A:H^s_{\rm comp}\longrightarrow H^t_{\rm loc}$')]
for x,y,w,h,title,body in boxes:
 ax.add_patch(FancyBboxPatch((x,y),w,h,boxstyle='round,pad=0.08',edgecolor='#2b7688',facecolor='white',linewidth=1.4))
 ax.text(x+.18,y+h-.38,title,fontsize=14,weight='bold',color='#14546b')
 ax.text(x+.18,y+h-.8,body,fontsize=13,va='top',linespacing=1.65,color='#172b3c')
for x1,y1,x2,y2 in [(5.85,5.7,6.1,5.7),(9,4.4,3.1,4.0),(5.85,2.5,6.1,2.5)]:
 ax.annotate('',xy=(x2,y2),xytext=(x1,y1),arrowprops=dict(arrowstyle='->',color='#2b7688',lw=2))
ax.text(.45,.65,'Example: nX = nY = 2, r = k = 1 gives c = 2 and delta = 1/2.',fontsize=13,color='#172b3c')
ax.text(.45,.25,'Proofs W2–W6; example W1. A sufficient local estimate; no constant-rank hypothesis.',fontsize=11,color='#425c6d')
fig.savefig(p/'fio-mapping.svg',bbox_inches='tight');fig.savefig(p/'fio-mapping.png',dpi=130,bbox_inches='tight');plt.close(fig)
