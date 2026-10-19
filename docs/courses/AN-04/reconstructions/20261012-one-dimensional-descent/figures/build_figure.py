"""Exact coordinate plots for ODD:X2 and F0; no numerical integration."""
from pathlib import Path
import hashlib,json
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
HERE=Path(__file__).resolve().parent
plt.rcParams.update({'svg.fonttype':'none','font.size':10})
fig,axes=plt.subplots(2,2,figsize=(12,8),layout='constrained')
a,b,c,d=axes.flat
def beta(t):
 return np.sign(t)*np.exp(-1/(abs(t)-1)) if abs(t)>1 else 0.
def h(t):
 return np.exp(-1/(abs(t)-1))/(abs(t)-1)**2 if abs(t)>1 else 0.
ts=np.linspace(-2,2,801)
a.axvspan(-1,1,color='#e7edf3')
a.plot(ts,[beta(t) for t in ts],label='beta(t)',color='#16627b',lw=2)
a.plot(ts,[h(t) for t in ts],label="h(t) = beta'(t)",color='#b36e18',lw=2)
a.set(xlabel='t',title='Exact smooth primitive and coefficient',ylim=(-.43,.63))
a.legend(fontsize=9)
b.axvspan(-1,1,color='#e7edf3')
ys=np.linspace(-.5,.5,5)
for y in ys:
 b.plot([-2,2],[y,y],lw=1,color='#16627b')
 b.plot([-1,1],[y,y],lw=3,color='#805694')
 c.plot([-np.exp(-1),np.exp(-1)],[y,y],lw=1,color='#16627b')
 c.plot([0],[y],marker='o',ms=5,color='#805694')
for t in [-2,-1.5,-1.2,1.2,1.5,2]:
 b.plot([t,t],[-.5,.5],color='#789ba8',lw=.8)
 c.plot([beta(t),beta(t)],[-.5,.5],color='#789ba8',lw=.8)
b.set(xlabel='t',ylabel='y',title='Original surface: each purple interval collapses',
      xlim=(-2.15,2.15),ylim=(-.65,.65))
c.axvline(0,color='#805694',lw=2)
c.set(xlabel='Re w = beta(t)',ylabel='Im w = y',
      title='Reduced strip: w = beta(t) + i y',
      xlim=(-.43,.43),ylim=(-.65,.65))
bs=np.linspace(-np.exp(-1),np.exp(-1),401)
d.plot(bs,-bs*bs,color='#16627b',lw=2,label='F(beta) = -beta²')
bb=np.exp(-1)
d.plot([-bb,bb],[-bb*bb,-bb*bb],color='#b36e18',ls='--',label='Endpoint chord')
d.set(xlabel='beta',ylabel='Comparison value',title='Concavity on the quotient interval')
d.legend(fontsize=9)
for ax in axes.flat:ax.grid(alpha=.17)
out=HERE/'constant-variable-descent.svg'
fig.savefig(out,metadata={'Date':None,'Creator':'Independent AN-04 exposition, CC0-1.0'})
plt.close(fig)
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
record={'svg':'figures/'+out.name,'svg_sha256':sha(out),'generator_sha256':sha(Path(__file__)),
 'coordinate_source':'ODD:X2 and F0','exact_formulae':{
  'beta':'sign(t)*exp(-1/(abs(t)-1)) outside [-1,1]; zero inside',
  'h':'exp(-1/(abs(t)-1))/(abs(t)-1)^2 outside [-1,1]; zero inside',
  'complex_coordinate':'w=beta(t)+i*y','comparison':'F(beta)=-beta^2'},
 'sampled_for_illustration':True,'numerical_integral_used':False,'scope':'The recorded calculations and diagrams concern the stated examples. The general analytic assertions use the written arguments.',
                                          'licence':'CC0-1.0'}
(HERE.parent/'figure-check.json').write_text(json.dumps(record,indent=2)+'\n','utf-8')
print(json.dumps({'figure_bytes':out.stat().st_size,'sha256':sha(out)}))
