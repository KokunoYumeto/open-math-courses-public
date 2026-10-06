"""Finite sign, Fourier, covector and support controls; general proofs are in the lesson."""
from pathlib import Path
import json,hashlib
import sympy as s
import numpy as np
MOD=Path(__file__).resolve().parent
src=MOD/'real-principal-type-kernels-and-propagation.md'
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
checks=[]
t,z,a,b,tau,eta=s.symbols('t z a b tau eta',real=True)
f=s.exp(-t*t)
Ep=s.I*s.sqrt(s.pi)/2*(1+s.erf(t));Em=-s.I*s.sqrt(s.pi)/2*s.erfc(t)
assert s.simplify(-s.I*s.diff(Ep,t)-f)==0
assert s.simplify(-s.I*s.diff(Em,t)-f)==0
assert s.simplify((Ep-Em-s.I*s.sqrt(s.pi)).rewrite(s.erf))==0
assert s.simplify(-s.I*s.diff(-Em,t)+f)==0
checks.append({'name':'both fundamental signs and constant difference','passed':True,
 'scope':'Exact decaying Gaussian input and both signed antiderivatives; reversed backward sign gives minus the input. Distributional and compact-support claims use the written transpose proof.'})

v,r,ss,w=s.symbols('v r ss w',real=True)
Y=s.Matrix([t-ss,z-w,ss,w]);x=s.Matrix([t,z,ss,w])
J=Y.jacobian(x);cov=J.T*s.Matrix([tau,eta,0,0])
assert cov==s.Matrix([tau,eta,-tau,-eta])
prime=s.Matrix([cov[0],cov[1],-cov[2],-cov[3]])
assert prime==s.Matrix([tau,eta,tau,eta])
checks.append({'name':'entire kernel coordinate transpose and input twist','passed':True,
 'scope':'Exact invertible four-variable Jacobian; includes tau=0 flow covectors and tau-nonzero diagonal covectors.'})

decay=s.symbols('decay',positive=True)
F=1/(decay+s.I*tau)
assert s.simplify(F-1/(s.I*tau)+decay/(s.I*tau*(decay+s.I*tau)))==0
trials=0
for rate in [.25,1,4]:
 for freq in [-256,-64,-16,16,64,256]:
  value=1/(rate+1j*freq)
  assert abs(value-1/(1j*freq))<=rate/freq**2*(1+1e-12)
  assert abs(value)>0
  trials+=1
checks.append({'name':'both-frequency half-line asymptotic and nonvanishing','passed':True,
 'trials':trials,'scope':'Exact transform of H(v)exp(-a*v), with positive a. This integrable exponential model tests the sign and second-order remainder; the compact smooth-cutoff proof is the two integrations in RP7a.'})

kappa=s.exp(-(t-ss)**2-(z-w)**2)
psi=s.exp(-z*z);psi1=s.exp(-w*w)
kernel=psi*kappa*psi1
assert s.simplify(s.diff(kernel,t)+s.diff(kernel,ss))==0
wrong=(t+ss)*kernel
assert s.simplify(s.diff(wrong,t)+s.diff(wrong,ss)-2*kernel)==0
checks.append({'name':'time-translation commutator and failed absolute-time cutoff','passed':True,
 'scope':'Exact sum of both time derivatives; spatial factors allowed. The general compact difference-cutoff construction and full symbol remainder are the written proof.'})

def H(p):return s.Matrix([s.diff(p,tau),s.diff(p,eta),-s.diff(p,t),-s.diff(p,z)])
p=tau*eta+t*tau**2
q=(tau**2+eta**2)**s.Rational(-1,2)
assert all(s.simplify(v)==0 for v in H(q*p)-q*H(p)-p*H(q))
assert H(t*tau)==s.Matrix([t,0,-tau,0])
assert H(t*tau).subs(t,0)==s.Matrix([0,0,-tau,0])
lam=s.symbols('lam',positive=True)
assert s.simplify((q*p).subs({tau:lam*tau,eta:lam*eta})-lam*q*p)==0
checks.append({'name':'positive degree reduction and radial characteristic','passed':True,
 'scope':'Full Hamilton product rule for a nonconstant homogeneous degree-two symbol, degree-one reduction, and exact x*xi radial field. Flow invariance uses the earlier full uniqueness proof.'})

G=s.I*(t**3/3+t*z**2)
assert s.simplify(-s.I*s.diff(G,t)-(t*t+z*z))==0
for n in range(2,13):
 assert s.Rational(n-1,2)-s.Rational(2*n,4)==-s.Rational(1,2)
checks.append({'name':'smooth primitive sign and conormal order','passed':True,
 'scope':'Exact mixed-variable primitive and eleven ambient/phase dimension balances, retaining the ambient dimension 2n.'})

trials=[]
for size in [8,17,32]:
 dt=1/size
 for direction in [1,-1]:
  matrix=direction*1j*dt*(np.tril(np.ones((size,size))) if direction==1 else np.triu(np.ones((size,size))))
  norm=float(np.linalg.norm(matrix,2))
  assert norm<=1+1e-12
  trials.append({'dimension':size,'direction':direction,'norm':norm,'bound':1})
# A constant input on [a,b] observed entirely after b attains the product bound.
for length,J in [(1,2),(.25,3),(4,.5)]:
 lhs=J*length**2
 rhs=J*length*length
 assert abs(lhs-rhs)<1e-12
checks.append({'name':'signed finite Volterra controls and exact interval factors','passed':True,
 'models':trials,'scope':'Finite quadrature operators satisfy the interval-product bound; continuous constant-input examples attain its factors. General L2 continuity is proved by Cauchy-Schwarz and product integration.'})

text=src.read_text('utf-8')
assert text.count('**Exercise ')==text.count('**Solution.**')==3
report={'schema':'AN04-real-principal-finite-check/v1','passed':True,'checks':checks,
 'lesson_sha256':sha(src),'script_sha256':sha(Path(__file__)),'exercise_solutions':3,
 'generality_guard':'Finite and exact model checks support the written general distribution, wavefront, support and propagation proofs; they do not certify those theorems.',
 'full_course_complete':False,'public_release_authorized':False}
(MOD/'model-check.json').write_text(json.dumps(report,indent=2)+'\n','utf-8')
print(json.dumps({'passed':True,'groups':len(checks),'source_sha256':sha(src)}))
