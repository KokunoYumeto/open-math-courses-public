"""Reproduce full normalization and the proved universal conductor-index identity."""
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch

fig, ax = plt.subplots(figsize=(9, 22), dpi=100)
fig.patch.set_facecolor('white')
ax.set(xlim=(0, 9), ylim=(0, 22))
ax.axis('off')
plt.subplots_adjust(left=0, right=1, top=1, bottom=0)
ax.text(4.5, 21.5, 'Full normalization procedures', ha='center',
        fontsize=24, fontweight='bold')
ax.text(4.5, 20.9, 'Every finite K / Q₂; unrestricted e = v(2)',
        ha='center', fontsize=15)
ax.text(4.5, 20.45, 'Separable generic algebras; repeated residue factors allowed',
        ha='center', fontsize=12)

def box(y, text, locator, color='#edf4ff'):
    ax.add_patch(FancyBboxPatch((.6, y), 7.8, 2.45,
        boxstyle='round,pad=0.02,rounding_size=0.16',
        facecolor=color, edgecolor='#365675', linewidth=1.6))
    ax.text(4.5, y+1.62, text, ha='center', va='center',
        fontsize=15, linespacing=1.65)
    ax.text(4.5, y+.42, locator, ha='center', va='center',
        fontsize=11, color='#365675')

def arrow(top, bottom, dashed=False):
    ax.add_patch(FancyArrowPatch((4.5,top),(4.5,bottom),
        arrowstyle='-|>', mutation_scale=22, linewidth=1.8,
        color='#365675', linestyle='--' if dashed else '-'))

box(17.35, 'Integral quartic order A₄; discriminant exponent 2d\n'
    'Finite integral-coset test and strict saturation\n'
    'Full B₄; exact index i₄', '6.0P.2: NF2–NF6; at most d enlargements')
box(13.95, 'B₄ = product Cⱼ, with residue degrees fⱼ\n'
    'Normalize each actual point quadratic over Cⱼ\n'
    'Joint trace/norm maximum or dyadic square defect',
    '6.0P.3–4: NF8–NF16; all split and unramified cases included')
box(10.55, 'Full B₈; quadratic indices ℓⱼ\n'
    'i₈ = 2i₄ + Σ fⱼℓⱼ\n'
    'ν = sum of fⱼ for zero normal quadratic discriminant',
    '6.0P.5: NF17–NF21; ℓⱼ: Cⱼ-lengths; i₄, i₈: R-lengths')
box(7.15, 'δ = 2d − i₄ − Σ fⱼℓⱼ − 2 + ν/2\n'
    'Inertia orbits and the earlier finite-order Swan proof\n'
    'ν is even; nontrivial wild E[3] action gives ν = 0',
    '6.0P.5: NF22–NF23; no general conductor theorem imported', '#eaf7ef')
box(3.75, 'Universal identity proved by the coherent comparison\n'
    'i₄ + Σ fⱼℓⱼ = d + M − 1 + ν/2\n'
    'Ordinary degree, logarithmic Swan and regular-point correction',
    '6.0BI: JM1–JM32; the original full-field scope', '#eaf7ef')
for top, bottom in [(17.3,16.45),(13.9,13.05),(10.5,9.65)]:
    arrow(top,bottom)
arrow(7.1,6.25)
ax.text(5.05,6.67,'JM28–JM32: comparison closes the gap',fontsize=10,
        va='center',color='#365675')
ax.text(4.5,2.9,'All original residual preparations are covered',ha='center',
        fontsize=16,fontweight='bold')
ax.text(4.5,1.65,
        'Even star rows 2 ≤ r ≤ 2g − 3, including r < g\n'
        'II / III with v(a₃) ≥ 2; every I₀*\n'
        'III* with v(a₁) ≥ 2\n'
        'II* with v(a₁) ≥ 2 and v(a₃) ≥ 4',
        ha='center',va='center',fontsize=13,linespacing=1.75)
ax.text(4.5,.45,'All allowed higher coefficients and infinite lower-bound valuations remain included.',
        ha='center',fontsize=10)
destination=Path(__file__).resolve().parents[1]/'assets/full-normalization-proof-map.png'
fig.savefig(destination,dpi=100,metadata={'Title':'Full normalization procedures and the proved conductor-index equality'})
plt.close(fig)
print(destination.name)
