"""Independent defining-integral and physical-Hessian checks for original L149."""
from pathlib import Path
import cmath
import json
import math
import mpmath as mp
from scipy.integrate import quad
from scipy.optimize import brentq

HERE=Path(__file__).resolve().parent
mp.mp.dps=50
rows=[]


def equal(name, actual, expected, tolerance=3e-9):
    error=abs(actual-expected)/max(1.,abs(expected))
    assert error<=tolerance,(name,actual,expected,error)
    def serial(value):
        return [value.real,value.imag] if isinstance(value,complex) else float(value)
    rows.append({"name":name,"actual":serial(actual),"expected":serial(expected),
                 "relative_or_absolute_error":float(error),"tolerance":tolerance,"pass":True})


def leq(name, actual, bound):
    assert actual<=bound+2e-9*max(1.,abs(bound)),(name,actual,bound)
    rows.append({"name":name,"actual":float(actual),"upper_bound":float(bound),"pass":True})


def raw(y):
    return math.exp(-1/(1-y*y)) if abs(y)<1 else 0.


normalization=quad(raw,-1,1,epsabs=1e-13,epsrel=1e-13)[0]


def chi(y, order=0):
    if abs(y)>=1:return 0.
    d=1-y*y
    value=raw(y)/normalization
    if order==0:return value
    if order==1:return value*(-2*y/d**2)
    return value*(4*y*y/d**4-2/d**2-8*y*y/d**3)


def integrate(function, points=None):
    return quad(function,-1,1,points=points,epsabs=3e-11,epsrel=3e-11,limit=500)[0]


for derivative in range(3):
    equal(f"probability kernel derivative integral order={derivative}",
          integrate(lambda y:chi(y,derivative)),1. if derivative==0 else 0.)


def ell(xi):
    return 2*math.log1p(max(xi,0.))


def smoothed(xi, eta, t):
    M=math.hypot(t,eta)
    point=-xi/M
    points=[point] if -1<point<1 else None
    return integrate(lambda y:chi(y)*ell(xi+M*y),points)


for t in (16.,64.):
    for eta in (0.,.8*t):
        M=math.hypot(t,eta)
        for ratio in (-.6,0.,.8):
            xi=ratio*M
            point=-xi/M
            points=[point]
            physical=smoothed(xi,eta,t)
            lower=max(0.,xi-M)
            upper=xi+M
            theta=quad(lambda theta:2*chi((theta-xi)/M)*math.log1p(theta)/M,
                       lower,upper,epsabs=3e-11,epsrel=3e-11,limit=500)[0]
            label=f"t={t} eta={eta} xi/M={ratio}"
            equal("two defining convolution coordinates "+label,physical,theta)
            xkernel=integrate(lambda y:chi(y,2)*(ell(xi+M*y)-ell(xi))/M**2,points)
            xdistribution=2*chi(point)/M-2*integrate(
                lambda y:chi(y)/(1+xi+M*y)**2 if xi+M*y>0 else 0.,points)
            equal("corner delta versus actual second kernel "+label,xkernel,xdistribution)
            Mp=eta/M
            Mpp=t*t/M**3
            ykernel=(Mp*Mp/M**2)*integrate(
                lambda y:(2*chi(y)+4*y*chi(y,1)+y*y*chi(y,2))*(ell(xi+M*y)-ell(xi)),points
            )-(Mpp/M)*integrate(
                lambda y:(chi(y)+y*chi(y,1))*(ell(xi+M*y)-ell(xi)),points)
            ellM=2*integrate(lambda y:chi(y)*y/(1+xi+M*y) if xi+M*y>0 else 0.,points)
            ellMM=2*chi(point)*point*point/M-2*integrate(
                lambda y:chi(y)*y*y/(1+xi+M*y)**2 if xi+M*y>0 else 0.,points)
            equal("scale chain versus actual eta-second kernel "+label,ykernel,Mp*Mp*ellMM+Mpp*ellM)
            leq("zero-order log comparison "+label,abs(physical-ell(xi)),4*math.log(M))
            for shift in (-1.3,1.3):
                leq(f"exact shift-weight bound h={shift} "+label,
                    abs(smoothed(xi+shift,eta,t)-physical),2*math.log1p(abs(shift)))

for t in (8.,32.,128.):
    for ratio in (.1,1.,10.):
        r=t*ratio
        mt=mp.mpf(t)
        mr=mp.mpf(r)
        def physical_radial(y):
            M=mp.sqrt(mt*mt+y*y)
            return M/mp.sqrt(mt)-mp.sqrt(M)
        radial=float(mp.diff(physical_radial,mr,2)/4)
        tangent=float(mp.diff(lambda y:mp.sqrt(mt*mt+mr*mr+y*y)/mp.sqrt(mt)
                             -mp.sqrt(mp.sqrt(mt*mt+mr*mr+y*y)),mp.mpf(0),2)/4)
        M=math.hypot(t,r)
        radial_formula=t*t/(4*M**3)*(1/math.sqrt(t)-1/(2*math.sqrt(M)))+r*r/(16*M**3.5)
        tangent_formula=(1/math.sqrt(t)-1/(2*math.sqrt(M)))/(4*M)
        equal(f"physical radial Hessian t={t} r/t={ratio}",radial,radial_formula)
        equal(f"physical tangential Hessian t={t} r/t={ratio}",tangent,tangent_formula)
        leq(f"normalized radial lower bound t={t} r/t={ratio}",1/16,radial*M**1.5)

ts=(64.,144.,256.)
radii=(.5,1.,1.5)
offsets=(1.,160.,800.)


def correction(r,t):
    M=math.hypot(t,r)
    return M/math.sqrt(t)-math.sqrt(M)


def seed(r,j):
    return radii[j]*abs(r)+correction(r,ts[j])-offsets[j]


for r in (-5.,-2.,0.,2.,5.):
    equal(f"actual finite maximum stable strip eta={r}",max(seed(r,j) for j in range(3)),seed(r,0))
leq("analytic second inactivity bound through 161",161/2+161**2/(2*144**1.5),159.)
leq("analytic third inactivity bound through 301",301+301**2/(2*256**1.5),799.)
switches=[brentq(lambda r:seed(r,1)-seed(r,0),1,1000),
          brentq(lambda r:seed(r,2)-seed(r,1),800,2000)]
switch_records=[]
for left,r in enumerate(switches):
    equal(f"adjacent seed crossing {left+1}",seed(r,left),seed(r,left+1))
    leq(f"third seed does not dominate crossing {left+1}",
        seed(r,2 if left==0 else 0),seed(r,left)+1e-8)
    def slope(j):
        M=math.hypot(ts[j],r)
        return radii[j]+r/M*(1/math.sqrt(ts[j])-1/(2*math.sqrt(M)))
    jump=slope(left+1)-slope(left)
    assert jump>0
    switch_records.append({"eta":r,"active_seed_indices":[left+1,left+2],
                           "positive_real_derivative_jump":jump,"positive_Levi_line_mass":jump/4})


def cq(function,a,b):
    return complex(quad(lambda x:function(x).real,a,b,epsabs=1e-10,epsrel=1e-11)[0],
                   quad(lambda x:function(x).imag,a,b,epsabs=1e-10,epsrel=1e-11)[0])


a,b=2.25,2.75
for z in (0j,.7+.5j,2+1j,-1-1.2j):
    actual=cq(lambda x:cmath.exp(-1j*x*z),a,b)
    expected=(cmath.exp(-1j*a*z)-cmath.exp(-1j*b*z))/(1j*z) if z else b-a
    equal(f"actual exterior-interval complex transform z={z}",actual,expected)
for eta in (0.,.5,1.,2.,4.):
    physical=2*math.pi*quad(lambda x:math.exp(2*eta*x),a,b,epsabs=1e-10,epsrel=1e-12)[0]
    expected=math.pi*(math.exp(5.5*eta)-math.exp(4.5*eta))/eta if eta else math.pi
    equal(f"physical exterior-interval squared plane eta={eta}",physical,expected)
for eta in (-4.,-1.,0.,1.,4.):
    actual=max(-2*eta,-3*eta)+max(-eta,eta)
    equal(f"exact separated supporting functions eta={eta}",actual,-eta if eta>=0 else -4*eta)
leq("explicit sufficient parameter D=1 t=1e8",math.log(1e8)/math.sqrt(1e8),1/144)

report={
    "schema":"AN02-L149-independent-examples/v1","status":"PASS","checks":len(rows),
    "scope":"Defining convolution in original and unscaled coordinates, actual smooth-kernel derivatives versus corner-distribution chain derivatives, physical high-precision radial/tangential Hessians, finite-stage inactivity and interfaces, actual exterior-interval transforms and physical squared norms, exact support gaps and parameter margin.",
    "checks_are_supplements_not_proofs":True,
    "maximum_equality_error":max(row.get("relative_or_absolute_error",0) for row in rows),
    "finite_seed_parameters":{"t":ts,"radii":radii,"G":offsets},
    "finite_seed_switches":switch_records,"rows":rows,
}
(HERE/"independent-example-checks160.json").write_text(json.dumps(report,indent=2)+"\n",encoding="utf-8")
print(json.dumps({key:report[key] for key in ("status","checks","maximum_equality_error")}))
