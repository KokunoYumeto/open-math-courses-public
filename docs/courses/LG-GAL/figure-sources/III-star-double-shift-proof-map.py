"""Reproduce the full quartic/point rings in the e=1, d=14 III* range."""
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch

fig, ax = plt.subplots(figsize=(9, 26), dpi=100)
fig.patch.set_facecolor('white')
ax.set(xlim=(0, 9), ylim=(0, 26))
ax.axis('off')
plt.subplots_adjust(left=0, right=1, top=1, bottom=0)
ax.text(4.5, 25.45, 'Two point shifts in the III* branch',
        ha='center', fontsize=23, fontweight='bold')
ax.text(4.5, 24.9, 'Full integer rings and the discriminant–Artin equality',
        ha='center', fontsize=13)

def box(y, height, title, body, locator, color):
    ax.add_patch(FancyBboxPatch((.55, y), 7.9, height,
        boxstyle='round,pad=.02,rounding_size=.17',
        facecolor=color, edgecolor='#365675', linewidth=1.5))
    ax.text(4.5, y+height-.48, title, ha='center',
            fontsize=17, fontweight='bold')
    ax.text(4.5, y+height/2-.12, body, ha='center', va='center',
            fontsize=13.4, linespacing=1.65)
    ax.text(4.5, y+.2, locator, ha='center', fontsize=10.4, color='#365675')

def arrow(y):
    ax.add_patch(FancyArrowPatch((4.5, y), (4.5, y-.55),
        arrowstyle='-|>', mutation_scale=20, linewidth=1.5, color='#365675'))

box(21.6, 2.65, 'Actual translated preparation',
    'e = v(2) = 1; v(a₁), v(a₂) ≥ 2; v(a₃) ≥ 4; v(a₄) = 3\n'
    'Apply Lemma 6.0D: x = X + π²r, raising v(a₆) to ≥ 6\n'
    'On these translated coefficients: v(b₂) = 4 ⇔ d = 14; M = 8',
    '6.0R.1–2: DS1–DS6; the b₂ test is made after translation', '#edf4ff')
arrow(21.47)
box(16.95, 4.0, 'Full quartic ring: one residue cancellation',
    'c = 1 + 2ζ, c² = −3; t = x² + a₄/c\n'
    'v(x) = 3/2; v(t) = 4; choose u to cancel the leading constant\n'
    's = t − uπ⁴; v(s) = 17/4\n'
    'B₄ basis: 1, x/π, s/π⁴, xs/π⁵\n'
    'v_F = 0, 2, 1, 3; τ = s/π⁴; i₄ = 10; D₄ = 8',
    '6.0R.3: DS7–DS11; distinct valuation classes prove the full ring', '#edf4ff')
arrow(16.82)
box(13.45, 2.85, 'First point shift',
    'Choose λ with v(a₂ − π²λ²) ≥ 3; w₁ = πλx\n'
    'v_F(A + 2w₁) = 14, by the exact scalar identity DS13\n'
    'E₁ = −xs − Ux + R₁; v(U) = 4; v_F(R₁) ≥ 24',
    '6.0R.4–5: DS12–DS17; DS16 proves that U does not cancel', '#eaf7ef')
arrow(13.32)
box(9.55, 3.25, 'Second point shift',
    'V = b₂b₈/(9π⁶); v(V) = 4\n'
    'Choose μ with v(μ²V − U) ≥ 5; w₂ = μxs/π³\n'
    'v_F(w₂) = 11; v_F(w₂² − μ²Vx) ≥ 24\n'
    'E₂ has unique leading term −xs: v_F(E₂) = 23; trace = 14',
    '6.0R.5: DS18–DS20; the other error terms have valuation ≥ 24', '#eaf7ef')
arrow(9.42)
box(6.05, 2.85, 'Full point ring and relative different',
    'η = (y − w₁ − w₂)/τ¹¹; full B₈ = B₄[η]\n'
    'Normalized constant valuation 1; normalized trace valuation 3\n'
    'L/F totally ramified quadratic; upper different min(9, 6) = 6\n'
    'Point index ℓ = length over B₄ = 11; D₈ = 2D₄ + 6 = 22',
    '6.0R.6: DS21–DS24; the normalized point equation is Eisenstein', '#fff5e6')

cols = ['d', 'M', 'D₄', 'D₈', 'i₄', 'i₈', 'δ', 'f']
table = ax.table(cellText=[['14','8','8','22','10','31','5','7']],
    colLabels=cols, cellLoc='center', bbox=[.065, 4.15/26, .87, 1.25/26])
table.auto_set_font_size(False)
table.set_fontsize(14)
for (row, col), cell in table.get_celld().items():
    cell.set_edgecolor('#9cb0c7')
    cell.set_linewidth(.8)
    cell.set_facecolor('#e8f0fa' if row == 0 else '#f5f8fc')
    if row == 0: cell.get_text().set_fontweight('bold')
ax.text(4.5, 3.77, 'ε₄ = 3, ε₈ = 7, ν = 0; i₄ + ℓ = 21 = d + M − 1',
        ha='center', fontsize=12.6)
ax.text(4.5, 3.31, '−Art(X/R) = M + 1 + δ = 14 = d',
        ha='center', fontsize=16, fontweight='bold')
ax.text(4.5, 2.37,
    'Base valuation v(π) = 1; quartic valuation v_F(π) = 4.\n'
    'Normalized constants and traces use v_F; relative different uses v_L.\n'
    'Dⱼ are base discriminant exponents; iⱼ are R-lengths; ℓ is a B₄-length.\n'
    'The finite unramified extension adjoining ζ preserves all these numbers.',
    ha='center', va='center', fontsize=10.8, linespacing=1.6)
ax.text(4.5, 1.18, 'Remaining III* scope: high a₁/a₃ with e ≥ 2, or e = 1 and d = 15',
        ha='center', fontsize=11.5, fontweight='bold')
ax.text(4.5, .55, 'Every other residual family and the universal NF24 identity remain required.\n'
        'Full conditions and proof locators: Lesson 8, Sections 6.0R.1–7.',
        ha='center', va='center', fontsize=11.5, linespacing=1.6)
dest = Path(__file__).resolve().parents[1]/'assets/III-star-double-shift-proof-map.png'
fig.savefig(dest, dpi=100, metadata={'Title':'III-star double point shift and full normalization proof'})
plt.close(fig)
print(dest.name)
