"""Exact sections and normalized Gaussian magnitudes for AN01-U094; CC0."""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

out=Path(__file__).resolve().parent
plt.rcParams.update({'font.size':12,'svg.fonttype':'none','svg.hashsalt':'AN01-U094'})
ink='#172334';blue='#155699';orange='#b34d12';green='#27754b'
fig,(a,b)=plt.subplots(1,2,figsize=(12.2,4.8))
t=np.linspace(-2.1,2.1,201)
a.plot(t,t,color=blue,lw=2.8,label=r'Singular line $z=T$')
for q in [-1.25,0,1.25]:
 a.annotate('',xy=(q-.48,q+.48),xytext=(q,q),
            arrowprops={'arrowstyle':'->','color':orange,'lw':2})
a.set(xlim=(-2.25,2.25),ylim=(-2.25,2.25),xlabel=r'$z$',ylabel=r'$T=ct$')
a.set_aspect('equal')
a.set_title(r'Exact section $y=0$',pad=13)
a.text(-2.02,1.75,r'Positive $dT-dz$',color=orange,fontsize=12)
a.text(.25,-.92,'Covectors shown at\none chosen scale.',fontsize=9.5,color=ink)
a.grid(alpha=.16)
a.legend(loc='lower right',fontsize=10,frameon=False)
r=np.linspace(0,2.5,501)
for longitudinal,color in [(0,blue),(1,green),(2,orange)]:
 b.plot(r,np.exp(-4*r*r/(longitudinal*longitudinal+1)),color=color,lw=2.3,
        label=rf'$b={longitudinal}$')
b.set(xlabel=r'Transverse radius $r$',ylabel='Normalized magnitude',
      xlim=(0,2.5),ylim=(0,1.05))
b.set_title(r'Gaussian packets: $\lambda=4,\ \sigma=1$',pad=13)
b.axhline(np.exp(-1),color='#64748b',lw=1,ls=':')
b.text(1.82,np.exp(-1)+.025,r'$e^{-1}$',color='#64748b')
b.grid(alpha=.16)
b.legend(frameon=False)
fig.suptitle('An exact wave can be singular on just one light ray',fontsize=16,color=ink)
fig.subplots_adjust(top=.80,bottom=.17,left=.06,right=.98,wspace=.38)
svg=out/'exact-light-ray.svg'
fig.savefig(svg,bbox_inches='tight',metadata={'Date':None})
svg.write_bytes(('\n'.join(line.rstrip() for line in svg.read_text(encoding='utf-8').splitlines())+'\n').encode())
fig.savefig(out/'exact-light-ray.png',dpi=160,bbox_inches='tight')
plt.close(fig)
