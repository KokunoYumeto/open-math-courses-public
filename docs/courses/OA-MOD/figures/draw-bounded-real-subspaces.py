"""Exact real and imaginary coordinate planes for RS7 at q=2."""
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np

plt.rcParams.update({'svg.fonttype':'none','svg.hashsalt':'oa-mod-rs7-v1','font.size':11})
out=Path(__file__).resolve().parent
fig,axes=plt.subplots(1,2,figsize=(11,5.2),constrained_layout=True)
t=np.array([-3.,3.])
for ax,sign,title in zip(axes,[1,-1],['Real coordinates','Imaginary coordinates']):
    ax.set_aspect('equal')
    ax.plot(t,sign*2*t,color='#1f5f99',lw=2.5,label=r'$K_2$')
    ax.plot(t,-sign*2*t,color='#bc6a28',lw=2,label=r'$iK_2$')
    ax.plot(t,sign*t/2,color='#267a4a',lw=2.5,label=r'$E=K_{1/2}$')
    src=(1,sign*2);dst=(2,sign)
    ax.scatter([src[0],dst[0]],[src[1],dst[1]],c=['#1f5f99','#267a4a'],s=38,zorder=5)
    ax.annotate('',xy=dst,xytext=src,arrowprops={'arrowstyle':'->','lw':1.7,'color':'#555555','connectionstyle':'arc3,rad=-0.22'})
    ax.text(1.55,sign*1.6,r'$J$',ha='center',va='center')
    ax.annotate('(1, '+str(sign*2)+')',src,xytext=(-40,10 if sign==1 else -20),textcoords='offset points')
    ax.annotate('(2, '+str(sign)+')',dst,xytext=(5,8 if sign==1 else -18),textcoords='offset points')
    ax.set_xlim(-2.6,2.85);ax.set_ylim(-2.6,2.85)
    ax.set_xticks([-2,-1,0,1,2]);ax.set_yticks([-2,-1,0,1,2])
    ax.axhline(0,color='#bbbbbb',lw=.8);ax.axvline(0,color='#bbbbbb',lw=.8);ax.grid(alpha=.12)
    ax.spines[['top','right']].set_visible(False)
    ax.set_xlabel('First coordinate');ax.set_ylabel('Second coordinate');ax.set_title(title)
    ax.legend(loc='lower left',framealpha=.95,fontsize=10)
fig.suptitle(r'$q=2:\quad R=\mathrm{diag}(2/5,8/5),\quad T=(4/5)I,\quad J(u,v)=(\overline{v},\overline{u})$',fontsize=13)
fig.savefig(out/'bounded-real-subspaces.svg',metadata={'Date':None})
fig.savefig(out/'bounded-real-subspaces.png',dpi=150)
plt.close(fig)
