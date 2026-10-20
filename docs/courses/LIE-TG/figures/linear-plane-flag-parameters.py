"""Unordered eigenlines and ordered flags, Theorem 8.2. CC0-1.0."""
from pathlib import Path
from html import escape

parts=['''<svg xmlns="http://www.w3.org/2000/svg" width="1280" height="1420" viewBox="0 0 1280 1420" role="img" aria-labelledby="title desc">
<title id="title">Which weights may be exchanged?</title>
<desc id="desc">A semisimple matrix line has two unordered eigenlines. A triangular two-dimensional algebra has an intrinsic line L, determined by its unique nilpotent matrix line, and the nonzero induced map N from V/L to L. The ordered weights a and d give parameter [a-d:a+d]. Projectivization discards scalar weights, while differentiation at a fixed origin preserves linear conjugacy.</desc>
<rect width="1280" height="1420" fill="#f8fafc"/>
<defs><marker id="arrow" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse"><path d="M0 0 L10 5 L0 10 Z" fill="#475569"/></marker></defs>
<style>text{font-family:Arial,sans-serif;fill:#102238;font-size:22px}.title{font-size:32px;font-weight:bold}.head{font-size:25px;font-weight:bold}.small{font-size:19px}.math{font-family:Georgia,serif}</style>''']
def text(x,y,s,cls='',anchor=None):
    a='' if anchor is None else f' text-anchor="{anchor}"'
    s=escape(s)
    for literal,base,sub in [('B_[u:v]','B','[u:v]'),('B_[1:1]','B','[1:1]'),('B_[1:−1]','B','[1:−1]'),('B_[0:1]','B','[0:1]'),('B_[−u:v]','B','[−u:v]'),('L_[a:d]','L','[a:d]'),('E_d','E','d')]:
        s=s.replace(literal,base+'<tspan baseline-shift="sub" font-size="75%">'+sub+'</tspan>')
    s=s.replace('B_[u:v]∨','B<tspan baseline-shift="sub" font-size="75%">[u:v]</tspan>∨')
    s=s.replace('D(Φ_*X_A)₀','D(Φ<tspan baseline-shift="sub" font-size="75%">*</tspan>X<tspan baseline-shift="sub" font-size="75%">A</tspan>)₀')
    parts.append(f'<text x="{x}" y="{y}" class="{cls}"{a}>{s}</text>')
def box(x,y,w,h,color='#ffffff'):
    parts.append(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="12" fill="{color}" stroke="#94a3b8"/>')
def arrow(x1,y1,x2,y2,both=False):
    first=' marker-start="url(#arrow)"' if both else ''
    parts.append(f'<path d="M{x1} {y1} L{x2} {y2}" fill="none" stroke="#475569" stroke-width="2" marker-end="url(#arrow)"{first}/>')
text(40,50,'The parameter belongs to the representation','title')
text(40,87,'Complex linear conjugacy retains more information than the projective image.')
box(40,115,575,342,'#e0f2fe');box(640,115,600,342,'#dcfce7')
text(65,157,'A nonscalar semisimple line','head')
text(65,198,'L_[a:d] = ℂ diag(a,d),   a ≠ d','math')
box(75,232,175,69);box(375,232,175,69)
text(162,274,'eigenline Eₐ','math','middle');text(462,274,'eigenline E_d','math','middle')
arrow(265,266,360,266,True)
text(312,327,'Basis exchange is allowed.','small','middle')
text(65,374,'[a:d] ~ [d:a]','head math')
text(65,417,'Both weights also scale with the generator.','small')
text(665,157,'A triangular matrix plane','head')
text(665,198,'B_[u:v] = ⟨N,uH+vI⟩,   (u,v) ≠ (0,0)','math')
box(675,232,190,69);box(1000,232,205,69)
text(770,273,'quotient V/L','math','middle');text(1102,273,'line L','math','middle')
arrow(879,266,985,266)
text(931,246,'N ≠ 0','small math','middle')
text(665,338,'N: V/L → L;  L = ker N = im N','math')
text(665,377,'a = u+v on L;  d = v−u on V/L','math')
text(665,417,'[u:v] = [a−d:a+d], with this fixed order.','small')
box(40,485,1200,230,'#ffffff')
text(65,528,'The intrinsic flag distinguishes s from −s','head')
text(65,569,'B_[1:1] = ⟨N, diag(2,0)⟩','math');text(675,569,'B_[1:−1] = ⟨N, diag(0,−2)⟩','math')
text(65,612,'Common kernel = 0','math');text(675,612,'Common kernel = L','math')
text(65,650,'Total image = L','math');text(675,650,'Total image = V','math')
text(65,690,'No invertible basis change can alter these dimensions.','small')
box(40,744,1200,250,'#e0f2fe')
text(65,786,'Projectivization forgets the scalar weight','head')
text(65,827,'z = x/y,   ρ(A) = (b + (a−d)z − cz²)∂z,   A = ((a,b),(c,d))','math')
text(65,867,'ker ρ = ℂI;   π(A) = A − ½ tr(A)I ∈ sl₂','math')
text(65,907,'u ≠ 0: every B_[u:v] maps to ⟨H,N⟩, independently of v/u.','math')
text(65,954,'u = 0: B_[0:1] maps to the one-dimensional nilpotent algebra ℂN.','small')
box(40,1022,1200,215,'#ecfdf5')
text(65,1064,'An analytic coordinate germ fixing 0 retains the matrix class','head')
text(65,1106,'Φ(0) = 0,  P = DΦ₀  ⇒  D(Φ_*X_A)₀ = PAP⁻¹','math')
text(65,1148,'For two already linear algebras, analytic equivalence at 0 implies linear conjugacy.','small')
text(65,1190,'This identity does not linearize arbitrary nonlinear fields.','small')
text(40,1284,'Duality is a different operation:  S B_[u:v]∨ S⁻¹ = B_[−u:v],  S exchanges the basis vectors.','small')
text(40,1324,'For u ≠ 0 it sends s = v/u to −s; Theorem 8.2 does not identify those parameters.','small')
text(40,1385,'Proof locators: Theorem 8.2, Corollaries 8.3–8.4 and Example 8.5.','small')
parts.append('</svg>')
Path(__file__).with_suffix('.svg').write_text('\n'.join(parts)+'\n',encoding='utf-8')
