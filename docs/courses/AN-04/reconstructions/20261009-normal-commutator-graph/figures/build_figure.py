"""Boundary quadratic forms and the changed gauge domain; CC0-1.0."""
from pathlib import Path
import hashlib,json
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
matplotlib.rcParams.update({'svg.fonttype':'path','svg.hashsalt':'an04-normal-commutator-graph-v1','font.size':11})
HERE=Path(__file__).resolve().parent;MOD=HERE.parent
fig,(ax,bx)=plt.subplots(1,2,figsize=(12,5.2))
fig.subplots_adjust(left=.075,right=.98,top=.79,bottom=.18,wspace=.32)
k=np.linspace(0,2,501);lam=np.sqrt(2+k*k)
ax.plot(k,-1/lam,color='#205c78',lw=2.2,label='Dirichlet: unit normal trace')
ax.plot(k,(k*k-1)/lam,color='#a95126',lw=2.2,label='Neumann: unit value trace')
ax.axhline(0,color='#66727c',lw=.9);ax.axvline(1,color='#66727c',lw=1,ls='--')
ax.scatter([1],[0],color='#a95126',s=32,zorder=3)
ax.annotate('Glancing: r = 0',xy=(1,0),xytext=(.1,.8),arrowprops={'arrowstyle':'->','color':'#66727c'},fontsize=11)
ax.set(xlim=(0,2),ylim=(-.85,1.3),xlabel=r'Spatial frequency $k$, with $\omega=1$',ylabel='Quadratic boundary form')
ax.set_title('Neumann has a remaining signed term',fontweight='bold',pad=15)
ax.legend(loc='lower right',fontsize=9,frameon=False);ax.grid(alpha=.15)
q=np.linspace(0,1.25,501)
bx.plot(q,np.ones_like(q),color='#205c78',lw=2.2,label=r'$U(q)=1,\quad U^\prime(0)=0$')
bx.plot(q,np.exp(-q),color='#a95126',lw=2.2,label=r'$w(q)=e^{-q},\quad w^\prime(0)=-1$')
bx.plot(q[q<=.75],1-q[q<=.75],ls='--',color='#62806d',lw=1.7,label=r'Tangent $1-q$')
bx.scatter([0],[1],color='#182d3d',s=32,zorder=3,clip_on=False)
bx.set(xlim=(0,1.25),ylim=(.15,1.18),xlabel=r'Normal coordinate $q$',ylabel='Exact scalar solution')
bx.set_title('A normal gauge changes the boundary jet',fontweight='bold',pad=15)
bx.legend(loc='lower left',fontsize=9,frameon=False);bx.grid(alpha=.15)
fig.suptitle('Normal commutators retain both the boundary form and the transformed domain',fontsize=14,fontweight='bold',y=.98)
out=HERE/'normal-commutator-boundary.svg';fig.savefig(out,metadata={'Date':None});plt.close(fig)
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
record={'svg':'figures/normal-commutator-boundary.svg','svg_sha256':sha(out),'generator_sha256':sha(Path(__file__)),
 'boundary_form_panel':{'omega':1,'k_interval':[0,2],'lambda':'sqrt(2+k^2)','Dirichlet':'-1/lambda','Neumann':'(k^2-1)/lambda','glancing_k':1,'continuous_frequency_extension':'Integer points are torus modes; curves display the exact symbol expressions.'},
 'gauge_panel':{'q_interval':[0,1.25],'C':'2i','S':'exp(q)','U':'1','w':'exp(-q)','tangent':'1-q','normal_derivatives_at_zero':[0,-1]},
 'actually_inspected':False,'exact_coordinate_review_complete':False}
(MOD/'figure-check.json').write_text(json.dumps(record,indent=2)+'\n','utf-8')
print(json.dumps({'svg':str(out),'sha256':sha(out)}))
