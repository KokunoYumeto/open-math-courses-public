"""Exact base and cotangent geometry for AN01-U102 Exercise2; CC0."""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
matplotlib.rcParams.update({'font.size':12,'svg.hashsalt':'AN01-U102-transverse-products','text.usetex':False})
D=Path(__file__).resolve().parent
blue='#17659b';orange='#bd6508';green='#147652';dark='#24354a'
fig,axs=plt.subplots(1,2,figsize=(12,6.5))
t=np.linspace(-2.7,2.7,301)
ax=axs[0]
ax.axhline(0,color='#c2cbd4',lw=.8)
ax.axvline(0,color=blue,lw=2,label=r'$x=0$')
ax.plot(t,-t/2,color=orange,lw=2,label=r'$x+2y=0$')
ax.scatter([0],[0],s=38,color=dark,zorder=6)
for vec,color in [((1,0),blue),((1,2),orange)]:
 ax.annotate('',xy=vec,xytext=(0,0),arrowprops=dict(arrowstyle='->',color=color,lw=2.4))
ax.text(1.02,.14,r'$(1,0)$',color=blue)
ax.text(1.10,2.02,r'$(1,2)$',color=orange)
ax.text(-.12,-.16,r'$0$',ha='right',va='top')
ax.set(xlim=(-2.4,2.4),ylim=(-2.4,2.4),xlabel=r'$x$',ylabel=r'$y$')
ax.set_title('Base coordinates and selected conormals',fontsize=13,fontweight='bold',pad=14)
ax.legend(loc='lower left',framealpha=.97)
ax.text(.5,-.21,r'$\delta(x)\,\delta(x+2y)=\frac{1}{2}\delta_{(0,0)}$',transform=ax.transAxes,ha='center',fontsize=15)
ax=axs[1]
ax.axhline(0,color=blue,lw=1.8,ls='--',label=r'$(t,0),\ t\ne0$')
ax.axvline(0,color='#c2cbd4',lw=.8)
ax.plot(t,2*t,color=orange,lw=1.8,ls='--',label=r'$(s,2s),\ s\ne0$')
ax.plot([1,2],[0,2],color=orange,lw=1.2,ls=':')
ax.plot([1,2],[2,2],color=blue,lw=1.2,ls=':')
for vec,color in [((1,0),blue),((1,2),orange),((2,2),green)]:
 ax.annotate('',xy=vec,xytext=(0,0),arrowprops=dict(arrowstyle='->',color=color,lw=2.2))
ax.scatter([0],[0],s=45,facecolor='white',edgecolor=dark,zorder=8)
ax.text(2.05,2.08,r'$(2,2)$',color=green)
ax.set(xlim=(-1.65,2.8),ylim=(-1.65,2.8),xlabel=r'$\xi$',ylabel=r'$\eta$')
ax.set_title('Covectors at the intersection',fontsize=13,fontweight='bold',pad=14)
ax.legend(loc='lower right',fontsize=10,framealpha=.97)
ax.text(.5,-.21,r'$(t,0)+(s,2s)=(t+s,2s)$',transform=ax.transAxes,ha='center',fontsize=15)
for ax in axs:
 ax.set_aspect('equal',adjustable='box')
 ax.spines[['top','right']].set_visible(False)
 ax.spines[['left','bottom']].set_color('#b9c1cb')
fig.suptitle('Independent conormals produce every nonzero covector at one point',fontsize=15,y=.98)
fig.subplots_adjust(left=.07,right=.96,top=.86,bottom=.23,wspace=.34)
assert np.linalg.det(np.array([[1.,0.],[1.,2.]]))==2.
fig.savefig(D/'transverse-hyperfunction-products.png',dpi=150,facecolor='white',metadata={'Software':'GPT-6 Astra (OpenAI); reproducible CC0 figure'})
fig.savefig(D/'transverse-hyperfunction-products.svg',facecolor='white',metadata={'Date':None,'Creator':'GPT-6 Astra (OpenAI); CC0'})
p=D/'transverse-hyperfunction-products.svg';p.write_bytes(('\n'.join(x.rstrip() for x in p.read_text(encoding='utf-8').splitlines())+'\n').encode())
plt.close(fig)
