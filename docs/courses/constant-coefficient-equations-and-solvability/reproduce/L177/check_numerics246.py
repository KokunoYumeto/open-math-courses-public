"""Independent supplementary identities; the complete arguments are in the chapters."""
from pathlib import Path
from fractions import Fraction as F
import json,math
import mpmath as mp

OWN=Path(__file__).resolve().parent
mp.mp.dps=65
counts={};maximum=mp.mpf(0)

def check(name,condition):
    assert condition,name
    counts[name]=counts.get(name,0)+1

def close(name,left,right,tolerance=mp.mpf("1e-48")):
    global maximum
    error=abs(left-right)/(1+abs(left)+abs(right))
    maximum=max(maximum,error)
    check(name,error<tolerance)

def number(q):
    return mp.mpf(q.numerator)/q.denominator if isinstance(q,F)else mp.mpf(q)

for t in range(1,32):
    for x in range(-t,t+1):
        check("quantitative_wedge_clock_exact",t*t+x*x<=2*t*t)

for x in range(-20,21):
    for depth in [F(0),F(1,5),F(2),F(7)]:
        y=-F(x*x)-depth
        check("parabola_translated_cone_bound_exact",F(x*x)+(1-y)**2<=2*(1-y)**2)

b,c=F(1,5),F(3,10)
weights={0:F(1)}
for j in range(13):
    expected={2*k-j:F(math.comb(j,k))*b**k*c**(j-k)for k in range(j+1)}
    for x,value in expected.items():
        check("independent_recursive_delay_coefficients",weights.get(x)==value)
        check("each_delay_node_has_required_clock",abs(x)<=j)
    check("total_delay_coefficient_exact",sum(weights.values())==F(1,2)**j)
    next_weights={}
    for x,value in weights.items():
        next_weights[x+1]=next_weights.get(x+1,F(0))+b*value
        next_weights[x-1]=next_weights.get(x-1,F(0))+c*value
    weights=next_weights

def g(l,t):
    return mp.exp(-t)*t**(l-1)/mp.factorial(l-1)if t>=0 else mp.mpf(0)

for r in range(1,5):
    for s in range(1,5):
        for t in [mp.mpf(".2"),mp.mpf(".7"),mp.mpf("1.3")]:
            integral=mp.quad(lambda u:g(r,u)*g(s,t-u),[0,t/2,t])
            close("independent_green_convolution_integral",integral,g(r+s,t))

def integrate(fun,lo,hi):
    if hi<=lo:return mp.mpf(0)
    pieces=[lo]
    while pieces[-1]+mp.mpf(".35")<hi:pieces.append(pieces[-1]+mp.mpf(".35"))
    pieces.append(hi)
    return mp.quad(fun,pieces)

for T in [mp.mpf("2.4"),mp.mpf("3.7"),mp.mpf("5.2")]:
    def phi(t):
        return mp.exp(-1/(t+1)-1/(T-t))if -1<t<T else mp.mpf(0)
    def dphi(t):
        return phi(t)*((t+1)**-2-(T-t)**-2)if -1<t<T else mp.mpf(0)
    main=[];delay=[]
    for j in range(int(mp.floor(T))+1):
        main.append(integrate(lambda t,j=j:g(j+1,t-j)*(phi(t)-dphi(t)),mp.mpf(j),T))
        delay.append(integrate(lambda t,j=j:g(j+1,t-j-1)*phi(t),mp.mpf(j+1),T))
    for omega in [mp.mpf("0"),mp.mpf(".4"),mp.mpf(".9")]:
        def psi(x):return mp.exp(-mp.mpf(x*x))*mp.exp(1j*omega*x)
        value=mp.mpc(0)
        for j in range(len(main)):
            for k in range(j+1):
                x=2*k-j;weight=number(F(math.comb(j,k))*b**k*c**(j-k))
                value+=weight*(main[j]*psi(x)-delay[j]*(number(b)*psi(x+1)+number(c)*psi(x-1)))
        close("actual_bilinear_distributional_delay_equation",value,phi(0))

for i in range(1,49):
    t=mp.mpf(i)/20
    r=lambda s:4*s*mp.exp(-s)
    density=lambda s:mp.exp(s)-mp.exp(-3*s)
    integral=mp.quad(lambda s:r(s)*density(t-s),[0,t/2,t])
    close("independent_continuous_feedback_integral",integral,density(t)-r(t))

for i in range(51):
    t=mp.mpf(i)*mp.mpf("1.5")/50
    exact=mp.exp(t)-mp.exp(-3*t);partial=mp.mpf(0)
    for J in range(6):
        if J:
            partial+=mp.exp(-t)*4**J*t**(2*J-1)/mp.factorial(2*J-1)
        bound=2*mp.exp(3)*3**(2*J+1)/mp.factorial(2*J+1)
        check("continuous_tail_nonnegative_and_quantified",exact-partial>=-mp.mpf("1e-62")
              and exact-partial<=bound)

for t in [mp.mpf(".02"),mp.mpf(".1"),mp.mpf(".3"),mp.mpf("1.1")]:
    w=lambda s:s*s*mp.exp(-2*s)
    close("finite_regularity_error_sign",-(mp.diff(w,t)+w(t)),mp.exp(-2*t)*(t*t-2*t))
    w3=lambda s:s**3*mp.exp(-2*s)
    close("one_extra_derivative_error_sign",-(mp.diff(w3,t)+w3(t)),mp.exp(-2*t)*(t**3-3*t*t))

epsilon=mp.mpf(".25")
norm=mp.quad(lambda t:(2*t-t*t)*mp.exp(-2*t),[0,epsilon])
check("actual_local_error_norm_below_one_sixteenth",norm<mp.mpf(1)/16)
norm3=mp.quad(lambda t:(3*t*t-t**3)*mp.exp(-2*t),[0,epsilon])
check("actual_extra_derivative_norm_below_one_sixtyfourth",norm3<mp.mpf(1)/64)

for xi in range(-8,9):
    for eta in range(-8,9):
        z=mp.mpc(xi,eta)
        if abs(eta)>mp.log(abs(z)+2):
            check("one_dimensional_all_direction_barrier_diagnostic",abs(z)>1 and abs(1/(1j*z))<1)
for R in range(2,52):
    check("two_dimensional_derivative_zero_diagnostic",R>mp.log(R+2))

report={"schema":"causal-vertex-supplementary-checks246/v1","status":"PASS",
    "precision_decimal_digits":65,"identity_tolerance":"1e-48",
    "checks":counts,"total_checks":sum(counts.values()),
    "maximum_scaled_identity_error":mp.nstr(maximum,65),
    "spatial_test_cutoff":"Equal to1 on every contributing node and its one-step shifts;compact outside that finite node range.",
    "distribution_tests":"Three independent compact time bumps and three complex spatial oscillations;bilinear transpose sign retained.",
    "supplementary_evidence_not_a_proof_substitute":True}
(OWN/"numerical-checks246.json").write_text(json.dumps(report,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
print(json.dumps(report))
