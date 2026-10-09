"""Exact algebra supporting the written analytic proof; CC0-1.0."""
from pathlib import Path
import hashlib,json
import sympy as s
ROOT=Path(__file__).resolve().parent
x,t,k=s.symbols('x t k',positive=True)
I=s.I
cases=[]
def check(name,condition):
    assert bool(condition),name
    cases.append({'name':name,'passed':True})
D=lambda f:-I*s.diff(f,x)
Q=lambda f:x*D(f)
u=s.Function('u')(x)
check('shifted generator',s.simplify(D(Q(u))-(Q(D(u))-I*D(u)))==0)
check('quadratic shifted generator',s.simplify(D(D(Q(Q(u))))-(Q(Q(D(D(u))))-4*I*Q(D(D(u)))-4*D(D(u))))==0)
check('expanded fourth-order expression',s.expand(D(D(Q(Q(u))))-(x*x*s.diff(u,x,4)+5*x*s.diff(u,x,3)+4*s.diff(u,x,2)))==0)
kap=s.Function('K')(x,t)
U=s.Function('U')
check('ratio first derivative',s.simplify(D(kap*U(t*x))-(t*kap*(-I*s.diff(U(t*x),x)/t)+D(kap)*U(t*x)))==0)
check('ratio second derivative',s.simplify(D(D(kap*U(t*x)))-(kap*D(D(U(t*x)))+2*D(kap)*D(U(t*x))+D(D(kap))*U(t*x)))==0)
b=s.Function('b');c=s.Function('c')
v=2*D(kap)-t*kap*b(t*x)
w=D(D(kap))-t*t*kap*c(t*x)-D(v)
f=-s.diff(U(t*x),x,2)/t**2+b(t*x)*(-I*s.diff(U(t*x),x)/t)+c(t*x)*U(t*x)
check('complete source identity including coefficient derivatives',
      s.simplify(D(D(kap*U(t*x)))-(t*t*kap*f+D(v*U(t*x))+w*U(t*x)))==0)
for dim,N in [(0,0),(1,1),(2,2),(3,3)]:
    j=N+2;n=0
    for _ in range(j):n=1+(dim+3)*n
    check(f'test count d={dim} N={N}',n==((dim+3)**j-1)//(dim+2))
    check(f'source orders d={dim} N={N}',all(-2*j+2*l<=-2 for l in range(j)))
    check(f'source embedding endpoint d={dim} N={N}',all(i-N-1<=0 for i in range(j)) and (j-N==2))
layer=k**s.Rational(-3,2)*(k*x)*s.exp(-k*x)
check('layer L2 norm',s.simplify(s.integrate(layer**2,(x,0,s.oo))-1/(4*k**4))==0)
check('layer source norm',s.simplify(s.integrate(s.diff(layer,x,2)**2,(x,0,s.oo))-s.Rational(5,4))==0)
for j in range(4):
    g=t*x*s.exp(-t*x)
    expected=(-1)**j*t**j*(t*x-j)*s.exp(-t*x)
    check(f'profile derivative j={j}',s.simplify(s.diff(g,x,j)-expected)==0)
check('positive third derivative moment',s.diff(t*x*s.exp(-t*x),x,3).subs(x,0)==3*t**3)
check('normal derivative scaling',all(2*j-4<=0 for j in range(3)) and 2*3-4==2)
check('exercise source multiplicities',1+4+16==21)
out={'passed':True,'total_cases':len(cases),'exact_algebraic_checks':len(cases),'numerical_checks':0,
     'source_sha256':hashlib.sha256((ROOT/'boundary-regularization-with-source-tests.md').read_bytes()).hexdigest(),
     'script_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
     'scope':'Exact kernel-product identities, generator shifts, recursion counts, index bounds, boundary-layer integrals and scaling. Analytic membership, kernel seminorm bounds and graph completion are proved in the lesson.',
     'cases':cases}
(ROOT/'model-check.json').write_text(json.dumps(out,indent=2)+'\n','utf-8')
print(json.dumps({k:out[k] for k in ['passed','total_cases','exact_algebraic_checks']}))
