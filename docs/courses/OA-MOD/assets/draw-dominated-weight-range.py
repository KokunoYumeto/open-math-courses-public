"""Reproduce the exact two-coordinate example in OA-MOD-DW-06."""
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle
plt.rcParams.update({'font.family':'DejaVu Sans','font.size':14})
fig,(a,b)=plt.subplots(1,2,figsize=(12,5.8))
a.add_patch(Rectangle((0,0),3,3,facecolor='#f3d4d0'))
a.plot([0,3],[0,0],color='#136d86',linewidth=6)
a.text(1.5,1.6,r'$\varphi(a,b)=+\infty$'+'\nwhen b > 0',ha='center',va='center',fontsize=16)
a.text(1.45,.24,r'finite: $\varphi(a,0)=a$',ha='center',color='#08566a',fontsize=14)
a.set(xlim=(-.2,3.1),ylim=(-.2,3.1),xlabel='a',ylabel='b',xticks=[0,1,2,3],yticks=[0,1,2,3])
a.set_title('Positive cone of the algebra',fontweight='bold',pad=15)
b.axhline(0,color='#136d86',linewidth=4);b.axvline(0,color='#bbbbbb')
b.plot([2,2],[0,1.8],'--',color='#b44132',lw=2)
b.annotate('',xy=(2,0),xytext=(2,1.8),arrowprops={'arrowstyle':'->','color':'#b44132','lw':2})
b.scatter([2,2],[0,1.8],s=60,color=['#136d86','#b44132'],zorder=3)
b.text(2.12,1.8,'(u,v)',va='center');b.text(2.1,-.25,'(u,0)',va='top')
b.text(.1,2.25,r'$H_\psi=\mathbb{C}^2$'+'\nreal slice shown',fontsize=16)
b.text(-.6,-.65,r'$K=\mathbb{C}(1,0)$',color='#08566a',fontsize=16)
b.text(.55,1.1,r'$CC^*$',color='#b44132',fontsize=17)
b.set(xlim=(-1,3),ylim=(-1,2.8),xlabel='Re u',ylabel='Re v',xticks=[-1,0,1,2,3],yticks=[-1,0,1,2])
b.set_title('The target has an unreached direction',fontweight='bold',pad=15)
for ax in [a,b]:ax.spines[['top','right']].set_visible(False);ax.grid(alpha=.13)
fig.suptitle(r'$Cz=(z,0)$ is isometric, but its range is proper',fontsize=19,fontweight='bold',y=.98)
fig.text(.5,.035,r'$H_\varphi=\mathbb{C},\quad T=C^*C=I,\quad U=C,\quad K=\operatorname{ran}C\ne H_\psi$',ha='center',fontsize=17)
fig.subplots_adjust(top=.80,bottom=.21,left=.07,right=.95,wspace=.37)
fig.savefig(Path(__file__).with_name('dominated-weight-range.png'),dpi=150)
plt.close(fig)

