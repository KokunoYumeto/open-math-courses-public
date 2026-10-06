"""Exact uniform margins for the corrected real-radius 8550 estimate.

GPT-6.1 Sol (OpenAI), Codex, Ultra; CC0. N. Gouillon's 2006 real-radius
mechanism and constants are credited. The course explicitly uses log(D/v),
v=log E, keeping E>=2 and the stated coefficient/265/150 cutoffs.
The entire symbolic proof is in Lesson7; these are its rational margins.
"""
from fractions import Fraction as F
import json
from laurent_constant import Interval as I, LN2, decimal_out

def cbrt(v):
    v=I.of(v);scale=1<<128
    def floor_root(q):
        target=q.numerator*scale**3//q.denominator
        lo,hi=0,1<<((target.bit_length()+2)//3)
        while hi-lo>1:
            mid=(lo+hi)//2
            if mid**3<=target:lo=mid
            else:hi=mid
        assert lo**3<=target<(lo+1)**3
        return lo
    assert v.lo>0
    return I(F(floor_root(v.lo),scale),F(floor_root(v.hi)+1,scale))

c0=368;c1=F(5141,1000);mu=F(946,1000);g=F(241,1000);ga=F(1309,1000)
L0=c1*265
C0=cbrt(3)+1/cbrt(L0)
theta=(1-1/I(L0)+(1-2/I(L0)).sqrt())/8
M0=(I(3).log()/3+F(1,2700))*cbrt(2*ga)**2/(cbrt(3)*cbrt(g)**2)
M0*=cbrt(F(2701,2700))
qm=F(3965,1000)+mu*(1-I(mu).log())
assert qm.lo>F(49,10)
delta=mu*(2+(M0*cbrt(c0)/mu).log())-F(3965,1000)
delta+=mu*qm.log()-(ga-1)*qm
assert delta.hi<F(34,1000)
# r<=1.1 implies t>14; the derivative surplus is then negative.
assert (1+(F(3965,1000)-mu*I(14).log())/14).lo>F(11,10)
assert (-(ga-1)*14+mu*(2+(M0*cbrt(c0)*F(11,10)/mu).log())).hi<0
assert (1+(F(3965,1000)-mu*I(8).log())/8).lo>F(12,10)
# P decreases up to265/150 because the square-root derivative dominates;
# beyond that breakpoint every term decreases.
assert (g/(2*I(c0).sqrt()*(I(F(265,150))**3).sqrt())).lo>ga/(265*c1)

def P(r):
    r=F(r)
    return ((F(1,3)+ga*r/265)/c1+g/I(c0*r).sqrt()+5*g/(36*c0*r)
            +3*cbrt(g)**2*cbrt(ga)*C0/(cbrt(2)**2*cbrt(c0)))

W=1/(c1*150*qm)+1/(c0*c0*54**2*qm)
W+=C0*cbrt(g)**2/(cbrt(2*ga)**2*cbrt(c0)*qm)
coef_const=F(2794,1000)-I(3).log()
dependent_degree_bound=2*I(4).log()-2+coef_const
assert dependent_degree_bound.hi<F(2468,1000)
H14=(2*I(14).log()+coef_const)/(3*c1*265*14)
H8=(2*I(8).log()+coef_const)/(3*c1*265*8)
Hglobal=2*(coef_const/2-1).exp()/(3*c1*265)
assert H14.hi<F(123,1000000)
assert H8.hi<F(180,1000000)
assert Hglobal.hi<F(421,1000000)
assert dependent_degree_bound.hi/(3*c1*265*14)<H14.lo
assert dependent_degree_bound.hi/(3*c1*265*8)<H8.lo
assert (dependent_degree_bound/(3*c1*150*qm)).hi<Hglobal.lo
assert (2*I(8).log()+coef_const).lo>2
assert (F(1)-coef_const/2).exp().lo>LN2.hi

margins=[theta-P(1)-F(123,1000000),
         theta-P(F(11,10))-F(34,1000)*W-F(180,1000000),
         theta-P(F(12,10))-F(34,1000)*W-F(421,1000000)]
assert all(v.lo>0 for v in margins)
# Conversion works also log2<=v<1, without inserting v>=1.
assert F(1,100000)/LN2.lo<F(15,1000000)
converted=F(500015,1000000)*(1+F(2,c0*54))*(1+1/L0)*c0*c1*9
assert converted<8550
omega2=(-50+(20*ga+1)/mu)*qm+20*F(34,1000)/mu
assert omega2.hi<0
assert (I(qm.lo/mu)+LN2.log()).lo>0 # Q/mu + log(v)>0 at v=log2
assert LN2.lo*c0*54>13770

result={'status':'passed','Q_min_lower':decimal_out(qm.lo,12),
        'derivative_excess_upper':decimal_out(delta.hi,12,up=True),
        'three_uniform_margin_lowers':[decimal_out(v.lo,12) for v in margins],
        'converted_coefficient_upper':decimal_out(converted,12,up=True),
        'scope':'Corrected Q=max(v/D,v/D+0.946log(D/v)+3.965), E>=2, exact original coefficient/265/150 cutoffs. All-degree/radius symbolic allocation; no78500claim.'}
if __name__=='__main__':print(json.dumps(result,indent=2))
