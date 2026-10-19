"""Reproduce the exact collapsed coordinate and quadratic barrier in RLP:X3."""
from pathlib import Path
import hashlib,json
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
HERE=Path(__file__).resolve().parent
plt.rcParams.update({'svg.fonttype':'none','font.size':10})
fig,ax=plt.subplots(1,3,figsize=(12,4.7),layout='constrained')
beta=lambda t:np.sign(t)*np.exp(-1/(np.abs(t)-1)) if abs(t)>1 else 0.
levels=[-2,-1.65,-1.3,-.8,0,.8,1.3,1.65,2]
colors=plt.cm.viridis(np.linspace(0,1,len(levels)))
ax[0].axvspan(-1,1,color='#dae5ee',alpha=.85)
for t,c in zip(levels,colors):
 ax[0].plot([t,t],[-.4,.4],color=c,lw=1.7)
 ax[1].plot([-.4,.4],[-beta(t),-beta(t)],color=c,lw=1.7)
ax[0].annotate('All times in [-1, 1]\ncollapse at each fixed y',xy=(0,.15),xytext=(0,.53),ha='center',fontsize=9,
 arrowprops={'arrowstyle':'->','color':'#34495e'})
ax[0].set(xlabel='Time t',ylabel='Active coordinate y',xlim=(-2.2,2.2),ylim=(-.48,.7),title='Before taking the quotient')
ax[1].plot([-.4,.4],[0,0],color='#34495e',lw=3)
ax[1].annotate('Image of the zero interval',xy=(0,0),xytext=(0,.22),ha='center',fontsize=9,
 arrowprops={'arrowstyle':'->','color':'#34495e'})
ax[1].set(xlabel='Re w = y',ylabel='Im w = -beta(t)',xlim=(-.5,.5),ylim=(-.46,.46),title='w = y - i beta(t)')
u=np.linspace(-.6,.6,251)
ax[2].plot(u,u*u,label='t = 0: coefficient 1',color='#247348',lw=2)
ax[2].plot(u,np.cos(np.exp(-1))*u*u,label='t = 2: coefficient cos(1/e)',color='#754199',lw=2,ls='--')
ax[2].set(xlabel='Inactive coordinate zeta',ylabel='Re (zeta² exp(w))',title='Quadratic normal barrier (y = 0)')
ax[2].legend(fontsize=8,loc='upper center')
for a in ax:a.grid(alpha=.2)
out=HERE/'reduced-coordinate-and-normal-barrier.svg'
fig.savefig(out,metadata={'Date':None,'Creator':'Independent AN-04 exposition, CC0-1.0'});plt.close(fig)
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
record={'svg':'figures/'+out.name,'svg_sha256':sha(out),'generator_sha256':sha(Path(__file__)),
 'coordinate_source':'RLP:X3 and F0','exact_formulae':{'beta':'sign(t)*exp(-1/(abs(t)-1)) for abs(t)>1; zero otherwise',
 'coordinate':'w=y-i*beta(t)','barrier_at_y_zero':'zeta^2*cos(beta(t))'},
 'sampled_for_illustration':True,'numerical_integral_used':False,'scope':'The recorded calculations and diagrams concern the stated examples. The general analytic assertions use the written arguments.',
                                          'licence':'CC0-1.0'}
(HERE.parent/'figure-check.json').write_text(json.dumps(record,indent=2)+'\n','utf-8')
print(json.dumps({'figure_bytes':out.stat().st_size,'sha256':sha(out)}))
