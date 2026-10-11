"""Exact original-cylinder example and two-boundary stream estimate."""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
R=Path(__file__).resolve().parent
plt.rcParams.update({'font.family':'DejaVu Sans','font.size':12,'mathtext.fontset':'dejavusans'})
r=np.linspace(0,1,501);u=2-4*r*r;psi=r*r*(1-r*r);K=r*r*(1-r*r)/2
fig,axs=plt.subplots(1,3,figsize=(15,6.6),facecolor='#f7f9fc')
fig.suptitle('Both the wall and the axis enter the original stream estimate',fontsize=20,y=.96)
fig.text(.5,.882,r'Exact steady Euler field: $u_r=u_\vartheta=0,\quad u_z=2-4r^2,\quad P=0,\quad z\in\mathbb{R}/(2\mathbb{Z})$.',ha='center',fontsize=15)
axs[0].plot(u,r,color='#24649b',lw=3)
axs[0].axvline(0,color='#808b99',lw=1)
axs[0].axhline(1/np.sqrt(2),color='#a86926',lw=1,ls='--')
axs[0].set(xlabel=r'Original axial velocity $u_z$',ylabel=r'Original radius $r$',xlim=(-2.25,2.25),ylim=(0,1),yticks=[0,.5,1])
axs[0].set_title('Opposite axial flows have zero net flux',fontsize=13,pad=12)
axs[0].text(.04,.08,r'$\int_0^1r(2-4r^2)\,dr=0$',transform=axs[0].transAxes,fontsize=14)
axs[0].text(.03,.73,r'$r=1/\sqrt{2}$',transform=axs[0].transAxes,fontsize=11,color='#8b541b')
axs[1].plot(r,psi,color='#176c55',lw=3,label=r'$r\varphi^\vartheta=r^2(1-r^2)$')
axs[1].plot(r,K,color='#70429b',lw=2,ls='--',label=r'$K=r^2(1-r^2)/2$')
axs[1].set(xlabel=r'Original radius $r$ at $a=b=1$',ylabel='Exact displayed quantities',xlim=(0,1),ylim=(0,.29))
axs[1].set_title('Both endpoint values vanish',fontsize=13,pad=12);axs[1].legend(loc='upper center',fontsize=10,frameon=False)
axs[1].scatter([0,1],[0,0],s=45,color='#176c55',zorder=5)
axs[1].text(.05,.05,'Axis',transform=axs[1].transAxes,color='#70429b')
axs[1].text(.78,.05,'Wall',transform=axs[1].transAxes,color='#176c55')
axs[2].axis('off')
axs[2].text(.02,.95,'Complete original weighted identities',fontsize=13,weight='bold',va='top')
lines=[
(r'$\mathcal{A}=\int R^{-1}|\nabla\psi|^2\,dy$',16),
(r'$=\int\left(R|\nabla\phi|^2+b^2\phi^2/R\right)\,dy$',13),
(r'$\int\psi^2/R\,dy\ \leq\ \mathcal{A}/(8b^2)$',15),
(r'$\mathcal{A}\ \leq\ (8b^2)^{-1}\int R^3Q^2\,dy$',14),
(r'$\int_{-1}^{1}\int_0^1 r(u_z^2+u_r^2)\,dr\,dz$',13),
(r'$\leq\ \frac{1}{8}\int_{-1}^{1}\int_0^1r\omega_\vartheta^2\,dr\,dz$',14),
(r'$\mathrm{Example:}\quad 4/3\leq 32/8=4$',15)]
for yy,(txt,size) in zip([.79,.65,.49,.34,.20,.06,-.10],lines):axs[2].text(.03,yy,txt,fontsize=size,va='center')
for ax in axs[:2]:ax.spines[['top','right']].set_visible(False);ax.grid(alpha=.18)
fig.text(.055,.085,'The bound applies to the zero-flux class. K is the exact optimal point-evaluation coefficient at the displayed sample scale.',fontsize=11)
fig.text(.055,.052,'Proof: Exercises 3 and 5, EX9–EX24. The integrated estimate is proved, without a claim that its constant is optimal.',fontsize=11)
fig.text(.055,.020,'Original domain and stream operator: Chen–Hou, arXiv:2210.07191v4, author TeX 10167–10285. Editorial derivation; no novelty claim.',fontsize=10)
fig.subplots_adjust(top=.78,bottom=.25,left=.06,right=.98,wspace=.30)
for ext in ['png','svg']:fig.savefig(R/('original-cylinder-stream-energy.'+ext),dpi=175,facecolor=fig.get_facecolor())

