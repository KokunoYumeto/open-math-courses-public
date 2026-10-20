"""The full complex two-by-two matrix catalogue, Theorem 8.2. CC0-1.0."""
from pathlib import Path
from html import escape

parts=['''<svg xmlns="http://www.w3.org/2000/svg" width="1280" height="1480" viewBox="0 0 1280 1480" role="img" aria-labelledby="title desc">
<title id="title">All complex matrix Lie subalgebras of gl2 under linear conjugacy</title>
<desc id="desc">An irreducible algebra is sl2 or gl2. A reducible algebra preserves a line, and its projection onto diagonal matrices has either the nilpotent line as kernel or zero kernel. All dimensions, scalar and Jordan lines, diagonal and triangular planes, and exact parameter relations are shown.</desc>
<rect width="1280" height="1480" fill="#f8fafc"/>
<defs><marker id="arrow" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse"><path d="M0 0 L10 5 L0 10 Z" fill="#475569"/></marker></defs>
<style>text{font-family:Arial,sans-serif;fill:#102238;font-size:22px}.title{font-size:31px;font-weight:bold}.head{font-size:25px;font-weight:bold}.small{font-size:19px}.math{font-family:Georgia,serif}</style>''']
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
def arrow(x1,y1,x2,y2):
    parts.append(f'<path d="M{x1} {y1} L{x2} {y2}" fill="none" stroke="#475569" stroke-width="2" marker-end="url(#arrow)"/>')
text(40,49,'Every matrix subalgebra, with its precise conjugacy','title')
text(40,86,'V = ℂ²,   [A,B] = AB − BA;   equivalence h ↦ P h P⁻¹, P ∈ GL₂(ℂ).','math')
box(40,110,1200,80,'#e0f2fe')
text(640,144,'Does h preserve a line L ⊂ V?','head','middle')
text(640,175,'This is a property of the matrix representation at the fixed origin.','small','middle')
arrow(340,190,340,225);arrow(930,190,930,225)
box(40,227,560,183,'#fef3c7')
text(65,265,'No: irreducible','head')
text(65,302,'π(h) = sl₂,   π(A) = A − ½ tr(A)I','math')
text(65,337,'[h,h] = sl₂  ⇒  sl₂ ⊂ h','math')
text(65,376,'h = sl₂   or   h = gl₂','head math')
box(630,227,610,183,'#dcfce7')
text(655,265,'Yes: choose L = ℂe₁','head')
text(655,302,'h ⊂ T = ⟨I,H,N⟩,   N = E₁₂','math')
text(655,337,'Diagonal image W; kernel h ∩ ℂN','math')
text(655,376,'The kernel is ℂN or zero.','head')
arrow(935,410,935,448)
box(40,450,1200,202,'#ffffff')
text(65,490,'Kernel ℂN:   h = W ⊕ ℂN','head math')
text(65,532,'dim W = 0','math');text(385,532,'dim W = 1','math');text(880,532,'dim W = 2','math')
text(65,571,'ℂN','head math');text(385,571,'B_[u:v] = ⟨N,uH+vI⟩','head math');text(880,571,'T = ⟨I,H,N⟩','head math')
text(65,616,'One nilpotent line','small');text(385,616,'[u:v] ∈ ℙ¹; exact equality only','small');text(880,616,'All upper triangular','small')
box(40,678,1200,252,'#ffffff')
text(65,720,'Kernel zero:   h = { D + β(D)N : D ∈ W }','head math')
text(65,758,'Commutativity: δ(D)β(E) = δ(E)β(D), where δ(diag(a,d)) = a−d.','math')
text(65,800,'W contains a nonscalar matrix','head');text(760,800,'W consists of scalars','head')
text(65,839,'β = tδ; shear I+tN sends the whole graph to W.','small')
text(65,882,'dim W = 1: L_[a:d];   dim W = 2: D = ⟨I,H⟩','math')
text(760,839,'h = ℂ(I+bN), or h = 0','math')
text(760,882,'b = 0: ℂI;  b ≠ 0: ℂ(I+N)','math')
box(40,958,1200,268,'#e0f2fe')
text(65,999,'No cases omitted; no hidden parameter identifications','head')
rows=[('0','0'),('1','L_[a:d] with [a:d] ~ [d:a];  ℂN;  ℂ(I+N)'),
      ('2','D;  B_[u:v] with [u:v] unchanged'),('3','T;  sl₂'),('4','gl₂')]
for i,(dim,models) in enumerate(rows):
    y=1041+36*i;text(65,y,'dim '+dim,'small');text(205,y,models,'math')
box(40,1253,1200,145,'#ecfdf5')
text(65,1293,'Why the two-dimensional parameter has an order','head')
text(65,1333,'Nilpotent set of B_[u:v] = ℂN  ⇒  L = ker N = im N is intrinsic.','math')
text(65,1370,'Its weights on L and V/L give [u:v] = [a−d:a+d]; exchanging them is not allowed.','small')
text(40,1441,'Proof: Lemma 8.1 and Theorem 8.2. Projective images: Corollary 8.3. Fixed-origin germs: Corollary 8.4.','small')
parts.append('</svg>')
Path(__file__).with_suffix('.svg').write_text('\n'.join(parts)+'\n',encoding='utf-8')
