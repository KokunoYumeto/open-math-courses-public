"""Exact identities supporting the adaptive scale and full estimate."""
from pathlib import Path
from datetime import datetime,timezone
import hashlib,json
import sympy as S
MOD=Path(__file__).resolve().parent
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
s,r,q,b,delta,lam,t,z=S.symbols('s r q b delta lambda t z',positive=True)
checks=[]
def eq(name,left,right):
 v=S.simplify(left-right)
 assert v==0,(name,v)
 checks.append({'name':name,'difference':str(v),'passed':True})
def yes(name,v):
 assert v is True or v==S.true,(name,v)
 checks.append({'name':name,'passed':True})
eq('Taylor upper bound slack',(s+r)**2-(s**2+s*r+r**2/2),s*r+r**2/2)
eq('half-ball maximum loss',(s*(s/2)+(s/2)**2/2)/s**2,S.Rational(5,8))
yes('chosen positive-value margin',S.Rational(3,4)-S.Rational(5,8)>0)
eq('slow-variation lower ratio',s/(s+q*s),1/(1+q))
eq('slow-variation upper ratio',s/(s-q*s),1/(1-q))
eq('symplectic Planck parameter',S.sqrt(b**2/b**-2),b**2)
eq('first product error',b**-2*b**2,1)
eq('second product remainder',b**-2*(b**2)**2,b**2)
eq('partition square error',(b**2)**2,b**4)
eq('corrected positive coefficient times large factor',b**2*b**-2,1)
eq('first commutator weight',b**-2*b**2,1)
eq('second commutator weight',b**-2*b**2,1)
eq('derivative square full remainder',b**2*(b**2)**2,b**6)
eq('derivative positivity normalization',b**2*b**-6,b**-4)
eq('derivative product error',b*b**-2*b**2,b)
eq('energy error cancellation',b**4*(b**-2)**2,1)
eq('frame solution coefficient',8*S.sqrt(2)*S.sqrt(S.Rational(3,2)),8*S.sqrt(3))
yes('exact 14T absorption gap',8*S.sqrt(3)<14)
eq('lower-order absorption constant',14/(1-S.Rational(1,8)),16)
eq('simple-zero denominator margin',1-S.Rational(3,4),S.Rational(1,4))
eq('no nearby zero lower bound',S.Rational(1,4)*S.Rational(1,4),S.Rational(1,16))
y=S.symbols('y',real=True)
eq('gradient to floor transition',1-S.Rational(3,5)**2,S.Rational(16,25))
yes('floor interval is nonempty',S.Rational(3,5)<S.Rational(16,25))
yes('gradient is larger than value at its boundary',S.Rational(16,25)>S.Rational(3,5))
a=S.sqrt(lam)/delta
for j in [0,1,2,3,4]:
 eq('cubic-flat dilation order '+str(j),delta**3/lam*(S.sqrt(lam)/delta)**j,delta*a**(j-2))
eq('unitary symplectic dilation Jacobian',S.sqrt(lam)/S.sqrt(lam),1)
eq('example a squared',S.Rational(1,160000)/S.Rational(1,20)**2,S.Rational(1,400))
eq('example imaginary amplitude',S.Rational(1,20)*400,20)
eq('example normalized time',S.Rational(1,20)*2*3,S.Rational(3,10))
eq('example restored norm constant',16*S.Rational(3,10)/S.Rational(1,10),48)
source=MOD/'adaptive-scales-and-principal-type-estimates.md'
v={'schema':'AN04-adaptive-principal-estimate-model-check/v1','source':source.name,
 'source_sha256':sha(source),'script_sha256':sha(Path(__file__)),
 'recorded_utc':datetime.now(timezone.utc).isoformat(),'passed':True,'total_cases':len(checks),
 'exact_algebraic_checks':len(checks),'numerical_checks':0,'cases':checks,
 'scope':'Finite scale identities, transition inequalities and exact absorption constants. The infinite-dimensional operator estimate and uniform analytic bounds are proved in the lesson.'}
(MOD/'model-check.json').write_text(json.dumps(v,ensure_ascii=False,indent=2)+'\n','utf-8')
print(json.dumps({'passed':True,'exact_checks':len(checks)}))
