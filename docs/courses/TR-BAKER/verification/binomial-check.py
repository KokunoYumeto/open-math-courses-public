"""Supplementary rational boundary and sign-case checks for Theorems 13.5–13.6."""
from fractions import Fraction as Q
from math import factorial, log, log1p
import json

def exp_interval(t,N=30):
    lo=sum((t**k/Q(factorial(k)) for k in range(N+1)),Q(0))
    first=t**(N+1)/Q(factorial(N+1))
    ratio=t/Q(N+2)
    assert 0<=ratio<1
    return lo,lo+first/(1-ratio)

def run():
    # Endpoint and radius inequalities, certified in rational arithmetic.
    assert exp_interval(Q(1))[1]<3
    assert exp_interval(Q(3,2))[1]<5
    assert exp_interval(Q(5,2))[0]>10
    assert exp_interval(Q(2))[0]>5
    log2_lower=2*sum((Q(1,3)**(2*k+1)/Q(2*k+1) for k in range(15)),Q(0))
    assert log2_lower>Q(69,100)
    assert 214*Q(69,100)**3>Q(702,10)
    assert Q(6,5)**4<5
    assert 3+43200*21**2==19051203<10**8
    assert 1+Q(25,2)/Q(3,2)<10
    assert 44*100<100000
    assert 214*15**2==48150<100000
    counts={"sum":0,"large_remainder":0,"logarithmic":0,"equal_bases":0,"equal_coefficients":0}
    for a in [-4,-3,-2,-1,1,2,3,4]:
      for b in [-4,-3,-2,-1,1,2,3,4]:
       for x in [-5,-4,-3,-2,-1,1,2,3,4,5]:
        for y in [-5,-4,-3,-2,-1,1,2,3,4,5]:
         for n in range(3,10):
          c=a*x**n-b*y**n
          if c==0 or abs(x*y)<=1: continue
          X,Y=max(abs(x),abs(y)),min(abs(x),abs(y))
          A,B=(abs(a),abs(b)) if abs(x)>=abs(y) else (abs(b),abs(a))
          P,R=A*X**n,B*Y**n
          H=max(1,log(abs(a)),log(abs(b)),log(abs(c)))
          if (a*x**n)*(b*y**n)<0:
              assert P+R==abs(c) and X**n<=abs(c)
              counts["sum"]+=1
          elif 2*abs(c)>=P:
              assert X**n<=2*abs(c)
              counts["large_remainder"]+=1
          else:
              u=Q(R-P,P)
              assert abs(u)<Q(1,2) and abs(R-P)==abs(c)
              g=log1p(float(u))
              assert abs(g)<=2*abs(float(u))*(1+1e-14)
              a2=max(1,log(X))
              assert a2<=2*log(X) and 1/a2+n/H<=1+n/H+1e-12
              counts["logarithmic"]+=1
              counts["equal_bases"]+=X==Y
              counts["equal_coefficients"]+=A==B
    assert all(counts[k]>0 for k in counts)
    # Family's excluded small-y range is an integer inequality for all sampled parameters.
    small_y=0
    for b in range(1,61):
      for n in range(3,14):
       for y in range(2,b+2):
        assert (b+1)*(y-1)**n < b*y**n
        small_y+=1
    return {"state":"passed","exact_endpoint_and_radius_checks":11,"sign_cases":counts,
            "small_y_integer_checks":small_y,
            "scope":"Rational endpoint margins and finite diagnostic cases; monotonicity and all-parameter proofs are in the lesson."}

if __name__=="__main__":
    print(json.dumps(run(),indent=2))
