"""CC0-1.0. Exact checks supplement, but do not certify, the analytic proof."""
from pathlib import Path
import hashlib,json
import sympy as S
ROOT=Path(__file__).resolve().parent
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
checks=[]
def equal(name,a,b):
 d=a-b
 ok=all(S.simplify(v)==0 for v in d) if isinstance(d,S.MatrixBase) else S.simplify(d)==0
 assert ok,(name,S.simplify(d));checks.append({'name':name,'passed':True,'kind':'exact_identity'})
def bound(name,condition):
 assert bool(condition),name;checks.append({'name':name,'passed':True,'kind':'exact_finite_inequality'})
x,z=S.symbols('x z',real=True);lam=S.symbols('lambda',positive=True);a,b,g=S.symbols('a b gamma',real=True)
D=lambda f,v:-S.I*S.diff(f,v)
P=lambda f:D(D(f,x),x)-z*D(D(f,z),z)
for j,chi in enumerate([x*z,x*x*z*z,1+x**3+z**3]):
 u=S.exp(-x)*(1+S.I*z+z*z)
 rhs=-2*S.I*S.diff(chi,x)*D(u,x)-S.diff(chi,x,2)*u+2*S.I*z*S.diff(chi,z)*D(u,z)+z*S.diff(chi,z,2)*u
 equal('complete localized differential source '+str(j),P(chi*u)-chi*P(u),rhs)
equal('unequal-order trace equality',lam**(2*g+a+b),2*(lam**(g+a-S.Rational(1,2))/S.sqrt(2))*(lam**(g+b+S.Rational(1,2))/S.sqrt(2)))
v=lam**S.Rational(3,2)*S.exp(-lam*x)
equal('normal input norm squared',S.integrate(v*v,(x,0,S.oo))*lam**-2,S.Rational(1,2))
equal('normal derivative norm squared',S.integrate(S.diff(v,x)**2,(x,0,S.oo))*lam**-4,S.Rational(1,2))
equal('lower boundary norm squared',v.subs(x,0)**2*lam**-3,1)
equal('stronger boundary norm squared',v.subs(x,0)**2*lam**(-3+S.Rational(1,2)),S.sqrt(lam))
eta,eps,s=S.symbols('eta epsilon s',real=True,positive=True)
weight=(1+eta**2)**(s/2)/(1+eps**2*eta**2)
equal('regularizer logarithmic derivative',S.diff(weight,eta)/weight,s*eta/(1+eta**2)-2*eps**2*eta/(1+eps**2*eta**2))
equal('ordered conjugation first symbol',-S.I*eta**2*S.diff(weight,eta)/weight,-S.I*eta**2*(s*eta/(1+eta**2)-2*eps**2*eta/(1+eps**2*eta**2)))
# Full Green identity with a nonconstant selfadjoint matrix test and complex R.
G=S.Matrix([[1+x,S.I*x],[-S.I*x,2]])
R=S.Matrix([[1+S.I,x],[S.I,2-S.I*x]])
u=S.exp(-x)*S.Matrix([1+S.I*x,1+x])
inner=lambda f,h:(S.conjugate(h).T*f)[0]
integrate=lambda f:S.integrate(S.expand(f),(x,0,S.oo))
Pu=D(D(u,x),x)-R*u
lhs=integrate(inner(D(u,x),D(G*u,x))-inner(R*u,G*u))
rhs=integrate(inner(Pu,G*u))-S.I*inner(D(u,x).subs(x,0),(G*u).subs(x,0))
equal('matrix Green source and boundary sign',lhs,rhs)
equal('matrix test selfadjoint',G,S.conjugate(G).T)
# A nonconstant first-order incoming operator and a differential weight.
L=lambda f:D(f,x)-z*D(f,z)-S.I*f
W=lambda f:f+D(D(f,z),z)
chi=1+x*z+z*z;u=S.exp(-x)*(1+z+S.I*z**3)
commW=lambda f:L(W(f))-W(L(f))
commChi=lambda f:L(chi*f)-chi*L(f)
equal('incoming full ordered commutator',L(W(chi*u)),W(chi*L(u))+commW(chi*u)+W(commChi(u)))
equal('incoming cutoff commutator order zero',commChi(u),(-S.I*S.diff(chi,x)+S.I*z*S.diff(chi,z))*u)
for N in [1,2,4,8,16,32]:
 terms=[1/(1+S.Rational(n*n,N*N))**2 for n in range(1,N+1)]
 bound('source L2 lower bound N='+str(N),sum(terms)>=S.Rational(N,4))
 total=sum(1/(S.Integer(1+n*n)*(1+S.Rational(n*n,N*N))**2) for n in range(1,65))
 bound('finite lower source norm N='+str(N),total<2)
result={'passed':True,'source_sha256':sha(ROOT/'localized-half-order-diffraction-estimate.md'),
 'script_sha256':sha(Path(__file__)),'total_cases':len(checks),'exact_algebraic_checks':len(checks),
 'numerical_checks':0,'checks':checks,'scope':'Exact finite identities and inequalities for the displayed examples, signs and ordered operations. The full microlocal estimates, graph limits and source preparation are proved in the lesson, not inferred from these checks.'}
(ROOT/'model-check.json').write_text(json.dumps(result,indent=2)+'\n','utf-8')
print(json.dumps({k:v for k,v in result.items() if k!='checks'}))
