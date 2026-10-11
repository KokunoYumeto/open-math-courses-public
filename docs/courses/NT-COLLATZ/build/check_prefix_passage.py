"""Exact finite regressions for maximal deviations and first-passage maps.
The asymptotic statements are proved in the lesson, not by these tests.
"""
from collections import defaultdict
from fractions import Fraction as F
from itertools import product
from math import comb
import json
import mpmath as mp


def step(x):
    y = 3*x + 1
    a = (y & -y).bit_length()-1
    return y >> a, a


def path(x,n):
    states=[x]; word=[]
    for _ in range(n):
        x,a=step(x); states.append(x); word.append(a)
    return states,word


def deviations(word):
    u=0; out=[0]
    for a in word:
        u+=a-2; out.append(u)
    return out


def good_probability(n,w):
    mass={0:F(1)}
    for _ in range(n):
        nxt=defaultdict(F)
        for u,p in mass.items():
            for a in range(1,w+2-u):
                v=u+a-2
                if -w<v<w:
                    nxt[v]+=p*F(1,2**a)
        mass=nxt
    return sum(mass.values(),F(0))


def maximal_bound(n,w):
    assert 0<w<n
    yp=F(2*(n+w),2*n+w)
    ym=F(2*(n-w),2*n-w)
    def g(y): return 1/(y*(2-y))
    return g(yp)**n/yp**w + g(ym)**n*ym**w


def theta(n,m):
    return F(sum(comb(m-1,j) for j in range(min(n,m))),2**(m-1))


def coordinates(word):
    s=c=0
    for a in word:
        c=3*c+2**s
        s+=a
    return s,c


def main():
    counts=defaultdict(int)
    for n in range(2,21):
        for w in range(1,n):
            bad=1-good_probability(n,w)
            assert 0<=bad<=1
            assert bad<=maximal_bound(n,w)
            counts['exact_maximal_bounds']+=1
        assert theta(n,3*n)<=F(27,32)**n
        counts['exact_overflow_bounds']+=1
    assert good_probability(2,2)==F(17,32)
    assert sum(F(s-1,2**s) for s in (3,4,5))==F(18,32)
    assert deviations((3,3,3,1,1,1))==[0,1,2,3,2,1,0]
    assert deviations((3,1,3,1,3,1))==[0,1,0,1,0,1,0]
    for z in (F(3),F(15,2),F(17),F(125,4)):
        for width in (F(5),F(19,2),F(28)):
            upper=z+width
            xs=[x for x in range(1,100,2) if z<=x<upper]
            D=len(xs); H=sum((F(1,x) for x in xs),F(0))
            ceilz=-(-z.numerator//z.denominator)
            laws=[{x:F(1,D) for x in xs},{x:F(1,x)/H for x in xs}]
            for n in range(1,5):
                for m in range(n+1,3*n+2):
                    q=2**m; a=q//2
                    th=theta(n,m)
                    for typ,law in enumerate(laws):
                        res=defaultdict(F)
                        for x,p in law.items(): res[x%q]+=p
                        delta=sum((abs(res[b]-F(1,a)) for b in range(1,q,2)),F(0))
                        cap=F(a,D) if typ==0 else F(a,ceilz)/H
                        assert delta<=cap
                        counts['exact_residue_bounds']+=1
                        for w in (1,2,3):
                            actual=sum((law[x] for x in xs if max(map(abs,deviations(path(x,n)[1])))>=w),F(0))
                            ideal=1-good_probability(n,w)
                            assert abs(actual-ideal)<=delta/2+th
                            counts['exact_event_transfers']+=1
    for nu in range(1,5):
        for word in product(range(1,5),repeat=nu):
            s,c=coordinates(word); modulus=3**nu
            w=max(map(abs,deviations(word)))+1
            residue=(c*pow(2**s,-1,modulus))%modulus
            for B in (1,2,7):
                budget=2**(2*w)*B+3**nu
                M=budget+1+((residue-budget-1)%modulus)
                if M%2==0: M+=modulus
                assert M>budget and M%2 and (2**s*M-c)%modulus==0
                X=(2**s*M-c)//modulus
                states,actual=path(X,nu)
                assert tuple(actual)==word and states[-1]==M
                assert X>0 and X%2
                assert all(v>B for v in states[:-1])
                assert (2**s*states[-1]-c)//modulus==X
                counts['exact_reverse_prefix_roundtrips']+=1
    for B in (10,20,50):
        for X in range(B+1,401):
            if X%2==0: continue
            states,word=path(X,60)
            hits=[j for j,v in enumerate(states) if v<=B]
            if not hits: continue
            n=hits[0]
            for h in range(1,min(n,4)+1):
                nu=n-h; M=states[nu]
                tail,_=path(M,h)
                assert all(v>B for v in tail[:-1]) and tail[-1]<=B
                s,c=coordinates(word[:nu])
                assert X==(2**s*M-c)//3**nu
                assert all(v>B for v in states[:nu])
                counts['exact_first_passage_roundtrips']+=1
    states,word=path(33,2)
    assert states==[33,25,19] and word==[2,2]
    assert F(1001,1000)**3 < F('1.004')
    assert F('1.004')-F('.14')/4+F('.000022') < F('.99')
    assert F('.14427')*F('1.1') < F('.2')
    assert F('.14426')*300000-1 >= F('.14')*300000
    assert F(1,3001)+F(1,240001)<1
    assert F('2.41')*142+F('3.41')<=3*142
    eta=F(5097587,77645938)
    assert eta>F(1,16) and eta<F(1,2)
    counts['exact_schedule_and_rate_inequalities']=7
    mp.mp.dps=80
    diagnostics=[]
    for logB in ('1e24','1e30','1e40'):
        L=mp.mpf(logB); ell=mp.log(2); d=mp.log(mp.mpf(4)/3)
        N=mp.floor(L/(10*ell)); h=mp.floor(L/100000)
        G=L**mp.mpf('.7')
        for C0 in ('.5','1','2','4'):
            C=mp.mpf(C0); W=C*mp.sqrt(N*mp.log(N))
            tests=[L>=300000,W<=mp.mpf('.000022')*L,
                   2*ell*W+mp.log(mp.mpf(8)/3)<=G,
                   G+2*ell*W+ell<h*d, mp.ceil(W)<N]
            assert all(tests)
            diagnostics.append({'log_B':logB,'C':C0,'finite_guards_pass':True})
    return {'passed':True,'exact_checks':dict(counts),
            'exercises':{'path_good_two_steps':'17/32','endpoint_good_two_steps':'18/32',
                         'first_passage_example':[33,25,19],
                         'component_rate_at_C_half':'1/16'},
            'numerical_diagnostics':{'precision_decimal_digits':80,'scales':diagnostics,
                                    'scope':'Log-scale finite-guard evaluations only, not exact certificates.'},
            'scope':'Finite regressions. General maximal, transport and correspondence proofs are in the lesson.'}


if __name__=='__main__':
    print(json.dumps(main(),indent=2))
