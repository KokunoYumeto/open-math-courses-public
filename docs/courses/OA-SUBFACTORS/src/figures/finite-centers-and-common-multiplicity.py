"""Reproducible exact two-dimensional schematic for Figure84.1."""
from pathlib import Path
from html import escape
W,H=1000,1440
p=[f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}">',
f'<rect width="{W}" height="{H}" fill="#f6f8fb"/>',
'<style>text{font-family:Arial,sans-serif;fill:#182738}.title{font-size:25px;font-weight:700}.head{font-size:20px;font-weight:700}.text{font-size:18px}.small{font-size:16px}.blue{fill:#d9e9fa;stroke:#376fa3}.gray{fill:#edf0f4;stroke:#7c8795}.green{fill:#d9eee3;stroke:#3e8260}.red{fill:#f7d8da;stroke:#a83f47}.panel{fill:#fff;stroke:#aab8c9}</style>']
def text(x,y,s,c='text'):
 p.append(f'<text x="{x}" y="{y}" class="{c}">{escape(s)}</text>')
def rect(x,y,w,h,c,rx=8):
 p.append(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{rx}" class="{c}"/>')
def panel(y,h,title):
 rect(24,y,952,h,'panel');text(44,y+34,title,'head')
def line(x1,y1,x2,y2,c='#7c8795'):
 p.append(f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="{c}" stroke-width="2"/>')
text(28,38,'Finite centers → common support → one exact integer','title')
text(28,69,'Actual core S ⊂ R, N ⊂ M; canonical lift ẑ commutes with every ambient unitary.','small')
panel(92,347,'A. Fixed finite-center constants and a uniform profile — 84.2–84.8')
rect(52,160,276,88,'blue');text(67,190,'U = Z(S), a = min τ(uᵢ)');text(67,224,'f = Cₐ(p) / Tr(p) ≤ 1/a')
rect(362,160,264,88,'blue');text(377,190,'T = Q(κ P·), κ ≥ 0');text(377,224,'Qκ = Pκ = 1')
rect(660,160,262,88,'green');text(675,190,'‖f − Tf‖₁ ≤ Γp');text(675,224,'‖f − Pf‖₂² ≤ 2Γp/a')
text(44,292,'Unweighted R₀ = QP = P*P; fixed space W = U ∩ V; gap γ on W⊥.')
text(44,338,'f₀ = Eᴡ(f); ‖f − f₀‖∞ ≤ √(2Γp / (γ a²)).')
text(44,384,'Choose Γp and all ambient unitary tolerances before selecting the projection p.')
text(44,417,'Finite joint algebra: dim(U ∨ V) ≤ dim(U) floor(d).','small')
panel(462,486,'B. Exact finite probability diagnostic: two common components — Exercise84.3')
text(44,526,'Eight joint atoms, each weight 1/8. Row atoms: 1/4; component atoms: 1/2.','small')
for b in range(2):
 x=70+465*b
 rect(x-16,553,430,244,'green' if b==0 else 'gray')
 rows=[(x+74,609),(x+74,735)]
 cols=[(x+323,609),(x+323,735)]
 for i,(xx,yy) in enumerate(rows):
  for j,(xxx,yyy) in enumerate(cols):line(xx,yy,xxx,yyy,'#3e8260' if b==0 else '#7c8795')
 for i,(xx,yy) in enumerate(rows):
  p.append(f'<circle cx="{xx}" cy="{yy}" r="8" fill="#376fa3"/>')
  text(x-2,yy-20,f's{2*b+i+1}: '+(['2+1/100','2−1/100'][i] if b==0 else '0'),'small')
 for j,(xx,yy) in enumerate(cols):
  p.append(f'<circle cx="{xx}" cy="{yy}" r="8" fill="#3e8260"/>')
  text(xx+15,yy+6,f'r{2*b+j+1}','small')
 text(x+141,672,'four edges','small')
 text(x+138,698,'weight 1/8','small')
 text(x+54,778,'selected z, α = 2' if b==0 else 'other W-atom, value 0')
text(44,839,'f = (2+1/100, 2−1/100, 0, 0); Eᴡ(f) = (2, 2, 0, 0); τ(f) = 1.')
text(44,882,'Here a = 1/4, γ = 1 and ‖f − Eᴡ(f)‖∞ = 1/100.')
text(44,924,'This diagnostic illustrates the common block; no actual Jones-core realization is claimed.','small')
panel(972,307,'C. Actual amplification and exact prescription — 84.10–84.15')
text(44,1036,'q = p ẑ; δᵤ(q) ≤ δᵤ(p)/√a. Delete Mₙ; old dimensions scale by n².')
text(44,1080,'Illustrated numbers: c = 3/5, n = 10, λ = 60, α = 2, η = 1/100.')
text(44,1124,'k = floor(λ(α−η)) = 119. Tr̃(q) = 60; Tr̃(p′) = 119/2; loss = 1/2.')
rect(95,1146,714,38,'green',0);rect(809,1146,6,38,'red',0)
text(104,1172,'rounded p′: 119/2');line(812,1184,855,1205,'#a83f47');text(846,1227,'loss 1/2','small')
text(44,1263,'ℓ = 1/120; δᵤ(p′) ≤ (δᵤ(p)/√a + 2√ℓ) / √(1−ℓ).')
text(28,1320,'Only the final bar widths encode scalar traces; graph positions and other rectangles are schematic.','small')
text(28,1363,'Proof locators: Lemmas84.1–84.3 and Theorem84.4; full argument retained beside this figure.','small')
text(28,1406,'Human source: Popa 1994, Theorem4.2.2, printed213–214. Finite-center hypothesis is explicit.','small')
p.append('</svg>')
Path(__file__).with_suffix('.svg').write_bytes(('\n'.join(p)+'\n').encode())
