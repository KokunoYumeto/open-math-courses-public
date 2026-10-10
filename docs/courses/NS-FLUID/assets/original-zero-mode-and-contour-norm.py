"""Original zero-mode receiver and exact nonorthogonal contour norm."""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
O=Path(__file__).resolve().parent
plt.rcParams.update({'font.size':14,'axes.grid':True,'grid.alpha':.2,'figure.facecolor':'#f8fafc','savefig.facecolor':'#f8fafc'})
fig,ax=plt.subplots(1,2,figsize=(12,5.6))
a=2.;r=np.linspace(.001,9,900);u=np.where(r<=a,r/2,a*a/(2*r))
ax[0].plot(r,u,lw=2.6,color='#2357a0');ax[0].axvline(a,ls='--',color='#67717c')
ax[0].set(xlabel='Original radius r',ylabel='Tangential velocity',title='A retained zero angular vorticity mode')
ax[0].text(3.6,.75,r'$u^\theta=a^2/(2r)$',color='#2357a0')
ax[0].text(.2,.15,r'$u^\theta=r/2$',color='#2357a0')
ks=np.linspace(0,12,300);norm=np.sqrt(1+ks*ks/10)
ax[1].plot(ks,norm,lw=2.6,color='#14745e')
ax[1].set(xlabel=r'Original coupling $|k|$',ylabel=r'Exact contour norm $\|P\|$',title='Fixed eigenvalues; varying contour norm')
ax[1].text(.7,3.3,r'$\lambda_0=2+i,\ \mu=-1$',fontsize=14)
ax[1].text(.7,2.9,r'$\|P\|=\sqrt{1+|k|^2/10}$',fontsize=14)
fig.suptitle('The entire receiver and the actual spectral projection both matter',fontsize=18)
fig.text(.5,.04,'EX1–EX3: a = 2.  EX7–EX10: exact matrix example; no vortex eigenvalue is numerically asserted.',ha='center',fontsize=11)
fig.tight_layout(rect=(0,.1,1,.93))
for ext in ['png','svg']:fig.savefig(O/('original-zero-mode-and-contour-norm.'+ext),dpi=150)
print('Exact receiver and matrix figure rendered.')

