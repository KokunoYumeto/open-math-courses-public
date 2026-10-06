"""Reproduce Figure49.1: exact expectation/cutoff maps and a two-level example.

No sampled operator spectrum is substituted for the proof. The plotted example
uses alpha=1/4, so its spectral thresholds are exactly 9/16 and 25/16.
"""
from pathlib import Path
from html import escape

OUT=Path(__file__).with_suffix('.svg')
parts=['<svg xmlns="http://www.w3.org/2000/svg" width="640" height="1110" viewBox="0 0 640 1110" role="img" aria-labelledby="title desc">',
       '<title id="title">A compatible hypertrace gives one finite Følner projection</title>',
       '<desc id="desc">Expectation correction, Powers–Størmer, and a common spectral cutoff; exact two-eigenvalue threshold example.</desc>',
       '<defs><marker id="arrow" markerWidth="8" markerHeight="8" refX="7" refY="4" orient="auto"><path d="M0,0 L8,4 L0,8" fill="#315b70"/></marker></defs>',
       '<rect width="640" height="1110" fill="#f9fcfe"/>']

def text(x,y,s,size=18,color='#163c50',anchor='middle',weight='normal'):
    parts.append(f'<text x="{x}" y="{y}" font-family="Arial, sans-serif" font-size="{size}" fill="{color}" text-anchor="{anchor}" font-weight="{weight}">{escape(s)}</text>')
def line(x1,y1,x2,y2,color='#315b70',arrow=False,width=2):
    parts.append(f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="{color}" stroke-width="{width}"'+(' marker-end="url(#arrow)"' if arrow else '')+'/>')
def box(y,title,detail):
    parts.append(f'<rect x="45" y="{y}" width="550" height="73" rx="9" fill="#eaf3f8" stroke="#6b96ad"/>')
    text(320,y+29,title,22,weight='bold');text(320,y+55,detail,18)
def arrow(y,label):
    line(320,y,320,y+38,arrow=True);text(342,y+24,label,16,anchor='start')

text(320,34,'One threshold tests every chosen unitary',24,weight='bold')
text(320,61,'Expected semifinite pair: E : B → A; u₁,…,uₘ ∈ M',18)
box(83,'φ is M-central and φ ∘ E = φ','φ may be singular; no normalization of A by M assumed')
arrow(156,'relative Day argument · 49.4')
box(199,'b ≥ 0, Tr(b) = 1, b bounded in B','‖E(b) − b‖₁ < δ; ‖uᵢbuᵢ* − b‖₁ < δ')
arrow(272,'apply E to the density · 49.11')
box(315,'b₀ = E(b) ∈ A; Tr(b₀) = 1','‖uᵢb₀uᵢ* − b₀‖₁ < 3δ; no equivariance needed')
arrow(388,'a = √b₀ · Powers–Størmer')
box(431,'a ∈ A; ‖a‖₂ = 1','‖uᵢauᵢ* − a‖₂² < 3δ')
arrow(504,'integrate the sum · 49.15–49.17')
box(547,'pₜ = 1(√t,∞)(a) ∈ A','∫ Tr(pₜ) dt = 1; ∫ Σᵢ defectᵢ² dt < ε²/2')
text(320,649,'δ = ε⁴/(48m²) ⇒ one nonzero finite-trace pₜ',21,weight='bold')
text(320,678,'Σᵢ ‖uᵢpₜuᵢ* − pₜ‖₂² < ε² Tr(pₜ)',20)
line(35,701,605,701,'#a8c3d1',width=1)
text(320,735,'Why a prescribed cutoff may fail',23,weight='bold')
text(320,765,'a = diag(3/4, 5/4); u swaps the coordinates',19)
text(320,793,'‖uau* − a‖₂² = 1/2; integral cutoff defect = 2',18)

x0,x1,y0=95,575,956
scale=240 # graph displays t in [0,2]; rational cutoffs plotted exactly
lo=x0+scale*9/16
hi=x0+scale*25/16
parts.append(f'<rect x="{lo}" y="847" width="{hi-lo}" height="{y0-847}" fill="#e5ba68" opacity="0.35"/>')
line(x0,y0,x1+10,y0,arrow=True);line(x0,y0,x0,823,arrow=True)
text(69,860,'2',18);text(69,959,'0',18)
text(90,819,'defect²',16,anchor='start')
line(x0,y0,lo,y0,'#126283',width=4)
line(lo,847,hi,847,'#b66e09',width=4)
line(hi,y0,x1,y0,'#126283',width=4)
for x,label in [(x0,'0'),(lo,'9/16'),(x0+scale,'1'),(hi,'25/16'),(x1,'2')]:
    line(x,y0-4,x,y0+6);text(x,986,label,16)
text(x1+14,961,'t',18,anchor='start')
text((lo+hi)/2,875,'defect² = 2',18)
text((lo+hi)/2,903,'interval length = 1',17)
text(x0+55,932,'pₜ = 1',17)
text(hi+50,932,'pₜ = 0',17)
text(320,1021,'At t = 1: orthogonal rank-one projections.',19)
text(320,1050,'Below 9/16: both are 1 and the defect vanishes.',18)
text(320,1080,'Example 49.5 · exact illustrative matrices, not a standard invariant',15)
parts.append('</svg>')
OUT.write_text('\n'.join(parts)+'\n',encoding='utf-8')
print(OUT)
