"""Original CC0 cotangent-correspondence schematic."""
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch

base = Path(__file__).resolve().parent
fig, ax = plt.subplots(figsize=(15, 8.4), dpi=170)
fig.patch.set_facecolor('#fbfaf6')
ax.set_xlim(0, 15)
ax.set_ylim(0, 8.4)
ax.axis('off')
ink, blue, green, orange = '#213142', '#275f9e', '#28734c', '#a14f21'

def label(x, y, t, size=17, color=ink, ha='left'):
    ax.text(x, y, t, fontsize=size, color=color, ha=ha, va='center')

def box(x, y, w, h, top, bottom, color):
    ax.add_patch(FancyBboxPatch((x, y), w, h, boxstyle='round,pad=0.08',
        facecolor='white', edgecolor=color, linewidth=1.8))
    label(x+w/2, y+h*.67, top, 20, color, 'center')
    label(x+w/2, y+h*.29, bottom, 17, color, 'center')

label(.5, 7.93, 'A coherent symbol candidate on the target cotangent space', 23)
label(.5, 7.34, r'$p:Z=\mathbf{P}^{n}\times D\longrightarrow D$', 20)
box(.8, 4.86, 5.35, 1.44, r'$T^*Z$', r'$G\ \mathrm{coherent}$', blue)
box(.8, 1.86, 5.35, 1.44, r'$W=Z\times_D T^*D$', r'$Lj^*G\in D^{[-n,0]}_{\mathrm{coh}}(\mathcal{O}_W)$', blue)
box(9.0, 1.86, 5.3, 1.44, r'$T^*D$', r'$B=Rq_*Lj^*G\in D^{[-n,n]}_{\mathrm{coh}}$', green)

ax.annotate('', (2.92, 3.44), (2.92, 4.72), arrowprops=dict(arrowstyle='->', lw=2, color=blue))
label(3.35, 4.07, r'$Lj^*$', 19, blue)
label(3.35, 3.67, 'Vertical covectors = 0', 13, blue)
ax.annotate('', (8.84, 2.62), (6.31, 2.62), arrowprops=dict(arrowstyle='->', lw=2, color=green))
label(7.57, 3.09, r'$Rq_*$', 19, green, 'center')
label(7.57, 2.10, 'Proper\nprojective image', 13, green, 'center')

label(8.6, 5.94, r'$j(z,\eta)=(z,(dp_z)^t\eta)$', 20, ha='center')
label(8.6, 5.29, r'$q(z,\eta)=\eta$', 20, ha='center')
label(8.6, 4.61, r'$\mathrm{Supp}\ H^a(B)\ \subseteq\ q(j^{-1}\mathrm{Supp}\ G)$', 19, green, 'center')

label(.6, 1.07, 'Theorem 5.10, (5.10a)–(5.10d): coherent candidate and analytic transported support.', 17)
label(.6, .5, 'Remaining: compare with a good filtration of the actual operator image; prove the dimension bound.', 15, orange)

fig.savefig(base / 'projective-symbol-image-leaf.png', bbox_inches='tight', facecolor=fig.get_facecolor())
fig.savefig(base / 'projective-symbol-image-leaf.svg', bbox_inches='tight', facecolor=fig.get_facecolor())
plt.close(fig)
