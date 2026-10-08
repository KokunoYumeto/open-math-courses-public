"""Independent real Hessians, circle means, pullbacks and integrability checks."""
from pathlib import Path
import json
import mpmath as mp
import numpy as np
mp.mp.dps=60;HERE=Path(__file__).resolve().parent;rows=[]
def add(name,actual,expected,tol=1e-38):
 error=float(abs(actual-expected));scale=max(1,float(abs(expected)))
 rows.append(dict(name=name,absolute_error=error,relative_error=error/scale,
  tolerance=tol,passed=error<=tol*scale))
def bound(name,value,limit,lower=False,tol=1e-40):
 rows.append(dict(name=name,actual=float(value),bound=float(limit),lower_bound=lower,
  tolerance=tol,passed=bool(value+tol>=limit if lower else value<=limit+tol)))
for R in [mp.mpf(1)/128,mp.mpf('.4')]:
 for k in [mp.mpf(1),mp.mpf(4)]:
  psi=lambda x,y:R*abs(y)-k*mp.log(1+mp.sqrt(x*x+y*y))
  for x in [mp.mpf(-2),mp.mpf(0),mp.mpf(1)]:
   for y in [mp.mpf('.1'),mp.mpf(1),mp.mpf(4)]:
    Levi=(mp.diff(psi,(x,y),(2,0))+mp.diff(psi,(x,y),(0,2)))/4
    radius=mp.sqrt(x*x+y*y);expected=-k/(4*radius*(1+radius)**2)
    add('actual-naive-real-Hessian-'+str((R,k,x,y)),Levi,expected)
    bound('actual-naive-strict-negative-sign-'+str((R,k,x,y)),Levi,0)

psi=lambda x,y:mp.mpf(1)/128*abs(y)-4*mp.log(1+mp.sqrt(x*x+y*y))
for h in [mp.mpf('.02'),mp.mpf('.05'),mp.mpf('.1'),mp.mpf('.2'),mp.mpf('.00001')]:
 mean=mp.quad(lambda theta:psi(h*mp.cos(theta),1+h*mp.sin(theta)),[0,mp.pi,2*mp.pi])/(2*mp.pi)
 difference=mean-psi(0,1)
 bound('actual-circle-mean-violation-'+str(h),difference,0)
 if h<mp.mpf('.001'):
  add('actual-small-circle-leading-Levi-coefficient',difference/(h*h),-mp.mpf(1)/4,1e-9)

t=mp.mpf(4096);a=mp.mpf(2);R=mp.mpf(1)/128
def strict(x,y):
 sy=t*t+y*y
 return R*abs(y)-a*mp.log(t*t+x*x+y*y)+mp.sqrt(sy)/mp.sqrt(t)-sy**mp.mpf('.25')
for x in [mp.mpf(0),t,-2*t]:
 for y in [t/50,t/10,t,4*t]:
  Levi=(mp.diff(strict,(x,y),(2,0))+mp.diff(strict,(x,y),(0,2)))/4
  sy=t*t+y*y;q=t*t/sy
  formula=sy**mp.mpf('-.75')/4*(q**mp.mpf('.75')+mp.mpf('.25')-mp.mpf('.75')*q)-a*t*t/(t*t+x*x+y*y)**2
  add('actual-strict-seed-real-Hessian-'+str((x,y)),t**mp.mpf('1.5')*Levi,t**mp.mpf('1.5')*formula)
  bound('actual-strict-Levi-lower-bound-'+str((x,y)),Levi,sy**mp.mpf('-.75')/32,lower=True)
  gradient=mp.sqrt(mp.diff(strict,(x,y),(1,0))**2+mp.diff(strict,(x,y),(0,1))**2)
  bound('actual-strict-gradient-bound-'+str((x,y)),gradient,R+a/t+1/mp.sqrt(t))

for x,y in [(0,0),(1,0),(0,1),(.3,-.4),(-1.2,.7)]:
 x,y=mp.mpf(x),mp.mpf(y);pullback=lambda u,v:(u*u+v*v)**2
 Levi=(mp.diff(pullback,(x,y),(2,0))+mp.diff(pullback,(x,y),(0,2)))/4
 add('actual-z-squared-pullback-Hessian-'+str((x,y)),Levi,4*(x*x+y*y))

# Independent multivariate real differentiation checks the complex matrix and phases.
def pullback(x1,x2,y1,y2):
 z1=mp.mpc(x1,y1);z2=mp.mpc(x2,y2)
 return abs(z1*z1+z2)**2+3*abs(z1-mp.j*z2*z2)**2
for point in [(0,0,0,0),(1,-.3,.4,1.1),(-.7,.8,-1.2,.5)]:
 pp=tuple(mp.mpf(v) for v in point);H=np.zeros((4,4))
 for j in range(4):
  for k in range(4):
   orders=[0]*4;orders[j]+=1;orders[k]+=1
   H[j,k]=float(mp.diff(pullback,pp,tuple(orders)))
 Levi=np.array([[(H[j,k]+H[j+2,k+2]+1j*H[j+2,k]-1j*H[j,k+2])/4 for k in range(2)] for j in range(2)])
 z1=complex(point[0],point[2]);z2=complex(point[1],point[3])
 J=np.array([[2*z1,1],[1,-2j*z2]])
 expected=J.conj().T@np.diag([1,3])@J
 add('actual-multivariate-holomorphic-Levi-pullback-'+str(point),np.max(abs(Levi-expected)),0,1e-12)

for n in [1,2,3]:
 area=2*mp.pi**n/mp.factorial(n-1)
 actual=area*mp.quad(lambda r:r**(2*n-1)/(1+r)**(2*n+2),[0,1,mp.inf])
 expected=mp.pi**n/(mp.factorial(n)*(2*n+1))
 add('actual-stage-integrable-complex-dimension-'+str(n),actual,expected)
add('actual-carrier-radius-sum',mp.mpf(1)/128+1/mp.sqrt(t),mp.mpf(3)/128)
bound('actual-strict-domain-support-gap',mp.mpf(3)/128,mp.mpf(1)/32)

status='PASS' if all(row['passed'] for row in rows) else 'FAIL'
record=dict(schema='AN02-L156-independent-checks181/v1',status=status,checks=len(rows),records=rows,
 max_relative_error=max(r.get('relative_error',0) for r in rows),
 checks_supplement_full_proofs=True,topology_and_scope_claims_not_inferred_from_samples=True)
(HERE/'independent-example-checks181.json').write_text(json.dumps(record,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print(json.dumps({k:v for k,v in record.items() if k!='records'}))
assert status=='PASS',[r for r in rows if not r['passed']]
