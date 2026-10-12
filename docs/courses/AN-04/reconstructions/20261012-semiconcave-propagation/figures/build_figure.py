"""Exact comparison and clock profiles for SCP:X2, X3 and A1."""
from pathlib import Path
import hashlib,json
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
HERE=Path(__file__).resolve().parent
plt.rcParams.update({'svg.fonttype':'none','font.size':10})
fig,axs=plt.subplots(2,2,figsize=(12,8),layout='constrained')
a,b,c,d=axs.flat
left=np.linspace(-1,-.0001,350);right=np.linspace(.0001,1,350)
a.plot(left,left,color='#17647e',lw=2);a.plot(right,1-right**2,color='#17647e',lw=2)
a.plot([0],[0],'o',color='#17647e');a.plot([0],[1],'o',mfc='white',mec='#17647e',ms=7)
a.annotate('Attained value 0',xy=(0,0),xytext=(-.88,.35),arrowprops={'arrowstyle':'->'},fontsize=9)
a.set(title='Semi-concave: upward turn is allowed',xlabel='t',ylabel='F+(t)',xlim=(-1.05,1.05),ylim=(-1.1,1.15))
b.plot(left,1+left,color='#765193',lw=2);b.plot(right,-right,color='#765193',lw=2)
b.plot([0],[0],'o',color='#765193');b.plot([0],[1],'o',mfc='white',mec='#765193',ms=7)
xs=np.linspace(-.25,.5,150);b.plot(xs,1/3-5*xs/3,'--',color='#b26c19',label='Decreasing endpoint chord')
b.plot([0],[1/3],'x',color='#b26c19',ms=8)
b.set(title='Quasi-concave only: downward turn fails',xlabel='t',ylabel='F-(t)',xlim=(-1.05,1.05),ylim=(-1.1,1.15))
b.legend(fontsize=8,loc='lower left')
def flat(s):
 return np.exp(-1/s) if s>0 else 0.
def smoothstep(s):
 if s<=0:return 0.
 if s>=1:return 1.
 return flat(s)/(flat(s)+flat(1-s))
distance=np.geomspace(.4,650,1000)
for A,color in [(1,'#66954a'),(16,'#b26c19'),(256,'#17647e')]:
 c.plot(distance,[smoothstep(z/A-1) for z in distance],label='A = '+str(A),color=color,lw=2)
c.set(xscale='log',xlabel='Normalized distance / R^(-epsilon)',ylabel='Profile value',
      title='Nested profiles before radius-1/10 smoothing',ylim=(-.05,1.12))
c.legend(fontsize=9)
ts=np.linspace(-1,1,501)
d.plot(ts,ts,color='#17647e',lw=2,label='beta1 = t')
d.plot(ts,ts+ts**3/3,color='#765193',lw=2,label='beta2 = t + t³/3')
d.set(title='Two clocks on a favorable one-sign tube',xlabel='t',ylabel='Clock value')
d.legend(fontsize=9)
for ax in axs.flat:ax.grid(alpha=.18)
out=HERE/'semiconcave-comparison-and-clocks.svg'
fig.savefig(out,metadata={'Date':None,'Creator':'Independent AN-04 exposition, CC0-1.0'});plt.close(fig)
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
j={'svg':'figures/'+out.name,'svg_sha256':sha(out),'generator_sha256':sha(Path(__file__)),
 'coordinate_source':'SCP:X2, X3, A1 and F0','exact_formulae':{
  'allowed_jump':'t for t<=0; 1-t^2 for t>0',
  'forbidden_jump':'1+t for t<0; -t for t>=0',
  'obstructing_chord':'1/3-5*t/3',
  'profile':'E(s)/(E(s)+E(1-s)), E(s)=exp(-1/s) for s>0, zero otherwise; s=distance/A-1',
  'profile_thresholds':[1,16,256],
  'clocks':['t','t+t^3/3']},
 'sampled_for_illustration':True,'actual_phase_space_distance_computed':False,
 'profile_scope':'Exact scalar profiles before convolution; the full mollified distance construction and overlap proof are in A1.',
 'actually_inspected':False,'exact_coordinate_review_complete':False,'licence':'CC0-1.0'}
(HERE.parent/'figure-check.json').write_text(json.dumps(j,indent=2)+'\n','utf-8')
print(json.dumps({'figure_bytes':out.stat().st_size,'sha256':sha(out)}))
