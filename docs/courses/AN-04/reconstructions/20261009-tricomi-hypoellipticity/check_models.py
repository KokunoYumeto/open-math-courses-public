"""Exact identities accompanying, not replacing, the Tricomi regularity proof."""
from pathlib import Path
import hashlib,json
import sympy as s
ROOT=Path(__file__).resolve().parent
cases=[]
def check(name,expression):
 result=s.simplify(s.expand(expression))
 assert result==0,(name,result)
 cases.append({'name':name,'exact_residual':str(result)})
for a in [s.Rational(1,2),s.Integer(1),s.Rational(3,2),s.Integer(2)]:
 check(f'a={a}: normal norm scale',a+s.Rational(1,2)-s.Rational(1,2)-a)
 check(f'a={a}: optimized A exponent',1-a/(a+1)-1/(a+1))
 check(f'a={a}: optimized B exponent',1-1/(a+1)-a/(a+1))
check('first weighted mixed index',(1+s.Rational(1,2)*0)/(1+s.Rational(1,2))-s.Rational(2,3))
check('second weighted mixed index',(2+s.Rational(2,3))/2-s.Rational(4,3))
check('normal derivative trace index',s.Rational(2,3)/2-s.Rational(1,3))
check('boundary pairing value index',2-s.Rational(1,3)-s.Rational(5,3))
check('commutator leaves one-third gain',s.Rational(4,3)-1-s.Rational(1,3))
x=s.symbols('x',real=True)
f,g,k=(s.Function(n)(x) for n in ['f','g','k'])
cross=sum((-s.diff(v,x,2)+k*v)**2-s.diff(v,x,2)**2-(k*v)**2
          -2*k*s.diff(v,x)**2+s.diff(k,x,2)*v**2 for v in [f,g])
flux=sum(-2*k*s.diff(v,x)*v+s.diff(k,x)*v**2 for v in [f,g])
check('full complex-valued Green identity as a total derivative',cross-s.diff(flux,x))
check('two-jet extension value',s.Integer(3)-2-1)
check('two-jet extension first derivative',-s.Integer(3)+4-1)
for n,value in [(0,s.Rational(1,2)),(1,s.Rational(1,4)),(2,s.Rational(1,4))]:
 check(f'exponential moment {n}',s.integrate(x**n*s.exp(-2*x),(x,0,s.oo))-value)
check('full example left norm',s.integrate((4*x-1)**2*s.exp(-2*x),(x,0,s.oo))-s.Rational(5,2))
check('full example signed boundary identity',s.Rational(1,2)+4+2-4-s.Rational(5,2))
check('omitted boundary term has size four',s.Rational(13,2)-s.Rational(5,2)-4)
for lam,q in [(1,1),(8,4),(27,9),(64,16)]:
 check(f'lambda={lam}: normal scale',s.Integer(lam)**s.Rational(2,3)-q)
 check(f'lambda={lam}: scaled lower support endpoint',s.Rational(1,q)*q-1)
 check(f'lambda={lam}: scaled upper support endpoint',s.Rational(2,q)*q-2)
check('second normal derivative exponent',2*s.Rational(2,3)-s.Rational(4,3))
check('potential exponent',2-s.Rational(2,3)-s.Rational(4,3))
source=ROOT/'tricomi-boundary-regularity.md'
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
result={'passed':True,'source_sha256':sha(source),'script_sha256':sha(Path(__file__)),
 'total_cases':len(cases),'exact_algebraic_checks':len(cases),'numerical_checks':0,'cases':cases,
 'scope':'Exact interpolation indices, complex Green identity, boundary example and scaling identities. The analytic regularity proof is in the lesson.'}
(ROOT/'model-check.json').write_text(json.dumps(result,indent=2)+'\n','utf-8')
print(json.dumps({k:v for k,v in result.items() if k!='cases'}))
