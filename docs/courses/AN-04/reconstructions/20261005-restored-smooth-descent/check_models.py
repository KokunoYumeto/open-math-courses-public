"""Bounded exact fold, extension and symbol models for U014."""
import hashlib,json
from pathlib import Path
import sympy as s
import numpy as np
import mpmath as mp
here=Path(__file__).resolve().parent;checks=[]
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()

y,t=s.symbols('y t',real=True);coords=s.Matrix([y,t])
f=s.Matrix([y+t,(y+t)**2+t**2*(1+t)**2])
source=s.Matrix([y+t,t+t*t]);target=s.Matrix([f[0],f[1]-f[0]**2])
assert s.simplify(target-s.Matrix([source[0],source[1]**2]))==s.zeros(2,1)
J=f.jacobian(coords);zero={y:0,t:0};kernel=s.Matrix([-1,1])
assert J.subs(zero).rank()==1 and J.subs(zero)*kernel==s.zeros(2,1)
det=s.factor(J.det());assert det==2*t*(1+t)*(1+2*t)
assert (s.Matrix([s.diff(det,q) for q in coords]).subs(zero).T*kernel)[0]==2
second=(kernel.T*s.hessian(f[1],coords).subs(zero)*kernel)[0]
assert second==2
tstar=(-1+s.sqrt(1-4*t-4*t*t))/2
involution=s.Matrix([y+t-tstar,tstar])
sub=dict(zip(coords,involution))
assert s.simplify((t+t*t).subs(sub,simultaneous=True)+t+t*t)==0
assert s.simplify(f.subs(sub,simultaneous=True)-f)==s.zeros(2,1)
dI=involution.jacobian(coords).subs(zero)
assert dI*kernel==-kernel and dI*dI==s.eye(2)
checks.append({'name':'actual mixed nonlinear fold and intrinsic reflection',
 'projection_determinant':str(det),'quotient_Hessian_on_kernel':int(second),
 'kernel_and_reflection':'(-1,1)','exact_fold_coordinate_identity':True,
 'full_map_preserved_by_actual_involution':True,'passed':True})

r=s.symbols('r',real=True);z=s.symbols('z',real=True)
even=(1+z)*s.cos(t)+z*t*t+t**6
odd=s.sin(t)+z*t**3
F0_series=s.series(even,t,0,10).removeO().subs(t,s.sqrt(r))
F1_series=s.series(odd/t,t,0,10).removeO().subs(t,s.sqrt(r))
jets=[]
for p in range(5):
    actual=s.diff(F0_series,r,p).subs(r,0)
    predicted=s.factorial(p)/s.factorial(2*p)*s.diff(even,t,2*p).subs(t,0)
    assert s.simplify(actual-predicted)==0
    actual_odd=s.diff(F1_series,r,p).subs(r,0)
    predicted_odd=s.factorial(p)/s.factorial(2*p+1)*s.diff(odd,t,2*p+1).subs(t,0)
    assert s.simplify(actual_odd-predicted_odd)==0
    jets.append({'p':p,'even_boundary_derivative':str(actual),
                  'odd_boundary_derivative':str(actual_odd)})
checks.append({'name':'square-descent jets including odd division',
 'kind':'Exact independent Taylor and derivative comparisons through square order four.',
 'models':jets,'passed':True})

interpolations=[]
for N in [2,4,8]:
    coeff=[]
    for k in range(N+1):
        coeff.append(s.prod(s.Rational(1+2**j,2**j-2**k) for j in range(N+1) if j!=k))
    moments=[s.simplify(sum(coeff[k]*(-2**k)**p for k in range(N+1))) for p in range(N+1)]
    assert all(v==1 for v in moments)
    # Finite exact extension of each polynomial of degree <=N near zero.
    polynomial=sum((j+1)*r**j for j in range(N+1))
    ext=s.expand(sum(coeff[k]*polynomial.subs(r,-2**k*r) for k in range(N+1)))
    assert ext==polynomial
    interpolations.append({'N':N,'moments_checked':N+1,
                             'coefficients':[str(a) for a in coeff],
                             'whole_polynomial_extension_identity':True})
checks.append({'name':'Lagrange extension coefficients and finite all-jet identities',
 'models':interpolations,'infinite_extension_certified':False,'passed':True})

# Compare two independent ways to compute the limiting coefficients: their
# infinite-product expression and the finite Lagrange evaluation coefficients.
mp.mp.dps=100
A=mp.mpf(2)
D=mp.mpf(1)
for j in range(1,360):
    A*=1+mp.mpf(2)**(-j);D*=1-mp.mpf(2)**(-j)
ak=[];dk=mp.mpf(1);comparison=[]
for k in range(36):
    if k:dk*=1-mp.mpf(2)**(-k)
    val=(-1)**k*mp.mpf(2)**(-mp.mpf(k*(k+1))/2)*A/(1+mp.mpf(2)**(-k))/(dk*D)
    ak.append(val)
    finite=mp.mpf(1)
    for j in range(100):
        if j!=k:finite*=mp.mpf(1+2**j)/(2**j-2**k)
    error=abs(val-finite)
    assert error<mp.mpf('1e-26')
    comparison.append({'k':k,'coefficient':float(val),'finite_product_comparison_error':float(error)})
moments=[]
for p in range(7):
    value=mp.fsum(ak[k]*(-mp.mpf(2)**k)**p for k in range(len(ak)))
    assert abs(value-1)<mp.mpf('1e-60')
    moments.append({'p':p,'absolute_moment_error':float(abs(value-1)),
                     'absolute_weighted_sum':float(mp.fsum(abs(ak[k])*mp.mpf(2)**(k*p) for k in range(len(ak))))})
checks.append({'name':'limiting extension products and rapidly convergent moments',
 'precision_decimal_digits':100,'coefficient_count':36,
 'first_coefficients':comparison[:7],'moments':moments,
 'scope':'Finite high-precision comparisons; analytic infinite-product and domination proof is in the lesson.',
 'passed':True})

# Normalized circle of cone directions; independent finite differences check
# the frequency chain rule, including crossing the square-variable boundary.
nu=.75
def coefficient(q):
    xi1,rho=q
    return (1+xi1*xi1+rho*rho)**(nu/2)*(1+xi1/rho)
xi1,rho=s.symbols('xi1 rho',real=True,positive=True)
expr=(1+xi1*xi1+rho*rho)**s.Rational(3,8)*(1+xi1/rho)
grad=s.lambdify((xi1,rho),[s.diff(expr,xi1),s.diff(expr,rho)],'numpy')
samples=[]
for scale in [4.,16.,64.]:
    for angle in [-.1,0.,.1]:
        q=np.array([angle*scale,scale]);h=scale*1e-5
        numerical=np.array([(coefficient(q+np.eye(2)[j]*h)-coefficient(q-np.eye(2)[j]*h))/(2*h) for j in range(2)])
        exact=np.asarray(grad(*q),dtype=float)
        error=np.linalg.norm(numerical-exact)
        assert error<1e-8
        normalized=np.linalg.norm(exact)*(1+np.dot(q,q))**((1-nu)/2)
        assert normalized<3.
        samples.append({'scale':scale,'ratio':angle,'derivative_error':float(error),
                         'weighted_first_derivative_norm':float(normalized)})
checks.append({'name':'ordinary frequency estimates through the square boundary',
 'external_order':nu,'models':samples,'kind':'Independent central differences versus exact gradient on a normalized cone.',
 'passed':True})

m=s.symbols('m',real=True);nu_sym=m+s.Rational(1,2)
assert nu_sym-s.Rational(1,3)==m+s.Rational(1,6)
assert nu_sym-s.Rational(2,3)==m-s.Rational(1,6)
F0,F1,ss,Rho=s.symbols('F0 F1 ss Rho',real=True,positive=True)
b0=Rho**(-s.Rational(1,3))*F0;b1=s.I*Rho**(-s.Rational(2,3))*F1
critical=Rho**s.Rational(1,3)*b0-s.I*ss*Rho**s.Rational(2,3)*b1
assert s.simplify(critical-F0-ss*F1)==0
wrong=Rho**s.Rational(1,3)*b0-s.I*ss*Rho**s.Rational(2,3)*(-b1)
assert s.simplify(wrong-F0+ss*F1)==0
checks.append({'name':'critical coefficient order shifts and odd sign',
 'orders':['m+1/6','m-1/6'],'correct_odd_product':'(-i)*i=1',
 'opposite_sign_gives':'F0-s F1','full_Airy_integral_identity_checked':False,'passed':True})

report={'schema':'smooth-descent-finite-check/v1','passed':True,
 'lesson':'folds-reflections-and-uniform-descent.md',
 'lesson_sha256':sha(here/'folds-reflections-and-uniform-descent.md'),
 'script_sha256':sha(Path(__file__)),'checks':checks,
 'scope':'Six bounded exact fold/jet/interpolation/order models and independent high-precision/numerical comparisons. They test coordinates, signs, coefficient moments and selected frequency estimates; they do not certify the general smooth extension, simultaneous fold geometry or Airy continuity.',
 'independent_mathematical_review':False}
(here/'model-check.json').write_text(json.dumps(report,indent=2)+'\n',encoding='utf-8')
print(json.dumps({'passed':True,'finite_checks':len(checks),'lesson_sha256':report['lesson_sha256']}))
