"""Supplementary exact extension, jet, transpose and correction probes."""
from pathlib import Path
from fractions import Fraction as F
import hashlib,json
import mpmath as mp
OWN=Path(__file__).resolve().parent
mp.mp.dps=65
counts={};maximum=mp.mpf(0)
def test(kind,condition):
    assert condition,kind
    counts[kind]=counts.get(kind,0)+1
def equal(kind,left,right):
    global maximum
    error=abs(left-right);maximum=max(maximum,error)
    test(kind,error<mp.mpf("1e-53"))
def mpf(x):
    x=F(x);return mp.mpf(x.numerator)/x.denominator
total=F(0)
for j in range(1,97):
    x=1-F(1,2**j);w=2**(j*j)
    eps=F(1,2**(j*j+2*j+8));gap=F(1,2**j)
    test("weighted_radius_exact",w*eps==F(1,2**(2*j+8)))
    test("expanded_support_inside_domain",0<x-eps<x+eps<1)
    test("tiny_radius_relative_to_boundary",eps<gap/8)
    test("expanded_support_isolates_point",eps<gap/2)
    total+=w*eps
    test("finite_geometric_error_sum",
         total==F(1,768)*(1-F(1,4**j)))
    r=gap/8
    test("exact_extension_countertest_support",0<x-r<x+r<1 and r<gap/2)
    test("increasing_datum_and_primitive_orders",j>=1 and j-1>=0)
for N in range(0,25):
    j=2*N+8
    exponent=j*j-N*(j+3)
    test("rapid_weight_beats_any_sampled_order",exponent>j)
    m=N+2;eps=F(1,2**(N+5))
    test("isolated_jet_low_order_decay",eps**(m-N)<1 and m>N)
    test("smooth_error_scaled_test_decay",eps**(m+1)<eps**(m-N))
    test("LF_fixed_order_countertest_amplification",eps**(N-m)>1)
test("exact_tail_band",F(3,4)-4-F(1,8)==F(-27,8)
     and F(3,4)-4+F(1,8)==F(-25,8))
test("singular_adjoint_point",F(3,4)-F(1,4)==F(1,2))
test("tail_outside_unknown_domain",F(-25,8)<-1)
test("singular_sampling_domains",
     (F(-3,4)-F(1,4),F(5,4)-F(1,4))==(-1,1))
test("ordinary_tail_sampling_fails",0-F(31,8)<-1)
test("disconnected_receiver_margin",
     min(F(-1,2)+2,1-F(1,2),F(15,4)-3,5-F(17,4))==F(1,2))
test("component_correction_constants",(-1)**2==1 and 4**2==16)
for j in range(1,65):
    alternating=sum(F((-1)**k,2**k) for k in range(1,j+1))
    test("finite_bilinear_ell1_series",
         alternating==F(-1,3)*(1-F(-1,2)**j))
    test("ell1_finite_norm",sum(F(1,2**k) for k in range(1,j+1))==1-F(1,2**j))

for k in range(-5,8):
    t=mp.mpf(k)/8
    for degree in range(1,7):
        phi=lambda x:(1+mp.mpc(".2",".3")*x)**degree
        actual=-mp.j*(mp.j*phi((t-mp.mpf(".25"))+mp.mpf(".25")))
        equal("proper_point_quotient_inverse",actual,phi(t))
        wrong=-mp.j*(-mp.j*phi(t))
        test("conjugated_point_coefficient_rejected",abs(actual-wrong)>mp.mpf(".1"))
for j in range(1,13):
    x=1-mp.power(2,-j);coef=mp.mpf((-1)**j)/(j+1)
    phi=lambda t:(1+mp.mpc(".1",".2")*t)**(j+2)
    action=lambda order,c,func:c*(-1)**order*mp.diff(func,x,order)
    actual=-mp.j*action(j-1,-mp.j*coef,lambda t:mp.diff(phi,t))
    expected=action(j,coef,phi)
    equal("complex_distributional_primitive",actual,expected)
    test("wrong_derivative_kernel_conjugation_rejected",
         abs(-actual-expected)>mp.mpf(".001"))
for a in [-1,0,1]:
    for b in [-1,0,1]:
        z1=mp.mpc(a,b);z2=mp.mpc(b,a)
        expected=z1+3*mp.j*z2
        for z3 in [0,mp.j,7]:
            actual=z1+3*mp.j*z2
            equal("noninjective_range_functional",actual,expected)
            test("range_functional_bound",
                 abs(actual)<=abs(z1)+3*abs(z2)+mp.mpf("1e-60"))
test("explicit_range_value",mp.mpf(1)+3*mp.j*mp.j==-2)
for component,base in [((-2,1),-1),((3,5),4)]:
    for n in range(1,10):
        x=mp.mpf(component[0])+(component[1]-component[0])*mp.mpf(n)/10
        w=lambda t:-t*t+base*base
        equal("smooth_error_derivative_removed",2*x+mp.diff(w,x),0)
        equal("componentwise_constant_remaining",x*x+w(x),base*base)

bump=lambda t:mp.exp(-1/(1-t*t)) if abs(t)<1 else mp.mpf(0)
parts=[-1,mp.mpf("-.5"),0,mp.mpf(".5"),1]
mass=mp.quad(bump,parts)
test("positive_normalizing_mass",0<mass<2)
rho=lambda t:bump(t)/mass
moment2=mp.quad(lambda t:t*t*rho(t),parts)
test("even_bump_second_moment",0<moment2<1)
equal("even_bump_first_moment",mp.quad(lambda t:t*rho(t),parts),0)
phi=lambda t:1+t+t*t+t**3
for j in range(1,7):
    x=1-mp.power(2,-j);eps=mp.power(2,-j*j-2*j-8)
    avg=mp.quad(lambda t:rho(t)*phi(x+eps*t),parts)
    difference=phi(x)-avg
    equal("actual_bump_polynomial_mollification",
          difference,-(1+3*x)*eps*eps*moment2)
    test("actual_bump_mean_value_bound",abs(difference)<=6*eps)
    test("actual_weighted_bump_error_bound",
         mp.power(2,j*j)*abs(difference)<=6*mp.power(2,-2*j-8))
rho_prime=lambda t:(-2*t/(1-t*t)**2)*rho(t) if abs(t)<1 else mp.mpf(0)
equal("Heaviside_distributional_derivative",
      -mp.quad(rho_prime,[0,mp.mpf(".5"),1]),rho(0))
report={"scope":"Supplementary finite exact and 65-digit probes of the worked mathematics; universal statements are proved in the chapters.",
        "status":"PASS","decimal_precision":65,"probe_count":sum(counts.values()),
        "probe_counts":counts,"maximum_numerical_identity_error":mp.nstr(maximum,25),
        "source_code_sha256":hashlib.sha256(Path(__file__).read_bytes()).hexdigest().upper(),
        "full_proofs_not_replaced_by_probes":True}
(OWN/"supplementary-example-probes237.json").write_text(
    json.dumps(report,indent=2)+"\n",encoding="utf-8")
print(json.dumps({k:report[k] for k in ["status","probe_count","decimal_precision",
                                    "maximum_numerical_identity_error"]}))
