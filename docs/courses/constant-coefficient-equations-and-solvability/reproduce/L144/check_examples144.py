"""Independent quadrature and algebra checks complement exact lesson arguments."""
from pathlib import Path
import json,math
from scipy.integrate import quad
import numpy as np
HERE=Path(__file__).resolve().parent;checks=[]
def check(name,actual,expected,tol=1e-10):
    assert abs(actual-expected)<=tol*max(1,abs(expected)),(name,actual,expected)
    checks.append({'name':name,'actual':float(actual),'expected':float(expected),'tolerance':tol,'pass':True})
for a in [.4,1,3.2]:
    check('Gaussian area a='+str(a),quad(lambda r:2*math.pi*r*math.exp(-a*r*r),0,math.inf)[0],math.pi/a)
    check('Gaussian second moment a='+str(a),quad(lambda r:2*math.pi*r**3*math.exp(-a*r*r),0,math.inf)[0],math.pi/a**2)
inside=quad(lambda r:2*math.pi*r**3/(1+r*r)**2,0,1)[0]
outside=quad(lambda r:2*math.pi/(r*(1+r*r)**2),1,math.inf)[0]
check('Disk inside',inside,math.pi*(math.log(2)-.5))
check('Disk outside',outside,math.pi*(math.log(2)-.5))
check('Disk normalized full norm',2*(inside+outside)/math.pi,4*math.log(2)-2)
for r in [.3,1,2,5]:
    s=r*r
    exact=math.pi*(math.log1p(s)+1/(1+s)-1) if r<=1 else math.pi*(2*math.log(2)-1+math.log(s/(1+s))+1/(1+s))
    physical=quad(lambda t:2*math.pi*t*(t if t<=1 else 1/t)**2/(1+t*t)**2,0,r,points=[1] if r>1 else None)[0]
    check('Disk cumulative at R='+str(r),physical,exact)
for r in [0,.5,2,8]:
    z=np.array([r,0],dtype=complex)
    H=2*(np.eye(2)/(1+r*r)-np.outer(np.conjugate(z),z)/(1+r*r)**2)
    ev=np.linalg.eigvalsh(H)
    check('Least Levi eigenvalue at r='+str(r),ev[0],2/(1+r*r)**2)
    check('Other Levi eigenvalue at r='+str(r),ev[1],2/(1+r*r))
check('Ellipse radial level',2/25*(5/math.sqrt(2))**2,1)
check('Ellipse tangential level',2/5*math.sqrt(5/2)**2,1)
curvature_data=math.pi*quad(lambda s:math.exp(-s)/(1+s),0,math.inf)[0]
assert 0<curvature_data<math.pi
checks.append({'name':'Data example3 curvature-weighted norm is finite','actual':curvature_data,'upper_bound':math.pi,'pass':True})
record={'schema':'AN02-L144-independent-example-checks/v1','status':'PASS','checks':checks,'count':len(checks),'meaning':'Numerical/algebra checks supplement complete exact proofs;no numerical result supplies a missing prerequisite.'}
(HERE/'independent-example-checks144.json').write_text(json.dumps(record,indent=2)+'\n',encoding='utf-8')
print(json.dumps({'status':'PASS','count':len(checks),'disk_ratio':4*math.log(2)-2,'example3_curvature_norm':curvature_data}))
