"""Exact polynomial coordinate model for Cubic collisions and uniform amplitudes.
Original illustration by GPT-6 Astra (OpenAI), October 2026; CC0.
Samples illustrate formulas C14, C31-C32 and C39; they are not proof.
"""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
plt.rcParams.update({'font.family':'DejaVu Sans','font.size':12,'svg.fonttype':'none'})
out=Path(__file__).resolve().parent
t=np.linspace(-1.6,1.6,1201)
fig,axes=plt.subplots(1,2,figsize=(16,6),layout='constrained')
colors=['#9b3b22','#363946','#176b83']
for a,col in zip([-3/5,0,3/5],colors):
    axes[0].plot(t,t**3/3+a*t,color=col,lw=2.5,label=rf'$a={a:g}$')
    if a<0:
        roots=np.array([-np.sqrt(-a),np.sqrt(-a)])
        axes[0].scatter(roots,roots**3/3+a*roots,s=65,c=col,zorder=5)
    if a==0:axes[0].scatter([0],[0],s=75,c=col,marker='D',zorder=6)
axes[0].axhline(0,color='#b9bec6',lw=.8)
axes[0].axvline(0,color='#b9bec6',lw=.8)
axes[0].set(xlabel=r'$t$',ylabel=r'$\phi_a(t)=t^3/3+at$',ylim=(-1.9,1.9),
            title='A. Two critical points, a merger, then none')
axes[0].legend(loc='upper left',frameon=False)
axes[0].text(.98,.04,r'$\phi_a^\prime(t)=t^2+a$',transform=axes[0].transAxes,ha='right',
              bbox={'facecolor':'white','edgecolor':'none','alpha':.9})
z=np.linspace(-.55,1.8,751)
tt,zz=np.meshgrid(t,z)
k=7/10;a=-3/5
F=tt**3/3+a*tt+(zz-k*tt**2)**2/2
cs=axes[1].contour(tt,zz,F,levels=[-.3,-.15,0,.15,.3,.6,1],colors='#9da8b5',linewidths=1)
axes[1].clabel(cs,inline=True,fontsize=9,fmt='%g')
axes[1].plot(t,k*t*t,color='#176b83',lw=2.8,label=r'$z_c(t)=(7/10)t^2$')
roots=np.array([-np.sqrt(3/5),np.sqrt(3/5)])
axes[1].scatter(roots,k*roots**2,c='#9b3b22',s=80,zorder=6)
axes[1].annotate(r'$(-\sqrt{3/5},\,21/50)$',xy=(roots[0],21/50),xytext=(-1.56,.85),
                 fontsize=10,arrowprops={'arrowstyle':'-','color':'#9b3b22'})
axes[1].annotate(r'$(\sqrt{3/5},\,21/50)$',xy=(roots[1],21/50),xytext=(.50,.02),
                 fontsize=10,arrowprops={'arrowstyle':'-','color':'#9b3b22'})
axes[1].set(xlabel=r'$t$',ylabel=r'$z$',ylim=(-.55,1.8),title='B. Exact transverse quadratic coordinates')
axes[1].legend(loc='upper center',frameon=True)
axes[1].text(.03,.04,r'$w=z-(7/10)t^2$'+'\n'+r'$f=t^3/3-(3/5)t+w^2/2$'+'\n'+r'$|\det\,\partial(t,z)/\partial(t,w)|=1$',
              transform=axes[1].transAxes,fontsize=11,bbox={'facecolor':'white','edgecolor':'#d4d9df','alpha':.95})
for ax in axes:ax.spines[['top','right']].set_visible(False)
fig.savefig(out/'cubic-collision-coordinates.png',dpi=150)
fig.savefig(out/'cubic-collision-coordinates.svg')
plt.close(fig)
p=out/'cubic-collision-coordinates.svg'
p.write_text('\n'.join(line.rstrip() for line in p.read_text(encoding='utf-8').splitlines())+'\n',encoding='utf-8')
