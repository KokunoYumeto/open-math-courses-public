"""Original figure for H14-H15 and H27. The envelope itself is not computed."""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
R=Path(__file__).resolve().parent
x=np.linspace(-1,1,501);y=np.linspace(.001,1,401)
X,Y=np.meshgrid(x,y)
P=(np.arctan((.5-X)/Y)-np.arctan((-.5-X)/Y))/np.pi
V=np.maximum(P-4*Y/np.pi,0)
V=np.ma.masked_where(X*X+Y*Y>=1,V)
fig,axes=plt.subplots(1,2,figsize=(12,5),layout='constrained')
ax=axes[0]
im=ax.pcolormesh(X,Y,V,shading='auto',cmap='viridis',vmin=0,vmax=1)
theta=np.linspace(0,np.pi,501)
ax.plot(np.cos(theta),np.sin(theta),color='black',lw=1.2)
ax.plot([-.5,.5],[0,0],color='#d4423a',lw=5,label=r'$J=[-1/2,1/2]$')
ax.plot([0,0],[0,1],color='white',lw=1,ls='--')
ax.scatter([0],[.25],s=32,color='white',edgecolor='black',zorder=5)
ax.annotate(r'$i/4$',(0,.25),xytext=(.2,.4),arrowprops=dict(arrowstyle='->'),color='white',fontsize=12)
ax.set(xlabel=r'$x$',ylabel=r'$y$',xlim=(-1.03,1.03),ylim=(-.025,1.03),title='An explicit lower barrier, not the envelope')
ax.set_aspect('equal');ax.legend(loc='upper right',fontsize=9)
fig.colorbar(im,ax=ax,label=r'$v_0=\max(p_J-4y/\pi,0)$',shrink=.75)
ax=axes[1]
yy=np.linspace(.001,1,1001)
vv=np.maximum(2*np.arctan(1/(2*yy))/np.pi-4*yy/np.pi,0)
c0=(2*np.arctan(2)-1)/np.pi
ax.plot(yy,vv,color='#17648f',lw=2,label=r'$v_0(iy)$')
ax.scatter([.25],[c0],s=45,color='#d4423a',zorder=4)
ax.axvline(.25,color='gray',lw=.8,ls=':')
ax.annotate(r'$\gamma(i/4)\geq(2\arctan 2-1)/\pi$'+'\n'+f'lower bound ≈ {c0:.4f}',(.25,c0),xytext=(.36,.67),arrowprops=dict(arrowstyle='->'),fontsize=11)
ax.set(xlabel=r'$y$',ylabel='Lower bound for the harmonic weight',xlim=(0,1),ylim=(0,1.04),title='Exact formula along the vertical radius')
ax.grid(alpha=.2);ax.legend(loc='upper right')
fig.suptitle('A boundary interval produces a positive harmonic weight',fontsize=15)
for ext in ['png','svg']:
 fig.savefig(R/('boundary-harmonic-barrier.'+ext),dpi=170)
svg=R/'boundary-harmonic-barrier.svg'
svg.write_text('\n'.join(line.rstrip() for line in svg.read_text(encoding='utf-8').splitlines())+'\n',encoding='utf-8')
print({'axis_value':float(c0),'interior_samples':int(V.count()),'exact_model':'H14-H15 and H27'})
