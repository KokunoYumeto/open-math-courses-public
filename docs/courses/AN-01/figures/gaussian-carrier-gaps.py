"""Exact scalar illustrations for Gaussian windows and analytic directions, CC0."""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
out=Path(__file__).resolve().parent
x=np.linspace(-1.3,1.3,321);eta=np.linspace(-1.3,1.3,321)
X,Y=np.meshgrid(x,eta);phase=(Y*Y-X*X)/2
h=.6;t=np.linspace(-1.2,1.6,561)
distance=np.maximum(np.maximum(-t,t-h),0)
gain=(t*t-distance*distance)/2
piece=np.where(t<=0,0,np.where(t<=h,t*t/2,h*t-h*h/2))
assert np.max(np.abs(gain-piece))<1e-14
assert np.max(np.abs(Y*Y/2-phase-X*X/2))<1e-14
plt.rcParams.update({'font.size':12,'axes.titlesize':14,'svg.fonttype':'none','svg.hashsalt':'AN01-U111-gaussian-carrier-gaps'})
fig,axs=plt.subplots(1,2,figsize=(12.8,5.0),constrained_layout=True)
a=axs[0];im=a.contourf(X,Y,phase,levels=np.linspace(-.85,.85,35),cmap='RdBu_r',extend='both')
a.contour(X,Y,phase,levels=[-.5,0,.5],colors='#253343',linewidths=.7)
a.axvline(0,color='black',linewidth=1)
a.set(xlabel=r'Real center $x$',ylabel=r'Imaginary center $\eta$',title=r'Point source: exact growth $(\eta^2-x^2)/2$',aspect='equal')
fig.colorbar(im,ax=a,label=r'$\lambda^{-1}\log|G_\lambda\delta_0(x+i\eta)|$',shrink=.83)
a=axs[1];a.plot(t,gain,color='#125d98',linewidth=2.5)
a.axvline(0,color='#657482',linestyle=':',linewidth=1)
a.axvline(h,color='#657482',linestyle=':',linewidth=1)
a.scatter([0,h],[0,h*h/2],color='#125d98',zorder=3)
a.text(-.9,.12,'No gain from\nthis bound',ha='center',color='#455461')
a.text(.27,.33,r'$\eta^2/2$',ha='center')
a.text(1.13,.59,r'$h\eta-h^2/2$',ha='center')
a.text(.6,-.075,r'$h=0.6$',ha='center')
a.set(xlabel=r'Imaginary center $\eta$ (covector $\xi=-\eta$)',ylabel=r'Distance gain $g_h(\eta)$',title=r'Holomorphic side: bound from $\Omega=(0,h)$',ylim=(-.1,.9),xlim=(-1.2,1.6))
a.grid(alpha=.18)
for ext in ['png','svg']:
 target=out/('gaussian-carrier-gaps.'+ext)
 fig.savefig(target,dpi=170,bbox_inches='tight',metadata={'Date':None} if ext=='svg' else None)
 if ext=='svg':
  target.write_bytes(('\n'.join(line.rstrip() for line in target.read_text(encoding='utf-8').splitlines())+'\n').encode('utf-8'))
print('Exact scalar identities checked; figure saved.')
