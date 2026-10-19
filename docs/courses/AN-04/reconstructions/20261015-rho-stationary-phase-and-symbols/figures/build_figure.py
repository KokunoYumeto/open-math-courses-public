"""Draw exact stationary scales and sampled sharp-model remainders; CC0-1.0."""
from pathlib import Path
import json,hashlib
import numpy as np
import matplotlib
matplotlib.use('Agg')
matplotlib.rcParams.update({'svg.fonttype':'none','font.size':10,'font.family':'DejaVu Sans'})
import matplotlib.pyplot as plt
HERE=Path(__file__).resolve().parent
lam=np.geomspace(1,2**20,401)
fig,axs=plt.subplots(1,3,figsize=(13.5,4.6),gridspec_kw={'width_ratios':[1,1.35,1.15]})
fig.subplots_adjust(left=.035,right=.99,top=.83,bottom=.20,wspace=.34)
ax=axs[0]
ax.set_title('A. Two transverse scales\nrho = 3/4, lambda = 4096',pad=14)
for y,r,color,label in [(1,1/8,'#156082','amplitude variation: +/- 1/8'),(.35,1/64,'#a43628','Fresnel: +/- 1/64')]:
 ax.plot([-r,r],[y,y],lw=5,color=color,solid_capstyle='butt')
 ax.scatter([-r,0,r],[y,y,y],c=color,s=[25,12,25])
 ax.text(0,y+.15,label,ha='center',fontsize=10)
ax.set_xlim(-.15,.15);ax.set_ylim(0,1.55);ax.set_xticks([-.125,0,.125],['-1/8','0','1/8'])
ax.set_yticks([]);ax.set_xlabel('normal coordinate z')
ax.text(.5,-.20,'z = lambda^(-1/4) v\nnew parameter = 64',ha='center',va='top',transform=ax.transAxes)
for side in ['left','right','top']:ax.spines[side].set_visible(False)
ax=axs[1];ax.set_title('B. Exact model and upper bound',pad=14)
curves=[]
for rho,label,color in [(.6,'rho=3/5','#156082'),(.75,'rho=3/4','#a43628'),(1.,'rho=1','#376f3e')]:
 eps=2*rho-1;actual=2*np.sin(lam**(-eps)/4);bound=.5*lam**(-eps)
 assert np.all(actual<=bound+1e-15) and np.all(actual>0)
 ax.loglog(lam,actual,c=color,label=label,lw=2)
 ax.loglog(lam,bound,c=color,ls='--',lw=.8,alpha=.8)
 curves.append({'rho':rho,'epsilon':eps,'sample_count':len(lam),
  'formula':'2 sin(lambda^(-epsilon)/4)','upper_bound':'lambda^(-epsilon)/2'})
ax.set_xlabel('lambda');ax.set_ylabel('normalized leading remainder')
ax.legend(fontsize=9,loc='lower left');ax.grid(alpha=.17,which='major')
ax=axs[2];ax.set_title('C. The endpoint retains an error',pad=14)
endpoint=2*np.sin(.25)
ax.semilogx(lam,np.full_like(lam,endpoint),c='#a43628',lw=2,label='rho=1/2')
ax.semilogx(lam,2*np.sin(lam**(-.5)/4),c='#156082',lw=2,label='rho=3/4')
ax.set_ylim(-.01,.57);ax.set_xlabel('lambda');ax.set_ylabel('normalized leading remainder')
ax.legend(fontsize=9);ax.grid(alpha=.17)
ax.text(10,.525,'constant = 2 sin(1/4)',fontsize=9,color='#a43628')
out=HERE/'rho-stationary-scales.svg'
fig.savefig(out,metadata={'Date':None,'Creator':'Independent AN-04 figure; CC0-1.0'});plt.close(fig)
raw=out.read_bytes()
assert b'<text' in raw and b'<font' not in raw and b'base64' not in raw
check={'svg':'figures/'+out.name,'svg_sha256':hashlib.sha256(raw).hexdigest(),
 'generator_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
 'scale_panel':{'rho':'3/4','delta':'1/4','epsilon':'1/2','lambda':4096,
 'amplitude_scale':'1/8','Fresnel_scale':'1/64','rescaled_parameter':64},
 'sampled_curves':curves,'endpoint':{'rho':'1/2','exact_error':'2 sin(1/4)'},
 'samples_are_not_a_proof':True,'embedded_font_files':False,'scope':'The recorded calculations and diagrams concern the stated examples. The general analytic assertions use the written arguments.'}
(HERE.parent/'figure-check.json').write_text(json.dumps(check,indent=2)+'\n','utf-8')
print(json.dumps({'svg':str(out),'samples':len(lam),'embedded_font_files':False}))
