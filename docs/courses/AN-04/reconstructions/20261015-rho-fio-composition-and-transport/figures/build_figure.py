"""Exact clean fiber and sampled sharp transport/product models; CC0-1.0."""
from pathlib import Path
import hashlib,json
import numpy as np
import matplotlib
matplotlib.use('Agg')
matplotlib.rcParams.update({'svg.fonttype':'none','font.family':'DejaVu Sans','font.size':10})
import matplotlib.pyplot as plt
HERE=Path(__file__).resolve().parent
R=np.geomspace(1,2**20,401);t=np.linspace(0,1,361)
fig,axs=plt.subplots(1,3,figsize=(14.4,4.8),gridspec_kw={'width_ratios':[1.15,1.25,1.25]})
fig.subplots_adjust(left=.035,right=.99,bottom=.19,top=.83,wspace=.36)
ax=axs[0];ax.set_title('A. One compact matching fiber',pad=15)
cx=.55*np.cos(2*np.pi*t);cy=.55*np.sin(2*np.pi*t)
ax.plot(cx,cy,c='#156082',lw=2)
for u0 in [0,.125,.25,.375,.5,.625,.75,.875]:
 v=np.array([.55*np.cos(2*np.pi*u0),.55*np.sin(2*np.pi*u0)])
 ax.plot([-1.25,v[0]],[0,v[1]],c='#a7bec9',lw=.7,zorder=0)
 ax.plot([v[0],1.25],[v[1],0],c='#a7bec9',lw=.7,zorder=0)
ax.scatter([-1.25,1.25],[0,0],c='#a43628',s=42,zorder=3)
ax.text(-1.25,-.19,'X: (0, 1)',ha='center',fontsize=9)
ax.text(1.25,-.19,'Z: (0, 1)',ha='center',fontsize=9)
ax.text(0,.75,'Y: s=0, (eta_s, eta_t)=(1,0)',ha='center',fontsize=9)
ax.text(0,0,'t mod 1\nfiber e=1',ha='center',va='center',fontsize=10,
        bbox={'facecolor':'white','edgecolor':'none','pad':2})
ax.text(0,-.9,'density dt has mass 1\nintegral U(t)V(t) dt = E11 / 2',ha='center',fontsize=9)
ax.set_xlim(-1.65,1.65);ax.set_ylim(-1.15,1.0);ax.set_aspect('equal');ax.axis('off')
ax=axs[1];ax.set_title('B. Actual transport coefficient',pad=15)
transport=[]
for rho,label,color in [(3/5,'rho=3/5','#156082'),(3/4,'rho=3/4','#a43628'),(1.,'rho=1','#376f3e')]:
 delta=1-rho;value=np.sqrt(1+delta**2*R**(2*delta))
 ax.loglog(R,value,c=color,lw=2,label=label)
 transport.append({'rho':label.removeprefix('rho='),'formula':'sqrt(1+delta^2 R^(2delta))','samples':len(R)})
ax.set_xlabel('R = xi = eta');ax.set_ylabel('|coefficient of PA / b|')
ax.grid(alpha=.16);ax.legend(fontsize=9,loc='upper left')
ax=axs[2];ax.set_title('C. Sharp product remainder',pad=15)
product=[]
for rho,label,color in [(3/5,'rho=3/5','#156082'),(3/4,'rho=3/4','#a43628')]:
 delta=1-rho;epsilon=2*rho-1
 # Stable evaluation of (R+R^delta)^delta - R^delta.
 phase=R**delta*np.expm1(delta*np.log1p(R**(delta-1)))
 value=2*np.sin(phase/2);bound=delta*R**(-epsilon)
 assert np.all(value>0) and np.all(value<=bound+1e-14)
 ax.loglog(R,value,c=color,lw=2,label=label)
 ax.loglog(R,bound,c=color,lw=.85,ls='--',alpha=.85)
 product.append({'rho':label.removeprefix('rho='),'formula':'2 sin(((R+R^delta)^delta-R^delta)/2)',
  'upper_bound':'delta R^(-epsilon)','samples':len(R)})
ax.set_xlabel('R');ax.set_ylabel('|product symbol / (a b) - 1|')
ax.grid(alpha=.16);ax.legend(fontsize=9,loc='lower left')
out=HERE/'clean-rho-composition-and-transport.svg'
fig.savefig(out,metadata={'Date':None,'Creator':'Independent AN-04 illustration; CC0-1.0'})
plt.close(fig);raw=out.read_bytes()
assert b'<text' in raw and b'<font' not in raw and b'base64' not in raw
obj={'svg':'figures/'+out.name,'svg_sha256':hashlib.sha256(raw).hexdigest(),
 'generator_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
 'matching_fiber':{'space':'R_s times (R/Z)_t','s':0,'external_states':[[0,1],[0,1]],
 'middle_covector':[1,0],'fiber_dimension':1,'integration_density':'dt, total mass 1',
 'projection':'base fiber displayed as (0.55 cos(2pi t),0.55 sin(2pi t)); fixed covectors stated',
 'matrix_integral':'E11/2','fiber_curve_samples':len(t)},
 'transport_models':transport,'product_models':product,'samples_are_not_a_proof':True,
 'embedded_font_files':False,'actually_inspected':False}
(HERE.parent/'figure-check.json').write_text(json.dumps(obj,indent=2)+'\n','utf-8')
print(json.dumps({'svg':str(out),'model_samples':len(R),'fiber_samples':len(t)}))
