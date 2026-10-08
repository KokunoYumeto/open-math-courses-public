"""Exact finite identities and separately labelled numerical samples. CC0-1.0."""
from pathlib import Path
import hashlib,json
import sympy as s
import numpy as np
from scipy.special import airy

ROOT=Path(__file__).resolve().parent
groups=[]
def add(name,cases,kind,scope):
    groups.append(dict(name=name,cases=cases,kind=kind,scope=scope,passed=True))
z=s.symbols("z",positive=True)
c=s.Rational(5,36)
coeff=[s.Integer(1)]
for j in range(12):
    coeff.append(s.simplify((j*(j+1)+c)*coeff[-1]/(2*s.I*(j+1))))
for N in range(1,13):
    m=sum(coeff[j]*z**(-j) for j in range(N))
    residual=s.expand(s.diff(m,z,2)+2*s.I*s.diff(m,z)+c*z**(-2)*m)
    assert s.simplify(residual*z**(N+1)-(N*(N-1)+c)*coeff[N-1])==0
    assert c/(N+1)<1
add("Volterra recurrence and weighted contraction",24,"exact",
    "Twelve formal residual identities and twelve exact weighted contraction constants.")

x=s.symbols("x",positive=True)
v=s.Function("v")
zz=s.Rational(2,3)*x**s.Rational(3,2)
y=x**s.Rational(-1,4)*v(zz)
rhs=x**s.Rational(3,4)*(s.Subs(s.diff(v(z),z,2),z,zz)+v(zz)+c*zz**(-2)*v(zz))
assert s.simplify(s.diff(y,x,2)+x*y-rhs)==0
add("Liouville change of variable",1,"exact","Full amplitude derivative, cancellation and the coefficient 5/36.")

u,w,p,q,t=s.symbols("u w p q t",real=True)
F=u+s.I*w;Fp=p+s.I*q
J=s.im(Fp*s.conjugate(F))
assert s.simplify(s.diff(J,u)*p+s.diff(J,w)*q+s.diff(J,p)*t*u+s.diff(J,q)*t*w)==0
assert s.simplify(F*s.conjugate(Fp)-Fp*s.conjugate(F)+2*s.I*J)==0
assert s.simplify(s.im(Fp/F)-J/(u*u+w*w))==0
assert s.simplify((t*F*F-Fp**2)/F**2-(t-(Fp/F)**2))==0
add("Conserved flux and quotient identities",4,"exact","Flux derivative, Wronskian sign, imaginary quotient and Riccati equation.")

gauss=[]
for j in range(5):
    moment=s.factorial2(6*j-1)/2**(3*j) if j else s.Integer(1)
    gauss.append(s.simplify((-1)**j*moment/(3**(2*j)*s.factorial(2*j))))
assert gauss[0]==1 and gauss[1]==-s.Rational(5,48)
for j in range(1,5):
    assert s.simplify(gauss[j]/gauss[j-1]+s.Rational((6*j-1)*(6*j-3)*(6*j-5),9*8*(2*j)*(2*j-1)))==0
add("Positive Gaussian coefficients",6,"exact","Leading normalization, first correction and four successive moment ratios.")

lam=s.symbols("lam",positive=True);mu=s.symbols("mu",real=True)
fx=s.Function("F");tx=lam**s.Rational(-1,3)*mu-lam**s.Rational(2,3)*x
# SymPy uses the argument as its differentiation dummy; substitute the complete second derivative.
second=s.diff(fx(tx),x,2)
atom=next(iter(second.atoms(s.Subs)))
model=second.xreplace({atom:tx*fx(tx)})
assert s.simplify(model+(x*lam**2-mu*lam)*fx(tx))==0
assert s.simplify(-s.I*s.diff(tx,x)-s.I*lam**s.Rational(2,3))==0
n,np_,b=s.symbols("n np b",nonzero=True)
K=s.Matrix([[0,b],[0,0]]);eye=s.eye(2)
inv=eye/n-K/n**2
reflection=-np_/n*eye-(n-np_)/n**2*K
assert s.simplify((n*eye+K)*inv-eye)==s.zeros(2)
assert s.simplify((n*eye+K)*reflection+np_*eye+K)==s.zeros(2)
add("Actual model and ordered Robin matching",4,"exact","Airy equation scaling, intrinsic normal sign, matrix inverse and full reflection identity.")

samples=np.linspace(-10,10,81)
ai,aip,bi,bip=airy(samples)
phi=(aip-1j*bip)/(ai-1j*bi)
flux=aip*bi-bip*ai
assert np.max(np.abs(flux+1/np.pi))<2e-13
expected=-1/(np.pi*(ai*ai+bi*bi))
assert np.allclose(phi.imag,expected,rtol=3e-12,atol=1e-18)
assert np.all(np.isfinite(phi)) and np.all(np.abs(phi)>0)
add("Real-axis quotient samples",81,"numerical",
    "SciPy samples on [-10,10] check normalization, flux, sign and finite nonzero values; global nonvanishing is proved in B3.")

tail_cases=0
for R in [5.,10.,20.]:
    ai,aip,bi,bip=airy(-R)
    F=np.sqrt(np.pi)*np.exp(1j*np.pi/4)*(ai-1j*bi)
    zz=2*R**1.5/3
    m=F*R**.25*np.exp(-1j*zz)
    assert abs((m-1-complex(coeff[1])/zz)*zz**2)<1
    phi=(aip-1j*bip)/(ai-1j*bi)
    assert abs((phi+1j*np.sqrt(R)-1/(4*R))*R**2.5)<1
    tail_cases+=2
for R in [5.,10.,20.]:
    ai,aip,bi,bip=airy(R)
    phi=(aip-1j*bip)/(ai-1j*bi)
    assert abs((phi-np.sqrt(R)+1/(4*R))*R**2.5)<1
    tail_cases+=1
add("Asymptotic normalization samples",tail_cases,"numerical",
    "Three negative amplitudes, three negative quotients and three positive quotients; samples do not establish differentiated remainders.")

source=ROOT/"zero-free-airy-quotients-and-robin-matching.md"
record=dict(passed=True,groups=groups,total_cases=sum(g["cases"] for g in groups),
    exact_cases=sum(g["cases"] for g in groups if g["kind"]=="exact"),
    numerical_cases=sum(g["cases"] for g in groups if g["kind"]=="numerical"),
    source_sha256=hashlib.sha256(source.read_bytes()).hexdigest(),
    script_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
    finite_checks_do_not_replace_proofs=True)
(ROOT/"model-check.json").write_text(json.dumps(record,indent=2)+"\n",encoding="utf-8")
print(json.dumps({k:record[k] for k in ["passed","total_cases","exact_cases","numerical_cases"]}))
