"""Original chart-overlap schematic for the separation lesson. CC0-1.0.

Run with Python and matplotlib from the course root; the PNG and SVG are
written alongside this source. The picture compares exact ring maps, rather
than the topology of real points of schemes.
"""
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch

root = Path(__file__).resolve().parent
fig, axs = plt.subplots(2, 1, figsize=(5.8, 7.0), facecolor='white')
colors = ['#1f5a83', '#356b39']
for ax, color, title, left, right, image, conclusion in zip(
    axs, colors,
    ['Doubled line: identical coordinates', 'Projective line: reciprocal coordinates'],
    [r'$k[t_a]$', r'$k[t]$'], [r'$k[t_b]$', r'$k[u]$'],
    [r'Image: $k[t]$', r'Image: $k[t,t^{-1}]$'],
    [r'$t_a,t_b\mapsto t$: $t^{-1}$ is missing', r'$t\mapsto t,\ u\mapsto t^{-1}$: surjective']):
    ax.set(xlim=(0,10), ylim=(0,3.4)); ax.axis('off')
    ax.text(5,3.16,title,ha='center',va='center',fontsize=14,weight='bold',color=color)
    for x, txt in [(1.7,left),(8.3,right)]:
        ax.add_patch(FancyBboxPatch((x-1.05,1.85),2.1,.68,boxstyle='round,pad=.12',fc='#f2f6f8',ec=color,lw=1.5))
        ax.text(x,2.19,txt,ha='center',va='center',fontsize=17)
        ax.add_patch(FancyArrowPatch((x,1.74),(5,1.65),arrowstyle='-|>',mutation_scale=15,color=color,lw=1.5))
    ax.text(5,1.24,r'Overlap: $k[t,t^{-1}]$',ha='center',va='center',fontsize=17)
    ax.text(5,.69,image,ha='center',va='center',fontsize=16,color=color)
    ax.text(5,.21,conclusion,ha='center',va='center',fontsize=15)
fig.tight_layout(h_pad=1.3)
fig.savefig(root/'chart-overlaps.png',dpi=180,metadata={'Software':None})
fig.savefig(root/'chart-overlaps.svg',metadata={'Creator':None,'Date':None})
plt.close(fig)
