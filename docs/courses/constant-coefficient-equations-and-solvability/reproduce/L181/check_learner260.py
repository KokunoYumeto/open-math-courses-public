"""Check finite entire particular solutions and explicit learner constants."""
from pathlib import Path
import json
import mpmath as mp
mp.mp.dps=90
OWN=Path(__file__).resolve().parent
counts={};worst=mp.mpf(0)
def equal(label,a,b):
    global worst
    error=abs(a-b)/(1+abs(b));worst=max(worst,error)
    assert error<mp.mpf("1e-65"),(label,error)
    counts[label]=counts.get(label,0)+1
def holds(label,condition):
    assert condition,label
    counts[label]=counts.get(label,0)+1
for eps in [0,1]:
    q=mp.mpf(7);h=mp.mpf(2);kap=mp.sqrt(q*q-1j*eps*h*h*q)
    c0=mp.mpf(3);c1=mp.mpf(-2)
    def W(y):
        return c0*mp.cosh(kap*y)+c1*mp.sinh(kap*y)/kap+mp.exp(-q)*y/kap*mp.quad(
            lambda tau:mp.sinh(kap*y*(1-tau))*mp.exp(-q*(tau*y-h)**2),[0,1])
    equal("entire_integral_initial_value",W(0),c0)
    equal("entire_integral_initial_derivative",mp.diff(W,0),c1)
    for y in [mp.mpf(".2"),mp.mpc(".7","-.3"),mp.mpc("-1.1",".4")]:
        equal("entire_integral_ode",mp.diff(W,y,2)-kap*kap*W(y),mp.exp(-q)*mp.exp(-q*(y-h)**2))
        x=mp.mpc(".3","-.1");t=mp.mpc("-.2",".05")
        u=lambda xx,yy,tt:mp.exp(1j*q*xx+1j*h*h*q*tt)*W(yy)
        result=mp.diff(lambda xx:u(xx,y,t),x,2)+mp.diff(lambda yy:u(x,yy,t),y,2)+eps*mp.diff(lambda tt:u(x,y,tt),t)
        equal("finite_mode_full_complex_operator",result,mp.exp(q*(1j*x+1j*h*h*t-(y-h)**2-1)))
p=mp.mpf(1)/4;h=mp.mpf(12)
equal("explicit_candidate_bound",-1-mp.log(p)-h*h*p/2,mp.log(4)-19)
holds("explicit_strict_candidate_gap",mp.log(4)-19<-(h+mp.mpf(3)/4))
for R in map(mp.mpf,[".1","1","4","20"]):
    for a in [0,1,3,7,21]:
        holds("unbounded_entire_homogeneous_cauchy_bound",1<=mp.exp(R)*mp.factorial(a)*R**(-a))
equal("example_cutoff_squared_distance",(mp.mpf(8)-2)**2-4,32)
equal("example_heat_kernel_distance_exponent",mp.mpf(32)/4,8)
for sigma in [mp.mpf(0),p/2,p]:
    equal("worked_vertical_bound",p/2+sigma-sigma*sigma/(2*p),
          mp.re((p-1j*sigma)**2/(2*p)+1j*(p-1j*sigma)))
record=dict(schema="AN02-analytic-learner-check260/v1",status="PASS",
    total_checks=sum(counts.values()),checks_by_kind=counts,precision_decimal_digits=90,
    tolerance="1e-65",max_scaled_error=str(worst),
    independent_entire_segment_integral_and_full_complex_operator=True,
    supplementary_only=True)
(OWN/"learner-checks260.json").write_text(json.dumps(record,indent=2)+"\n",encoding="utf-8")
print(json.dumps(record))
