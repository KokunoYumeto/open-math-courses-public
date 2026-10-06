"""Original coordinate illustration of the two-arm support obstruction, CC0.

The exact open rectangles are A=(-3,-1)x(-2,2), B=(1,3)x(-2,2),
C=(-3,3)x(1,2). Their excluded boundaries are dashed. The characteristic
line y=0 meets two intervals and misses the middle interval [-1,1].
Reproduce using Python and matplotlib; no external illustration is imported.
"""
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
matplotlib.rcParams['svg.hashsalt']='planar-support-gap-v1'
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle

out=Path(__file__).resolve().parent
fig,ax=plt.subplots(figsize=(7.5,6.1),layout='constrained')
for x,y,width,height,color in [
    (-3,-2,2,4,'#83bfd6'), (1,-2,2,4,'#edc384'),
    (-3,1,6,1,'#aabf9c'),
]:
    ax.add_patch(Rectangle((x,y),width,height,facecolor=color,
                          edgecolor='none',alpha=0.88,zorder=1))
# Draw the true exterior boundary of the union, not internal rectangle seams.
ax.plot([-3,3,3,1,1,-1,-1,-3,-3],
        [2,2,-2,-2,1,1,-2,-2,2],
        linestyle=(0,(5,3)),color='#536172',linewidth=1.8,zorder=2)
ax.axhline(0,color='#4a5568',linestyle=':',linewidth=2,zorder=3)
ax.plot([-1,1],[0,0],color='#a62938',linewidth=5,zorder=4)
ax.scatter([-1,1],[0,0],facecolors='white',edgecolors='#a62938',s=45,zorder=5)
ax.text(-2,0.50,'Left arm',ha='center',fontsize=18)
ax.text(2,0.50,'Right arm',ha='center',fontsize=18)
ax.text(0,1.48,'Top: in both covers',ha='center',fontsize=17)
ax.text(0,-0.55,'Missing middle',ha='center',color='#a62938',fontsize=18)
ax.text(0,-2.62,r'$X_L=A\cup C\qquad X_R=B\cup C$',
        ha='center',fontsize=17)
ax.set_xlim(-3.6,3.6);ax.set_ylim(-2.85,2.55);ax.set_aspect('equal')
ax.set_xticks([-3,-1,0,1,3]);ax.set_yticks([-2,0,1,2])
ax.set_xlabel(r'$x_1$',fontsize=17)
ax.set_ylabel(r'$x_2$',fontsize=17,rotation=0,labelpad=14)
ax.tick_params(labelsize=14)
ax.set_title(r'$P(\xi)=\xi_1\xi_2$',fontsize=20,pad=14)
ax.grid(alpha=0.12)
for spine in ('top','right'):
    ax.spines[spine].set_visible(False)
fig.savefig(out/'planar-support-gap.png',dpi=180,
            metadata={'Author':'GPT-6.1 Sol (OpenAI), Ultra',
                      'Description':'Original exact rectangle drawing, CC0-1.0'})
fig.savefig(out/'planar-support-gap.svg',
            metadata={'Creator':'GPT-6.1 Sol (OpenAI), Ultra','Date':'2026-09',
                      'Description':'Original exact rectangle drawing, CC0-1.0'})
plt.close(fig)
