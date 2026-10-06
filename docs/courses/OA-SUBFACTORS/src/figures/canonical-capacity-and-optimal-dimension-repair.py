"""Exact reproducible SVG for Figure85.1; standard library only."""
from pathlib import Path
from html import escape
W,H=1000,1320
p=[f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}">',
f'<rect width="{W}" height="{H}" fill="#f6f8fb"/>',
'<style>text{font-family:Arial,sans-serif;fill:#182738}.title{font-size:25px;font-weight:700}.head{font-size:20px;font-weight:700}.text{font-size:18px}.small{font-size:16px}.blue{fill:#d9e9fa;stroke:#376fa3}.gray{fill:#edf0f4;stroke:#7c8795}.green{fill:#d9eee3;stroke:#3e8260}.red{fill:#f7d8da;stroke:#a83f47}.panel{fill:#fff;stroke:#aab8c9}</style>']
def text(x,y,s,c='text'):p.append(f'<text x="{x}" y="{y}" class="{c}">{escape(s)}</text>')
def rect(x,y,w,h,c,rx=8):p.append(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{rx}" class="{c}"/>')
def panel(y,h,title):rect(24,y,952,h,'panel');text(44,y+34,title,'head')
text(28,38,'Canonical capacity and the least-cost dimension repair','title')
text(28,69,'Actual N ⊂ M and core S ⊂ R; applies to both canonical rows A and B.','small')
panel(92,303,'A. Every finite represented central unit has trace at least 1 — 85.1–85.4')
rect(52,159,276,86,'blue');text(67,190,'Physical atom u, m = τ(u)');text(67,223,'K(u) finite → m K(u) ≥ 1')
rect(362,159,264,86,'blue');text(377,190,'Diffuse central region');text(377,223,'K = ∞ almost everywhere')
rect(660,159,262,86,'green');text(675,190,'K = C(1), C(e) = 1');text(675,223,'target h feasible ⇔ h ≤ K')
text(44,288,'Finite unit trace t → at most floor(t) central atoms; finite capacity part is countably atomic.')
text(44,330,'Example necessary bound: τ(u) = 1/4 → finite K(u) ≥ 4. Infinite-capacity atoms are allowed.')
text(44,371,'Capacity guarantees existence of a bounded target; it does not guarantee profile closeness.')
panel(418,434,'B. Exact trim and fill: a central-data diagnostic — 85.5–85.9')
text(44,481,'Weights (1/4, 1/4, 1/2); old dimension ζ = (3, 1, 2); target h = (2, 2, 2).')
text(44,520,'Capacity (8, 8, ∞): feasible. Bars: 60 pixels per dimension; heights encode region weights.','small')
regions=[(74,24,'Region 1: weight 1/4',3,2),(380,24,'Region 2: weight 1/4',1,2),(686,48,'Region 3: weight 1/2',2,2)]
for x,h,label,old,new in regions:
 text(x,567,label)
 text(x,605,'old p','small')
 rect(x,617,min(old,new)*60,h,'blue',0)
 if old>new:rect(x+new*60,617,(old-new)*60,h,'red',0)
 text(x,697,'repaired q','small')
 rect(x,709,min(old,new)*60,h,'blue',0)
 if new>old:rect(x+old*60,709,(new-old)*60,h,'green',0)
 text(x,792,'remove 1 × 1/4' if old>new else 'add 1 × 1/4' if new>old else 'keep entire dimension','small')
text(44,831,'‖p − q‖₂² = removed trace + added trace = 1/4 + 1/4 = ‖ζ − h‖₁ = 1/2.')
panel(875,288,'C. Feasible scalar profiles and squared amplification — 85.10–85.15')
text(44,944,'θ z ≤ Kₐ, t = θ τ(z), ρ = ‖ζ − θ z‖₁/t; the error includes all mass outside z.')
text(44,988,'Delete a common Mₙ: Knew = n²Kₐ, ζnew = n²ζ; k = floor(n²θ), b = 1/(n²θ) < 1.')
text(44,1032,'Exact minimum repair cost Dₙ = ‖n²ζ − k z‖₁; Dₙ / (k τ(z)) ≤ (ρ + b)/(1 − b).')
text(44,1076,'δᵤ(qₙ) ≤ δᵤ(p) √((1 + ρ)/(1 − b)) + 2 √((ρ + b)/(1 − b)).')
text(44,1120,'No assumption that u commutes with the smaller center; compare whole projections.')
text(28,1202,'Middle-panel bars encode dimensions and trace costs; capacities are diagnostic, not a core construction.','small')
text(28,1245,'Proof locators: Theorem85.2 (capacity), Theorem85.4 (optimal repair), Theorem85.6 (rounding).','small')
text(28,1288,'Human context: Popa 1994, Theorem4.2.2, printed213–214. The scalar-profile input remains explicit.','small')
p.append('</svg>')
Path(__file__).with_suffix('.svg').write_bytes(('\n'.join(p)+'\n').encode())
