"""Reproducible exact lattice fibre and a labelled bound example, CC0."""
from pathlib import Path
import json, math
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np

w = Path(__file__).resolve().parent
out = w.parent
out.mkdir(exist_ok=True)
points = [(s, j) for s in range(-8, 9) for j in range(-8, 9) if 2*s+3*j == 12]
assert points == [(-6, 8), (-3, 6), (0, 4), (3, 2), (6, 0)]
q, height, u, ell = 5**4*7**3, 8, 175, 1225
assert (height-1)**6 < q <= height**6 and u <= 3*height**3
weight = 25*7**(5/6)
terms = [weight*height**6/(u*ell), weight*height**5/u, weight*height**3]
assert all(t < height**6 for t in terms)

plt.rcParams.update({'font.size': 14, 'axes.titlesize': 16, 'font.family': 'DejaVu Sans'})
fig, (left, right) = plt.subplots(1, 2, figsize=(11.8, 5.4),
                                gridspec_kw={'width_ratios': [1, 1.17]})
for ax in [left, right]:
    ax.spines[['top', 'right']].set_visible(False)
left.set_title(r'One determinant fibre: $2s+3j=12$')
left.set_xlim(-8.5, 8.5); left.set_ylim(-8.5, 8.5)
left.set_aspect('equal'); left.set_xticks(range(-8, 9, 2)); left.set_yticks(range(-8, 9, 2))
left.set_xlabel('$s$'); left.set_ylabel('$j$', rotation=0, labelpad=12)
left.grid(color='#e4e8ed', linewidth=.7)
left.axhline(0, color='#8e99a5', linewidth=.7); left.axvline(0, color='#8e99a5', linewidth=.7)
xx = np.linspace(-8, 8, 200)
left.plot(xx, (12-2*xx)/3, color='#175787', linewidth=1.8)
left.scatter(*zip(*points), color='#175787', s=48, zorder=4)
left.annotate('', xy=(3, 2), xytext=(0, 4),
              arrowprops={'arrowstyle': '->', 'color': '#b55727', 'lw': 2.3}, zorder=5)
left.text(1.8, 4.1, 'step (3, −2)', color='#9f4b20', fontsize=12)
left.text(-7.6, -7.1, 'T = 8; five integer points', fontsize=12)

labels = [r'$WH^6/(UL)$', r'$WH^5/U$', r'$WH^3$']
right.set_title('Three terms in the weighted count')
right.barh([2, 1, 0], terms, color=['#175787', '#37769d', '#78a7c1'], height=.52)
right.set_yticks([2, 1, 0], labels)
right.set_xscale('log'); right.set_xlim(65, 7e5)
right.set_xlabel('Upper-bound terms; logarithmic scale')
right.axvline(height**6, color='#b55727', linestyle='--', linewidth=1.7)
right.text(height**6*1.12, 1.75, '$H^6$', color='#9f4b20')
right.set_ylim(-.5, 4)
right.text(85, 3.55, r'$q=5^4 7^3$,  $H=8$', fontsize=13)
right.text(85, 3.13, r'$U=175$,  $L=1225$', fontsize=13)
right.text(85, 2.71, r'$W=25\,7^{5/6}$', fontsize=13)
right.grid(axis='x', color='#e4e8ed', linewidth=.7)
fig.subplots_adjust(left=.065, right=.965, bottom=.17, top=.89, wspace=.46)
for suffix in ['png', 'svg']:
    fig.savefig(out/f'character-determinant-fibre.{suffix}', dpi=180,
                metadata={'Creator': 'GPT-6.1 Sol (OpenAI), Codex, Ultra'})
plt.close(fig)
(out/'character-determinant-fibre-data.json').write_text(json.dumps({
    'lattice': {'r': 2, 'h': 3, 'm': 12, 'T': 8, 'coordinates_s_j': points, 'step': [3, -2]},
    'bound_example': {'q': q, 'H': height, 'U': u, 'L': ell, 'W_exact': '25*7^(5/6)',
                     'terms_approximate': terms, 'comparison_H6': height**6},
    'proof_locators': ['Lemma5.20/equation5.58', 'Proposition5.24/equations5.67/5.70'],
    'scope': 'Exact integer fibre; numerical display of explicitly stated proved upper-bound expressions. Bars are not measured character sums.',
    'source_attribution': 'Own CC0 figure; classical Burgess method credited in the lesson. No source figure copied.'
}, indent=2)+'\n', encoding='utf-8')
print(out/'character-determinant-fibre.png')
