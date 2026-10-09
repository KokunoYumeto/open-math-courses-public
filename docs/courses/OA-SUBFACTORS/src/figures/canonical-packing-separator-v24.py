"""Reproduce Figure CGP: exact maps and proved normalized cost lower bounds.

Independently authored; public domain, CC0-1.0.
Run with Python, NumPy and Matplotlib. No external images are used.
"""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch

OUT = Path(__file__).resolve().parent
plt.rcParams.update({'font.family': 'DejaVu Sans', 'svg.fonttype': 'none',
                     'font.size': 11, 'mathtext.fontset': 'dejavusans'})
fig = plt.figure(figsize=(15.2, 8.5), facecolor='white')
fig.suptitle('Canonical packing gives one actual stage and a uniform selection floor',
             fontsize=18, y=.965, fontweight='bold')
left = fig.add_axes([.035, .24, .53, .62])
left.set_xlim(0, 1); left.set_ylim(0, 1); left.axis('off')
left.set_title('Physical gluing, including the old residual lift (CGP.6–CGP.13)',
               fontsize=12, loc='left', pad=15)

def box(x, y, w, h, label, color):
    left.add_patch(FancyBboxPatch((x, y), w, h,
                   boxstyle='round,pad=0.009,rounding_size=0.018',
                   facecolor=color, edgecolor='#41546b', linewidth=1.2))
    left.text(x+w/2, y+h/2, label, ha='center', va='center',
              fontsize=12, linespacing=1.5)

blue, green, gold = '#e8f0fb', '#e6f4eb', '#fff2d2'
box(.015, .69, .32, .17, '$q_i A_j q_i$\ncanonical retained cell', blue)
box(.655, .69, .32, .17, "$r_i' U_i A_j U_i^* r_i'$\noriginal physical cut cell", green)
box(.015, .39, .32, .17, '$q_0 A_j q_0$\nwhole canonical residual', gold)
box(.655, .39, .32, .17, '$f_* W A_j W^* f_*$\nwhole physical residual', gold)
for y in [.775, .475]:
    left.add_patch(FancyArrowPatch((.345, y), (.64, y),
                   arrowstyle='-|>', mutation_scale=17, color='#364c65', linewidth=1.8))
left.text(.49, .825, '$v_i=U_i w_i^*q_i$', ha='center', fontsize=12)
left.text(.49, .525, '$v_0^*v_0=q_0$', ha='center', fontsize=12)
left.text(.49, .435, '$v_0v_0^*=f_*$', ha='center', fontsize=12)
left.text(.5, .30, r'$W=v_0+\sum_i v_i\ \in\mathcal{U}(N_k)$',
          ha='center', fontsize=14, color='#143e63')
left.text(.5, .215, r'$q_0c\in q_0A_jq_0\quad\longmapsto\quad f_*c\in WA_jW^*$',
          ha='center', fontsize=13)
left.text(.5, .12, r'$WD_jW^*\ \subset\ WB_jW^*\ \subset\ WA_jW^*$',
          ha='center', fontsize=14, color='#143e63')
left.text(.5, .025, 'Actual common continuation; all three rows; both finite traces; exact prefix/cups',
          ha='center', fontsize=10.5)

ax = fig.add_axes([.64, .38, .325, .44])
cn = np.sqrt(2)/5
x = np.linspace(0, cn, 401)
full = (cn-x)**2/2
near = (cn-x)**2/4
ax.plot(x, full, color='#136e50', linewidth=2.6, label='Full family: $(c-\\varepsilon)^2/(2h_+^2)$')
ax.plot(x, near, color='#a96e11', linewidth=2.6, label='Near-cover: $(c-\\varepsilon)^2/(4h_+^2)$')
delta = (9-4*np.sqrt(2))/200
ax.scatter([.1, .1], [delta, delta/2], c=['#136e50', '#a96e11'], s=50, zorder=4)
ax.axvline(.1, color='#64748b', linewidth=1, linestyle='--')
ax.annotate(r'$\delta/h_+^2=(9-4\sqrt{2})/200$', xy=(.1, delta),
            xytext=(.13, .026), fontsize=11, arrowprops={'arrowstyle': '->', 'color': '#136e50'})
ax.set_xlim(0, .3); ax.set_ylim(0, .044)
ax.set_xlabel(r'Original physical error $\varepsilon/h_+$', fontsize=12)
ax.set_ylabel(r'Proved floor for $\Delta/h_+^2$', fontsize=12)
ax.set_title('Every selection, every feasible packing (CGP.17–CGP.19)', fontsize=11.5, pad=12)
ax.grid(alpha=.2); ax.spines[['top', 'right']].set_visible(False)
ax.legend(loc='upper right', fontsize=9, frameon=False)
fig.text(.804, .265, '$c/h_+=\\sqrt{2}/5$; 625 fixed physical unitaries\n'
         'Actual index-25 inclusion, all-smooth amenable; prefix through $N_1$',
         ha='center', fontsize=10.5, linespacing=1.6)

fig.text(.5, .15, r'Physical mixing $\Longrightarrow$ convex closure $C$ '
         r'$\Longrightarrow$ normal $0\leq z\leq1$ in $Z(S)$', ha='center', fontsize=14)
fig.text(.5, .095, r'$\sum_i\tau(zg_i)\ \geq\ \tau(z)+\delta/2$'
         '   for every full family with target errors below $h_+/10$ (CGP.20–CGP.22)',
         ha='center', fontsize=13, color='#143e63')
fig.text(.5, .035, 'The graph is a lower bound, not an attained optimum. Rectangle areas are schematic. '
         'The full scalar trace-fiber partition remains valid.', ha='center', fontsize=10.5, color='#475569')
for suffix in ['png', 'svg']:
    fig.savefig(OUT / ('canonical-packing-separator-v24.'+suffix), dpi=160)
plt.close(fig)
print('Rendered canonical-packing-separator-v24.png and .svg')
