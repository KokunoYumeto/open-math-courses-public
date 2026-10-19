"""The exact radial coordinate map and the gravitational shear multiplier."""
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch

plt.rcParams.update({'font.family':'DejaVu Sans','svg.fonttype':'none','font.size':12})
fig,ax=plt.subplots(figsize=(12,6.5))
fig.patch.set_facecolor('#f6fafc');ax.set_facecolor('#f6fafc')
ax.set_xlim(0,12);ax.set_ylim(0,6.5);ax.axis('off')
ink='#15354b';accent='#147991'
ax.text(.45,6.1,'The radial direction carries the wave response',fontsize=20,weight='bold',color=ink)
ax.text(.45,5.62,r'$x=\rho_c\log(\rho/\rho_c),\quad \rho_c=2\nu/c,\quad W_k(x)=k^2e^{2x/\rho_c}$',fontsize=15,color=ink)
ax.annotate('',xy=(.65,4.35),xytext=(10,4.35),arrowprops={'arrowstyle':'->','lw':2,'color':accent})
for x,label in [(3.3,r'$-2\rho_c$'),(6.55,r'$-\rho_c$'),(9.8,r'$0$')]:
    ax.plot([x,x],[4.25,4.45],color=ink,lw=1.5);ax.text(x,3.94,label,ha='center',fontsize=14,color=ink)
ax.plot([9.8,9.8],[4.15,5.05],color=accent,lw=3)
ax.text(9.8,5.18,'Cutoff '+r'$\rho=\rho_c$',ha='center',fontsize=12,color=ink)
ax.text(.65,4.65,'Horizon: '+r'$x\to-\infty$',fontsize=12,color=ink)
ax.annotate('',xy=(3.6,4.88),xytext=(6.5,4.88),arrowprops={'arrowstyle':'->','lw':2,'color':'#b05a23'})
ax.text(5.05,5.12,'Ingoing: '+r'$t+x/c$'+' constant',ha='center',fontsize=11,color='#945025')
ax.text(9.8,3.45,'Zero boundary drive:\n'+r'$\partial_x\varphi(t,0)=0$',ha='center',fontsize=12,color=ink)
ax.text(.65,3.45,r'$c^{-2}\varphi_{tt}-\varphi_{xx}+W_k\varphi=0$',fontsize=14,color=ink)

def box(x,y,w,head,formula):
    ax.add_patch(FancyBboxPatch((x,y),w,.95,boxstyle='round,pad=.12',facecolor='white',edgecolor='#8ab8c8',lw=1.4))
    ax.text(x+w/2,y+.64,head,ha='center',fontsize=12,weight='bold',color=ink)
    ax.text(x+w/2,y+.23,formula,ha='center',fontsize=13,color=ink)
box(.65,1.7,3.65,'Boundary metric source',r'$A_{0c}=a_{\rm src}/c,\quad A_{zc}=0$')
box(7.4,1.7,3.65,'Momentum response',r'$V_{\rm BY}=-c\,\delta T^{\rm BY}_{0y}/p_0$')
ax.annotate('',xy=(7.2,2.18),xytext=(4.5,2.18),arrowprops={'arrowstyle':'->','lw':2,'color':accent})
ax.text(5.85,2.52,'Ingoing vacuum shear',ha='center',fontsize=11,color=ink)
ax.text(6,.93,r'$V_{\rm BY}/a_{\rm src}=-1+\frac{q^2}{2}\frac{I_{-iw}(q)}{qI_{-iw}^{\prime}(q)}$',ha='center',fontsize=19,color=ink)
ax.text(.65,.25,r'$q=k\rho_c,\quad w=\omega\rho_c/c$'+'  ·  Exact linear response, lesson V6b (S19)–(S21), (S37)–(S41)',fontsize=11,color='#466171')
fig.savefig(Path(__file__).with_suffix('.svg'),bbox_inches='tight',pad_inches=.15)
fig.savefig(Path(__file__).with_suffix('.png'),dpi=150,bbox_inches='tight',pad_inches=.15)
plt.close(fig)
