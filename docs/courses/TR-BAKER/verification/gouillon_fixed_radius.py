"""Rational interval certificate for Gouillon's 9400 and 7200 estimates.

GPT-6.1 Sol (OpenAI), Codex, Ultra; CC0. The source constants and fixed
radius substitutions are N. Gouillon's (2006), Corollaries 2.2–2.3.
The course supplies a complete deduction using its proved log(3) criterion.
Scalar checks certify the explicit uniform majorants, not a finite sweep
as a substitute for their symbolic proof. Standard library only.
"""
from fractions import Fraction as F
import json
from laurent_constant import Interval as I, decimal_out

def cbrt(v):
    v=I.of(v)
    assert v.lo>0
    scale=1<<128
    def floor_root(q):
        target=q.numerator*scale**3//q.denominator
        lo,hi=0,1<<((target.bit_length()+2)//3)
        while hi-lo>1:
            mid=(lo+hi)//2
            if mid**3<=target:lo=mid
            else:hi=mid
        assert lo**3<=target<(lo+1)**3
        return lo
    return I(F(floor_root(v.lo),scale),F(floor_root(v.hi)+1,scale))

mu=F(946,1000); gamma=F(1309,1000); g=F(241,1000)
M0=(I(3).log()/3+F(1,2700))*cbrt(2*gamma)**2
M0/=cbrt(3)*cbrt(g)**2
M0*=cbrt(F(2701,2700))

rows=[]
for name,E,c0,c1,m,q0,q1,delta,target in [
 ('complex',F(66,10),317,F(5378,1000),F(86,10),F(3317,1000),F(1888,1000),F(39,1000),9400),
 ('positive_real',F(55,10),313,F(5386,1000),F(65,10),F(3409,1000),F(1705,1000),F(395,10000),7200)]:
    lam=I(E).log()
    assert 1<lam.lo<lam.hi<q1
    assert 3*lam.hi<m
    assert 265*lam.hi<1000
    qm=q0+mu*(1+I(q1/mu).log())
    assert qm.lo>F(49,10)
    assert qm.lo>mu/(gamma-1)
    dq=q0+q1
    k0=c0*m*m*dq/lam**3
    l0=c1*1000/lam
    assert k0.lo/2>l0.hi
    C=cbrt(3)+1/cbrt(l0)
    theta=(1-1/l0+(1-2/l0).sqrt())/8
    excess=mu*(2+(M0*cbrt(c0)/(mu*lam)).log())-q0
    excess+=mu*qm.log()-(gamma-1)*qm
    assert excess.hi<delta
    # Bounds for the five height/arithmetic terms, with a_j >= m,
    # DQ >= q0+q1, Dh >= 1000, Q/h <= 1/150.
    psi=(F(1,3)+gamma/F(150))/c1
    psi+=g/(c0*dq/lam).sqrt()+g*lam**2/(c0*m*dq)
    psi+=3*cbrt(g)**2*cbrt(gamma)*C/(cbrt(2)**2*cbrt(c0))
    # D T / [(K+1)(L+1)lambda]: each of the three terms in T.
    tnorm=1/(150*c1*qm)+lam**5/(c0*c0*m**4*qm**2)
    tnorm+=C*cbrt(g)**2/(cbrt(2*gamma)**2*cbrt(c0)*qm)
    margin=theta-psi-delta*tnorm
    assert margin.lo>0
    coeff_cut=-I(m).log()+lam.log()+lam+F(524,1000)
    assert coeff_cut.hi<F(31,10)
    # Full conversion bound (7.71), using the actual larger minima.
    converted=F(50001,100000)*(1+2/k0)*(1+1/l0)*c0*c1*m*m/lam**3
    assert converted.hi<target
    # Omega2 now includes the bounded derivative excess delta.
    omega2=(-50+(20*gamma+1)/mu)*qm+20*delta/mu
    assert omega2.hi<0
    assert c1*150*qm.lo>3700
    assert F(249,1000)-gamma/2700>F(2485,10000)
    rows.append({'case':name,'Q_min':[decimal_out(qm.lo,12),decimal_out(qm.hi,12,up=True)],
                 'derivative_excess_upper':decimal_out(excess.hi,12,up=True),
                 'chosen_delta':str(delta),'normalized_margin_lower':decimal_out(margin.lo,12),
                 'converted_coefficient_upper':decimal_out(converted.hi,12,up=True),
                 'target':target})

result={'status':'passed','cases':rows,
        'scope':'Uniform outward rational scalar certificates for full symbolic 9400/7200 deductions; no 8550/78500 claim.'}
if __name__=='__main__':print(json.dumps(result,indent=2))
