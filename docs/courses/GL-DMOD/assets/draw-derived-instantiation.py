from pathlib import Path
import json
import math
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import Circle
import numpy as np

ROOT = Path(__file__).resolve().parent
import argparse
parser = argparse.ArgumentParser()
parser.add_argument('--output', type=Path, default=ROOT)
OUT = parser.parse_args().output
OUT.mkdir(parents=True, exist_ok=True)
plt.rcParams.update({'svg.hashsalt': 'full-infinite-derived-instantiation-v1', 'font.family': 'DejaVu Sans', 'font.size': 12})
R = 1 / 32
epsilon = 1.0
A = 3 / math.sqrt(2)
K = math.sqrt(1 + epsilon**2 + A**2)
r = 1 / 1024
a = 1 / 512
bound = r + K * (a + r)
inner = R / math.sqrt(2)
assert a > r and bound < inner
assert 2 * R * math.sqrt(1 + epsilon**2) < 1 / 4
assert 2 * A * R < 1 / 4 and K * R < 1 / 4
L = 1 / 8
M = math.sqrt(epsilon**2 + A**2)
assert L * M < 1

fig, axes = plt.subplots(1, 2, figsize=(16.8, 7.3), gridspec_kw={'width_ratios': [1.05, 1.35]})
fig.patch.set_facecolor('#f7fafc')
ax = axes[0]
t = np.linspace(-R, R, 601)
width = A * (R - np.abs(t))
ax.fill_between(t, -width, width, color='#bdd3e5', alpha=.70)
ax.plot(t, width, color='#365b7b', linewidth=2)
ax.plot(t, -width, color='#365b7b', linewidth=2)
ax.add_patch(Circle((0, 0), inner, fill=False, linestyle='--', color='#445a64', linewidth=1.6))
ax.add_patch(Circle((0, 0), bound, color='#64a996', alpha=.40))
ax.add_patch(Circle((0, 0), r, color='#805f9d', alpha=.90))
ax.annotate(r'$U\subset B(0,1/1024)$', xy=(0, r), xytext=(-.034, .044),
            arrowprops={'arrowstyle': '->', 'color': '#805f9d'}, color='#684982', fontsize=12)
ax.annotate(r'$r+K_G(a+r)$' + '\n' + r'$=(1+3K_G)/1024$', xy=(bound / math.sqrt(2), bound / math.sqrt(2)),
            xytext=(-.034, -.047), arrowprops={'arrowstyle': '->', 'color': '#34836e'}, color='#216d5a', fontsize=11)
ax.text(.0005, .033, r'Open complex ball: $\rho=R/\sqrt{2}$', ha='center', fontsize=11)
ax.text(0, .077, r'$R=1/32,\ \epsilon=1,\ A=3/\sqrt{2}$', ha='center', fontsize=12)
ax.text(0, -.071, r'$D_R:\ |x|<A(R-|\Re t|)$', ha='center', fontsize=12)
ax.set(xlim=(-.040, .040), ylim=(-.081, .082), xlabel=r'Base real time $\Re t$', ylabel=r'Real slice $\Re x$')
ax.set_aspect('equal')
ax.grid(alpha=.16)
ax.set_title('Actual round domain and compact auxiliary margin', pad=20, fontsize=14)

ax = axes[1]
ax.axis('off')
ax.set_title('Strict modules for the whole relative-kernel ring', pad=20, fontsize=14)
boxes = [
    (.90, 'Full infinite symbols and every finite relation', r'Holomorphic complement kernels; common final $G$'),
    (.69, r'$\mathcal{R}=E(G;D_R)$', 'Roundness + proper fibers + literal product boundaries'),
    (.48, r'$\mathcal{F}=H^1_{S_*}(q_{G*}\mathcal{O}_\Omega)$', r'Strict $\mathcal{R}$ action; exact analytic concentration'),
    (.27, r'$\mathcal{Q}_{\mathcal{R}}=\Gamma_SJ_{\mathcal{R}}^{\bullet}(\mathcal{F})[-1]$', 'Actual module-derived support object; every-degree action'),
]
for y, title, sub in boxes:
    ax.text(.50, y, title, ha='center', va='center', fontsize=13,
            bbox={'boxstyle': 'round,pad=.5', 'facecolor': '#e9f1f6', 'edgecolor': '#5f829d'})
    ax.text(.50, y - .060, sub, ha='center', fontsize=10.5)
for upper, lower in zip(boxes, boxes[1:]):
    ax.annotate('', xy=(.50, lower[0] + .045), xytext=(.50, upper[0] - .085),
                arrowprops={'arrowstyle': '->', 'color': '#466982', 'lw': 1.8})
ax.text(.50, .095, r'Finite projectives: $dH+Hd=1$ in tensor and Hom models.', ha='center', fontsize=12)
ax.text(.50, .045, 'Arbitrary-module flatness and faithfulness remain separate.', ha='center', fontsize=11)

fig.suptitle('Full infinite-order finite diagrams on an actual derived support module', fontsize=19, y=.975, weight='bold')
fig.text(.5, .055, r'Exact $N=2$ example at one phase; $K_G=\sqrt{13/2}$, $a=1/512$, $LM_G=\sqrt{11/2}/8<1$.', ha='center', fontsize=11)
fig.text(.5, .030, 'Left: Im t = Im x = 0 only; the proof uses every complex norm. Dashed circle is an excluded open-ball boundary.', ha='center', fontsize=10.5)
fig.text(.5, .008, 'Proof: ID.1–ID.6. Free human target: Micro-hyperbolic systems, Corollary 3.2.5. No ordinary distribution limit is used.', ha='center', fontsize=10.5)
fig.subplots_adjust(left=.075, right=.985, top=.82, bottom=.15, wspace=.27)
fig.savefig(OUT / 'full-infinite-derived-instantiation.png', dpi=160, metadata={'Software': 'Reproducible mathematical figure'})
fig.savefig(OUT / 'full-infinite-derived-instantiation.svg', metadata={'Date': None, 'Creator': 'Reproducible mathematical figure'})
data = {
    'normal_dimension': 2, 'fixed_phase': 0, 'lambda_prime': 'pi/4', 'B_prime': '3/2',
    'epsilon': '1', 'A': '3/sqrt(2)', 'K_G': 'sqrt(13/2)',
    'round_R': '1/32', 'outer_coefficient_base_and_normal_radius': '1/4',
    'output_ball_r': '1/1024', 'auxiliary_halfspace_a': '1/512',
    'auxiliary_norm_bound': '(1+3*sqrt(13/2))/1024',
    'inner_open_complex_ball_radius': '1/(32*sqrt(2))',
    'auxiliary_bound_strictly_inside_round_domain': True,
    'directional_Lipschitz_L': '1/8', 'M_G': 'sqrt(11/2)', 'L_times_M_G': 'sqrt(11/2)/8',
    'full_complex_norms_proved': True, 'plot_slice': 'Im(t)=Im(x)=0',
    'strict_module': 'F=H1_(S*) q_(G*) O_Omega, over the whole canonical R=E(G;D_R)',
    'derived_object': 'Gamma_S J_R(F)[-1]',
    'proof_locators': ['ID.1', 'ID.2', 'ID.3', 'ID.4', 'ID.5', 'ID.6'],
    'free_human_target': 'https://perso.imj-prg.fr/pierre-schapira/wp-content/uploads/schapira-pub/Microhyp.pdf Corollary3.2.5',
    'ordinary_distribution_limit_asserted': False, 'arbitrary_module_flatness_asserted': False, 'license': 'CC0-1.0',
}
(OUT / 'full-infinite-derived-instantiation-data.json').write_text(json.dumps(data, indent=2) + '\n', encoding='utf-8')
