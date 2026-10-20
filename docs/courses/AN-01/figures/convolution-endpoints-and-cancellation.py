from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
plt.rcParams.update({'font.size':12,'svg.hashsalt':'AN01-U033-endpoints-cancellation'})
out=Path(__file__).resolve().parent
fig,axes=plt.subplots(1,2,figsize=(12.5,5.3),layout='constrained')
x=np.linspace(-3,3,1801)
axes[0].plot(x,np.exp(-abs(x)),color='#212c39',lw=2.4,label=r'$k(x)=e^{-|x|}$')
for e,c in [(1,'#b34e2d'),(.3,'#11768a')]:
    y=np.where(abs(x)>=e,np.exp(-abs(x))*np.sinh(e)/e,(1-np.exp(-e)*np.cosh(x))/e)
    axes[0].plot(x,y,color=c,lw=2,label=rf'$k*\eta_\varepsilon,\ \varepsilon={e:g}$')
axes[0].set(xlabel='$x$',ylabel='kernel average',title='Unit mass concentrating at zero',ylim=(0,1.08))
axes[0].legend(loc='upper right',fontsize=11)
x=np.geomspace(1.1,100,1000)
positive=4/(np.sqrt(x+1)+np.sqrt(x-1))
# Stable rationalization of twice the second difference of sqrt(x).
negative=4/((np.sqrt(x+1)+np.sqrt(x))*(np.sqrt(x)+np.sqrt(x-1))*(np.sqrt(x+1)+np.sqrt(x-1)))
axes[1].loglog(x,positive,color='#b34e2d',lw=2.3,label='positive interval input')
axes[1].loglog(x,negative,color='#11768a',lw=2.3,label='mean-zero interval input')
axes[1].loglog(x,2*x**(-.5),'--',color='#b34e2d',alpha=.55,label=r'$2x^{-1/2}$')
axes[1].loglog(x,.5*x**(-1.5),'--',color='#11768a',alpha=.55,label=r'$\frac{1}{2}x^{-3/2}$')
axes[1].set(xlabel='$x>1$',ylabel='absolute potential',title='One extra power from zero mean')
axes[1].legend(loc='lower left',fontsize=11)
for ax in axes:
    ax.grid(alpha=.17)
    ax.spines[['top','right']].set_visible(False)
name='convolution-endpoints-and-cancellation'
fig.savefig(out/(name+'.png'),dpi=170)
fig.savefig(out/(name+'.svg'),metadata={'Date':None})
p=out/(name+'.svg');p.write_text('\n'.join(l.rstrip() for l in p.read_text(encoding='utf-8').splitlines())+'\n',encoding='utf-8')
