"""Original CC0 graph of the exactly specified kernel and its transform."""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
here=Path(__file__).resolve().parent
plt.rcParams.update({'font.size':24,'axes.titlesize':28,'axes.labelsize':26,
                     'xtick.labelsize':24,'ytick.labelsize':24})
fig, axes=plt.subplots(1,2,figsize=(12,5.3),layout='constrained')
u=np.linspace(-15,15,2500)
K=4*np.pi*np.cos(u/2)**2/(np.pi**2-u**2)**2
axes[0].plot(u,K,color='#153f68',lw=3)
axes[0].fill_between(u,0,K,color='#153f68',alpha=.18)
axes[0].set(title='Positive kernel',xlabel='$u$',ylabel='$K(u)$',xlim=(-15,15),ylim=(0,.145))
axes[0].set_xticks([-10,0,10]);axes[0].set_yticks([0,.05,.1])
v=np.linspace(-1.2,1.2,2000)
w=np.where(abs(v)<=1,(1-abs(v))*np.cos(np.pi*v)+np.sin(np.pi*abs(v))/np.pi,0)
axes[1].plot(v,w,color='#153f68',lw=3)
axes[1].fill_between(v,0,w,color='#153f68',alpha=.18)
axes[1].plot([-.5,.5],[1/np.pi,1/np.pi],'--',color='#a75038',lw=2.5)
axes[1].plot([-.5,.5],[1/np.pi,1/np.pi],'o',color='#a75038',ms=7)
axes[1].text(.11,.39,r'$1/\pi$',color='#a75038',fontsize=25)
axes[1].set(title='Frequency window',xlabel='$v$',ylabel='$w(v)$',xlim=(-1.2,1.2),ylim=(0,1.08))
axes[1].set_xticks([-1,0,1]);axes[1].set_yticks([0,.5,1])
for ax in axes:ax.grid(alpha=.16)
fig.savefig(here/'positive_kernel.png',dpi=180)
