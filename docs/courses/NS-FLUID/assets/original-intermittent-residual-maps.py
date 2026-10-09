"""Exact residual maps and projections of an actual finite frequency set."""
from pathlib import Path
from itertools import product
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch
R=Path(__file__).resolve().parent
plt.rcParams.update({'font.size':11,'axes.spines.top':False,'axes.spines.right':False})
fig,ax=plt.subplots(figsize=(13,6.5));ax.set(xlim=(0,13),ylim=(0,6.5));ax.axis('off')
def box(x,y,w,h,title,body,color):
 ax.add_patch(FancyBboxPatch((x,y),w,h,boxstyle='round,pad=0.08',fc=color,ec='#3c5260',lw=1.2))
 ax.text(x+w/2,y+h-.22,title,ha='center',va='top',fontweight='bold',fontsize=12)
 ax.text(x+w/2,y+h/2-.11,body,ha='center',va='center',fontsize=11,linespacing=1.45)
box(.2,4.5,3.55,1.42,'Original equation, IC1',r'$u,p,S,f,\nu,L$'+'\nFull force, viscosity and mean','#e5f0f6')
box(4.55,4.5,3.65,1.42,'Constructed coefficients, IC2–IC3',r'$\rho=8D_0\sqrt{\delta^2+|S|^2}$'+'\n'+r'$\sum_{\xi\in\Lambda^+}a_\xi^2(I-\xi\otimes\xi)=\rho I-S$','#e8f2e5')
box(9,4.5,3.7,1.42,'Complete velocity, IC4–IC5',r'$v=\varkappa^{-1}\operatorname{curl}w^{(p)}$'+'\n'+r'$w=v+z,\quad \nabla\cdot w=0,\quad\langle w\rangle=0$','#f6eddc')
box(.2,1.68,3.55,1.68,'Centered pair, IC6–IC8',r'$\phi_\xi=\eta_\xi^2-1$'+'\n'+r'$\partial_tz+\nabla\cdot K_{\rm pair}$'+'\n'+r'$=\nabla\Phi+P_0r_*$','#e8f2e5')
box(4.55,1.68,3.65,1.68,'Nonopposite pairs, OS3–OS7',r'$\nabla\cdot O=\nabla Q_O+E_O$'+'\n'+r'$O=Q_OI+\mathcal{R}E_O+D$'+'\n'+r'$\nabla\cdot D=0$','#e5f0f6')
box(9,1.68,3.7,1.68,'Original new stress, OS6',r'$T_*=H_*+\mathcal{R}(G+E_O)$'+'\n'+r'$S_*=T_*-(\operatorname{tr}T_*/3)I$'+'\n'+r'$p_*=p-\rho-\Phi-Q_O-\operatorname{tr}T_*/3$','#f6eddc')
for a,b in [((3.86,5.2),(4.42,5.2)),((8.31,5.2),(8.88,5.2)),((10.85,4.38),(10.85,3.5)),((8.31,2.5),(8.88,2.5))]:
 ax.annotate('',xy=b,xytext=a,arrowprops={'arrowstyle':'->','lw':1.6,'color':'#3c5260'})
ax.plot([1.98,1.98,10.0],[1.55,1.36,1.36],color='#3c5260',lw=1.3)
ax.annotate('',xy=(10.0,1.58),xytext=(10.0,1.36),arrowprops={'arrowstyle':'->','lw':1.3,'color':'#3c5260'})
ax.text(6.5,6.3,'The complete finite correction: original pressure, mean and viscosity remain explicit',ha='center',fontweight='bold',fontsize=14)
ax.text(6.5,1.1,r'$G=\partial_tv-\nu\Delta w+P_0r_*,\qquad \mathcal{R}(-\nu\Delta w)=-\nu(\nabla w+(\nabla w)^T)$',ha='center',fontsize=13)
ax.text(6.5,.56,'Proof: IC1–IC15, IK22/IK28 and OS1–OS16. Arrows identify exact maps, not size estimates.',ha='center',fontsize=11)
ax.text(6.5,.14,'Human comparison: Buckmaster–Vicol, arXiv:1709.10033v4, original perturbation and oscillation equations.',ha='center',fontsize=10)
fig.tight_layout()
for ext in ['png','svg']:fig.savefig(R/f'original-intermittent-residual-map.{ext}',dpi=175)
plt.close(fig)

def b(s):
 out=np.zeros_like(np.asarray(s,dtype=float));positive=s>0;out[positive]=np.exp(-1/s[positive]);return out
def chi(t):
 t=np.asarray(t);a=b(4-t*t);c=b(t*t-1);return a/(a+c)
fig,ax=plt.subplots(1,2,figsize=(13,6))
q=np.linspace(0,4.2,1001)
ax[0].plot(q,chi(q),label=r'$\chi$',color='#1565a8',lw=2)
ax[0].plot(q,chi(q)-chi(2*q),label=r'$\psi=\chi-\chi(2\,\cdot)$',color='#16805d',lw=2)
ax[0].plot(q,chi(q/2)-chi(4*q),label=r'$\tau=\chi(\,\cdot/2)-\chi(4\,\cdot)$',color='#9b5424',ls='--',lw=1.6)
ax[0].set(xlim=(0,4.2),ylim=(-.03,1.08),xlabel=r'Auxiliary radial argument $|\xi|$',ylabel='Specified multiplier value',title='Actual smooth cutoff profiles, IK2 and IK23')
ax[0].legend(fontsize=10)
# The original L=2pi, lambda=1000, sigma=1/1000, NLambda=5,
# r=2 give kappa=1000 and beta=5. All three-vector components
# below are exact integers before the displayed orthogonal projection.
xi5=np.array([3,4,0]);a5=np.array([0,0,5]);c5=np.array([4,-3,0])
zeta5=np.array([0,3,4]);d5=np.array([5,0,0]);e5=np.array([0,4,-3])
ind=np.array(list(product(range(-2,3),repeat=3)),dtype=int)
one=ind[:,0,None]*xi5+ind[:,1,None]*a5+ind[:,2,None]*c5
two=ind[:,0,None]*zeta5+ind[:,1,None]*d5+ind[:,2,None]*e5
carrier=np.array([600,1400,800]);points=np.unique((one[:,None,:]+two[None,:,:]).reshape(-1,3),axis=0)+carrier
e=np.array([3,7,4])/np.sqrt(74);f=np.array([7,-3,0])/np.sqrt(58)
x=points@e;y=points@f;center=1000*np.sqrt(74)/5;radius=20*np.sqrt(3);gap=center-radius
ax[1].scatter(x,y,s=2,color='#1565a8',alpha=.45,rasterized=True)
theta=np.linspace(0,2*np.pi,501)
ax[1].plot(center+radius*np.cos(theta),radius*np.sin(theta),color='#9b5424',label=r'Proved enclosing radius $2\sqrt{3}\beta r$')
ax[1].axvline(gap,color='#16805d',ls='--',label=r'$K_{\zeta\zeta\prime}=\varkappa|\zeta+\zeta\prime|-2\sqrt{3}\beta r$')
ax[1].set(xlabel=r'Original frequency projection $k\cdot e$',ylabel=r'Original frequency projection $k\cdot f$',title='Actual nonopposite finite support, OS9',aspect='equal')
fig.legend(*ax[1].get_legend_handles_labels(),loc='lower center',bbox_to_anchor=(.53,.165),ncol=2,fontsize=9)
fig.subplots_adjust(bottom=.34,top=.88,wspace=.3)
fig.text(.04,.12,r'$L=2\pi,\ \lambda=1000,\ \sigma=1/1000,\ N_\Lambda=5,\ r=2;\quad e=(3,7,4)/\sqrt{74},\ f=(7,-3,0)/\sqrt{58}.$',fontsize=11)
fig.text(.04,.075,'Right: orthogonal projection of every frequency of the actual scalar product at t=0; the circle is a proved enclosure.',fontsize=10)
fig.text(.04,.03,'Proof: IB14, IK2–IK9 and OS9. Human source: Buckmaster–Vicol, arXiv:1709.10033v4. Kernel bounds are proved in the text.',fontsize=10)
for ext in ['png','svg']:fig.savefig(R/f'original-periodic-inverse-frequencies.{ext}',dpi=175)
