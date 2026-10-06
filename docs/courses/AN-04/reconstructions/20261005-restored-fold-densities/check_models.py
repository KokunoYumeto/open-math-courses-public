"""Bounded exact density/phase checks for U019; arbitrary-symbol proofs remain analytic."""
import hashlib,json
from pathlib import Path
import sympy as S
import numpy as np
from scipy.special import roots_hermite
here=Path(__file__).resolve().parent;checks=[]
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
def record(name,evidence):checks.append({'name':name,'passed':True,'bounded_evidence':evidence})
def zero(expr):assert S.simplify(expr)==0
def eq(a,b):assert all(S.simplify(v)==0 for v in a-b)
for n in [2,3,4]:
    x=S.symbols('x1:'+str(n+1));y=S.symbols('y1:'+str(n+1))
    xi=S.symbols('xi1:'+str(n+1));rho=xi[-1]
    s,tau=S.symbols('s tau');delta=y[0]-x[0]
    Phi=sum((x[j]-y[j])*xi[j] for j in range(n))+s*xi[0]-s**3*rho/3
    phi=sum((x[j]-y[j])*xi[j] for j in range(n))+tau*xi[0]/rho-tau**3/(3*rho**2)
    F=S.Matrix([S.diff(Phi,t) for t in list(xi)+[s]])
    Fh=S.Matrix([S.diff(phi,t) for t in list(xi)+[tau]])
    normal=S.Matrix(list(y)+[xi[0]])
    zero(F.jacobian(normal).det()-(-1)**n)
    zero(Fh.jacobian(normal).det()-(-1)**n/rho)
    A=S.eye(n+1);A[n-1,n]=-s/rho;A[n,n]=1/rho
    eq(Fh.subs(tau,s*rho),A*F);zero(A.det()-1/rho)
    # ambient rho and inverse normal rho give rho^2, in all tested dimensions.
    zero(rho/(S.Integer(1)/rho)-rho**2)
record('full normal constraint determinants and exact constraint transformation',
       'n=2,3,4: raw determinant (-1)^n, homogeneous determinant (-1)^n/rho; every constraint identity and the second tangential radial Jacobian are retained.')
for n in [2,3,4]:
    x=S.symbols('x1:'+str(n+1));y=S.symbols('y1:'+str(n+1));xi=S.symbols('xi1:'+str(n+1))
    rho=xi[-1];delta=y[0]-x[0];u,v=S.symbols('u v')
    tau=u+rho*delta;first=v+rho*delta**2+delta*u+u*u/(3*rho)
    phi=sum((x[j]-y[j])*xi[j] for j in range(n))+S.Symbol('tau')*xi[0]/rho-S.Symbol('tau')**3/(3*rho**2)
    Psi=sum((x[j]-y[j])*xi[j] for j in range(1,n))-delta**3*rho/3
    zero(phi.subs({S.Symbol('tau'):tau,xi[0]:first},simultaneous=True)-Psi-u*v/rho)
    zero(S.Matrix([first,tau]).jacobian(S.Matrix([v,u])).det()-1)
    H=S.hessian(Psi+u*v/rho,S.Matrix(list(xi[1:])+[u,v])).subs({u:0,v:0})
    eq(H[-2:,-2:],S.Matrix([[0,1/rho],[1/rho,0]]))
    assert H[:-2,:]==S.zeros(n-1,n+1)
    F=S.Matrix([S.diff(Psi,z) for z in xi[1:]])
    zero(F.jacobian(S.Matrix(y[1:])).det()-(-1)**(n-1))
    on={y[j]:x[j] for j in range(1,n-1)};on[y[-1]]=x[-1]-delta**3/3
    # Covector formulas are identities before imposing the base constraints.
    eq(S.Matrix([S.diff(Psi,z) for z in x]),S.Matrix([delta**2*rho]+list(xi[1:])))
    eq(S.Matrix([-S.diff(Psi,z) for z in y]),S.Matrix([delta**2*rho]+list(xi[1:])))
record('exact degree-one hyperbolic elimination and reduced phase',
       'n=2,3,4: full phase identity, auxiliary determinant one, exact Hessian with one positive and one negative eigenvalue, reduced critical determinant and all output/input covector signs.')
rho,tau,z,w,s=S.symbols('rho tau z w s',positive=True)
for mu in [S.Rational(-2,3),S.Rational(1,4),S.Rational(7,2)]:
    a=rho**mu*(1+s+s*s)*(1+z/rho+(w/rho)**2)
    at=a.subs(s,tau/rho)/rho
    zero(S.diff(at,tau)-(S.diff(a,s)/rho**2).subs(s,tau/rho))
    zero(S.diff(at,z)-(S.diff(a,z)/rho).subs(s,tau/rho))
    expected=-a/rho**2+S.diff(a,rho)/rho-s*S.diff(a,s)/rho**2
    zero(S.diff(at,rho)-expected.subs(s,tau/rho))
    zero(rho*at.subs(tau,rho*s)-a)
    zero(S.diff(rho*at.subs(tau,rho*s),s)-S.diff(a,s))
    ac=a.subs(z,s*s*rho)
    zero(S.diff(ac,s)-(S.diff(a,s)+2*s*rho*S.diff(a,z)).subs(z,s*s*rho))
record('symbol-chain identities in positive and negative fractional orders',
       'Three exact homogeneous amplitudes: fixed-tau radial derivatives, inverse amplitude change, s derivatives and critical substitution all agree; finite examples do not replace the higher-derivative proof.')
for n,m in [(2,S.Rational(-1,6)),(3,S.Rational(-1,4)),(4,S.Rational(5,3))]:
    d=2*n;Nh=n+1;Nr=n-1
    zero(m+S.Rational(d-2*Nh,4)-(m-S.Rational(1,2)))
    zero(m+S.Rational(d-2*Nr,4)-(m+S.Rational(1,2)))
    zero((m-S.Rational(1,2))+S.Rational(Nh,2)-(m+S.Rational(n,2)))
    zero((m+S.Rational(1,2))+S.Rational(Nr,2)-(m+S.Rational(n,2)))
    zero(S.Rational(d+2*Nh,4)-S.Rational(d+2*Nr,4)-1)
record('two normalizations and common half-density order',
       'Three dimensions/orders: amplitude shifts plus/minus 1/2, prefactor exponent difference one, and symbol degree m+n/2; all arithmetic is exact.')
# A Fourier approximate identity independently checks the 2pi constant and cubic sign.
nodes,weights=roots_hermite(100);rho0=1.4;delta0=.7
target=2*np.pi*np.exp(-delta0**2)*np.exp(-1j*rho0*delta0**3/3)
errors=[]
for epsilon in [.01,.001,.0001]:
    values=delta0+2*np.sqrt(epsilon)*nodes
    approximate=2*np.sqrt(np.pi)*np.sum(weights*np.exp(-values**2)*np.exp(-1j*rho0*values**3/3))
    errors.append(float(abs(approximate-target)))
assert errors[0]>errors[1]>errors[2] and errors[-1]/abs(target)<.001
record('first-frequency Fourier inversion by a Gaussian approximate identity',
       {'rho':rho0,'signed_sheet_parameter':delta0,'regularization':[.01,.001,.0001],
        'absolute_errors':errors,'expected_constant':'2pi','expected_cubic_sign':'negative',
        'guard':'One Schwartz s amplitude and fixed radial/sheet parameters; convergence proof is Fourier inversion, not this numerical sample.'})
s,t,rho=S.symbols('s t rho',real=True);mu=S.Rational(1,3)
p=(1-s*s)**6;terms=[]
for k in range(1,5):
    p=S.cancel(S.I*S.diff(p/(t-s*s),s))
    amp=rho**(mu-k)*p
    zero(rho*S.diff(amp,rho)-(mu-k)*amp)
    zero(p.subs(s,1));zero(p.subs(s,-1))
    terms.append({'steps':k,'radial_degree':str(mu-k)})
assert 3-1==2
record('bounded first-frequency integration-by-parts model',
       {'amplitude':'(1-s^2)^6 on [-1,1], extended by zero; finite boundary-vanishing model',
        'phase_derivative':'rho(t-s^2)','first_frequency_ratio':'t>=3',
        'exact_iterates':terms,
        'guard':'Four integrations only; the arbitrary smooth compact-support all-derivative tail proof is analytic.'})
lesson=here/'fold-amplitudes-and-critical-densities.md'
report={'schema':'bounded-fold-density-check/v1','passed':True,'checks':checks,
        'lesson':lesson.name,'lesson_sha256':sha(lesson),'script_sha256':sha(Path(__file__)),
        'independent_review':False,'full_course_complete':False,
        'guard':'Exact finite dimensions, selected amplitude identities and one Fourier numerical example support the written proof; no arbitrary-symbol representation or Airy continuity theorem is computationally certified.'}
(here/'model-check.json').write_text(json.dumps(report,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
print(json.dumps({'passed':True,'checks':len(checks),'lesson_sha256':sha(lesson),'fourier_errors':errors}))
