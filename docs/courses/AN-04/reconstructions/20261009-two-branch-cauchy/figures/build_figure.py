"""Exact Hamilton base projections and the two-jet cancellation example. CC0."""
from pathlib import Path
import hashlib,json
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
matplotlib.rcParams.update({'svg.fonttype':'path','svg.hashsalt':'AN04-two-branch-cauchy',
 'font.size':11,'axes.spines.top':False,'axes.spines.right':False})
P=Path(__file__).resolve().parent
fig,(a,b)=plt.subplots(1,2,figsize=(10.4,4.7))
t=np.linspace(0,1,101)
a.plot(-.75*t,t,color='#16677a',lw=2.5,label=r'$\lambda_+=3/4,\ x=-3t/4$')
a.plot(1.25*t,t,color='#a25630',lw=2.5,label=r'$\lambda_-=-5/4,\ x=5t/4$')
a.scatter([0],[0],color='#253c4d',s=28,zorder=3)
a.set(xlim=(-1,1.5),ylim=(-.05,1.1),xlabel='x',ylabel='t',title='Two signed Hamilton rays\n'+r'$\beta=1/4,\ C=1,\ \xi=1$')
a.legend(frameon=False,loc='upper left',fontsize=9)
b.plot([-1,1],[0,0],color='#8a9ca5',lw=3,ls='--',label='t = 0: position identically zero')
b.plot([-1,-.5],[0,0],color='#16677a',lw=2)
b.plot([-.5,.5],[.5,.5],color='#16677a',lw=2.5,label='t = 1/2: two jumps')
b.plot([.5,1],[0,0],color='#16677a',lw=2)
b.scatter([-.5,-.5,.5,.5],[0,.5,0,.5],facecolors='white',edgecolors='#16677a',zorder=5,s=35)
b.vlines([-.5,.5],0,.5,color='#16677a',ls=':',alpha=.6)
b.set(xlim=(-1,1),ylim=(-.12,.86),xlabel='x',ylabel='u(t,x)',title='The other initial jet carries the singularity')
b.text(-.92,.61,r'$\partial_tu(0)=\delta_0$',fontsize=12)
b.legend(frameon=False,loc='lower left',fontsize=9)
fig.tight_layout(w_pad=2)
out=P/'two-branches-and-cauchy-jets.svg'
fig.savefig(out,metadata={'Date':None});plt.close(fig)
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
record={'svg':'figures/'+out.name,'svg_sha256':sha(out),'generator_sha256':sha(Path(__file__)),
 'coordinates':{'left':{'beta':'1/4','C':1,'xi':1,'rays':['x=-3t/4','x=5t/4'],'time_covectors':['3/4','-5/4'],'time_interval':[0,1]},
 'right':{'times':[0,'1/2'],'positive_time_height':'1/2','positive_time_jumps':['-1/2','1/2']}},
 'base_projections_not_full_phase_space':True,'endpoint_values_distributionally_immaterial':True,
 'proof_locator':'**F0. Exact coordinates of the figure.**','exact_functions':True,
 'actually_inspected':False,'exact_coordinate_review_complete':False,'licence':'CC0-1.0'}
(P.parent/'figure-check.json').write_text(json.dumps(record,indent=2)+'\n','utf-8')
print(json.dumps({'svg_bytes':out.stat().st_size,'svg_sha256':sha(out)}))
