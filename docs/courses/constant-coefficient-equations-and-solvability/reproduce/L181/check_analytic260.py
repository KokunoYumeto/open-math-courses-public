"""Supplement the complete nonsurjectivity proof with high-precision checks."""
from pathlib import Path
import json,math
import mpmath as mp
mp.mp.dps=90
OWN=Path(__file__).resolve().parent
counts={};worst=mp.mpf(0)
def equal(label,left,right):
    global worst
    error=abs(left-right)/(1+abs(right));worst=max(worst,error)
    assert error<mp.mpf("1e-65"),(label,error)
    counts[label]=counts.get(label,0)+1
def holds(label,condition):
    assert condition,label
    counts[label]=counts.get(label,0)+1
def scaled_W(y,h,q,eps):
    kap=mp.sqrt(q*q-1j*eps*h*h*q)
    a=mp.sqrt(q)*(y-h);c=kap/(2*mp.sqrt(q))
    return -mp.sqrt(mp.pi/q)/(4*kap)*mp.exp(kap*kap/(4*q))*(
        mp.exp(kap*(y-h))*mp.erfc(a+c)+mp.exp(-kap*(y-h))*mp.erfc(-a+c))
def scaled_integral(y,h,q,eps):
    kap=mp.sqrt(q*q-1j*eps*h*h*q)
    # Split around the translated Gaussian peaks instead of leaving them in
    # one infinite quadrature interval.
    r0=abs(y-h)
    cuts=sorted(set([mp.mpf(0),max(mp.mpf(0),r0-1),r0,r0+1,mp.inf]))
    return -mp.quad(lambda r:mp.exp(-kap*r)*(
        mp.exp(-q*(y-r-h)**2)+mp.exp(-q*(y+r-h)**2)),cuts)/(2*kap)

labels=[]
for diagonal in range(25):
    for h in range(1,diagonal+2):
        k=diagonal+2-h
        n=3+diagonal*(diagonal+1)//2+h
        labels.append(n);holds("enumeration_h_below_label",h<=n)
holds("enumeration_bijection",labels==list(range(4,4+len(labels))))
for n in range(5,13):
    logq=mp.loggamma(math.factorial(n)+1)
    logprev=mp.loggamma(math.factorial(n-1)+1)
    holds("factorial_lacunarity",logq>=n*logprev)
for n in range(4,13):
    holds("factorial_frequency_lower_bound",math.factorial(n)>=n*n)

for M in [0,2,10]:
    H=4*(M+2)
    for h in [1,H,H+3]:
        for yreal in [-M-1,M+1]:
            for ix in [-1,1]:
                for iy in [-1,1]:
                    for it in [-1,1]:
                        bracket=-mp.mpf(ix)/8-h*h*mp.mpf(it)/(8*H*H)-(yreal-h)**2+(mp.mpf(iy)/8)**2-1
                        holds("complex_tube_forcing_bound",bracket<-mp.mpf(".5"))

for eps in [0,1]:
    for h,q in [(1,mp.mpf(4)),(2,mp.mpf(9)),(3,mp.mpf(20))]:
        kap=mp.sqrt(q*q-1j*eps*h*h*q)
        holds("resolvent_root_bounds",mp.re(kap)>=q and q<=abs(kap)<=mp.root(2,4)*q+mp.mpf("1e-75"))
        for y in [mp.mpf(0),mp.mpf(h)-mp.mpf(".3"),mp.mpf(h)+mp.mpf(".7")]:
            exact=scaled_W(y,h,q,eps)
            integral=scaled_integral(y,h,q,eps)
            equal("closed_resolvent_vs_green_integral",exact,integral)
            second=mp.diff(lambda yy:scaled_W(yy,h,q,eps),y,2)
            equal("independent_resolvent_ode",second-kap*kap*exact,mp.exp(-q*(y-h)**2))
            holds("resolvent_uniform_real_bound",abs(exact)<=1/(q*q)+mp.mpf("1e-75"))
    for h in [1,2,3]:
        errors=[]
        for q in map(mp.mpf,["256","1024","4096"]):
            exact=mp.exp(-q)*scaled_W(mp.mpf(0),h,q,eps)
            main=-mp.sqrt(mp.pi)/(2*q**mp.mpf("1.5"))*mp.exp(-q*(h+mp.mpf(".75")))*mp.exp(1j*eps*(mp.mpf(h)**3/2-mp.mpf(h)**2/4))
            error=abs(exact/main-1);errors.append(error)
            holds("tail_nonvanishing",abs(exact)>0)
        # For the Laplacian the only error is an exponentially smaller endpoint
        # tail; it rounds to zero at this precision. For heat the 1/q trend is
        # visible and decreases along the grid.
        holds("fixed_h_tail_asymptotic_trend",errors[-1]<=errors[0]+mp.mpf("1e-75"))

for p in map(mp.mpf,[".1",".7","2"]):
    for s in [-p,0,p]:
        t=s-1j*p
        equal("bottom_contour_exact_exponent",mp.re(t*t/(2*p)+1j*t),s*s/(2*p)+p/2)
    for sign in [-1,1]:
        for sigma in [0,p/3,p]:
            t=sign*p-1j*sigma
            equal("vertical_contour_exact_exponent",mp.re(t*t/(2*p)+1j*t),p/2+sigma-sigma*sigma/(2*p))
            holds("vertical_contour_decay_floor",mp.re(t*t/(2*p)+1j*t)>=p/2)
    for h in [1,3]:
        q=mp.mpf(17)
        exact=mp.quad(lambda t:mp.exp(-h*h*q*t*t/(2*p)),[-p,0,p])
        closed=mp.sqrt(2*mp.pi*p/(h*h*q))*mp.erf(h*mp.sqrt(q*p/2))
        equal("selected_time_gaussian_integral",exact,closed)

for R in map(mp.mpf,[".2","1","3"]):
    for theta in [mp.pi*k/8 for k in range(16)]:
        for phase in [mp.pi*j/4 for j in range(8)]:
            z=R*mp.exp(1j*phase);Y1=4*R*mp.cos(theta);Y2=4*R*mp.sin(theta)
            real=mp.re((z-Y1)**2+Y2*Y2)
            holds("heat_boundary_complex_kernel_distance",real>=8*R*R-mp.mpf("1e-75"))
            rho=2*R
            kernel=(rho*rho-z*z)/(rho*rho-2*rho*z*mp.cos(theta)+z*z)
            holds("poisson_complex_coordinate_bound",abs(kernel)<=5+mp.mpf("1e-75"))

record=dict(schema="AN02-global-analytic-checks260/v1",status="PASS",
    precision_decimal_digits=90,tolerance="1e-65",total_checks=sum(counts.values()),
    checks_by_kind=counts,max_scaled_error=str(worst),
    independent_green_quadrature_and_special_function_ODE=True,
    finite_parameter_tests_not_actual_infinite_forcing_evaluation=True,
    full_nonsurjectivity_proof_supplied_in_formal=True)
(OWN/"analytic-checks260.json").write_text(json.dumps(record,indent=2)+"\n",encoding="utf-8")
print(json.dumps(record))
