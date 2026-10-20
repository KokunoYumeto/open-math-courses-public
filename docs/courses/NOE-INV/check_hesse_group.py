"""Exact order, character table and Molien sum in Q[zeta]/(zeta^2+zeta+1)."""
from fractions import Fraction as Q
from pathlib import Path
from collections import Counter
import sympy as s,json
b=Path(__file__).resolve().parent
class K(tuple):
 def __new__(cls,a=0,c=0):return tuple.__new__(cls,(Q(a),Q(c)))
 def __add__(v,w):w=w if isinstance(w,K) else K(w);return K(v[0]+w[0],v[1]+w[1])
 __radd__=__add__
 def __neg__(v):return K(-v[0],-v[1])
 def __sub__(v,w):return v+-w
 def __mul__(v,w):w=w if isinstance(w,K) else K(w);return K(v[0]*w[0]-v[1]*w[1],v[0]*w[1]+v[1]*w[0]-v[1]*w[1])
 __rmul__=__mul__
 def expression(v):return s.Rational(v[0].numerator,v[0].denominator)+s.Rational(v[1].numerator,v[1].denominator)*w
def mm(a,c):return tuple(sum(a[2*i+k]*c[2*k+j] for k in range(2)) for i in range(2) for j in range(2))
I=(K(1),K(),K(),K(1));A=(K(0,1),K(),K(),K(1));B=(K(Q(1,3),Q(2,3)),K(Q(1,9),Q(2,9)),K(2,4),K(-Q(1,3),-Q(2,3)))
group={I};queue=[I]
while queue:
 g=queue.pop()
 for h in [A,B]:
  new=mm(g,h)
  if new not in group:group.add(new);queue.append(new)
 assert len(group)<=24,'Unexpected pencil group size'
assert len(group)==24
Ai=mm(A,A);C=mm(mm(A,B),Ai);D=mm(mm(Ai,B),A)
minusI=tuple(-e for e in I)
assert mm(B,B)==mm(C,C)==mm(D,D)==minusI
products={name:[str(e) for e in mm(g,h)] for name,g,h in [('BC',B,C),('CB',C,B),('CD',C,D),('DB',D,B)]}
assert mm(B,C)==D and mm(C,B)==tuple(-e for e in D)
table=Counter((g[0]+g[3],g[0]*g[3]-g[1]*g[2]) for g in group)
w,t,a,c=s.symbols('w t a b')
rows=[{'trace':str(tr.expression()),'determinant':str(det.expression()),'multiplicity':num} for (tr,det),num in table.items()]
molien=sum(num/(1-tr.expression()*t+det.expression()*t*t) for (tr,det),num in table.items())/24
num,den=s.fraction(s.together(molien-1/((1-t**4)*(1-t**6))))
assert s.rem(s.Poly(num,w),s.Poly(w*w+w+1,w)).is_zero
P=c**4-216*a**3*c;R=c**6+540*a**3*c**3-5832*a**6
for label,m in [('A',A),('B',B)]:
 aa=m[0].expression()*a+m[1].expression()*c;cc=m[2].expression()*a+m[3].expression()*c
 for polynomial in [P,R]:
  remainder=s.rem(s.Poly(s.expand(polynomial.subs({a:aa,c:cc},simultaneous=True)-polynomial),w),s.Poly(w*w+w+1,w))
  assert remainder.is_zero
result={'group_order':len(group),'generators_A':[str(e.expression()) for e in A],'generators_B':[str(e.expression()) for e in B],'quaternion_conjugates_C':[str(e.expression()) for e in C],'quaternion_conjugates_D':[str(e.expression()) for e in D],'quaternion_relations':'B^2=C^2=D^2=-I, BC=D=-CB, A cycles B,C,D','trace_determinant_table':rows,'Molien_series':'1/((1-t^4)*(1-t^6))','pencil_invariants':['b^4-216*a^3*b','b^6+540*a^3*b^3-5832*a^6'],'checks':'All group closure, quaternion relations, both invariance identities, and exact rational Molien identity passed.'}
(b/'hesse-group-certificates.json').write_bytes((json.dumps(result,indent=2)+'\n').encode('utf8'))
print(json.dumps(result,ensure_ascii=False))
