"""Nilpotent flags and exact projective parameters, Theorem 8.9. CC0-1.0."""
from pathlib import Path
from html import escape
parts=['''<svg xmlns="http://www.w3.org/2000/svg" width="1280" height="1480" viewBox="0 0 1280 1480" role="img" aria-labelledby="title desc">
<title id="title">Nilpotent matrices determine which projective weights can move</title>
<desc id="desc">A rank-one nilpotent line determines an ordered incident flag in three-dimensional vector space. A translation nilpotent plane has common kernel and total image of dimension two; its dual nilpotent plane has both of dimension one. The ordinary parameter equivalences and the additional polarity operation are displayed separately, including two self-dual four-dimensional parameters.</desc>
<rect width="1280" height="1480" fill="#f8fafc"/>
<defs><marker id="arrow" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0 L10 5 L0 10 Z" fill="#475569"/></marker></defs>
<style>text{font-family:Arial,sans-serif;fill:#102238;font-size:22px}.title{font-size:30px;font-weight:bold}.head{font-size:25px;font-weight:bold}.small{font-size:19px}.math{font-family:Georgia,serif}</style>''']
def text(x,y,s,cls='',anchor=None):
    a='' if anchor is None else f' text-anchor="{anchor}"'
    parts.append(f'<text x="{x}" y="{y}" class="{cls}"{a}>{escape(s)}</text>')
def box(x,y,w,h,color='#fff'):parts.append(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="12" fill="{color}" stroke="#94a3b8"/>')
def arrow(x,y,xx,yy):parts.append(f'<path d="M{x} {y} L{xx} {yy}" stroke="#475569" stroke-width="2" marker-end="url(#arrow)"/>')
text(40,48,'The intrinsic flag fixes the order of the weights','title')
text(40,85,'All matrices below are represented by their unique traceless parts in sl₃(ℂ).','small')
box(40,110,1200,256,'#e0f2fe')
text(65,152,'A nilpotent line ℂN, N = E₂₃','head')
box(65,180,310,70);box(480,180,330,70);box(915,180,300,70)
text(220,222,'L = im N = ℂe₂','math','middle');text(645,222,'P = ker N = ⟨e₁,e₂⟩','math','middle');text(1065,222,'V = ℂ³','math','middle')
arrow(390,215,465,215);arrow(825,215,900,215)
text(65,289,'D(a,c) has ordered weights c on L, a on P/L, and 0 on V/P, before trace removal.','small')
text(65,331,'K₂(a,c) and F₄(a,c): [a:c] is exact under ordinary projective conjugacy.','math')
box(40,397,580,271,'#dcfce7');box(650,397,590,271,'#fef3c7')
text(65,439,'Translation nilpotent plane U','head')
text(65,480,'U = ⟨E₁₃,E₂₃⟩','math')
text(65,521,'Common kernel = total image = P','math')
text(65,559,'dim P = 2','math')
text(65,600,'T₃(a,c): unordered relative weights a,c','small')
text(65,639,'[a:c] ~ [c:a]','head math')
text(675,439,'The dual nilpotent plane U′','head')
text(675,480,'U′ = ⟨E₂₃,E₂₁⟩','math')
text(675,521,'Common kernel = total image = L','math')
text(675,559,'dim L = 1','math')
text(675,600,'W₃(a,c): unordered relative weights a−c,−c','small')
text(675,639,'[a:c] ~ [a:a−c]','head math')
box(40,699,1200,246,'#fff')
text(65,742,'Nilpotent rank and the Jordan part distinguish the exceptional rows','head')
text(65,783,'E = E₁₃+E₂₁:  e₃ → e₁ → e₂ → 0;   E² = E₂₃,   E³ = 0.','math')
text(65,824,'A nilpotent plane containing this rank-two chain differs from U and U′.','small')
text(65,864,'The mixed rows Z₃ and Z₃′ have no semisimple matrix outside their nilpotent plane.','small')
text(65,907,'The diagonal families T₃ and W₃ always have such a matrix: D(a,c), (a,c) ≠ (0,0).','small')
box(40,976,1200,295,'#e0f2fe')
text(65,1019,'Duality is an additional operation, with explicit parameter action','head')
text(65,1060,'δ(M) = −Q⁻¹MᵀQ,   Q = ((−1,0,0),(0,0,1),(0,1,0)).','math')
text(65,1101,'δ(p)=R,   δ(R)=p,   δ(q)=−q,   δ(A)=−A,   δ(B)=A+B.','math')
text(65,1142,'δD(a,c)=D(c−a,c);   T₃(a,c) ↔ W₃(c−a,c).','math')
text(65,1183,'F₄(a,c) ↔ F₄(c−a,c);   K₂(a,c) ↔ K₂(c−a,c).','math')
text(65,1230,'F₄ is self-dual exactly at [a:c]=[1:0] or [1:2].','head math')
text(40,1320,'Distinct ordinary conjugacy types can be dual: K₂(1,3) and K₂(2,3) form one such pair.','small')
text(40,1364,'One-dimensional distinct-eigenvalue lines have six parameter values from permuting three eigenlines.','small')
text(40,1420,'Proof: Theorem 8.9 and Corollary 8.10. Worked examples: Solutions 11–12.','small')
parts.append('</svg>')
Path(__file__).with_suffix('.svg').write_text('\n'.join(parts)+'\n',encoding='utf-8')
