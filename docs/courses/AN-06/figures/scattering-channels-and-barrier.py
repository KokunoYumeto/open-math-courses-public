"""Original CC0 figure for the coefficient ordering and exact barrier formula.

Run with Python, numpy and matplotlib; output files are adjacent to this source.
No source image or private reference data are used.
"""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle

plt.rcParams.update({'font.family':'DejaVu Sans','font.size':11,
                     'svg.hashsalt':'AN06-exact-barrier-v1'})
out=Path(__file__).resolve().parent
energy=np.unique(np.r_[np.linspace(.04,4,900),1.,1.+np.pi**2/4])
k=np.sqrt(energy)
q=np.sqrt((energy-1).astype(complex))
d=np.empty_like(q)
mask=abs(q)>1e-12
d[mask]=np.sin(2*q[mask])/q[mask]
d[~mask]=2
c=np.cos(2*q).real
alpha=((k*k+q*q)*d/(2*k)).real
beta=((k*k-q*q)*d/(2*k)).real
assert np.max(abs(c*c+alpha*alpha-1-beta*beta))<1e-11
t=np.exp(-2j*k)/(c-1j*alpha)
r=-1j*beta*t
transmission=abs(t)**2;reflection=abs(r)**2
assert np.max(abs(transmission+reflection-1))<1e-12
zero=np.where(energy==1)[0][0]
assert abs(transmission[zero]-.5)<1e-12

fig,(ax,bx)=plt.subplots(1,2,figsize=(13.6,5),gridspec_kw={'width_ratios':[1.2,1]})
fig.subplots_adjust(left=.025,right=.985,bottom=.17,top=.83,wspace=.20)
ax.set_xlim(-4.1,4.1);ax.set_ylim(-1.25,1.25);ax.axis('off')
ax.add_patch(Rectangle((-1,-.9),2,1.8,facecolor='#e5eaf0',edgecolor='#8394a6'))
ax.text(0,.05,r'$V=1$'+'\n'+r'$-1\leq x\leq1$',ha='center',va='center',fontsize=13)
ax.annotate('',xy=(4,-1.03),xytext=(-4,-1.03),arrowprops={'arrowstyle':'->','color':'#576573'})
ax.text(4.02,-1.03,r'$x$',ha='left',va='center')
blue='#1c6ea4';orange='#b65c26'
for x0,x1,y,color,label in [
    (-3.8,-1.25,.66,blue,r'Incoming: $C_l^+e^{ikx}$'),
    (3.8,1.25,.66,blue,r'Incoming: $C_r^-e^{-ikx}$'),
    (-1.25,-3.8,-.5,orange,r'Outgoing: $C_l^-e^{-ikx}$'),
    (1.25,3.8,-.5,orange,r'Outgoing: $C_r^+e^{ikx}$')]:
    ax.annotate('',xy=(x1,y),xytext=(x0,y),arrowprops={'arrowstyle':'->','lw':2.5,'color':color})
    ax.text((x0+x1)/2,y+.18,label,ha='center',color=color,fontsize=10.7)
ax.set_title('Coefficient ordering: momenta (+k, -k)',pad=20,fontsize=12)
ax.text(0,-1.38,r'$(C_l^+,C_r^-)\ \mapsto\ (C_r^+,C_l^-)$',ha='center',fontsize=13)
bx.plot(energy,transmission,color=blue,lw=2,label=r'Transmission $|t|^2$')
bx.plot(energy,reflection,color=orange,lw=2,label=r'Reflection $|r|^2$')
bx.axvline(1,color='#88939b',lw=1,ls=':')
bx.plot([1],[.5],marker='o',color='#354552',ms=5)
bx.annotate(r'$q=0$: both $1/2$',xy=(1,.5),xytext=(1.5,.6),fontsize=10,
            arrowprops={'arrowstyle':'->','color':'#576573'})
resonance=1+np.pi**2/4
bx.plot([resonance],[1],marker='o',color=blue,ms=4)
bx.annotate(r'$2q=\pi$: $|t|^2=1$',xy=(resonance,1),xytext=(2.3,.83),fontsize=10,
            arrowprops={'arrowstyle':'->','color':'#576573'})
bx.set_xlim(0,4);bx.set_ylim(0,1.05)
bx.set_xlabel(r'Positive energy $\lambda=k^2$');bx.set_ylabel('Probability')
bx.grid(alpha=.18);bx.legend(loc='center right',fontsize=10)
bx.set_title(r'Exact barrier: $a=1$, $v_0=1$',pad=20,fontsize=12)
fig.suptitle('Two free channels and their conserved total probability',fontsize=15,y=.97)
fig.text(.5,.035,'Theorem 4.1, equations (12)–(16). Numerical samples of the exact formulas; free threshold λ = 0 is excluded.',
         ha='center',fontsize=10,color='#4b5965')
fig.savefig(out/'scattering-channels-and-barrier.png',dpi=150,metadata={'Software':'AN06 original CC0 plot'})
fig.savefig(out/'scattering-channels-and-barrier.svg',metadata={'Date':None,'Creator':'AN06 original CC0 plot'})
plt.close(fig)
print('Original channel/probability figure generated; exact probability checks passed.')
