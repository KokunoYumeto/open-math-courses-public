from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

out = Path(__file__).resolve().parent
plt.rcParams.update({'font.size':11,'svg.fonttype':'none','svg.hashsalt':'AN01-U144-transverse-density'})
fig, ax = plt.subplots(1,3,figsize=(14,4.5),layout='constrained')
blue, orange, purple = '#1766a3', '#bd5a16', '#704191'
theta = np.pi/6
s = np.linspace(-1.5,1.5,601)
ax[0].plot(s,0*s,color=blue,lw=2,label=r'$Y:y=0$')
ax[0].plot(s*np.cos(theta),s*np.sin(theta),color=orange,lw=2,label=r'$Z:\theta=\pi/6$')
t = np.linspace(0,theta,101)
ax[0].plot(.55*np.cos(t),.55*np.sin(t),color='black',lw=1)
ax[0].text(.64,.12,r'$\theta$',fontsize=13)
ax[0].scatter([0],[0],color=purple,zorder=5)
ax[0].annotate(r'$(dS_Y)(dS_Z)=2\delta_0$',xy=(0,0),xytext=(-1.35,-.85),arrowprops={'arrowstyle':'->'},fontsize=12)
ax[0].set(xlim=(-1.5,1.5),ylim=(-1.15,1.15),xlabel='$x$',ylabel='$y$',title='A line intersection carries an angle factor')
ax[0].set_aspect('equal');ax[0].legend(loc='upper left',frameon=False)
s = np.linspace(-1.2,1.2,601)
ax[1].plot(s,-s*s,color=blue,lw=2)
for q in [-1,-.5,0,.5,1]:
    for sign in [-1,1]:
        v = sign*.18*np.array([2*q,1])
        ax[1].annotate('',xy=(q+v[0],-q*q+v[1]),xytext=(q,-q*q),arrowprops={'arrowstyle':'->','color':orange,'lw':1.3})
ax[1].text(-1.25,.47,r'$W=(s,-s^2,0)$')
ax[1].text(-1.25,.25,r'$\eta=\pm0.18(2s,1)$ in $T^*Y$')
ax[1].set(xlim=(-1.5,1.5),ylim=(-1.8,.7),xlabel='$x$',ylabel='$y$ in the plane $z=0$',title='The restricted normal stays in the plane')
ax[1].set_aspect('equal')
t=np.linspace(.12,np.pi/2,1001)
ax[2].plot(t,1/np.sin(t),color=purple,lw=2)
ax[2].scatter([np.pi/6,np.pi/2],[2,1],color=purple,zorder=5)
ax[2].annotate(r'$(\pi/6,2)$',xy=(np.pi/6,2),xytext=(.8,3),arrowprops={'arrowstyle':'->'})
ax[2].set(xlim=(0,np.pi/2),ylim=(.5,9),xlabel=r'$\theta$ (radians)',ylabel=r'$1/\sigma=1/\sin\theta$',title='Parallel alignment has no finite limit')
ax[2].set_xticks([0,np.pi/6,np.pi/3,np.pi/2],['0',r'$\pi/6$',r'$\pi/3$',r'$\pi/2$'])
for a in ax:
    a.spines[['top','right']].set_visible(False)
    a.grid(alpha=.15)
fig.savefig(out/'transverse-density-factors.png',dpi=170)
fig.savefig(out/'transverse-density-factors.svg',metadata={'Date':None})
plt.close(fig)
for suffix in ['py','svg']:
    p=out/('transverse-density-factors.'+suffix)
    p.write_text('\n'.join(line.rstrip() for line in p.read_text(encoding='utf-8').splitlines())+'\n',encoding='utf-8')
