"""Exact addition-law, ideal-chain and multiplicity-constant examples."""
from collections import Counter
from datetime import datetime, timezone
from functools import reduce
from itertools import product
from math import factorial
from pathlib import Path
import json
import sympy as s

checks=Counter()


def check(test,family):
    assert bool(test),(family,test)
    checks[family]+=1


x,y,u,v=s.symbols("x y u v")
variables=(x,y,u,v)
left=[1,x,y,x*x,x*y,y*y]
right=[1,u,v,u*u,u*v,v*v]
basis=[s.expand(a*b) for a in left for b in right]


def curve_reduce(poly):
    poly=s.rem(s.Poly(s.expand(poly),y),
               s.Poly(y*y-x**3+2,y)).as_expr()
    return s.rem(s.Poly(s.expand(poly),v),
                 s.Poly(v*v-u**3+2,v)).as_expr().expand()


# Derive the whole bidegree(2,2) addition-law space independently by
# solving exact polynomial identities against the chord formula.
den=u-x
nx=(v-y)**2-(x+u)*den**2
ny=-y*den**3+(v-y)*(x*den**2-nx)
columns=[]
for j in range(108):
    monomial=basis[j%36]
    columns.append((
        curve_reduce(den**2*monomial) if j<36
        else curve_reduce(-nx*monomial) if j>=72 else 0,
        curve_reduce(den**3*monomial) if 36<=j<72
        else curve_reduce(-ny*monomial) if j>=72 else 0))
keys=sorted(set((i,m) for col in columns for i in range(2)
                for m,c in s.Poly(col[i],*variables).terms()))
matrix=s.Matrix([[s.Poly(col[i],*variables).coeff_monomial(m)
                  for col in columns] for i,m in keys])
kernel=matrix.nullspace()
check(len(kernel)==3,"addition_law_space_dimension")
laws=[]
for vector in kernel:
    check(matrix*vector==s.zeros(matrix.rows,1),
          "symbolic_addition_law_identity")
    laws.append([s.expand(sum(vector[36*j+k]*basis[k] for k in range(36)))
                 for j in range(3)])


def add(p,q):
    if p is None:return q
    if q is None:return p
    a,b=p;c,d=q
    if a==c and b==-d:return None
    slope=(3*a*a/(2*b)) if p==q else (d-b)/(c-a)
    e=s.cancel(slope*slope-a-c)
    return e,s.cancel(slope*(a-e)-b)


points=[None]
point=None
generator=(s.Rational(3),s.Rational(5))
for _ in range(4):
    point=add(point,generator)
    check(s.cancel(point[1]**2-point[0]**3+2)==0,
          "rational_curve_points")
    points.extend([point,(point[0],-point[1])])


def projective_basis(p):
    if p is None:return [0,0,0,0,0,1]
    a,b=p
    return [1,a,b,a*a,a*b,b*b]


for p,q in product(points,repeat=2):
    bp=projective_basis(p);bq=projective_basis(q)
    values=[a*b for a in bp for b in bq]
    result=add(p,q)
    expected=s.Matrix([0,1,0] if result is None
                      else [result[0],result[1],1])
    nonzero=0
    for vector in kernel:
        value=s.Matrix([sum(vector[36*j+k]*values[k] for k in range(36))
                        for j in range(3)])
        if value!=s.zeros(3,1):
            nonzero+=1
            check(value.cross(expected)==s.zeros(3,1),
                  "addition_law_values")
    check(nonzero>0,"addition_law_coverage")

# Compute the ideals from all translated derivatives by polynomial gcd;
# compare with the predicted roots and multiplicities, including the example.
for T,S in product(range(1,4),range(1,4)):
    P=s.prod((y-a)**(2*T+1) for a in range(2*S+1)).expand()
    for j in range(1,4):
        derivatives=[s.diff(P,y,k) for k in range((j-1)*T+1)]
        polynomials=[s.Poly(f.subs(y,y+a),y)
                     for a in range((j-1)*S+1) for f in derivatives]
        actual=reduce(s.gcd,polynomials).monic().as_expr()
        predicted=s.prod((y-a)**((3-j)*T+1)
                         for a in range((3-j)*S+1)).expand()
        check(s.expand(actual-predicted)==0,
              "translated_derivative_ideal_chain")
    check(2*T+1>=T+1,"generic_coset_multiplicity")

# Keep the strict inequalities and powers of two in the nonzero-jet proof.
for n in range(2,13):
    K=factorial(n)*3**(n-1)
    C=max(4*K,2**(2*n)*factorial(n-1))
    check(C*C>4*n*K,"hyperplane_order_threshold")
    for r in range(2,n+1):
        check(C>2**(n-1+r)*factorial(r-1),
              "extremal_multiplicity_contradiction")
    U=s.Rational(8*C*C+1,2)
    T=s.floor(U)
    Dmax=s.floor(U/(C*C))
    check(T>2*n*K*Dmax,"rounded_order_threshold")

output={
    "utc":datetime.now(timezone.utc).isoformat(),
    "state":"passed","checks":dict(checks),"total":sum(checks.values()),
    "addition_law_linear_system":{"rows":matrix.rows,"columns":matrix.cols,
                                  "kernel_dimension":len(kernel)},
    "addition_laws_affine_model_y2_x3_minus2":[[str(p) for p in law]
                                             for law in laws],
    "limits":"Finite exact computations reconstruct the three bidegree(2,2) addition laws for y^2=x^3-2, check rational pairs including the identity/doubling/inverses, compare derivative ideals with polynomial gcds, and test the strict constants. They supplement the manuscript proofs; the final quantitative logarithm bound and its applications are still unfinished."
}
Path(__file__).with_suffix(".json").write_text(
    json.dumps(output,indent=2)+"\n",encoding="utf-8")
print(json.dumps({k:v for k,v in output.items()
                  if k!="addition_laws_affine_model_y2_x3_minus2"}))
