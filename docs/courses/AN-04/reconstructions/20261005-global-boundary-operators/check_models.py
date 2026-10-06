"""Finite checks of exact coordinates and signs; not replacements for the proofs."""
from pathlib import Path
import hashlib,json,math
import sympy as S
import numpy as np
ROOT=Path(__file__).resolve().parent
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
t,r,z,x,y,a,b=S.symbols('t r z x y a b',positive=True)
ar=1+r/2;br=1-r/2
checks=[]
assert S.simplify((t*ar+t*br)/2-t)==0
assert S.simplify(2*(t*ar-t*br)/(t*ar+t*br)-r)==0
assert S.det(S.Matrix([t*ar,t*br]).jacobian([t,r]))==-t
assert S.simplify((a*t*ar+b*t*br)/2-t*(a*ar+b*br)/2)==0
rbar=2*(a*ar-b*br)/(a*ar+b*br)
assert S.simplify(rbar.subs(r,-2)+2)==0 and S.simplify(rbar.subs(r,2)-2)==0
checks.append('Exact positive-corner inverse, signed determinant and preservation of both side faces')
zinv=r/ar;rinv=2*z/(2-z)
assert S.simplify(zinv.subs(r,rinv)-z)==0
assert S.simplify((2/(2-z))/ar.subs(r,rinv)-1)==0
assert S.simplify((t*ar)*(2-zinv)/2-t)==0
assert S.simplify(S.diff(zinv,r)-ar**-2)==0
assert S.simplify(S.diff(x*br/ar,r)+x*ar**-2)==0
checks.append('Full inverse kernel prefactors, radial inverse and fixed-output boundary measure')
p,q,rho,eta=S.symbols('p q rho eta',real=True)
F=p+q**2;alpha=S.exp(p+2*q)
normal=alpha*q
J=S.Matrix([F,normal]).jacobian([p,q])
tau_bar=S.Matrix([eta,rho/normal])
ordinary=J.T*tau_bar
compressed=S.Matrix([ordinary[0],q*ordinary[1]])
claimed=S.Matrix([S.diff(F,p)*eta+S.diff(S.log(alpha),p)*rho,
 q*S.diff(F,q)*eta+(1+q*S.diff(S.log(alpha),q))*rho])
assert S.simplify(compressed-claimed)==S.zeros(2,1)
assert S.simplify(claimed.jacobian([eta,rho]).subs(q,0).det())==1
checks.append('Full nonlinear compressed covector transition including both tangential-normal cross terms')
for n in range(1,9):
 ordered=[v for j in range(n) for v in [n+j,j]]
 inversions=sum(ordered[i]>ordered[j] for i in range(2*n) for j in range(i+1,2*n))
 assert (-1)**inversions==(-1)**(n*(n+1)//2)
checks.append('Symplectic top-wedge sign in dimensions one through eight')
f=1+t**2+rho**3+t*rho
full=f.subs({t:t*(1+r/2),rho:rho*(1+r/2)},simultaneous=True)
v=S.symbols('v',real=True)
integrand=(t*S.diff(f,t)+rho*S.diff(f,rho)).subs({t:t*(1+v*r/2),rho:rho*(1+v*r/2)},simultaneous=True)
# GL16 retains t and rho outside the differentiated a evaluation.
integrand=t*S.diff(f,t).subs({t:t*(1+v*r/2),rho:rho*(1+v*r/2)},simultaneous=True)+rho*S.diff(f,rho).subs({t:t*(1+v*r/2),rho:rho*(1+v*r/2)},simultaneous=True)
assert S.simplify(full-f-r*S.integrate(integrand,(v,0,1))/2)==0
checks.append('Exact radial first-difference integral before the signed Fourier integration by parts')
D=lambda expr,var,k=1:(-S.I)**k*S.diff(expr,var,k)
for pp in range(4):
 for qq in range(4):
  symbol=x**pp*z**qq
  for degree in range(5):
   u=x**degree
   output=x**pp*x**qq*D(u,x,qq)
   for k in range(5):
    direct=D(output,x,k).subs(x,0)
    jet=0
    for j in range(k+1):
     akj=sum(S.binomial(j,i)*D(D(symbol,x,k-j),z,i).subs({x:0,z:0}) for i in range(j+1))
     jet+=S.binomial(k,j)*akj*D(u,x,j).subs(x,0)
    assert S.simplify(direct-jet)==0,(pp,qq,degree,k)
checks.append('All nested boundary-jet coefficients against 400 polynomial operator/input/order cases')
B=S.Matrix([[1+x,1],[x,2+x]])
inv=B.inv()
assert S.simplify(S.diff(inv,x)+inv*S.diff(B,x)*inv)==S.zeros(2)
E=S.Matrix([[1,2],[3,0]])
correction=-E*inv
assert S.simplify(E+correction*B)==S.zeros(2)
assert S.simplify(E-inv*E*B)!=S.zeros(2)
checks.append('Ordered matrix inverse derivative and parametrix cancellation with a noncommuting error')
for ss in [-3.4,-.2,.6,3.2]:
 aa=math.floor(ss);bb=aa+1
 w=np.array([2**(-d*(ss-aa)) if d>=0 else 2**(d*(bb-ss)) for d in range(-80,81)])
 total=1/(1-2**(-(ss-aa)))+1/(1-2**(-(bb-ss)))-1
 assert np.sum(w)<=total+1e-12
 matrix=np.array([[2**(-(j-l)*(ss-aa)) if j>=l else 2**(-(l-j)*(bb-ss)) for j in range(30)] for l in range(30)])
 assert np.linalg.norm(matrix,2)<=total+1e-12
checks.append('Summable dyadic coordinate matrix at four positive and negative noninteger indices')
result={'passed':True,'finite_groups':len(checks),'checks':checks,
 'source_hashes':{p.name:sha(p) for p in ROOT.glob('*.md')},'script_sha256':sha(Path(__file__)),
 'scope':'Finite symbolic and numerical checks support exact identities; the complete analytic proofs are in the companions.',
 'U031_restored':False}
(ROOT/'model-check.json').write_text(json.dumps(result,indent=2)+'\n','utf-8')
print(json.dumps({'passed':True,'finite_groups':len(checks)}))
