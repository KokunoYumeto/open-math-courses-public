"""Exact independent algebra checks for the displayed model mechanisms; CC0."""
from pathlib import Path
import hashlib,json
import sympy as s

root=Path(__file__).resolve().parent
q,qp,r,rho,sigma,t,x,h=s.symbols('q qp r rho sigma t x h',real=True)
checks=[]
def zero(name,expr):
    reduced=s.simplify(expr)
    assert reduced==0,(name,reduced)
    checks.append({'name':name,'exact':True,'passed':True})
zero('normal density cancellation',s.diff(qp*r,r)/(qp*r)-1/r)
phase=(1-1/r)*sigma-qp*r*rho
zero('normal phase first derivative',s.diff(phase,r)-(sigma/r**2-qp*rho))
zero('normal phase second derivative',s.diff(phase,r,2)+2*sigma/r**3)
eps=s.Rational(1,10000);delta=s.Rational(1,2);C=2
assert eps<delta/(1024*(C+1))
checks.append({'name':'figure collar satisfies the exact analytic smallness bound','exact':True,'passed':True})
zero('largest adverse near-cone term at allowed collar',
     4*(delta/(1024*(C+1)))*C/(delta/s.Integer(2))-s.Rational(1,192))
# The adverse term is <= |sigma|/128 for every C>0, and < |sigma|/32.
assert s.Rational(1,192)<s.Rational(1,32)
ray_q=h*h;ray_rho=h;ray_t=-2*h-s.Rational(2,3)*h**3;ray_x=2*h
for name,expr in [
 ('Hamilton normal position',s.diff(ray_q,h)-2*ray_rho),
 ('Hamilton normal momentum',s.diff(ray_rho,h)-1),
 ('Hamilton physical clock',s.diff(ray_t,h)+2*(1+ray_q)),
 ('Hamilton tangential position',s.diff(ray_x,h)-2),
 ('characteristic identity',ray_rho**2+1-(1+ray_q)),
 ('compressed normal momentum',ray_q*ray_rho-h**3),
 ('left endpoint physical time',ray_t.subs(h,s.Rational(1,2))+s.Rational(13,12)),
 ('endpoint normal height',ray_q.subs(h,s.Rational(1,2))-s.Rational(1,4)),
 ('quadratic lower constant',1/(4*(1+s.Rational(1,12))**2)-s.Rational(36,169)),
]:zero(name,expr)
pieces=[s.Integer(0),(x+t)**2/4,t*t/2-(x-t)**2/4,t*t/2]
for j,p in enumerate(pieces):
 zero('forced-wave equation in sector '+str(j+1),s.diff(p,t,2)-s.diff(p,x,2)-(0 if j<2 else 1))
for j,interface in enumerate([-t,s.Integer(0),t]):
 for a,name in [(None,'value'),(x,'spatial first derivative'),(t,'time first derivative')]:
  f=pieces[j+1]-pieces[j]
  if a is not None:f=s.diff(f,a)
  zero('matching '+name+' at interface '+str(j+1),f.subs(x,interface))
for side,j in [('negative',0),('positive',3)]:
 zero('initial position on '+side+' half-line',pieces[j].subs(t,0))
 zero('initial velocity on '+side+' half-line',s.diff(pieces[j],t).subs(t,0))
# These checks concern algebra and exact coordinates; the oscillatory estimates,
# weak traces and wavefront conclusions are analytic proofs in the lesson.
source=root/'zero-extension-and-incoming-glancing-regularity.md'
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
result={'passed':True,'total_cases':len(checks),'exact_algebraic_checks':len(checks),
        'numerical_checks':0,'source_sha256':sha(source),'script_sha256':sha(Path(__file__)),
        'checks':checks,'analytic_proof_replaced_by_computation':False}
(root/'model-check.json').write_text(json.dumps(result,indent=2)+'\n','utf-8')
print(json.dumps({k:v for k,v in result.items() if k!='checks'}))
