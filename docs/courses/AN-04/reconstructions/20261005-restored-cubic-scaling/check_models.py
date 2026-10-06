"""Exact weighted phases and independent integral models for U013."""
import hashlib,json
from pathlib import Path
import sympy as s
import numpy as np
from scipy.integrate import quad
here=Path(__file__).resolve().parent;checks=[]
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
x1,x2,z,w,e1,e2=s.symbols('x1 x2 z w e1 e2',real=True)
r=s.symbols('r',positive=True)
X1,X2,Z,W,J1,J2=s.symbols('X1 X2 Z W J1 J2',real=True)
v=[x1,x2,z,w,e1,e2]
angular=e2/e1
cubic=z**3+2*z*z*w-3*z*w*w+w**3
h=e1*(cubic+x1*z*z+x2*z*w+z*angular**2+angular**3+(z+w)**4)
marked={x1:0,x2:0,z:0,w:0,e1:1,e2:0}
assert h.subs(marked)==0
assert all(s.diff(h,a).subs(marked)==0 for a in v)
assert all(s.diff(h,a,b).subs(marked)==0 for a in v for b in v)
phase=x1*e1+x2*e2+h
scaled=phase.subs({x1:X1/r**3,x2:X2/r**3,z:Z/r**2,w:W/r**2,
                  e1:r**6+r**3*J1,e2:r**3*J2},simultaneous=True)
residual=s.cancel(scaled-r**3*X1-X1*J1-X2*J2)
Q=Z**3+2*Z*Z*W-3*Z*W*W+W**3
assert s.simplify(s.limit(residual,r,s.oo)-Q)==0
assert s.simplify(s.limit(r*(residual-Q),r,s.oo)-(X1*Z*Z+X2*Z*W))==0
checks.append({'name':'full homogeneous weighted Taylor model',
 'frequency_count':2,'zero_two_jet_checked':True,
 'surviving_cubic':str(Q),'leading_mixed_error':'(X1 Z^2 + X2 Z W)/r, with T=r^3',
 'quartic_and_angular_terms_included':True,'passed':True})

eta=s.symbols('eta',positive=True);x=s.symbols('x',real=True)
O=s.zeros(2).row_join(-s.eye(2)).col_join(s.eye(2).row_join(s.zeros(2)))
output=s.Matrix([x,z,eta,w*w*eta]);input_=s.Matrix([x+z*w*w,w,eta,-2*z*w*eta])
variables=[x,z,w,eta]
sigma=output.jacobian(variables).T*O*output.jacobian(variables)
assert s.simplify(sigma-input_.jacobian(variables).T*O*input_.jacobian(variables))==s.zeros(4)
assert sigma.subs({w:0,eta:1}).rank()==2 and sigma.subs({w:1,eta:1}).rank()==4
toy=(x+z*w*w)*eta
actual=s.expand(toy.subs({x:X1/r**3,z:Z/r**2,w:W/r**2,eta:r**6+r**3*J1},simultaneous=True))
assert s.expand(actual-(r**3*X1+X1*J1+Z*W**2+J1*Z*W**2/r**3))==0
T=s.symbols('T',positive=True)
flat_scaled=T**2*(X1/T)*(1+J1/T)
incorrect_subtraction=T**2*(X1/T)*(1+J1/T**2)
assert s.expand(flat_scaled-incorrect_subtraction)==X1*J1-X1*J1/T
assert s.limit(flat_scaled-incorrect_subtraction,T,s.oo)==X1*J1
checks.append({'name':'actual changing-rank canonical phase and the flat subtraction test',
 'common_ranks_at_w_0_and_1':[2,4],
 'scaled_phase':'T X + X zeta + Z W^2 + T^(-1) zeta Z W^2',
 'flat_source_subtraction_mismatch':'X zeta (1-1/T) does not tend to zero',
 'source_observation_status':'Author consistency observation; no official erratum claimed.',
 'passed':True})

m,eps=s.symbols('m eps',real=True);kappa=s.Rational(2,3);norm_models=[]
for n,a,b in [(1,0,0),(1,1,1),(2,2,1),(1,0,3),(3,4,0)]:
    k=a+b;mu=m+s.Rational(k,4)
    inp=-(n+kappa*b)/2;out=2*mu-kappa*b-(n+kappa*a)/2
    difference=s.simplify(out-inp)
    assert difference==2*m+s.Rational(k,6)
    assert difference.subs(m,-s.Rational(k,12))==0
    assert difference.subs(m,-s.Rational(k,12)+eps)==2*eps
    norm_models.append({'n':n,'a':a,'b':b,'input_exponent':str(inp),
                        'output_exponent':str(out),'ratio_exponent':str(difference)})
checks.append({'name':'distinct input and output norm Jacobians',
 'models':norm_models,'zero_parameter_dimensions_included':True,'passed':True})

weight_models=[]
for mu in [-2.,-.5,0.,.5,3.]:
    ratios=[]
    for t in [2.,4.,16.,64.]:
        for zz in [0.,-.49*t,.5*t,t,-t,-t+1/t,-t+10/t,10*t,t**3]:
            freq=t*t+t*zz
            ratio=t**(-2*mu)*(1+freq*freq)**(mu/2)/(1+zz*zz)**abs(mu)
            ratios.append(ratio)
    assert max(ratios)<=4**abs(mu)+1e-12
    weight_models.append({'mu':mu,'maximum_normalized_majorant_ratio':float(max(ratios))})
checks.append({'name':'whole-frequency amplitude majorant near cancellation',
 'models':weight_models,'includes_zero_and_fixed_frequency_at_zeta_near_minus_T':True,'passed':True})

# Integrate the modulated Gaussian directly, independently of partial-
# Fourier substitution. This bounded Schwartz model checks the same scalings.
gaussian=[]
for t in [2.,4.]:
    zeta=.5;Y=.7;kappa_float=2/3;frequency=t*t+t*zeta
    real=quad(lambda y:np.exp(-(t*y)**2/2)*np.cos((t*t-frequency)*y),-np.inf,np.inf,
              epsabs=2e-12,epsrel=2e-12)[0]*np.exp(-Y*Y/2)
    imag=quad(lambda y:np.exp(-(t*y)**2/2)*np.sin((t*t-frequency)*y),-np.inf,np.inf,
              epsabs=2e-12,epsrel=2e-12)[0]
    expected=np.sqrt(2*np.pi)/t*np.exp(-zeta*zeta/2-Y*Y/2)
    norm_sq=(quad(lambda y:np.exp(-(t*y)**2),-np.inf,np.inf,epsabs=2e-12)[0]
             *quad(lambda yy:np.exp(-(t**kappa_float*yy)**2),-np.inf,np.inf,epsabs=2e-12)[0])
    assert abs(real-expected)<2e-12 and abs(imag)<2e-12
    assert abs(norm_sq-np.pi*t**(-1-kappa_float))<2e-12
    gaussian.append({'T':t,'direct_transform':float(real),'scaled_transform':float(expected),
                     'direct_norm_squared':float(norm_sq),'scaled_norm_squared':float(np.pi*t**(-1-kappa_float))})
checks.append({'name':'direct Gaussian Fourier integral and input norm',
 'kind':'Independent adaptive quadrature versus exact Gaussian scaling; Schwartz model, not a compact-input theorem proof.',
 'models':gaussian,'passed':True})

# A genuinely smooth compact profile cancels the W^3 phase at Z=0.
def rho(ww):return np.exp(-1/(1-ww*ww)) if abs(ww)<1 else 0.
mass=quad(rho,-1,1,epsabs=2e-13,epsrel=2e-13)[0]
nodes,weights=np.polynomial.legendre.leggauss(160)
compact_models=[]
for zz in [0.,.1,-.1]:
    # Q=W^3+Z W^2+Z^3, multiplied by exp(-i W^3).
    real=quad(lambda ww:rho(ww)*np.cos(zz*ww*ww),-1,1,epsabs=2e-13,epsrel=2e-13)[0]
    imag=quad(lambda ww:rho(ww)*np.sin(zz*ww*ww),-1,1,epsabs=2e-13,epsrel=2e-13)[0]
    direct=np.exp(1j*zz**3)*(real+1j*imag)
    sampled=np.dot(weights,np.exp(1j*(nodes**3+zz*nodes**2+zz**3))*np.exp(-1j*nodes**3)
                    *np.array([rho(ww) for ww in nodes]))
    assert abs(direct-sampled)<3e-12
    assert real>=np.cos(.1)*mass-2e-13
    compact_models.append({'Z':zz,'limit_integral_real':float(direct.real),
                            'limit_integral_imag':float(direct.imag),'independent_quadrature_error':float(abs(direct-sampled))})
assert mass>0
checks.append({'name':'nonzero limiting cubic integral with a smooth compact profile',
 'compact_profile_mass':float(mass),'analytic_real_part_lower_bound':float(np.cos(.1)*mass),
 'models':compact_models,'passed':True})

report={'schema':'cubic-scaling-finite-check/v1','passed':True,
 'lesson':'cubic-scaling-and-necessary-continuity.md',
 'lesson_sha256':sha(here/'cubic-scaling-and-necessary-continuity.md'),
 'script_sha256':sha(Path(__file__)),'checks':checks,
 'scope':'Six bounded exact weighted-phase/form/norm models and independent numerical integrals. They test the stated scaling, cancellation majorant and nonzero profile. They do not certify general FIO necessity, transitive prerequisites or fold/Airy estimates.',
 'independent_mathematical_review':False}
(here/'model-check.json').write_text(json.dumps(report,indent=2)+'\n',encoding='utf-8')
print(json.dumps({'passed':True,'finite_checks':len(checks),'lesson_sha256':report['lesson_sha256']}))
