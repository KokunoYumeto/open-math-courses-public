"""Bounded exact tests for affine extrema, timeout coding and rank clocks."""
from fractions import Fraction as F
from itertools import product
from collections import Counter,defaultdict
from math import comb
from decimal import Decimal,localcontext
import json,random
counts=Counter()
def orbit(n,m):
    values=[n]; bits=[]
    for _ in range(m):
        b=n%2;bits.append(b);n=(3*n+1)//2 if b else n//2;values.append(n)
    return values,bits
def coordinates(bits):
    A=s=0
    for j,b in enumerate(bits):
        A=3**b*A+b*2**j;s+=b
    return A,s
for j in range(1,15):
    maxima=defaultdict(lambda:F(-1));argmax=defaultdict(list)
    for bits in product((0,1),repeat=j):
        A,s=coordinates(bits); Q=F(A,3**s)
        k=0; explicit=F(0)
        for i,b in enumerate(bits):
            if b:k+=1;explicit+=F(2**i,3**k)
        assert Q==explicit
        bound=F(2**(j-s))*(1-F(2,3)**s)
        assert Q<=bound<=F(2**(j-1),3)
        if Q==bound:assert bits==(0,)*(j-s)+(1,)*s
        if Q>maxima[s]:maxima[s]=Q;argmax[s]=[bits]
        elif Q==maxima[s]:argmax[s].append(bits)
        counts['affine_words']+=1
    for s in range(j+1):
        assert maxima[s]==F(2**(j-s))*(1-F(2,3)**s)
        assert argmax[s]==[(0,)*(j-s)+(1,)*s]
        counts['fixed_count_extrema']+=1
    assert max(maxima.values())==F(2**(j-1),3)
    assert argmax[max(maxima,key=maxima.get)]==[(0,)*(j-1)+(1,)]
timeouts={}
for m in range(1,13):
    codes={}
    for x in range(2**m,2**(m+1)):
        values,bits=orbit(x,m);code=tuple(bits)
        assert code not in codes;codes[code]=x
        for j in range(m+1):
            A,s=coordinates(bits[:j])
            assert 2**j*values[j]==3**s*x+A
            assert 6*2**j*values[j]<=7*3**s*x
            counts['actual_affine_prefixes']+=1
        low=min(values)
        for q in range(m+1):
            if low>2**q:
                for j in range(m+1):
                    s=sum(bits[:j])
                    assert 7*3**s*2**(m+1)>6*2**(q+j)
                counts['literal_timeouts']+=1
            timeouts.setdefault((m,q),0)
            timeouts[(m,q)]+=low>2**q
        counts['shell_sources']+=1
    assert len(codes)==2**m
    for bits,x in codes.items():assert tuple(orbit(x,m)[1])==bits
    for q in range(m+1):
        # Uniform barrier B=(m+1-q)log2+log(7/6), with all prefixes strict.
        survivors=0
        for bits in codes:
            if all(7*3**sum(bits[:j])*2**(m+1)>6*2**(q+j) for j in range(m+1)):
                survivors+=1
        assert timeouts[(m,q)]<=survivors
        counts['timeout_to_barrier_counts']+=1
for L in range(1,13):
    for K in [F(1,2),F(1),F(2),F(3)]:
        if K>=2*L:continue
        ratio=1-K/(2*L)
        for C in [F(1),F(3,2),F(2),F(4)]:
            for m in range(L,min(12,(C*L)//1)+1):
                q=(ratio*m)//1; loss=K*m/(2*L)
                ceil_loss=-((-loss)//1)
                assert m-q==ceil_loss
                assert m-q<=C*K/2+1 and 0<=q<m
                counts['exact_low_rank_rounding']+=1
# Exact rank telescope, with no choice of an actual orbit asserted here.
for M in range(2,401):
    for r in [F(4,5),F(9,10),F(19,20)]:
        m=M; drops=0; steps=0
        while m>=2:
            q=(r*m)//1
            if q<1:break
            drops+=m-q;steps+=1
            assert drops==M-q-(steps-1)
            assert m<=r**(steps-1)*M
            counts['rank_telescope_prefixes']+=1
            m=q-1
for S in range(2,65):
    for L in range(1,S):
        V=(S-L)*(S+L-1)//2
        assert V==sum(range(L,S))
        # For each suffix/prefix removal, the retained rank cost only decreases.
        for omitted in [set(),{L},{S-1},{m for m in range(L,S) if m%2}]:
            assert sum(m for m in range(L,S) if m not in omitted)<=V
            counts['decreasing_rank_cost_cases']+=1
# Actual finite chains verify endpoint exclusions and the direct-passage map.
for n in range(32,2048):
    x=n;total=0;thresholds=[];values=[n]
    while x.bit_length()-1>=4:
        m=x.bit_length()-1;q=(9*m)//10
        if q<1:break
        block,bits=orbit(x,m)
        h=next((j for j in range(1,m+1) if block[j]<=2**q),None)
        if h is None:break
        y=block[h];total+=h;values+=block[1:h+1]
        assert 2**(q-1)<y<=2**q
        assert values[-1]==y and all(z>2**q for z in values[:-1])
        assert not thresholds or q<thresholds[-1]
        thresholds.append(q)
        counts['actual_direct_passages']+=1
        if y==2**q:break
        assert y.bit_length()-1==q-1
        x=y
# Exact exercise values.
assert F(4,3)+F(8,9)==F(20,9)
assert F(1,3)+F(2,9)==F(5,9)
assert orbit(12,3)[0]==[12,6,3,5]
assert sum(m-q for m,q in [(20,18),(17,15),(14,12)])==20-12-2==6
counts['solved_exercises_exact_parts']=3
# Logarithmic/geometric magnitudes are explicitly numerical, not certificates.
with localcontext() as ctx:
    ctx.prec=90;D=Decimal;ln2=D(2).ln();ln3=D(3).ln()
    a0=ln3/(2*ln2);g=1-a0
    kappa=1+((ln2/ln3)*(ln2/ln3).ln()+(1-ln2/ln3)*(1-ln2/ln3).ln())/ln2
    A=1/(2*kappa);diagnostic_cases=0
    for M in [100,1000,10**6,10**12,10**24]:
        MM=D(M)
        for w in [D(1),MM.ln().sqrt(),MM.ln()]:
            L=int((A*MM.ln()+w.ln())/ln2)
            assert L>0
            lhs=(-kappa*D(L)*ln2).exp()
            rhs=(kappa*ln2).exp()/MM.sqrt()/((kappa*w.ln()).exp())
            assert lhs<=rhs+D('1e-80')
            diagnostic_cases+=1
    # A broad set of geometric rank sums and their explicit majorants.
    for M in range(10,501,7):
        for r in [D('.85'),D('.9'),D('.95')]:
            m=M;total=D(0)
            while m>=1:
                total+=D(m).sqrt()
                m=int(r*D(m))-1
            assert total<=D(M).sqrt()/(1-r.sqrt())
            diagnostic_cases+=1
print(json.dumps({'passed':True,'counts':dict(counts),
 'exact_scope':'Integer/Fraction affine coordinates and extrema, actual finite prefix comparisons, shell parity bijections, timeout containment, rank rounding, telescopes, direct first passages and decreasing-rank costs.',
 'diagnostics':{'precision_digits':90,'cases':diagnostic_cases,'scope':'Real logarithmic scales and square-root geometric sums only; not exact certificates.'},
 'formal_status':'Bounded regression checks. General statements are proved in the lesson, not by enumeration.'},indent=2))

