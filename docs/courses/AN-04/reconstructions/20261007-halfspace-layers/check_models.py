"""Independent finite algebra checks; these do not certify analytic estimates."""
from pathlib import Path
import json,hashlib
import sympy as S
ROOT=Path(__file__).resolve().parent
I=S.I
checks=[]
lam=S.symbols('lam',positive=True);z,r=S.symbols('z r',real=True)
H=[S.Matrix([[j+1,j*j+2],[3-j,2*j-1]]) for j in range(6)]
for a in [2,-1,-3]:
 U=[]
 for n in range(6):
  u=H[n]-sum((S.binomial(a-j,n-j)*U[j]*(I*lam)**(n-j) for j in range(n)),S.zeros(2))
  U.append(u.applyfunc(S.expand))
 # Independently expand the rational/polynomial normal multiplier at z=1/kappa.
 model=sum((U[j]*z**j*(1+I*lam*z)**(a-j) for j in range(6)),S.zeros(2))
 for p in range(2):
  for q in range(2):
   actual=S.series(model[p,q],z,0,6).removeO().expand()
   assert all(S.simplify(actual.coeff(z,n)-H[n][p,q])==0 for n in range(6))
checks.append({'name':'Full six-coefficient model expansion','passed':True,'normal_degrees':[2,-1,-3],'matrix_size':2})

psi=S.Matrix([1+2*r+3*r**2-r**3+5*r**6,2-r+4*r**3+2*r**5])
for m in range(1,6):
 A=[S.Matrix([[ell+1+r+r**2,2-r+ell*r**3],[r**2-ell,3+ell*r+r**4]]) for ell in range(m+1)]
 jets=[S.Matrix([a+1,2-a]) for a in range(m)]
 direct=0
 for ell in range(1,m+1):
  for k in range(ell):
   test=(A[ell]*jets[ell-1-k]).dot(psi)
   direct+=-I*I**k*S.diff(test,r,k).subs(r,0)
 grouped=0
 for a in range(m):
  for b in range(m-a):
   for q in range(m-a-b):
    coeff=I**(q-1)*S.binomial(b+q,q)*A[a+b+q+1].diff(r,q).subs(r,0)*jets[a]
    grouped+=I**b*coeff.dot(psi.diff(r,b).subs(r,0))
 assert S.simplify(direct-grouped)==0
checks.append({'name':'Complete source against polynomial dual tests','passed':True,'normal_degrees':[1,2,3,4,5],'includes_all_coefficient_derivatives':True})

x=S.symbols('x',real=True)
G=S.Matrix(3,3,lambda b,c:S.integrate(x**(b+c)/(1+x*x)**3,(x,-S.oo,S.oo)))
assert G==S.pi*S.Matrix([[3,0,1],[0,1,0],[1,0,3]])/8
assert set(G.eigenvals())=={S.pi/8,S.pi/4,S.pi/2}
v=S.Matrix([1,I,2])
direct=S.integrate(S.expand_complex((1+I*x+2*x*x)*S.conjugate(1+I*x+2*x*x))/(1+x*x)**3,(x,-S.oo,S.oo))
assert S.simplify(direct-(S.conjugate(v.T)*G*v)[0])==0
assert direct!=sum(S.conjugate(v[j])*G[j,j]*v[j] for j in range(3))
checks.append({'name':'Full three-jet Fourier Gram norm','passed':True,'cross_terms_nonzero':True})

k=S.symbols('k',real=True)
for h in range(1,5):
 actual=(-I)**h/S.factorial(h-1)*(-1)**(h-1)*S.diff(1/(lam-I*k),lam,h-1)
 assert S.simplify(actual-(k+I*lam)**(-h))==0
checks.append({'name':'Negative model kernel Fourier phase and factorial','passed':True,'pole_orders':[1,2,3,4]})

sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
record={'schema':'AN04-halfspace-layers-models/v1','source_sha256':sha(ROOT/'halfspace-layers.md'),
 'script_sha256':sha(Path(__file__)),'passed':True,'general_theorem_certified':False,'checks':checks}
(ROOT/'model-check.json').write_text(json.dumps(record,indent=2)+'\n',encoding='utf-8')
print(json.dumps({'passed':True,'finite_check_groups':len(checks)}))
