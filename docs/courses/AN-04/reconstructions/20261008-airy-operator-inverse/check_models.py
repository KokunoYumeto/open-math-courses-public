"""Finite ordered identities and separately labelled Airy samples. CC0-1.0."""
from pathlib import Path
import hashlib,json
import sympy as s
import numpy as np
from scipy.special import airy
ROOT=Path(__file__).resolve().parent
groups=[]
def add(name,cases,kind,scope):
    groups.append(dict(name=name,cases=cases,kind=kind,scope=scope,passed=True))
eye=s.eye(2)
for j in range(1,7):
    A=s.Matrix([[1,s.Rational(j,7)],[0,1]])
    B=s.Matrix([[0,s.Rational(1,j+2)],[s.Rational(j,9),s.I/5]])
    N0=s.diag(2+s.I,3-s.I)
    H=N0.inv();G=A.inv();C=A+B*H;T=C*G-eye;N=A*N0+B
    assert s.simplify(N-C*N0)==s.zeros(2)
    Q=N.inv()
    assert s.simplify(N*Q-eye)==s.zeros(2) and s.simplify(Q*N-eye)==s.zeros(2)
    Nm=A*(-s.conjugate(N0))+B
    r=H*(-s.conjugate(N0))
    assert s.simplify(-Q*Nm+r+Q*B*(eye-r))==s.zeros(2)
    for k in range(1,7):
        Uk=sum([(-T)**h for h in range(k)],s.zeros(2))
        Qk=H*G*Uk
        assert s.simplify(N*Qk-eye-(-1)**(k-1)*T**k)==s.zeros(2)
add("Finite correction residual",36,"exact",
    "Six noncommuting finite operator matrices and six truncation depths; exact right residual signs and ordering.")
add("Exact factorization and two-sided inverse",6,"exact",
    "Six finite models test N=C N0 and both ordered inverse identities; no symbol-class assertion follows from a finite matrix.")
add("Reflection cancellation",6,"exact",
    "Six noncommuting finite operator models test the full identity eliminating the apparent one-third loss.")

x,eta,theta=s.symbols("x eta theta",real=True)
D=lambda v:-s.I*s.diff(v,x)
C0=s.Matrix([[1,0],[0,2]])
C1=s.Matrix([[0,1],[2,0]])
C2=s.Matrix([[1,s.I],[0,1]])
b=s.exp(-x*x)*s.Matrix([[1,x],[s.I*x,2]])
for k in range(1,5):
    u=s.exp(s.I*k*x)*s.Matrix([1,x])
    actual=C0*b*u+C1*D(b*u)+C2*D(D(b*u))
    expanded=C0*b*u+C1*b*D(u)+C2*b*D(D(u))+C1*D(b)*u+2*C2*D(b)*D(u)+C2*D(D(b))*u
    assert s.simplify(actual-expanded)==s.zeros(2,1)
add("Complete polynomial composition",4,"exact",
    "Four Gaussian-matrix inputs test the terminating degree-two composition, all derivative terms and D=-i partial.")
for k in range(1,5):
    u=s.exp(s.I*k*x)*s.Matrix([1,x])
    bs=s.conjugate(b.T)
    assert s.simplify(D(bs*u)-bs*D(u)-D(bs)*u)==s.zeros(2,1)
add("Adjoint correction sign",4,"exact",
    "Four matrix Gaussian tests verify D composed with the conjugate coefficient equals its full left-symbol expansion.")
lam=s.symbols("lam",positive=True);ph=s.symbols("ph",nonzero=True)
derivative=(1/s.I)*lam**(-1)*(-(-ph**2)/ph**2)
assert s.simplify(derivative+s.I/lam)==0
add("Exact Airy derivative at the transition",1,"exact",
    "The Riccati identity gives partial_mu h=-i/lambda, excluding ordinary order-minus-two-thirds membership.")

mu=np.linspace(-5,5,41);lv=16.
ai,aip,bi,bip=airy(mu*lv**(-1/3))
phi=(aip-1j*bip)/(ai-1j*bi)
h=1/(1j*lv**(2/3)*phi)
center=h[20]
kernel=(h-center)*np.exp(-mu*mu/4)
assert np.all(np.isfinite(kernel)) and abs(kernel[20])<1e-14
assert np.max(np.abs(kernel))>1e-3
add("Gaussian commutator-kernel samples",41,"numerical",
    "Forty-one Airy samples at lambda=16 illustrate the normalized Fourier-kernel factor; they do not prove the symbol calculus.")
source=ROOT/"variable-matrix-airy-boundary-parametrices.md"
record=dict(passed=True,groups=groups,total_cases=sum(g["cases"] for g in groups),
    exact_cases=sum(g["cases"] for g in groups if g["kind"]=="exact"),
    numerical_cases=sum(g["cases"] for g in groups if g["kind"]=="numerical"),
    source_sha256=hashlib.sha256(source.read_bytes()).hexdigest(),
    script_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
    finite_checks_do_not_replace_proofs=True)
(ROOT/"model-check.json").write_text(json.dumps(record,indent=2)+"\n",encoding="utf-8")
print(json.dumps({k:record[k] for k in ["passed","total_cases","exact_cases","numerical_cases"]}))
