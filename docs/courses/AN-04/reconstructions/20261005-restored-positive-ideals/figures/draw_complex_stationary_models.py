"""Exact M1--M7 quadratic model; write only beside this reproducible source."""
from pathlib import Path
import json, hashlib
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.colors import Normalize

out=Path(__file__).resolve().parent
plt.rcParams.update({'font.family':'DejaVu Sans','font.size':14,'axes.titlesize':16,'axes.labelsize':14,'svg.fonttype':'path','svg.hashsalt':'AN04-U028-complex-stationary-exact-model-v1'})
fig,axs=plt.subplots(3,1,figsize=(8,14))
fig.subplots_adjust(top=.85,bottom=.07,left=.13,right=.92,hspace=.72)
fig.suptitle('Semipositive complex stationary phase\nExact model M1–M7',fontsize=19,y=.985)
p=1.0
x1=np.linspace(-1.5,1.5,121);x2=np.linspace(-.2,2.2,121)
X1,X2=np.meshgrid(x1,x2);im=(X2-p)**2
ax=axs[0];implot=ax.pcolormesh(X1,X2,im,cmap='Blues',norm=Normalize(0,1.5),shading='auto',rasterized=False)
ax.plot(x1,np.ones_like(x1),color='#b54e26',lw=2.5,label=r'$\operatorname{Im} f=0$: $x_2=1$')
ax.annotate('',xy=(1.1,1.55),xytext=(-1.1,1.55),arrowprops={'arrowstyle':'<->','color':'#1e293b','lw':2})
ax.text(0,1.75,r'$x_1$ direction: imaginary Hessian is null',ha='center',fontsize=12)
ax.set(xlabel=r'Real coordinate $x_1$',ylabel=r'Real coordinate $x_2$',xlim=(-1.5,1.5),ylim=(-.2,2.2))
ax.set_title('A. Exact real plane, p = 1\n'+r'$\operatorname{Im} f=(x_2-1)^2$,  $\operatorname{Im} f_{xx}=\mathrm{diag}(0,2)$',pad=13)
ax.legend(loc='lower center',fontsize=12)
cb=fig.colorbar(implot,ax=ax,fraction=.04,pad=.025);cb.ax.set_title(r'$\operatorname{Im} f$',fontsize=12,pad=9)

ax=axs[1];u=np.linspace(-1,2,601);T=.8+.4j;theta=.5*np.arctan(.5)
ax.plot(u,np.zeros_like(u),color='#1e293b',lw=2.3,label='Original real contour')
for s in [.25,.5,.75]:ax.plot(u,np.full_like(u,.4*s),color='#94a3b8',lw=1.2,ls='--')
ax.plot(u,np.full_like(u,.4),color='#176b8d',lw=2.1,label=r'Translate to $\operatorname{Im}z_2=2/5$')
v=np.linspace(-1.8,1.5,601);z=T+np.exp(1j*theta)*v
ax.plot(z.real,z.imag,color='#b54e26',lw=2.3,label=r'Rotate by $\theta_2=\frac{1}{2}\arctan(1/2)$')
ax.plot([T.real],[T.imag],'o',color='#6d4894',ms=8)
ax.annotate(r'$T_2=4/5+2i/5$',xy=(.8,.4),xytext=(1.04,.72),fontsize=13,arrowprops={'arrowstyle':'->','color':'#6d4894'})
ax.annotate('',xy=(-.65,.4),xytext=(-.65,0),arrowprops={'arrowstyle':'->','color':'#176b8d','lw':2})
ax.set(xlabel=r'$\operatorname{Re}z_2$',ylabel=r'$\operatorname{Im}z_2$',xlim=(-1,2),ylim=(-.25,1))
ax.set_title('B. Actual analytic model contours, p = 1\nFinite plotting window; virtual point is nonreal',pad=13)
ax.legend(loc='lower right',fontsize=11);ax.grid(alpha=.2)

ax=axs[2];ps=np.linspace(-1.5,1.5,1001)
for t,col in [(1,'#176b8d'),(4,'#b54e26'),(16,'#6d4894')]:ax.plot(ps,np.exp(-t*ps**2/5),lw=2.5,color=col,label=r'$t='+str(t)+'$')
ax.set(xlabel=r'Real parameter $p$',ylabel=r'$|\exp(itf_0(p))|$',xlim=(-1.5,1.5),ylim=(0,1.05))
ax.set_title('C. Exact critical-value damping\n'+r'$f_0=(2+i)p^2/5$,  $\operatorname{Im}f_0=\frac{5}{4}|\operatorname{Im}T|^2$',pad=13)
ax.legend(loc='lower center',ncol=3,fontsize=12);ax.grid(alpha=.2)
for ext in ['svg','png']:fig.savefig(out/f'complex-stationary-models.{ext}',dpi=160,metadata={'Date':None} if ext=='svg' else {'Software':'Matplotlib; exact AN04 U028 model M1–M7'})
plt.close(fig)
files={f.name:hashlib.sha256(f.read_bytes()).hexdigest() for f in [out/'complex-stationary-models.svg',out/'complex-stationary-models.png',Path(__file__).resolve()]}
record={'schema':'an04-u028-exact-model-figure/v1','phase':'x1^2/2+x2^2/2+i(x2-p)^2','p_panels_A_B':1,'hessian':[[1,0],[0,'1+2i']],'imaginary_hessian':[[0,0],[0,2]],'T2':'(4+2i)p/5','f0':'(2+i)p^2/5','translation_y':'0 <= y <= 2p/5, p=1','translation_min_imaginary_part':'p*y-5*y^2/4','rotation_theta1':'0 <= theta1 <= pi/4','rotation_theta2':'0 <= theta2 <= arctan(1/2)/2','final_imaginary_part':'p^2/5+u1^2/2+sqrt(5)*u2^2/2','damping_t':[1,4,16],'schematic':False,'finite_plotting_window':True,'proof_locators':['M1','M2','M3','M4','M5','M6','M7','B1','B2'],'file_sha256':files}
(out/'complex-stationary-models.json').write_text(json.dumps(record,indent=2)+'\n',encoding='utf-8')
print(json.dumps(record))
