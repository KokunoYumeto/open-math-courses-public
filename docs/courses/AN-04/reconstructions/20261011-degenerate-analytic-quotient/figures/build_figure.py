"""Exact collapsed-interval coordinate and endpoint rational barrier."""
from pathlib import Path
import hashlib,json
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
HERE=Path(__file__).resolve().parent
plt.rcParams.update({'font.size':12,'svg.fonttype':'none','svg.hashsalt':'an04-degenerate-analytic-quotient','font.family':'DejaVu Sans'})
fig=plt.figure(figsize=(11,9),constrained_layout=True)
grid=fig.add_gridspec(2,2,height_ratios=[1,1.1])
left=fig.add_subplot(grid[0,0]);right=fig.add_subplot(grid[0,1]);bar=fig.add_subplot(grid[1,:])
t=np.linspace(-1,1,601)
prim=lambda t:np.where(t>1/3,(t-1/3)**2/2,np.where(t< -1/3,-(t+1/3)**2/2,0))
xx=np.linspace(-.8,.8,5)
left.axvspan(-1/3,1/3,color='#d6e8dc')
for x in xx:
 left.plot(t,np.full_like(t,x),color='#236b94',lw=1.5)
 left.plot([-1/3,1/3],[x,x],color='#247248',lw=3)
 right.plot(np.full_like(t,x),-prim(t),color='#236b94',lw=1.5)
 right.plot([x],[0],'o',color='#247248',ms=7)
for tt in [-1,-.8,-.6,0,.6,.8,1]:
 left.axvline(tt,color='#a36521',alpha=.6,lw=1)
 right.axhline(-float(prim(np.array(tt))),color='#a36521',alpha=.6,lw=1)
left.set(title='Source: a(t) = max(|t| − 1/3, 0)',xlabel='Time t',ylabel='Active coordinate x',xlim=(-1,1),ylim=(-.9,.9))
left.set_xticks([-1,-1/3,1/3,1],['−1','−1/3','1/3','1'])
right.set(title='Image: u = x − i A(t)',xlabel='Re u = x',ylabel='Im u = −A(t)',xlim=(-.9,.9),ylim=(-.24,.24))
right.text(0,.035,'Each green segment becomes one point',ha='center',fontsize=10,color='#247248')
delta=1/512;T=delta/64
s=np.linspace(0,4,601);x=1-delta*s
dminus=1+delta+x;dplus=1+delta-x
value=4*delta*(dminus/(dminus*dminus+T*T)+dplus/(dplus*dplus+T*T))
bar.plot(s,value,color='#236b94',lw=3,label='Exact Re Fδ(x − iT)')
bar.axhline(1,color='#a36521',ls='--',lw=2,label='Required level 1')
bar.axvspan(0,1/16,color='#d6e8dc',label='Endpoint region: 0 ≤ s ≤ 1/16')
bar.set(title='Barrier example: a = 1, δ = 1/512, T = δ/64',xlabel='Scaled distance from the right endpoint: s = (1 − x)/δ',ylabel='Real part of the rational barrier',xlim=(0,4),ylim=(0,4.5))
bar.legend(loc='upper right',fontsize=11)
for ax in [left,right,bar]:ax.grid(alpha=.17)
fig.suptitle('A complex quotient across a zero interval, and a uniform endpoint barrier',fontsize=15)
out=HERE/'degenerate-quotient-and-barrier.svg'
fig.savefig(out,metadata={'Date':None,'Creator':'AN-04 original reproducible figure'});plt.close(fig)
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
(HERE.parent/'figure-check.json').write_text(json.dumps({'svg':'figures/degenerate-quotient-and-barrier.svg','svg_sha256':sha(out),'generator_sha256':sha(Path(__file__)),'actual_formulas':['A(t)=0 for |t|<=1/3; A(t)=(t-1/3)^2/2 for t>1/3; A(t)=-(t+1/3)^2/2 for t<-1/3','u=x-i A(t)','Re F_delta(x-iT)=4 delta ((1+delta+x)/((1+delta+x)^2+T^2)+(1+delta-x)/((1+delta-x)^2+T^2))','delta=1/512, T=delta/64, x=1-delta*s'],'scope':'First two panels show the exact degenerate coordinate; last panel uses the different constant-coefficient barrier example. All strict region inequalities and exact fibers are proved analytically.'                           },indent=2)+'\n','utf-8')
print(json.dumps({'figure':str(out),'sha256':sha(out)}))
