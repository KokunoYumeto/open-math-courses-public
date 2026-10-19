"""Exact profiles for reciprocal compression and pole cancellation."""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
out=Path(__file__).resolve().parent
plt.rcParams.update({'font.size':11,'axes.spines.top':False,'axes.spines.right':False,'svg.hashsalt':'AN01-U120-reciprocal-poles'})
fig,ax=plt.subplots(1,3,figsize=(14.4,4.7),layout='constrained')
x=np.linspace(-2,2,1601)
for t,c in [(1,'#157a89'),(3,'#bd681d'),(8,'#704ba0')]:
 ax[0].plot(x,t*t*x/(1+t*t*x*x),label=f't = {t}',color=c,lw=1.8)
for z in [np.linspace(-2,-.15,500),np.linspace(.15,2,500)]:
 ax[0].plot(z,1/z,'--',color='#5a626b',lw=1)
ax[0].axhline(0,color='#89939c',lw=.6)
ax[0].set(xlabel='x',ylabel='regular approximant',ylim=(-4.5,4.5),title='Reciprocal compression (Theorem 1)')
ax[0].legend(frameon=False,loc='upper right')
def bump(z):
 v=np.zeros_like(z,dtype=float);m=np.abs(z)<1
 v[m]=np.exp(-1/(1-z[m]**2))
 return v
z=np.linspace(0,1.12,1001)
ratio=np.empty_like(z);ratio[0]=-12/np.e
ratio[1:]=4*(bump(2*z[1:])-bump(z[1:]))/z[1:]**2
ax[1].plot(z,ratio,color='#157a89',lw=2)
ax[1].scatter([0],[-12/np.e],color='#157a89',zorder=5)
ax[1].annotate(r'$-12/e$',xy=(0,-12/np.e),xytext=(.2,-3.5),arrowprops={'arrowstyle':'->','color':'#5a626b'})
ax[1].axhline(0,color='#89939c',lw=.6)
ax[1].set(xlabel='x',ylabel=r'$[q(2x)-2q(x)]/x^3$',title='A canceled numerator (R19)')
y=np.linspace(-7,7,1401)
profile=-4*y*y/(1+y*y)**2
ax[2].plot(y,profile,color='#704ba0',lw=2)
ax[2].fill_between(y,profile,0,color='#704ba0',alpha=.12)
ax[2].axhline(0,color='#89939c',lw=.6)
ax[2].set(xlabel=r'inner coordinate $y=x/\varepsilon$',ylabel='limiting imaginary profile',title='The retained mass (R28)')
ax[2].text(.5,.14,r'$\int_{\mathbb{R}}-4y^2/(1+y^2)^2\,dy=-2\pi$',transform=ax[2].transAxes,ha='center',fontsize=10,bbox={'facecolor':'white','edgecolor':'none','alpha':.9,'pad':3})
fig.savefig(out/'reciprocal-scales-and-pole-mass.svg',metadata={'Creator':'GPT-6 Astra (OpenAI)','Date':None})
fig.savefig(out/'reciprocal-scales-and-pole-mass.png',dpi=180,metadata={'Author':'GPT-6 Astra (OpenAI)'})
plt.close(fig)
svg=out/'reciprocal-scales-and-pole-mass.svg'
svg.write_text('\n'.join(line.rstrip() for line in svg.read_text(encoding='utf-8').splitlines())+'\n',encoding='utf-8')
