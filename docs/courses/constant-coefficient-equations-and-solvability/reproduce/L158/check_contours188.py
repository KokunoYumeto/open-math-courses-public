"""Direct Gaussian inverse integrals and logarithmic contour/Jacobian probes."""
from pathlib import Path
import json,math
import mpmath as mp
mp.mp.dps=65;HERE=Path(__file__).resolve().parent;rows=[]
def equal(name,value,expected,tol=1e-42):
 error=abs(value-expected);scale=max(1,abs(expected))
 absolute=float(error)
 rows.append(dict(name=name,absolute_error=absolute if math.isfinite(absolute)else mp.nstr(error,15),relative_error=float(error/scale),
  tolerance=tol,passed=bool(error<=mp.mpf(str(tol))*scale)))
def less(name,value,bound,tol=1e-45):
 rows.append(dict(name=name,actual=float(value),bound=float(bound),
  tolerance=tol,passed=bool(value<=bound+mp.mpf(str(tol)))))
R=mp.mpf(2);x=mp.mpf(1)
for eps in [mp.mpf('.3'),mp.mpf(1)]:
 for order in [0,1,2]:
  def integrand(t):
   ell=mp.log(2+t*t);z=t+1j*R*ell;J=1+1j*R*2*t/(2+t*t)
   return z**order*mp.exp(1j*x*z-eps*z*z)*J
  positive=mp.quad(integrand,[0,1,2,4,8,16,32,mp.inf])
  total=2*positive.real if order%2==0 else 2j*positive.imag
  q=lambda y:mp.exp(-y*y/(4*eps))/mp.sqrt(4*mp.pi*eps)
  target=(-1j)**order*mp.diff(q,x,order)
  equal('actual-shifted-Gaussian-inverse-D'+str(order)+'-epsilon'+str(eps),total/(2*mp.pi),target)
for radius in [mp.mpf(2),mp.mpf(4),mp.mpf(9)]:
 for x in [mp.mpf('.5'),mp.mpf(1)]:
  R=mp.mpf(2)
  def f(t):
   ell=mp.log(2+t*t);z=t+1j*R*ell
   return mp.exp(1j*x*z)*(1+1j*R*2*t/(2+t*t))
  direct=mp.quad(f,[-radius,0,radius])/(2*mp.pi)
  boundary=(2+radius*radius)**(-R*x)*mp.sin(x*radius)/(mp.pi*x)
  equal('unregularized-atom-actual-finite-contour-boundary-'+str((radius,x)),direct,boundary)
for R in [mp.mpf(2),mp.mpf(5),mp.mpf(20)]:
 for r in [mp.mpf(0),mp.mpf('.2'),mp.mpf('.7'),mp.mpf(1),mp.mpf(9),mp.mpf(50)]:
  ell=mp.log(2+r*r);z=r+1j*R*ell
  less('actual-final-contour-logarithmic-strip-'+str((R,r)),abs(z.imag),mp.ceil(2*R)*mp.log(1+abs(z)))
  less('actual-Jacobian-bound-'+str((R,r)),abs(1+1j*R*2*r/(2+r*r)),1+R)
  for eps in [mp.mpf('.25'),mp.mpf(1)]:
   equal('actual-complex-Gaussian-modulus-'+str((R,r,eps)),
    abs(mp.exp(-eps*z*z)),mp.exp(-eps*r*r+eps*R*R*ell*ell))
for m in [1,3,10]:
 for real in [mp.mpf(4),mp.mpf(20),mp.mpf(300)]:
  z=real+1j*mp.mpf('.5')*m*mp.log(1+real)
  for t in [mp.mpc(0,2),mp.mpc('-1.2','.8')]:
   w=z+t
   less('actual-width-after-bounded-polynomial-displacement-'+str((m,real,t)),
    abs(w.imag),(2*m+3)*mp.log(1+abs(w)))
for z in [mp.mpc(0,0),mp.mpc('.4','.3'),mp.mpc(2,-1),mp.mpc(-3,2)]:
 direct=mp.quad(lambda t:(1-abs(t))*mp.exp(-1j*t*z),[-1,0,1])
 closed=1 if z==0 else 2*(1-mp.cos(z))/(z*z)
 equal('actual-triangle-Fourier-integral-'+str(z),direct,closed)
 masses=-mp.exp(1j*z)+2-mp.exp(-1j*z)
 equal('actual-D2-triangle-point-mass-sign-'+str(z),z*z*direct,masses)
for j in [1,10,100]:
 Rj=2*mp.pi*j;s=mp.log(Rj)
 less('actual-triangle-persistent-zero-residual-'+str(j),abs(2*(1-mp.cos(Rj))/(Rj*Rj)),mp.mpf('1e-50'))
 for eta in [mp.mpf(-2),mp.mpf('-.3'),mp.mpf('.3'),mp.mpf(2)]:
  z=Rj+1j*s*eta
  direct=mp.log(abs(2*(1-mp.cos(z))/(z*z)))/s
  closed=(mp.log(4)+2*mp.log(abs(mp.sinh(s*eta/2)))-mp.log(Rj*Rj+s*s*eta*eta))/s
  equal('actual-triangle-complex-profile-'+str((j,eta)),direct,closed)
assert all(r['passed']for r in rows),[r for r in rows if not r['passed']]
record=dict(schema='AN02-original-logarithmic-contour-checks188/v1',status='PASS',checks=len(rows),
 records=rows,precision_decimal_digits=65,maximum_relative_error=max(r.get('relative_error',0)for r in rows),
 numerical_scope='Actual complex logarithmic-cycle Gaussian Fourier inverses for delta and its first two D derivatives; actual finite unregularized integrals and independent endpoint evaluations; strip inclusion,exact complex Gaussian moduli,Jacobian and bounded-displacement strip widths;direct physical triangular-function Fourier integrals,point-mass signs,persistent zeros and exact complex profiles.',
 checks_are_proof_supplements=True,full_all_dimensions_and_all_derivative_orders_proof_in_formal_text=True,
 no_finite_numerical_probe_claimed_as_general_support_or_compactness_proof=True)
(HERE/'independent-contour-checks188.json').write_text(json.dumps(record,indent=2,allow_nan=False)+'\n',encoding='utf-8')
print(json.dumps(dict(status='PASS',checks=len(rows),maximum_relative_error=record['maximum_relative_error'])))
