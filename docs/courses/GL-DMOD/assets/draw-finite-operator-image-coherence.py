"""Original CC0 schematic; symbolic intervals are explicitly not to scale."""
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch

base = Path(__file__).resolve().parent
fig, ax = plt.subplots(figsize=(15, 8.6), dpi=170)
fig.patch.set_facecolor('#fbfaf6')
ax.set_facecolor('#fbfaf6')
ax.set_xlim(0, 15)
ax.set_ylim(0, 8.6)
ax.axis('off')

ink = '#213142'
blue = '#275f9e'
green = '#28734c'
orange = '#a14f21'

def label(x, y, t, size=16, color=ink, ha='left'):
    ax.text(x, y, t, fontsize=size, color=color, ha=ha, va='center')

def box(x, y, w, h, text, color):
    ax.add_patch(FancyBboxPatch((x, y), w, h, boxstyle='round,pad=0.08',
        facecolor='white', edgecolor=color, linewidth=1.8))
    label(x + w/2, y + h/2, text, 18, color, 'center')

def interval(y, a, b, color):
    ax.plot([a, b], [y, y], color=color, lw=9, solid_capstyle='round')
    ax.scatter([a, b], [y, y], s=65, color=color, zorder=3)

label(.5, 8.12, 'A finite induced resolution computes every possible output degree', 23)
label(.5, 7.58, r'$d=\dim_{\mathbf{C}} Z,\quad s=3d+1,\quad A_j=\mathcal{O}(-k_j)^{r_j}\otimes\mathcal{D}_Z$', 19)

box(.6, 6.25, 4.1, .75, r'$p_+C$', blue)
box(5.45, 6.25, 4.1, .75, r'$p_+M$', green)
box(10.3, 6.25, 4.1, .75, r'$p_+K[s+1]$', orange)
for x in (4.82, 9.67):
    ax.annotate('', (x+.47, 6.625), (x, 6.625),
        arrowprops=dict(arrowstyle='->', lw=2, color=ink))
label(7.5, 5.68, r'$\operatorname{Cone}(C\to M)=K[s+1]$', 20, ha='center')

label(.65, 4.87, 'Independent bound for the actual output', 17, green)
interval(4.32, 8.25, 13.95, green)
label(8.25, 3.83, r'$-d$', 17, green, 'center')
label(13.95, 3.83, r'$2d$', 17, green, 'center')
label(.65, 3.07, 'Bound for the unresolved cone', 17, orange)
interval(2.58, 1.3, 5.8, orange)
label(1.3, 2.1, r'$-4d-2$', 17, orange, 'center')
label(5.8, 2.1, r'$-d-2$', 17, orange, 'center')
ax.plot([7.04, 7.04], [2.22, 4.56], ls='--', color='#8792a0', lw=1.5)
label(7.04, 1.58, r'$-d-1$', 17, ink, 'center')
label(10.7, 2.63, 'Two absent cone degrees give', 17, ha='center')
label(10.7, 2.12, r'$H^q(p_+C)\ \cong\ H^q(p_+M)\quad(q\geq -d)$', 17, blue, 'center')

label(.65, .94, 'Finite cones of the coherent induced images prove coherence of the actual output.', 17)
label(.65, .44, 'Symbolic degree intervals are schematic, not to scale. Proof: (5.9l)–(5.9q).', 13, '#687282')

fig.savefig(base / 'finite-operator-image-coherence.png', bbox_inches='tight', facecolor=fig.get_facecolor())
fig.savefig(base / 'finite-operator-image-coherence.svg', bbox_inches='tight', facecolor=fig.get_facecolor())
plt.close(fig)
