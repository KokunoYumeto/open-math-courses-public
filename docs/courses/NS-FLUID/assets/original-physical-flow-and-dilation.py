"""Exact analytic illustrations for PT3--PT21, VD4--VD21 and EX1--EX2."""
from pathlib import Path
import json
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch
OUT=Path(__file__).resolve().parent
plt.rcParams.update({'font.family':'DejaVu Sans','font.size':12,'axes.spines.top':False,'axes.spines.right':False})
colors=['#17365D','#007E87','#BA641B','#7C4692']
nu=.7;beta=2.;a=.6;b=np.array([1.,2.,-1.]);times=[0.,.5,1.,2.]
fig,axs=plt.subplots(1,2,figsize=(14,6),layout='constrained')
rad=np.linspace(0,4,500);samples=[]
for t,c in zip(times,colors):
 q=nu*np.expm1(t/beta);kap=np.exp(t/(2*beta))
 val=b[0]*np.exp(3*t/(4*beta))*(1+4*a*q)**(-1.5)*np.exp(-a*kap**2*rad**2/(1+4*a*q))
 axs[0].plot(rad,val,color=c,label=f't = {t:g}',lw=2.2)
 samples.append({'t':t,'q_t':q,'kappa_t':kap,'first_component_at_origin':float(val[0])})
axs[0].set(xlabel=r'Original radius $|\xi|$',ylabel='First vector component',title='The exact Gaussian formula (EX1)')
axs[0].legend(frameon=False);axs[0].grid(alpha=.18)
t=np.linspace(0,3,400);q=nu*np.expm1(t/beta);N0=float(b@b*(np.pi/(2*a))**1.5);N=N0*(1+4*a*q)**(-1.5)
axs[1].plot(t,N,color=colors[0],lw=2.3,label=r'$\|\mathcal{S}(t)f\|_2^2$')
axs[1].plot(t,N0-N,color=colors[1],lw=2.3,label=r'$\frac{2\nu}{\beta}\int_0^t\|\nabla\mathcal{S}(u)f\|_2^2du$')
axs[1].axhline(N0,color=colors[2],ls='--',lw=1.7,label=r'Original $\|f\|_2^2$')
axs[1].set(xlabel='Original elapsed time t',ylabel='Full three-dimensional squared norm',title='The exact energy balance (EX2)')
axs[1].legend(frameon=False,fontsize=10,loc='center right');axs[1].grid(alpha=.18)
fig.suptitle('Heat and dilation with the original volume and coefficients',fontsize=17)
fig.supxlabel(r'$f(\xi)=(1,2,-1)e^{-0.6|\xi|^2}$; $\nu=0.7$, $\beta=2$. Analytic example in the full vector space; no solenoidal claim.',fontsize=11)
for ext in ['png','svg']:fig.savefig(OUT/('original-heat-dilation.'+ext),dpi=160)
plt.close(fig)
(OUT/'original-heat-dilation-data.json').write_text(json.dumps({'formula':'EX1--EX2','nu':nu,'beta':beta,'a':a,'b':b.tolist(),'initial_squared_norm':N0,'samples':samples,'method':'Direct evaluation of proved analytic formulas; no computed spectrum.'},indent=2)+'\n',encoding='utf8')
fig,ax=plt.subplots(figsize=(14,8));ax.set(xlim=(0,14),ylim=(0,8));ax.axis('off')
def box(x,y,w,h,text,c):
 ax.add_patch(FancyBboxPatch((x,y),w,h,boxstyle='round,pad=0.16',facecolor='#F5F8FC',edgecolor=c,lw=1.7))
 ax.text(x+w/2,y+h/2,text,ha='center',va='center',fontsize=12,color='#142638',linespacing=1.5)
box(.4,4.85,5.3,1.6,'Physical pure-swirl vorticity\n'+r'$\Omega=\omega^\theta(s,z)e_\theta\in L^2(\mathbb{R}^3)$'+'\n'+r'$\|\Omega\|_2^2=2\pi\int s|\omega^\theta|^2\,ds\,dz$',colors[0])
box(8.2,4.85,5.3,1.6,'Canonical physical velocity\n'+r'$U=\mathcal{B}\Omega\in L^6,\quad\nabla U\in L^2$'+'\n'+r'$\operatorname{curl}U=\Omega,\quad\operatorname{div}U=0$',colors[1])
ax.annotate('',xy=(8,5.65),xytext=(5.9,5.65),arrowprops={'arrowstyle':'->','lw':2,'color':colors[0]})
ax.text(6.95,6.05,'Full Fourier receiver\nPT5, including zero frequency',ha='center',fontsize=10)
box(.4,1.9,5.3,1.65,'Transport: exact physical volume\n'+r'$\mathcal{G}(t)\Omega=\Omega\circ\Phi_{-t},\quad\det D\Phi_t=1$'+'\n'+r'$D(\mathcal{M})=\{\Omega:\bar U_\ell\cdot\nabla\Omega\in L^2\}$',colors[0])
box(8.2,1.9,5.3,1.65,'Actual compact ring coupling\n'+r'$\mathcal{S}\Omega=\bar\Omega_\ell\cdot\nabla U+\Omega\cdot\nabla\bar U_\ell$'+'\n'+r'$\mathcal{K}\Omega=-U\cdot\nabla\bar\Omega_\ell$',colors[1])
for x in [3.05,10.85]:ax.annotate('',xy=(x,3.8),xytext=(x,4.6),arrowprops={'arrowstyle':'->','lw':1.8,'color':colors[0]})
ax.text(7,.92,r'$|Q_\ell|=2\pi^2\ell R^2,\quad\|\mathcal{S}\|\leq\mu_\ell^*\to0,\quad\mathcal{K}\ \mathrm{compact}$',ha='center',fontsize=16,color=colors[0])
ax.text(7,.35,'PT1-PT21 prove the maps, domains and bounds. EX7 shows why a general velocity is not in L2.',ha='center',fontsize=11)
ax.text(7,7.3,'The original physical space receives every part of the ring generator',ha='center',fontsize=17,color=colors[0])
fig.tight_layout()
for ext in ['png','svg']:fig.savefig(OUT/('original-physical-ring-operators.'+ext),dpi=160)
plt.close(fig)
print(json.dumps({'figures':['original-heat-dilation.png','original-physical-ring-operators.png'],'analytic_samples':len(samples)}))
