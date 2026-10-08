"""Supplementary probes of original examples; none is a proof of the theorem."""
from pathlib import Path
from datetime import datetime,timezone
from fractions import Fraction
import hashlib,json
import mpmath as mp
OWN=Path(__file__).resolve().parent;mp.mp.dps=65
counts={};errors=[];checks=[]
def close(name,actual,expected,tol=mp.mpf("1e-48")):
    err=abs(actual-expected);assert err<tol,(name,str(err))
    counts[name]=counts.get(name,0)+1;errors.append(err)
def exact(name,condition):
    assert condition,name
    counts[name]=counts.get(name,0)+1
def b(z):return mp.sinh(z)/z if z else mp.mpf(1)
for k in range(1,6):
    lam=mp.j*k*mp.pi
    close("simple_resonant_derivative",mp.diff(b,lam),(-1)**k/(mp.j*k*mp.pi))
    close("double_resonant_derivative",mp.diff(lambda z:b(z)**2,lam,2),-2/(k*mp.pi)**2)
    for ix in range(-16,17):
        x=mp.mpf(ix)/9
        coefficient=(-1)**(k+1)*k*mp.pi
        u=lambda t:coefficient*t*mp.sin(k*mp.pi*t)
        close("direct_resonant_real_average",mp.quad(lambda y:u(x-y)/2,[-1,0,1]),mp.cos(k*mp.pi*x))
for ix in range(-7,8):
    x=mp.mpf(ix)/5
    v=lambda t:-mp.pi**2/2*t*t*mp.cos(mp.pi*t)
    close("double_average_real_solution",mp.quad(lambda y:(2-abs(y))*v(x-y)/4,[-2,0,2]),mp.cos(mp.pi*x))
for ix in range(-8,9):
    x=mp.mpf(ix)/5
    close("translated_first_derivative",mp.diff(lambda t:mp.exp(2*(t+mp.mpf(3)/4))/2,x-mp.mpf(3)/4),mp.exp(2*x))
    close("translated_second_derivative",mp.diff(lambda t:mp.exp(3*(t-mp.mpf(1)/2))/9,x+mp.mpf(1)/2,2),mp.exp(3*x))
beta=lambda y:mp.exp(-1/(1-y*y))if abs(y)<1 else mp.mpf(0)
Z=mp.quad(beta,[-1,-mp.mpf(1)/2,0,mp.mpf(1)/2,1])
c=mp.quad(lambda y:beta(y)*mp.exp(-2*y),[-1,-mp.mpf(1)/2,0,mp.mpf(1)/2,1])/Z
exact("smooth_kernel_multiplier_strict_bounds",1<c<mp.cosh(2))
for ix in range(-5,6):
    x=mp.mpf(ix)/3
    close("compact_smooth_kernel_exponential_solution",
        mp.quad(lambda y:beta(y)*mp.exp(2*(x-y))/c,[-1,-mp.mpf(1)/2,0,mp.mpf(1)/2,1])/Z,mp.exp(2*x))
B=lambda s:mp.exp(-1/s)if s>0 else mp.mpf(0)
def h(t):return B(t+mp.mpf(7)/4)/(B(t+mp.mpf(7)/4)+B(-mp.mpf(5)/4-t))
def boundary_u(x):return sum(h(x-k)/(2-x+k)for k in range(4))
for ix in range(-19,40):
    x=mp.mpf(ix)/20
    close("boundary_forcing_telescoping",boundary_u(x)-boundary_u(x-1),1/(2-x))
for alpha in [(a,d)for a in range(6)for d in range(6)]:
    a,d=alpha
    derivative=(-2*mp.j)**a*(mp.j/3)**d
    close("entire_point_carrier_moment",(mp.j)**(a+d)*derivative,2**a*(-mp.mpf(1)/3)**d)
# Cauchy reconstruction at an actual zero of a fixed multiplier.
circle=[mp.exp(2*mp.pi*mp.j*k/128)for k in range(128)]
multiplier=lambda z:z**3*(z-2*mp.j)
for center in [mp.mpf(0),mp.mpf(1)/20,mp.j/20]:
    for degree in range(8):
        Phi=lambda z:(1+z)**degree
        quotient_mean=sum(multiplier(center+t)*Phi(center+t)/multiplier(center+t)for t in circle)/128
        close("compact_division_circle_value",quotient_mean,Phi(center))
        bound=max(abs(multiplier(center+t)*Phi(center+t))for t in circle)/(mp.mpf(9)/10)**4
        exact("compact_division_circle_lower_bound",min(abs(multiplier(center+t))for t in circle)>=(mp.mpf(9)/10)**4)
        exact("compact_division_circle_upper_bound",abs(Phi(center))<=bound)
for j in range(1,101):
    gap=Fraction(1,j+1);nextgap=Fraction(1,j+2)
    Y=(Fraction(-4)+gap,Fraction(4)-gap);Zeta=(Fraction(-2)+gap,Fraction(4)-gap)
    exact("exact_eroded_interval",Zeta==(max(Y[0],Y[0]+2),min(Y[1],Y[1]+2)))
    exact("strict_exhaustion_margin",gap>nextgap)
    exact("summable_tail_exact",sum((Fraction(1,2**k)for k in range(j+1,j+21)),Fraction(0))<Fraction(1,2**j))
# An asymmetric compact smoothing kernel checks the reflection physically.
shift=mp.pi/2
F1=mp.quad(lambda t:beta(4*t)*mp.exp(-mp.j*t),[-mp.mpf(1)/4,0,mp.mpf(1)/4])
close("asymmetric_reflected_smoothing_phase",mp.exp(mp.j*shift)*F1,mp.j*F1)
close("asymmetric_unreflected_smoothing_phase",mp.exp(-mp.j*shift)*F1,-mp.j*F1)
exact("asymmetric_smoothings_differ",abs(2*mp.j*F1)>0)
record={"schema":"AN02-original-example-probes219/v1","observed_at_utc":datetime.now(timezone.utc).isoformat(),
    "status":"PASS","decimal_precision":mp.mp.dps,"probe_count":sum(counts.values()),"counts":counts,
    "maximum_identity_error":str(max(errors)),"compact_smooth_multiplier_c":str(c),
    "proof_status":"Supplementary numerical and rational checks only; the complete analytic arguments are in the formal and learner texts.",
    "independent_review":False,"source_code_sha256":hashlib.sha256(Path(__file__).read_bytes()).hexdigest().upper()}
(OWN/"supplementary-example-probes219.json").write_text(json.dumps(record,indent=2)+"\n",encoding="utf-8")
print(json.dumps(record))
