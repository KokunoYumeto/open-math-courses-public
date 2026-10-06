"""Exact finite-integral certificates for the d=1, K=3 mollifier.

All certificate operations use Fraction. Decimal logarithms are descriptive.
The analytic identities are proved in Section 26 of the course lesson
Zeros on the critical line: Hardy and the mollifier method.
"""
from fractions import Fraction as F
from math import comb, factorial
from functools import lru_cache
from pathlib import Path
import json
import mpmath as mp

ZERO=(0,0,0)
def clean(p): return {m:c for m,c in p.items() if c}
def add(*ps):
    q={}
    for p in ps:
        for m,c in p.items(): q[m]=q.get(m,F(0))+c
    return clean(q)
def scale(p,c): return clean({m:v*c for m,v in p.items()})
def mul(p,q):
    r={}
    for a,c in p.items():
        for b,d in q.items():
            m=tuple(x+y for x,y in zip(a,b))
            r[m]=r.get(m,F(0))+c*d
    return clean(r)
def power(p,n):
    r={ZERO:F(1)}
    for _ in range(n): r=mul(r,p)
    return r
def upoly(cs): return clean({(i,0,0):F(c) for i,c in enumerate(cs)})
def du(p): return clean({(i-1,j,k):c*i for (i,j,k),c in p.items() if i})
def translate(p,axis):
    q={}
    for (i,j,k),c in p.items():
        assert j==k==0
        for a in range(i+1):
            m=[i-a,0,0]; m[axis]=a
            q[tuple(m)]=q.get(tuple(m),F(0))+c*comb(i,a)*(-1)**a
    return clean(q)

def operator_kernels(Q,R,theta,second):
    """Four polynomials multiplying f0*g0, fx*g0, f0*gy, fx*gy."""
    raw=[{} for _ in range(4)]
    def D(k,l):
        return -F(factorial(k+l),1)/(2*R)**(k+l+1)
    for i,qi in enumerate(Q):
        for j,qj in enumerate(Q):
            if not qi or not qj: continue
            for k in range(i+1):
                for l in range(j+1):
                    m=(i-k,j-l)
                    z=qi*qj*(-1)**(i+j)*comb(i,k)*comb(j,l)
                    vals=[D(k,l),
                          k*D(k-1,l) if k else F(0),
                          l*D(k,l-1) if l else F(0),
                          k*l*D(k-1,l-1) if k and l else F(0)]
                    for p,v in zip(raw,vals): p[m]=p.get(m,F(0))+z*v
    if second:
        a={ZERO:F(-1),(0,1,0):theta}
        b={ZERO:F(-1),(0,0,1):theta}
    else:
        a={(0,0,1):-theta}; b={(0,1,0):-theta}
    ap=[power(a,i) for i in range(len(Q))]
    bp=[power(b,i) for i in range(len(Q))]
    return [add(*(scale(mul(ap[i],bp[j]),c)
                  for (i,j),c in p.items())) for p in raw]

def coefficient(k,l,r,q):
    return F((-1)**(k+l-r-q)*factorial(k)*factorial(l),
             factorial(r)*factorial(q))*sum(
        (F(1,factorial(j)*factorial(k-j-r)*factorial(l-j-q))
         for j in range(min(k-r,l-q)+1)),F(0))

def build_integrands(P,Q,R,theta,second):
    kernels=operator_kernels(Q,R,theta,second)
    groups={(False,False):{},(True,False):{},
            (False,True):{},(True,True):{}}
    one_minus_u={ZERO:F(1),(1,0,0):F(-1)}
    for k,Pk in P.items():
        for l,Pl in P.items():
            for r in range(k+1):
                for q in range(l+1):
                    c=coefficient(k,l,r,q)
                    p=1+k+l-r-q
                    active=(r>=2,q>=2)
                    left=translate(Pk,1) if active[0] else Pk
                    right=translate(Pl,2) if active[1] else Pl
                    if second:
                        # The first polynomial has parameter -theta*x;
                        # the second has parameter -theta*y.
                        f0=add(du(Pk),scale(Pk,R*theta)) if r==0 else left
                        fx=scale(Pk,-theta) if r==0 else {}
                        g0=add(du(Pl),scale(Pl,R*theta)) if q==0 else right
                        gy=scale(Pl,-theta) if q==0 else {}
                    else:
                        # x belongs to the right, y to the left.
                        f0=add(du(Pl),scale(Pl,-R*theta)) if q==0 else right
                        fx=scale(Pl,theta) if q==0 else {}
                        g0=add(du(Pk),scale(Pk,-R*theta)) if r==0 else left
                        gy=scale(Pk,theta) if r==0 else {}
                    core=add(mul(kernels[0],mul(f0,g0)),
                             mul(kernels[1],mul(fx,g0)),
                             mul(kernels[2],mul(f0,gy)),
                             mul(kernels[3],mul(fx,gy)))
                    weight=power(one_minus_u,p-1)
                    if active[0]: weight=mul(weight,{(0,r-2,0):F(1,factorial(r-2))})
                    if active[1]: weight=mul(weight,{(0,0,q-2):F(1,factorial(q-2))})
                    term=scale(mul(core,weight),c/F(factorial(p-1)))
                    groups[active]=add(groups[active],term)
    return groups

def integrate(groups,lam):
    """Return coefficients of 1,e^lam,e^(2lam), by exact integration."""
    @lru_cache(None)
    def J(i,q):
        if q==0: return (F(1,i+1),F(0),F(0))
        z=q*lam
        out=[F(0)]*3
        out[q]=F(1)/z
        out[0]=-F(1)/z
        if i:
            prev=J(i-1,q)
            out=[-F(i)/z*v for v in prev]
            out[q]+=F(1)/z
        return tuple(out)
    @lru_cache(None)
    def inner(j):
        # int_0^u t^j exp(lam*t) dt = exp(lam*u)*P_j(u)+constant.
        return tuple((1,m,F((-1)**(j-m)*factorial(j),factorial(m))/lam**(j-m+1))
                     for m in range(j+1))+(
                         (0,0,-F((-1)**j*factorial(j))/lam**(j+1)),)
    @lru_cache(None)
    def moment(i,j,k,a,b):
        if (not a and j) or (not b and k): return (F(0),)*3
        left=inner(j) if a else ((0,0,F(1)),)
        right=inner(k) if b else ((0,0,F(1)),)
        out=[F(0)]*3
        for q,m,c in left:
            for r,n,d in right:
                vals=J(i+m+n,q+r)
                out=[x+c*d*y for x,y in zip(out,vals)]
        return tuple(out)
    out=[F(0)]*3
    for (a,b),poly in groups.items():
        for (i,j,k),c in poly.items():
            vals=moment(i,j,k,a,b)
            out=[x+c*y for x,y in zip(out,vals)]
    return tuple(out)

def exp_interval(x,n=140):
    assert x>=0 and x<n+2
    lo=sum((x**k/F(factorial(k)) for k in range(n+1)),F(0))
    hi=lo+x**(n+1)/F(factorial(n+1))/(1-x/F(n+2))
    return lo,hi
def bound_expression(terms):
    lo=hi=F(0)
    for x,c in terms.items():
        a,b=exp_interval(x)
        lo+=c*(a if c>=0 else b)
        hi+=c*(b if c>=0 else a)
    return lo,hi
def dec(x):
    return mp.mpf(x.numerator)/x.denominator
def rounded_interval(lo,hi,den=10**12):
    return F(lo.numerator*den//lo.denominator,den),F(-((-hi.numerator*den)//hi.denominator),den)
def c_expression(P,Q,R,theta):
    first=integrate(build_integrands(P,Q,R,theta,False),R*theta)
    second=integrate(build_integrands(P,Q,R,theta,True),-R*theta)
    out={}
    for n,c in enumerate(first):
        x=n*R*theta; out[x]=out.get(x,F(0))+c/theta
    for n,c in enumerate(second):
        x=2*R-n*R*theta; out[x]=out.get(x,F(0))-c/theta
    return {x:c for x,c in out.items() if c}

def shaped_P(coefs):
    u={(1,0,0):F(1)}
    base=upoly([0,1])
    one_minus_u={ZERO:F(1),(1,0,0):F(-1)}
    return add(base,*(scale(mul(u,power(one_minus_u,j)),F(c))
                      for j,c in enumerate(coefs,1)))
def Q_odd(base,coefs):
    z=upoly([1,-2])
    p=add(upoly([F(base)]),*(scale(power(z,j),F(c)) for j,c in coefs.items()))
    a=[p.get((i,0,0),F(0)) for i in range(max(i for i,j,k in p)+1)]
    a=[x/a[0] for x in a]  # exact Q(0)=1
    return a

mp.mp.dps=70
Ptest={0:upoly([0,F(25,28),0,F(3,28)])}
Rt=F(13,10); tt=F(49,100); lt=2*Rt
test=c_expression(Ptest,[F(1),F(-1)],Rt,tt)
I1=F(989,980); I0=F(629,2058)
expected={F(0):F(1,2)-I1/tt*(lt**2+2*lt+2)/lt**3
          +tt*I0*(-F(1)/(2*lt)+F(1,2)-lt/4),
          lt:I1/tt*2/lt**3+tt*I0/(2*lt)}
assert test==expected, (test,expected)
print("Classical constant: exact symbolic agreement.",flush=True)

theta=F(4,7)-F(1,10**12)  # fixed, strictly below 4/7
assert theta<F(4,7)
cases=[
 ("critical_line",F("1.3036"),F("0.417293962"),
  {0:shaped_P(["0.261076","-1.071007","-0.236840","0.260233"]),
   2:upoly([0,F("1.048274"),F("1.319912"),F("-0.940058")]),
   3:upoly([0,-F("0.522811"),F("0.686510"),F("0.049923")])},
  Q_odd("0.490464",{1:"0.636851",3:"-0.159327",5:"0.032011"})),
 ("simple_critical_line",F("1.1167"),F("0.407511457"),
  {0:shaped_P(["0.052703","-0.657999","-0.003193","-0.101832"]),
   2:upoly([0,F("1.049837"),F("-0.097446")]),
   3:upoly([0,-F("0.035113"),F("0.156465")])},
  Q_odd("0.483777",{1:"0.516223"}))
]
records=[]
for name,R,target,P,Q in cases:
    assert Q[0]==1
    assert sum(P[0].values())==1 and all(ZERO not in p for p in P.values())
    print("Building "+name+"...",flush=True)
    terms=c_expression(P,Q,R,theta)
    lo,hi=bound_expression(terms)
    clo,chi=rounded_interval(lo,hi)
    lower_exp=exp_interval(R*(1-target),n=30)[0]
    margin=lower_exp-chi
    assert margin>F(1,10**10), (name,str(chi),str(margin))
    c_approx=sum((dec(c)*mp.exp(dec(x)) for x,c in terms.items()),mp.mpf(0))
    records.append({
      'claim':name,'theta':str(theta),'R':str(R),'strict_target':str(target),
      'P':{str(k):{str(i):str(c) for (i,j,l),c in p.items()} for k,p in P.items()},
      'Q_coefficients':[str(x) for x in Q],
      'exponential_expression':[{'exponent':str(x),'coefficient':str(c)} for x,c in terms.items()],
      'c_lower':str(clo),'c_upper':str(chi),
      'positive_certificate_margin':str(margin),
      'compact_margin_lower':str(F(1,10**10)),
      'c_descriptive':mp.nstr(c_approx,35),
      'proportion_descriptive':mp.nstr(1-mp.log(c_approx)/dec(R),35),
      'certificate_exact':True})
    print(name+": c in ["+str(clo)+","+str(chi)+"], proportion "+
          mp.nstr(1-mp.log(c_approx)/dec(R),20),flush=True)

result={
 'nature':'Exact Fraction polynomial differentiation and finite integral recurrences. Exponentials have positive degree140 Taylor lower sums and geometric tail upper bounds. Degree30 positive sums prove exp(R*(1-target))>c_upper. mpmath only prints descriptive decimals.',
 'classical_formula_exact_symbolic_agreement':True,
 'cases':records,'all_assertions_passed':True}
Path(__file__).with_suffix('.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
