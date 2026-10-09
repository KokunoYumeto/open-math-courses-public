"""Original physical shear and exact coefficient powers for the viscosity proof."""
from pathlib import Path
from fractions import Fraction
import numpy as np
from scipy.integrate import quad
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
O=Path(__file__).resolve().parent
plt.rcParams.update({'font.family':'DejaVu Sans','font.size':11})
L=2*np.pi;alpha=2*np.pi/L;epsilon=.1;nu=epsilon;kappa=epsilon**2;A=1.
def bump(r):return np.exp(-1/(1-r*r)) if 0<=r<1 else 0.
den=quad(lambda r:r*r*bump(r),0,1,epsabs=1e-13)[0]
def moment(j):
    return quad(lambda r:r*r*bump(r)*np.sinc(j*epsilon*alpha*r/np.pi),0,1,epsabs=1e-13)[0]/den
m1=moment(1);m2=moment(2)
xs=np.linspace(0,L,501)
actual=nu*A*m1*alpha*np.sin(alpha*xs)
printed=kappa/2*A*m1*alpha*np.sin(alpha*xs)
defect=(nu-kappa/2)*alpha**2*A*m1*np.cos(alpha*xs)
fig,(ax,bx)=plt.subplots(2,1,figsize=(11,8),sharex=True,layout='constrained')
ax.plot(xs,actual,color='#0f766e',lw=2.7,label=r'Actual $S_{13}=S_{31}$')
ax.plot(xs,printed,color='#b45309',lw=2.7,label=r'Printed $\kappa/2$ tensor term')
ax.set(title='Both original viscous coefficients on the same Euler shear',ylabel='Physical stress entry')
ax.legend(loc='upper right');ax.axhline(0,color='#64748b',lw=.8);ax.grid(alpha=.2)
bx.plot(xs,defect,color='#1d4ed8',lw=2.7)
bx.set(xlabel=r'Original coordinate $x_3$',ylabel=r'Original equation defect, component 1')
bx.axhline(0,color='#64748b',lw=.8);bx.grid(alpha=.2)
bx.set_xticks([0,np.pi/2,np.pi,3*np.pi/2,2*np.pi],['0','π/2','π','3π/2','2π'])
fig.text(.51,.015,'VV5–VV7 and EX1–EX4. L = 2π, α = 1, A = 1, ε = ν = 0.1, κ = ε² = 0.01.\nRadial unit-ball bump kernel; m₁ is its exact cosine moment, evaluated by quadrature.\nThe full covariance trace and its pressure are retained in EX2–EX3.',
         ha='center',fontsize=10)
fig.get_layout_engine().set(rect=(0,.10,1,.90))
for ext in ['png','svg']:fig.savefig(O/f'original-viscous-starting-tensor.{ext}',dpi=170)
plt.close(fig)
labels=['Stress: ST26','Energy: EE17','Time window: AB12','Temporal correction: VD₀,₄','Principal correction: VD₀,₁']
values=[Fraction(17,8),Fraction(163,32),Fraction(443,40),Fraction(2977,8),Fraction(6041,16)]
fig,ax=plt.subplots(figsize=(11,6),layout='constrained')
ys=np.arange(len(labels))
ax.scatter([float(v) for v in values],ys,s=100,color='#0f766e',zorder=3)
for yv,v in zip(ys,values):
    ax.hlines(yv,1,float(v),color='#94a3b8',lw=2)
    ax.annotate(str(v),(float(v),yv),xytext=(10,7),textcoords='offset points')
ax.set_xscale('log');ax.set_xlim(1,900)
ax.set_yticks(ys,labels);ax.set_ylim(-.6,len(labels)-.5);ax.invert_yaxis()
ax.set(xlabel='Exact net exponent d − w(1 − η), logarithmic axis',
       title='The actual stage decay absorbs the changing energy-profile constant')
ax.grid(axis='x',alpha=.2)
fig.text(.51,.018,'VK3–VK9 and EX5–EX7. Original choices b = 1024 and η = 1/8.\nThe dots show exact exponents. The complete coefficients Dⱼ, profile factor and λ₁ prefactors\nremain in VK5 and VK9; this plot does not set them to one.',
         ha='center',fontsize=10)
fig.get_layout_engine().set(rect=(0,.13,1,.87))
for ext in ['png','svg']:fig.savefig(O/f'original-vanishing-stage-powers.{ext}',dpi=170)
plt.close(fig)
print(f'Physical kernel moments m1={m1:.12g}, m2={m2:.12g}; both figures generated.')
