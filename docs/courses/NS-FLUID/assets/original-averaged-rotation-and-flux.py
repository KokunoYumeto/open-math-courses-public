"""Reproduce the Gaussian rotation bound, full dilation factor and dyadic energy map."""
from pathlib import Path
import json
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch
out=Path(__file__).resolve().parent
alpha,gamma=2.,1.
a,b=9*alpha,2*(alpha-1)**2
rstar=a/(a+b+np.sqrt(a*a+a*b+b*b))
theta_star=np.arcsin(np.sqrt(rstar))
theta_old=np.arctan2(4,3)
theta=np.linspace(0,np.pi/2,301)
def defect(t):
    delta=9*alpha+2*(alpha-1)**2*np.sin(t)**2
    return 4*alpha*np.pi**1.5*(alpha-1)**2*np.sin(2*t)/(np.sqrt(3*gamma)*delta**1.5)
lam=np.linspace(.25,2,301)
plt.rcParams.update({'font.family':'DejaVu Sans','font.size':11})
fig,ax=plt.subplots(1,2,figsize=(13,6))
ax[0].plot(theta,defect(theta),color='#174a67',lw=2.3)
ax[0].plot(theta_star,defect(theta_star),'o',color='#b96210',label=r'Exact maximum $\theta_*$')
ax[0].plot(theta_old,defect(theta_old),'s',color='#71419b',label=r'Original $\cos\theta=3/5$')
ax[0].set(xlabel=r'Original rotation angle $\theta$ (radians)',ylabel=r'Exact energy defect $\mathcal{E}_\theta(u_{2,1})$',title='The full Gaussian family: alpha = 2, gamma = 1')
ax[0].set_xticks([0,np.pi/4,np.pi/2],['0',r'$\pi/4$',r'$\pi/2$'])
ax[0].legend(fontsize=10);ax[0].grid(alpha=.2)
ax[1].plot(lam,lam**2.5,color='#137f84',lw=2.3,label=r'Full coefficient $\lambda^{5/2}$')
ax[1].axhline(1,color='#b96210',linestyle='--',label='Omitted-dilation coefficient 1')
ax[1].axvline(1,color='#555555',lw=.8)
ax[1].set(xlabel=r'Actual common dilation $\lambda$',ylabel='Coefficient multiplying the original convection',title='Both input dilations and the output inverse')
ax[1].legend(fontsize=10);ax[1].grid(alpha=.2)
fig.suptitle('Exact rotation optimization and the missing dilation contribution',fontsize=17)
fig.subplots_adjust(left=.075,right=.98,top=.83,bottom=.29,wspace=.28)
fig.text(.5,.18,r'Left: $4\alpha\pi^{3/2}(\alpha-1)^2\sin(2\theta)/(\sqrt{3\gamma}[9\alpha+2(\alpha-1)^2\sin^2\theta]^{3/2})$.',ha='center',fontsize=11)
fig.text(.5,.105,r'Right: $\operatorname{Dil}_{\lambda^{-1}}C(\operatorname{Dil}_{\lambda}u,\operatorname{Dil}_{\lambda}v)=\lambda^{5/2}C(u,v)$.',ha='center',fontsize=12)
fig.text(.5,.035,'Complete proofs: Exercise 2, EX4–EX7, and MB23–MB26. The curves evaluate exact formulas, not numerical fluid evolutions.',ha='center',fontsize=10)
fig.savefig(out/'original-averaged-rotation-and-dilation.png',dpi=160)
fig.savefig(out/'original-averaged-rotation-and-dilation.svg')
plt.close(fig)

fig,ax=plt.subplots(figsize=(14,5.2))
ax.set(xlim=(-1.9,8.4),ylim=(-1.8,2.1));ax.axis('off')
positions=[0,2,4.5,6.5]
labels=['N','N+1','M-1','M']
for x,n in zip(positions,labels):
    ax.add_patch(FancyBboxPatch((x-.5,-.15),1,.65,boxstyle='round,pad=.08',facecolor='#eaf1f5',edgecolor='#174a67',lw=1.5))
    ax.text(x,.175,r'$\frac{1}{2}X_{'+n+r'}^2$',ha='center',va='center',fontsize=17)
    ax.annotate('',xy=(x,-1),xytext=(x,-.25),arrowprops={'arrowstyle':'->','lw':1.5,'color':'#b96210'})
    ax.text(x,-1.2,r'$\nu\lambda^{2('+n+r')\alpha}X_{'+n+r'}^2$',ha='center',fontsize=11,color='#8d4b0d')
for left,right,label,style in [
    (-1.8,-.65,r'$\lambda^{N-1}X_NX_{N-1}^2$','-'),
    (.65,1.35,r'$\lambda^N X_N^2X_{N+1}$','-'),
    (2.65,3.85,'All internal transfers','--'),
    (5.15,5.85,r'$\lambda^{M-1}X_{M-1}^2X_M$','-'),
    (7.15,8.3,r'$\lambda^M X_M^2X_{M+1}$','-')]:
    ax.annotate('',xy=(right,.2),xytext=(left,.2),arrowprops={'arrowstyle':'->','lw':1.8,'color':'#137f84','linestyle':style})
    ax.text((left+right)/2,.9,label,ha='center',fontsize=10,color='#0c686d')
ax.text(3.2,1.8,'The actual finite-window energy balance',ha='center',fontsize=19)
ax.text(3.2,1.37,'Incoming boundary flux + internal transfers − outgoing boundary flux − full dissipation',ha='center',fontsize=10)
ax.text(3.2,-1.65,r'EX20–EX23: every internal transfer cancels in the sum; both boundary fluxes remain until their limits are proved.',ha='center',fontsize=11)
fig.subplots_adjust(left=.02,right=.98,top=.98,bottom=.18)
fig.text(.5,.09,'The diagram shows N, N+1, M−1 and M for M ≥ N+3. The omitted interior indices are retained in the exact sum.',ha='center',fontsize=10)
fig.text(.5,.035,'For the proved nonnegative trajectories, each horizontal flux is nonnegative in its displayed direction. No trajectory values are plotted.',ha='center',fontsize=10)
fig.savefig(out/'original-dyadic-boundary-energy.png',dpi=160)
fig.savefig(out/'original-dyadic-boundary-energy.svg')
(out/'original-averaged-rotation-and-flux-data.json').write_text(json.dumps({
    'alpha':alpha,'gamma':gamma,'theta_star':theta_star,'original_theta':theta_old,
    'rotation_samples':[{'theta':float(t),'energy_defect':float(d)} for t,d in zip(theta,defect(theta))],
    'dilation_samples':[{'lambda':float(l),'full_coefficient':float(l**2.5),'omitted_dilation_coefficient':1.} for l in lam],
    'dyadic_diagram':{'indices':labels,'scope':'Exact finite sum EX20; all internal modes retained. Arrows have the indicated sign for nonnegative trajectories.'},
    'proof':'AVERAGED_OPERATOR_EXERCISES_20261010.md EX4–EX7 and EX20–EX23; ORIGINAL_AVERAGED_OPERATOR_20261010.md MB23–MB26'
},indent=2)+'\n',encoding='utf-8')
print(json.dumps({'theta_star':theta_star,'rotation_samples':len(theta),'dilation_samples':len(lam)}))
