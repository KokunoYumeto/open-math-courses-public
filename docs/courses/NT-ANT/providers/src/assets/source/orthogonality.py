"""Original CC0 figure: the exact four character values modulo 5.

Run with Python and matplotlib. Both PNG and editable SVG are produced.
"""
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np

out = Path(__file__).resolve().parent.parent
fig, axes = plt.subplots(1, 2, figsize=(9, 3.7), constrained_layout=True)
for ax in axes:
    t = np.linspace(0, 2*np.pi, 401)
    ax.plot(np.cos(t), np.sin(t), color='#9aa5b1', lw=1)
    ax.axhline(0, color='#cbd5e1', lw=.7)
    ax.axvline(0, color='#cbd5e1', lw=.7)
    ax.set_aspect('equal')
    ax.set_xlim(-1.4, 1.6)
    ax.set_ylim(-1.35, 1.35)
    ax.set_xticks([])
    ax.set_yticks([])
    for spine in ax.spines.values():
        spine.set_visible(False)
axes[0].scatter([1], [0], s=180, c='#164e63')
axes[0].annotate('1 + 1 + 1 + 1', (1,0), xytext=(-1.3,.65), fontsize=13)
axes[0].set_title('n = 1: all four values equal 1', fontsize=12)
axes[0].text(-1.25,-1.15,'Sum = 4; detector = 1', fontsize=12)
points=[(1,0,'1',(.12,.04)),(0,1,'i',(.06,.08)),(-1,0,'-1',(-.3,.04)),(0,-1,'-i',(.06,-.16))]
for x,y,label,(dx,dy) in points:
    axes[1].annotate('',(x,y),(0,0),arrowprops={'arrowstyle':'->','color':'#164e63','lw':1.7})
    axes[1].scatter([x],[y],s=55,c='#164e63')
    axes[1].text(x+dx,y+dy,label,fontsize=14)
axes[1].set_title('n = 2: the four fourth roots of unity', fontsize=12)
axes[1].text(-1.25,-1.32,'Sum = 0; detector = 0', fontsize=12)
fig.savefig(out/'orthogonality.png', dpi=160, metadata={'Software':None})
fig.savefig(out/'orthogonality.svg', metadata={'Date':None,'Creator':'GPT-6.1 Sol (OpenAI), Codex, Ultra; original CC0 figure'})
plt.close(fig)
