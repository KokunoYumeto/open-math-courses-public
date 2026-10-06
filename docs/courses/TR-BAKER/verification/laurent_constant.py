"""Exact interval checks for Laurent's constant and the numerical proof margins.

Original certificate: GPT-6.1 Sol (OpenAI), in Codex, Ultra; October 2026.
CC0. Mathematical source: M. Laurent, Acta Arith. 133 (2008), 325-348,
Theorems 1-2 and Corollary 1. The course supplies the proof and bridge lemmas.
Only Python's standard library and rational/integer arithmetic are used.
"""
from fractions import Fraction as F
from math import isqrt
import json

BITS = 128
SCALE = 1 << BITS

def lower(x):
    return F((x.numerator * SCALE) // x.denominator, SCALE)

def upper(x):
    return -lower(-x)

class Interval:
    def __init__(self, lo, hi=None):
        lo = F(lo); hi = lo if hi is None else F(hi)
        assert lo <= hi
        self.lo, self.hi = lower(lo), upper(hi)

    @staticmethod
    def of(value):
        return value if isinstance(value, Interval) else Interval(value)

    def __add__(self, value):
        q = self.of(value)
        return Interval(self.lo + q.lo, self.hi + q.hi)

    __radd__ = __add__

    def __neg__(self):
        return Interval(-self.hi, -self.lo)

    def __sub__(self, value):
        return self + (-self.of(value))

    def __rsub__(self, value):
        return self.of(value) - self

    def __mul__(self, value):
        q = self.of(value)
        ends = [a*b for a in [self.lo,self.hi] for b in [q.lo,q.hi]]
        return Interval(min(ends), max(ends))

    __rmul__ = __mul__

    def __truediv__(self, value):
        q = self.of(value)
        assert q.lo*q.hi > 0
        return self * Interval(1/q.hi, 1/q.lo)

    def __rtruediv__(self, value):
        return self.of(value)/self

    def __pow__(self, n):
        assert isinstance(n, int) and n >= 0
        out = Interval(1); v = self
        while n:
            if n & 1: out = out*v
            v = v*v; n //= 2
        return out

    def sqrt(self):
        assert self.lo >= 0
        def floor_root(x):
            return isqrt((x.numerator*SCALE*SCALE)//x.denominator)
        return Interval(F(floor_root(self.lo), SCALE),
                        F(floor_root(self.hi)+1, SCALE))

    def log(self):
        assert self.lo > 0
        def log_q(x):
            # Reduce to [1,2), where the atanh series has t <= 1/3.
            k = 0
            while x >= 2: x /= 2; k += 1
            while x < 1: x *= 2; k -= 1
            t = (x-1)/(x+1)
            total = 2*sum((t**(2*j+1))/F(2*j+1) for j in range(61))
            tail = 2*t**123/(123*(1-t*t))
            ln2 = log_unit(F(2))
            return Interval(total,total+tail) + k*ln2
        a, b = log_q(self.lo), log_q(self.hi)
        return Interval(a.lo,b.hi)

    def exp(self):
        def exp_q(x):
            if x < 0: return 1/exp_q(-x)
            assert x <= 6
            term = F(1); total = term
            for j in range(1,61):
                term *= x/j; total += term
            first = term*x/61
            tail = first/(1-x/62)
            return Interval(total,total+tail)
        a,b = exp_q(self.lo), exp_q(self.hi)
        return Interval(a.lo,b.hi)

def log_unit(x):
    t = (x-1)/(x+1)
    total = 2*sum((t**(2*j+1))/F(2*j+1) for j in range(61))
    tail = 2*t**123/(123*(1-t*t))
    return Interval(total,total+tail)

def atan_q(x, terms):
    total = sum((-1)**j*x**(2*j+1)/F(2*j+1) for j in range(terms))
    nxt = (-1)**terms*x**(2*terms+1)/F(2*terms+1)
    return Interval(min(total,total+nxt),max(total,total+nxt))

# Machin's identity: pi/4 = 4 atan(1/5) - atan(1/239).
# The tangent addition formula gives exactly 1, with the angle in (0,pi/2).
PI = 16*atan_q(F(1,5),31) - 4*atan_q(F(1,239),10)
E = Interval(1).exp()
LN2 = Interval(2).log()

def constants(h, a1, a2, rho=F(63,10), mu=F(14,25)):
    h,a1,a2,rho,mu = map(Interval.of,(h,a1,a2,rho,mu))
    sigma = (1+2*mu-mu*mu)/2
    lam = sigma*rho.log()
    H = h/lam+1/sigma
    omega = 2*(1+(1+1/(4*H*H)).sqrt())
    theta = (1+1/(4*H*H)).sqrt()+1/(2*H)
    rootomega = omega.sqrt()
    omega_quarter = rootomega.sqrt()
    theta_quarter = theta.sqrt().sqrt()
    omega_five_fourths = omega*omega_quarter
    radical = (omega*omega/9
               + 8*lam*omega_five_fourths*theta_quarter/(3*(a1*a2).sqrt()*H.sqrt())
               + F(4,3)*(1/a1+1/a2)*lam*omega/H)
    C = mu/(lam**3*sigma)*(omega/6+radical.sqrt()/2)**2
    Cp = (C*sigma*omega*theta/(lam**3*mu)).sqrt()
    U = h+lam/sigma
    A0 = Cp*U*U*a1*a2
    Cpp = (1+lam/(h*sigma))**2*(C+(omega*theta).sqrt()/(U*a1*a2)
                                + A0.log()/(U*U*a1*a2))
    return Cpp*a1*a2,lam

C1,lam = constants(20,F(83,10),F(83,10))
assert F(251203,10000) < C1.lo < C1.hi < F(251205,10000)
cutoff = -Interval(F(83,10)).log()+lam.log()+F(181,100)
assert cutoff.hi < F(21,100)

root17 = Interval(17).sqrt()
H = Interval(2)
omega = 2*(1+(1+1/(4*H*H)).sqrt())
theta = (1+1/(4*H*H)).sqrt()+1/(2*H)
omega_three_fourths = omega.sqrt()*omega.sqrt().sqrt()
F2 = (omega_three_fourths*H.sqrt()/(6*theta.sqrt().sqrt())
      + (omega*omega.sqrt()*H/(9*theta.sqrt())
         + 8*omega_three_fourths*H.sqrt()/(3*theta.sqrt().sqrt())
         + 8*omega.sqrt()/(3*theta.sqrt())).sqrt()/2)
assert F2.lo > F(266,100)

K = Interval(8)
f8 = (((1+(K-1).sqrt())*K.sqrt()/(K-1)).log()
      + K.log()/(6*K*(K-1))+F(3,2)+(6/(3+root17)).log()
      +(K/(K-1)).log()/(K-1))
assert f8.hi < F(7,4)

c0 = -2*((5+root17)/4).log()+(2*PI/E.sqrt()).log()+Interval(F(32,21)).log()+F(7,4)
def phi(k):
    k = Interval(k)
    return F(3,50)*k-k.log()+c0+2/(1+(k-1).sqrt())
def dphi(k):
    k = Interval(k); r=(k-1).sqrt()
    return F(3,50)-1/k-1/(r*(1+r)**2)
assert dphi(19).hi < 0 < dphi(20).lo
assert phi(19).lo > F(437,1000)
assert dphi(19).lo > -F(2,1000)

N = Interval(32)
epsilon_upper = 2/N*(F(3,2)*N.log()+(2*PI).log()/2
                    +1/(12*N)+(1+((E-1)/E)**32).log())
assert epsilon_upper.hi < F(2,5)

geometry = F(3,2)*(4/(3+root17))**2+1+1/Interval(7).sqrt()
assert geometry.hi < F(186,100)
perturb = (12*Interval(-F(28,5)).exp()).exp()/2
assert perturb.hi < F(53,100)

# E-dependent positive-real estimate, uniformly for v=log E >= log 2.
# h=10v and a1=a2=(7/3)v majorize the coefficient for the chosen
# scale a_j=(7/2) D log A_j. All remaining dependence is log(ca*v)/v,
# which decreases because ca*v > e.
MU = Interval(F(14,25))
SIGMA = (1+2*MU-MU*MU)/2
HE = 11/SIGMA
OE = 2*(1+(1+1/(4*HE*HE)).sqrt())
TE = (1+1/(4*HE*HE)).sqrt()+1/(2*HE)
CE = MU/SIGMA**4*(OE/6+(OE*OE/9
       +8*SIGMA*F(3,7)*OE*OE.sqrt().sqrt()*TE.sqrt().sqrt()/(3*HE.sqrt())
       +F(8,3)*F(3,7)*SIGMA*OE/HE).sqrt()/2)**2
CPE = (CE*OE*TE/(SIGMA*SIGMA*MU)).sqrt()
CAE = F(5929,9)*CPE
assert (CAE*LN2).lo > E.hi
LMN_MAJORANT = F(5929,400)*(CE+F(9,539)*(OE*TE).sqrt()
                         +F(9,5929)*(CAE*LN2).log()/LN2)
assert LMN_MAJORANT.hi < F(34419,1000) < F(351,10)
real_cutoff = SIGMA.log()-Interval(F(7,2)).log()+F(181,100)
assert real_cutoff.hi < F(47,100)

# Unit-circle specialization of the same refined determinant theorem.
UC = Interval(F(23,5))
UA1 = 22*PI
ULOG = Interval(22).log()
ULAM = F(23,25)*ULOG
UR = (UC/UA1).sqrt()
US = (UC*UA1).sqrt()
UA,UL = Interval(40),Interval(11)
unit_b_ratio = F(5,2)*(UR+US/UA+1/(2*UA)+F(3,2)/(UA*UL))/(UC-1/(UA*UL))
assert unit_b_ratio.hi < F(392,1000)
assert Interval(F(392,1000)).log().hi < -F(9,10)
unit_geometry = (US/2+F(1,8)+UA1/(2*UA*UL)+1/(8*UL)
                -UC/12*(UA1/(US+F(1,2)+1/(2*UL))
                         +1/(UR+2/(UA*UL))))
assert unit_geometry.hi < F(623,100)
unit_main = UC*ULAM/2
assert unit_main.lo > F(654,100)
assert (F(51,10)-ULOG-ULAM/2).lo > 0
unit_arithmetic = (ULAM*(UL+1)/12+1)*((UC+1)*UA*UL*UL).log()/(UA*UL*UL)
assert unit_arithmetic.hi < F(9,1000)
unit_exponent = 8*F(3,5)*UC/(F(23,25)**2*ULOG)
assert unit_exponent.hi < F(844,100)
unit_offset = Interval(25).log()-F(47,20)
assert (Interval(1156).log()-unit_offset).lo > 6
assert UR.hi+F(2,440) < 1
assert US.hi+F(1,2)+F(1,22) < 40

def decimal_out(x, places, up=False):
    scale = 10**places
    n = (x.numerator*scale)//x.denominator
    if up and F(n,scale) < x: n += 1
    return f"{n//scale}.{n%scale:0{places}d}"

RESULT = {
    "status":"all exact rational interval checks passed",
    "laurent_complex_constant_interval":[decimal_out(C1.lo,8),decimal_out(C1.hi,8,True)],
    "upper_constant":"25.2",
    "E_dependent_coefficient_majorant":[decimal_out(LMN_MAJORANT.lo,8),
                                       decimal_out(LMN_MAJORANT.hi,8,True)],
    "E_dependent_upper_constant":"35.1",
    "unit_circle_logarithmic_main_coefficient":[decimal_out(unit_exponent.lo,8),
                                               decimal_out(unit_exponent.hi,8,True)],
    "unit_circle_margin":"main > 6.54, geometry < 6.23, arithmetic < 0.009",
    "proof_margin_checks":["coefficient cutoff","K >= 8","factorial f(8)","convex remainder minimum",
                           "epsilon(32)","rectangle prefactor","perturbation exponential"],
    "rounding":"outward rational rounding after every operation; 128 binary fractional bits",
    "arithmetic":"integers and Fraction only"
}

if __name__ == "__main__":
    print(json.dumps(RESULT,indent=2))

