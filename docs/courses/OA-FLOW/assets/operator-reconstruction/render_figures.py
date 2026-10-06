from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch
import numpy as np

OUT=Path(__file__).resolve().parent/'assets'
OUT.mkdir(exist_ok=True)
plt.rcParams.update({'font.size':11,'svg.hashsalt':'independent-l157-l158-20261004'})
navy='#16324f'; blue='#236a99'; orange='#b85c16'

fig,ax=plt.subplots(figsize=(12,6.4))
ax.set(xlim=(0,12),ylim=(0,6.4));ax.axis('off')
ax.text(6,6.12,'Full logarithm domains and the prescribed product',ha='center',fontsize=17,color=navy,weight='bold')
def box(x,y,w,h,title,body):
    ax.add_patch(FancyBboxPatch((x,y),w,h,boxstyle='round,pad=0.12',facecolor='#edf4fa',edgecolor=blue,lw=1.4))
    ax.text(x+w/2,y+h-.27,title,ha='center',va='center',fontsize=12,weight='bold',color=navy)
    ax.text(x+w/2,y+h/2-.18,body,ha='center',va='center',fontsize=11,linespacing=1.7)
box(.35,3.65,4.8,1.55,'Complete domain comparison',r'$D(H)=D(K),\quad K=H+a$'+'\n'+r'$a=a^*\in M,\quad \|a\|<\infty$')
box(6.85,3.65,4.8,1.55,'Derivative at zero',r'$u_t=e^{itK}e^{-itH}$'+'\n'+r'$(u_t-1)/t\ \longrightarrow\ ia$')
ax.annotate('',xy=(6.6,4.65),xytext=(5.4,4.65),arrowprops={'arrowstyle':'->','color':blue,'lw':2})
ax.text(6,4.85,'LP6–LP10',ha='center',fontsize=9)
ax.annotate('',xy=(5.4,4.03),xytext=(6.6,4.03),arrowprops={'arrowstyle':'->','color':orange,'lw':2})
ax.text(6,3.73,'adjoint test',ha='center',fontsize=9)
box(.7,.65,10.6,2.25,'The product and its adjoint are identified before taking limits',
    r'$u_t-I=i\int_0^t B_r\,dr,\qquad u_t^*-I=-i\int_0^t B_r^*\,dr$'+'\n'+
    r'$B_r=e^{irK}a e^{-irH},\qquad \|(u_{t+h}-u_t)/h\|\leq\|a\|$'+'\n'+
    'Both bounded vector limits pass to every normal positive functional (SF-2).')
ax.annotate('',xy=(6,2.98),xytext=(6,3.43),arrowprops={'arrowstyle':'->','color':blue,'lw':2})
fig.tight_layout()
fig.savefig(OUT/'logarithmic-proof-map.png',dpi=160)
fig.savefig(OUT/'logarithmic-proof-map.svg',metadata={'Date':None})
plt.close(fig)

fig=plt.figure(figsize=(12,8.3))
grid=fig.add_gridspec(2,2,height_ratios=[.8,1.15],hspace=.48,wspace=.28)
ax=fig.add_subplot(grid[0,:])
ax.set(xlim=(-2.5,2.5),ylim=(-1.23,.3),xlabel=r'$t=\operatorname{Re}z$',ylabel=r'$\operatorname{Im}z$')
ax.axhspan(-1,0,color='#edf4fa')
ax.axhline(0,color=blue);ax.axhline(-1,color=orange)
ax.set_yticks([-1,0]);ax.text(-2.35,.08,r'$A(t)=H^{it}K^{-it}$',color=blue,fontsize=12)
ax.text(-2.35,-1.19,r'$B(t)=H^{it}TK^{-it}$',color=orange,fontsize=12)
ax.text(1.0,-.47,r'$z=t-is,\quad 0<s<1$',ha='center',fontsize=13,color=navy)
for end,start,col in [((-.2,0),(-.55,-.4),blue),((-.2,-1),(-.55,-.6),orange)]:
    ax.annotate('',xy=end,xytext=start,arrowprops={'arrowstyle':'->','color':col,'lw':2})
ax.set_title('Joint boundary limits on the normalized lower strip (PS7–PS11)',fontsize=15,color=navy,pad=14)
r=np.linspace(-3,3,2401)
for col,s in enumerate([.12,.70]):
    a=fig.add_subplot(grid[1,col])
    p0=np.sin(np.pi*s)/(2*(np.cosh(np.pi*r)-np.cos(np.pi*s)))
    p1=np.sin(np.pi*s)/(2*(np.cosh(np.pi*r)+np.cos(np.pi*s)))
    a.plot(r,p0,color=blue,label=fr'$P_s^0$: full mass ${1-s:.2f}$')
    a.plot(r,p1,color=orange,label=fr'$P_s^1$: full mass ${s:.2f}$')
    a.set(xlabel=r'$r$',ylabel='Kernel value',title=fr'Exact formulas sampled at $s={s:.2f}$',xlim=(-3,3),ylim=(0,None))
    a.grid(alpha=.2);a.legend(loc='upper right',fontsize=10)
fig.text(.5,.02,'The finite plotting window is illustrative; the labelled integrals are over the entire real line.',ha='center',fontsize=10)
fig.savefig(OUT/'strip-kernels.png',dpi=160,bbox_inches='tight')
fig.savefig(OUT/'strip-kernels.svg',bbox_inches='tight',metadata={'Date':None})
plt.close(fig)
print('Rendered four original figure files in',OUT)
