"""Exact calculations for a Hesse-pencil proof; not a completeness claim."""
from pathlib import Path
import sympy as s,json,itertools,collections
b=Path(__file__).resolve().parent
triples=[(i,j,3-i-j) for i in range(3,-1,-1) for j in range(3-i,-1,-1)]
coeff=s.symbols('c0:10'); x,y,z=s.symbols('x y z');variables=[x,y,z]
f=sum(s.factorial(3)/s.prod(s.factorial(v) for v in e)*c*s.prod(v**q for v,q in zip(variables,e)) for c,e in zip(coeff,triples))
letters=s.symbols('u0:3 v0:3 w0:3 r0:3')
rows=[letters[i:i+3] for i in range(0,12,3)]
bracket=lambda ids:s.det(s.Matrix([rows[i] for i in ids]))
symbolic=s.Poly(s.expand(bracket([0,1,2])*bracket([0,1,3])*bracket([0,2,3])*bracket([1,2,3])),*letters)
lookup=dict(zip(triples,coeff))
S=s.expand(sum(n*s.prod(lookup[tuple(e[i:i+3])] for i in range(0,12,3)) for e,n in symbolic.terms()))
H=s.expand(s.det(s.hessian(f,variables)))
hcoeff=[s.Poly(H,x,y,z).coeff_monomial(s.prod(v**q for v,q in zip(variables,e)))*s.prod(s.factorial(v) for v in e)/s.factorial(3) for e in triples]
T=s.expand(sum(s.diff(S,c)*hc for c,hc in zip(coeff,hcoeff)))
a,c=s.symbols('a b')
slice_values={co:(a if e in [(3,0,0),(0,3,0),(0,0,3)] else c/6 if e==(1,1,1) else 0) for co,e in zip(coeff,triples)}
S0=s.factor(S.subs(slice_values));T0=s.factor(T.subs(slice_values))
Js=s.factor(s.det(s.Matrix([[s.diff(S0,a),s.diff(S0,c)],[s.diff(T0,a),s.diff(T0,c)]])))
# At F=x^3+y^3+z^3, the six off-diagonal infinitesimal directions
# give the six mixed monomials; the diagonal directions and the pencil
# span the remaining four-dimensional space.
directions=[]
fs=f.subs(slice_values).subs({a:1,c:0})
for i in range(3):
 for j in range(3):
  if i!=j:directions.append(variables[j]*s.diff(fs,variables[i]))
directions.extend([x*s.diff(fs,x)-z*s.diff(fs,z),y*s.diff(fs,y)-z*s.diff(fs,z),x**3+y**3+z**3,x*y*z])
tangent=s.Matrix([[s.Poly(g,x,y,z).coeff_monomial(s.prod(v**q for v,q in zip(variables,e))) for g in directions] for e in triples])
result={'coefficient_order':triples,'S':str(S),'S_terms':len(s.Poly(S,*coeff).terms()),'T':str(T),'T_terms':len(s.Poly(T,*coeff).terms()),'Hesse_S':str(S0),'Hesse_T':str(T0),'Hesse_Jacobian':str(Js),'dominance_tangent_determinant':str(tangent.det()),'Hesse_matrix_D_squared':-27}
(b/'aronhold-computations.json').write_bytes((json.dumps(result,indent=2)+'\n').encode('utf8'))
print(json.dumps({k:v for k,v in result.items() if k not in ['S','T']},ensure_ascii=False))
