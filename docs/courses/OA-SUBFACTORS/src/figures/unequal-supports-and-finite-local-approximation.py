"""Reproduce the exact two-dimensional support/transport proof schematic."""
from pathlib import Path
from html import escape
W,H=900,1330
parts=[f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}">',
'<defs><marker id="arrow" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0L10 5L0 10" fill="#294961"/></marker></defs>',
'<rect width="900" height="1330" fill="#f7fafc"/>']
def text(x,y,s,size=22,color='#17354b',weight='normal'):
 parts.append(f'<text x="{x}" y="{y}" font-family="Arial,sans-serif" font-size="{size}" fill="{color}" font-weight="{weight}">{escape(s)}</text>')
def rect(x,y,w,h,color,stroke='none'):
 parts.append(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="5" fill="{color}" stroke="{stroke}"/>')
def arrow(x1,y1,x2,y2,dashed=False):
 dash=' stroke-dasharray="8 6"' if dashed else ''
 parts.append(f'<path d="M{x1} {y1}L{x2} {y2}" fill="none" stroke="#294961" stroke-width="2.5" marker-end="url(#arrow)"{dash}/>')
text(32,42,'Keep every initial support',29,weight='bold')
text(32,76,'Unequal columns → one exact transported projection → finite local approximation',20)
for y,h in [(104,282),(412,408),(848,386)]:rect(24,y,852,h,'white','#c9d6df')
text(44,141,'1. Overlap of initial supports does not consume extra range',23,weight='bold')
text(44,176,'Lemma 74.1: Σ τ(rᵢ) ≤ 1;  yᵢ = yᵢrᵢ;  vᵢ* vⱼ = δᵢⱼrᵢ',21)
text(44,211,'Initial supports (M₈ example)',19);text(455,211,'Orthogonal final projections',19)
for y,w,label,color in [(229,170,'r₁: trace 1/4','#267aab'),(273,85,'r₂: trace 1/8','#7e5da8'),(317,85,'r₃: trace 1/8','#389984')]:
 rect(44,y,w,28,color);text(44+w+12,y+22,label,18)
arrow(360,285,430,285)
rect(455,249,170,48,'#267aab');rect(628,249,85,48,'#7e5da8');rect(716,249,85,48,'#389984')
text(455,332,'τ(g) = 1/4 + 1/8 + 1/8 = 1/2',21)
text(455,365,'The initial projections may overlap.',19)
text(44,450,'2. Transport the variable diagonal projection exactly',23,weight='bold')
text(44,485,'Illustrative data: f₁ = 1, f₂ = z, f₃ = 0; τ(z) = 1/4',21)
text(44,518,'L = 3, c = 5/4, τ(q) = 1/24, ρ = 7/8, λ = 1/7',21)
for x,label,height,color in [(55,'d₁₁f₁',112,'#267aab'),(215,'d₂₂f₂',28,'#7e5da8'),(375,'d₃₃f₃',0,'#b8c5cf')]:
 rect(x,552,126,118,'#edf2f5','#ccd7df')
 if height:rect(x+4,666-height,118,height,color)
 text(x+5,698,label,20)
text(55,731,'F = d₁₁ + d₂₂z ∈ Bₗ',21)
text(55,763,'τ(F) = 35/96',21)
arrow(530,596,593,596)
rect(615,547,221,126,'#e7f2ee','#75a99a')
text(635,581,'H = s⁰F ∈ S',22,weight='bold')
text(635,617,'τ(H) = 5/96',22)
text(635,650,'s⁰ ∈ Nₗ ∩ S',20)
text(540,725,'T₀* T₀ = H;  T₀ T₀* = g',20)
text(540,762,'V ∈ U(N):  VHV* = g',20)
text(44,801,'74.13–74.18: no column deletion and no additional padded identity.',20)
text(44,888,'3. What the estimates prove',23,weight='bold')
rect(45,912,810,96,'#e9f4ed','#8bb49b')
text(62,943,'g ∈ VSV*, τ(g) = cτ(q) > 0',21,weight='bold')
text(62,978,'Small commutators and small compression distance (Theorem 74.2)',20)
arrow(450,1010,450,1052)
rect(45,1060,810,79,'#eaf2fa','#8baac7')
text(62,1090,'sⱼ = 1[1/2,1](E_Bⱼ(g)) ∈ Bⱼ',21,weight='bold')
text(62,1123,'Finite local form for every finite test set and trace cap (74.3–74.4)',19)
arrow(740,1141,740,1172,True)
text(44,1196,'Common central support / unrestricted global and generating conclusions: open',19,color='#8c5035')
text(32,1256,'Proof locators 74.1–74.24. First local form: Popa, Theorem 4.3.1, pp. 217–219.',15)
text(32,1279,'Rounding motivation: 4.2.2, pp. 213–214. Polar completion: Appendix A.2.1, pp. 249–251.',15)
text(32,1302,'Schematic objects and trace arithmetic; not a prescribed Jones-core model.',15)
parts.append('</svg>')
Path(__file__).with_suffix('.svg').write_text('\n'.join(parts)+'\n',encoding='utf-8')
