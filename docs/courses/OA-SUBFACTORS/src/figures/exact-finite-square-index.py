"""Independently authored CC0 schematic for Proposition31.6 and Corollary31.7."""
from pathlib import Path
from html import escape
out=['<svg xmlns="http://www.w3.org/2000/svg" width="760" height="860" viewBox="0 0 760 860" role="img" aria-labelledby="title desc">',
'<title id="title">An exact finite square forces an algebraic-integer index</title>',
'<desc id="desc">Finite matrix-frame coefficients transport to the actual factor inclusion. Its scalar Jones index is an eigenvalue of L transpose L. The strongly amenable weighted-spin index16/3, and all its positive integer powers, fail this necessary condition.</desc>',
'<defs><marker id="arrow" markerWidth="8" markerHeight="8" refX="7" refY="4" orient="auto"><path d="M0,0 L8,4 L0,8" fill="#365c78"/></marker></defs><rect width="760" height="860" fill="white"/>']
def text(x,y,s,size=18,bold=False,color='#17324a'):
 out.append(f'<text x="{x}" y="{y}" font-family="Arial, sans-serif" font-size="{size}" font-weight="{"bold" if bold else "normal"}" fill="{color}">{escape(s)}</text>')
def box(x,y,w,h,color):out.append(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="9" fill="{color}" stroke="#9eb3c5"/>')
def arrow(x,y,u,v):out.append(f'<line x1="{x}" y1="{y}" x2="{u}" y2="{v}" stroke="#365c78" stroke-width="2" marker-end="url(#arrow)"/>')
text(25,37,'What an exact finite square would imply',25,True)
text(25,70,'Actual II₁ factors P ⊂ Q;  d = [Q : P] < ∞.  Proposition 31.6.',18)
box(20,92,720,236,'#eff5fb')
text(90,135,'B',27,True);arrow(140,126,574,126);text(607,135,'Q',27,True)
text(84,163,'finite dimensional',16);text(585,163,'factor',16)
text(90,261,'A',27,True);arrow(140,253,574,253);text(607,261,'P',27,True)
arrow(99,227,99,178);arrow(619,227,619,178)
text(198,196,'E_P(B) ⊂ A',21,True)
text(198,229,'ultraweak span(BP) = Q',19,True)
text(45,305,'All embeddings are unital; E_P is the physical tracial expectation.',17)
arrow(380,339,380,365)
box(20,377,720,180,'#eef8f4')
text(40,410,'Finite frame uᵣ ∈ B for F : B → A  (Lemma 30.1)',20,True)
text(40,447,'Normal transport:  x = Σᵣ uᵣ E_P(uᵣ* x),   x ∈ Q.',19)
text(40,485,'On L²(Q):  Σᵣ uᵣ e_P uᵣ* = 1.',19)
text(40,529,'E_Q(e_P) = 1/d  ⇒  Σᵣ uᵣ uᵣ* = d1.',21,True)
arrow(380,568,380,593)
box(20,605,720,102,'#eff5fb')
text(40,640,'s = Lt,  (Lᵀs)ⱼ / tⱼ = d  ⇒  LᵀLt = dt.',22,True)
text(40,678,'det(XI − LᵀL) is monic with integer coefficients.',20)
box(20,729,720,100,'#fff3e5')
text(40,764,'Weighted spin:  dʳ = 16ʳ/3ʳ is rational and not an integer.',19,True)
text(40,799,'No exact square at any r ≥ 1. Its bicommutant holds by 62.6.',18)
text(25,850,'Proofs: 31.6–31.7. Finite-frame source: Lemma 30.1; human context: Bischoff et al., App. C.',14)
out.append('</svg>')
Path(__file__).with_name('exact-finite-square-index.svg').write_text('\n'.join(out)+'\n',encoding='utf-8')
