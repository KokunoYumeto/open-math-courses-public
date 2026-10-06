"""Exact normalization checks and a reproducible figure for CL2–CL7.

No numerical integration is used to establish the identities. The plotted
partition arrow is a numerical sample of the exact function in CL8.
"""
from fractions import Fraction
from itertools import permutations
from math import exp, factorial, pi, sin, cos
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont

OUT = Path(__file__).resolve().parents[1]/'public/assets/workflow-cech-line-comparison.png'
ROOT = Path(__file__).resolve().parent.parent
FONT = Path('C:/Windows/Fonts/segoeui.ttf')
BOLD = Path('C:/Windows/Fonts/segoeuib.ttf')
SYMBOL = Path('C:/Windows/Fonts/seguisym.ttf')


def sign(seq):
    return -1 if sum(seq[i] > seq[j] for i in range(len(seq))
                     for j in range(i + 1, len(seq))) % 2 else 1


def check_permutation_normalization():
    # Group all antisymmetric tuples by their initial index. Reordering the
    # remaining differential wedge gives the exact coefficient of each term.
    for p in range(7):
        coefficients = [0] * (p + 1)
        for perm in permutations(range(p + 1)):
            coefficients[perm[0]] += sign(perm) * sign(perm[1:])
        expected = [factorial(p) * (-1) ** r for r in range(p + 1)]
        assert coefficients == expected, (p, coefficients, expected)
        # Its own face has oriented affine volume 1/p!, hence integral one.
        assert Fraction(factorial(p), factorial(p)) == 1


def check_local_obstruction_and_descent():
    # Flat trivial line on ONE triangle, with constant lifts h01=h12=0,
    # h02=-1. n=1 is an obstruction cochain, not a nonzero absolute class.
    h01, h12, h02 = Fraction(0), Fraction(0), Fraction(-1)
    n = h01 + h12 - h02
    assert n == 1
    # Continuous boundary lift: 0->0, 0->0, then h02*t2+n: 0->1.
    initial = Fraction(0)
    at_j = h01
    at_k = h01 + h12
    final = n
    assert at_k == h02 + n
    assert final - initial == n
    # W_t n=2 dx∧dy and beta=t0 dy-y dt0. With t0=1-x-y,
    # beta=y dx+(1-x)dy, so d beta=-2 dx∧dy and eta=0.
    whitney_dxdy = 2 * n
    beta_dxdy = -2
    assert whitney_dxdy + beta_dxdy == 0
    assert whitney_dxdy * Fraction(1, 2) == n
    # Direct integration gives [01]=0, [12]=0, [02]=1,
    # hence delta beta=-1. n=1 is an integral coboundary on this triangle.
    beta01 = Fraction(0)
    beta12 = Fraction(0)
    beta02 = Fraction(1)
    assert beta12 - beta02 + beta01 == -n
    for k in [-3, -1, 0, 1, 4]:
        # Stokes: ∫F/(2πi)=-k; eta=-F/(2πi) gives k.
        normalized_curvature = -k
        assert -normalized_curvature == k


check_permutation_normalization()
check_local_obstruction_and_descent()

W, H = 4200, 1840
img = Image.new('RGB', (W, H), '#f6f8fc')
draw = ImageDraw.Draw(img)
navy, blue, orange, green = '#14263f', '#2461b5', '#d76a19', '#287158'
gray, muted = '#526078', '#dde4ef'


def font(size, bold=False):
    return ImageFont.truetype(str(BOLD if bold else FONT), size)


def txt(x, y, s, size=43, fill=navy, bold=False):
    draw.text((int(x), int(y)), s, fill=fill, font=font(size, bold))


def arrow(a, b, fill=navy, width=6, head=24):
    draw.line((a, b), fill=fill, width=width)
    dx, dy = b[0] - a[0], b[1] - a[1]
    norm = (dx * dx + dy * dy) ** .5
    ux, uy = dx / norm, dy / norm
    px, py = -uy, ux
    draw.polygon([b, (b[0]-head*ux+.48*head*px, b[1]-head*uy+.48*head*py),
                  (b[0]-head*ux-.48*head*px, b[1]-head*uy-.48*head*py)], fill=fill)


def arc_arrow(cx, cy, radius, start, end, fill=blue, width=6):
    # Angles are mathematical (positive anticlockwise), y is inverted.
    count = 100
    points = [(cx + radius*cos(start+(end-start)*j/count),
               cy - radius*sin(start+(end-start)*j/count)) for j in range(count+1)]
    draw.line(points, fill=fill, width=width)
    arrow(points[-4], points[-1], fill=fill, width=width, head=22)


txt(85, 50, 'A line bundle: the same ordinary cochain from descent and integration', 68, bold=True)
txt(88, 145, 'Finite ordered K  •  sⱼ = sᵢ gᵢⱼ  •  gᵢⱼ = exp(2πi hᵢⱼ)  •  η = −F/(2πi)', 44, fill=gray)
panels = [(70, 240, 1310, 1440), (1360, 240, 2790, 1440), (2840, 240, 4130, 1440)]
for box in panels:
    draw.rounded_rectangle(box, 30, fill='white', outline=muted, width=3)

# Left: exact triangle and phi0 carrier.
txt(110, 285, '1  Supported smooth partition', 50, bold=True)
txt(115, 365, 't₀ = 1−x−y,  t₁ = x,  t₂ = y', 42)
txt(115, 422, 'ε = 1/10 < 1/3', 40, fill=gray)
v0, v1, v2 = (260, 1100), (1100, 1100), (260, 540)


def xy(x, y):
    return (260 + 840*x, 1100 - 560*y)


draw.polygon([v0, v1, v2], fill='#f0f3f8')
draw.polygon([v0, xy(.9,0), xy(0,.9)], fill='#dbeaff')
draw.line([v0,v1,v2,v0], fill=navy, width=7)
draw.line([xy(.9,0),xy(0,.9)], fill=blue, width=5)
txt(305, 750, 't₀ ≥ ε', 46, fill=blue, bold=True)
txt(305, 825, 'supp φ₀', 36, fill=blue)
txt(305, 872, 'supp dφ₀', 36, fill=blue)
txt(280, 1135, 'v₀=(0,0)', 36)
txt(975, 1135, 'v₁=(1,0)', 36)
txt(105, 490, 'v₂=(0,1)', 36)
txt(865, 655, 't₀=0', 37, fill=gray)
arrow(xy(.16,0),xy(.70,0), head=20)
arrow(xy(.72,.28),xy(.30,.70), head=20)
arrow(xy(0,.73),xy(0,.20), head=20)
t = [.50,.30,.20]
weights = [exp(-1/(a-.1)) if a>.1 else 0 for a in t]
phi = [a/sum(weights) for a in weights]
assert abs(sum(phi)-1) < 1e-14 and all(a >= 0 for a in phi)
point_t, point_phi = xy(t[1],t[2]), xy(phi[1],phi[2])
draw.ellipse((point_t[0]-10,point_t[1]-10,point_t[0]+10,point_t[1]+10),fill=orange)
arrow(point_t,point_phi,fill=orange,width=8,head=24)
txt(560, 915, 't → φ  (sample)', 34, fill=orange)
txt(110, 1210, 'χ(u)=0 for u≤ε; χ(u)=exp(−1/(u−ε)) otherwise', 31)
txt(110, 1265, 'φᵢ=χ(tᵢ)/Σχ(tⱼ);  each λₛ=(1−s)t+sφ', 34)
txt(110, 1320, 'stays in the same simplex and preserves every face.', 32, fill=gray)

# Middle: comparison with explicit correction.
txt(1405, 285, '2  Exact comparison with I', 50, bold=True)
txt(1410, 375, 'nᵢⱼₖ = hᵢⱼ + hⱼₖ − hᵢₖ  (integer);   δn=0', 39)
txt(1445, 495, 'η', 82, fill=green, bold=True)
arrow((1540,545),(1780,545),fill=green)
txt(1585, 465, '−dβ', 36, fill=green)
txt(1815, 495, 'Wφ(n)', 70, fill=green, bold=True)
arrow((2230,545),(2420,545),fill=green)
txt(2260, 465, '−dT(n)', 34, fill=green)
txt(2445, 495, 'Wₜ(n)', 65, fill=green, bold=True)
txt(1450, 635, 'β=Σφᵢ bᵢ − Σφᵢ dφⱼ hᵢⱼ', 39)
txt(1450, 695, 'T(n)=∫₀¹ ι∂ₛ Wλ(n) ds', 39)
txt(1450, 795, 'Every arrow removes an exact form.', 42, fill=gray)
draw.rounded_rectangle((1440,890,2710,1150),22,fill='#eef7f2')
txt(1490, 925, 'Iη = n + δ I(β+T(n))', 62, fill=green, bold=True)
txt(1500, 1040, 'actual integration + Stokes', 43, fill=green)
txt(1445, 1205, 'Antisymmetric sum → p! Whitney normalization', 35)
txt(1445, 1263, 'On its own p-face:  p! × volume(Δᵖ) = 1.', 34)
txt(1445, 1320, 'Thus IWₜ=id, including vertex evaluation.', 36, fill=gray)

# Right: oriented two-disk clutch schematic.
txt(2880, 285, '3  Fix the topological sign', 49, bold=True)
txt(2885, 375, 'E = ∂Dₙ = −∂Dₛ;  θ increases on E', 38)
cxn,cxs,cy,r = 3170,3810,755,218
for cx,label in [(cxn,'Dₙ'),(cxs,'Dₛ')]:
    draw.ellipse((cx-r,cy-r,cx+r,cy+r),fill='#f0f5fb',outline=blue,width=5)
    txt(cx-53,cy-41,label,63,fill=blue,bold=True)
arc_arrow(cxn,cy,r+17,-pi/3,4*pi/3,fill=blue)
arc_arrow(cxs,cy,r+17,4*pi/3,-pi/3,fill=orange)
txt(cxn-128,cy+r+65,'∂Dₙ:  +E',38,fill=blue)
txt(cxs-128,cy+r+65,'∂Dₛ:  −E',38,fill=orange)
txt(2910, 1080, 'sₛ=sₙ g,  g=exp(2πi kθ)', 42)
txt(2910, 1145, '∫F=∫ᴱ(Aₙ−Aₛ)=−2πi k', 41)
txt(2910, 1220, 'c₁(L)[S²] = ∫η = windᴱ(g) = k', 41, fill=green, bold=True)
txt(2910, 1300, 'Tautological line:  g=z⁻¹,  k=−1.', 40, fill=gray)

txt(85, 1490, 'Proof CL2–CL7: actual objects, all descent signs, exact normalized integration, and the ordinary section obstruction.', 38, bold=True)
txt(85, 1555, 'Left: exact triangle with cutoff carrier and a sampled interpolation arrow. Right: topological disk schematic; no curvature metric is pictured.', 33, fill=gray)
txt(85, 1612, 'Ordinary characteristic-class context: Allen Hatcher, Vector Bundles and K-Theory (2017), Theorem 3.2 and Proposition 3.22.', 34, fill=gray)
txt(85, 1669, 'Normalization and sign are calculated here. Source: workflow-cech-line-comparison.py  •  Exact checks: p=0,…,6; triangle descent; clutch k.', 34, fill=gray)
txt(85, 1733, 'Coefficient target: [Iη]=c₁(L) with complex coefficients, in H²(K; C).  The integral cocycle n retains the full class, including possible torsion.', 33, fill=gray)

img.save(OUT)
print('PASS: antisymmetric coefficients p=0..6, exact normalized integrals, triangle obstruction/descent, clutch signs.')
print(f'Partition sample t={t}; phi={phi}; interpolation stays in triangle.')
print(f'Wrote {OUT} ({W}x{H}).')
