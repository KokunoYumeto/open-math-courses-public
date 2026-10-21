"""Integer-only outward interval certificate for the numerical comparison.

No binary floating-point operations or special-function libraries are used.
Intervals have dyadic endpoints with denominator2**128. Logarithms are
enclosed by their integrated geometric series, after binary range reduction.
"""
from pathlib import Path
from math import isqrt, factorial, comb
from fractions import Fraction
import json

BITS=128
Q=1<<BITS
def ceildiv(a,b):return -((-a)//b)

class I:
    __slots__=('lo','hi')
    def __init__(self,lo,hi=None):self.lo=lo;self.hi=lo if hi is None else hi
    @staticmethod
    def of(x):return x if isinstance(x,I) else I(x*Q)
    def __add__(self,b):
        b=I.of(b);return I(self.lo+b.lo,self.hi+b.hi)
    __radd__=__add__
    def __neg__(self):return I(-self.hi,-self.lo)
    def __sub__(self,b):return self+-I.of(b)
    def __rsub__(self,b):return I.of(b)+-self
    def __mul__(self,b):
        b=I.of(b);v=[self.lo*b.lo,self.lo*b.hi,self.hi*b.lo,self.hi*b.hi]
        return I(min(v)//Q,ceildiv(max(v),Q))
    __rmul__=__mul__
    def __truediv__(self,b):
        b=I.of(b);assert b.lo>0
        vals=[(a*Q,c) for a in [self.lo,self.hi] for c in [b.lo,b.hi]]
        return I(min(a//c for a,c in vals),max(ceildiv(a,c) for a,c in vals))
    def __rtruediv__(self,b):return I.of(b)/self
    def __pow__(self,n):
        assert isinstance(n,int) and n>=0
        r=I.of(1);a=self
        while n:
            if n&1:r=r*a
            a=a*a;n//=2
        return r
    def lower_fraction(self):return str(Fraction(self.lo,Q))
    def upper_fraction(self):return str(Fraction(self.hi,Q))

def rat(a,b):return I(a*Q//b,ceildiv(a*Q,b))

def series_log_from_z(z):
    assert 0<=z.lo<=z.hi<=Q//2
    term=z;z2=z*z;total=I.of(0)
    for k in range(64):
        total=total+term/(2*k+1);term=term*z2
    # 2*z**129/(129*(1-z*z)) <2**(-128) for0<=z<=1/2.
    total=2*total
    return I(total.lo,total.hi+1)

LN2=series_log_from_z(rat(1,3))
def log_point(a):
    assert a>0
    exponent=a.bit_length()-BITS-1
    if exponent>=0:m=rat(a,1<<(BITS+exponent))
    else:m=rat(a<<(-exponent),Q)
    assert m.lo>=Q and m.hi<=2*Q+1
    z=(m-1)/(m+1)
    return series_log_from_z(z)+exponent*LN2

def log(x):
    x=I.of(x);assert x.lo>0
    return I(log_point(x.lo).lo,log_point(x.hi).hi)

def sqrt(x):
    x=I.of(x);assert x.lo>=0
    a=isqrt(x.lo*Q);b=isqrt(x.hi*Q)
    return I(a,b+(b*b<x.hi*Q))

E=sum((rat(1,factorial(k)) for k in range(65)),I.of(0))
# Sum after1/64! is bounded by2/65! <2**(-128).
E=I(E.lo,E.hi+1)
assert E.lo>rat(2718,1000).hi and E.hi<rat(2719,1000).lo
LN3=log(3);LN5=log(5);LN10=log(10);LN13=log(13)

# Independent exact arithmetic checks of the enclosure operations.
arithmetic_checks=0
for a in [Fraction(-7,3),Fraction(1,7),Fraction(23,4)]:
    for b in [Fraction(1,11),Fraction(2,3),Fraction(9,2)]:
        ia=rat(a.numerator,a.denominator);ib=rat(b.numerator,b.denominator)
        for interval,value in [(ia+ib,a+b),(ia*ib,a*b),(ia/ib,a/b)]:
            assert Fraction(interval.lo,Q)<=value<=Fraction(interval.hi,Q)
            arithmetic_checks+=1
for k in range(1,100):
    x=rat(k,7);s=sqrt(x)
    assert Fraction(s.lo,Q)**2<=Fraction(k,7)<=Fraction(s.hi,Q)**2
    arithmetic_checks+=1
for n in range(1,30):
    assert log(2**n).lo<=n*LN2.lo and log(2**n).hi>=n*LN2.hi
    arithmetic_checks+=1

def constants(g,log_factorial_n):
    n=g+1;x=log(n);y=log(4*n)
    eps=rat(1,200*g*g);lam=2*eps;kap=1+eps
    ag=g*y+5*x+15
    jg=12*(13+4*E**2)/(25+4*E**2)*n*y+56*x+54
    lz=g*2*LN2+(g+1)*x+log(1+lam)+log(jg)
    lc4=lz+log(8*n)+log(ag)
    c7=4*ag/((13+4*E**2)*g)
    lc5=x+g*LN2+(2*g+1)*lc4-log_factorial_n-g*log(6*c7)
    bg=lc5+4*g+4
    # Analytical bounds from22.204 and22.212 enclose the two exponentially
    # small terms without constructing exponentially large degree integers.
    i4=I(0,ceildiv(Q,100000*n*n))
    i5=I(0,ceildiv(Q,10**13*n**4))
    i6=rat(1,n*(1<<g))
    vg=(n*bg+g*LN3+LN2+1)*i4
    eg=(13*g+2)*i5
    direction=3+LN2+rat(3,2)*log(g)
    mg=vg+(13*g+1)*i5+(log(4*n)+lc4+2)*i6+g*c7*(12*n*n+1)+2*n*direction
    mm=mg+vg+LN5*i4
    kg=log(kap)+g*LN2+log_factorial_n+g*LN3+bg+g
    pg=kg+7*g+3+2*g*LN2+log(2*n)+lc4
    cg=pg+3+log(g*sqrt(g)*(g+2*n*(1+g*sqrt(g))))
    ar=vg+(n+log(n*n)+lc4+2)*i6+g*c7*(2*n*n+2)+n*(3*LN2+rat(g,4)*(1+2*LN2)+bg+x)
    sg=vg+bg*i4+(log(8*n)+lc4+2)*i6+g*c7*(12*n*n+1)+2*n*direction
    zg=(log(2*n)+lc4+2)*i4
    lc=log(2900000)+6*g*LN10+2*g*g*2*LN2+(2*g*g+9*g+rat(123,10))*x
    result=[]
    for periodic in [False,True]:
        r=kap/(jg-kap) if periodic else 2*kap/(jg-2*kap)
        growth=vg+(log((8 if periodic else 4)*n)+lc4+3)*i6+g*c7*((1+lam)*(2*E+1 if periodic else E)**2*n*n+1)+n*direction
        basis=n*cg if periodic else rat(3,2)*n*log(g)
        transfer=LN2*i4+(0 if periodic else n*(3+rat(3,2)*log(g)+2*LN2))
        amplification=16*n*n*ag*LN13 if periodic else 8*n*n*ag*(log(13*n)+lz)
        a=(r*mm+eg+ar+transfer+amplification+basis+2)/(1-r)
        height=r*(a+mm)+eg
        capacity=(11 if periodic else 7)*n*n*ag
        margin=(capacity-2*height-growth-basis-ar-2)/(n*n*ag)
        threshold=a+height+sg+zg+1+(pg+LN2)*i4
        log_ratio=log(threshold+i5)+lc5-lc
        result.append((margin,log_ratio))
    return result

min_margin=[None,None];max_log_ratio=None
log_factorial=I.of(0)
for g in range(1,10000):
    log_factorial=log_factorial+log(g+1)
    for case,(margin,ratio) in enumerate(constants(g,log_factorial)):
        assert margin.lo>(Q//2 if case==0 else 2*Q),(g,case,'contraction margin')
        assert ratio.hi<rat(-1,25).lo,(g,case,'David constant')
        if min_margin[case] is None or margin.lo<min_margin[case][1].lo:min_margin[case]=(g,margin)
        if max_log_ratio is None or ratio.hi>max_log_ratio[2].hi:max_log_ratio=(g,case,ratio)
    if g in [100,1000,5000]:print('Certified through g='+str(g),flush=True)

# Exact finite versions of the Hermite count and factorial denominator.
finite_checks=0
for N in range(1,21):
    for a in range(1,N+1):
        for b in range(1,N-a+1):
            assert factorial(N)%(a*b)==0
            finite_checks+=1
for S in range(100,301):
    for T in range(1,21):
        # The factors removed from the Hermite coefficient bound satisfy
        # T**2<=exp(T), and the remaining numerical estimates are proved
        # by log and exp series in the manuscript.
        assert 2*log(T).hi<=(I.of(T)).lo
        finite_checks+=1

result={'state':'passed','method':'Exact integer directed dyadic intervals;128 fractional bits;64-term integrated geometric log series;65-term exponential series.','finite_parameter_certificate':{'integers_g_from':1,'integers_g_through':9999,'branches_per_integer':2,'strict_inequalities_certified':39996,'nonperiodic_scaled_margin_lower_bound':'1/2','periodic_scaled_margin_lower_bound':'2','log_final_constant_ratio_upper_bound':'-1/25','smallest_margin_locations':[v[0] for v in min_margin],'largest_log_ratio_location':{'g':max_log_ratio[0],'periodic':bool(max_log_ratio[1])}},'interval_arithmetic_checks':arithmetic_checks,'additional_exact_checks':finite_checks,'tail':'All integers g>=10000 are covered by the elementary estimates in the manuscript, not by this finite loop.','limits':'This is a certificate for the explicit constant comparisons and listed finite examples. The mathematical extrapolation and arithmetic arguments are proved in the manuscript.'}
base=Path(__file__).resolve().parent
(base/'elliptic-numerical-extrapolation-check.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
print(json.dumps(result),flush=True)
