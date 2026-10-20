"""Exact moving-norm balls and the closed-set distance exclusion."""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import Polygon,Circle

fig,axes=plt.subplots(1,2,figsize=(13,5.4),constrained_layout=True)
ax=axes[0]
ax.axhline(0,color='#193d63',lw=2)
ax.fill_between([-4.5,7.5],-1,0,color='#e6e9ed')
for (x,y),color in zip([(-3,1),(0,2),(4,3)],['#126f91','#18847d','#ba633c']):
    vertices=np.array([[x-y,y],[x,y+y/2],[x+y,y],[x,y-y/2]])
    ax.add_patch(Polygon(vertices,closed=True,facecolor=color,alpha=.16))
    ax.plot(*np.vstack([vertices,vertices[0]]).T,color=color,lw=2)
    ax.scatter([x],[y],color=color,s=25)
    ax.text(x,y+.12,f'({x}, {y})',ha='center',fontsize=10,
            bbox=dict(facecolor='white',edgecolor='none',alpha=.9))
ax.annotate(r'$y/2$',xy=(4,1.5),xytext=(4,.65),ha='center',
            arrowprops=dict(arrowstyle='->',color='#555'))
ax.text(-4.3,-.55,r'$F=\{y=0\}$',fontsize=11)
ax.set_xlim(-4.5,7.5);ax.set_ylim(-.9,5)
ax.set_xlabel(r'$x$');ax.set_ylabel(r'$y$')
ax.set_title(r'$p_{(x,y)}(v)=(|v_1|+2|v_2|)/y$',pad=14,fontsize=13)
ax=axes[1]
ax.axhline(0,color='#193d63',lw=2,label=r'$F_0$')
ax.axvline(0,color='#7c4687',lw=2,label=r'$F_1$')
for center,color,label in [((.4,1.6),'#18847d',r'$d=1.6,\ r=0.8$'),
                           ((1.6,.4),'#ba633c',r'$d=1.6,\ r=0.8$')]:
    ax.add_patch(Circle(center,.8,facecolor=color,alpha=.15))
    ax.add_patch(Circle(center,.8,fill=False,edgecolor=color,lw=2))
    ax.scatter(*center,color=color,s=25)
ax.text(.4,2.58,r'$(0.4,1.6)$',ha='center',fontsize=10)
ax.text(1.6,-.65,r'$(1.6,0.4)$',ha='center',fontsize=10)
ax.annotate('',xy=(1.2,1.6),xytext=(.4,1.6),
            arrowprops=dict(arrowstyle='<->',color='#12665f'))
ax.text(.8,1.76,r'$0.8$',ha='center',fontsize=10,
        bbox=dict(facecolor='white',edgecolor='none',alpha=.9))
ax.text(2.5,.10,r'$F_0$',color='#193d63',fontsize=12)
ax.text(.08,2.38,r'$F_1$',color='#7c4687',fontsize=12)
ax.scatter([0],[0],color='#272727',zorder=5,s=28)
ax.set_xlim(-.65,2.85);ax.set_ylim(-.85,2.85)
ax.set_xlabel(r'$x$');ax.set_ylabel(r'$y$')
ax.set_title(r'$d(x,y)=\max\{|x|,|y|\}$',pad=14,fontsize=13)
for ax in axes:
    ax.set_aspect('equal')
    ax.grid(alpha=.16)
    ax.spines[['top','right']].set_visible(False)
out=Path(__file__).resolve().parent
for ext in ['png','svg']:
    fig.savefig(out/f'moving-norm-separation.{ext}',dpi=160,
                metadata={'Creator':'GPT-6 Astra (OpenAI)'} if ext=='svg' else None)
    if ext=='svg':
        p=out/'moving-norm-separation.svg'
        p.write_text('\n'.join(s.rstrip() for s in p.read_text(encoding='utf-8').splitlines())+'\n',encoding='utf-8',newline='\n')
