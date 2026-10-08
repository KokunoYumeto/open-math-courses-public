"""Supplementary physical and exact-rational checks of the original examples."""
from pathlib import Path
from datetime import datetime,timezone
from fractions import Fraction
import hashlib,json
import mpmath as mp
OWN=Path(__file__).resolve().parent;mp.mp.dps=65
counts={};errors=[]
def close(name,actual,expected,tol=mp.mpf("1e-48")):
    err=abs(actual-expected);assert err<tol,(name,str(err))
    errors.append(err);counts[name]=counts.get(name,0)+1
def exact(name,condition):
    assert condition,name
    counts[name]=counts.get(name,0)+1
def bump(t):return mp.exp(-1/(1-t*t))if abs(t)<1 else mp.mpf(0)
def bump_prime(t):return -2*t*bump(t)/(1-t*t)**2 if abs(t)<1 else mp.mpf(0)
center=-mp.mpf(2)/5;width=mp.mpf(7)/10
f=lambda t:bump((t-center)/width)
fp=lambda t:bump_prime((t-center)/width)/width
u=lambda t:2*sum(fp(t-1-2*k)for k in range(8))
for ix in range(-6,19):
    x=mp.mpf(ix)/3;cuts=[mp.mpf(-1),mp.mpf(1)]
    for k in range(8):
        for marker in [center-width,center,center+width]:
            y=x-1-2*k-marker
            if -1<y<1:cuts.append(y)
    close("physical_locally_finite_average",mp.quad(lambda y:u(x-y)/2,sorted(set(cuts))),f(x))
for ix in range(-200,201,5):
    c=mp.mpf(ix)/2
    k=mp.nint((c-mp.pi/2)/mp.pi);t=mp.pi/2+k*mp.pi
    exact("averaging_window_interior",abs(t-c)<3*mp.log(2+abs(c)))
    exact("averaging_window_strict_lower_bound",abs(mp.sin(t)/t)>(3+abs(c))**-3)
    exact("point_mass_strict_window_bound",1>(2+abs(c))**-2)
    close("point_mass_reflected_transform",mp.exp(mp.j*mp.mpf(3)/4*c),mp.conj(mp.exp(-mp.j*mp.mpf(3)/4*c)))
def density(y):
    return (1+y/3)*mp.exp(-1/(1-4*y*y))if abs(y)<mp.mpf(1)/2 else mp.mpf(0)
pieces=[-mp.mpf(1)/2,-mp.mpf(1)/4,0,mp.mpf(1)/4,mp.mpf(1)/2]
d=mp.quad(lambda y:density(y)*mp.exp(-y),pieces)
exact("asymmetric_smooth_kernel_positive_multiplier",d>0)
for ix in range(-5,6):
    x=mp.mpf(ix)/3
    close("smooth_kernel_analytic_forcing",mp.quad(lambda y:density(y)*mp.exp(x-y)/d,pieces),mp.exp(x))
for z in [mp.mpf(3)/4+mp.j/5,7-mp.j/3,15+mp.j/4]:
    F=mp.quad(lambda y:density(y)*mp.exp(-mp.j*y*z),pieces)
    for m in [1,2,3]:
        derivative_transform=mp.quad(lambda y:mp.diff(density,y,m)*mp.exp(-mp.j*y*z),pieces)
        close("complex_integration_by_parts",derivative_transform,(mp.j*z)**m*F)
for gamma in range(9):
    for x in [-mp.mpf(2)/3,mp.mpf(3)/4]:
        for z in [mp.mpf(1)/3,mp.mpf(5)/2,mp.mpf(7)/4+mp.j/3]:
            derivative_action=(-1)**gamma*mp.diff(lambda t:mp.exp(-mp.j*t*z),x,gamma)
            close("compact_derivative_Fourier_sign",derivative_action,(mp.j*z)**gamma*mp.exp(-mp.j*x*z))
for j in range(2,102):
    left=Fraction(1)-Fraction(5,4*j);right=Fraction(1)-Fraction(3,4*j)
    exact("exact_escape_support_inside_domains",Fraction(-1)<left<right<Fraction(1))
    exact("fixed_transpose_compact",Fraction(-5,4)<left<right<Fraction(5,4))
    exact("support_escape_distance",Fraction(1)-right==Fraction(3,4*j))
    radius=Fraction(1,j+6)
    exact("translated_test_support_inside_solution_component",
          Fraction(1,4)<Fraction(3,4)-radius<Fraction(3,4)+radius<Fraction(5,4))
for N in range(9):
    for k in range(1,13):
        h=Fraction(1,2**k)
        mh=mp.mpf(h.numerator)/h.denominator
        close("scaled_common_order_jet",mp.diff(lambda x:mh**N*(x/mh)**(N+1),0,N+1),
              mp.factorial(N+1)/mh)
    previous=None
    for k in range(6,19):
        h=mp.mpf(2)**(-k);logratio=(N+1)*mp.log(h)+1/(3*h)
        lower=(N+1)*mp.log(h)-(N+2)*mp.log(3*h)-mp.log(mp.factorial(N+2))
        exact("boundary_exponential_polynomial_lower_bound",logratio>=lower)
        if previous is not None:exact("boundary_obstruction_ratio_increases",logratio>previous)
        previous=logratio
record={"schema":"AN02-original-support-example-probes222/v1","observed_at_utc":datetime.now(timezone.utc).isoformat(),
    "status":"PASS","decimal_precision":mp.mp.dps,"probe_count":sum(counts.values()),"counts":counts,
    "maximum_identity_error":str(max(errors)),"smooth_kernel_analytic_multiplier":str(d),
    "proof_status":"Supplementary physical integrations,signs and exact-rational geometry only;complete necessity and support proofs are in the formal text.",
    "independent_review":False,"source_code_sha256":hashlib.sha256(Path(__file__).read_bytes()).hexdigest().upper()}
(OWN/"supplementary-example-probes222.json").write_text(json.dumps(record,indent=2)+"\n",encoding="utf-8")
print(json.dumps(record))
