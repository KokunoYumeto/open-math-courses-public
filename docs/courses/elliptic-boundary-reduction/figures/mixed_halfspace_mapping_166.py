"""Reproduce the exact MH9 model, MH20 Gram matrix and MH3/MH4 maps."""
from pathlib import Path
import json
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

out = Path(__file__).resolve().parent
fig, axs = plt.subplots(2, 2, figsize=(16, 10))
fig.patch.set_facecolor('#fafaf6')
for ax in axs.flat:
    ax.set_facecolor('#fafaf6')
ink, blue, red = '#182937', '#176397', '#a64032'
ax = axs[0, 0]
ax.axhline(0, color=ink, lw=1)
ax.axvline(0, color=ink, lw=1)
angle = np.linspace(0, np.pi, 250)
ax.plot(2 * np.cos(angle), 2 * np.sin(angle), '--', color=blue, lw=2)
ax.plot([0], [-1], 'x', ms=12, mew=3, color=red)
ax.text(.18, -1.06, r'Only model pole: $-i\lambda=-i$', fontsize=12, color=red)
ax.text(0, 1.1, 'Upper half-plane: no model poles', ha='center', fontsize=12, color=blue)
ax.set(xlim=(-3, 3), ylim=(-1.8, 2.3), xlabel=r'$\operatorname{Re}\kappa$', ylabel=r'$\operatorname{Im}\kappa$')
ax.set_title(r'Exact sample $\eta=0$, $\lambda=1$: $(\kappa+i)^{-1}$', fontsize=14, color=ink)
ax.set_aspect('equal', adjustable='box')

ax = axs[0, 1]
theta_negative = np.linspace(-4, -.0001, 400)
theta_positive = np.linspace(.0001, 3, 300)
ax.plot(theta_negative, -np.exp(theta_negative), color=blue, lw=2.5)
ax.plot(theta_positive, np.zeros_like(theta_positive), color=blue, lw=2.5)
ax.plot([0, 0], [-1, 0], 'o', color=blue, mfc='#fafaf6', ms=7)
ax.axvline(0, color=ink, lw=.8)
ax.axhline(0, color=ink, lw=.8)
ax.set(xlim=(-4, 3), ylim=(-1.15, .25), xlabel=r'$\theta=r-s$', ylabel=r'$\operatorname{Im}K(\theta)$')
ax.text(-3.8, -.8, r'$K(\theta)=-i e^\theta$ for $\theta<0$', fontsize=13, color=blue)
ax.text(.35, -.25, r'$K(\theta)=0$ for $\theta>0$', fontsize=13, color=blue)
ax.text(.35, -.9, 'No point value is assigned at zero.', fontsize=11, color=ink)
ax.set_title(r'MH9: the full inverse Fourier factor is $1/(2\pi)$', fontsize=14, color=ink)

ax = axs[1, 0]
ax.axis('off')
ax.set_title('MH15–MH20: keep the entire boundary-jet Gram matrix', fontsize=14, color=ink)
entries = [['3', '0', '1'], ['0', '1', '0'], ['1', '0', '3']]
table = ax.table(cellText=entries, rowLabels=['b = 0', 'b = 1', 'b = 2'], colLabels=['c = 0', 'c = 1', 'c = 2'], cellLoc='center', bbox=[.25, .40, .58, .39])
table.auto_set_font_size(False)
table.set_fontsize(16)
for (r, c), cell in table.get_celld().items():
    cell.set_edgecolor('#a4adb5')
    cell.set_facecolor('#e4eef4' if (r, c) in [(1, 2), (3, 0)] else '#fafaf6')
ax.text(.25, .84, r'$G^{(3)}=\frac{\pi}{8}$ times the displayed matrix', fontsize=16)
ax.text(.05, .27, r'$G_{02}=G_{20}=\pi/8$: the cross terms remain.', fontsize=15, color=blue)
ax.text(.05, .15, r'$\gamma_- = \pi/8,\quad \gamma_+ = \pi/2$', fontsize=16, color=ink)
ax.text(.05, .04, r'MH16 retains the extra factor $1/(2\pi)$ in the norm.', fontsize=12, color=ink)

ax = axs[1, 1]
ax.axis('off')
ax.set_title('The two exact maps, for the original order a', fontsize=14, color=ink)
ax.text(.04, .82, 'Volume input; s ≥ 0, any real t', fontsize=13, color=ink)
ax.text(.04, .66, r'$\overline{H}_{(s,t)}\ \longrightarrow\ \overline{H}_{(s-a,t)}$', fontsize=19, color=blue)
ax.text(.04, .54, r'$r^+ A e^+$; MH3, MH11–MH13', fontsize=13, color=ink)
ax.text(.04, .35, 'Boundary-supported input; every real ν and τ', fontsize=13, color=ink)
ax.text(.04, .20, r'$H_{(-m,\tau)}\ \longrightarrow\ \overline{H}_{(\nu,\tau-m-a-\nu)}$', fontsize=18, color=blue)
ax.text(.04, .07, r'$r^+ A w$, $\operatorname{supp}w\subset Y$; MH4, MH14–MH18', fontsize=13, color=ink)
fig.suptitle('Complete tangential coefficients give actual half-space maps', fontsize=20, color=ink)
fig.text(.03, .015, 'Proof source: ORIGINAL_MIXED_HALFSPACE_MAPPING_166.md, MH1–MH20. Numerical sample uses η = 0 only; no frequency weight is replaced.', fontsize=11, color=ink)
fig.tight_layout(rect=(0, .045, 1, .94), w_pad=3, h_pad=3)
fig.savefig(out / 'mixed_halfspace_mapping_166.png', dpi=180)
fig.savefig(out / 'mixed_halfspace_mapping_166.svg')
plt.close(fig)
(out / 'mixed_halfspace_mapping_166_sample.json').write_text(json.dumps({'eta': 0, 'lambda': 1, 'h': 1, 'normal_model': '(kappa+i)^(-1)', 'inverse_fourier_coefficient': '1/(2*pi)', 'negative_profile': '-i*exp(theta)', 'positive_profile': 0, 'interface_value': None, 'm3_gram_matrix_in_units_pi_over_8': [[3,0,1],[0,1,0],[1,0,3]], 'proof_locators': ['MH9', 'MH16', 'MH20', 'MH3', 'MH4']}, indent=2)+'\n', encoding='utf-8')
print(json.dumps({'png': str(out / 'mixed_halfspace_mapping_166.png'), 'svg': str(out / 'mixed_halfspace_mapping_166.svg')}))
