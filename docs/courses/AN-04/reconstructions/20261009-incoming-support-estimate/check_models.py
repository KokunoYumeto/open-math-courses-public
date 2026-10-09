"""CC0-1.0. Exact ordered algebra, evolution signs and geometric margins."""
from pathlib import Path
import hashlib,json
import sympy as S
ROOT=Path(__file__).resolve().parent
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
checks=[]
def equal(name,a,b):
 d=a-b
 if isinstance(d,S.MatrixBase): ok=all(S.simplify(v)==0 for v in d)
 else: ok=S.simplify(d)==0
 assert ok,(name,d)
 checks.append({'name':name,'passed':True,'kind':'exact_identity'})
def bound(name,value):
 assert bool(value),name
 checks.append({'name':name,'passed':True,'kind':'exact_inequality'})
x,z,rho,eta=S.symbols('x z rho eta',real=True)
a=S.symbols('a',nonnegative=True)
N=S.Matrix([[0,1],[0,0]]);B=S.diag(1,2);I=S.eye(2)
M=I+S.I*x*N;Mi=I-S.I*x*N;q=M*B*Mi
equal('nilpotent square',N*N,S.zeros(2))
equal('ordered inverse',M*Mi,I)
equal('fundamental matrix ODE',S.diff(M,x),S.I*N*M)
equal('inverse matrix ODE',S.diff(Mi,x),-S.I*Mi*N)
equal('transported matrix',q,B+S.I*x*N)
equal('matrix transport equation',S.diff(q,x),S.I*(N*q-q*N))
equal('transported determinant',q.det(),2)
equal('scalar transport defect',-S.I*(N*B-B*N),-S.I*N)
h=S.Function('h')
u=M*S.Matrix([0,1])*h(z+x)
D=lambda f,v:-S.I*S.diff(f,v)
A=lambda f:D(f,z)+N*f
equal('exact full factor on the example',D(u,x)-A(u),S.zeros(2,1))
equal('principal-only factor on the example',D(u,x)-D(u,z),S.Matrix([1,0])*h(z+x))
equal('second-order homogeneous equation',D(D(u,x),x)-D(D(u,z),z)-2*N*D(u,z),S.zeros(2,1))
U=S.Matrix([S.Function('u1')(x,z),S.Function('u2')(x,z)])
equal('full ordered factor product',D(D(U,x)-A(U),x)+A(D(U,x)-A(U)),D(D(U,x),x)-D(D(U,z),z)-2*N*D(U,z))
p=rho**2-x*eta**2
equal('Hamilton normal coordinate',S.diff(p,rho),2*rho)
equal('Hamilton normal covector',-S.diff(p,x),eta**2)
equal('Hamilton tangential coordinate',S.diff(p,eta),-2*x*eta)
equal('Hamilton tangential covector',-S.diff(p,z),0)
equal('negative-graph normal-coordinate slope',(-2*x)/(-2*S.sqrt(x)),S.sqrt(x))
path=S.Rational(2,3)*(x**S.Rational(3,2)-a**S.Rational(3,2))
equal('path derivative',S.diff(path,x),S.sqrt(x))
equal('path initial displacement',path.subs(x,a),0)
equal('reference slice displacement',path.subs({x:S.Rational(1,16),a:0}),S.Rational(1,96))
equal('whole initial-height displacement',S.Rational(2,3)*S.Rational(1,64)**S.Rational(3,2),S.Rational(1,768))
equal('whole-family margin',S.Rational(1,1024)+S.Rational(1,768),S.Rational(7,3072))
bound('strict slice inclusion',S.Rational(7,3072)<S.Rational(1,384))
equal('left slice endpoint',S.Rational(1,96)-S.Rational(1,384),S.Rational(1,128))
equal('right slice endpoint',S.Rational(1,96)+S.Rational(1,384),S.Rational(5,384))
for height in [S.Integer(0),S.Rational(1,256),S.Rational(1,64)]:
 for initial in [-S.Rational(1,1024),S.Integer(0),S.Rational(1,1024)]:
  hit=initial+path.subs({x:S.Rational(1,16),a:height})
  bound('plotted slice point '+str((height,initial)),abs(hit-S.Rational(1,96))<S.Rational(1,384))
result={'passed':True,'source_sha256':sha(ROOT/'incoming-root-estimates-on-the-full-support.md'),
 'script_sha256':sha(Path(__file__)),'total_cases':len(checks),'exact_algebraic_checks':len(checks),'numerical_checks':0,'checks':checks,
 'scope':'Ordered example products, Hamilton signs, exact paths and whole-family margins. The full analytic theorem and actual weak traces are proved in the lesson, not certified by these finite checks.'}
(ROOT/'model-check.json').write_text(json.dumps(result,indent=2)+'\n','utf-8')
print(json.dumps({k:v for k,v in result.items() if k!='checks'}))
