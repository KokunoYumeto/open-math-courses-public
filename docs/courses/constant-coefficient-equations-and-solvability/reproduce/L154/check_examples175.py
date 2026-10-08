"""Actual polynomial jets, roots, torus coefficients, heat operators and moments."""
from pathlib import Path
import json,math
import numpy as np
import mpmath as mp
mp.mp.dps=60
HERE=Path(__file__).resolve().parent;rows=[]
def add(name,actual,expected,tol=1e-40):
 err=float(abs(actual-expected));scale=max(1,float(abs(expected)))
 rows.append(dict(name=name,absolute_error=err,relative_error=err/scale,
                  tolerance=tol,passed=err<=tol*scale))
def bound(name,actual,limit,upper=True,slack=mp.mpf('1e-45')):
 rows.append(dict(name=name,actual=float(actual),bound=float(limit),upper_bound=upper,
                  passed=bool(actual<=limit+slack if upper else actual+slack>=limit)))
for center in [mp.j,mp.mpc(0)]:
 p=lambda z:(z-center)**2
 for x in [mp.mpf(v) for v in ['-4','-1','0','.5','3','8']]:
  jets=[mp.diff(p,x,a) for a in range(3)]
  d=abs(x-center);A=mp.sqrt(sum(abs(v)**2 for v in jets))
  B=mp.sqrt(sum(abs(v)**2 for v in jets[1:]))
  add('actual-double-root-full-strength-'+str((center,x)),A,d*d+2)
  add('actual-double-root-positive-jets-'+str((center,x)),B,2*mp.sqrt(d*d+1))
  add('actual-double-root-ratio-'+str((center,x)),A/B,(d*d+2)/(2*mp.sqrt(d*d+1)))

# Universal dimension-one comparison, using actual derivatives of factored inputs.
root_sets=[[mp.j,mp.j],[mp.mpc(0),mp.mpc(0)],
 [mp.mpc(1,.2),mp.mpc(-2,.5)],[mp.mpc(0,.3)]*3,
 [mp.mpc(-2,.2),mp.mpc(1,1.1),mp.mpc(3,-.4),mp.mpc(.2,2)]]
for index,roots in enumerate(root_sets):
 degree=len(roots);poly=lambda z:mp.fprod(z-r for r in roots)
 D=mp.sqrt(sum((mp.factorial(degree)/mp.factorial(degree-a))**2 for a in range(1,degree+1)))
 lower=1/(2*max(1,D));upper=mp.sqrt(1+sum(1/mp.factorial(a) for a in range(1,degree+1))**2)
 for x in [mp.mpf(v) for v in ['-7','-1.2','0','.7','3','10']]:
  jets=[mp.diff(poly,x,a) for a in range(degree+1)]
  ratio=mp.sqrt(sum(abs(v)**2 for v in jets))/mp.sqrt(sum(abs(v)**2 for v in jets[1:]))
  distance=min(abs(x-r) for r in roots)
  bound('actual-ratio-distance-lower-'+str((index,x)),ratio,lower*(1+distance),upper=False)
  bound('actual-ratio-distance-upper-'+str((index,x)),ratio,upper*(1+distance)**degree)

# Closest complex points of actual affine polynomials with complex coefficients.
for c in [np.array([1,2j]),np.array([1+.3j,-.4+1.2j]),np.array([-.2j,2-1j])]:
 for point in [np.array([0.,0.]),np.array([1.,-2.]),np.array([-3.,.7])]:
  constant=.4+.6j;value=c@point+constant;norm=np.linalg.norm(c)
  zero=point-value*np.conjugate(c)/(norm*norm)
  add('actual-affine-nearest-zero-'+str((c.tolist(),point.tolist())),c@zero+constant,0,1e-13)
  add('actual-affine-zero-distance-'+str((c.tolist(),point.tolist())),np.linalg.norm(zero-point),abs(value)/norm,1e-13)
  full=np.sqrt(abs(value)**2+norm*norm)/norm
  add('actual-affine-strength-distance-'+str((c.tolist(),point.tolist())),full,
      np.sqrt(1+(abs(value)/norm)**2),1e-13)

# Extract actual complex homogeneous coefficients and compare with true derivatives.
angles=2*np.pi*np.arange(64)/64
w1=np.exp(1j*angles)[:,None]/np.sqrt(2);w2=np.exp(1j*angles)[None,:]/np.sqrt(2)
polys=[(lambda x,y:x*x+3*x*y+2*y*y,[(2,0),(1,1),(0,2)]),
       (lambda x,y:(1+1j)*x**3-2*x*x*y+3j*y**3,[(3,0),(2,1),(1,2),(0,3)])]
for index,(poly,indices) in enumerate(polys):
 values=poly(w1,w2)
 for alpha in indices:
  coefficient=np.mean(values*np.exp(-1j*(alpha[0]*angles[:,None]+alpha[1]*angles[None,:])))
  recovered=coefficient*math.factorial(alpha[0])*math.factorial(alpha[1])*2**(sum(alpha)/2)
  actual=mp.diff(poly,(mp.mpf(0),mp.mpf(0)),alpha)
  add('actual-unit-torus-coefficient-'+str((index,alpha)),recovered,complex(actual),1e-13)

# Actual heat characteristic coordinates and geometric bounds.
for a,b in [(-2,.3),(.4,-1.2),(0,0),(1,1),(3,-3),(.1,.7)]:
 z1=a+1j*b;z2=-2*a*b+1j*(a*a-b*b);eta=np.hypot(b,a*a-b*b)
 add('actual-heat-polynomial-zero-'+str((a,b)),z1*z1+1j*z2,0,1e-13)
 bound('heat-spatial-coordinate-bound-'+str((a,b)),abs(z1),np.sqrt(3)*(1+eta),slack=1e-12)
 bound('heat-time-coordinate-bound-'+str((a,b)),abs(z2),3*(1+eta)**2,slack=1e-12)
for t in [mp.mpf(v) for v in ['.1','.5','1','3','10']]:
 z1=(1+mp.j)*t;z2=-2*t*t
 add('sharp-heat-root-spatial-'+str(t),abs(z1),mp.sqrt(2)*t)
 add('sharp-heat-root-time-'+str(t),abs(z2),2*t*t)

# Integrate the actual complex solution and its moments on t=0.
for a0 in [mp.mpf('.8'),mp.mpf(1),mp.mpf(2)]:
 for x in [mp.mpf(v) for v in ['-.3','0','.4','1']]:
  value=mp.quad(lambda s:mp.exp(-a0*s+(mp.j-1)*x*s),[0,mp.inf])
  add('actual-heat-solution-integral-'+str((a0,x)),value,1/(a0+(1-mp.j)*x))
 for j in [1,2,3,5,8]:
  spatial=mp.quad(lambda s:((1+mp.j)*s)**j*mp.exp(-a0*s),[0,mp.inf])
  temporal=mp.quad(lambda s:(-2*s*s)**j*mp.exp(-a0*s),[0,mp.inf])
  add('actual-spatial-heat-derivative-'+str((a0,j)),spatial,(1+mp.j)**j*mp.factorial(j)/a0**(j+1))
  add('actual-time-heat-derivative-'+str((a0,j)),temporal,(-2)**j*mp.factorial(2*j)/a0**(2*j+1))
  rational=lambda x:1/(a0+(1-mp.j)*x)
  add('actual-rational-spatial-derivative-'+str((a0,j)),(-mp.j)**j*mp.diff(rational,0,j),
      (1+mp.j)**j*mp.factorial(j)/a0**(j+1))

# Differentiate the actual kernels in the physical coordinates, including D signs.
for s in [mp.mpf('.2'),mp.mpf('.9'),mp.mpf('2')]:
 for x,t in [(mp.mpf(0),mp.mpf(0)),(mp.mpf('.3'),mp.mpf('-.2'))]:
  kernel=lambda a,b:mp.exp((mp.j-1)*a*s-2*mp.j*b*s*s)
  heat=mp.diff(kernel,(x,t),(0,1))-mp.diff(kernel,(x,t),(2,0))
  add('actual-heat-operator-'+str((s,x,t)),heat,0)
  for j in [1,2,3]:
   add('actual-kernel-spatial-D-phase-'+str((s,x,t,j)),(-mp.j)**j*mp.diff(kernel,(x,t),(j,0)),
       ((1+mp.j)*s)**j*kernel(x,t))
   add('actual-kernel-time-D-phase-'+str((s,x,t,j)),(-mp.j)**j*mp.diff(kernel,(x,t),(0,j)),
       (-2*s*s)**j*kernel(x,t))

# Independent positive radial moments and the noninteger calculus supremum.
for q in [0,2,4,8,12,16,24,40]:
 actual=mp.quad(lambda r:2*mp.pi*r*(1+r)**q*mp.exp(-2*r),[0,mp.inf])
 expected=2*mp.pi*sum(mp.binomial(q,l)*mp.factorial(l+1)/2**(l+2) for l in range(q+1))
 add('actual-two-dimensional-exponential-moment-'+str(q),actual,expected)
for q,delta in [(mp.mpf('3.5'),mp.mpf('.7')),(mp.mpf(4),mp.mpf(2)),(mp.mpf('.4'),mp.mpf(1))]:
 location=max(0,q/delta-1);function=lambda r:(1+r)**q*mp.exp(-delta*r)
 maximum=1 if q<=delta else (q/delta)**q*mp.exp(-q+delta)
 add('actual-calculus-maximum-'+str((q,delta)),function(location),maximum)
 if location>0:add('actual-stationary-exponential-moment-'+str((q,delta)),mp.diff(function,location),0)
 for r in [mp.mpf(0),location,location+1,2*location+1]:
  bound('actual-moment-supremum-'+str((q,delta,r)),function(r),maximum)
for n,expected in [(1,mp.pi/2),(2,mp.pi/2),(3,mp.pi**2/8)]:
 sphere=2*mp.pi**(mp.mpf(n)/2)/mp.gamma(mp.mpf(n)/2)
 integral=mp.quad(lambda r:sphere*r**(n-1)/(1+r*r)**(n+1),[0,mp.inf])
 add('actual-real-frequency-integrability-'+str(n),integral,expected)

result=dict(schema='AN02-regularity-bridge-checks175/v1',status='PASS' if all(r['passed'] for r in rows) else 'FAIL',
 checks=len(rows),records=rows,precision_decimal_digits=60,
 max_relative_error=max(r.get('relative_error',0) for r in rows),
 calculations_supplement_full_proofs=True,independent_agent_review=False)
(HERE/'independent-example-checks175.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
print(json.dumps({k:result[k] for k in ['status','checks','max_relative_error']}))
assert result['status']=='PASS',[(r['name'],r.get('absolute_error')) for r in rows if not r['passed']]
