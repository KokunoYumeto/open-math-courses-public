"""Bound finite exact models to the complete function-normal-form lesson."""
import hashlib
import json
import math
import subprocess
import sys
from pathlib import Path
import numpy as np
import sympy as s

here=Path(__file__).resolve().parent
source=here/'real-and-complex-symplectic-function-normal-forms.md'
text=source.read_text(encoding='utf-8')
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
checks=[]
prepared=subprocess.run([sys.executable,'-X','utf8',str(here/'check_algebra.py'),'--check-only'],capture_output=True,text=True,check=True)
models=json.loads(prepared.stdout)
assert models=={'bounded_checks':8,'all_passed':True,'source_documents_needed':False,'state_mutated':False}
checks.append({'name':'eight complete finite preparation model families','passed':True,
    'model_script_sha256':sha(here/'check_algebra.py'),
    'scope':'Weighted bracket/dilation, positive normalizers, contraction polynomial, degrees and full coordinates, nonconstant multiplier law, nested words, parity, complex division and bounded flat-quotient jets.'})

x,y,z,xi,eta,h=s.symbols('x y z xi eta h',real=True)
variables=[x,y,z,xi,eta,h]
def pb(f,g):
    return s.expand(sum(s.diff(f,k)*s.diff(g,j)-s.diff(f,j)*s.diff(g,k) for j,k in [(x,xi),(y,eta),(z,h)]))
def one_form(positions,momenta):
    return [s.simplify(sum(m*s.diff(q,v) for q,m in zip(positions,momenta))) for v in variables]
def canonical(positions,momenta):
    assert one_form(positions,momenta)==[xi,eta,h,0,0,0]
    for i in range(3):
        for j in range(3):
            assert s.simplify(pb(momenta[i],positions[j])-(1 if i==j else 0))==0
            assert s.simplify(pb(momenta[i],momenta[j]))==0
            assert s.simplify(pb(positions[i],positions[j]))==0

canonical([-xi/h,y,z+x*xi/h],[x*h,eta,h])
inverse={'x':xi/h,'xi':-x*h,'z':z+(xi/h)*x}
for alpha in [s.Rational(2,3),s.Rational(3,4)]:
    K=1+y
    canonical([x*K**alpha,y,z],[xi*K**(-alpha),eta-alpha*xi*x/K,h])
    tau=s.symbols('tau',positive=True)
    # Here eta is the tangential momentum, since K depends on y.
    eta_s=eta-alpha*xi*x/K*(1-s.exp(-tau))
    assert s.simplify(s.diff(eta_s,tau)+alpha*xi*x*s.exp(-tau)/K)==0
    assert s.simplify(s.limit(eta_s,tau,s.oo)-(eta-alpha*xi*x/K))==0
    assert s.simplify((eta_s-alpha*(xi*s.exp(-alpha*tau))*(x*s.exp(-(1-alpha)*tau))/K)
        -(eta-alpha*xi*x/K))==0
canonical([x,y,z-s.Rational(1,3)*x*x],[xi+s.Rational(2,3)*x*h,eta,h])
checks.append({'name':'full real exchange, tangential-drift and fourth-contact canonical maps','passed':True,
    'scope':'All one-form components and every canonical bracket, two exact backwards tangential flows and their invariant momentum; no general flow proof inferred.'})

K=s.exp(x+s.I*y)
p=K*(xi+s.I*eta)
pbar=s.conjugate(p)
assert s.simplify(pb(p,pbar)+4*s.I*s.exp(2*x)*eta)==0
w=-x-s.I*y
f0=2*K
assert s.simplify(pb(p,s.conjugate(w)).subs({xi:0,eta:0})+f0)==0
q=s.simplify(s.exp(w)*p)
assert q==xi+s.I*eta and pb(q,s.conjugate(q))==0
full=s.exp(w+s.conjugate(w))*(pb(p,pbar)+pb(p,s.conjugate(w))*pbar+pb(w,pbar)*p+pb(w,s.conjugate(w))*p*pbar)
assert s.simplify(full)==0
simple_real=s.exp(y)*xi
simple_imag=s.exp(y)*x*eta
assert s.simplify(pb(simple_real,simple_imag)-s.exp(2*y)*(eta-x*xi))==0
checks.append({'name':'exact exponential bracket, elliptic zero-set model and simple bracket','passed':True,
    'scope':'Full four-term multiplier identity in an actual nonconstant complex model, initial anti-conjugate coefficient equation and exact final commuting symbol.'})

# Fixed-order existence is substantive even when every existing zero has that order.
quad=x*x+y*y
assert s.diff(quad,x,2).subs({x:0,y:0})==2
for yy in [s.Rational(1,100),-s.Rational(1,100)]:
    assert s.Poly(quad.subs(y,yy),x).discriminant()<0
cubic=x**3+x*y
assert s.diff(cubic,x,3)==6 and s.diff(cubic,x).subs(x,0)==y
assert text.count('**Exercise ')==text.count('**Solution.**')==14
assert 'existence of the fixed-order zero on each nearby curve' in text
assert not any(ord(ch)<32 and ch not in '\n\r\t' for ch in text)
checks.append({'name':'pointwise and vacuous fixed-order counterexamples and source controls','passed':True,
    'scope':'Exact cubic unfolding, two real leaf parameters with no quadratic zero, fourteen solution markers and unintended-control-byte guard.'})

# Independently verify the polynomial flow-integral exercise.
P,Q=s.symbols('P Q',real=True)
u=1+s.Rational(6,5)*P-s.Rational(9,4)*Q+2*P*Q+s.Rational(3,7)*P*P+s.Rational(5,2)*Q**3
f=1+2*P-3*Q+4*P*Q+P*P+5*Q**3
assert s.expand(u+s.Rational(2,3)*P*s.diff(u,P)+s.Rational(1,3)*Q*s.diff(u,Q)-f)==0
assert s.Rational(5,2)+s.Rational(2,5)*(-s.Rational(9,4))==s.Rational(8,5)
assert s.Rational(3,4)+s.Rational(3,5)*(-s.Rational(9,4))==-s.Rational(3,5)
checks.append({'name':'exact graded degree and contraction-integral solutions','passed':True,
    'scope':'All six polynomial coefficients and three degrees checked independently of prose.'})

# A finite projected Fourier model of the parameter solver, checked two ways.
# This is not a discretization claiming proof of the local fundamental solution.
modes=[(i,j) for i in range(-3,4) for j in range(-3,4) if (i,j)!=(0,0)]
index={v:k for k,v in enumerate(modes)}
count=len(modes)
lam=np.array([1j*i-j for i,j in modes])
T=np.diag(1/lam)
dxT=np.diag(np.array([1j*i for i,j in modes])/lam)
dyT=np.diag(np.array([1j*j for i,j in modes])/lam)
Mcos=np.zeros((count,count),complex)
Msin=np.zeros((count,count),complex)
for col,(i,j) in enumerate(modes):
    for shift in [-1,1]:
        if (i+shift,j) in index:
            Mcos[index[(i+shift,j)],col]+=0.5
        if (i,j+shift) in index:
            Msin[index[(i,j+shift)],col]+=shift/(2j)
A0=Mcos@dxT+0.5*Msin@dyT
eps=0.11
A=eps*A0
norm=float(np.linalg.norm(A,2))
assert norm<=1.5*eps+1e-12
datum=np.array([np.exp(-0.2*(i*i+j*j))*(1+0.1j*(i-j)) for i,j in modes])
g=np.linalg.solve(np.eye(count)+A,datum)
solution=T@g
assert np.max(np.abs((np.diag(lam)+eps*(Mcos@np.diag([1j*i for i,j in modes])
    +0.5*Msin@np.diag([1j*j for i,j in modes])))@solution-datum))<1e-12
series=datum.copy()
term=datum.copy()
for _ in range(30):
    term=-A@term
    series+=term
assert np.max(np.abs(series-g))<1e-12

grid=np.arange(41)*2*np.pi/41
gx,gy=np.meshgrid(grid,grid,indexing='ij')
basis=np.stack([np.exp(1j*(i*gx+j*gy)) for i,j in modes])
field_x=np.einsum('k,kij->ij',np.array([1j*i for i,j in modes])*solution,basis)
field_y=np.einsum('k,kij->ij',np.array([1j*j for i,j in modes])*solution,basis)
Lu=(1+eps*np.cos(gx))*field_x+(1j+0.5*eps*np.sin(gy))*field_y
projection=np.einsum('kij,ij->k',basis.conjugate(),Lu)/41**2
assert np.max(np.abs(projection-datum))<1e-12
step=1e-6
def solve_parameter(t):
    return T@np.linalg.solve(np.eye(count)+t*A0,datum)
numerical=(solve_parameter(eps+step)-solve_parameter(eps-step))/(2*step)
analytic=-T@np.linalg.solve(np.eye(count)+A,A0@g)
parameter_error=float(np.max(np.abs(numerical-analytic)))
assert parameter_error<1e-8
checks.append({'name':'finite parameter Neumann solver and independent spatial Fourier projection','passed':True,
    'modes':count,'grid_points':41**2,'operator_norm':norm,'parameter_derivative_max_error':parameter_error,
    'scope':'Projected nonzero Fourier modes with variable elliptic coefficients, direct matrix inverse, Neumann series and independent oversampled derivative quadrature. This finite projected model does not prove the local solver or all-order regularity.'})

# Flux normalization of the Cauchy fundamental kernel on an actual circle.
theta=np.arange(64)*2*np.pi/64
for radius in [1,0.5,0.125,0.015625]:
    zz=radius*np.exp(1j*theta)
    phi=1+zz+zz.conjugate()+2*zz*zz.conjugate()
    contour=np.mean(phi)
    assert abs(contour-(1+2*radius*radius))<1e-12
checks.append({'name':'Cauchy boundary normalization','passed':True,
    'scope':'Exact sampled degree-two trigonometric boundary flux tends to test value1 with error2r squared; distributional polar integral identity and Fourier bounds are proved in the lesson.'})

report={'schema':'bounded-function-normal-form-computational-check/v1','passed':all(r['passed'] for r in checks),
    'checks':checks,'lesson':source.name,'lesson_sha256':sha(source),'script_sha256':sha(Path(__file__)),
    'independent_review':False,'scope':'Finite exact/algebraic and independent numerical checks of the written models. General theorem proofs, local solver, smooth jets and all-order estimates remain author mathematical arguments.'}
(here/'model-check.json').write_text(json.dumps(report,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
print(json.dumps({'checks':len(checks),'prepared_model_families':8,'all_passed':report['passed'],'lesson_sha256':report['lesson_sha256']}))
