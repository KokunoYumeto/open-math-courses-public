"""Reproduce the central-covector curve and complete scalar operator diagram."""
from pathlib import Path
from html import escape
from math import erf
p=['<svg xmlns="http://www.w3.org/2000/svg" width="1100" height="760" viewBox="0 0 1100 760" role="img" aria-labelledby="title desc"><title id="title">Angular output reserve</title><desc id="desc">Central covectors follow sigma=16+8 kappa erf(kappa), inside the reserve cone. The sequence isometry relocates the full residual output. Its cutoff cross term is smooth flat in both original variables.</desc><rect width="1100" height="760" fill="#f7f9fc"/>']
def text(x,y,t,size=19,color='#162942'):p.append(f'<text x="{x}" y="{y}" font-family="Arial,sans-serif" font-size="{size}" fill="{color}">{escape(t)}</text>')
def line(x1,y1,x2,y2,color='#64758b',width=2):p.append(f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="{color}" stroke-width="{width}"/>')
def box(x,y,w,h,t,sub):p.append(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="10" fill="white" stroke="#355a85" stroke-width="2"/>');text(x+13,y+29,t,22);text(x+13,y+57,sub,17)
text(30,38,'A missing tangential direction supplies an output reserve',27)
text(30,70,'Example centers (c = 8, N = 16); the packet scale may be larger. Frequency tails are controlled.',18)
# Coordinates: kappa in [-4,4], eta_1 in [0,52].
px=lambda x:265+48*x;py=lambda y:390-5*y
line(px(-4.3),py(0),px(4.3),py(0));line(px(0),py(0),px(0),py(54))
for x in [-4,-2,0,2,4]:line(px(x),py(0)-4,px(x),py(0)+4);text(px(x)-7,py(0)+23,str(x),15)
for y in [16,32,48]:line(px(0)-4,py(y),px(0)+4,py(y));text(px(0)+8,py(y)+5,str(y),15)
for sign in [-1,1]:line(px(0),py(0),px(sign*4),py(8),'#8b9cad')
pts=[(x,16+8*x*erf(x)) for x in [(-4+i/32) for i in range(257)]]
p.append('<polyline fill="none" stroke="#176b8c" stroke-width="3" points="'+' '.join(f'{px(x):.3f},{py(y):.3f}' for x,y in pts)+'"/>')
text(43,111,'η₁',20);text(490,414,'κ',20);text(35,454,'σ₁(κ) = 16 + 8 κ erf(κ)',21)
text(35,484,'σ₁ ≥ 8 + 8|κ|;  |κ|/σ₁ < 1/8',18)
text(35,514,'Reserve: η₁ > 0,  |κ| < η₁/2',18)
box(545,106,510,83,'S₀ = p(Dv) D J Uχ','Full residual factor, with sequence-valued output')
box(545,224,510,83,'V(κ): modulated packet isometry','An actual isometry into one boundary box')
box(545,342,510,83,'S̃ = U⁻¹ β V(Dv) S₀','One scalar full residual on the original manifold')
for y in [189,307]:line(798,y,798,y+34,'#355a85',3)
box(35,552,1020,82,'A = Q̂ + S̃,     Q̂ = (I − P)Q','P = U⁻¹βΠβU; both norms are controlled by ‖A Dₐu‖ and the original Banach norm.')
text(35,676,'Exact cross term:  E = U⁻¹ β Π(Dv) (1 − β²) V(Dv) S₀',21)
text(35,710,'Q*E is smooth and flat in both original variables; its quadratic form is bounded by C ‖u‖²B.',18)
text(35,744,'See O0–O2, R0–R3, C0–C2 and X2. Curve samples evaluate the displayed exact function.',16)
p.append('</svg>');Path(__file__).with_name('angular-output-reserve.svg').write_text(''.join(p),'utf-8')
