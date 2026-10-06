"""Kernel/image covolumes for A(x,y)=2x+y on Z^2.

Original figure: GPT-6.1 Sol (OpenAI), Codex, Ultra; October 2026. CC0.
All source vertices and projections are rational; only plotting uses floats.
"""
from fractions import Fraction as F
from math import sqrt
from pathlib import Path
import json
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import Polygon

ROOT = Path(__file__).resolve().parents[1]
u, t, p = (-1, 2), (0, 1), (F(2, 5), F(1, 5))
assert 2*u[0]+u[1] == 0 and 2*t[0]+t[1] == 1
assert u[0]*p[0]+u[1]*p[1] == 0
assert abs(u[0]*t[1]-u[1]*t[0]) == 1
assert abs(u[0]*p[1]-u[1]*p[0]) == 1
cell = [(0, 0), u, (u[0]+t[0], u[1]+t[1]), t]
root = sqrt(5)
def adapted(v):
    x, y = map(float, v)
    return ((-x+2*y)/root, (2*x+y)/root)

plt.rcParams.update({'font.family': 'DejaVu Sans', 'font.size': 12})
fig, axes = plt.subplots(1, 2, figsize=(12, 5.3), constrained_layout=True)
points = [(x, y) for x in range(-2, 3) for y in range(-1, 5)]
axes[0].scatter([x for x,y in points], [y for x,y in points],
                color='#8995a7', s=20, zorder=2)
axes[0].add_patch(Polygon(cell, facecolor='#b8d5eb', edgecolor='#286c9b',
                          linewidth=1.8, alpha=.75))
axes[0].plot([-2, 1], [4, -2], color='#73509b', linewidth=1.4)
for v, color in [(u, '#73509b'), (t, '#286c9b'), (p, '#b46220')]:
    axes[0].annotate('', xy=v, xytext=(0,0),
                     arrowprops={'arrowstyle':'->', 'lw':2.4, 'color':color})
axes[0].plot([t[0],p[0]],[t[1],p[1]],color='#b46220',linestyle='--',linewidth=1.2)
axes[0].text(-1.08,2.12,r'$u=(-1,2)$',ha='right',color='#5b3b80')
axes[0].text(.10,1.07,r'$t=(0,1)$',color='#225b80')
axes[0].text(.50,.13,r'$p=(2/5,1/5)$',fontsize=11,color='#94511e')
axes[0].text(-.5,1.9,'cell area = 1',ha='center',fontsize=11,
             bbox={'facecolor':'white','alpha':.9,'edgecolor':'none','pad':2})
axes[0].text(-1.7,3.65,r'$\ker A$',color='#5b3b80')
axes[0].set(xlim=(-2.1,1.65),ylim=(-.65,4.15),aspect='equal',
            xlabel='$x$',ylabel='$y$',title=r'Source lattice: $A(x,y)=2x+y$')

adapted_points = [adapted(v) for v in points]
axes[1].scatter([x for x,y in adapted_points], [y for x,y in adapted_points],
                color='#8995a7',s=20,zorder=2)
axes[1].add_patch(Polygon([adapted(v) for v in cell], facecolor='#b8d5eb',
                          edgecolor='#286c9b',linewidth=1.8,alpha=.75))
axes[1].add_patch(Polygon([(0,0),(root,0),(root,1/root),(0,1/root)],
                          facecolor='#cdbbdd',edgecolor='#73509b',alpha=.6,
                          linewidth=1.5))
axes[1].axhline(0,color='#73509b',linewidth=1.4)
axes[1].annotate('',xy=(root,0),xytext=(0,0),
                 arrowprops={'arrowstyle':'<->','color':'#73509b','lw':2})
axes[1].text(root/2,-.23,r'kernel step $=\sqrt{5}$',ha='center',color='#5b3b80')
axes[1].annotate('',xy=(0,1/root),xytext=(0,0),
                 arrowprops={'arrowstyle':'<->','color':'#b46220','lw':2})
axes[1].text(-.13,.22,r'$1/\sqrt{5}$',ha='right',color='#94511e')
axes[1].text(1.4,.77,r'$A=\sqrt{5}\,z_{\rm normal}$',ha='center',color='#225b80')
axes[1].text(1.4,1.12,r'image lattice $=\mathbb{Z}$, step $=1$',ha='center')
axes[1].text(1.4,1.53,r'$\sqrt{5}\,(1/\sqrt{5})=1$',ha='center',fontsize=14,
             bbox={'facecolor':'white','alpha':.95,'edgecolor':'#d6dce5','pad':6})
axes[1].set(xlim=(-.7,3.6),ylim=(-.65,2.10),aspect='equal',
            xlabel='orthonormal kernel coordinate',ylabel='normal coordinate',
            title='Project the lift; preserve the cell area')
for ax in axes:
    ax.spines[['top','right']].set_visible(False)
    ax.grid(color='#d9dfe8',linewidth=.5)
    ax.set_axisbelow(True)
fig.suptitle(r'$\operatorname{covol}(\ker A\cap\mathbb{Z}^2)=\frac{1\cdot\sqrt{5}}{1}=\sqrt{5}$',
             fontsize=16)
dest = ROOT/'figures/kernel-image-volume.png'
fig.savefig(dest,dpi=160)
plt.close(fig)
RESULT = {'map': ['2','1'], 'kernel_basis':list(u),'image_lift':list(t),
          'orthogonal_projection':[str(x) for x in p],
          'source_cell_area':1,'kernel_covolume':'sqrt(5)',
          'image_covolume':1,'jacobian':'sqrt(5)',
          'projected_step':'1/sqrt(5)','path':str(dest)}
if __name__ == '__main__':
    print(json.dumps(RESULT,indent=2))
