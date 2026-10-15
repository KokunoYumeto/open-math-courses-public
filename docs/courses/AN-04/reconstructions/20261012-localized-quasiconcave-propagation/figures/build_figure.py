"""Exact constant-coefficient transported weight and the proven shell powers."""
from pathlib import Path
import hashlib,json
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
matplotlib.rcParams['svg.fonttype']='none'
MOD=Path(__file__).resolve().parents[1]
eps=.3;R=1.;t=.1;a=.01
y=np.linspace(-1.3,1.3,1201);real=eps/2+(y*y-t*t)/R**2
fig=plt.figure(figsize=(11.5,8.2),layout='constrained')
gs=fig.add_gridspec(2,2);ax1=fig.add_subplot(gs[0,0]);ax2=fig.add_subplot(gs[0,1]);ax3=fig.add_subplot(gs[1,:])
ax1.plot(y,real,color='#146b87',label='Re v = 0.15 + y^2 - 0.01')
for val,name,col in [(eps/3,'epsilon/3','#64748b'),(2*eps/3,'2 epsilon/3','#588b3f'),(1+eps/3,'1 + epsilon/3','#b45309')]:
 ax1.axhline(val,color=col,linestyle='--',linewidth=.9,label=name)
ax1.axvspan(-np.sqrt(eps/12),np.sqrt(eps/12),color='#a6c998',alpha=.3)
for l,u in [(-1.2,-1),(1,1.2)]:ax1.axvspan(l,u,color='#e9b67b',alpha=.35)
ax1.set(title='Exact transported real part at t = 0.1',xlabel='y / R (R = 1)',ylabel='Real exponent',ylim=(0,1.85))
ax1.legend(fontsize=8,loc='upper center')
ax2.semilogy(y,a**real,color='#69468c',label='|a^v| = 0.01^(Re v)')
ax2.axvspan(-np.sqrt(eps/12),np.sqrt(eps/12),color='#a6c998',alpha=.3)
for l,u in [(-1.2,-1),(1,1.2)]:ax2.axvspan(l,u,color='#e9b67b',alpha=.35)
ax2.set(title='Weight before multiplying by the cutoff',xlabel='y / R',ylabel='Absolute weight')
ax2.legend(fontsize=8)
lam=np.geomspace(1e-8,1e-1,600)
ax3.loglog(lam,lam**.25,color='#146b87',label='unmeasured forcing: lambda^(3/2) lambda^(-5/4)')
ax3.loglog(lam,np.ones_like(lam),color='#b45309',label='unknown error: lambda^(1/4) lambda^(-1/4)')
ax3.set(title='Exact shell-error powers; constant factors suppressed',xlabel='Frequency parameter lambda',ylabel='Power of lambda')
ax3.legend(fontsize=9,loc='lower right')
for ax in [ax1,ax2,ax3]:ax.grid(alpha=.2)
p=MOD/'figures/transported-weight-and-shell-powers.svg';fig.savefig(p);plt.close(fig)
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
v={'svg':'figures/transported-weight-and-shell-powers.svg','svg_sha256':sha(p),
 'generator_sha256':sha(Path(__file__)),'actually_inspected':False,
 'numerical_samples_of_exact_formula':True,'arbitrary_coefficient_transport_inferred_from_plot':False,
 'parameters':{'epsilon':'3/10','R':'1','t':'1/10','a':'1/100'},
 'exact_formula':'v=epsilon/2+(y-it)^2/R^2; |a^v|=a^(Re v)',
 'inner_region':'y^2/R^2<epsilon/12','outgoing_cutoff_region':'1<|y|/R<6/5',
 'shell_power_constants_suppressed':True,'source_locator':'**F0. An exact model and its shell powers.**'}
(MOD/'figure-check.json').write_text(json.dumps(v,indent=2)+'\n','utf-8')
print(json.dumps({'figure_bytes':p.stat().st_size,'sha256':sha(p)}))
