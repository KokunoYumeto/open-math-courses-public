"""Exact commuting square for AQ01/AQ03; no source artwork or network input."""
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

fig, ax = plt.subplots(figsize=(9, 6.5), dpi=100)
fig.patch.set_facecolor('#fbfcff')
ax.set(xlim=(0, 9), ylim=(0, 6.5))
ax.axis('off')
ax.text(4.5, 6.05, 'Conjugating an inner automorphism', ha='center', fontsize=20, weight='bold', color='#162845')

def matrix(cx, cy, entries, prefix=''):
    dx, dy = .36, .27
    for i in range(2):
        for j in range(2):
            ax.text(cx+(2*j-1)*dx, cy+(1-2*i)*dy, str(entries[i][j]), ha='center', va='center', fontsize=23, color='#162845')
    for sign in (-1, 1):
        x=cx+sign*.8
        ax.plot([x-sign*.12,x,x,x-sign*.12], [cy+.58,cy+.58,cy-.58,cy-.58], lw=1.5, color='#162845')
    if prefix: ax.text(cx-1.05,cy,prefix,ha='right',va='center',fontsize=20,color='#162845')

matrix(2,4.55,[[0,1],[0,0]])
matrix(7,4.55,[[0,-1],[0,0]])
matrix(2,2.0,[[1,-1],[1,-1]],r'$\frac{1}{2}$')
matrix(7,2.0,[[-1,1],[-1,1]],r'$\frac{1}{2}$')
arrow=dict(arrowstyle='->',lw=2,color='#256ba2',mutation_scale=20)
ax.annotate('',xy=(5.8,4.55),xytext=(3.2,4.55),arrowprops=arrow)
ax.text(4.5,4.83,r'$\mathrm{Ad}_v$',ha='center',fontsize=18,color='#256ba2')
ax.annotate('',xy=(5.45,2),xytext=(3.2,2),arrowprops=arrow)
ax.text(4.35,2.3,r'$\mathrm{Ad}_{\alpha(v)}$',ha='center',fontsize=18,color='#256ba2')
for x in (2,7):
    ax.annotate('',xy=(x,2.8),xytext=(x,3.75),arrowprops=arrow)
    ax.text(x+.2,3.23,r'$\alpha=\mathrm{Ad}_w$',va='center',fontsize=16,color='#256ba2')
ax.text(4.5,.72,r'$\alpha\circ\mathrm{Ad}_v=\mathrm{Ad}_{\alpha(v)}\circ\alpha$',ha='center',fontsize=21,color='#162845')
ax.text(4.5,.26,'Exact entries from AQ.9–10  •  Normality proved in AQ01',ha='center',fontsize=12,color='#475569')
fig.subplots_adjust(left=0,right=1,bottom=0,top=1)
fig.savefig(Path(__file__).with_name('inner-automorphism-conjugation.png'),dpi=100,facecolor=fig.get_facecolor())
plt.close(fig)
