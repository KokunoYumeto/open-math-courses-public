"""Exact finite regressions for the survival lesson; not infinite proofs."""
from collections import Counter, defaultdict
from decimal import Decimal, localcontext
from fractions import Fraction as F
from itertools import product
from math import comb
import json

counts=Counter()
def words(n,p):
    for bits in product((0,1),repeat=n):
        k=sum(bits)
        yield bits,p**k*(1-p)**(n-k)
def path(bits):
    k=0
    out=[F(1)]
    for j,b in enumerate(bits,1):
        k+=b
        out.append(F(3**k,2**j))
    return out
def fail(message):
    raise AssertionError(message)

# Finite stopped moments, boundary overshoot and optimized survival bound.
alphabets=[((-1,F(1,2)),(1,F(1,2))),
           ((-1,F(2,3)),(2,F(1,3))),
           ((-1,F(1,4)),(0,F(1,2)),(1,F(1,4)))]
for alphabet in alphabets:
    assert sum(x*w for x,w in alphabet)==0
    v=sum(x*x*w for x,w in alphabet); L=max(abs(x) for x,w in alphabet)
    for n in range(1,8):
        rows=[]
        for seq in product(alphabet,repeat=n):
            weight=F(1); sums=[F(0)]
            for x,w in seq:
                weight*=w; sums.append(sums[-1]+x)
            rows.append((sums,weight))
        for h in [F(0),F(1,2),F(2)]:
            survival=sum((w for s,w in rows if min(s)>=-h),F(0))
            assert survival**2*v*n<=4*(h+L)**2
            counts['optimized_survival_cases']+=1
            for H in [F(1,2),F(1),F(3)]:
                EY=EY2=Etau=upper=horizon=quad=F(0)
                for sums,weight in rows:
                    tau=next((j for j in range(1,n+1) if sums[j]<-h or sums[j]>=H),n)
                    Y=sums[tau]
                    assert -h-L<=Y<=H+L
                    if min(sums)>=-h:
                        assert Y>=H or tau==n
                    EY+=weight*Y; EY2+=weight*Y*Y; Etau+=weight*tau
                    upper+=weight*(Y>=H); horizon+=weight*(tau==n)
                    quad+=weight*(Y+h+L)*(H+L-Y)
                    counts['stopped_word_cases']+=1
                assert EY==0 and EY2==v*Etau
                assert quad==(h+L)*(H+L)-v*Etau>=0
                assert upper<=(h+L)/(H+h+L) and horizon<=Etau/n
                assert survival<=upper+horizon
                assert survival<=(h+L)/(H+h+L)+(h+L)*(H+L)/(v*n)
                counts['stopped_moment_cases']+=1

# Square the explicit atom bound to eliminate roots completely.
for p in [F(1,4),F(1,3),F(1,2),F(2,3),F(3,4)]:
    for n in range(1,129):
        total=F(0)
        for k in range(n+1):
            mass=comb(n,k)*p**k*(1-p)**(n-k)
            assert mass**2*n*8*p*(1-p)<=9
            total+=mass; counts['binomial_atom_cases']+=1
        assert total==1

# The three-block map and conditional bound with exact centered rational steps.
# Endpoint spacing is 1; bins are half open of length exactly 1.
for p in [F(1,3),F(2,3)]:
    for m in range(8,11):
        a=m//4; b=m-2*a
        maxatom=max(comb(b,k)*p**k*(1-p)**(b-k) for k in range(b+1))
        for B in [F(1,2),F(1),F(2)]:
            bins=defaultdict(F)
            for bits,weight in words(m,p):
                z=[F(0)]
                for bit in bits:z.append(z[-1]+bit-p)
                first,middle,last=bits[:a],bits[a:a+b],bits[a+b:]
                assert first+middle+last==bits
                assert weight==(p**sum(first)*(1-p)**(a-sum(first))
                                *p**sum(middle)*(1-p)**(b-sum(middle))
                                *p**sum(last)*(1-p)**(a-sum(last)))
                if min(z)>-B:
                    q=(z[-1]+B)//1
                    assert q>=0
                    assert all(z[m-j]-z[m]>-(q+1) for j in range(a+1))
                    bins[q]+=weight
                counts['three_block_word_cases']+=1
            for q,mass in bins.items():
                outer_first=outer_last=F(0)
                for outer,wgt in words(a,p):
                    z=[F(0)]
                    for bit in outer:z.append(z[-1]+bit-p)
                    if min(z)>-B:outer_first+=wgt
                    if min(z[a-j]-z[a] for j in range(a+1))>-(q+1):outer_last+=wgt
                assert mass<=outer_first*outer_last*maxatom
                v=p*(1-p)
                assert mass**2*v*v*a*a*b*8*p*(1-p)<=144*(B+1)**2*(q+2)**2
                counts['conditional_bin_cases']+=1

# Exact multiplicative stopping and terminal change of weights.
for m in range(1,12):
    trajectories=[(bits,path(bits)) for bits,_ in words(m,F(1,2))]
    for u in [F(1),F(3,2),F(2),F(3),F(10)]:
        stopped=crossing=remainder=tilted_remainder=F(0)
        for bits,values in trajectories:
            t=next((j for j,y in enumerate(values) if y>u),None)
            if t is None:
                y=values[-1]
                remainder+=y/F(2**m)
                tilted_remainder+=F(3**sum(bits),4**m)
            else:
                y=values[t]
                assert u<y<=3*u/2
                crossing+=F(1,2**m)
            stopped+=y/F(2**m)
            counts['multiplicative_word_cases']+=1
        assert stopped==1
        assert remainder==tilted_remainder
        assert crossing<=1/u
        assert 1<=3*u*crossing/2+remainder
        counts['multiplicative_maximum_cases']+=1

# A nonvacuous rational specialization of the lower bound:
# eps=1/20, p*<13/20 by 2^20<3^13; K=75.
assert 2**20<3**13
for n in [64,128,256,512]:
    for u in [F(1),F(3,2),F(2),F(10)]:
        assert u**20<=3**n
        alive={0:1}
        for j in range(1,n+1):
            nxt=defaultdict(int)
            for s,multiplicity in alive.items():
                for bit in (0,1):
                    k=s+bit
                    if F(3**k,2**j)<=u:nxt[k]+=multiplicity
            alive=nxt
        total=sum(alive.values())
        crossing=1-F(total,2**n)
        assert F(2,3)/u*(1-F(75,n))<=crossing<=1/u
        terminal=F(sum(c*3**k for k,c in alive.items()),4**n)
        assert terminal<=F(75,n)
        counts['positive_lower_bound_dp_cases']+=1

# Exact event counts retained for a separate high-precision diagnostic.
barrier_counts={}
for m in range(1,15):
    for threshold in [F(1,4),F(1,2),F(3,4)]:
        nwords=0
        for bits in product((0,1),repeat=m):
            s=0; good=True
            for j,bit in enumerate(bits,1):
                s+=bit
                if 3**s*threshold.denominator<=threshold.numerator*2**j:
                    good=False; break
            if good:nwords+=1
        barrier_counts[(m,threshold)]=nwords
        counts['exact_barrier_counts']+=1

# Four exercise solutions.
walks=[tuple(2*b-1 for b in bits) for bits in product((0,1),repeat=4)]
assert sum(sum(w)>=0 for w in walks)==11
assert sum(all(sum(w[:j])>=0 for j in range(5)) for w in walks)==6
assert F(2,3)*(-1)+F(1,3)*2==0
assert F(2,3)+F(1,3)*4==2 and F(16,200)==F(2,25)
for bits in [(1,1,0),(1,0,1),(0,1,1)]:
    assert F(1,8)/(F(2,3)**2*F(1,3))==F(27,32)
    assert path(bits)[-1]==F(9,8)
assert [bits for bits in [(1,1,0),(1,0,1),(0,1,1)] if min(path(bits))>F(3,4)]==[(1,1,0)]
cross=[bits for bits in product((0,1),repeat=3) if max(path(bits))>F(3,2)]
assert cross==[(1,1,0),(1,1,1)]
assert F(9,16)+F(7,16)==1 and 1-F(3,4)**2==F(7,16)

with localcontext() as ctx:
    ctx.prec=90
    D=Decimal; ln2=D(2).ln(); ln3=D(3).ln()
    p=ln2/ln3; v=p*(1-p)*ln3**2
    kappa=1+(p*p.ln()+(1-p)*(1-p).ln())/ln2
    theta=(p/(1-p)).ln()/ln3
    assert abs(v-ln2*(D(3)/2).ln())<D('1e-85')
    cp=3/(8*p*(1-p)).sqrt(); w=(-theta).exp()
    likelihood_cases=0
    max_relative_error=D(0)
    for m in range(1,65):
        for s in range(m+1):
            Z=s*ln3-m*ln2
            lhs=D(2)**(-m)/(p**s*(1-p)**(m-s))
            rhs=(-kappa*m*ln2-theta*Z).exp()
            error=abs(lhs/rhs-1)
            max_relative_error=max(max_relative_error,error)
            assert error<D('1e-80')
            likelihood_cases+=1
    for (m,threshold),nwords in barrier_counts.items():
        B=(D(threshold.denominator)/D(threshold.numerator)).ln()
        constant=max(D(8)**D('1.5')*(8*kappa*ln2).exp(),
                     32*D(2).sqrt()*cp/v*(B+1)*(theta*B).exp()*(2-w)/(1-w)**2)
        bound=constant/(D(m)**D('1.5'))*(-kappa*m*ln2).exp()
        assert D(nwords)/D(2)**m<=bound
    diagnostics={'kind':'90-digit Decimal numerical diagnostics, not exact certificates',
                 'p_star':str(p),'kappa':str(kappa),'variance':str(v),'theta':str(theta),
                 'likelihood_cases':likelihood_cases,
                 'max_likelihood_relative_error':str(max_relative_error),
                 'survival_bound_cases':len(barrier_counts)}
print(json.dumps({'passed':True,'exact_arithmetic':'Python integers and Fraction',
                  'counts':dict(counts),'solved_exercises':4,
                  'numerical_diagnostics':diagnostics,
                  'scope':'Bounded regression and numerical diagnostics only. General theorems have written proofs in the lesson.'},indent=2))

