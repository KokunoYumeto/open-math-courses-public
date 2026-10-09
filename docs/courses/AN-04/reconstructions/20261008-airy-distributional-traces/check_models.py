"""Exact signs and exponents, plus independent normal-layer quadrature. CC0-1.0."""
from pathlib import Path
import json,hashlib
import sympy as s
import mpmath as mp
P=Path(__file__).resolve().parent;groups=[]
def group(name,values,kind='exact algebra'):
 vals=[bool(v) for v in values];assert all(vals),(name,vals)
 groups.append({'name':name,'kind':kind,'cases':len(vals),'passed':True})
t=s.symbols('t');p=s.Integer(1);q=s.Integer(0);jets=[(p,q)]
for j in range(8):
 p,q=s.diff(p,t)+t*q,p+s.diff(q,t);jets.append((s.expand(p),s.expand(q)))
group('Airy derivative recurrence and first normal traces',[
 jets[1]==(0,1),jets[2]==(t,0),jets[3]==(1,t),jets[4]==(t*t,2),
 jets[5]==(4*t,t*t),jets[6]==(t**3+4,6*t),jets[7]==(9*t*t,t**3+10),jets[8]==(t**4+28*t,12*t*t)])
mu,lam,x,y=s.symbols('mu lam x y',real=True,positive=True)
z=-x*lam**s.Rational(2,3)-mu*lam**(-s.Rational(1,3))
group('Affine equation and Dq signs',[
 s.simplify(-s.diff(z,x)**2*z-x*lam**2-mu*lam)==0,
 s.simplify(-s.I*s.diff(z,x))==s.I*lam**s.Rational(2,3),
 s.simplify((-s.diff(z,x)**2*z).subs(x,0))==mu*lam,
 s.simplify(s.diff(z,x,2))==0])
A,D=s.symbols('A D',nonnegative=True);a=A*A;b=(A+D)**2;energy=s.Rational(2,3)*((A+D)**3-A**3)
group('Positive-ray exponential weights',[
 s.simplify(energy-(b-a)*A-D**2*(3*A+2*D)/3)==0,
 s.simplify(((A+D)**3-A**3)**2-((A+D)**2-A**2)**3-A**2*D**2*(9*A**2+10*A*D+3*D**2))==0,
 s.simplify((b-a)-(2*A*D+D**2))==0])
amp=s.exp(s.I*lam**s.Rational(2,3)*y);current=amp;checks=[]
for n in range(1,7):
 current=s.I/lam*s.diff(current,y)
 checks.append(s.simplify(current/amp-(-1)**n*lam**(-s.Rational(n,3)))==0)
group('Exact transpose sign and one-third gains',checks)
group('Finite-loss integrability exponents',[
 s.Rational(3*(M+k+d+1)+1,3)>M+k+1+d
 for M,k,d in [(0,0,2),(1,2,2),(3,0,4),(0,5,3)]])
mp.mp.dps=40
def chi(a):
 if a<=-2:return mp.mpf(0)
 if a>=-1:return mp.mpf(1)
 u=a+2;u0=mp.exp(-1/u);u1=mp.exp(-1/(1-u));return u0/(u0+u1)
def F(t):return mp.airyai(t)-1j*mp.airybi(t)
f0=F(0)
def integrand(t):return abs(chi(-t)*F(-t)/f0)**2
c=mp.quad(integrand,[0,1,mp.mpf('1.5'),2])
errs=[]
for lam_value,rho in [(8,4),(64,16),(512,64)]:
 actual=mp.quad(lambda q:integrand(rho*q),[0,mp.mpf(1)/rho,mp.mpf('1.5')/rho,mp.mpf(2)/rho])
 errs.append(abs(actual*rho-c))
group('Independent affine-layer quadrature',[0<c<3,*[e<mp.mpf('1e-30') for e in errs]],'40-digit quadrature; analytic identity proved in X3')
out={'passed':True,'groups':groups,'total_cases':sum(g['cases'] for g in groups),'exact_cases':sum(g['cases'] for g in groups if g['kind']=='exact algebra'),'normal_layer_constant':str(c),'quadrature_errors':[str(e) for e in errs],'scope':'Finite formula checks only; no analytic completeness or sharp energy bound inferred.','source_sha256':hashlib.sha256((P/'distributional-airy-kernels-and-boundary-traces.md').read_bytes()).hexdigest(),'script_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}
(P/'model-check.json').write_text(json.dumps(out,indent=2)+'\n','utf-8');print(json.dumps(out,indent=2))
