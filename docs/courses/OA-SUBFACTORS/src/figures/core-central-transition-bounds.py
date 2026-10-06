"""Reproducible original diagram of the proved central transition bounds."""
from pathlib import Path
from html import escape
W,H=900,1160
p=[f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}">',
'<defs><marker id="arrow" markerWidth="8" markerHeight="8" refX="7" refY="4" orient="auto"><path d="M0,0 L8,4 L0,8" fill="#315e78"/></marker></defs>',
f'<rect width="{W}" height="{H}" fill="#f6f8fb"/>',
'<style>text{font-family:Arial,sans-serif;font-size:20px;fill:#18364c}.title{font-size:27px;font-weight:bold}.head{font-size:23px;font-weight:bold}.math{font-family:Georgia,serif;font-size:25px}.small{font-size:18px}.arrow{fill:none;stroke:#315e78;stroke-width:2.5;marker-end:url(#arrow)}</style>']
def text(x,y,s,c=''):
    p.append(f'<text x="{x}" y="{y}" class="{c}">{escape(s)}</text>')
def panel(y,h,s):
    p.append(f'<rect x="25" y="{y}" width="850" height="{h}" rx="14" fill="white" stroke="#a9bdcc"/>')
    text(47,y+37,s,'head')
def arrow(x,y,xx,yy):p.append(f'<path d="M{x},{y} L{xx},{yy}" class="arrow"/>')
text(34,42,'A common basis controls the joint center','title')
text(34,76,'General cores; exact bounds precede the remaining localization problem.','small')
panel(99,232,'1. Keep the first range and pull it down  [68.1]')
p.append('<rect x="48" y="157" width="770" height="50" fill="#e8f1f7" stroke="#789bae"/>')
p.append('<rect x="48" y="157" width="180" height="50" fill="#b9d8e9" stroke="#789bae"/>')
text(63,189,'q₁ = eK₁','math');text(283,189,'1 − eK₁: normalized trace (d − 1)/d','math')
text(48,246,'v₁ = eK₁  →  a₁ = 1;     g = Σ aᵢ* aᵢ ≥ 1.','math')
text(48,290,'t = ⌈d⌉,   b_d = 1 + d(t − 1),   1/d ≤ κ ≤ b_d/d.','math')
panel(353,310,'2. Both central transitions are bounded  [68.9–68.11]')
text(48,427,'D₀ = Z(S) ∨ Z(R)','math')
arrow(400,438,155,486);arrow(421,438,675,486)
text(78,521,'Q₀ → Z(S)','math');text(571,521,'Pκ → Z(R)','math')
text(48,568,'x ≥ 0:     x ≤ d Q₀(x),      x ≤ d Pκ(x) ≤ b_d P₀(x).','math')
text(48,613,'At most ⌊d⌋ supports of any finite partition overlap on either side.','small')
panel(685,326,'3. Comparable positive kernels can still differ  [68.17]')
pts={'s1':(124,790),'s2':(124,944),'r1':(747,790),'r2':(747,944)}
for a,b,label,dx,dy in [('s1','r1','3/2',0,-12),('s2','r2','3/2',0,-12),('s1','r2','1/2',-65,-8),('s2','r1','1/2',65,-8)]:
    x,y=pts[a];xx,yy=pts[b]
    p.append(f'<path d="M{x},{y} L{xx},{yy}" stroke="#315e78" stroke-width="2"/>')
    text((x+xx)/2+dx,(y+yy)/2+dy,label,'math')
for label,(x,y) in pts.items():
    p.append(f'<circle cx="{x}" cy="{y}" r="28" fill="#e8f1f7" stroke="#315e78"/>')
    text(x-13,y+8,label,'math')
text(48,986,'Each edge has joint measure 1/4; κ has both marginals 1.','small')
text(34,1051,'b = (1, 3):    Q₀ b = (2, 2),    Qκ b = (3/2, 5/2).','math')
text(34,1090,'Proved: small ‖ζ − Qκ P₀ ζ‖₁/c from relative Følner  [68.13].','small')
text(34,1128,'Still required: the stronger joint-density or compressed-mixing input.','small')
p.append('</svg>')
Path(__file__).with_suffix('.svg').write_text('\n'.join(p)+'\n',encoding='utf-8')
