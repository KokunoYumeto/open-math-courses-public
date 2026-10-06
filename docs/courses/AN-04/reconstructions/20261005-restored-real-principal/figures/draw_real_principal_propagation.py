"""Original exact base projection and forced model; no full cotangent plot claim."""
from pathlib import Path
import hashlib,json
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import Polygon
out=Path(__file__).resolve().parent
dest=out/'real-principal-type-propagation.svg'
plt.rcParams.update({'font.size':21,'svg.fonttype':'none'})
fig,(ax,bx)=plt.subplots(2,1,figsize=(7.8,11.8),gridspec_kw={'height_ratios':[1.7,1]},layout='constrained')
blue='#27697c';red='#a74737';grey='#67717a';ink='#233b49'
ax.add_patch(Polygon([(-1,-1),(1,-1),(1,1)],facecolor=blue,alpha=.13))
ax.add_patch(Polygon([(-1,-1),(-1,1),(1,1)],facecolor=red,alpha=.10))
ax.plot([-1,1],[-1,1],color=ink,lw=2.8)
ax.text(.64,-.64,r'$E_+:\ t\geq s$',color=blue,ha='center',fontsize=23)
ax.text(-.64,.64,r'$E_-:\ t\leq s$',color=red,ha='center',fontsize=23)
ax.annotate('',(.85,-.28),(.05,-.28),arrowprops={'arrowstyle':'->','lw':3,'color':blue})
ax.annotate('',(-.85,.28),(-.05,.28),arrowprops={'arrowstyle':'->','lw':3,'color':red})
ax.text(.12,.10,r'$t=s$',rotation=43,ha='left',va='bottom',color=ink,fontsize=21)
ax.set(xlim=(-1,1),ylim=(-1,1),xlabel=r'output time $t$',ylabel=r'input time $s$')
ax.set_xticks([-1,0,1]);ax.set_yticks([-1,0,1]);ax.set_aspect('equal')
ax.set_title('Two flow branches\n'+r'$z=w,\quad\eta\neq0$'+' (fixed)',fontsize=25,pad=18)
ax.spines[['top','right']].set_visible(False)
bx.plot([-1,0],[0,0],color=grey,lw=3,ls=(0,(4,3)))
bx.plot([0,1],[0,0],color=blue,lw=4)
bx.scatter([0],[0],s=230,color=red,zorder=3)
bx.text(-.52,.33,'regular',ha='center',color=grey,fontsize=24)
bx.text(.52,.33,'singular',ha='center',color=blue,fontsize=24)
bx.text(0,-.38,'forcing singularity\n'+r'$D_tu=-i\delta(t)\delta(z)$',ha='center',color=red,fontsize=23)
bx.set(xlim=(-1.12,1.12),ylim=(-.8,.65),xlabel=r'time $t$')
bx.set_xticks([-1,0,1]);bx.set_yticks([]);bx.spines[['left','top','right']].set_visible(False)
bx.set_title(r'$u=H(t)\delta(z)$'+'\n'+r'$z=0,\quad\tau=0,\quad\eta\neq0$',fontsize=25,pad=16)
fig.savefig(dest,metadata={'Creator':'GPT-6.1 Sol (OpenAI), Ultra','Date':None})
qa=out/'real-principal-type-propagation-qa.png';fig.savefig(qa,dpi=150);plt.close(fig)
print('Saved the exact signed-flow illustration.')
