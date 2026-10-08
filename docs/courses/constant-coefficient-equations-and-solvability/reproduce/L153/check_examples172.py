"""Actual compact-test transforms, contour homotopies, norms and Hessians."""
from pathlib import Path
import json
import numpy as np
import mpmath as mp
mp.mp.dps=55
HERE=Path(__file__).resolve().parent;rows=[]
def add(name,actual,expected,tol=1e-11):
 err=float(abs(actual-expected));scale=max(1,float(abs(expected)))
 rows.append(dict(name=name,absolute_error=err,relative_error=err/scale,tolerance=tol,passed=err<=tol*scale))
def bound(name,actual,limit,upper=True,slack=1e-12):
 a=float(actual);l=float(limit)
 rows.append(dict(name=name,actual=a,bound=l,upper_bound=upper,
                  passed=a<=l+slack if upper else a+slack>=l))
def bump(x):
 x=np.asarray(x);y=np.zeros_like(x,dtype=float);inside=np.abs(x)<.25
 y[inside]=np.exp(1-1/(1-16*x[inside]**2));return y
bn,bw=np.polynomial.legendre.leggauss(420)
bx=bn*.25;bw=bw*.25;bb=bump(bx);bweighted=bw*bb
def transform(z):
 z=np.asarray(z,dtype=complex);out=np.empty(z.shape,dtype=complex)
 flat=z.ravel();target=out.ravel()
 for start in range(0,len(flat),600):
  target[start:start+600]=np.exp(-1j*flat[start:start+600,None]*bx[None,:])@bweighted
 return out
b1=float(np.sum(bweighted));b2=float(np.sum(bw*bb*bb))

# The actual compact smooth bump on the actual curved complex contour.
nodes,weights=np.polynomial.legendre.leggauss(48)
centers=np.arange(-1095,1100,10)
xi=(centers[:,None]+5*nodes[None,:]).ravel()
rw=np.tile(5*weights,len(centers))
for R in [0,.35,.8]:
 z=xi+1j*R*np.log(2+xi*xi)
 jac=1+1j*2*R*xi/(2+xi*xi);fz=transform(z)
 for x in [0,.12,2]:
  integral=np.sum(rw*fz*np.exp(1j*x*z)*jac)/(2*np.pi)
  expected=float(bump(np.asarray([x]))[0])
  add('actual-compact-bump-contour-'+str((R,x)),integral,expected,2e-7)

# Real-plane Plancherel checked against an independent physical-space integral.
for eta in [-1.3,-.2,0,.7,2]:
 fz=transform(xi+1j*eta)
 plane=float(np.sum(rw*np.abs(fz)**2))
 physical=float(2*np.pi*np.sum(bw*bb*bb*np.exp(2*bx*eta)))
 add('actual-shifted-plane-Plancherel-'+str(eta),plane,physical,3e-9)
for z in [0j,.5+.3j,-2+.8j,4-1.1j,12+2j]:
 fz=abs(transform(np.asarray([z]))[0])
 bound('actual-support-growth-'+str(z),fz,b1*np.exp(.25*abs(z.imag)))

# Actual derivatives of the compact bump and its translated/amplitude responses.
mb=lambda x:mp.exp(1-1/(1-16*x*x))
add('actual-bump-center-second-derivative',mp.diff(mb,0,2),-32,1e-40)
for j in [1,3,5,9]:
 amplitude=mp.mpf(2)**(-j);center=mp.mpf(j)+mp.mpf('.5')
 profile=lambda x:amplitude*mb(x-center)
 add('actual-moving-height-'+str(j),profile(center),amplitude,1e-40)
 add('actual-moving-derivative-'+str(j),mp.diff(profile,center,2),-32*amplitude,1e-40)
 add('actual-locally-weighted-height-'+str(j),mp.mpf(2)**j*profile(center),1,1e-40)

# Exact complex determinants in several dimensions, evaluated as matrices.
rng=np.random.default_rng(172)
for n in [1,2,3,4]:
 for R in [.2,1,3]:
  point=rng.normal(size=n);eta=rng.normal(size=n);eta/=np.linalg.norm(eta)
  grad=2*point/(2+point@point)
  matrix=np.eye(n)+1j*R*np.outer(eta,grad)
  add('actual-complex-Jacobian-'+str((n,R)),np.linalg.det(matrix),1+1j*R*(eta@grad),1e-13)

# Differentiate both sides of the full homotopy identity, without simplification.
eta=[mp.mpf('.6'),mp.mpf('.8')]
H=lambda z:mp.exp(-z[0]**2-z[1]**2)*(1+mp.mpf('.3')*z[0]*z[1])
for point in [(mp.mpf('.2'),mp.mpf('-.4')),(mp.mpf('1.1'),mp.mpf('.7'))]:
 for R in [mp.mpf('.2'),mp.mpf('.9')]:
  for s in [mp.mpf(0),mp.mpf('.4'),mp.mpf('.8')]:
   def pullback(ss):
    ell=mp.log(2+sum(x*x for x in point))
    z=[point[l]+1j*ss*R*eta[l]*ell for l in range(2)]
    dot=sum(eta[l]*2*point[l]/(2+sum(x*x for x in point)) for l in range(2))
    return H(z)*(1+1j*ss*R*dot)
   left=mp.diff(pullback,s);right=mp.mpc(0)
   for l in range(2):
    def flux(value):
     p=list(point);p[l]=value;ell=mp.log(2+sum(x*x for x in p))
     z=[p[k]+1j*s*R*eta[k]*ell for k in range(2)]
     return 1j*R*eta[l]*ell*H(z)
    right+=mp.diff(flux,point[l])
   add('actual-homotopy-derivatives-'+str((point,R,s)),left,right,1e-40)

# Independent real differentiation of the radial and full seed functions.
def correction(t,y):return mp.sqrt(t*t+y*y)/mp.sqrt(t)-(t*t+y*y)**mp.mpf('.25')
for t,a in [(mp.mpf('4096'),mp.mpf(2)),(mp.mpf('65536'),mp.mpf(4))]:
 for ratio in [mp.mpf(v) for v in ['.01','.1','.4','1','3','10']]:
  y=t*ratio;s=t*t+y*y;q=t*t/s
  radial=mp.diff(lambda u:correction(t,u),y,2)
  add('actual-radial-Hessian-'+str((t,ratio)),radial*s**mp.mpf('.75'),
      q**mp.mpf('.75')+mp.mpf('.25')-mp.mpf('.75')*q,1e-40)
  for real in [mp.mpf(0),t/mp.mpf(2)]:
   seed=lambda x,v:abs(v)-a*mp.log(t*t+x*x+v*v)+correction(t,v)
   levi=(mp.diff(seed,(real,y),(2,0))+mp.diff(seed,(real,y),(0,2)))/4
   exact=(q**mp.mpf('.75')+mp.mpf('.25')-mp.mpf('.75')*q)/4
   exact-=a*t*t*s**mp.mpf('.75')/(t*t+real*real+y*y)**2
   add('actual-full-seed-Levi-'+str((t,ratio,real)),levi*s**mp.mpf('.75'),exact,1e-40)
   bound('strict-full-seed-lower-'+str((t,ratio,real)),levi*s**mp.mpf('.75'),mp.mpf(1)/32,upper=False)

# Explicit weight: integrate the actual positive norm, with a certified tail bound.
en,ew=np.polynomial.legendre.leggauss(900);ey=en*40;ew=ew*40
phi=np.sqrt(1+ey*ey)-(1+ey*ey)**.25
physical_inner=np.exp(2*ey[:,None]*bx[None,:])@(bw*bb*bb)
norm=float(2*np.pi*np.sum(ew*np.exp(-2*phi)*physical_inner))
tail_bound=float(2*np.pi*np.e**2*np.exp(-40)) # Rigorous ||b||_2^2<=1/2.
bound('actual-explicit-weighted-norm-bound',norm+tail_bound,4*np.pi*np.e**2*b2)
for y in [-20,-2,-.1,0,.4,3,15]:
 yy=mp.mpf(y)
 pv=correction(mp.mpf(1),yy)
 grad=mp.diff(lambda r:correction(mp.mpf(1),r),yy)
 levi=mp.diff(lambda r:correction(mp.mpf(1),r),yy,2)/4
 bound('explicit-gradient-'+str(y),abs(grad),1)
 bound('explicit-curvature-'+str(y),levi,mp.mpf(1)/16*(1+yy*yy)**(-mp.mpf('.75')),upper=False)
 bound('explicit-growth-'+str(y),pv,mp.mpf('.75')*abs(yy)-1,upper=False)
 for left,right in [(-.4,.45),(.1,.3),(-.3,-.1)]:
  support=max(mp.mpf(left)*yy,mp.mpf(right)*yy)
  bound('noncentered-support-'+str((y,left,right)),pv-support,-1,upper=False)

result=dict(schema='AN02-smooth-topology-checks172/v1',status='PASS' if all(r['passed'] for r in rows) else 'FAIL',
 checks=len(rows),records=rows,precision_decimal_digits=55,
 compact_transform_quadrature=dict(physical_nodes=420,contour_nodes=len(xi),real_cutoff=1100,
   method='Composite48-point Gauss-Legendre on length10 intervals, resolving the central logarithmic branch scale'),
 explicit_weighted_norm_squared=norm,certified_imaginary_tail_bound=tail_bound,
 exact_tail_bound_formula='2*pi*e^2*exp(-40), using 0<=b<=1 on an interval of length1/2',
 bump_L2_squared=b2,max_relative_error=max(r.get('relative_error',0) for r in rows),
 calculations_supplement_full_proofs=True,independent_agent_review=False)
(HERE/'independent-example-checks172.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
print(json.dumps({k:result[k] for k in ['status','checks','max_relative_error','explicit_weighted_norm_squared']}))
assert result['status']=='PASS',[(r['name'],r.get('absolute_error')) for r in rows if not r['passed']]
