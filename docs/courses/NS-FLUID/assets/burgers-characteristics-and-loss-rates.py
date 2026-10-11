"""Original characteristic coordinates and full residual derivatives at the origin."""
from pathlib import Path
import numpy as np
import sympy as z
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
R=Path(__file__).resolve().parent
def records(m):
 ts=[(1,0,(0,)*(m+1),1)]
 for _ in range(m):
  nxt=[]
  for c,j,a,b in ts:
   nxt.append((c,j+1,a,b+1))
   for k,v in enumerate(a):
    if v:
     aa=list(a);aa[k]-=1;aa[k+1]+=1;nxt.append((c*v,j,tuple(aa),b+1))
   aa=list(a);aa[0]+=1;nxt.append((-b*c,j,tuple(aa),b+2))
  ts=nxt
 return ts
def jet(beta,j):return z.Integer(0) if j%2==0 else z.factorial(j)*z.binomial(beta,(j-1)//2)
def residual_at_origin(delta,n):
 m=2*n+1;q=z.Rational(4*n+1,2);qf=float(q);C=(1+delta**2)**(-qf/2);value=np.zeros_like(delta)
 for c,j,a,b in records(m):
  N=sum(a);coef=c*jet(q/2-1,j)*z.prod(jet(q/2,k+2)**v for k,v in enumerate(a))
  value-=float(coef)*C**(1+N)*delta**(qf+1-m+qf*N)/(1+C*delta**qf)**b
 return value
plt.rcParams.update({'font.size':11,'axes.titlesize':12,'figure.dpi':160})
fig,axes=plt.subplots(1,2,figsize=(12,4.6),constrained_layout=True)
s=np.linspace(-1,1,900);a=s+s**3
for t,color in [(0,'#184f77'),(.5,'#429e86'),(.9,'#a5649c'),(1,'#d56631')]:
 axes[0].plot(a,(1-t)*s+s**3,label=f't = {t:g}',color=color)
axes[0].set(title='EX7–EX11: original characteristic map, λ = 1/2',xlabel='Original initial position a = s + s³',ylabel='Position X(t, a) = (1 − t)s + s³')
axes[0].axhline(0,color='#9ba8b1',lw=.6);axes[0].axvline(0,color='#9ba8b1',lw=.6);axes[0].legend(loc='upper left',frameon=False)
axes[0].annotate('At t = 1:\nderivative vanishes at a = 0',xy=(0,0),xytext=(.35,-1.3),arrowprops=dict(arrowstyle='->',color='#485563'),fontsize=9)
delta=np.geomspace(1e-7,.16,300)
for n,color in [(1,'#184f77'),(2,'#a5649c')]:
 m=2*n+1;A=float(z.factorial(m)*z.binomial(n-1+z.Rational(1,4),n))
 axes[1].loglog(delta,np.abs(residual_at_origin(delta,n)),color=color,lw=2.6,label=f'Full derivative, m = {m}')
 axes[1].loglog(delta,A*np.sqrt(delta),'--',color='#d56631' if n==1 else '#429e86',lw=1.3,label=('(3/2)' if n==1 else '(75/4)')+' δ¹ᐟ², proved leading term')
axes[1].set(title='EX19–EX28: actual derivative at original y = 0',xlabel='Original smoothing parameter δ',ylabel='Absolute original residual derivative |fδ⁽ᵐ⁾(0)|')
axes[1].legend(loc='lower right',fontsize=9,frameon=False);axes[1].grid(True,which='major',alpha=.2)
fig.suptitle('Original Burgers characteristics and the exact constructed loss rates',fontsize=15)
for ext in ['png','svg']:fig.savefig(R/('burgers-characteristics-and-loss-rates.'+ext))
plt.close(fig)
