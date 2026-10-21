"""Finite checks for22.211--217; general proofs are in the manuscript."""
from pathlib import Path
from fractions import Fraction as F
from collections import Counter
from math import comb, factorial, prod
from itertools import product
import json
import mpmath as mp
import sympy as sp

base=Path(__file__).resolve().parent
counts=Counter()
def check(name,condition):
    assert condition,name
    counts[name]+=1

# These compare actual finite normal-index counts with the proposed bounds,
# including nonintegral Theta and the one-dimensional normal case.
for g in range(1,17):
    n=g+1
    for j in range(g):
        q=g-j
        check('sharp_factorial',F(factorial(n),factorial(j)*factorial(q))<=F(n**(j+1),factorial(j)))
        check('sharp_periodic_factorial',F(factorial(n),factorial(j)*factorial(q-1))<=F(q*n**(j+1),factorial(j)))
        full_ratio=F(2**g*factorial(n)*(2*n)**q,4**g*n**(g+1)*factorial(j)*factorial(q))
        periodic_ratio=F(2**g*factorial(n)*(2*n)**q,g*4**g*n**(g+1)*factorial(j)*factorial(q-1))
        check('full_rank_cancellation',full_ratio<=F(1,2**j*factorial(j)))
        check('periodic_rank_cancellation',periodic_ratio<=F(q,g*2**j*factorial(j)))
        for theta in [F(7,4),F(13,3),F(101,2),F(1200)]:
            tt=theta.numerator//theta.denominator; nn=2*n*tt
            rising=prod(theta+k for k in range(1,q+1))
            check('full_normal_count',F(comb(nn+q,q),1)/rising<=F((2*n)**q,factorial(q)))
            for t0 in [1,2,min(nn+1,7)]:
                count=sum(comb(nn-a+q-1,q-1) for a in range(t0))
                check('truncated_normal_count',F(count,1)/rising<=F(t0,1)/theta*F((2*n)**(q-1),factorial(q-1)))

for N in range(1,21):
    for t in range(1,N+2):
        explicit=sum(a+b<=N and b<t for a,b in product(range(N+1),repeat=2))
        check('normal_triangle_enumeration',explicit==t*(N+1)-t*(t-1)//2==comb(N+2,2)-comb(N-t+2,2))
check('figure_counts',comb(14,2)==91 and 3*13-3==36)
check('elliptic_growth_constant',F(23,2)*F(22,7)+F(11,4)<40)
check('reduced_lattice_singular_value',F(3,4)/(F(5,4)+F(3,4))>F(1,4))
check('log272_certificate',sum(F(6)**i/factorial(i) for i in range(18))>272)
check('log1005_certificate',sum(F(7)**i/factorial(i) for i in range(22))>1005)
check('log3_33_certificate',sum(F(2)**i/factorial(i) for i in range(8))>F(333,100))

# Rank of expanded field columns and the integer kernel are checked in an
# algebraic field rather than with approximate complex singular values.
s=sp.sqrt(2)
matrix=sp.Matrix([[1,s,2,2*s],[2,2*s,4,4*s]])
check('field_expanded_complex_rank',matrix.rank()==1)
check('integer_auxiliary_kernel',matrix*sp.Matrix([-2,0,1,0])==sp.zeros(2,1))
x=sp.symbols('x')
check('nonzero_auxiliary_section',sp.Poly(x-2,x).degree()==1)

# Direct power-series substitution tests the divided-jet change of variables.
z,w=sp.symbols('z w')
for N in range(1,7):
    p=sum(((-1)**a)*(a+1)*z**a*w**(N-a) for a in range(N+1))
    for values in [(1,2,-1,3),(F(1,2),-1,2,F(1,3))]:
        a,b,c,d=map(sp.Rational,values)
        transformed=sp.Poly(p.subs({z:a*z+b*w,w:c*z+d*w},simultaneous=True),z,w)
        entry_sum=abs(a)+abs(b)+abs(c)+abs(d)
        check('divided_jet_basis_bound',max(map(abs,transformed.coeffs()))<=entry_sum**N*(N+1))

for eta in [F(1,k) for k in range(5,101)]:
    check('strict_pigeonhole_exponent',2*eta*(4*eta+1)<4*eta)

mp.mp.dps=100
samples=[]
for g in [1,2,3,5,10,20]:
    n=g+1;eps=mp.mpf(1)/(200*g*g);kap=1+eps;lam=2*eps
    ag=g*mp.log(4*n)+5*mp.log(n)+15
    jg=12*(13+4*mp.e**2)/(25+4*mp.e**2)*n*mp.log(4*n)+56*mp.log(n)+54
    c4=4**g*n**(g+1)*(1+lam)*8*n*ag*jg
    c6=n*2**g
    c7=4*mp.log(4*n)/(13+4*mp.e**2)+(60+20*mp.log(n))/((13+4*mp.e**2)*g)
    c5=c6*c4**(2*g+1)/(factorial(n)*6**g*c7**g)
    bg=mp.log(c5)+4*g+4
    vg=(n*bg+g*mp.log(3)+mp.log(2)+1)/c4
    eg=(13*g+2)*5**g/c5
    mg=vg+(13*g+1)*5**g/c5+(mp.log(4*n*c4)+2)/c6+g*c7*(12*n*n+1)+2*n*(3+mp.log(2)+mp.mpf('1.5')*mp.log(g))
    kg=mp.log(kap*2**g*factorial(n)*3**g)+g*(bg+1)
    pg=kg+7*g+3+2*g*mp.log(2)+mp.log(2*n*c4)
    for D in [1,3,10]:
        for h in [mp.mpf(1),mp.mpf(7)]:
            b=10*h
            for vmax in [h,D*b]:
                vv=[vmax]*g
                for ell in [mp.mpf(1),5*D*vmax]:
                    ll=mp.log(b)+h+mp.log(D)+ell;rr=b+mp.log(D)+ell
                    ss=mp.floor(c4*D*ll/ell)
                    u0=c5*D**(2*g+2)*rr*ll**(g+1)*mp.fprod(vv)/ell**(2*g+1)
                    theta=u0/(D*ll)
                    ti=[c7*u0/(D*ss**2*v) for v in vv]
                    assert u0>=c5/5**g*D**3*b
                    assert mp.log(u0)<=bg*D*ll and all(t<=u0 for t in ti)
                    assert D*(mp.log(D)+(D-1)*(13*g+1)*D*b)<=eg*u0
                    assert mp.log(D)+mp.log(2)+g*mp.log(3)+n*mp.log(u0)<=vg*u0
                    assert 40/ss**2<1 and mp.log(2*n*ss)<=mp.log(2*n*c4)+2*D*ll
                    max_log_w=2*D*h+mp.mpf('1.5')*mp.log(D)+mp.log(h)/2+mp.log(b)/2
                    assert max_log_w<=3*D*ll
                    z=(1+lam)*4**g*n**(g+1)*jg
                    assert mp.floor(ss/z)>=1 and mp.floor(theta/(g*z))>=1
                    eta=kap/(D*jg);a=mp.mpf(100)
                    delta=4*eta*(a+mg+vg+mp.log(5)/c4)*u0
                    assert 2*eta*(delta+(a+mg+vg+mp.log(5)/c4)*u0)<delta
                    samples.append({'g':g,'D':D,'h':str(h),'v':str(vmax),'ell':str(ell),'m_g':mp.nstr(mg,18),'period_separation_constant':mp.nstr(pg,18),'log10_U0':mp.nstr(mp.log10(u0),18)})

result={'exact':{'total':sum(counts.values()),'families':dict(counts)},'numerical':{'total':len(samples),'precision_decimal_digits':100,'scope':'Scalar parameter stress samples, not claims that every sample is realized by elliptic points.','samples':samples},'scope':'Finite combinatorial, algebraic and parameter checks; the complete numerical logarithm bound is still unfinished.'}
(base/'elliptic-numerical-auxiliary-check.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
print(json.dumps({'exact_checks':result['exact'],'numerical_samples':len(samples)}))
