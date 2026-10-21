"""Exact examples for multidegrees, subgroup jets, and period distances."""
from collections import Counter
from datetime import datetime, timezone
from itertools import product
from math import comb, factorial
from pathlib import Path
import json
import sympy as s

checks = Counter()


def check(test, family):
    assert bool(test), (family, test)
    checks[family] += 1


x,y,A,B=s.symbols("x y A B")
base=[s.Integer(1),x,y]


def reduce_curve(p):
    return s.rem(s.Poly(s.expand(p),y),
                 s.Poly(y*y-x**3-A*x-B,y)).as_expr().expand()


def derivation(p):
    return reduce_curve(s.diff(p,x)*2*y+s.diff(p,y)*(3*x*x+A))


images=[]
for a,b,c in product(range(2),base,base):
    images.append((reduce_curve(b*c) if a==0 else s.Integer(0),
                   reduce_curve(derivation(b)*c) if a==0
                   else reduce_curve(b*c)))
keys=sorted(set((j,mon) for v in images for j in range(2)
                for mon,coefficient in s.Poly(v[j],x,y).terms()))
matrix=s.Matrix([[s.Poly(v[j],x,y).coeff_monomial(mon) for v in images]
                 for j,mon in keys])
check(matrix[[i for i,k in enumerate(keys) if k[0]==0],:].rank()==6,
      "diagonal_restriction_rank")
check(matrix.rank()==12,"diagonal_first_normal_jet_rank")
for av,bv in [(-1,0),(0,1),(-2,3),(2,-1)]:
    check(4*av**3+27*bv**2 != 0,"nonsingular_examples")
    check(matrix.subs({A:av,B:bv}).rank()==12,
          "specialized_first_normal_jet_rank")

for degree in range(1,21):
    normal_monomials=[(i,j,degree-i-j)
                      for i in range(min(2,degree)+1)
                      for j in range(degree-i+1)]
    check(len(normal_monomials)==3*degree,"plane_cubic_section_basis")


def indices(q,n):
    if q==0:
        yield ()
    else:
        for a in range(n+1):
            for rest in indices(q-1,n-a):
                yield (a,)+rest


for q in range(1,6):
    for n in range(9):
        all_indices=list(indices(q,n))
        check(len(all_indices)==comb(n+q,q),"normal_jet_count")
        for cap in range(1,n+3):
            count=sum(a[-1]<cap for a in all_indices)
            check(count<=cap*comb(n+q-1,q-1),
                  "truncated_normal_jet_count")

# Product square lattice, graph B={(z,(m+ni)z)}.
# The Gram determinant computes volume independently of the projection formula.
for m,n in product(range(-2,3),repeat=2):
    norm=m*m+n*n
    basis=s.Matrix([[1,0],[0,1],[m,-n],[n,m]])
    gram=basis.T*basis
    covol=1+norm
    check(gram.det()==covol**2,"graph_lattice_covolume")
    projection=basis*gram.inv()*basis.T
    for coords in product(range(-1,2),repeat=4):
        omega=s.Matrix(coords)
        perp=(s.eye(4)-projection)*omega
        distance_squared=(perp.T*perp)[0]
        if distance_squared:
            check(distance_squared>=s.Rational(1,covol*covol),
                  "period_distance_exterior_bound")

# With g=2 and W={z0=z1-z2}, the only possible dimensions are 0 and 1;
# the one-dimensional subgroup has the diagonal tangent space.
# Use exact rational weights, for both Q_B=1 and Q_B=S+1.
for C in [216,222,300]:
    Q0=4*C*C
    S=Q0-1
    weight=C**3*Q0
    U=C*C*weight
    for QB in [1,Q0]:
        AG0=s.Rational(U*U*Q0,C*54*weight**3)
        AGB=s.Rational(U*QB*6*weight,C*54*weight**3)
        scale=s.sqrt(AGB)
        check(scale**3<=AG0,"extremal_minimum")
        t=s.simplify(scale*weight)
        D=int(s.floor(t))
        check(t>=s.Rational(C,54) and D>=t/2,
              "positive_integer_parts")
        HG=54*t**3
        HB=6*t
        check(U*QB*HB==C*HG,"extremal_equality")
        check(U*U*Q0>=C*HG,"other_subgroup_inequality")
        T=int(U)
        N=6*T
        HD=54*D**3
        bound=s.Rational(648,C)*HD
        if QB==Q0:
            S0=Q0//(C*C)
            rank_bound=S0*(N+1)*6*D
            check(rank_bound<=bound,"nonperiodic_rank_bound")
        else:
            T0=U//(C*C)
            rank_bound=6*QB*T0*6*D
            check(rank_bound<=bound,"periodic_rank_bound")
        check(6<=54*U**2,"subgroup_degree_bound")

# Preserve a degree bound while the additive denominator R0 varies.
# Unequal elliptic weights make the refined estimate 9 for a subgroup
# whose actual degree is 6; the total scale U grows with R0.
C=216
R1,R2=C**3,2*C**3
ratio=6*C**6
scale=s.Rational(1,6*C*C)
for R0 in [C*C,C**3,2*C**4]:
    U=ratio*R0
    weights=[s.Rational(U,R0),s.Rational(U,R1),s.Rational(U,R2)]
    t=[scale*d for d in weights]
    HG=54*s.prod(t)
    HB=3*(t[1]+t[2])
    check(U*HB==C*HG,"anisotropic_extremal_equality")
    refined=s.Rational(C*54)*scale**2*s.Rational(U,R0)*s.Rational(
        max(R1,R2),R1*R2)
    check(refined==9 and 6<=refined,"uniform_subgroup_degree_bound")

result={"utc":datetime.now(timezone.utc).isoformat(),"state":"passed",
        "checks":dict(checks),"total":sum(checks.values()),
        "limits":"Finite exact computations verify diagonal jet ranks, cubic section counts, normal monomial counts, graph-lattice volumes and period distances, and extremal-weight/rank inequalities in two sampling patterns. General proofs, rather than these examples, establish the stated lemmas. The full quantitative logarithm bound is still unfinished."}
Path(__file__).with_suffix(".json").write_text(
    json.dumps(result,indent=2)+"\n",encoding="utf-8")
print(json.dumps(result))
