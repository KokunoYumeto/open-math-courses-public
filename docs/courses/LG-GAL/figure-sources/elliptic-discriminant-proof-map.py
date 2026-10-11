"""Reproduce the odd-residue proof map; run from this file's directory."""
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch
from PIL import Image

root = Path(__file__).resolve().parents[1]
assets = root / 'assets'
assets.mkdir(exist_ok=True)
plt.rcParams.update({'font.family': 'DejaVu Sans', 'font.size': 15})
fig, ax = plt.subplots(figsize=(5, 12), dpi=180)
ax.set(xlim=(0, 5), ylim=(0, 12))
ax.axis('off')
ax.text(2.5, 11.65, 'Additive reduction', ha='center', fontsize=21, weight='bold')
ax.text(2.5, 11.25, 'Odd residue characteristic', ha='center', fontsize=17)
ax.text(2.5, 10.85, 'Discriminant, ramification and fibre geometry', ha='center', fontsize=11)
boxes = [
    (9.6, 'Cubic order  A_g = R[x]/g\nDiscriminant exponent  d', '6.0K.2–3; DA2, DA4', '#edf4ff'),
    (7.55, 'Integral closure  B_g\nDiscriminant exponent  d − 2i', 'Index  i = length(B_g/A_g)', '#edf4ff'),
    (5.5, 'Three nonzero 2-torsion points\nPermutation conductor  3 − o + δ', 'Trace dual and ramification: 6.0K.2; DA3', '#edf4ff'),
    (3.45, 'Prepared regular-model charts\nComponent count  M = 2i + 2 − o', 'All additive branches: 6.0K.4–5', '#edf8ef'),
    (1.4, 'd = M + 1 + δ = −Art(X/R)', 'Euler identity: 6.0H; DA1, DA5', '#fff4dc'),
]
for y, text, locator, colour in boxes:
    ax.add_patch(FancyBboxPatch((.3, y-.58), 4.4, 1.16, boxstyle='round,pad=.12',
                               facecolor=colour, edgecolor='#27445f', linewidth=1.3))
    ax.text(2.5, y+.15, text, ha='center', va='center', linespacing=1.6)
    ax.text(2.5, y-.42, locator, ha='center', fontsize=10, color='#37516a')
for y1, y2 in zip([9.6, 7.55, 5.5, 3.45], [7.55, 5.5, 3.45, 1.4]):
    ax.add_patch(FancyArrowPatch((2.5,y1-.73),(2.5,y2+.73),arrowstyle='-|>',
                                mutation_scale=18,color='#27445f',linewidth=1.4))
ax.text(2.5, .35, 'o: inertia orbits on the three roots\nδ: Swan conductor of H¹',
        ha='center', fontsize=11)
fig.subplots_adjust(left=0, right=1, top=1, bottom=0)
target = assets / 'elliptic-discriminant-proof-map.png'
fig.savefig(target, facecolor='white', metadata={'Software': 'Matplotlib'})
plt.close(fig)
# Retain pixels but remove software, timestamps and other incidental metadata.
with Image.open(target) as image:
    image.copy().save(target)
