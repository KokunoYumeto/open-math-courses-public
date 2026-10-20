from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
matplotlib.rcParams.update({'font.size':10,'svg.hashsalt':'AN01-weighted-conormal-v1','svg.fonttype':'none'})
out=Path(__file__).resolve().parent
s=np.linspace(-1.3,1.3,1301)
b=np.zeros_like(s);inside=np.abs(s)<1
b[inside]=s[inside]*np.exp(-1/(1-s[inside]**2))
fig,ax=plt.subplots(1,3,figsize=(14,4.5),layout='constrained')
ax[0].plot(s,b,color='#225ea8',lw=2)
ax[0].axhline(0,color='0.65',lw=.8)
ax[0].plot([-1,0,1],[0,0,0],'o',mfc='white',mec='#b45309',ms=6)
ax[0].plot([-1,1],[-.18,-.18],color='#b45309',lw=4)
ax[0].text(0,-.205,r'$\operatorname{supp}b=[-1,1]$',ha='center',color='#b45309')
ax[0].set(xlim=(-1.3,1.3),ylim=(-.24,.24),xlabel=r'$s$',ylabel=r'$b(s)$',title='Smooth weight; three zeros in its support')
q=np.linspace(-1.25,1.25,501);active=np.abs(q)<=1
ax[1].plot(q,q*q,':',color='0.6',lw=1.5)
ax[1].plot(q[active],q[active]**2,color='#225ea8',lw=2)
for t in [-1,-.5,0,.5,1]:
 for sign in [-1,1]:
  dx,dy=sign*.18*np.array([-2*t,1.])
  ax[1].annotate('',xy=(t+dx,t*t+dy),xytext=(t,t*t),arrowprops=dict(arrowstyle='->',color='#b45309',lw=1.5))
 ax[1].plot(t,t*t,'o',mfc='white' if t in [-1,0,1] else '#225ea8',mec='#225ea8',ms=5)
ax[1].set(xlim=(-1.5,1.5),ylim=(-.32,1.7),xlabel=r'$x$',ylabel=r'$y$',title=r'Parabola: covectors $\pm0.18(-2s,1)$')
ax[1].set_aspect('equal',adjustable='box')
for end in [(1.3,0),(-1.3,0),(0,1.3),(0,-1.3)]:
 ax[2].annotate('',xy=end,xytext=(0,0),arrowprops=dict(arrowstyle='->',color='#225ea8',lw=2))
ax[2].plot(0,0,'o',mfc='white',mec='0.35',ms=6,zorder=5)
ax[2].text(.15,.36,r'$\Sigma(v)$: four full rays',color='#225ea8')
ax[2].text(0,-1.53,'Exact axes: rapid decay\nEvery surrounding cone: no rapid decay',ha='center',fontsize=9)
ax[2].set(xlim=(-1.6,1.6),ylim=(-1.85,1.6),xlabel=r'$\xi$',ylabel=r'$\eta$',title='Compact crossed density: frequency projection')
ax[2].set_aspect('equal',adjustable='box')
for a in ax:a.spines[['top','right']].set_visible(False)
fig.savefig(out/'weighted-conormal-directions.png',dpi=170)
fig.savefig(out/'weighted-conormal-directions.svg',metadata={'Date':None})
plt.close(fig)
p=out/'weighted-conormal-directions.svg'
p.write_text('\n'.join(line.rstrip() for line in p.read_text(encoding='utf-8').splitlines())+'\n',encoding='utf-8')
