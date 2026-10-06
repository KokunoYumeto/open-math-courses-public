"""Reproduce the exact two-chart calculation in relative-maslov-line M8."""
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch
out=Path(__file__).resolve().parent
plt.rcParams.update({'font.family':'DejaVu Sans','font.size':11,'svg.fonttype':'path'})
fig,(ax,steps)=plt.subplots(2,1,figsize=(4.5,7.5),height_ratios=[1,1.4],layout='constrained')
fig.suptitle('A rotating line\nFourth-root transitions',fontsize=14)
for x,y,color in [([0,.25],[-1,-1],'#ba5a28'),([.25,.75],[0,0],'#12677a'),([.75,1],[-1,-1],'#ba5a28')]:
 ax.plot(x,y,color=color,lw=3)
for x in [.25,.75]:
 ax.scatter([x,x],[-1,0],facecolors='white',edgecolors='#233746',s=55,zorder=4)
ax.scatter([0,1],[-1,-1],color='#ba5a28',s=25,zorder=4)
ax.axvline(.5,color='#999',ls=':',lw=1)
ax.text(.5,-.47,'Intersection dimension changes\ntransition stays 1',ha='center',va='center',fontsize=10)
ax.set_xticks([0,.25,.5,.75,1],[r'$0$',r'$\pi/4$',r'$\pi/2$',r'$3\pi/4$',r'$\pi$'])
ax.set_yticks([-1,0],[r'$-1$',r'$0$'])
ax.set_ylabel(r'Integer $\sigma$')
ax.text(.5,.15,r'$g_{ab}=1$',ha='center',fontsize=12)
ax.text(.12,-1.23,r'$g_{ab}=-i$',ha='center',fontsize=11)
ax.text(.88,-1.23,r'$g_{ab}=-i$',ha='center',fontsize=11)
ax.set_ylim(-1.3,.4);ax.set_xlim(-.02,1.02)
ax.set_xlabel(r'Line angle $t$ modulo $\pi$')
ax.set_title('Exact transition on the overlap',fontsize=12)
ax.spines[['top','right']].set_visible(False)
steps.set_xlim(0,1);steps.set_ylim(0,1);steps.axis('off')
boxes=[
 (.81,r'Chart $b$:  $z_b=1$',r'$0\leq t\leq\pi/2$'),
 (.46,r'Chart $a$:  $z_a=1$',r'$\pi/2\leq t\leq7\pi/8$'),
 (.11,r'Chart $b$:  $z_b=i$',r'$7\pi/8\leq t\leq\pi$')]
for y,title,interval in boxes:
 steps.add_patch(FancyBboxPatch((.10,y-.09),.80,.18,boxstyle='round,pad=.015',facecolor='#eef5f7',edgecolor='#12677a'))
 steps.text(.5,y+.027,title,ha='center',va='center',fontsize=12)
 steps.text(.5,y-.038,interval,ha='center',va='center',fontsize=10)
for start,end,label in [(.70,.57,r'$g_{ab}=1:\quad z_a=z_b$'),(.35,.22,r'$g_{ab}=-i:\quad z_b=i\,z_a$')]:
 steps.annotate('',xy=(.5,end),xytext=(.5,start),arrowprops={'arrowstyle':'->','color':'#233746'})
 steps.text(.5,(start+end)/2,label,ha='center',va='center',fontsize=11,
            bbox={'facecolor':'white','edgecolor':'none','pad':1})
steps.set_title(r'Constant chart coordinates give holonomy $i$',fontsize=12)
fig.savefig(out/'maslov-transition.svg')
fig.savefig(out/'maslov-transition.png',dpi=160)
print('Wrote exact transition and transport diagram.')
