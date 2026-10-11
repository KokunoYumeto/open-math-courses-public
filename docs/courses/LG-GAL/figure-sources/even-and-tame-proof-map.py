"""Reproduce the characteristic-two even-row and tame-cubic proof map."""
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch
from PIL import Image

root = Path(__file__).resolve().parents[1]
plt.rcParams.update({'font.family': 'DejaVu Sans', 'font.size': 14})
fig, ax = plt.subplots(figsize=(5, 14), dpi=180)
ax.set(xlim=(0, 5), ylim=(0, 14))
ax.axis('off')
ax.text(2.5, 13.65, 'Characteristic two', ha='center', fontsize=22, weight='bold')
ax.text(2.5, 13.27, 'An even row and the two tame families', ha='center', fontsize=14)
ax.text(2.5, 12.94, 'Every finite K/Q₂; unrestricted e and h, including h = ∞', ha='center', fontsize=10)

boxes = [
    (11.85, 'Prepared even row  r = 2g − 2\ng = min(2h, 2e + 1)', 'd = 6g − 2; M = 4g − 1: EV6–EV8', '#edf4ff'),
    (9.9, 't = x² + a₄/c;  τ = t/π^(2g−1)\nB₄ basis: 1, x/π^(g−1),\nt/π^(2g−1), xt/π^(3g−2)', 'i₄ = 6g − 4; D₄ = 4: EV10–EV16', '#edf4ff'),
    (7.95, 'z₀ = λx/π^(g−1);  vL(error) = 5\nη = (z − z₀)/τ²;  B₈ = B₄[η]\nRelative different exponent in F: 4g − 4', 'D₈ = 4g + 4; i₈ = 16g − 8: EV19–EV27', '#edf4ff'),
    (6.0, 'i₈ − i₄ = d + M − 1\nδ = 2g − 2;  f = 2g\nd = M + 1 + δ = −Art(X/R)', 'Exact even-row equality: EV27; Lemma6.0H', '#fff4dc'),
    (3.7, 'IV and IV*:  T = K(ρ), ρ³ = π; tame cubic\nSmooth special model after scaling\nσ: (X,Y) ↦ (ζ²X,Y) or (ζX,Y)\nδ = 0; f = 2; (d,M) = (4,3) or (8,7)', 'Two independent tame cases: EV28–EV34', '#edf8ef'),
    (1.75, 'After finite unramified splitting:\nB₄ = R × O_T;  B₈ = R² × O_T²\nD₄ = 2; D₈ = 4\ni₄ = d − 1; i₈ = 3d − 2\ni₈ − i₄ = d + M', 'Full product normalization: EV35–EV37', '#fff4dc'),
]
for y, text, locator, colour in boxes:
    ax.add_patch(FancyBboxPatch((.3, y-.73), 4.4, 1.46,
                 boxstyle='round,pad=.10', facecolor=colour,
                 edgecolor='#27445f', linewidth=1.3))
    ax.text(2.5, y+.12, text, ha='center', va='center', linespacing=1.45, fontsize=11.5 if y == 1.75 else 12.5)
    ax.text(2.5, y-.59, locator, ha='center', fontsize=9.1, color='#37516a')
for upper, lower in [(11.85,9.9),(9.9,7.95),(7.95,6.0),(3.7,1.75)]:
    ax.add_patch(FancyArrowPatch((2.5,upper-.88),(2.5,lower+.88),
                 arrowstyle='-|>', mutation_scale=17, color='#27445f', linewidth=1.4))
ax.text(2.5, 4.85, 'Separate proof: tame cubic good models', ha='center', fontsize=11, weight='bold')
ax.text(2.5, .25, 'Dⱼ: K-normalized discriminant exponents; iⱼ: R-lengths\nError: L = K(x); relative different: F, the degree-eight field\nShorter even rows and other additive families remain open.',
        ha='center', fontsize=8.5, linespacing=1.4)
fig.subplots_adjust(left=0, right=1, top=1, bottom=0)
target = root/'assets/even-and-tame-proof-map.png'
fig.savefig(target, facecolor='white', metadata={'Software': 'Matplotlib'})
plt.close(fig)
with Image.open(target) as rendered:
    rendered.copy().save(target)
