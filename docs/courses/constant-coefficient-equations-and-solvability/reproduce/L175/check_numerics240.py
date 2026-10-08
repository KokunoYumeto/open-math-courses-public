"""Supplementary exact and high-precision mathematical checks, not proof substitutes."""
from pathlib import Path
from fractions import Fraction as Q
from collections import defaultdict
from datetime import datetime, timezone
import hashlib, json
import mpmath as mp

ROOT=Path(__file__).resolve().parent
mp.mp.dps=65
counts=defaultdict(int)
maximum=mp.mpf(0)

def probe(group, statement):
    assert statement,group
    counts[group]+=1

def near(group, actual, expected, tolerance=mp.mpf("1e-54")):
    global maximum
    error=abs(actual-expected)
    maximum=max(maximum,error)
    probe(group,error<tolerance)

def convolution(a,b):
    result=defaultdict(Q)
    for x,ax in a.items():
        for y,by in b.items(): result[x+y]+=ax*by
    return {x:v for x,v in result.items() if v}

for N in range(81):
    geometric={2*j:Q(-1,4)**j for j in range(N+1)}
    result=convolution({0:Q(1),2:Q(1,4)},geometric)
    probe("exact_geometric_inverse_residual",
          result=={0:Q(1),2*N+2:Q(1,4)*Q(-1,4)**N})
    odd={2*j+1:Q(-1) for j in range(N+1)}
    result=convolution({1:Q(1),-1:Q(-1)},odd)
    probe("exact_difference_inverse_residual",result=={0:Q(1),2*N+2:Q(-1)})

def stage_weight(t,stage):
    a=Q(1)
    for j in range(1,stage):
        b=Q(1) if j==1 else min(Q(1),max(Q(0),abs(t)-j+1))
        a=(1+Q(1,2**j))*a+2**j*b
    return a

for t in [Q(j,4) for j in range(-32,33)]:
    stopped=max(2,int(abs(t))+3)
    a=stage_weight(t,stopped)
    tail=Q(1)
    for stage in range(stopped+1,stopped+9):
        tail*=1+Q(1,2**(stage-1))
        probe("exact_local_weight_stabilization",stage_weight(t,stage)==a*tail)
        probe("positive_monotone_weights",stage_weight(t,stage)>=stage_weight(t,stage-1)>=1)
probe("exercise7_exact_weights", [stage_weight(Q(5,2),j) for j in [2,3,4]]
      ==[Q(7,2),Q(67,8),Q(859,64)])

for power in [2,4,6]:
    c=mp.pi*10**power;ell=mp.log(c)
    for xi in range(-4,5):
        x=mp.mpf(xi)/5
        for yi in [-8,-4,-1,1,4,8]:
            y=mp.mpf(yi)/10;z=c+ell*(x+mp.j*y)
            actual=abs(mp.sin(z))**2
            expected=mp.sin(c+ell*x)**2+mp.sinh(ell*y)**2
            near("complex_sine_modulus",actual/(1+expected),expected/(1+expected))
            if xi==0:
                reduced=mp.log(2*mp.sinh(ell*abs(y)))/ell
                direct=mp.log(abs(-2*mp.j*mp.sin(c+ell*mp.j*y)))/ell
                near("exact_real_zero_profile_formula",reduced,direct)
                error=abs(reduced-abs(y))
                bound=mp.exp(-2*ell*abs(y))/(ell*(1-mp.exp(-2*ell*abs(y))))
                probe("quantitative_profile_error_bound",error<=bound*(1+mp.mpf("1e-55")))

for j in range(1,13):
    delta=mp.mpf(j)/7
    integrated=4*mp.quad(lambda y:y*mp.sqrt(delta**2-y**2),[0,delta])
    normalized=integrated/(mp.pi*delta**2)
    near("profile_disk_average",normalized,4*delta/(3*mp.pi))
    probe("absolute_mean_support_bound",normalized<2*delta)

def bump(t):
    return mp.exp(-1/(1-t*t)) if abs(t)<1 else mp.mpf(0)

def bump_derivative(t):
    return -2*t*mp.exp(-1/(1-t*t))/(1-t*t)**2 if abs(t)<1 else mp.mpf(0)

for j in range(-8,9):
    b=mp.mpf(j)/10
    # i*partial(delta_a) has transpose -i*phi'(t+a);
    # the exact shifted jump pairs as - integral_b^infinity phi'.
    pairing=-mp.quad(bump_derivative,[b,(b+1)/2,1])
    near("complex_bilinear_jump_transpose",pairing,bump(b))
    probe("conjugated_transpose_rejected",abs(-pairing-bump(b))>mp.mpf("1e-5"))

mass=mp.quad(bump,[-1,0,1])
near("normalized_probability_bump",mp.quad(lambda t:bump(t)/mass,[-1,0,1]),1)
for j in range(1,13):
    eta=mp.mpf(j)/24
    transform=mp.quad(lambda t:bump(t)*mp.cos(eta*t)/mass,[-1,0,1])
    h=transform**2
    probe("probability_peak_strict_bound",0<h<1)
    probe("probability_peak_quadratic_lower_bound",h>=mp.exp(-2*eta**2))

for width in [mp.mpf("0.1"),mp.mpf("0.3"),mp.mpf("1"),mp.mpf("2")]:
    q=mp.exp(mp.pi/(2*width)+1)
    probe("strict_real_zero_window_threshold",width*mp.log(q)>mp.pi/2)
for n in range(1,5):
    for M in range(4):
        for A in [Q(0),Q(1,2),Q(2)]:
            r=int(n+2*M+A)+1
            gap=Q(r)-n-2*M-A
            probe("strict_fixed_derivative_loss",gap>0)

record=dict(schema="AN02-finite-order-supplementary-checks240/v1",
            observed_at_utc=datetime.now(timezone.utc).isoformat(),status="PASS",
            decimal_precision=mp.mp.dps,checks_by_group=dict(counts),total_checks=sum(counts.values()),
            maximum_absolute_identity_error=mp.nstr(maximum,65),
            identities_compared_after_scaling_when_large=True,
            formal_proofs_not_replaced_by_finite_samples=True,
            code_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest().upper())
(ROOT/"numerical-checks240.json").write_text(json.dumps(record,indent=2)+"\n",encoding="utf-8")
print(json.dumps(record))
