from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Ellipse
p=Path(__file__).resolve().parent
fig=plt.figure(figsize=(12,8.5),facecolor='#f4f8fb')
gs=fig.add_gridspec(2,2,height_ratios=[.65,1],hspace=.38,wspace=.28)
a=fig.add_subplot(gs[0,:]);a.axis('off')
a.text(0,1.07,'The symbol that survives every compact perturbation',fontsize=20,weight='bold',color='#172b3c')
a.text(.02,.77,r'$\|A\|_{\rm ess}^{\,2}=\|A^*A\|_{\rm ess}=\lim_{R\to\infty}\sup_{|\eta|\geq R}\|b\|^2$',fontsize=22,color='#14546b')
a.text(.02,.5,'Upper bound: positive matrix factor + compact error + finite-dimensional removal.',fontsize=12,color='#172b3c')
a.text(.02,.32,'Lower bound: shrinking packets are weakly zero; compact operators send them to zero.',fontsize=12,color='#172b3c')
a.text(.02,.14,'Local branches: a filter in log(|xi| / |eta|) separates relative frequency magnitudes.',fontsize=12,color='#172b3c')
b=fig.add_subplot(gs[1,0]);b.set_facecolor('white')
for R,color in [(16,'#148798'),(64,'#bd5d2b')]:
 h=R**-.5
 b.add_patch(Ellipse((0,R),width=2*h,height=2/h,facecolor=color,alpha=.22,edgecolor=color,lw=2))
 b.plot([0],[R],'o',color=color)
 b.annotate(f'R = {R}\nh = {h:.3f}',(.02,R),xytext=(.22,R+4),fontsize=11,color=color)
b.set(xlim=(-.55,.55),ylim=(0,85),xlabel='x - x₀',ylabel='frequency ξ',title='Packet scales in T3 (schematic)')
b.text(.02,.03,'Spatial width ~ R⁻¹ᐟ²; frequency width ~ R¹ᐟ².\nEllipses are scale guides, not support boundaries.',transform=b.transAxes,fontsize=9,color='#425c6d')
c=fig.add_subplot(gs[1,1]);c.set_facecolor('white')
t=np.linspace(0,20,1200)
c.plot(t,1/np.log(np.e+np.exp(t)),color='#148798',lw=2.5,label='1 / log(e + ⟨ξ⟩): tends to zero')
c.plot(t,np.sin(t),color='#bd5d2b',lw=1.8,label='sin(log⟨ξ⟩): |q| returns to one')
c.axhline(0,color='#a7b6c1',lw=.8)
c.set(xlabel='log⟨ξ⟩',ylabel='symbol coefficient q(ξ)',title='Actual symbols in Examples T1–T2',ylim=(-1.15,1.15))
c.legend(loc='lower left',fontsize=9)
for ax in [b,c]:
 ax.spines[['top','right']].set_visible(False);ax.grid(alpha=.15)
fig.text(.08,.015,'Exact statements and proofs: T1–T7. The numerical essential-norm formula requires one canonical graph.',fontsize=11,color='#425c6d')
fig.savefig(p/'fio-compactness.svg',bbox_inches='tight');fig.savefig(p/'fio-compactness.png',dpi=130,bbox_inches='tight');plt.close(fig)
