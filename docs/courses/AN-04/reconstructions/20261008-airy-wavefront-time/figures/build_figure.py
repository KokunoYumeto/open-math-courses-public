"""Exact affine glancing time projection and normalized Airy samples. CC0."""
from pathlib import Path
import hashlib,json
import numpy as np
from scipy.special import airy
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
matplotlib.rcParams.update({'svg.fonttype':'path','svg.hashsalt':'AN04-airy-time-layer',
 'font.size':11,'axes.spines.top':False,'axes.spines.right':False})
P=Path(__file__).resolve().parent
fig,(ax,bx)=plt.subplots(1,2,figsize=(10.4,4.8))
for ep,col,label in [(1,'#a25630',r'$F_+$: past'),(-1,'#16677a',r'$F_-$: future')]:
    ss=ep*np.linspace(0,.85,250)
    ax.plot(ss**2,-ss-2*ss**3/3,color=col,lw=2.4,label=label)
    a,b=ep*.5,ep*.59
    ax.annotate('',xy=(b*b,-b-2*b**3/3),xytext=(a*a,-a-2*a**3/3),
                arrowprops={'arrowstyle':'->','color':col,'lw':2})
ax.scatter([0],[0],color='#172d3e',s=28,zorder=4)
ax.axhline(0,color='#85939c',lw=.8,ls=':');ax.axvline(0,color='#172d3e',lw=1.2)
ax.set(xlim=(-.05,.8),ylim=(-1.4,1.4),xlabel=r'$q=s^2$',ylabel=r'physical time $t=-s-2s^3/3$')
ax.set_title('The two branches of one glancing ray');ax.legend(loc='upper left',frameon=False)
ax.text(.37,.02,r'$H_p t<0$',color='#314452')
qs=np.linspace(0,.5,501)
for L,col in [(8,'#a25630'),(64,'#637b32'),(512,'#16677a')]:
    a=(.25-qs)*L**(2/3);b=.25*L**(2/3)
    ai,_,bi,_=airy(a);aib,_,bib,_=airy(b)
    vals=np.abs((ai-1j*bi)/(aib-1j*bib))
    bx.semilogy(qs,vals,color=col,lw=2,label=fr'$\lambda={L}$')
bx.axvline(.25,color='#85939c',ls='--',lw=1)
bx.set(xlim=(0,.5),ylim=(1e-20,2),xlabel=r'$q$',ylabel=r'$|F((1/4-q)\lambda^{2/3})/F(\lambda^{2/3}/4)|$')
bx.set_title('Elliptic boundary value, interior decay');bx.legend(frameon=False,loc='lower left')
bx.text(.258,1e-4,r'$q=r=1/4$',fontsize=10,color='#425461')
fig.tight_layout(w_pad=2.7)
out=P/'airy-time-and-layer.svg';fig.savefig(out,metadata={'Date':None});plt.close(fig)
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
record={'svg':'figures/'+out.name,'svg_sha256':sha(out),'generator_sha256':sha(Path(__file__)),
 'coordinates':{'ray':'q=s^2, t=-s-2s^3/3','s_range':['-17/20','17/20'],'omitted_z':'-s+2s^3/3',
 'elliptic_r':'1/4','lambda':[8,64,512],'q_range':[0,'1/2']},
 'ray_projection_exact':True,'airy_profiles_are_numerical_samples':True,'proof_locator':'**F0. Exact coordinates of the figure.**',
 'actually_inspected':False,'exact_coordinate_review_complete':False,'licence':'CC0-1.0'}
(P.parent/'figure-check.json').write_text(json.dumps(record,indent=2)+'\n','utf-8')
print(json.dumps({'svg_bytes':out.stat().st_size,'svg_sha256':sha(out)}))
