"""Original corrected energy and exact scalar integrating-factor example."""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch
P=Path(__file__).resolve().parent
fig=plt.figure(figsize=(14,10),facecolor='#f7fafc')
canvas=fig.add_axes([0,0,1,1]);canvas.set_xlim(0,1);canvas.set_ylim(0,1);canvas.axis('off')
ink='#16354b';blue='#16758c';orange='#b96120'
canvas.text(.045,.954,'The signed corrector and the input integral it must control',fontsize=21,fontweight='bold',color=ink)
canvas.add_patch(FancyBboxPatch((.045,.729),.91,.16,boxstyle='round,pad=0.012',fc='white',ec='#cad9e3'))
canvas.text(.062,.849,r'$M_n=a_nd_n(\epsilon^2/c_n)a_{n+1},\quad\lambda_n=q^{5n/2}q^{5/2}K,\quad\kappa_n=q^{5n/2}$',fontsize=19,color=ink)
canvas.text(.062,.789,r'$\mathcal{E}_n^*=E_{1,n}+E_{4,n}-\frac{\lambda_n}{2\kappa_n}M_n,\qquad (\mathcal{E}_n^*)^{\prime}=-\lambda_n a_{n+1}\mathcal{E}_n^*+\mathcal{F}_n$',fontsize=23,color=blue)
canvas.text(.062,.74,'RC7–RC11 keep the full original viscosity, both adjacent scales and the orthogonal diffusion defect.',fontsize=13,color=ink)
canvas.text(.05,.669,'A scalar inference test: K = 1024; every plotted value follows the exact formulas RC19–RC22',fontsize=16,fontweight='bold',color=ink)
K=1024.;delta=K**-.5;T=.5+delta
r=np.linspace(.5,T,501);theta=(r-.5)/delta
total=.5+delta*(theta-2*theta**3/3)
tail=delta*(1/3-theta+2*theta**3/3)
ax1=fig.add_axes([.08,.315,.38,.29]);ax2=fig.add_axes([.575,.315,.36,.29])
ax1.plot(r,total,color=blue,lw=2.6);ax1.axhline(.5,color=ink,ls='--',lw=1)
ax1.axvspan(.5+delta/np.sqrt(2),T,color=orange,alpha=.12)
ax1.set_title('The total input integral stays positive',fontsize=14,pad=12,color=ink)
ax1.set_xlabel('Original time t',fontsize=12);ax1.set_ylabel(r'$\int_0^t z_K(s)\,ds$',fontsize=15)
ax1.set_ylim(.498,.518);ax1.ticklabel_format(useOffset=False,axis='both');ax1.grid(alpha=.16)
ax1.text(.502,.4986,'Lower bound: 1/2',fontsize=11,color=ink)
kernel=np.exp(-K*tail);lo=.5+3*delta/4;hi=.5+7*delta/8;lower=np.exp(73*np.sqrt(K)/768)
ax2.plot(r,kernel,color=orange,lw=2.6);ax2.axvspan(lo,hi,color=orange,alpha=.15)
ax2.hlines(lower,lo,hi,color=ink,ls='--',lw=1.4)
ax2.set_title('Short subintervals amplify the forcing',fontsize=14,pad=12,color=ink)
ax2.set_xlabel('Original source time r',fontsize=12);ax2.set_ylabel(r'$\exp(-K\int_r^T z_K(s)\,ds)$',fontsize=15)
ax2.ticklabel_format(useOffset=False,axis='x');ax2.grid(alpha=.16)
canvas.text(.055,.245,r'$y_K^{\prime}=-Kz_Ky_K+K^{-14},\quad y_K(0)=0,\quad y_K(T)\geq\frac{1}{8} K^{-29/2}\exp\left(\frac{73}{768}\sqrt{K}\right)$',fontsize=21,color=orange)
canvas.text(.055,.181,'The positive total integral alone does not bound the forced energy by a constant times K to power minus14.',fontsize=14,color=ink)
canvas.text(.055,.143,'For the actual cascade, RC13–RC18 calculate each signed subinterval integral from its original rotor equation.',fontsize=14,color=ink)
canvas.text(.045,.091,'The curves are samples of exact scalar functions. They are not cascade trajectories or a counterexample to the main theorem.',fontsize=12,color=ink)
canvas.text(.045,.058,'Proof: ORIGINAL_VISCOUS_ROTATION_CORRECTORS_20261011.md, RC1–RC24. Human comparison: Tao, arXiv:1402.0290v3,2405–2539.',fontsize=10.5,color='#445f73')
canvas.text(.045,.032,'The complete corrected-energy forcing and the exact input primitive remain in the accompanying proof. No scalar damping replaces viscosity.',fontsize=11,color='#445f73')
for ext in ['png','svg']:fig.savefig(P/f'original-viscous-rotation-correctors.{ext}',dpi=150,facecolor=fig.get_facecolor())
plt.close(fig)
