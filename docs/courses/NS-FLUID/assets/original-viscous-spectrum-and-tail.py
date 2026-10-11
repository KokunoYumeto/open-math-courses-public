"""Reproducible spectral diagram and physical counterexample profiles.

The profile is exactly EX13. The numerical evaluation uses its Euler integral:
integral_0^infty t^alpha(nu+t)^(-5/2) exp(-rho^2/(4(nu+t)))dt
= nu^(alpha-3/2) B(3/2-alpha,1+alpha)
  * M(3/2-alpha,5/2,-rho^2/(4nu)).
This follows by y=nu/(nu+t), retaining both endpoints. M is the
confluent hypergeometric function evaluated by scipy.special.hyp1f1.
The equality also follows by integrating its exponential series termwise
against the finite Beta weight. The plotted values are numerical evaluations,
not interval-certified enclosures or computed eigenvalues of the ring.
"""
from pathlib import Path
import json
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import Circle,Rectangle
from scipy.special import gamma,hyp1f1
OUT=Path(__file__).resolve().parent
plt.rcParams.update({'font.family':'DejaVu Sans','font.size':12,'axes.spines.top':False,'axes.spines.right':False})
colors=['#17365D','#007E87','#BB641B','#784690'];nu=.7;c=1.;alphas=[-.25,0.,.125,.2]
r=np.geomspace(.02,1000,180);samples=[]
fig,axs=plt.subplots(1,2,figsize=(14,6),layout='constrained')
for alpha,col in zip(alphas,colors):
 pref=c*nu**(alpha-1.5)*gamma(1.5-alpha)/(2*(4*np.pi)**1.5*gamma(2.5))
 om=pref*r*hyp1f1(1.5-alpha,2.5,-r*r/(4*nu))
 lead=c*4**(-alpha)*gamma(1.5-alpha)/(2*np.pi**1.5*gamma(1+alpha))
 asym=lead*r**(2*alpha-2)
 axs[0].loglog(r,om,color=col,lw=2,label=rf'$\alpha={alpha:g}$')
 sel=r>=4;axs[0].loglog(r[sel],asym[sel],color='#333333',ls='--',lw=1.1,alpha=.65)
 axs[1].loglog(r,np.pi**2*r*r*abs(om),color=col,lw=2)
 axs[1].loglog(r[sel],np.pi**2*r[sel]**2*abs(asym[sel]),color='#333333',ls='--',lw=1.1,alpha=.65)
 samples.extend({'alpha':alpha,'rho':float(rr),'omega_theta_equator':float(v),'l1_shell_density':float(np.pi**2*rr*rr*abs(v)),'leading_equatorial_coefficient':float(lead)} for rr,v in zip(r,om))
axs[0].set(xlabel=r'Original radius $\rho=|x|$',ylabel=r'$\Omega^\theta_{\alpha,c}(\rho,0)$',title='Actual smooth field, including its spatial tail')
axs[1].set(xlabel=r'Original radius $\rho=|x|$',ylabel=r'Full shell density $\pi^2\rho^2|\Omega^\theta(\rho,0)|$',title='The complete physical L1 volume contribution')
axs[0].legend(frameon=False)
axs[1].text(.03,.96,'All four shell integrals diverge at infinity (EX15).',transform=axs[1].transAxes,fontsize=10,va='top',bbox={'facecolor':'white','alpha':.9,'edgecolor':'none'})
for ax in axs:ax.grid(alpha=.18,which='both')
fig.suptitle('Square-integrable vorticity with a nonintegrable physical tail',fontsize=17)
fig.supxlabel(r'$\nu=0.7$, $c=1$. Solid: numerical evaluation of EX13. Dashed: proved leading term EX15. No ring spectrum is computed.',fontsize=11)
for ext in ['png','svg']:fig.savefig(OUT/('original-vorticity-endpoint-tail.'+ext),dpi=160)
plt.close(fig)
(OUT/'original-vorticity-tail-data.json').write_text(json.dumps({'nu':nu,'c':c,'sample_count':len(samples),'samples':samples,'method':'Numerical evaluation of the exact physical integral EX13 through its Euler-integral hypergeometric expression; EX15 supplies the proved leading coefficient.'},indent=2)+'\n',encoding='utf8')
fig,ax=plt.subplots(figsize=(14,8));ax.set(xlim=(0,14),ylim=(0,8));ax.axis('off');ax.set_aspect('equal')
ax.add_patch(Rectangle((1,2),2,4.7,color='#ECE8F2',alpha=.8))
ax.plot([3,3],[2,6.7],color=colors[3],ls='--',lw=1.8)
ax.annotate('',xy=(10.5,2),xytext=(1,2),arrowprops={'arrowstyle':'->','lw':1.5,'color':colors[0]})
ax.annotate('',xy=(1,6.9),xytext=(1,2),arrowprops={'arrowstyle':'->','lw':1.5,'color':colors[0]})
ax.text(10.6,1.85,r'$\operatorname{Re}\lambda$',fontsize=13);ax.text(.4,7,r'$\operatorname{Im}\lambda$',fontsize=13)
center=(6.8,4.4);radius=1.3
ax.add_patch(Circle(center,radius,fill=False,color=colors[1],lw=2.2))
ax.scatter([center[0]],[center[1]],color=colors[0],s=42);ax.text(6.3,5.05,r'Actual Euler $\lambda_\infty$',fontsize=12)
ax.scatter([6.4],[4.02],color=colors[2],s=52);ax.text(6.5,3.68,r'An enclosed $\lambda_\beta$',fontsize=12)
ax.plot([center[0],center[0]+radius],[center[1],center[1]],color=colors[1],lw=1.4);ax.text(7.42,4.54,r'$\rho$',fontsize=13)
ax.text(8.25,5.5,r'$\Gamma$ lies in the proved resolvent set',fontsize=12,color=colors[1])
ax.annotate('',xy=(5.5,2.65),xytext=(3,2.65),arrowprops={'arrowstyle':'<->','lw':1.4,'color':colors[0]})
ax.text(4.25,2.96,r'$\delta=\operatorname{Re}\lambda_\infty-\rho-\mu>0$',ha='center',fontsize=11)
ax.text(3,1.65,r'$\mu=\|\mathcal{S}\|$',ha='center',fontsize=12)
ax.text(7.2,6.5,'Strong resolvent convergence + actual compact coupling',ha='center',fontsize=14,color=colors[0])
ax.text(7,.95,r'$P_\beta f_*\to f_*\ne0\quad\Longrightarrow\quad\lambda_\beta\quad\Longrightarrow\quad\Lambda_\beta=\beta\lambda_\beta+\frac{1}{4}$',ha='center',fontsize=18,color=colors[0])
ax.text(7,.35,'VP1-VP20 prove every step. Diagram is schematic; positions are not numerical spectral values.',ha='center',fontsize=11)
ax.text(7,7.7,'The actual unstable mode survives the full viscous perturbation',ha='center',fontsize=17,color=colors[0])
fig.tight_layout()
for ext in ['png','svg']:fig.savefig(OUT/('original-viscous-spectral-transfer.'+ext),dpi=160)
plt.close(fig)
print(json.dumps({'figures':['original-vorticity-endpoint-tail.png','original-viscous-spectral-transfer.png'],'numerical_samples':len(samples)}))
