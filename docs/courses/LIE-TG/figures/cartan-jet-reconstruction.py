"""Figure 7.1: finite Cartan reconstruction. Original diagram, CC0-1.0."""
from pathlib import Path
from html import escape

out=Path(__file__).with_suffix('.svg')
parts=['<svg xmlns="http://www.w3.org/2000/svg" width="520" height="1260" viewBox="0 0 520 1260" role="img" aria-labelledby="title desc">',
 '<title id="title">Finite Cartan reconstruction and the scalar exception</title>',
 '<desc id="desc">For k at least two, characteristic fibres of the first derived Cartan distribution recover projection to the previous jet level. At first order, several dependent variables force the unique maximal isotropic slope-vertical space; one dependent variable admits contact maps such as Legendre transformation.</desc>',
 '<defs><marker id="arrow" markerWidth="8" markerHeight="8" refX="7" refY="4" orient="auto"><path d="M0 0L8 4L0 8Z" fill="#24649a"/></marker></defs>',
 '<rect width="520" height="1260" fill="#fbfaf5"/>',
 '<g font-family="Segoe UI,DejaVu Sans,sans-serif" fill="#12333d">']
def text(x,y,value,size=18,weight='normal',anchor='start'):
 parts.append(f'<text x="{x}" y="{y}" font-size="{size}" font-weight="{weight}" text-anchor="{anchor}">{escape(value)}</text>')
def box(x,y,w,h,fill='#eef4f6'):
 parts.append(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="10" fill="{fill}" stroke="#678c99" stroke-width="1.4"/>')
def arrow(x1,y1,x2,y2):
 parts.append(f'<path d="M{x1} {y1}L{x2} {y2}" fill="none" stroke="#24649a" stroke-width="2" marker-end="url(#arrow)"/>')
text(260,32,'Recovering finite jet maps',24,'bold','middle')
text(260,62,'n ≥ 1, m ≥ 1; the upper square has k ≥ 2',16,anchor='middle')
for x in [24,296]:
 box(x,92,200,118);box(x,292,200,118)
 text(x+100,130,'Jᵏ, Cₖ',23,'bold','middle')
 text(x+100,165,'Vₖ = Char(Cₖ¹)',18,anchor='middle')
 text(x+100,191,'highest-jet fibre',16,anchor='middle')
 text(x+100,337,'Jᵏ⁻¹, Cₖ₋₁',23,'bold','middle')
 text(x+100,375,'lower finite jet level',16,anchor='middle')
arrow(230,148,288,148);text(260,128,'Φₖ',20,anchor='middle')
arrow(230,348,288,348);text(260,328,'Φₖ₋₁',20,anchor='middle')
for x in [124,396]:
 arrow(x,216,x,284);text(x+13,253,'πₖ,ₖ₋₁',17)
text(260,447,'Cₖ¹ = Cₖ + [Cₖ,Cₖ]',20,anchor='middle')
text(260,480,'Cₖ¹ = (dπₖ,ₖ₋₁)⁻¹ Cₖ₋₁',20,anchor='middle')
text(260,514,'Iterate the descent to J¹.',18,'bold','middle')
parts.append('<path d="M24 536H496" stroke="#9aafb4"/>')
box(24,556,472,202,'#eff5ec')
text(44,589,'m = 1: contact maps on J¹',21,'bold')
text(44,623,'Slope fibres need not be preserved.',18)
text(44,657,'Example with n = 1:',18)
text(260,691,'L(x,z,p) = (p, xp − z, x)',20,anchor='middle')
text(260,730,'q ≠ 0: Q = 1/q    (Exercise 6)',18,anchor='middle')
box(24,782,472,310,'#f6f0e8')
text(44,817,'m > 1: point maps on J⁰',21,'bold')
text(44,853,'C₁ = H ⊕ V₁,   V₁ = Hom(H, Kᵐ)',18)
text(44,889,'Let S be Levi-isotropic and let',18)
text(44,917,'s = dim(projection of S to H).',18)
text(260,957,'dim S ≤ mn − (m − 1)s',21,'bold','middle')
text(260,997,'dim S = mn  ⇒  s = 0  ⇒  S = V₁',18,anchor='middle')
text(44,1035,'V₁ is the unique isotropic mn-plane.',18)
text(44,1066,'Thus Φ₁ descends to the point space J⁰.',18)
text(260,1136,'Higher levels are unique prolongations.',20,'bold','middle')
text(260,1174,'zₖ ↦ (zₖ₋₁, P_zₖ)',22,anchor='middle')
text(260,1210,'The image plane recovers every highest derivative.',17,anchor='middle')
text(260,1242,'Lemmas 7.1–7.2 and Theorem 7.3',16,anchor='middle')
parts.append('</g></svg>')
out.write_bytes(('\n'.join(parts)+'\n').encode('utf-8'))
