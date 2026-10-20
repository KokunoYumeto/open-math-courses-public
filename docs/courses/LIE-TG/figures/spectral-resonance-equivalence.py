"""Exact spectral, resonance and reciprocal parameter mechanisms. CC0-1.0."""
from pathlib import Path
from html import escape
parts=['''<svg xmlns="http://www.w3.org/2000/svg" width="1280" height="1320" viewBox="0 0 1280 1320" role="img" aria-labelledby="title desc">
<title id="title">Spectral, resonant and reciprocal parameter equivalence</title>
<desc id="desc">The spectral list records exponent and block length. A common spectral shift is allowed in B1 because vertical dilations belong to it, whereas A1 permits only exponent scaling. The polynomial extension coefficient transforms by t plus r+1 minus kappa times d. At resonance zero and nonzero coefficients are distinct. Exchanging coordinate foliations identifies kappa and its reciprocal.</desc>
<defs><marker id="arrow" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="8" markerHeight="8" orient="auto-start-reverse"><path d="M0 0 L10 5 L0 10z" fill="#334155"/></marker></defs>
<rect width="1280" height="1320" fill="#f8fafc"/>
<style>text{font-family:Arial,sans-serif;fill:#102238;font-size:22px}.title{font-size:31px;font-weight:bold}.sub{font-size:25px;font-weight:bold}.small{font-size:19px}.math{font-family:Georgia,serif}</style>''']
def text(x,y,s,cls='',anchor=None):
    a=''if anchor is None else f' text-anchor="{anchor}"'
    parts.append(f'<text x="{x}" y="{y}" class="{cls}"{a}>{escape(s)}</text>')
def box(x,y,w,h,color='#ffffff'):parts.append(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="13" fill="{color}" stroke="#94a3b8"/>')
def line(x1,y1,x2,y2,arrow=False):parts.append(f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="#334155" stroke-width="2"'+(' marker-end="url(#arrow)"'if arrow else '')+'/>')
text(42,49,'The exact parameter equivalence mechanisms','title')
text(42,87,'Theorem 7.15: all exponents move together; polynomial resonance retains a class.','')
box(42,112,1196,442)
text(66,151,'Spectral list: (αᵢ, nᵢ) means e^(αᵢx) P_(nᵢ−1)','sub math')
for y,vals in [(226,[0,1,3]),(360,[2,3,5])]:
    line(104,y,1082,y,True)
    for val,n in zip(vals,[1,2,1]):
        xx=145+val*167
        parts.append(f'<circle cx="{xx}" cy="{y}" r="7" fill="#155e75"/>')
        text(xx,y-19,f'α = {val}','small','middle');text(xx,y+33,f'n = {n}','small','middle')
text(1120,233,'α ∈ R','small');text(1120,367,'real slice','small')
text(640,300,'ỹ = e^(2x)y:  Σ → Σ+2;  p → p+2Y;  Y → Y.','math','middle')
text(66,435,'B₁: common affine change α → aα+b, a ≠ 0; block lengths are retained.','')
text(66,473,'A₁: common scaling α → aα only; a zero exponent stays zero.','')
text(66,514,'Thus these two lists are B₁-equivalent and A₁-inequivalent. Exercise 7.','small')
box(42,578,1196,386,'#ecfdf5')
text(66,619,'Resonance of the affine quotient lift','sub')
text(66,660,'H = xp + κY + t x^R q,   R = r+1,   kernel = Pᵣq.','math')
text(66,699,'ỹ = y + d x^R  ⇒  t → t+(R−κ)d.','math')
text(66,735,'p changes by Rd x^(R−1)q, which lies in the kernel.','small')
box(66,765,543,157);box(633,765,581,157)
text(337,807,'κ ≠ R','sub math','middle');text(337,851,'Choose d = −t/(R−κ).','math','middle');text(337,889,'Every t is equivalent to zero.','small','middle')
text(923,807,'κ = R','sub math','middle');text(923,851,'Translation leaves t unchanged.','', 'middle');text(923,889,'Constant y scale: two classes, t=0 and t≠0.','small','middle')
box(42,988,1196,259)
text(66,1027,'Exchanging the two invariant coordinate foliations','sub')
text(66,1070,'Tκ = ⟨p, q, xp+κY⟩,   κ ≠ 0,1.','math')
text(66,1112,'X = y,  ỹ = x:   diag(1,κ) → diag(κ,1) → diag(1,1/κ).','math')
text(66,1154,'The last step rescales the isotropy generator by 1/κ.','small')
text(66,1196,'The complete point-equivalence relation is κ ~ 1/κ.','')
text(42,1291,'Local holomorphic coordinates; no classification of singular orbits or restricted projective conjugacy is asserted.','small')
parts.append('</svg>')
Path(__file__).with_suffix('.svg').write_text('\n'.join(parts)+'\n',encoding='utf-8')
