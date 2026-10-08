"""Exact finite checks; these supplement, and do not replace, the proofs. CC0-1.0."""
from pathlib import Path
import hashlib,json
import sympy as s

ROOT=Path(__file__).resolve().parent
t,x=s.symbols("t x",real=True)
I=s.I
star=lambda a:a.conjugate().T
pair=lambda a,b:(star(b)*a)[0]
zero=lambda a:all(s.simplify(v)==0 for v in a)
groups=[]
def add(name,cases,scope):
    groups.append(dict(name=name,cases=cases,scope=scope,passed=True))

# Matrix square series and exact ordered derivatives.
c=[s.Integer(1)]+[s.binomial(s.Rational(1,2),n) for n in range(1,13)]
f=sum(c[n]*t**n for n in range(13))
assert s.Poly(s.expand(f*f-1-t),t).terms()[-1][0][0]>=13
k=s.Matrix([[t,I],[-I,-t]])
assert zero(k*k-(1+t*t)*s.eye(2))
assert not zero(k*k.diff(t)-k.diff(t)*k)
for n in range(1,8):
    ordered=sum((k**j*k.diff(t)*k**(n-1-j) for j in range(n)),s.zeros(2))
    assert zero(s.diff(k**n,t)-ordered)
add("Positive matrix square and ordered derivatives",8,"Exact series coefficients through degree12 and seven ordered derivative identities.")

# Exact scalar completion tensored with the same positive matrix.
cases=0
for r in [s.Rational(-1),s.Rational(0),s.Rational(1,2),s.Rational(1)]:
    y=(2+s.sqrt(4-r))/2
    b0=s.sqrt(y);b1=-1/(2*b0);g=1/(4*y)
    assert s.simplify(-2+t+(b0+t*b1)**2-g*(t*t-r))==0
    for v in [-1,0,1]:
        H=8*s.eye(2)+2*k.subs(t,v)
        assert zero((-2+b0*b0+g*r)*H)
        assert zero((s.Rational(1,2)+b0*b1)*H)
        assert zero((b1*b1-g)*H)
        assert all(ev>0 for ev in H.eigenvals())
        cases+=1
add("Tensor-weighted characteristic completion",cases,"Four root parameters, including the negative-r side, and three positive matrix weights.")

# The counterexample genuinely has nonpositive polynomial and a positive block value.
A0=-s.diag(1,0);A2=-s.diag(0,1);A1=s.Matrix([[0,1],[1,0]])
v=s.Matrix([1,-t])
assert zero(A0+t*A1+t*t*A2+v*star(v))
block=A0.row_join(A1/2).col_join((A1/2).row_join(A2))
w=s.Matrix([0,1,1,0])
assert pair(block*w,w)==1
assert s.Rational(1,2) in block.eigenvals()
add("Polynomial versus block-form obstruction",1,"Exact all-real polynomial factorization and the positive block witness.")

# Complete cancellation of Ra and Za, retaining the lower Hermitian part.
cases=0
A=s.Matrix([[1+x,I],[-I,2-x]])
C=s.Matrix([[2,1+I*x],[1-I*x,-1]])
B=C-I*A.diff(x)/2
Rh=s.Matrix([[3+x,I],[-I,1-x]])
Ra=s.Matrix([[1,2-I],[2+I,-1]])
J=(A*Rh-Rh*A)/2
for n in [1,2,3,4]:
    Zh=s.Matrix([[n,I],[-I,-n]])
    Za=s.Matrix([[2*n,1-I],[1+I,-n]])
    Z=Zh+I*Za
    H=8*s.eye(2)+2*(Ra+Za)
    E10=B.diff(x)+I*J-A*Ra
    E00=(A*Rh.diff(x)+Rh.diff(x)*A)/2+I*(C*Rh-Rh*C)-(star(B)*Ra+Ra*B)
    Z10=-I*A*Z
    Z00=(star(B)*Z-star(Z)*B)/I
    D10=A*H/2
    D00=(star(B)*H+H*B)/2
    expected10=B.diff(x)+I*J+4*A+I*A*Zh
    expected00=(A*Rh.diff(x)+Rh.diff(x)*A)/2+I*(C*Rh-Rh*C)+4*(star(B)+B)-(star(B)*Zh-Zh*B)/I
    assert zero(E10-Z10+D10-expected10)
    assert zero(E00-Z00+D00-expected00)
    cases+=1
add("Exact matrix damping cancellation",cases,"Noncommuting finite tangential model; all Ra and Za terms cancel in both cross and diagonal entries.")

# Expand the full inhomogeneous Robin boundary form.
cases=0
for n in range(1,7):
    T=s.Matrix([[1,I],[0,n]])
    A=-star(T)*T
    B=s.Matrix([[I,n],[1-I,2]])
    S0=s.Matrix([[2,I],[-I,-1]])
    K=s.Matrix([[I,1],[n,-2]])
    b0=s.Matrix([1+I,n]);beta=s.Matrix([2,I*n])
    b1=beta-K*b0
    direct=pair(A*b1,b1)+2*s.re(pair(B*b0,b1))+pair(S0*b0,b0)
    Rb=star(K)*A*K-star(K)*B-star(B)*K+S0
    expanded=pair(Rb*b0,b0)+pair(A*beta,beta)+2*s.re(pair((B-A*K)*b0,beta))
    assert s.simplify(direct-expanded)==0
    assert s.simplify(pair(A*beta,beta)+pair(T*beta,T*beta))==0
    cases+=1
add("Exact Robin defect expansion",cases,"Arbitrary complex vectors and noncommuting matrices, with the negative defect square retained.")

# Regularizer logarithmic derivative, conjugation sign and finite bound samples.
eta,eps,order=s.symbols("eta epsilon order",real=True,positive=True)
a=(1+eta*eta)**(order/2)/(1+eps*eps*eta*eta)
b=order*eta/(1+eta*eta)-2*eps*eps*eta/(1+eps*eps*eta*eta)
assert s.simplify(s.diff(a,eta)/a-b)==0
e=-eta*eta*b
cases=0
for sv in [-2,0,3]:
    for ev in [s.Rational(1,8),s.Rational(1,2),s.Integer(1)]:
        for nv in [s.Rational(1,4),s.Integer(1),s.Integer(4),s.Integer(16)]:
            val=e.subs({order:sv,eps:ev,eta:nv})
            assert s.simplify((abs(sv)+2)**2*(1+nv*nv)-val*val)>=0
            cases+=1
add("Regularizer sign and uniform leading bound",cases,"Exact logarithmic derivative and36 rational samples; the all-derivative proof is in D6.")

source=ROOT/"uniform-matrix-damping-and-robin-defects.md"
result={"passed":True,"groups":groups,"total_cases":sum(g["cases"] for g in groups),
        "source_sha256":hashlib.sha256(source.read_bytes()).hexdigest(),
        "script_sha256":hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        "finite_checks_do_not_replace_proofs":True}
(ROOT/"model-check.json").write_text(json.dumps(result,indent=2)+"\n",encoding="utf-8")
print(json.dumps({"groups":len(groups),"cases":result["total_cases"],"passed":True}))
