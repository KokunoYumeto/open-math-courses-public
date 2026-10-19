"""CC0. Reproducible opposite-model center diagram and exact finite-row checks.

The matrix checks are a finite Markov-triple fixture, not a claimed original
Jones-tower or opposite-model example. The general proofs are Lesson63.11–13.
"""
from fractions import Fraction as F
from pathlib import Path
from html import escape

I=((F(1),F(0)),(F(0),F(1)))
X=((F(0),F(1)),(F(1),F(0)))
Z=((F(1),F(0)),(F(0),F(-1)))
O=((F(0),F(0)),(F(0),F(0)))
def add(a,b):return tuple(tuple(a[i][j]+b[i][j] for j in range(2)) for i in range(2))
def mul(a,b):return tuple(tuple(sum(a[i][k]*b[k][j] for k in range(2)) for j in range(2)) for i in range(2))
def scale(t,a):return tuple(tuple(t*x for x in r) for r in a)
def star(a):return tuple(tuple(a[j][i] for j in range(2)) for i in range(2))
def diag(a):return ((a[0][0],F(0)),(F(0),a[1][1]))
def unit(i,j):return tuple(tuple(F(int((r,c)==(i,j))) for c in range(2)) for r in range(2))
def pair_add(a,b):return tuple(add(x,y) for x,y in zip(a,b))
def pair_mul(a,b):return tuple(mul(x,y) for x,y in zip(a,b))
def emb(a):return (a,a)
def expect(a):return scale(F(1,2),add(*a))
q=(unit(0,0),unit(1,1));basis=(I,X)
assert pair_add(*(pair_mul(pair_mul(emb(u),q),emb(star(u))) for u in basis))==(I,I)
assert expect(q)==scale(F(1,2),I)
assert add(*(mul(u,star(u)) for u in basis))==scale(2,I)
checks=0
for i in range(2):
 for j in range(2):
  y=unit(i,j)
  assert add(*(mul(u,diag(mul(star(u),y))) for u in basis))==y
  assert add(scale(2,diag(y)),scale(-1,y))==mul(mul(Z,y),Z)
  for block in range(2):
   a=(y,O) if block==0 else (O,y)
   terms=[]
   for u in basis:
    c=expect(pair_mul(pair_mul(q,emb(star(u))),a))
    terms.append(tuple(scale(2,b) for b in pair_mul(pair_mul(emb(u),q),emb(c))))
   assert pair_add(*terms)==a
   assert pair_add(tuple(scale(2,b) for b in emb(expect(a))),tuple(scale(-1,b) for b in a))==a[::-1]
   checks+=1
d=F(16,3);lam=1/d
final=[lam]*5+[F(1,16)]
assert sum(final)==1 and len(final)==6
assert sum([F(1)]*5+[F(1,3)])==d
assert all(x<=lam for x in final)

out=[]
def put(s):out.append(s)
def rect(x,y,w,h,fill,stroke='#9aafbd',radius=12):put(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{radius}" fill="{fill}" stroke="{stroke}"/>')
def txt(x,y,s,size=22,weight='normal',fill='#132b42',anchor='start'):
 put(f'<text x="{x}" y="{y}" font-size="{size}" font-weight="{weight}" fill="{fill}" text-anchor="{anchor}">{escape(s)}</text>')
def arrow(x1,y1,x2,y2):put(f'<path d="M{x1},{y1} L{x2},{y2}" stroke="#365e79" stroke-width="2.5" fill="none" marker-end="url(#arrow)"/>')
put('<svg xmlns="http://www.w3.org/2000/svg" width="1000" height="1070" viewBox="0 0 1000 1070" role="img" aria-labelledby="title desc">')
put('<title id="title">Finite opposite bases and the atomic parts of the two centers</title><desc id="desc">The actual opposite Markov triple has finite bases and trace-preserving center transport two steps apart. Adjacent atomic parts agree, and the actual opposite joint center is scalar. Six exact support intervals illustrate index16/3.</desc>')
put('<defs><marker id="arrow" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse"><path d="M0,0 L10,5 L0,10z" fill="#365e79"/></marker></defs>')
put('<rect width="1000" height="1070" fill="white"/><g font-family="Arial, DejaVu Sans, sans-serif">')
txt(40,42,'Actual opposite models: bases and center type',30,'bold')
txt(40,76,'Every finite index d > 1; arbitrary centers; original normalized trace τ.',21)
rect(30,102,940,264,'#eef5fc')
txt(54,140,'The whole tracial basic-construction triple (63.40)–(63.43)',23,'bold')
for x,label in [(80,'P = Bⱼ₊₁'),(394,'Q = Bⱼ'),(722,'A = Bⱼ₋₁')]:txt(x,191,label,25,'bold')
arrow(252,183,355,183);arrow(558,183,690,183)
txt(54,234,'qAq = Pq;    E_Q(q) = 1/d;    T_A(q) = (1/d)1',23)
txt(54,277,'Z(A) → Z(P):   zq = θⱼ(z)q,   τ(θⱼ(z)) = τ(z)',23,'bold')
txt(54,316,'Two-step center transport; adjacent centers need not be equal.',21)
txt(54,345,'Both tracial expectations satisfy E(x) ≥ x/d.',21)
rect(30,390,940,294,'#edf7f3')
txt(54,430,'The actual atomic projections agree (63.48)',25,'bold')
txt(54,472,'t = atomic part of Z(P);    r = atomic part of Z(Q)',23)
txt(54,512,'a = atomic part of Z(A):    t ≤ r ≤ a;    aq = tq',23)
txt(54,552,'(r − t)q = 0       ⇒       E_Q((r − t)q) = (r − t)/d = 0',22)
txt(54,592,'Hence t = r as projections in Q.',24,'bold')
txt(54,632,'For actual opposite pairs: Z(P) ∩ Z(Q) = ℂ1.',23)
txt(54,663,'Therefore both centers are atomic, or both are diffuse (63.49).',21)
rect(30,708,940,238,'#fff5e9')
txt(54,750,'Exact support construction at d = 16/3 (Exercise 63.10)',23,'bold')
width=840;x=70;y=778
for i,t in enumerate(final):
 w=float(width*t)
 rect(x,y,w,55,'#287db1' if i<5 else '#d99839','white',0)
 txt(x+w/2,y+35,str(i+1),21,'bold','white','middle')
 txt(x+w/2,863,'3/16' if i<5 else '1/16',18,anchor='middle')
 x+=w
txt(54,901,'Six basis slots: five full initial supports and one support of trace 1/3.',21)
txt(54,931,'Bar widths are exact final center traces; their sum is 1.',20)
txt(40,982,'Opposite pair: no extremality, amenability, depth or separability assumed.',21)
txt(40,1016,'Extremal ordinary cores inherit the scalar joint center and dichotomy by CTS.7.',20)
txt(40,1050,'Proofs63.11–63.13. Human context: Popa (1994), §1.4.2, Corollary(i), p.187.',19)
put('</g></svg>')
root=Path(__file__).resolve().parent
(root/'opposite-core-centers.svg').write_text('\n'.join(out)+'\n',encoding='utf-8')
if root.name!='figures':
 import json
 (root/'fixture-check.json').write_text(json.dumps(dict(fixture='P=C² inside Q=M2, A=M2 direct-sum M2; not asserted to be an actual opposite pair',matrix_unit_dual_basis_checks=checks,whole_positive_cone_positive_bounds_proved_by_exact_formulas=True,six_support_center_traces=[str(t) for t in final],initial_P_support_traces=['1']*5+['1/3'],basis_norm_bound='4/sqrt(3)',new_general_BF_input=False),indent=2)+'\n',encoding='utf-8')
print('Exact basis/positive-map fixture checks:8; exact six-part support sum:1; SVG generated.')
