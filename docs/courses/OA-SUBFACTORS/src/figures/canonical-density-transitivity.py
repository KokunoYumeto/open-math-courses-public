"""Reproducible original proof diagram, with actual types and signed cup indices."""
from pathlib import Path
from html import escape
W,H=900,1280
parts=[f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}">',
'<defs><marker id="arrow" markerWidth="8" markerHeight="8" refX="7" refY="4" orient="auto"><path d="M0,0 L8,4 L0,8" fill="#365b75"/></marker></defs>',
'<rect width="900" height="1280" fill="#f6f8fb"/>',
'<style>text{font-family:Arial,sans-serif;font-size:19px;fill:#182e43}.title{font-size:29px;font-weight:bold}.head{font-size:22px;font-weight:bold}.math{font-family:Georgia,serif;font-size:23px}.small{font-size:17px}.note{fill:#774914}.arrow{fill:none;stroke:#365b75;stroke-width:2.4;marker-end:url(#arrow)}</style>']
def text(x,y,s,cls=''):
    parts.append(f'<text x="{x}" y="{y}" class="{cls}">{escape(s)}</text>')
def panel(y,h,title):
    parts.append(f'<rect x="25" y="{y}" width="850" height="{h}" rx="14" fill="white" stroke="#b8ccd9"/>')
    text(47,y+35,title,'head')
def box(x,y,w,h,lines):
    parts.append(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="9" fill="#eaf2f9" stroke="#92acbd"/>')
    for j,s in enumerate(lines):text(x+14,y+29+28*j,s,'math' if j==0 else '')
def arrow(x,y,xx,yy):
    parts.append(f'<path d="M{x},{y} L{xx},{yy}" class="arrow"/>')
text(34,42,'The full central density is forced by two closures','title')
text(34,74,'Any finite-index II₁ chain A ⊂ B ⊂ C; no extremality or finite depth.','small')
panel(97,337,'1. Both partial closures meet at the middle factor  [66.2]')
box(48,162,340,82,['X: A–B,  Y: B–C','F ∈ End₍A–C₎(X ⊠ᴮ Y)'])
box(497,162,330,82,['Pᵧ(F) ∈ End₍A–B₎(X)','close Y with Rᵧ'])
arrow(396,204,489,204)
text(405,184,'Pᵧ','small')
box(48,281,340,78,['Qₓ(F) ∈ End₍B–C₎(Y)','close X with Sₓ'])
box(497,281,330,78,['V* (1 ⊠ F ⊠ 1) V','endomorphism of L²(B)'])
arrow(218,251,218,273)
text(237,266,'Qₓ','small')
arrow(396,320,489,320)
arrow(662,251,662,273)
text(48,402,'ℓₓ(PᵧF) = rₓ(PᵧF) = ℓᵧ(QₓF) = rᵧ(QₓF).','math')
panel(456,340,'2. Fourth roots balance the duality maps  [66.1, 66.3]')
text(48,531,'κ = κ_(A,B),  ω = κ_(B,C),  ν = κ_(A,C).','math')
text(48,570,'t = κ¼ ∈ B,   u = ω¼ ∈ B′ ∩ C,   v = tu.','math')
text(48,609,'u commutes with B; v ∈ A′ ∩ C is not yet known central.','small note')
box(48,634,779,73,['τ_C(v²z) = τ_C(νv⁻²z) for every z ∈ A′ ∩ C','Choose z = v² − νv⁻²; faithfulness gives v⁴ = ν.'])
text(48,744,'ν = κω ∈ Z(A′ ∩ C); canonical expectations compose.','math')
text(48,777,'The input centrality of ν is known from its own two-trace definition.','small')
panel(818,331,'3. Actual cups for 65.14 — here i = 1, m = 3  [66.4]')
box(48,882,353,82,['Lower: M₋₄ ⊂ M₋₂ ⊂ M₀','g₁ᵇˡᵏ = d r₋₂ r₋₃ r₋₁ r₋₂'])
box(488,882,353,82,['Upper: M₀ ⊂ M₂ ⊂ M₄','Q₀ = d e₂ e₁ e₃ e₂'])
text(48,1002,'E_(M₋₂′ ∩ M₀)(g₁ᵇˡᵏ) = d⁻²1;    rⱼ = κⱼ½ eⱼ κⱼ½.','math')
text(48,1037,'Finite domain pair: M₋₆′ ∩ M₋₂ ⊂ M₋₆′ ∩ M₀.','small')
text(48,1070,'Finite target pair: M₂′ ∩ M₆ ⊂ M₀′ ∩ M₆.','small')
text(48,1112,'No comparison arrow is proved by this density identity.','note')
text(34,1201,'Complete proof and six solutions: 66.1–66.30; all factor and cup labels are exact.','small')
text(34,1235,'Human source: Longo–Roberts, A Theory of Dimension, Theorem3.8, arXiv p.15.','small')
text(34,1264,'Concrete prerequisites:6.5,63.1–63.4; actual normalized blocked word:64.1–64.2.','small')
parts.append('</svg>')
Path(__file__).with_suffix('.svg').write_text('\n'.join(parts)+'\n',encoding='utf-8')
