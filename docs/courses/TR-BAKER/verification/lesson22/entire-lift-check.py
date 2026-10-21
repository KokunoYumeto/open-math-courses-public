"""Exact mechanism checks for 22.58--64; the written proof is authoritative."""
from pathlib import Path
import json,hashlib
import sympy as sp
from fractions import Fraction as F
ROOT=Path(__file__).resolve().parent
checks=[]
def check(name,value):
    assert value,name
    checks.append(name)

x,y=sp.symbols("x y",real=True)
i=sp.I
def dz(f):return (sp.diff(f,x)-i*sp.diff(f,y))/2
def db(f):return (sp.diff(f,x)+i*sp.diff(f,y))/2

# Ga in P1: actual unit radial frame and its connection.
r2=x*x+y*y
Ax=i*y/(1+r2); Ay=-i*x/(1+r2)
curvature=sp.simplify(sp.diff(Ay,x)-sp.diff(Ax,y))
check("FS curvature in a real unit frame",curvature==-2*i/(1+r2)**2)
check("radial gauge",sp.simplify(x*Ax+y*Ay)==0)
abar=sp.simplify((Ax+i*Ay)/2)
g=sp.log(1+r2)/2
check("dbar primitive of the unit-frame connection",sp.simplify(db(g)-abar)==0)
check("frame normalization equality",sp.simplify(sp.exp(2*g)-(1+r2))==0)
t,R=sp.symbols("t R",positive=True)
integral=sp.integrate(2*t/(1+t*t*R)**2,(t,0,1))
check("radial curvature integration",sp.simplify(integral-1/(1+R))==0)

# Hessian and its exact eigenvalue lower bound, tested by rational matrices.
for n in (1,2,3):
    for k in range(1,9):
        vec=sp.Matrix([sp.Rational(j-k,j+2) for j in range(n)])
        norm=(vec.T*vec)[0]
        N=n+4
        hess=N*((1+norm)*sp.eye(n)-vec*vec.T)/(1+norm)**2
        low=sp.Rational(N)/(1+norm)**2
        residual=sp.simplify(hess-low*sp.eye(n))
        for size in range(1,n+1):
            import itertools
            for idx in itertools.combinations(range(n),size):
                check(f"Hessian principal minor n={n},k={k},idx={idx}",
                      residual.extract(idx,idx).det()>=0)
        check(f"Hessian radial eigenvalue n={n},k={k}",
              hess*vec==low*vec)
for n in range(1,9):
    for s in range(4):
        N=n+s+3
        check(f"weighted integrability n={n},s={s}",2*s+4-2*N+2*n-1==-3)

# Fundamental-solution radial Laplacian and unit flux factors.
rr=sp.symbols("r",positive=True)
for dim in (2,4,6,8):
    radial=sp.log(rr) if dim==2 else rr**(2-dim)/(2-dim)
    check(f"harmonic away from origin dimension={dim}",
          sp.simplify(sp.diff(radial,rr,2)+(dim-1)/rr*sp.diff(radial,rr))==0)
    check(f"unit flux after sphere-area normalization dimension={dim}",
          sp.simplify(rr**(dim-1)*sp.diff(radial,rr))==1)

# Addition-law base points: multiplication by a vanishing common factor
# only increases the order and does not destroy propagation of initial jets.
z,v=sp.symbols("z v")
for T in range(1,9):
    for center in (0,2):
        standard=(z+v-center)**T
        degenerate=(z-center)**T*standard
        for order in range(T+1):
            js=sp.diff(standard,v,order).subs(v,0)
            jb=sp.diff(degenerate,v,order).subs(v,0)
            check(f"valid chart jet T={T},s={center},t={order}",
                  sp.expand(js-sp.factorial(T)/sp.factorial(T-order)*(z-center)**(T-order))==0)
            check(f"base-point chart jet T={T},s={center},t={order}",
                  sp.expand(jb-(z-center)**T*js)==0)

# At a valid tuple, multiplication by a unit gives an invertible triangular
# system of jets. At an invalid tuple this converse cannot be used.
for D in range(1,5):
    for T in range(1,6):
        c=sp.symbols("c:"+str(T))
        h=sum(c[j]*v**j for j in range(T))
        rows=[sp.diff((2+v)**D*h,v,t).subs(v,0) for t in range(T)]
        matrix=sp.Matrix(rows).jacobian(c)
        expected=2**(D*T)*sp.prod(sp.factorial(t) for t in range(T))
        check(f"unit jet inversion D={D},T={T}",matrix.det()==expected)
check("zero scalar invalidates converse",(v*1).subs(v,0)==0 and sp.Integer(1).subs(v,0)!=0)

# Count and contradiction ratios use the exact same auxiliary parameters.
for n in range(2,6):
    for m in (1,3):
        for c in (1,4):
            b=8;S=b**(2*n+1);k=max(5,2*(n+4));q=3
            A=2*n*m*q*S**(n*k);D=A//S**k;T=A-n;M=T//2
            count=sp.binomial(D+n,n)
            rows=m*q*sp.binomial(T+n-1,n-1)
            check(f"enough independent monomials n={n},m={m},c={c}",count>=2*rows)
            check(f"propagated order n={n},m={m},c={c}",8*(M+1)>=A)
            ratio=F(b*q,2*c)*F(A,8)**(n-1)/D**n
            check(f"multiplicity contradiction ratio n={n},m={m},c={c}",
                  ratio==F(b,4*c*n*m*8**(n-1)))

result={"status":"passed","checks":len(checks),"scope":"Mechanisms in22.58--64",
 "families":["Polynomial-weight Hessian and integrability","Radial unitary connection and frame normalization on Ga","Laplace fundamental-solution flux","Addition-chart zeros and valid-chart jet inversion","Auxiliary count and dyadic multiplicity ratio"],
 "limit":"Exact examples supplement the written arguments; they do not independently prove the general AST."}
(ROOT/"entire-lift-check.json").write_text(json.dumps(result,indent=2)+"\n",encoding="utf-8")
print(json.dumps(result,indent=2))
