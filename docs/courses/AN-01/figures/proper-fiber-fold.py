"""Exact proper fold and its integrated density, AN01-U103 Exercise 5; CC0."""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
matplotlib.rcParams.update({'font.size':12,'svg.hashsalt':'AN01-U103-proper-fold','text.usetex':False})
D=Path(__file__).resolve().parent
blue='#17659b';orange='#bd6508';green='#147652';dark='#24354a'
fig,axs=plt.subplots(1,2,figsize=(12,6.7))
t=np.linspace(-1.75,1.75,401);ax=axs[0]
ax.axhline(0,color='#c2cbd4',lw=.8);ax.axvline(0,color='#c2cbd4',lw=.8)
ax.plot(t*t,t,color=blue,lw=2.5,label=r'$(x,y)=(t^2,t)$')
for s in [-1.25,-.6,0,.6,1.25]:
 start=np.array([s*s,s]);end=start+.32*np.array([1,-2*s])
 ax.annotate('',xy=end,xytext=start,arrowprops=dict(arrowstyle='->',lw=2,color=green if s==0 else orange))
ax.scatter([0],[0],s=35,color=green,zorder=4)
ax.text(.42,.12,r'$(1,0)$ at the vertex',color=green,fontsize=11)
ax.text(2.65,-1.27,r'$(1,-2t)$',color=orange,ha='center')
ax.axvline(1,color=dark,ls=':',lw=1)
ax.scatter([1,1],[-1,1],s=24,color=dark)
ax.text(.28,1.5,r'$y=\pm\sqrt{x}$',color=dark)
ax.set(xlim=(-.35,3.5),ylim=(-2,2),xlabel=r'output $x$',ylabel=r'fiber $y$')
ax.set_aspect('equal',adjustable='box')
ax.set_title('Proper fibers and their conormals\nOnly the vertex has zero fiber component')
ax.legend(loc='upper right',fontsize=10)
ax=axs[1]
x=np.linspace(.012,3.5,600)
ax.axvline(0,color='#c2cbd4',lw=.8)
ax.plot(x,1/np.sqrt(x),color=blue,lw=2.5,label=r'$x^{-1/2}$ for $x>0$')
ax.plot([-1,0],[0,0],color=blue,lw=2.5)
ax.plot(x,.5/np.sqrt(x),color=orange,ls='--',lw=1.8,label=r'each branch: $1/(2\sqrt{x})$')
ax.annotate('',xy=(.018,4.25),xytext=(.08,3.55),arrowprops=dict(arrowstyle='->',color=blue,lw=2))
ax.text(.23,3.5,'Unbounded as x approaches 0\nLocally integrable; no point mass',fontsize=11,color=dark)
ax.set(xlim=(-1,3.5),ylim=(-.18,4.35),xlabel=r'output $x$',ylabel='density')
ax.set_title('The integrated scalar density\n'+r'$\int\delta(x-y^2)\,dy=H(x)x^{-1/2}$')
ax.legend(loc='upper right',bbox_to_anchor=(1,.58),fontsize=10)
fig.suptitle('A fold concentrates a singularity at its critical value',fontsize=17,y=.98)
fig.text(.5,.035,'Exact curves and conormal directions; arrows show selected positive multiples.\nExercise 5 proves the change of variables, integrability and both output wavefront directions.',ha='center',fontsize=11)
fig.subplots_adjust(top=.82,bottom=.18,wspace=.3)
fig.savefig(D/'proper-fiber-fold.svg',metadata={'Date':None})
fig.savefig(D/'proper-fiber-fold.png',dpi=170)
plt.close(fig)
svg=D/'proper-fiber-fold.svg'
svg.write_bytes(('\n'.join(line.rstrip() for line in svg.read_text(encoding='utf-8').splitlines())+'\n').encode())
