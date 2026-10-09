"""Exact matrix example; both outputs come from this one reproducible figure."""
from pathlib import Path
import json
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
plt.rcParams["svg.hashsalt"] = "oa-flow-l35-reconstruction-20261009-v1"
import numpy as np

HERE = Path(__file__).resolve().parent
OUT = HERE / 'figures'
OUT.mkdir(exist_ok=True)
energies = np.array([0, 2, 5], dtype=int)
frequency = energies[:, None] - energies[None, :]
data = {
    'energies': energies.tolist(), 'frequency_row_minus_column': frequency.tolist(),
    'action_spectrum': sorted(set(frequency.ravel().tolist())),
    'p_intervals': [
        {'range': 'r <= 0', 'projection': '0', 'rank': 0},
        {'range': '0 < r <= 2', 'projection': 'E11', 'rank': 1},
        {'range': '2 < r <= 5', 'projection': 'E11 + E22', 'rank': 2},
        {'range': '5 < r', 'projection': '1', 'rank': 3}],
    'derivation_norm': 5, 'centered_implementer': [-2.5, -0.5, 2.5],
    'centered_norm': 2.5, 'proof_locators': ['L35 Section 9, equations (34)–(35)', 'Sections 5–6, equations (24), (26)'],
    'free_mathematical_ancestry': 'Dorte Olesen, Theorem 2, Pacific J. Math. 53 (1974), pp.558–560; https://msp.org/pjm/1974/53-2/pjm-v53-n2-p23-s.pdf'
}
(OUT / 'matrix-frequencies-data.json').write_text(json.dumps(data, indent=2) + '\n', encoding='utf-8')
plt.rcParams.update({'font.family': 'DejaVu Sans', 'font.size': 13, 'svg.fonttype': 'none'})
fig, axes = plt.subplots(1, 2, figsize=(13, 6.5), gridspec_kw={'width_ratios': [1, 1.25]})
ax, stair = axes
ax.imshow(frequency, cmap='RdBu_r', vmin=-5, vmax=5)
for j in range(3):
    for k in range(3):
        value = int(frequency[j,k])
        ax.text(k, j, f'E{j+1}{k+1}\n{value:+d}' if value else f'E{j+1}{k+1}\n0',
                ha='center', va='center', color='white' if abs(value) >= 3 else '#182233', fontsize=17)
ax.set_xticks(range(3), ['h₁ = 0', 'h₂ = 2', 'h₃ = 5'])
ax.set_yticks(range(3), ['h₁ = 0', 'h₂ = 2', 'h₃ = 5'])
ax.set_xlabel('Column energy hₖ')
ax.set_ylabel('Row energy hⱼ')
ax.set_title('Frequency of Eⱼₖ = hⱼ − hₖ', pad=16)
for left, right, rank in [(-1,0,0), (0,2,1), (2,5,2), (5,6,3)]:
    stair.plot([left,right],[rank,rank], color='#174d72', linewidth=3)
for r, old in [(0,0),(2,1),(5,2)]:
    stair.plot(r, old, 'o', color='#174d72', markersize=9)
    stair.plot(r, old+1, 'o', markeredgecolor='#174d72', markerfacecolor='white', markersize=9, markeredgewidth=2)
stair.set_xlim(-1,6)
stair.set_ylim(-.4,3.5)
stair.set_xticks([0,2,5])
stair.set_yticks([0,1,2,3], ['0', 'E₁₁', 'E₁₁ + E₂₂', '1'])
stair.set_xlabel('Frequency threshold r')
stair.set_ylabel('Projection p(r) (heights show rank)')
stair.set_title('Annihilator of frequencies ≥ r', pad=16)
stair.grid(axis='x', color='#cbd5e1', linestyle=':')
stair.spines[['top','right']].set_visible(False)
fig.suptitle('h = diag(0, 2, 5)      d(x) = i[h,x]', fontsize=21, y=.98)
fig.text(.5,.10,'Action spectrum: {0, ±2, ±3, ±5}      ‖d‖ = 5      ‖h − (5/2)1‖ = 5/2', ha='center', fontsize=14)
fig.text(.5,.045,'Closed dots retain the endpoint value; open dots begin the next interval.\nExact proof: L35 §9, (34)–(35); free ancestry: Olesen, Theorem 2, pp.558–560.', ha='center', fontsize=11, color='#334155')
fig.tight_layout(rect=(0,.17,1,.92))
fig.savefig(OUT / 'matrix-frequencies.svg', metadata={'Date': None})
fig.savefig(OUT / 'matrix-frequencies.png', dpi=140)
plt.close(fig)

# A filter-support illustration for the actual comparison proof, not sampled data.
fig, (plane, explanation) = plt.subplots(1,2,figsize=(12,6),gridspec_kw={'width_ratios':[1,1]})
corners = np.array([[-2,-3],[-1,-3],[3,1],[3,2]])
plane.fill(corners[:,0],corners[:,1],color='#f4c56c',alpha=.6,label='1 ≤ λ − μ ≤ 2')
plane.plot([-3,3],[-3,3],color='#155e75',linewidth=3,label='λ = μ')
for center in [(-1.3,-2.75),(.0,-1.5),(2.0,.5)]:
    from matplotlib.patches import Rectangle
    plane.add_patch(Rectangle((center[0]-.18,center[1]-.18),.36,.36,fill=False,linewidth=2,color='#984b13'))
plane.text(-2.8,2.3,'Possible joint frequencies\nafter band comparison',color='#155e75',fontsize=12)
plane.annotate('',xy=(1.8,1.8),xytext=(.0,2.25),arrowprops={'arrowstyle':'->','color':'#155e75'})
plane.set(xlim=(-3,3),ylim=(-3,3),xlabel='α frequency λ',ylabel='Φ frequency μ')
plane.set_aspect('equal')
plane.legend(loc='lower right',fontsize=10)
plane.set_title('A difference filter misses the diagonal',fontsize=15,pad=15)
explanation.axis('off')
explanation.text(.02,.95,'Exact mechanism of Lemma 7',fontsize=19,va='top')
explanation.text(.02,.79,'α-band [a,b]  ⊆  Φ-band [a,b]\n\nDisjoint interval filters have product zero.\n\nA smooth off-diagonal joint filter is a finite\nsum of rectangle pieces; their separated\nFourier series converge in time-domain L¹.\n\nΓₜ = αₜ Φ₋ₜ has frequency λ − μ.\nEvery filter away from zero vanishes.\n\nΓ has only the zero band, so D − E = 0.',fontsize=13,va='top',linespacing=1.35)
fig.text(.5,.035,'The shaded strip illustrates supp H ⊆ [1,2]; boxes are sample localization pieces, not the full cover.\nAxes are filter coordinates. Proof: L35 Lemma 7, (20)–(21). Free ancestry: Olesen, pp.556–559.',ha='center',fontsize=10,color='#334155')
fig.tight_layout(rect=(0,.12,1,.95))
fig.savefig(OUT/'commuting-localization.svg',metadata={'Date': None})
fig.savefig(OUT/'commuting-localization.png',dpi=140)
plt.close(fig)
assert frequency.tolist() == [[0,-2,-5],[2,0,-3],[5,3,0]]
assert data['action_spectrum'] == [-5,-3,-2,0,2,3,5]
print('Exact matrix spectrum and centered norm data verified; PNG and SVG generated.')
