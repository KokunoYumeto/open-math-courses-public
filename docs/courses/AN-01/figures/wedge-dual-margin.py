"""Exact cone example for AN01-U081; original, CC0. numpy/matplotlib required."""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import Wedge,Circle

plt.rcParams.update({'font.family':'DejaVu Sans','font.size':12,'svg.hashsalt':'AN01-U081'})
fig,axes=plt.subplots(1,3,figsize=(15,5.3),layout='constrained')
blue='#246ca6';orange='#be601b';green='#22805b'
for ax in axes:
 ax.set_aspect('equal');ax.set_xlim(-1.35,1.35);ax.set_ylim(-1.3,1.35)
 ax.axhline(0,color='#abb4c1',lw=.8);ax.axvline(0,color='#abb4c1',lw=.8)
 ax.set_xticks([-1,0,1]);ax.set_yticks([-1,0,1]);ax.spines[['top','right']].set_visible(False)
ax=axes[0];ax.set_title('Imaginary approach cones')
ax.add_patch(Wedge((0,0),1.18,0,90,facecolor=blue,alpha=.16))
ax.add_patch(Wedge((0,0),1.18,30,60,facecolor=green,alpha=.37))
for angle in [0,90,30,60]:
 t=np.deg2rad(angle);ax.plot([0,1.18*np.cos(t)],[0,1.18*np.sin(t)],color=green if angle in [30,60] else blue,ls='--',lw=1.5)
ax.text(.91,.24,r'$\Gamma$',color=blue);ax.text(.42,.62,r'$\Gamma_1$',color=green)
ax.text(.93,.63,r'$\pi/6$',fontsize=11);ax.text(.5,1.06,r'$\pi/3$',fontsize=11)
ax.set_xlabel(r'$y_1$');ax.set_ylabel(r'$y_2$')
ax=axes[1];ax.set_title('Dual directions and angular margin')
ax.add_patch(Circle((0,0),1,fill=False,edgecolor='#c3cad3',lw=1))
t=np.linspace(0,np.pi/2,200);ax.plot(np.cos(t),np.sin(t),color=blue,lw=5,label=r'$D$ (closed)')
ax.plot([1,0],[0,1],'o',color=blue,ms=7)
t=np.linspace(-np.pi/12,7*np.pi/12,250);ax.plot(1.12*np.cos(t),1.12*np.sin(t),color=orange,lw=3,label=r'$M$ (open)')
for t0 in [-np.pi/12,7*np.pi/12]:ax.plot(1.12*np.cos(t0),1.12*np.sin(t0),'o',mfc='white',mec=orange,ms=6,mew=1.5)
ax.text(-.94,1.01,r'$7\pi/12$',fontsize=11);ax.text(.73,-.51,r'$-\pi/12$',fontsize=11)
ax.text(-1.24,-.91,r'$m=\cos(5\pi/12)>0$',fontsize=12)
ax.legend(loc='lower left',bbox_to_anchor=(0,-.01),frameon=False,fontsize=10)
ax.set_xlabel(r'$\theta_1$');ax.set_ylabel(r'$\theta_2$')
ax=axes[2];ax.set_title('The shifted point lies inside the tube')
ax.add_patch(Circle((0,0),1,facecolor='#edf4fa',edgecolor=blue,lw=1.4))
m=(np.sqrt(6)-np.sqrt(2))/4;theta=np.array([1.,0.]);y=m/(2*np.sqrt(2))*np.ones(2);p=y-theta
assert np.linalg.norm(p)<1
assert 1-np.linalg.norm(p)>=m*np.linalg.norm(y)/2
ax.plot(-1,0,'o',color=blue,ms=6);ax.plot(*p,'o',color=orange,ms=6)
ax.annotate('',p,-theta,arrowprops=dict(arrowstyle='->',color=orange,lw=2.5))
ax.annotate(r'$-\theta$',(-1,0),xytext=(-1.25,-.42),arrowprops=dict(arrowstyle='-',color=blue))
ax.annotate(r'$y-\theta$',p,xytext=(-.8,.56),arrowprops=dict(arrowstyle='-',color=orange))
ax.text(-.63,-.75,r'$y=\frac{m}{2\sqrt{2}}(1,1)$',fontsize=13)
ax.text(.2,.35,r'$|y-\theta|<1$',color=blue)
ax.set_xlabel('First imaginary coordinate');ax.set_ylabel('Second imaginary coordinate')
fig.suptitle('A fixed angular margin gives a holomorphic wedge',fontsize=18)
out=Path(__file__).resolve().parent
fig.savefig(out/'wedge-dual-margin.png',dpi=180)
fig.savefig(out/'wedge-dual-margin.svg',metadata={'Date':None,'Creator':'Original AN01-U081 figure; CC0'})
p=out/'wedge-dual-margin.svg';p.write_bytes(('\n'.join(s.rstrip() for s in p.read_text(encoding='utf-8').splitlines())+'\n').encode())
