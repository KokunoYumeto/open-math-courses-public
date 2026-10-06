"""Reproduce the exact corner-normalization and orthogonal-error schematic."""
from pathlib import Path
from html import escape
W,H=900,1370
parts=[f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}">',
'<defs><marker id="arrow" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0L10 5L0 10" fill="#294961"/></marker></defs>',
'<rect width="900" height="1370" fill="#f7fafc"/>']
def text(x,y,s,size=21,color='#17354b',weight='normal'):
 parts.append(f'<text x="{x}" y="{y}" font-family="Arial,sans-serif" font-size="{size}" fill="{color}" font-weight="{weight}">{escape(s)}</text>')
def rect(x,y,w,h,color,stroke='none',radius=5):
 parts.append(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{radius}" fill="{color}" stroke="{stroke}"/>')
def arrow(x1,y1,x2,y2):
 parts.append(f'<path d="M{x1} {y1}L{x2} {y2}" fill="none" stroke="#294961" stroke-width="2.5" marker-end="url(#arrow)"/>')
text(32,42,'General corners → finite commuting squares',29,weight='bold')
text(32,77,'Exact corner masses, orthogonal support errors and ambient norm-one projections',20)
for y,h in [(104,300),(426,442),(890,438)]:rect(24,y,852,h,'white','#c9d6df')
text(44,143,'1. Two different normalizations; the corner index stays d',23,weight='bold')
text(44,180,'Illustrative trace t = 3/8;  q = Lₚρ(p);  e = e_R',21)
rect(44,202,389,125,'#eaf2fa','#8baac7');rect(457,202,399,125,'#e7f2ee','#75a99a')
text(62,238,'Compatible state: φ₁(q) = t² = 9/64',21,weight='bold')
text(62,278,'ψ = (64/9) φ₁ | qBq',22)
text(62,309,'ψ(q) = 1',21)
text(475,238,'Jones projection: eₚ = (8/3) qeq',21,weight='bold')
text(475,278,'eqe = (3/8)e;  Tr(eₚ) = 1',21)
text(475,309,'Corner index = dt/t = d',21)
text(44,365,'R → pR preserves the normalized trace, including the center (75.6–75.13).',20)
text(44,390,'The retained commuting factor supplies trace pairing; R need not be a factor.',19)
text(44,465,'2. Account for all orthogonal errors before finite selection',23,weight='bold')
text(44,504,'F_S = y − f_Syf_S − b;   G_s is supported entirely in f_S M f_S.',21)
text(44,543,'F_S ⟂ G_s;  ‖G_s‖₂² = compression error² + commutator error².',21)
text(44,582,'‖F_S‖₂² ≤ 2δ²τ(S).  Maximality gives S = 1 (75.18–75.19).',21)
text(44,626,'Finite selection example: R* = 1, ε = 1/10, δ = 1/40.',21)
rect(50,653,400,40,'#267aab',radius=0);rect(450,653,399,40,'#389984',radius=0);rect(849,653,1,40,'#bb4d43',radius=0)
text(50,723,'Selected supports: 400/800 + 399/800',20)
text(520,723,'Residual f_I: 1/800 (one red pixel)',20)
rect(50,750,52,24,'#bb4d43',radius=0);text(116,770,'Residual inset enlarged; this inset is not to scale.',19)
text(44,811,'‖y − b_I‖₂² ≤ 2/1600 + 1/800 = 1/400 < ε² = 1/100.',22,weight='bold')
text(44,845,'Exact removal: F − f_I F f_I = y − f_I y f_I − b_I (75.20).',20)
text(44,929,'3. Actual domains and codomains of the norm-one projections',23,weight='bold')
for y,label in [(949,'B(L²M)'),(1031,'B = ⟨M,e_R⟩ = ρ(R)′'),(1113,'M'),(1195,'N')]:
 rect(54,y,405,53,'#eaf2fa','#8baac7');text(72,y+35,label,23,weight='bold')
for y,label in [(1003,'Π: cofinal finite-dimensional averaging'),(1085,'Φ: trace-pairing density, τ(xΦ(T)) = φ(LₓT)'),(1167,'E_N: trace-preserving expectation')]:
 arrow(240,y,240,y+25);text(478,y+20,label,17)
text(478,1241,'Π_M = ΦΠ;  Π_N = E_NΦΠ',20,weight='bold')
text(44,1290,'All maps ucp; neither composite is asserted normal (75.25–75.28).',20)
parts.append('<path d="M32 1339H868" stroke="#8c5035" stroke-width="1.5" stroke-dasharray="8 6"/>')
text(32,1360,'Whole-stage alignment / generating tunnel: still open. Popa, 3.2.4(ii), 4.4.1; trace/support schematic.',16,color='#8c5035')
parts.append('</svg>')
Path(__file__).with_suffix('.svg').write_text('\n'.join(parts)+'\n',encoding='utf-8')
