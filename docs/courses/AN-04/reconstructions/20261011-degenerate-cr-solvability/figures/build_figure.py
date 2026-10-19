"""Exact degenerate coordinate and illustrative spatial resolvent products."""
from pathlib import Path
import hashlib,json
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
HERE=Path(__file__).resolve().parent
plt.rcParams.update({'font.size':12,'svg.fonttype':'none','svg.hashsalt':'an04-degenerate-cr-solvability','font.family':'DejaVu Sans'})
fig,ax=plt.subplots(2,1,figsize=(11,8),constrained_layout=True)
t=np.linspace(-1,1,601)
primitive=np.where(t>1/3,(t-1/3)**2/2,np.where(t< -1/3,-(t+1/3)**2/2,0))
ax[0].plot(t,-primitive,color='#236b94',lw=3)
ax[0].axvspan(-1/3,1/3,color='#d6e8dc',alpha=.8)
ax[0].plot([-1/3,1/3],[0,0],color='#247248',lw=4,label='One image for the entire zero interval')
ax[0].set(title='Exact coordinate: u(t,x₁) = x₁ − i ∫₀ᵗ a(s) ds',xlabel='t',ylabel='Imaginary part of u',xlim=(-1,1))
ax[0].set_xticks([-1,-1/3,0,1/3,1],['−1','−1/3','0','1/3','1'])
ax[0].legend(loc='upper right',fontsize=10)
xi=np.geomspace(1,1024,400)
for n,col in [(1,'#236b94'),(2,'#a36521'),(4,'#247248'),(8,'#673a87')]:
    product=np.ones_like(xi)
    for j in range(1,n+1):product/=1+(2**(-j-2)*xi)**2
    ax[1].loglog(xi,product,label=f'N = {n}',color=col,lw=2.5)
ax[1].set(title='Successive spatial smoothing, illustrated with εⱼ = 2⁻ʲ⁻²',xlabel='Spatial frequency magnitude |ξ|',ylabel='E_N(ξ)',xlim=(1,1024),ylim=(1e-20,2))
ax[1].legend(ncol=4,loc='lower left',fontsize=11)
for a in ax:a.grid(alpha=.2)
fig.suptitle('A zero coefficient interval and the resolvents used for smooth solvability',fontsize=15)
f=HERE/'degenerate-coordinate-and-products.svg'
fig.savefig(f,metadata={'Date':None,'Creator':'AN-04 original reproducible figure'});plt.close(fig)
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
(HERE.parent/'figure-check.json').write_text(json.dumps({'svg':'figures/degenerate-coordinate-and-products.svg','svg_sha256':sha(f),'generator_sha256':sha(Path(__file__)),'actual_formulas':['a(t)=max(|t|-1/3,0) on [-1,1]','Im u=-primitive(a)','E_N=product_(j=1)^N (1+(2^(-j-2) xi)^2)^(-1)'],'scope':'The coordinate is exact. The displayed resolvent sequence illustrates the construction and is not asserted to work uniformly for an arbitrary coefficient family.'                           },indent=2)+'\n','utf-8')
print(json.dumps({'figure':str(f),'sha256':sha(f)}))
