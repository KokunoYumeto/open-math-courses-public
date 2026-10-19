"""CC0: exact opposite-model cups and the existing PG abstract-pair obstruction."""
from pathlib import Path
from html import escape
from fractions import Fraction as F
import json
import itertools
R=Path(__file__).resolve().parent
def canvas(height,title):return [f'<svg xmlns="http://www.w3.org/2000/svg" width="760" height="{height}" viewBox="0 0 760 {height}" role="img"><title>{escape(title)}</title><defs><marker id="a" markerWidth="8" markerHeight="8" refX="7" refY="4" orient="auto"><path d="M0,0 L8,4 L0,8" fill="#365c78"/></marker></defs>',f'<rect width="760" height="{height}" fill="white"/>']
def text(out,x,y,s,size=18,bold=False):out.append(f'<text x="{x}" y="{y}" font-family="Arial, sans-serif" font-size="{size}" font-weight="{"bold" if bold else "normal"}" fill="#17324a">{escape(s)}</text>')
def box(out,x,y,w,h,c):out.append(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="8" fill="{c}" stroke="#9eb3c5"/>')
def arrow(out,x,y,u,v):out.append(f'<line x1="{x}" y1="{y}" x2="{u}" y2="{v}" stroke="#365c78" stroke-width="2" marker-end="url(#a)"/>')
out=canvas(1050,'The canonical tracial tower inside the actual opposite model')
text(out,25,36,'The actual opposite model has its own tracial cup',23,True)
text(out,25,69,'Bⱼ = Mⱼ′ ∩ T;  λ = 1/d.  No factoriality of Bⱼ is assumed.',18)
box(out,20,90,720,166,'#eff5fb')
for x,s in [(52,'Mⱼ₋₁'),(320,'Mⱼ'),(581,'Mⱼ₊₁')]:text(out,x,128,s,24,True)
arrow(out,152,120,284,120);arrow(out,410,120,553,120)
for x,s in [(52,'Bⱼ₊₁'),(320,'Bⱼ'),(581,'Bⱼ₋₁')]:text(out,x,213,s,24,True)
arrow(out,152,204,284,204);arrow(out,410,204,553,204)
text(out,47,244,'The bottom row consists of fixed actual commutants in the finite T.',17)
box(out,20,278,720,173,'#fff4e7')
text(out,40,312,'Original cup eⱼ:  E_Bⱼ(eⱼ) = λhⱼ',21,True)
text(out,40,349,'hⱼ = ηⱼ(κⱼ⁻¹) > 0;  Fⱼ(x) = Eⱼ(hⱼ¹ᐟ² x hⱼ¹ᐟ²).',19)
text(out,40,384,'eⱼ x eⱼ = Fⱼ(x)eⱼ;  τ(Fⱼ(x)) = τ(hⱼx).',19)
text(out,40,423,'Eⱼ : Bⱼ → Bⱼ₊₁ preserves the inherited trace.',19)
arrow(out,380,462,380,486)
box(out,20,498,720,183,'#eef8f4')
text(out,40,534,'Corrected cup qⱼ = hⱼ⁻¹ᐟ² eⱼ hⱼ⁻¹ᐟ²',22,True)
text(out,40,573,'qⱼ x qⱼ = Eⱼ(x)qⱼ;   E_Bⱼ(qⱼ) = λ1.',20)
text(out,40,611,'W*(Bⱼ, qⱼ) = Bⱼ₋₁;   qⱼ has full central support.',19)
text(out,40,651,'Canonical trace on the whole basic construction:  Tr = dτ.',19,True)
box(out,20,704,720,259,'#eff5fb')
text(out,40,738,'Actual weighted spin: p = 1/4, q = 3/4, λ = 3/16.',19,True)
for yy,label,a,b in [(773,'First-site labels','P₀','P₁'),(809,'h','3','1/3'),(845,'E_Bⱼ(eⱼ)','9/16','1/16'),(881,'E_Bⱼ(qⱼ)','3/16','3/16')]:
 text(out,40,yy,label,18);text(out,407,yy,a,18);text(out,604,yy,b,18)
text(out,40,928,'Cup vectors on 01,10:  (√3/2, 1/2)  →  (1/2, √3/2).',18)
text(out,25,997,'Proofs 63.6–63.8; exact weighted-spin calculation: Exercise 63.7.',17)
text(out,25,1029,'Human context: Popa, Classification of amenable subfactors, §1.4.3, printed188.',15)
out.append('</svg>');(R/'opposite-tracial-tower.svg').write_text('\n'.join(out)+'\n',encoding='utf-8')
out=canvas(610,'The actual strongly amenable index-ten original and opposite pairs are not isomorphic')
text(out,25,36,'An unmarked pair map must preserve these weights',23,True)
text(out,25,69,'The same actual index-ten PG model; both larger algebras are II₁ factors.',17)
groups=[('Original: M₋₁ ⊂ M₀','C_[0,0] = ℂ³',[F(2,5),F(1,5),F(2,5)],'#2678b2',40),('Opposite: R₂ ⊂ R₁','C_[1,1] = ℂ³',[F(1,4),F(1,2),F(1,4)],'#24856c',412)]
for title,algebra,weights,color,x0 in groups:
 text(out,x0,116,title,20,True);text(out,x0,146,algebra,18)
 out.append(f'<line x1="{x0}" y1="383" x2="{x0+296}" y2="383" stroke="#7990a3"/>')
 for i,w in enumerate(weights):
  x=x0+16+95*i;h=float(w)*400;y=383-h
  out.append(f'<rect x="{x}" y="{y}" width="66" height="{h}" fill="{color}"/>')
  text(out,x+11,y-14,str(w),19,True);text(out,x+19,414,'P'+str(i),18)
box(out,20,447,720,107,'#fff4e7')
text(out,40,483,'{1/5, 2/5, 2/5}  ≠  {1/4, 1/4, 1/2}',23,True)
text(out,40,522,'No permutation of the minimal projections preserves their traces.',19)
text(out,25,582,'Proof 63.9, equations63.37–63.38. Actual model: PG1–PG14; bar scale: 400px/trace unit.',14)
out.append('</svg>');(R/'nonextremal-opposite-pair.svg').write_text('\n'.join(out)+'\n',encoding='utf-8')
assert sorted(groups[0][2])!=sorted(groups[1][2]) and sum(groups[0][2])==sum(groups[1][2])==1
assert all(tuple(groups[0][2])!=p for p in itertools.permutations(groups[1][2]))
# Exact two-site arithmetic in Q(sqrt(3)); no numeric diagonalization.
def z(a=0,b=0):return (F(a),F(b))
def add(x,y):return (x[0]+y[0],x[1]+y[1])
def mul(x,y):return (x[0]*y[0]+3*x[1]*y[1],x[0]*y[1]+x[1]*y[0])
def mm(a,b):return [[add(mul(a[i][0],b[0][j]),mul(a[i][1],b[1][j])) for j in range(2)] for i in range(2)]
def adj(a):return [list(x) for x in zip(*a)]
def scale(c,a):return [[mul(c,x) for x in row] for row in a]
e=[[z(F(3,4)),z(0,F(1,4))],[z(0,F(1,4)),z(F(1,4))]]
q=[[z(F(1,4)),z(0,F(1,4))],[z(0,F(1,4)),z(F(3,4))]]
hroot=[[z(0,F(1,3)),z()],[z(),z(0,1)]]
v=mm(hroot,e)
assert mm(e,e)==e and mm(q,q)==q and mm(mm(hroot,e),hroot)==q
assert mm(adj(v),v)==e and mm(v,adj(v))==q
for i in range(2):
 p=[[z(),z()],[z(),z()]];p[i][i]=z(1)
 assert mm(mm(e,p),e)==scale(z([F(3,4),F(1,4)][i]),e)
 assert mm(mm(q,p),q)==scale(z([F(1,4),F(3,4)][i]),q)
assert [F(3,4)*F(3,4),F(1,4)*F(1,4)]==[F(9,16),F(1,16)]
assert [F(1,4)*F(3,4),F(3,4)*F(1,4)]==[F(3,16),F(3,16)]
assert F(16,3)*F(3,16)==1
if not R.name=='figures':(R/'figure-arithmetic.json').write_text(json.dumps(dict(PG_original=[str(w) for w in groups[0][2]],PG_opposite=[str(w) for w in groups[1][2]],all_six_permutations_incompatible=True,bar_height_scale=400,unit='minimal projection trace'),indent=2)+'\n',encoding='utf-8')
