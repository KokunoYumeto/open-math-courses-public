"""Exact kernel-support bound and boundary-jet profiles. Independent illustration, CC0."""
from pathlib import Path
import hashlib,json
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
matplotlib.rcParams.update({'svg.fonttype':'path','svg.hashsalt':'AN04-boundary-preserving-localization','font.size':11,'axes.spines.top':False,'axes.spines.right':False})
P=Path(__file__).resolve().parent
fig,(ax,bx)=plt.subplots(1,2,figsize=(10.4,4.8))
x=np.linspace(0,1/3,251)
ax.fill_between(x,x/2,2*x,color='#cee4e8')
ax.plot(x,x/2,color='#16677a',lw=2,label=r'$q_{\rm in}=q_{\rm out}/2$')
ax.plot(x,2*x,color='#a25630',lw=2,label=r'$q_{\rm in}=2q_{\rm out}$')
ax.axvline(1/3,color='#738892',lw=1,ls='--')
ax.set(xlim=(0,.4),ylim=(0,.73),xlabel=r'$q_{\rm out}$',ylabel=r'$q_{\rm in}$')
ax.set_title('A permitted normal kernel support')
ax.legend(frameon=False,loc='upper left',fontsize=10)
ax.text(.075,.025,'Support bound only; kernel values are not shown.',fontsize=8.5,color='#415664')
q=np.linspace(0,.5,251)
bx.plot(q,(1+q*q)*np.exp(-q*q),color='#16677a',lw=2.5,label=r'$(1+q^2)e^{-q^2}$; slope $0$ at $0$')
bx.plot(q,(1+q)*np.exp(-q*q),color='#a25630',lw=2.5,ls='--',label=r'$(1+q)e^{-q^2}$; slope $1$ at $0$')
bx.plot([0,.12],[1,1],color='#16677a',lw=1,ls=':')
bx.plot([0,.12],[1,1.12],color='#a25630',lw=1,ls=':')
bx.scatter([0],[1],color='#243b4b',s=25,zorder=4)
bx.set(xlim=(0,.5),ylim=(.93,1.22),xlabel=r'$q$',ylabel='localized profile at t = 0')
bx.set_title('The boundary multiplier jet matters')
bx.legend(frameon=False,loc='lower left',fontsize=9.5)
fig.tight_layout(w_pad=2.8)
out=P/'normal-support-and-boundary-jets.svg';fig.savefig(out,metadata={'Date':None});plt.close(fig)
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
record={'svg':'figures/'+out.name,'svg_sha256':sha(out),'generator_sha256':sha(Path(__file__)),
 'coordinates':{'support':'q_out/2 <= q_in <= 2 q_out','q_out_range':[0,'1/3'],'profiles':['(1+q^2) exp(-q^2)','(1+q) exp(-q^2)'],'q_range':[0,'1/2'],'boundary_slopes':[0,1]},
 'support_region_not_kernel_values':True,'exact_functions':True,'proof_locator':'**F0. Exact figure coordinates.**',
 'actually_inspected':False,'exact_coordinate_review_complete':False,'licence':'CC0-1.0'}
(P.parent/'figure-check.json').write_text(json.dumps(record,indent=2)+'\n','utf-8')
print(json.dumps({'svg_bytes':out.stat().st_size,'svg_sha256':sha(out)}))
