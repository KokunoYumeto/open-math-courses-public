"""Reproducible proof schematic; no geometric shape is claimed for normal fibres."""
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle
root = Path(__file__).parent
fig, ax = plt.subplots(figsize=(11.2, 5.4))
fig.patch.set_facecolor('#fbfcff')
ax.set_facecolor('#fbfcff')
ax.set_xlim(-1.45, 1.45)
ax.set_ylim(-.34, 1.40)
ax.add_patch(Rectangle((-1, 0), 2, 1, facecolor='#e8effb', edgecolor='none'))
ax.plot([-1, -1, 1, 1], [0, 1, 1, 0], color='#2f5f9e', lw=1.8, linestyle='--')
ax.plot([-1, 1], [0, 0], color='#8b3047', lw=4)
ax.plot([-1, 1], [0, 0], 'o', ms=6, mfc='#fbfcff', mec='#8b3047', mew=1.5)
for height in [.27, .53, .78]:
    ax.annotate('', xy=(.74,height), xytext=(-.72,height),
                arrowprops=dict(arrowstyle='->', color='#305887', lw=1.6))
ax.text(0, 1.23, r'$\Phi:N\times B\ \cong\ \{f\in B,\ \rho<c\}\cap V$',
        ha='center', fontsize=16, color='#14253d')
ax.text(0, 1.08, 'Projection to one base coordinate and squared normal radius',
        ha='center', fontsize=10, color='#56647a')
ax.text(0, .92, r'$U_m\cap\mathrm{tube}=B\times(N\setminus\{\nu\})$',
        ha='center', fontsize=14, color='#16395e')
ax.text(.0, .65, 'Controlled flow preserves each original stratum',
        ha='center', fontsize=11, color='#16395e', bbox=dict(fc='#e8effb', ec='none', pad=3))
ax.text(0, .40, r'$d f(\xi_k)=\partial_k,\qquad d\rho(\xi_k)=0$',
        ha='center', fontsize=14, color='#16395e', bbox=dict(fc='#e8effb', ec='none', pad=3))
ax.text(0, .12, 'Normal fibres are suppressed; dashed edges are excluded boundaries',
        ha='center', fontsize=10, color='#56647a')
ax.text(0, -.11, r'$M_m\cap\mathrm{tube}=B\times\{\nu\},\qquad \rho=0$',
        ha='center', fontsize=14, color='#8b3047')
ax.text(-1.12, 1, r'$c$', ha='right', va='center', fontsize=13)
ax.text(-1.12, 0, '$0$', ha='right', va='center', fontsize=13)
ax.text(-1.27, .53, r'$\rho$', ha='center', va='center', fontsize=15)
ax.text(-1, -.24, r'$-\varepsilon$', ha='center', fontsize=13)
ax.text(1, -.24, r'$\varepsilon$', ha='center', fontsize=13)
ax.text(0, -.25, r'$b_k$', ha='center', fontsize=15)
ax.axis('off')
fig.text(.50, .08, r'$Rj_*:[a,b]\ \mapsto\ [a,b+2n]\qquad i^!:[a,b]\ \mapsto\ [a,b+2n+1]$',
         ha='center', fontsize=15, color='#14253d')
fig.text(.50, .035, 'Closed dimension skeleta + exact c-soft extensions give the intrinsic bound; finite link coefficients remain separate.',
         ha='center', fontsize=10, color='#56647a')
fig.subplots_adjust(left=.05, right=.95, bottom=.16, top=.98)
fig.savefig(root / 'fixed-whitney-dimension-layer.png', dpi=180)
fig.savefig(root / 'fixed-whitney-dimension-layer.svg')
