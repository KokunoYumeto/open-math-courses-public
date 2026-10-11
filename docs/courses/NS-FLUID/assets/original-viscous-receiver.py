"""Full physical input moments and complete receiver energies; exact diagram."""
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch
root=Path(__file__).resolve().parent
fig=plt.figure(figsize=(14,9.5),facecolor='#f7fafc')
ax=fig.add_axes([0,0,1,1]);ax.set_xlim(0,1);ax.set_ylim(0,1);ax.axis('off')
ink='#16354b';blue='#16758c';orange='#b96120'
ax.text(.04,.953,'The actual input history controls the full viscous receiver',fontsize=21,fontweight='bold',color=ink)
ax.text(.04,.914,r'$\kappa_n=q^{5n/2},\quad S=\sqrt{1+\epsilon^2e^{-2K^{10}}},\quad\nu>0,\quad u(0)=\psi_{1,n_0}$',fontsize=17,color=ink)
def box(x,y,w,h):ax.add_patch(FancyBboxPatch((x,y),w,h,boxstyle='round,pad=0.012',fc='white',ec='#cad9e3'))
box(.04,.54,.43,.30);box(.51,.54,.44,.30)
ax.text(.06,.8,'Original physical input moments',fontsize=17,fontweight='bold',color=ink)
ax.text(.06,.734,r'$J_n(t)=\int_0^t a_n(s)^2\,ds$',fontsize=20,color=blue)
ax.text(.06,.668,r'$H_n(t)=\int_0^t(t-s)a_n(s)^2\,ds$',fontsize=20,color=blue)
ax.text(.06,.595,r'$P_n=\sqrt{2(E_{2,n}+E_{3,n})}\leq\kappa_n\epsilon S J_n$',fontsize=18,color=ink)
ax.text(.53,.8,'Every amplifier term cancels in the pair',fontsize=16,fontweight='bold',color=ink)
ax.text(.53,.736,r'$-\kappa_n\epsilon^{-1}K^{10}c_n^2b_n$',fontsize=18,color=ink)
ax.text(.53,.689,r'$+\kappa_n\epsilon^{-1}K^{10}b_nc_n^2=0$',fontsize=18,color=ink)
ax.text(.53,.619,r'$-\nu(\|\nabla u_{2,n}\|_2^2+\|\nabla u_{3,n}\|_2^2)\leq0$',fontsize=16,color=blue)
ax.text(.53,.566,'The bound retains both complete band fields.',fontsize=13,color=ink)
box(.04,.30,.91,.18)
ax.text(.06,.438,'The weak drive keeps its entire original exponential and past history',fontsize=17,fontweight='bold',color=ink)
ax.text(.06,.377,r'$0\leq c_n(t)\leq\kappa_n\epsilon^2e^{-K^{10}}J_n(t)\exp\left(\kappa_n^2K^{10}S H_n(t)\right)$',fontsize=23,color=orange)
ax.text(.06,.324,'VR8–VR11 use the exact positive heat response of the original band. The physical lower time endpoint remains zero.',fontsize=12,color=ink)
box(.04,.085,.91,.15)
ax.text(.06,.199,'First receiver: a constructed interval in the original physical clock',fontsize=17,fontweight='bold',color=ink)
ax.text(.06,.15,r'$n=n_0+1,\quad 0\leq t<T_{\rm rec}=\min\{T_*,100q^{-5n_0/2},t_J\},\quad\sqrt{2E_{4,n}(t)}\leq K^{-20}$',fontsize=18,color=ink)
ax.text(.06,.105,r'$K\geq\max\{10^{10},(400q^5\sqrt{2})^4\},\quad 0<\epsilon\leq1,\quad J_{n_0+1}(t_J)=q^{-5n_0/2}K^{-1/4}$',fontsize=15,color=ink)
ax.text(.04,.049,'Proof: ORIGINAL_VISCOUS_RECEIVER_BOUNDS_20261011.md, VR1–VR24. Human comparison: Terence Tao, arXiv:1402.0290v3,2039–2106.',fontsize=10,color='#445f73')
ax.text(.04,.023,'Exact proved bounds, not numerical samples. If the input threshold is never reached then t_J is infinite. The full transfer induction is proved in UI1-UI59.',fontsize=10,color='#445f73')
for ext in ['png','svg']:fig.savefig(root/f'original-viscous-receiver.{ext}',dpi=150,facecolor=fig.get_facecolor())
plt.close(fig)
