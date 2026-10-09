"""CC0-1.0. Reproduce the HG actual endpoint checks and schematic full-family diagram."""
from collections import defaultdict
from fractions import Fraction as F
from math import gcd
import datetime,json,pathlib,random
own=pathlib.Path(__file__).resolve().parent

def wm_mul(x,y):
    lamps,v,h=x; other,w,k=y
    shifted=frozenset(tuple(a+b for a,b in zip(p,v)) for p in other)
    return lamps^shifted,tuple(a+b for a,b in zip(v,w)),h+k
def wm_inv(x):
    lamps,v,h=x
    return frozenset(tuple(a-b for a,b in zip(p,v)) for p in lamps),tuple(-a for a in v),-h
wm_id=(frozenset(),(0,0,0),0)
wm_labels=[wm_id,(frozenset([(0,0,0)]),(0,0,0),1)]+[(frozenset(),tuple(int(j==k) for j in range(3)),0) for k in range(3)]
def ah_mul(x,y):
    lamps,h=x; other,k=y
    return lamps^frozenset(v+h for v in other),h+k
def ah_inv(x):
    lamps,h=x
    return frozenset(v-h for v in lamps),-h
ah_id=(frozenset(),0)
ah_labels=[ah_id,(frozenset([0]),0),(frozenset(),1)]

def counts(labels,mul,inv,ident,depth):
    pairs=[mul(x,inv(y)) for x in labels for y in labels]
    out={ident:1}; result=[out]
    for n in range(depth):
        nxt=defaultdict(int)
        for x,c in out.items():
            for p in pairs:nxt[mul(x,p)]+=c
        out=dict(nxt); result.append(out)
    return result,pairs

checks=[]
for name,labels,mul,inv,ident,lam,depth in [('WM',wm_labels,wm_mul,wm_inv,wm_id,F(3,2),3),('AH',ah_labels,ah_mul,ah_inv,ah_id,F(2),5)]:
    a=len(labels); d=F(a-1)+lam; d*=F(a-1)+1/lam
    stages,pairs=counts(labels,mul,inv,ident,depth)
    totalcases=0
    for n,C in enumerate(stages[1:],1):
        assert sum(C.values())==a**(2*n)
        assert sum(F(c)*lam**g[-1]/d**n for g,c in C.items())==1
        assert sum(F(c)*lam**(-g[-1])/d**n for g,c in C.items())==1
    # Each chosen canonical projection is an actual one-word diagonal, repeated
    # as a separate physical cell after factor comparison; old trace sum <=1.
    for pref in [pairs[0],pairs[1],pairs[-1]]:
        t=lam**pref[-1]/d
        for repetitions in [1,3,min(20,int(1/t))]:
            if repetitions*t>1:continue
            prev=None
            for n in range(1,depth+1):
                C=stages[n]; suffix=stages[n-1]
                old=defaultdict(int)
                for end,c in suffix.items():old[mul(pref,end)]+=c
                assert all(h<=C.get(g,0) for g,h in old.items())
                assert sum(F(h)*lam**g[-1]/d**n for g,h in old.items())==t
                ranks=[dict(old) for _ in range(repetitions)]
                capacities=defaultdict(int);H=defaultdict(int)
                for g,c in C.items():capacities[g[-1]]+=c
                for rank in ranks:
                    for g,h in rank.items():H[g[-1]]+=h
                excess={h:max(0,H[h]-c) for h,c in capacities.items()}
                delta=sum(F(e)*lam**h/d**n for h,e in excess.items())
                dual=sum(F(e)*lam**(-h)/d**n for h,e in excess.items())
                if prev is not None:assert delta<=prev
                prev=delta
                for grade,remove in excess.items():
                    todo=remove
                    for rank in ranks:
                        for g in list(rank):
                            if g[-1]!=grade:continue
                            z=min(todo,rank[g]);rank[g]-=z;todo-=z
                            if not todo:break
                        if not todo:break
                    assert todo==0
                retained=defaultdict(int)
                for rank in ranks:
                    for g,h in rank.items():retained[g[-1]]+=h
                # q0 is a projection of actual endpoint blocks; no coarse
                # off-endpoint matrix unit is used in its return.
                q0={}
                for grade,c in capacities.items():
                    todo=c-retained[grade]
                    assert 0<=todo<=c
                    for g,blocksize in C.items():
                        if g[-1]!=grade:continue
                        z=min(todo,blocksize);q0[g]=z;todo-=z
                    assert todo==0
                retainedtrace=sum(F(h)*lam**g[-1]/d**n for rank in ranks for g,h in rank.items())
                qtrace=sum(F(h)*lam**g[-1]/d**n for g,h in q0.items())
                assert qtrace==1-retainedtrace
                assert repetitions*t-retainedtrace==delta
                olddual=sum(F(h)*lam**(-g[-1])/d**n for g,h in old.items())*repetitions
                newdual=sum(F(h)*lam**(-g[-1])/d**n for rank in ranks for g,h in rank.items())
                assert olddual-newdual==dual
                totalcases+=1
    checks.append({'model':name,'parameter':str(lam),'depth':depth,'actual_endpoint_blocks':[len(x) for x in stages],'capacity_and_actual_return_cases':totalcases,'both_finite_traces_normalized':True})

def digit_certificate(A,B,N,K):
    initial=K;bits={};remaining=K
    for r in range(N,0,-1):
        b=(remaining*pow(B**r,-1,A))%A
        bits[r]=b;remaining=(remaining-b*B**r)//A
    bits[0]=remaining
    assert all(x>=0 for x in bits.values())
    assert sum(b*A**(N-r)*B**r for r,b in bits.items())==initial
    return bits
rng=random.Random(20261008);integercases=0;monoidcases=0
for A in range(2,13):
    for B in range(1,A):
        if gcd(A,B)>1:continue
        for N in range(1,8):
            cap=(A-1)*sum(A**(N-r)*B**r for r in range(1,N+1))
            for extra in [0,1,A**N-1,rng.randrange(A**N*3)]:
                digit_certificate(A,B,N,cap+extra);integercases+=1
        D=(A+4*B)*(4*A+B)
        for m in range(3):
            n=(m+1)*(A-1).bit_length()+3*m
            for K in [1,2,7]:
                digits=digit_certificate(A,B,2*n,K*D**(n-m))
                assert sum(F(b*A**(2*n-r)*B**r,D**n) for r,b in digits.items())==F(K,D**m)
                monoidcases+=1
checks.append({'positive_digit_cases':integercases,'rational_trace_monoid_cases':monoidcases,'actual_huge_WM_parameter_materialized':False})
(own/'checks.json').write_text(json.dumps({'checked_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'results':checks,'scope':'Finite exact arithmetic and actual endpoint rank constructions supplement the written proofs; no general-inclusion closure or numerical materialization of the astronomical fixed WM parameter.'},indent=2),encoding='utf-8')

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch
plt.rcParams.update({'font.family':'DejaVu Sans','font.size':11,'svg.hashsalt':'equal-weight-full-family-v19'})
fig,ax=plt.subplots(figsize=(15,9));ax.set_xlim(0,15);ax.set_ylim(0,9);ax.axis('off')
def box(x,y,w,h,text,color='#E7EFF7'):
    ax.add_patch(FancyBboxPatch((x,y),w,h,boxstyle='round,pad=0.05,rounding_size=.10',facecolor=color,edgecolor='#28435C',linewidth=1.3))
    ax.text(x+w/2,y+h/2,text,ha='center',va='center',linespacing=1.5)
def arrow(x1,y1,x2,y2,label=None):
    ax.add_patch(FancyArrowPatch((x1,y1),(x2,y2),arrowstyle='-|>',mutation_scale=15,color='#28435C',linewidth=1.6))
    if label:ax.text((x1+x2)/2,(y1+y2)/2+.15,label,ha='center',va='bottom',fontsize=10)
ax.text(.25,8.65,'Full finite families through equal physical word weights',fontsize=20,fontweight='bold',color='#17344D')
ax.text(.25,8.22,'HG.1–HG.5 and HG.9: the auxiliary factor proves a cost limit; every cut and residual returns to actual Jones stages.',fontsize=11)
box(.35,5.65,4.0,2.05,'ACTUAL canonical suffix Cₙ\nBlocks indexed by group endpoint g\nGrade h(g); physical weight λʰ / dⁿ\nDual weight λ⁻ʰ / dⁿ\nFixed old physical supports align to gᵢ', '#E7EFF7')
box(5.2,5.65,4.45,2.05,'AUXILIARY grade algebra Ĉₙ\nJoin equal-weight endpoint blocks\nMatrix-unit embedding Cₙ → Ĉₙ\nIndependent paired word probability\nFinite-permutation invariance ⇒ factor', '#EFEAF9')
arrow(4.4,6.65,5.1,6.65)
box(10.4,5.65,4.2,2.05,'FINITE cost and its limit\nΔₙ = Σₕ λʰ d⁻ⁿ (Hₙ,ₕ − cₙ,ₕ)₊\nΔₙ decreases to 0\nΣᵢ τ(gᵢ) = Σᵢ τ(rᵢ) ≤ 1\nHG.2 uses the auxiliary factor', '#E9F3EA')
arrow(9.7,6.65,10.3,6.65)
box(.35,2.85,4.0,2.05,'ACTUAL rank cuts inside Cₙ\nRemove (Hₙ,ₕ − cₙ,ₕ)₊ ranks\nfrom actual endpoint blocks\nReturn rᵢ′ = Uᵢgᵢ′Uᵢ* ≤ rᵢ\nTotal physical loss = Δₙ', '#E7EFF7')
box(5.2,2.85,4.45,2.05,'ACTUAL canonical certificate q₀\nAllocate cₙ,ₕ − min(Hₙ,ₕ,cₙ,ₕ)\ninside actual endpoint capacities\nτ(q₀) = τ(f + Σᵢ(rᵢ − rᵢ′))\nPlace q₀ onto this whole residual', '#E7EFF7')
arrow(12.5,5.55,12.5,5.25);arrow(12.5,5.25,2.35,5.25);arrow(2.35,5.25,2.35,4.95)
arrow(4.4,3.85,5.1,3.85)
box(10.4,2.85,4.2,2.05,'FULL physical partition\nUnits rᵢ′ and f* sum exactly to 1\nIndividual actual whole tunnels\nAll three expectation rows\nPrefix and every old cup retained', '#E9F3EA')
arrow(9.7,3.85,10.3,3.85)
ax.text(.4,2.35,'Same physical target y:  error ≤ old error + (1 + √2) ‖y‖ √Δₙ.  No auxiliary matrix unit is placed in M.',fontsize=12,color='#17344D')
box(.35,.45,14.25,1.25,'HG.10: exact index-ten affine completion, with no cuts\nAt paired depth m: τ(q) = 20⁻ᵐ and ρ(q) = 5⁻ᵐ for a genuine grade −m word projection.\nResidual τ(f) = K / 20ᵐ ⇒ K finite actual cells, each of physical trace 20⁻ᵐ; all old blocks stay fixed.', '#FFF2DD')
fig.tight_layout(pad=.6)
fig.savefig(own/'equal-weight-full-family-v19.svg',bbox_inches='tight',metadata={'Date':None})
fig.savefig(own/'equal-weight-full-family-v19.png',dpi=110,bbox_inches='tight')
print(json.dumps(checks))

# Normalize serializer whitespace without changing the exact geometry.
svg_path=own/'equal-weight-full-family-v19.svg'
svg_path.write_text('\n'.join(line.rstrip() for line in svg_path.read_text(encoding='utf-8').splitlines()).rstrip()+'\n',encoding='utf-8')
