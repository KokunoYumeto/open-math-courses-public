"""Exact finite checks supporting, not replacing, the proofs in 22.29--34."""
from collections import Counter
from datetime import datetime, timezone
from fractions import Fraction
from itertools import product
from math import comb, factorial
from pathlib import Path
import hashlib
import json
import sympy as sp

ROOT = Path(__file__).resolve().parent
counts = Counter()
X = sp.symbols('X0:4')
u, v, x, y, s = sp.symbols('u v x y s')

def homogeneous_derivative(q, direction):
    if direction == 0:
        return sp.expand(X[0]**2*sp.diff(q, X[1]) + X[0]*X[2]*sp.diff(q, X[3]))
    return sp.expand(X[0]*X[2]*sp.diff(q, X[2]) + X[0]*X[3]*sp.diff(q, X[3]))

charts = [
    ((1,u,v,u*v), (lambda q: sp.diff(q,u), lambda q: v*sp.diff(q,v))),
    ((u,1,u*v,v), (lambda q: -u*u*sp.diff(q,u), lambda q: v*sp.diff(q,v))),
    ((u,u*v,1,v), (lambda q: sp.diff(q,v), lambda q: -u*sp.diff(q,u))),
    ((u*v,u,v,1), (lambda q: -v*v*sp.diff(q,v), lambda q: -u*sp.diff(q,u))),
]
for degree in range(1,4):
    for exponents in product(range(degree+1), repeat=4):
        if sum(exponents) != degree:
            continue
        q0 = sp.prod(z**e for z,e in zip(X,exponents))
        for length in range(1,4):
            for word in product(range(2),repeat=length):
                q, e = q0, degree
                for direction in word[:-1]:
                    q = homogeneous_derivative(q,direction)
                    e += 1
                direction=word[-1]
                out=homogeneous_derivative(q,direction)
                for coordinates, derivations in charts:
                    substitution=dict(zip(X,coordinates))
                    xi=sp.sympify(coordinates[0])
                    local=sp.expand(q.subs(substitution, simultaneous=True))
                    derivative=derivations[direction]
                    rhs=xi*derivative(local)-e*derivative(xi)*local
                    lhs=out.subs(substitution,simultaneous=True)
                    assert sp.expand(lhs-rhs)==0
                    counts['homogeneous_change_of_chart']+=1
                affine=q0.subs(dict(zip(X,(1,x,y,x*y))),simultaneous=True)
                for i in word:
                    affine=sp.diff(affine,x) if i==0 else y*sp.diff(affine,y)
                assert sp.expand(out.subs(dict(zip(X,(1,x,y,x*y))),simultaneous=True)-affine)==0
                counts['exact_affine_derivative_words']+=1

for n,delta,a in product(range(2,7),range(1,4),range(2,5)):
    cs=[1]; Bs=[]; Ks=[]
    for r in range(1,n):
        B=delta
        for c in cs:B*=c
        K=factorial(r)*B+1
        Bs.append(B); Ks.append(K); cs.append(cs[-1]+(a-1)*K)
        for D in range(1,6):
            assert comb(K*D+r,r)>B*D**r
            counts['strict_component_escape']+=1
    Bn=delta
    for c in cs:Bn*=c
    L=sum(Ks); C=2**(n-1)*factorial(n-1)*Bn
    for D,extra in product(range(1,6),range(4)):
        T=2*L*D+extra; T0=T-L*D
        assert T0>=1 and 2*T0>=T
        assert comb(T0+n-2,n-1)*2**(n-1)*factorial(n-1)>=T**(n-1)
        counts['point_length_and_order_budget']+=1
    for m in range(1,4):
        ell=4*n*m*8**(n-1)*C+1; S=ell**(2*n+1); k=5
        assert S**k>=16*L
        for q in [1,S+1]:
            A=2*n*m*q*S**(n*k); D=A//S**k
            ratio=Fraction(ell*q,2)*Fraction(A,8)**(n-1)/D**n
            assert ratio==Fraction(ell,4*n*m*8**(n-1)) and ratio>C
            counts['extrapolation_geometric_margin']+=1

# A nonreduced family tests the generic primary length and the final point length.
# Coordinates s=y-1-x, v=y-1 give Delta=v*d_s+(v+1)*d_v.
def delta(q):return sp.expand(v*sp.diff(q,s)+(v+1)*sp.diff(q,v))
for m in range(1,6):
    q=s**m
    for t in range(m):
        assert sp.expand(q.subs(s,0))==0
        counts['primary_derivatives_absorbed']+=1
        q=delta(q)
    assert sp.expand(q.subs(s,0)-factorial(m)*v**m)==0
    counts['primary_escape_exact']+=1
    assert sp.resultant(s**m,q,s)==factorial(m)**m*v**(m*m)
    counts['nonreduced_intersection_resultant']+=1
    basis=sp.groebner([s**m,q],s,v,order='lex')
    leading=[p.LM(order=basis.order).exponents for p in basis.polys]
    standard=[(i,j) for i in range(m*m+1) for j in range(m*m+1)
              if not any(i>=a and j>=b for a,b in leading)]
    assert len(standard)==m*m
    counts['nonreduced_intersection_length']+=1

# Both projective points and their exact local ideals in Example 22.34.
assert set(map(str,sp.groebner([y-1-x,y-1],x,y).exprs))=={'x','y - 1'}
assert set(map(str,sp.groebner([v-u*v-u,v-u*v],u,v).exprs))=={'u','v'}
counts['simple_projective_intersections']=2
for t in range(2,30):
    assert comb(t+3,3)-comb(t+1,3)==(t+1)**2
    counts['segre_hilbert_degree']=counts.get('segre_hilbert_degree',0)+1

result={'utc':datetime.now(timezone.utc).isoformat(),'state':'passed',
        'cases':dict(counts),'total':sum(counts.values()),
        'script_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        'limits':'Exact finite algebra and parameter checks; the general theorem is established by the manuscript proof. No general AST completion assertion.'}
(ROOT/'global-multiplicity-check.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
print(json.dumps(result,indent=2))
