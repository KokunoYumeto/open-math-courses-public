"""Finite regression checks for maximal parity deviations and orbit envelopes.
Integer/Fraction assertions are exact. Analytic diagnostics are explicitly
separate; no finite experiment proves an infinite theorem.
"""
from fractions import Fraction as F
from functools import lru_cache
from itertools import product
from math import comb
import json
import mpmath as mp

counts={}
def T(n):return (3*n+1)//2 if n%2 else n//2
def trajectory(n,M):
    xs=[n];bits=[];ys=[0]
    for i in range(M):
        bits.append(xs[-1]%2);ys.append(ys[-1]+2*bits[-1]-1);xs.append(T(xs[-1]))
    return xs,bits,ys
def tail(M,k):return sum(comb(M,j) for j in range(k,M+1))
def reflect(w,a):
    z=0
    for j,v in enumerate(w):
        z+=v
        if z==a:return w[:j+1]+tuple(-v for v in w[j+1:])
    raise AssertionError("reflection domain")
reflection_checks=0
for M in range(0,12):
    words=list(product((-1,1),repeat=M))
    walks=[]
    for w in words:
        y=[0]
        for v in w:y.append(y[-1]+v)
        walks.append((w,y))
    for a in range(1,M+2):
        hitting=0;absolute=0;domain=set();image=set()
        for w,y in walks:
            hitting+=max(y)>=a;absolute+=max(map(abs,y))>=a
            if max(y)>=a and y[-1]<a:
                v=reflect(w,a)
                assert sum(v)>a and reflect(v,a)==w
                domain.add(w);image.add(v);reflection_checks+=1
        terminal={w for w,y in walks if y[-1]>a}
        assert image==terminal and len(domain)==len(image)
        k=(M+a+1)//2;kp=(M+a)//2+1
        assert hitting==tail(M,k)+tail(M,kp)
        assert absolute<=2*hitting<=4*tail(M,k)
counts['reflected_words']=reflection_checks

@lru_cache(None)
def B(r,z,a):
    if abs(z)>a:return 2**r
    if r==0:return 0
    return B(r-1,z-1,a)+B(r-1,z+1,a)
def ch(q,z):return (q**z+q**(-z))/2
ncosh=0
for q in [F(1),F(3,2),F(2),F(5,4)]:
    for r in range(9):
        for a in range(5):
            for z in range(-4,5):
                assert B(r,z,a)*ch(q,a)<=2**r*ch(q,z)*ch(q,1)**r
                assert ch(q,z-1)+ch(q,z+1)==2*ch(q,z)*ch(q,1)
                ncosh+=1
counts['rational_cosh_potentials']=ncosh
ntail=0
for M in range(1,101):
    for k in range(M//2+1,M+1):
        lhs=sum((2*j-M)*comb(M,j) for j in range(k,M+1))
        assert lhs==k*comb(M,k)
        assert (2*k-M)*tail(M,k)<=lhs
        ntail+=1
counts['weighted_binomial_tails']=ntail

bijections=affine=half_good=full_good=relative=0
assert F(7,6)**4<2
for M in range(11):
    seen=set()
    for n in range(2**M,2**(M+1)):
        xs,bits,ys=trajectory(n,M);seen.add(tuple(bits))
        s=0;b=F(0)
        for k in range(M+1):
            assert xs[k]==F(3**s,2**k)*n+b
            affine+=1
            slope=F(3**s,2**k)
            assert n*slope<=xs[k]<=F(7,6)*n*slope
            relative+=1
            if k<M:
                b=(3**bits[k]*b+bits[k])/2;s+=bits[k]
        A=max(map(abs,ys))
        for eta in [F(1,4),F(1,2),F(3,4),F(1)]:
            num,den=eta.numerator,eta.denominator
            def envelope():
                for k,x in enumerate(xs):
                    middle=x**(2*den)*4**(k*den)
                    assert 3**(k*den)*n**(2*(den-num))<=middle
                    assert middle<=3**(k*den)*n**(2*(den+num))
            if F(2)**(num*M)>=F(7,6)**(2*den) and 3**(den*A)<=2**(num*M):
                envelope();half_good+=1
            if F(3)**(den*A)*F(7,6)**(2*den)<=F(2)**(2*num*M):
                envelope();full_good+=1
    assert len(seen)==2**M
    bijections+=1
counts.update(parity_shell_bijections=bijections,exact_affine_identities=affine,
              half_allowance_trajectories=half_good,affine_allowance_trajectories=full_good,
              relative_affine_comparisons=relative)
assert trajectory(87,6)==([87,131,197,296,148,74,37],[1,1,1,0,0,0],[0,1,2,3,2,1,0])
assert trajectory(65,6)==([65,98,49,74,37,56,28],[1,0,1,0,1,0],[0,1,0,1,0,1,0])
assert F(37)-F(27,64)*87==F(19,64)
assert F(28)-F(27,64)*65==F(37,64)

mp.mp.dps=90
lam=mp.log(3)/mp.log(2);a0=lam/2;K=2+mp.sqrt(3)
beta=mp.log(mp.mpf(7)/6,2);c0=1/(2*lam**2)
assert 0<beta<mp.mpf(1)/4
def I(t):return (mp.mpf('.5')+t)*mp.log(1+2*t)+(mp.mpf('.5')-t)*mp.log(1-2*t)
analytic=[]
for s in ['0.001','0.01','0.1','0.25','0.49']:
    t=mp.mpf(s);th=mp.log((mp.mpf('.5')+t)/(mp.mpf('.5')-t))/2
    assert abs(2*t*th-mp.log(mp.cosh(th))-I(t))<mp.mpf('1e-85')
    assert 2*t*t<I(t)<mp.log(2)
    analytic.append(dict(t=s,entropy=mp.nstr(I(t),30)))
for n in range(1,101):
    c=mp.sqrt(2*n)*(mp.mpf(n)/mp.e)**n
    fact=mp.factorial(n)
    assert mp.exp(mp.mpf('.75'))/mp.sqrt(2)*c<=fact*(1+mp.mpf('1e-85'))
    assert fact<=mp.e/mp.sqrt(2)*c*(1+mp.mpf('1e-85'))
for taus in ['0.1','0.4','0.75']:
    tau=mp.mpf(taus);u=tau/lam;delta=(mp.mpf('.5')-u)/2
    N=int(mp.ceil(max(1,2/(mp.mpf('.5')-u))))
    for fraction in [1,2,5,10]:
        eta=tau/fraction;M=max(N,int(mp.ceil(2*beta/eta)))
        v=eta/lam-beta/(lam*M);aa=int(mp.floor(2*v*M))+1;k=(M+aa+1)//2;p=mp.mpf(k)/M
        assert 0<k<M and v<p-mp.mpf('.5')<=v+mp.mpf(1)/M
        assert 1-p>=delta-mp.mpf('1e-85')
        assert v>=eta/(2*lam)-mp.mpf('1e-85')
        J=mp.log((mp.mpf('.5')+u)/(mp.mpf('.5')-u))/lam
        assert M*(I(eta/lam)-I(v))<=beta*J+mp.mpf('1e-85')
constant_rows=[]
for etas in ['0.001','0.01','0.1','0.4','0.75']:
    eta=mp.mpf(etas);u=eta/lam;b=I(u)
    J=mp.log((mp.mpf('.5')+u)/(mp.mpf('.5')-u))/lam
    oldm=int(mp.ceil(max(1,1/eta,(mp.log(2*K,2)-2)/(a0-eta))))
    newm=int(mp.ceil(max(1,beta/eta)))
    oldC=max(2*mp.exp(J),mp.exp(b*(oldm-1)))
    newC=max(2*mp.exp(beta*J),mp.exp(b*(newm-1)))
    assert newm<=oldm and newC<=oldC
    for M in range(0,newm):
        assert newC*mp.exp(-b*M)>=1-mp.mpf('1e-85')
    constant_rows.append(dict(eta=etas,new_startup=newm,old_startup=oldm,
                              new_constant=mp.nstr(newC,25),old_constant=mp.nstr(oldC,25)))
small_samples=0
for M in range(41):
    for etas in ['0.0001','0.001','0.01','0.1','0.25','0.5','1']:
        eta=mp.mpf(etas)
        if eta*M<2*beta:
            assert 2*mp.exp(-c0*eta*eta*M)>1
            small_samples+=1
counts['all_rank_small_range_diagnostics']=small_samples
counts['analytic_parameter_rows']=len(analytic)
print(json.dumps(dict(passed=True,counts=counts,
 exact_scope="Exhaustive reflection words through length11; rational cosh potentials through9 remaining-time levels; weighted tails through100; parity and trajectory samples on shells0 through10.",
 analytic_diagnostics=dict(precision_decimal_digits=90,entropy_rows=analytic,factorial_samples=100,uniform_startup_samples=12,constant_comparisons=constant_rows,beta=mp.nstr(beta,30),
 scope="Finite high-precision numerical diagnostics only, separate from integer and Fraction checks."),
 proof_scope="General real inequalities and all infinite conclusions are supplied by the written lesson. No Lean build or independent verification claimed."),indent=2))

