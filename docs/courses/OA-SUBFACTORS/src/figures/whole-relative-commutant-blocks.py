"""Reproduce the exact two-dimensional support-repair and finite-row diagram."""
from pathlib import Path
from html import escape
W,H=900,1390
parts=[f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}">',
'<defs><marker id="arrow" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0L10 5L0 10" fill="#294961"/></marker></defs>',
'<rect width="900" height="1390" fill="#f7fafc"/>']
def text(x,y,s,size=21,color='#17354b',weight='normal'):
 parts.append(f'<text x="{x}" y="{y}" font-family="Arial,sans-serif" font-size="{size}" fill="{color}" font-weight="{weight}">{escape(s)}</text>')
def rect(x,y,w,h,color,stroke='none'):
 parts.append(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="5" fill="{color}" stroke="{stroke}"/>')
def arrow(x1,y1,x2,y2):
 parts.append(f'<path d="M{x1} {y1}L{x2} {y2}" fill="none" stroke="#294961" stroke-width="2.5" marker-end="url(#arrow)"/>')
text(32,43,'Whole finite blocks inside a residual corner',29,weight='bold')
text(32,79,'Retain f → insert the local algebra in a core → repair a finite-stage support',20)
for y,h in [(106,325),(453,425),(900,416)]:rect(24,y,852,h,'white','#c9d6df')
text(44,145,'1. A corner block enters a whole core (76.6–76.7)',23,weight='bold')
rect(45,166,387,137,'#eaf2fa','#8baac7');rect(476,166,377,137,'#e7f2ee','#75a99a')
text(61,204,'Retained whole stage: f ∈ N_m',21,weight='bold')
text(61,243,'s = fb;  b ∈ B_m',21)
text(61,282,'P_s = f(bA_m b)',21)
arrow(434,234,468,234)
text(492,204,'New whole core S₁ ⊂ R₁',21,weight='bold')
text(492,243,'f, b, s ∈ S₁;  P_s ⊂ R₁',21)
text(492,282,'All a_y ∈ R₁;  R₁ may have center.',19)
text(44,347,'Cup-tail rotation u ∈ N_m fixes A_m and inserts f into the future core.',20)
text(44,387,'s need not lie in N_m. The projection retained in the tail is f.',21,weight='bold')
text(44,417,'No BF or second central local form is used.',19)
text(44,492,'2. Repair the finite threshold without losing its whole origin',23,weight='bold')
text(44,533,'g = 1[1/2,1](E_Bⱼ¹(s));  η = ‖g − s‖₂;  |τ(g) − τ(s)| ≤ η².',21)
rect(45,554,809,124,'#fff3ea','#cba47b')
text(63,589,'Adjust s within f to r:  r ≤ f,  τ(r) = τ(g),  ‖r − s‖₂ ≤ η.',21)
text(63,626,'v ∈ U(N):  vgv* = r,  ‖v − 1‖₂ ≤ 4η.',22,weight='bold')
text(63,659,'r ∈ vBⱼ¹v*;  full finite block r(vAⱼ¹v*)r.',21)
text(44,719,'Compression error ≤ (α/8)√τ(s) + 12R*η + ξ',22,weight='bold')
text(44,758,'Four support-change units + eight target-conjugation units = twelve.',20)
text(44,799,'η < min(√τ(s)/4, α√τ(s)/(128R*));  ξ < α√τ(s)/16.',21)
text(44,839,'Final normalized errors < 9√2α/32 and 9√2α/64 (76.9–76.12).',20)
text(44,939,'3. Retain the prescribed finite prefix (76.13–76.25)',23,weight='bold')
text(44,978,'Higher index a = d^(k+1);  φE_k = φ;  actual higher core S_k ⊂ R.',21)
for x,label,color in [(45,'D ⊂ N_k','#e7f2ee'),(323,'Q ⊂ N','#eaf2fa'),(601,'P ⊂ M','#fff3ea')]:
 rect(x,999,254,54,color,'#8baac7');text(x+18,1035,label,23,weight='bold')
text(44,1093,'P = ⊕ P_rᵢ ⊕ fA_k;   Q = ⊕ Q_rᵢ ⊕ fB_k;   D = ⊕ D_rᵢ ⊕ C f.',20)
text(44,1135,'E_N(P) = Q;  E_Nₖ(P) = D;  A_k ⊂ P and B_k ⊂ Q exactly.',21)
text(44,1177,'Selected whole-stage supports: Σ τ(rᵢ) > 1 − θ;  residual τ(f) < θ.',21)
text(44,1219,'A unital M₂ ⊂ N_k commutes with P. Every earlier cup is in A_k.',21)
text(44,1261,'The selected blocks may use different ordinary continuations of the same prefix.',19)
text(44,1298,'The residual is an old corner block; it is retained in the finite square.',19)
parts.append('<path d="M32 1338H868" stroke="#8c5035" stroke-width="1.5" stroke-dasharray="8 6"/>')
text(32,1364,'Exact full whole-stage partition / single-stage alignment / generating tunnel: still open.',18,color='#8c5035')
text(32,1385,'Proof 76.1–76.25. Popa, 3.2.4(i), 4.3.1, 4.4.1. Domains/support schematic; no geometric subfactor model.',15)
parts.append('</svg>')
Path(__file__).with_suffix('.svg').write_text('\n'.join(parts)+'\n',encoding='utf-8')
