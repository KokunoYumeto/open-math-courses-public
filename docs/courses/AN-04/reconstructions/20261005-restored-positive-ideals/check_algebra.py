"""All eight original finite model families; historical state operations omitted."""
import json,math
import numpy as np
import sympy as s
from scipy.integrate import quad
def zero(v):return s.simplify(v)==0
def zeros(M):return all(zero(v) for v in M)
checks=[]
def record(name,detail):checks.append({'name':name,'passed':True,'scope':detail})

r,p,q,t=s.symbols('r p q t',positive=True,real=True)
z,w=s.symbols('z w',real=True);x1,x2,x3=s.symbols('x1 x2 x3',real=True)
xi=s.Matrix([r,z]);xx=s.Matrix([x1,x2]);H=2*r+z**2/(2*r)
grad=s.Matrix([s.diff(H,v) for v in xi]);gens=xx-grad
assert zero((xi.dot(grad)-H))
assert zeros(s.hessian(H,xi)*xi)
assert zeros(gens.jacobian(xx)-s.eye(2))
pb=sum(s.diff(gens[0],xi[j])*s.diff(gens[1],xx[j])-s.diff(gens[0],xx[j])*s.diff(gens[1],xi[j]) for j in range(2))
assert zero(pb) and zero(H.subs({r:t*r,z:t*z})-t*H)
assert s.diff(r,r)==1 and zero(s.diff(r,r).subs(r,t*r)-1)
record('Degree-one generating graph and Poisson closure','Full rational gradient/Hessian/Euler/complex generator matrix; H=r gives a nonzero degree-zero gradient, contradicting the source degree-zero statement.')

Hp=-s.I*z**2/(2*r);B=s.hessian(Hp,xi)
assert zero(xi.dot(s.Matrix([s.diff(Hp,v) for v in xi]))-Hp)
B0=B.subs(z,0);metric=-2*s.im(B0)
assert metric==s.diag(0,2/r) and metric.rank()==1
assert zeros(B*xi)
phi=x1*r+x2*z+s.I*z**2/(2*r)
G=s.Matrix([s.diff(phi,v) for v in xi])
assert zeros(G.jacobian(xx)-s.eye(2))
Phi=s.hessian(phi,[x1,x2,r,z])
assert zero((Phi/s.I).det()-1)
assert zeros(s.Matrix([s.diff(phi,v) for v in xx])-xi)
record('Non-strict positive conic phase','Exact phase and entire Fourier Hessian, determinant det(Phi/i)=1, complex nondegeneracy, degree-one H and real radial Hermitian null direction.')

Hcross=-s.I*z**2*w**2/r**3;v3=s.Matrix([r,z,w]);Bc=s.hessian(Hcross,v3)
assert zero(Hcross.subs({r:t*r,z:t*z,w:t*w})-t*Hcross)
gc=s.Matrix([s.diff(Hcross,v) for v in v3])
assert zeros(gc.subs(z,0)) and zeros(gc.subs(w,0))
assert zeros(Bc.subs({z:0,w:0}))
assert Bc.subs(z,0).rank()==1 and Bc.subs(w,0).rank()==1
assert -2*s.im(Bc.subs(z,0))==s.diag(0,4*w**2/r**3,0)
assert -2*s.im(Bc.subs(w,0))==s.diag(0,0,4*z**2/r**3)
record('Nonsmooth real zero set and changing positive rank','Negative imaginary quartic product produces two angular axes meeting, positive tangent rank one away from their intersection and rank zero at it; no strict imaginary Hessian is assumed.')

Hbad=s.I*z**3/r**2
assert zeros(s.hessian(Hbad,xi).subs(z,0))
assert zeros(s.Matrix([s.diff(Hbad,v) for v in xi]).subs(z,0))
assert s.im(Hbad.subs({r:1,z:1}))==1 and s.im(Hbad.subs({r:1,z:-1}))==-1
assert s.diff(Hbad,z,3).subs(z,0)==6*s.I/r**2
assert zero(s.im(s.diff(Hbad,z))-3*z**2/r**2)
record('Positive real-zero tangents do not imply a positive ideal','All tangent imaginary Hessians vanish on the real zero set of the cubic H, while ImH changes sign. Flat ambiguity with |ImHprime|=O(z^2) cannot change the cubic coefficient.')

x,eta,b,eps=s.symbols('x eta b eps',real=True,positive=True)
rho=s.symbols('rho',positive=True,real=True)
cgauss=1+s.I*b
ph=x*rho+cgauss*eta**2/(2*rho)+s.I*eps*rho*x**2/2
reduced=x*rho+s.I*eps*rho*x**2/2
assert zero(ph-reduced-cgauss*eta**2/(2*rho))
assert s.diff(ph,eta,2)==cgauss/rho
G=s.Matrix([s.diff(ph,rho),s.diff(ph,eta)])
assert G.jacobian([x,eta]).subs({x:0,eta:0})==s.diag(1,cgauss/rho)
Ph0=s.hessian(ph,[x,rho,eta]).subs({x:0,eta:0})
assert zero((Ph0/s.I).det()-(b-s.I)/rho)
assert zero(s.im(ph)-(b*eta**2/(2*rho)+eps*rho*x**2/2))
for bv in [0.1,0.5,1.0,3.0]:
 for rv in [0.7,1.0,2.3]:
  coeff=(bv-1j)/(2*rv)
  actual=quad(lambda u:np.real(np.exp(-coeff*u*u)),-np.inf,np.inf,epsabs=1e-11)[0]+1j*quad(lambda u:np.imag(np.exp(-coeff*u*u)),-np.inf,np.inf,epsabs=1e-11)[0]
  expected=(2*np.pi*rv)**0.5*(bv-1j)**(-0.5)
  assert abs(actual-expected)<2e-10*max(1,abs(expected)),(bv,rv,actual,expected)
record('Partial positive-phase elimination and Gaussian branch','Whole nondegenerate model with eta eliminated, exact determinant (b-i)/rho, both signs and homogeneity, plus twelve independently integrated damped Gaussians verifying sqrt(rho)(b-i)^(-1/2).')

n,N,m,j,L=s.symbols('n N m j L')
mu=m+(n-2*N)/4;sigma=m-n/4
assert zero(mu+(N-n)/2-j-(sigma-j))
assert zero(-(n+2*N)/4+(n+N)/2-n/4)
assert zero(mu+N-(n+N)/2-L-(sigma-L))
assert zero((m+(n-2*(N-1))/4)-mu-s.Rational(1,2))
for dim in range(1,5):
 D=s.diag(*range(1,dim+1));P=s.BlockMatrix([[s.zeros(dim),s.eye(dim)],[s.eye(dim),-s.I*D]]).as_explicit()
 assert zero((P/s.I).det()-1)
record('All representation orders, constants and normal-phase blocks','Symbolic n,N,m,j,L accounting verifies (2pi)^(n/4), sigma-j and sigma-L, the half-order after eliminating one variable, and four full normal-phase determinant blocks.')

u=s.symbols('u',positive=True,real=True);flat=s.exp(-1/u**2)
for order in range(6):
 coefficient=s.simplify(s.diff(flat,u,order)/flat)
 assert s.Poly(s.expand(coefficient.subs(u,1/t)),t) is not None
for K in [1,2,4,8,16]:
 peak=(K/2)**(K/2)*math.exp(-K/2)
 for uv in [0.03,0.08,0.2,0.5,1.,2.]:
  assert math.exp(-1/uv**2)*uv**(-K)<=peak*(1+1e-12)
for power in range(1,9):
 assert zero(s.diff(t**power*s.exp(-t),t).subs(t,power))
record('Flat angular coefficients and exponential damping','Six complete derivative polynomials and the exact all-power maximum formula support flat ideal coefficients; eight damping maxima retain all-order mechanism rather than a finite closure claim.')

annular_halfwidth=.2
def bump(u):
 if abs(u)>=annular_halfwidth:return 0.
 return math.exp(-1/(1-(u/annular_halfwidth)**2))
normal=quad(bump,-annular_halfwidth,annular_halfwidth,epsabs=1e-13)[0]
assert normal>0
def chi(ratio):return bump(math.log(ratio))/normal
for rv in [2.,10.,100.]:
 value=quad(lambda tt:chi(rv/tt)/tt,rv*math.exp(-annular_halfwidth),rv*math.exp(annular_halfwidth),epsabs=1e-12)[0]
 assert abs(value-1)<2e-12
 for muv in [-2.,-.5,0.,1.25]:
  actual=quad(lambda tt:tt**muv*chi(rv/tt)/tt,rv*math.exp(-annular_halfwidth),rv*math.exp(annular_halfwidth),epsabs=1e-10,epsrel=1e-12)[0]
  moment=quad(lambda uu:math.exp(-muv*uu)*bump(uu)/normal,-annular_halfwidth,annular_halfwidth,epsabs=1e-12)[0]
  assert abs(actual-rv**muv*moment)<3e-11*max(1,abs(actual))
record('Actual smooth annular Mellin partition and orders','A C-infinity logarithmic bump normalized in dt/t is checked at three radii and twelve positive/negative symbol orders. Its annulus always has t comparable to the frequency; this is a model of uniform symbol division, not its proof.')

assert len(checks)==8 and all(r['passed'] for r in checks)
print(json.dumps({'passed':True,'finite_model_groups':len(checks),'no_course_or_source_writes':True}))
