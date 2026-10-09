"""Portable exact checks and reproducible POR diagram. CC0-1.0."""
from collections import Counter, defaultdict
from fractions import Fraction as Q
from itertools import product
from math import comb, factorial
from pathlib import Path
import datetime, json, random
import matplotlib
matplotlib.use('Agg')
matplotlib.rcParams['svg.hashsalt']='permutation-orbit-residual-v25'
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch

D=Path(__file__).resolve().parent

def prod(xs):
    out=Q(1)
    for x in xs: out*=x
    return out

def allocation(weights,old_letters,depth,endpoint=None):
    n=len(weights[0]);r=len(old_letters)
    assert all(sum(w,Q())==1 and min(w)>0 for w in weights)
    occupancy=[sum(a in letters for letters in old_letters) for a in range(n)]
    orbits=defaultdict(list)
    for word in product(range(n),repeat=depth):
        orbits[tuple(sorted(word))].append(word)
    residual=set();retained=[set() for i in range(r)];deleted=[set() for i in range(r)]
    trace_totals=[dict(loss=Q(),retained=Q(),residual=Q(),old=Q()) for w in weights]
    integrality=0;record=[]
    for kind,words in sorted(orbits.items()):
        counts=Counter(kind);size=factorial(depth)
        for c in counts.values(): size//=factorial(c)
        assert size==len(words)
        total_occupancy=sum(occupancy[a] for a in kind)
        occurrences=[(i,word) for word in words for i,letters in enumerate(old_letters) if word[0] in letters]
        R=len(occurrences)
        assert R*depth==size*total_occupancy
        integrality+=1
        cut=max(R-size,0);keep=min(R,size)
        for index,(i,word) in enumerate(occurrences):
            (retained if index<keep else deleted)[i].add(word)
        qwords=words[:size-keep];residual.update(qwords)
        for j,w in enumerate(weights):
            mass=prod(w[a] for a in kind)
            assert all(prod(w[a] for a in word)==mass for word in words)
            trace_totals[j]['loss']+=mass*cut
            trace_totals[j]['retained']+=mass*keep
            trace_totals[j]['residual']+=mass*(size-keep)
            trace_totals[j]['old']+=mass*R
        record.append(dict(type=list(kind),size=size,old_occurrences=R,retained=keep,deleted=cut,residual=size-keep))
    assert all(retained[i].isdisjoint(deleted[i]) for i in range(r))
    assert all(all(word[0] in old_letters[i] for word in retained[i]) for i in range(r))
    for j,w in enumerate(weights):
        S=sum(w[a]*occupancy[a] for a in range(n))
        variance=sum(w[a]*(occupancy[a]-S)**2 for a in range(n))
        t=trace_totals[j]
        assert t['old']==S and t['retained']+t['loss']==S
        assert t['retained']+t['residual']==1
        excess=t['loss']-max(S-1,0)
        assert excess>=0 and excess**2<=variance/depth
        expectation=sum((prod(w[a] for a in word)*max(Q(sum(occupancy[a] for a in word),depth)-1,0) for word in product(range(n),repeat=depth)),Q())
        assert t['loss']==expectation
        t.update(mean=S,variance=variance)
    vertices=0
    if endpoint:
        blocks=Counter(endpoint(word) for word in product(range(n),repeat=depth))
        q_ranks=Counter(endpoint(word) for word in residual)
        old_ranks=[Counter(endpoint(word) for word in product(range(n),repeat=depth) if word[0] in letters) for letters in old_letters]
        new_ranks=[Counter(endpoint(word) for word in words) for words in retained]
        relation={g:q_ranks[g]+sum(new[g] for new in new_ranks)-dimension for g,dimension in blocks.items()}
        for g,dimension in blocks.items():
            assert 0<=q_ranks[g]<=dimension
            assert all(0<=new[g]<=old[g]<=dimension for new,old in zip(new_ranks,old_ranks))
            vertices+=1
        # The actual full-stage signed rank relation has the physical and
        # original dual value zero. This checks full endpoint blocks, not an AF
        # replacement. The stage weights are supplied by the actual WM model.
        for j,w in enumerate(weights):
            representatives={}
            for word in product(range(n),repeat=depth):
                g=endpoint(word);mass=prod(w[a] for a in word)
                if g in representatives:assert representatives[g]==mass
                representatives[g]=mass
            assert sum((representatives[g]*v for g,v in relation.items()),Q())==0
    return dict(orbits=len(orbits),integrality_checks=integrality,trace_vertices=vertices,totals=trace_totals,records=record)

fixture=allocation([[Q(1,3),Q(2,3)],[Q(2,3),Q(1,3)]],[{0},{0}],3)
assert fixture['totals'][0]['loss']==Q(1,9)
assert fixture['totals'][0]['retained']==Q(5,9) and fixture['totals'][0]['residual']==Q(4,9)
assert fixture['totals'][1]['loss']==Q(4,9)
assert fixture['totals'][1]['retained']==Q(8,9) and fixture['totals'][1]['residual']==Q(1,9)
assert [x['old_occurrences'] for x in fixture['records']]==[2,4,2,0]

tested=0;orbits=0;vertices=0
for depth in range(1,9):
    for p in [Q(1,5),Q(1,3),Q(1,2),Q(2,3),Q(4,5)]:
        for family in [[],[set()],[{0}],[{0},{0}],[{0},{1}],[{0,1},{0},{1}]]:
            out=allocation([[p,1-p],[1-p,p]],family,depth)
            tested+=1;orbits+=out['orbits']
rng=random.Random(2509)
for trial in range(60):
    n=rng.randrange(2,5);den=Q(sum(range(1,n+1)))
    w=[Q(a,1)/den for a in range(1,n+1)]
    other=list(reversed(w));family=[{a for a in range(n) if rng.randrange(2)} for i in range(rng.randrange(0,5))]
    out=allocation([w,other],family,rng.randrange(1,5))
    tested+=1;orbits+=out['orbits']

# Actual WM five-label group endpoints; separate testing parameter 7/5.
# This does not change the original rational WM endpoint in the text.
zero=(frozenset(),(0,0,0),0)
def mul(a,b):
    lamps,v,r=a;other,w,t=b
    shifted=frozenset(tuple(v[j]+x[j] for j in range(3)) for x in other)
    return (lamps.symmetric_difference(shifted),tuple(v[j]+w[j] for j in range(3)),r+t)
def labels(sign):
    return [zero,(frozenset({(0,0,0)}),(0,0,0),sign)]+[(frozenset(),tuple(sign if j==axis else 0 for j in range(3)),0) for axis in range(3)]
alphabet=[(i,j) for i in range(5) for j in range(5)]
endpoints=[mul(labels(1)[i],labels(-1)[j]) for i,j in alphabet]
lam=Q(7,5);index=(4+lam)*(4+1/lam)
physical=[lam**g[2]/index for g in endpoints]
dual=[lam**(-g[2])/index for g in endpoints]
assert index==Q(891,35) and sum(physical,Q())==sum(dual,Q())==1
def actual_endpoint(word):
    g=zero
    for a in word:g=mul(g,endpoints[a])
    assert g[2]%2==len(g[0])%2
    return g
chosen=alphabet.index((0,1))
actual=[]
for depth in [1,2,3]:
    out=allocation([physical,dual],[{chosen}]*35,depth,actual_endpoint)
    assert out['totals'][0]['mean']==Q(875,891)
    assert out['totals'][1]['mean']==Q(1715,891)
    actual.append(dict(depth=depth,orbits=out['orbits'],full_endpoint_vertices=out['trace_vertices'],totals=out['totals']))
    tested+=1;orbits+=out['orbits'];vertices+=out['trace_vertices']

def binary_loss(p,occupancy,depth):
    return sum((Q(comb(depth,c))*p**c*(1-p)**(depth-c)*max(Q(occupancy*c,depth)-1,0) for c in range(depth+1)),Q())
loss_curve=[binary_loss(Q(1,3),2,h) for h in range(1,97)]
dual_curve=[binary_loss(Q(2,3),2,h) for h in range(1,97)]
assert all(x*x<=Q(8,9)/h for h,x in enumerate(loss_curve,1))
assert all((x-Q(1,3))**2<=Q(8,9)/h for h,x in enumerate(dual_curve,1))

fig=plt.figure(figsize=(16,11),dpi=135,facecolor='white')
ax=fig.add_axes([0,0,1,1]);ax.set_xlim(0,16);ax.set_ylim(0,11);ax.axis('off')
navy='#183b56';blue='#3678a8';green='#2d8766';red='#bc583e';light='#e7eef3'
ax.text(.55,10.55,'Permutation orbits complete the actual whole residual',fontsize=22,weight='bold',color=navy)
ax.text(.55,10.12,'POR.1–21: actual finite Jones maps, separate traces, exact finite allocation',fontsize=12,color=navy)
def box(x,y,w,h,title,body):
    ax.add_patch(FancyBboxPatch((x,y),w,h,boxstyle='round,pad=0.12',facecolor=light,edgecolor=blue))
    ax.text(x+.18,y+h-.4,title,fontsize=14,weight='bold',color=navy)
    ax.text(x+.18,y+h-.83,body,fontsize=12,color=navy,va='top',linespacing=1.6)
box(.65,7.85,4.6,1.7,'Original downward row F','F = Nₘ′ ∩ Nₖ;  m − k = 2ℓ\nphysical τ ↔ LEFT dimension\nmodule ρ ↔ RIGHT dimension')
box(5.85,7.85,4.0,1.7,'Dual even fusion word',r'$Z=(\overline{X}\otimes_P X)^l$, outer $N_k$–$N_k$'+'\nZʰ is the same actual word\neach dimension multiplies separately')
box(10.45,7.85,4.85,1.7,'Actual repeated copies','F⊗ʰ ↪ Nⱼ′ ∩ Nₖ\nj = k + (m − k)h\nfirst copy remains the original F')
for x in [5.3,9.95]:ax.annotate('',xy=(x+.45,8.65),xytext=(x,8.65),arrowprops=dict(arrowstyle='->',color=navy,lw=2))
ax.text(.65,7.28,r'Word $p_{a_1}\otimes\cdots\otimes p_{a_h}$:  $\tau=\prod_t w_{a_t}^{\tau}$  and  $\rho=\prod_t w_{a_t}^{\rho}$',fontsize=14,color=navy)
ax.text(.65,6.85,'Permutation orbit O: identical word weights; old count Rₒ = |O|·(Σoₐ)/h ∈ ℤ.',fontsize=14,color=navy)
ax.text(.65,6.37,'Retain min(Rₒ, |O|) old occurrences. Choose |O| − min(Rₒ, |O|) residual words.',fontsize=14,color=green)
ax.text(.65,5.94,'Therefore τ(q₀) + Στ(gᵢ′) = 1 exactly; Δτ ≤ √(vτ/h) → 0.',fontsize=16,weight='bold',color=green)
ax.plot([.55,15.45],[5.48,5.48],color=light,lw=2)
ax.text(.65,5.06,'Exact arithmetic check: two letters, occupancies (2, 0), h = 3',fontsize=14,weight='bold',color=navy)
cols=['first letters c','orbit size','old Rₒ','retain','delete','residual']
rows=[[0,1,0,0,0,1],[1,3,2,2,0,1],[2,3,4,3,1,0],[3,1,2,1,1,0]]
table=ax.table(cellText=rows,colLabels=cols,colWidths=[.14,.12,.12,.12,.12,.12],bbox=[.04,.253,.53,.17],cellLoc='center')
table.auto_set_font_size(False);table.set_fontsize(11)
for (row,col),cell in table.get_celld().items():
    cell.set_edgecolor('white');cell.set_facecolor(light if row==0 else '#f5f8fb')
    cell.get_text().set_color(navy)
ax.text(.65,2.25,'Physical weights (1/3, 2/3):  loss 1/9; retain 5/9; residual 4/9.',fontsize=12,color=navy)
ax.text(.65,1.81,'Dual weights (2/3, 1/3):  loss 4/9; retain 8/9; residual 1/9.',fontsize=12,color=navy)
ax.text(.65,1.35,'The dual old total is 4/3. Its values remain separate and explicit.',fontsize=12,color=red)
ax.text(.65,.82,'Whole residual f* gets q₀’s actual origin. All three rows, prefix/cups and fixed targets return.',fontsize=12,color=navy)
ax.text(.65,.35,'Left map is not trace preservation to the upward RIGHT tower trace. Arithmetic table is not claimed as a subfactor invariant.',fontsize=10,color=navy)
plot=fig.add_axes([.64,.22,.31,.23])
hs=list(range(1,97))
plot.plot(hs,[float(x) for x in loss_curve],color=green,label='exact physical loss')
plot.plot(hs,[float(x) for x in dual_curve],color=red,label='exact dual loss')
plot.plot(hs,[(8/(9*h))**.5 for h in hs],color=blue,ls='--',label='proved physical bound')
plot.axhline(1/3,color=red,lw=.7,ls=':')
plot.set_xlabel('number h of actual copies');plot.set_ylabel('cut trace')
plot.set_ylim(0,1);plot.legend(fontsize=8,frameon=False);plot.grid(alpha=.2)
fig.savefig(D/'permutation-orbit-residual-v25.png',dpi=135)
fig.savefig(D/'permutation-orbit-residual-v25.svg',metadata={'Date':None})
plt.close(fig)

report={'checked_at_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),
 'exact_allocations':tested,'permutation_orbits_integrality_checks':orbits,
 'actual_full_endpoint_trace_vertices':vertices,'actual_WM_checks':actual,
 'fixture':fixture,'binary_loss_curve_exact_points':96,
 'scope':'Exact arithmetic checks plus actual full WM endpoint ranks; mathematical proof is in the companion exposition.',
 'cc0':'CC0-1.0'}
def serial(x):
    if isinstance(x,Q):return str(x)
    raise TypeError(type(x).__name__)
(D/'CHECKS.json').write_text(json.dumps(report,indent=2,ensure_ascii=False,default=serial)+'\n',encoding='utf-8')
print(json.dumps({k:report[k] for k in ['exact_allocations','permutation_orbits_integrality_checks','actual_full_endpoint_trace_vertices','binary_loss_curve_exact_points']}))
