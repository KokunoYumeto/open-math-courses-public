"""Draw the exact orthogonal heat remainder and retained viscous receiver bounds."""
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch
R=Path(__file__).resolve().parent
plt.rcParams.update({'font.family':'DejaVu Sans','font.size':13,'mathtext.fontset':'dejavusans'})
fig=plt.figure(figsize=(15,10),facecolor='#f6f8fb')
ax=fig.add_axes([.06,.53,.88,.36]);ax.set(xlim=(0,1),ylim=(0,1));ax.axis('off')
fig.text(.06,.955,'The full heat field retains a positive future contribution',fontsize=24,weight='bold',color='#16334c')
ax.text(0,1.03,r'1   Projecting at time $s$ leaves an exact orthogonal field',fontsize=17,weight='bold')
for xx,title,formula in [
 (.01,'Full field',r'$e^{\nu s\Delta}\psi_{i,n}$'),
 (.37,'Packet projection',r'$R(s)\psi_{i,n}$'),
 (.72,'Orthogonal field',r'$h_s=Q_{i,n}e^{\nu s\Delta}\psi_{i,n}$')]:
 ax.add_patch(FancyBboxPatch((xx,.59),.26,.29,boxstyle='round,pad=.008',facecolor='white',edgecolor='#7892a5'))
 ax.text(xx+.13,.79,title,ha='center',fontsize=14)
 ax.text(xx+.13,.66,formula,ha='center',fontsize=15 if xx<.7 else 13)
ax.text(.315,.7,'=',ha='center',fontsize=22);ax.text(.675,.7,'+',ha='center',fontsize=22)
ax.text(.015,.39,r'$\langle e^{\nu r\Delta}h_s,\psi_{i,n}\rangle=R(r+s)-R(r)R(s)>0\quad(r,s>0)$',fontsize=20,color='#136e83')
ax.text(.015,.18,r'$R(t)=\int e^{-\nu t\lambda}\,d\mu_{i,n}(\lambda),\qquad \lambda=4\pi^2|\xi|^2$',fontsize=18)
ax.text(.015,-.025,'The original Fourier mass is one and is not concentrated at one radius. The exact covariance proves strict positivity.',fontsize=13,color='#465b70')
ax=fig.add_axes([.06,.08,.88,.33]);ax.set(xlim=(0,1),ylim=(0,1));ax.axis('off')
ax.text(0,1.09,'2   The same original viscosity sharpens the full receiver bounds',fontsize=17,weight='bold')
ax.text(.015,.86,r'$\gamma_n=4\pi^2\nu q^{2n},\qquad J_n^\nu(t)=\int_0^t e^{-\gamma_n(t-s)}a_n(s)^2\,ds$',fontsize=19)
ax.text(.015,.59,r'$P_n(t)\leq\kappa_n\epsilon S J_n^\nu(t),\qquad H_n^\nu(t)=\int_0^tJ_n^\nu(s)\,ds$',fontsize=20,color='#136e83')
ax.text(.015,.31,r'$c_n(t)\leq\kappa_n\epsilon^2e^{-K^{10}}J_n^\nu(t)\exp\!\left(\kappa_n^2K^{10}S H_n^\nu(t)\right)$',fontsize=19,color='#8b4b23')
ax.text(.015,.055,r'$J_n^\nu\leq J_n,\qquad H_n^\nu\leq H_n.$  All integrals start at original physical time zero.',fontsize=15)
fig.text(.06,.02,'Exact identities and bounds, not a numerical solution. Proof: Exercise 4, EX12-EX16; Exercise 5, EX17-EX22.',fontsize=11,color='#465b70')
fig.savefig(R/'positive-heat-remainder-and-viscous-receiver.png',dpi=150,facecolor=fig.get_facecolor())
fig.savefig(R/'positive-heat-remainder-and-viscous-receiver.svg',facecolor=fig.get_facecolor());plt.close(fig)

