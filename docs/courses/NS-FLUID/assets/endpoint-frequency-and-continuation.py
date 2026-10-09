"""Exact support ratios and the physical time windows in 5.3 and 6.2–8.2."""
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle
fig,axs=plt.subplots(2,1,figsize=(13,8.4),layout='constrained',gridspec_kw={'height_ratios':[1,1.2]})
ax=axs[0];ax.set_xlim(-.6,4.6);ax.set_ylim(-.7,2)
ax.axhline(0,color='#6c7685',lw=1)
for j,lab in enumerate(['1','2','4','8','16']):
    valid=j<=2
    ax.scatter(j,0,s=170,color='#197654' if valid else '#b54a38',zorder=4)
    ax.text(j,-.27,'$'+lab+'$',ha='center',fontsize=17)
    ax.text(j,.27,'allowed' if valid else 'zero integral',ha='center',fontsize=13)
ax.text(-.5,1.57,'Three Fourier vectors must add to zero',fontsize=18,weight='bold')
ax.text(-.5,1.05,r'$|\xi_H|>H/4,\quad |\xi_M|<M,\quad |\xi_L|<L\leq M$',fontsize=19)
ax.text(-.5,.68,r'$H/4<2M\quad\Longrightarrow\quad H/M<8$',fontsize=19)
ax.text(2,-.65,r'Highest / middle frequency, $H/M$ (logarithmic spacing)',ha='center',fontsize=13)
ax.set_axis_off()
ax=axs[1];ax.set_xlim(-.07,1.36);ax.set_ylim(-.65,1.25)
ax.text(0,1.08,'Actual nested time windows; the equation and time stay unchanged',fontsize=17,weight='bold')
for y,l,r,color,label in [(.65,0,1,'#d9e5f0','Original smooth interval'),(.32,.5,1,'#89bacd','Frequency absorption and enstrophy inequality'),(-.01,.75,1,'#53a481','Uniform original velocity $H^1$ bound')]:
    ax.add_patch(Rectangle((l,y-.1),r-l,.2,color=color))
    ax.text(1.035,y,label,va='center',fontsize=11,wrap=True)
for x,label in [(0,'$a$'),(.5,'$a+T/2$'),(.75,'$a+3T/4$'),(1,'$a+T$')]:
    ax.plot([x,x],[-.23,.8],ls=':',color='#7c8189',lw=.8)
    ax.text(x,-.3,label,ha='center',fontsize=14)
ax.text(0,-.54,r'At $t_n\uparrow T_*$, the same $H^1$ bound supplies a common restart length (8.1–8.2).',fontsize=13)
ax.set_axis_off()
fig.suptitle('Frequency support and continuation',fontsize=22,weight='bold')
out=Path(__file__).with_suffix('')
fig.savefig(out.with_suffix('.png'),dpi=160)
fig.savefig(out.with_suffix('.svg'))
plt.close(fig)
