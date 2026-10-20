"""Reproduce the exact rank-one classification diagram. CC0-1.0."""
from pathlib import Path
from fractions import Fraction
import html

OUT = Path(__file__).with_suffix('.svg')
parts = ['''<svg xmlns="http://www.w3.org/2000/svg" width="1280" height="1160" viewBox="0 0 1280 1160" role="img" aria-labelledby="title desc">
<title id="title">Intransitive actions and projective coefficient spaces</title>
<desc id="desc">An exact classification diagram for generic rank-one holomorphic actions. The three orbit-restriction dimensions give the translation, affine and projective cases. The coefficient curve example is the conic z0 z2 equals z1 squared; a constant matrix induces x maps to x divided by one plus x.</desc>
<defs><marker id="arrow" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="8" markerHeight="8" orient="auto-start-reverse"><path d="M0 0 L10 5 L0 10z" fill="#334155"/></marker></defs>
<rect width="1280" height="1160" fill="#f8fafc"/>
<style>text{font-family:Arial,sans-serif;fill:#102238;font-size:22px}.title{font-size:32px;font-weight:bold}.sub{font-size:25px;font-weight:bold}.small{font-size:19px}.math{font-family:Georgia,serif}.blue{fill:#155e75}.green{fill:#166534}</style>''']

def text(x,y,s,cls='',anchor=None):
    a = '' if anchor is None else f' text-anchor="{anchor}"'
    parts.append(f'<text x="{x}" y="{y}" class="{cls}"{a}>{html.escape(s)}</text>')

def line(x1,y1,x2,y2,arrow=False,color='#334155',width=2):
    mark=' marker-end="url(#arrow)"' if arrow else ''
    parts.append(f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="{color}" stroke-width="{width}"{mark}/>')

def box(x,y,w,h,color='#e0f2fe'):
    parts.append(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="14" fill="{color}" stroke="#94a3b8"/>')

text(48,53,'Rank-one actions and the projective coefficient curve','title')
text(48,90,'Holomorphic germs; equivalence by local point coordinates. Theorem 7.6 and Proposition 7.7.','small')
box(48,115,1184,105)
text(640,151,'g ⊂ { f(x,y) ∂y }   →   gx = restriction to the orbit x = constant','sub math','middle')
text(640,187,'Finite dimension + the line theorem: generic d = dim gx is 1, 2, or 3.','', 'middle')
for x,centre in [(48,235),(452,639),(856,1043)]:
    line(centre,220,centre,250,True)
    box(x,254,376,260,'#ffffff')
text(235,290,'d = 1: translations','sub','middle')
text(235,329,"g′ = 0",'math','middle')
text(235,367,'∂y ∈ g  ⇒  fy = 0','math','middle')
text(235,405,'a(V) = V(x) ∂y','sub math','middle')
text(235,450,'V finite dimensional, 1 ∈ V','small','middle')
text(235,482,'All fields commute.','small','middle')
text(639,290,'d = 2: affine motions','sub','middle')
text(639,329,"g′ ≠ 0, g″ = 0",'math','middle')
text(639,367,'a(x) V ⊂ V  ⇒  a is constant','small math','middle')
text(639,405,'b(V) = C y∂y + V(x) ∂y','sub math','middle')
text(639,450,"b(V)′ = a(V)",'math small','middle')
text(639,482,'The translation ideal is intrinsic.','small','middle')
text(1043,290,'d = 3: projective motions','sub','middle')
text(1043,329,'gx ≅ sl₂; finitely many kernels','small math','middle')
text(1043,367,'Kx holomorphic  ⇒  Kx = 0','math','middle')
text(1043,405,'c = ⟨∂y, y∂y, y²∂y⟩','sub math','middle')
text(1043,450,'One constant sl₂ triple','small','middle')
text(1043,482,'No decomposition theorem needed.','small','middle')
text(48,553,'Coefficient-space equivalence for a(V) and b(V)','sub')
text(48,592,'g(φ(x)) = λ(x) C f(x),     C ∈ GLs(C),     φ′λ ≠ 0.','math')
text(48,626,'The orbit-preserving point map is X = φ(x), Y = λ(x)y + μ(x).','')
text(48,657,'For a(V): μ arbitrary.   For b(V): μ ∈ λV.   Germ base points must be matched.','small')
box(48,681,1184,430,'#ffffff')
text(76,718,'Exact conic example: V = W = ⟨1, x, x²⟩','sub')
text(76,753,'f = (1,x,x²)ᵀ;  φ = x/(1+x);  λ = 1/(1+x)²;  |x| < 1.','math')
text(76,788,'C = [(1,2,1), (0,1,1), (0,0,1)]   ⇒   [Cf(x)] = [f(φ(x))].','math')
text(76,826,'Real slice in z₀ = 1: (u,v) = (x,x²), so v = u².','small')
ox,oy,sx,sy=254,1053,228,172
line(ox-110,oy,ox+270,oy,True)
line(ox,oy+12,ox,oy-200,True)
text(ox+280,oy+8,'u','math')
text(ox-8,oy-214,'v','math')
pts=[]
for k in range(-45,101):
    t=Fraction(k,100)
    pts.append(f'{ox+sx*float(t):.3f},{oy-sy*float(t*t):.3f}')
parts.append('<polyline points="'+' '.join(pts)+'" fill="none" stroke="#155e75" stroke-width="4"/>')
for t,color,label,dx,dy in [(Fraction(1,2),'#155e75','x = 1/2',30,-30),(Fraction(1,3),'#166534','φ(x) = 1/3',-170,-17)]:
    px,py=ox+sx*float(t),oy-sy*float(t*t)
    parts.append(f'<circle cx="{px}" cy="{py}" r="7" fill="{color}"/>')
    text(px+dx,py+dy,label,'small')
line(376,1008,337,1031,True)
text(626,880,'C sends (1, 1/2, 1/4)ᵀ','math')
text(626,920,'to (9/4, 3/4, 1/4)ᵀ.','math')
text(626,960,'Dividing by 9/4 gives (1, 1/3, 1/9)ᵀ.','math')
text(626,1002,'(z₀+2z₁+z₂)z₂ − (z₁+z₂)²','math')
text(626,1042,'= z₀z₂ − z₁².','math')
text(626,1081,'Conic preservation is an exact polynomial identity.','small')
text(48,1144,'Generic normalization excludes critical transverse points; [1:x²] and [1:x] differ at x=0. Example 7.10.','small')
parts.append('</svg>')
OUT.write_text('\n'.join(parts)+'\n',encoding='utf-8')
print(str(OUT))
