from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrowPatch, FancyBboxPatch
B=Path(__file__).resolve().parents[4]
out=Path(__file__).resolve().parent
out.mkdir(parents=True,exist_ok=True)
plt.rcParams.update({'font.family':'DejaVu Sans','font.size':11})
fig,ax=plt.subplots(figsize=(13.5,6.2))
fig.patch.set_facecolor('#f8fafc');ax.set_facecolor('#f8fafc')
ax.set_xlim(0,13.5);ax.set_ylim(0,6.2);ax.axis('off')
def box(x,y,w,h,label,sub,color):
 p=FancyBboxPatch((x,y),w,h,boxstyle='round,pad=0.12,rounding_size=0.14',facecolor=color,edgecolor='#334155',linewidth=1.2)
 ax.add_patch(p)
 ax.text(x+w/2,y+h*0.68,label,ha='center',va='center',fontsize=12,weight='bold',color='#0f172a')
 ax.text(x+w/2,y+h*0.33,sub,ha='center',va='center',fontsize=10,color='#334155')
def arrow(x1,y1,x2,y2):
 ax.add_patch(FancyArrowPatch((x1,y1),(x2,y2),arrowstyle='-|>',mutation_scale=15,linewidth=1.5,color='#475569'))
ax.text(0.25,5.75,'Actual first patched inverse: common normal tails and ordered correction',fontsize=15,weight='bold',color='#0f172a')
box(0.3,3.8,3.2,1.25,'Local raw inverse $T_i$','$p_i=M_i\\kappa^m(I+Z_i)$','#dbeafe')
box(4.15,4.35,3.8,1.1,'Positive real tail','$\\kappa>0,\\;|\\kappa|\\geq C_iT$','#dcfce7')
box(4.15,2.95,3.8,1.1,'Negative real tail','$\\kappa<0,\\;|\\kappa|\\geq C_iT$','#dcfce7')
box(8.65,3.7,4.15,1.45,'One coefficient sequence','$c_{in}=U_{in}M_i^{-1}$ on both tails','#fef3c7')
arrow(3.55,4.65,4.02,4.75);arrow(3.55,4.2,4.02,3.65)
arrow(8.0,4.85,8.52,4.65);arrow(8.0,3.5,8.52,4.1)
box(0.45,0.75,4.25,1.3,'Separated tangential kernel','$y\\ne z$: integrate by parts in $\\eta$','#ede9fe')
box(5.25,0.75,3.35,1.3,'Actual finite patch','$Q=\\sum_i\\vartheta_iT_i\\vartheta_i$','#dbeafe')
box(9.15,0.75,3.75,1.3,'First corrected coefficient','$Q_2$: $C_1=-M^{-1}A_{m-1}M^{-1}-m\\delta M^{-1}$','#fee2e2')
arrow(2.65,3.68,2.65,2.2);arrow(6.2,2.8,6.2,2.2);arrow(10.7,3.55,10.7,2.2)
arrow(4.85,1.4,5.1,1.4);arrow(8.75,1.4,9.0,1.4)
ax.text(0.45,0.3,r'The diagram states AL1–AL18. It does not assert all-length closure for $Q\mathcal{R}_F^j$ or a general one-sided trace.',fontsize=9.8,color='#475569')
fig.tight_layout(pad=0.4)
fig.savefig(out/'normal_laurent_actual_first_patch.png',dpi=180,bbox_inches='tight')
fig.savefig(out/'normal_laurent_actual_first_patch.svg',bbox_inches='tight')
print(out/'normal_laurent_actual_first_patch.png')

