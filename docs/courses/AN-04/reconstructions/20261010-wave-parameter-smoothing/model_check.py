"""Exact finite checks for WS5--WS32; the analytic proof is in the lesson."""
from pathlib import Path
import json,hashlib
import sympy as s

checks=[]
def equal(name,left,right):
    residual=s.simplify(left-right)
    assert residual==0,(name,residual)
    checks.append({'name':name,'passed':True,'method':'exact symbolic identity'})
def positive(name,value):
    value=s.simplify(value)
    assert value.is_positive,(name,value)
    checks.append({'name':name,'passed':True,'exact_positive_value':str(value)})
Q=s.Rational
cstar=Q(101,100)
equal('initial Euclidean radius',Q(2,5)*cstar,Q(101,250))
equal('transformed target radius',Q(101,250)+Q(1,100),Q(207,500))
positive('target radius is strictly inside M',Q(21,50)-Q(207,500))
positive('metric path cannot leave unit ball',1/cstar-Q(2,5))
equal('support excess at maximal time',Q(2,5)*cstar+3*(cstar-1)+Q(1,100),Q(111,250))
equal('common zero-region gap',Q(1,2)-Q(111,250),Q(7,125))
equal('uniform backward observation gap',Q(99,100)-Q(21,50)-Q(1,2),Q(7,100))
equal('compact spatial travel bound',Q(21,50)+Q(201,100)+Q(6,5),Q(363,100))
positive('travel stays inside radius four',4-Q(363,100))
equal('flow displacement over five units',5*Q(1,500),Q(1,100))
equal('sample velocity has unit length',Q(3,5)**2+Q(4,5)**2,1)
hit=Q(3,2)-Q(1,5)/Q(3,5)
equal('reflection time',hit,Q(7,6))
equal('reflection tangential coordinate',Q(1,10)+(hit-Q(3,2))*Q(4,5),-Q(1,6))
dt=-Q(11,10)-Q(3,2)
equal('sample backward time increment',dt,-Q(13,5))
r=-Q(1,5)-dt*Q(3,5)
y=Q(1,10)+dt*Q(4,5)
equal('sample reflected normal coordinate',r,Q(34,25))
equal('sample tangential coordinate',y,-Q(99,50))
equal('sample squared spatial radius',r*r+y*y,Q(577,100))
positive('sample is exterior to observation boundary',r*r+y*y-Q(8,5)**2)
positive('sample target is inside M',Q(21,50)**2-Q(1,5)**2-Q(1,10)**2)
a,c,t,x,z=s.symbols('a c t x z', real=True)
B=s.Matrix([[1,0],[a,1]])
A=s.Matrix([[1,a],[a,1+a*a]])
equal('shear determinant',B.det(),1)
assert A==B*B.T
checks.append({'name':'positive spatial matrix is B times its transpose','passed':True,'method':'exact matrix identity'})
assert B.inv()*A*B.inv().T==s.eye(2)
checks.append({'name':'exact transformed principal matrix','passed':True,'method':'exact matrix identity'})
metric=(s.Matrix([x,z]).T*A.inv()*s.Matrix([x,z]))[0]
equal('metric ball under the shear',metric,x*x+(z-a*x)**2)
equal('normalized wave coefficient derivative',s.diff(c**-2,c),-2*c**-3)
positive('one-dimensional interior gap',Q(99,100)-Q(2,5)-Q(2,5))
u=s.Function('u')(a,x,t)
def Rt(v):return a*a*s.diff(v,t,2)+a*s.diff(v,t)+v
def P(v):return -s.diff(v,x,2)-Rt(v)
for k in range(1,4):
    correction=sum(s.binomial(k,j)*(s.diff(a*a,a,j)*s.diff(u,a,k-j,t,2)+s.diff(a,a,j)*s.diff(u,a,k-j,t)) for j in range(1,k+1))
    equal('parameter commutator sign, order '+str(k),P(s.diff(u,a,k))-s.diff(P(u),a,k),correction)
v=s.Function('v')(x,t)
def Rr(w):return (a+x)*s.diff(w,t,2)+(1+x*x)*s.diff(w,t)+x*w
forcing=-s.diff(v,x,2)-Rr(v)
for j in range(4):
    terms=sum(s.binomial(j,h)*(s.diff(a+x,x,h)*s.diff(v,x,j-h,t,2)+s.diff(1+x*x,x,h)*s.diff(v,x,j-h,t)+s.diff(x,x,h)*s.diff(v,x,j-h)) for h in range(j+1))
    equal('ordinary normal recurrence, order '+str(j),s.diff(v,x,j+2)+terms+s.diff(forcing,x,j),0)
result={'schema':'AN04-wave-parameter-smoothing-exact-checks/v1','total_cases':len(checks),
        'exact_algebraic_checks':len(checks),'numerical_checks':0,'all_passed':True,
        'analytic_proof_established_by_these_checks':False,'checks':checks}
result['passed']=True
result['source_sha256']=hashlib.sha256(Path(__file__).with_name('wave-smoothing-uniform-in-the-coefficients.md').read_bytes()).hexdigest()
result['script_sha256']=hashlib.sha256(Path(__file__).read_bytes()).hexdigest()
Path(__file__).with_name('model-check.json').write_text(json.dumps(result,indent=2)+'\n','utf-8')
print(json.dumps({k:result[k] for k in ['total_cases','exact_algebraic_checks','all_passed']}))
