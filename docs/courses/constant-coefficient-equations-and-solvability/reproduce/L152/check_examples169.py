"""Independent actual integrations, derivatives, root products and real metrics."""
from pathlib import Path
import json
import numpy as np
import mpmath as mp
mp.mp.dps=55
HERE=Path(__file__).resolve().parent
rows=[]
def add(name,actual,expected,tol=1e-10):
 error=float(abs(actual-expected));scale=max(1,float(abs(expected)))
 rows.append(dict(name=name,absolute_error=error,relative_error=error/scale,
                  tolerance=tol,passed=error<=tol*scale))

# Integrate the actual normal Laplacian over its four-dimensional ball slices.
for r,delta in [(mp.mpf(a),mp.mpf(b)) for a,b in
 [('0.2','0.7'),('1','0.1'),('2','0.3'),('0.8','0.03'),('4','1'),('1','2')]]:
 actual=mp.quad(lambda rho:2*delta**2/(rho**2+delta**2)**2 *
           (mp.pi*(r*r-rho*rho))*(2*mp.pi*rho),[0,r])
 expected=2*mp.pi**2*(r*r-delta**2*mp.log(1+r*r/delta**2))
 add('normal-ball-mass-'+str(r)+'-'+str(delta),actual,expected,1e-40)

# Differentiate the actual scalar log regularization in its real normal plane.
for x,y,d in [(.2,.3,.4),(-.6,.1,.2),(0,0,.3),(.7,-.5,1)]:
 q=lambda u,v:mp.log(u*u+v*v+d*d)/2
 lap=mp.diff(q,(x,y),(2,0))+mp.diff(q,(x,y),(0,2))
 add('normal-real-laplacian-'+str((x,y,d)),lap,
     2*d*d/(x*x+y*y+d*d)**2,1e-12)

# Full real graph Jacobians and independent area integration over the ball.
for u,v in [(0,0),(.2,.7),(-.8,.3),(1.5,-.9),(.4,-1.1)]:
 matrix=np.array([[1,0],[0,1],[2*u,-2*v],[2*v,2*u]],float)
 jac=np.sqrt(np.linalg.det(matrix.T@matrix))
 add('full-4x2-Gram-'+str((u,v)),jac,1+4*(u*u+v*v),1e-13)
for r in [mp.mpf(v) for v in ['.1','.3','.7','1','2','5','12']]:
 b=(mp.sqrt(1+4*r*r)-1)/2
 area=mp.quad(lambda rho:2*mp.pi*rho*(1+4*rho*rho),[0,mp.sqrt(b)])
 add('actual-curved-surface-area-'+str(r),area,mp.pi*(2*r*r-b),1e-40)
 rows.append(dict(name='degree-bound-'+str(r),passed=area<=2*mp.pi*r*r))
for gamma in [.7+.3j,2-1j,-.2+1.4j]:
 g=mp.mpc(gamma);r=mp.mpf('1.3')
 # Actual real derivative of Gamma(y)=(gamma*y,y).
 matrix=np.array([[gamma.real,-gamma.imag],[gamma.imag,gamma.real],[1,0],[0,1]])
 jac=np.sqrt(np.linalg.det(matrix.T@matrix));radius=r/mp.sqrt(1+abs(g)**2)
 area=mp.quad(lambda rho:jac*2*mp.pi*rho,[0,radius])
 add('affine-slope-area-'+str(gamma),area,mp.pi*r*r,1e-13)

# Source polynomial transformed directly; actual jets and numerical root products.
for a,b in [(0j,0j),(3+.2j,0j),(-.4+.9j,.2-.3j),(8-2j,4+.7j)]:
 aa,bb=mp.mpc(a),mp.mpc(b);sigma=1/(1+mp.sqrt(abs(aa)**2+abs(bb)**2))
 transformed=lambda x,y:(aa+x)**2-(bb+sigma*y)
 strength=abs(transformed(0,0))**2+abs(mp.diff(lambda x:transformed(x,0),0))**2
 strength+=abs(mp.diff(lambda y:transformed(0,y),0))**2
 strength+=abs(mp.diff(lambda x:transformed(x,0),0,2))**2
 add('actual-transformed-jets-'+str((a,b)),strength,
     abs(aa*aa-bb)**2+4*abs(aa)**2+4+sigma*sigma,1e-40)
 for yy in [.1+.2j,-.6+.3j,.7-.5j]:
  roots=np.roots([1,2*a,a*a-b-float(sigma)*yy])
  add('actual-root-discriminant-'+str((a,b,yy)),
       (roots[0]-roots[1])**2,4*(b+float(sigma)*yy),1e-11)

# Safe circles at central multiple zeros: integrate the actual analytic quotient.
for m in [1,2,3,5]:
 root_list=[0]*m
 for radius in [.15,.21]:
  angles=2*np.pi*np.arange(2048)/2048
  t=radius*np.exp(1j*angles)
  g=lambda z:1+(.3+.2j)*z+z*z
  q=t**m;num=q*g(t)
  add('safe-circle-quotient-'+str((m,radius)),np.mean(num/q),g(0),1e-12)

# Actual surface-density integration, with full Gram area, on a complex disk.
nodes,weights=np.polynomial.legendre.leggauss(48)
beta=.5+.25j;s=.36
radial=(nodes+1)*s/2;rw=weights*s/2
angles=2*np.pi*np.arange(512)/512
y=beta+radial[:,None]*np.exp(1j*angles)[None,:]
jac=1+4*np.abs(y)**2;density=1/(np.pi*s*s*jac)
for x1,x2 in [(0,0),(.8,-.3),(-1.5,.7),(2.1,1.4),(-.4,-1.2)]:
 kernel=np.exp(1j*(x1*y+x2*y*y))
 actual=np.sum(rw*radial*np.mean(density*jac*kernel,axis=1)*2*np.pi)
 expected=np.exp(1j*(x1*beta+x2*beta*beta))
 add('actual-curved-density-mean-'+str((x1,x2)),actual,expected,1e-12)
 alpha=mp.mpc('.3','-.2');be=mp.mpc(beta)
 mode=lambda a,b:(1+alpha*a)*mp.exp(1j*(a*be+b*be*be))
 first=-1j*mp.diff(mode,(x1,x2),(0,1))+mp.diff(mode,(x1,x2),(2,0))
 add('actual-single-factor-mode-'+str((x1,x2)),first,
     2j*alpha*be*mp.exp(1j*(x1*be+x2*be*be)),1e-40)
 repeated=-mp.diff(mode,(x1,x2),(0,2))-2j*mp.diff(mode,(x1,x2),(2,1))
 repeated+=mp.diff(mode,(x1,x2),(4,0))
 add('actual-repeated-factor-mode-'+str((x1,x2)),repeated,0,1e-40)

for s in [mp.mpf(v) for v in ['.2','.5','1','2']]:
 norm=mp.quad(lambda r:2*mp.pi*r/(mp.pi**2*s**4*(1+4*r*r)),[0,s])
 add('actual-density-L2-'+str(s),norm,mp.log(1+4*s*s)/(4*mp.pi*s**4),1e-40)

# Repeated characteristic point: actual real derivatives and tested Fourier jets.
la=mp.mpc(1,.5);A=mp.mpc(1);B=mp.mpc(2,-1);C=mp.mpc(0,-.5)
tau=mp.mpc(1,1);e=tau/abs(tau)
mode=lambda x:(A+B*x+C*x*x)*mp.exp(1j*la*x)
for x in [-1,-.3,0,.7,1.2]:
 third=1j*mp.diff(mode,x,3)+3*la*mp.diff(mode,x,2)
 third-=3j*la*la*mp.diff(mode,x,1)+la**3*mode(x)
 add('actual-cubic-operator-'+str(x),third,0,1e-40)
 density_sum=sum((x*tau)**a*v for a,v in enumerate([A,B/tau,C/tau**2]))*mp.exp(1j*la*x)
 add('complex-direction-density-'+str(x),density_sum,mode(x),1e-40)
v=lambda x:mp.exp(-1/(1-x*x)) if abs(x)<1 else mp.mpf(0)
transform=lambda z:mp.quad(lambda x:v(x)*mp.exp(-1j*x*z),[-1,0,1])
jets=[mp.diff(transform,-la,a) for a in range(3)]
tested=mp.quad(lambda x:v(x)*mode(x),[-1,0,1])
add('actual-tested-forward-signs',A*jets[0]+1j*B*jets[1]-C*jets[2],tested,1e-38)
intermediate=[(1j)**a*e**(-a)*coeff for a,coeff in enumerate([A,B,C])]
for a,coeff in enumerate([A,B,C]):
 add('unit-direction-reflection-'+str(a),(-1j)**a*abs(tau)**(-a)*intermediate[a],
     coeff/tau**a,1e-40)

result=dict(schema='AN02-surface-independent-checks169/v1',status='PASS' if all(r['passed'] for r in rows) else 'FAIL',
 checks=len(rows),records=rows,precision_decimal_digits=55,
 max_relative_error=max(r.get('relative_error',0) for r in rows),
 calculations_supplement_full_proof=True,independent_agent_review=False)
(HERE/'independent-example-checks169.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
print(json.dumps({k:result[k] for k in ['status','checks','max_relative_error']}))
assert result['status']=='PASS',[(r['name'],r.get('absolute_error')) for r in rows if not r['passed']]
