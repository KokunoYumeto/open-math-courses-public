from pathlib import Path
from fractions import Fraction as Q
from math import comb, ceil
import datetime, hashlib, json, random

D=Path(__file__).resolve().parent
R=D.parents[1]
def dot(a,b): return sum((x*y for x,y in zip(a,b)),Q())
def nearest(x): return (x+Q(1,2)).numerator//(x+Q(1,2)).denominator
def floor(x): return x.numerator//x.denominator

def construction(n,weights,hs,aa,kappas,theta,index,depth):
    s=len(n); r=len(hs)
    z=[sum((t*v[b] for t,v in zip(theta,kappas)),Q()) for b in range(s)]
    bs=[Q(n[b])-sum(a[b] for a in aa)+z[b] for b in range(s)]
    assert all(0<x<n[b] for b,x in enumerate(bs))
    eta=min(min(x,n[b]-x) for b,x in enumerate(bs))
    K=max((sum(abs(v[b]) for v in kappas) for b in range(s)),default=0)/Q(2)
    cutoff=max(1,ceil((r+K)/eta))
    assert all(dot(weights[0],v)==0 for v in kappas)
    assert all(dot(w,n)==1 and all(x>0 for x in w) for w in weights)
    assert all(0<=a[b]<=hs[i][b]<=n[b] for i,a in enumerate(aa) for b in range(s))
    totals=[{'retained':Q(),'loss':Q(),'residual':Q(),'correction':Q()} for _ in weights]
    sum_min=Q();sum_unit=Q();small_mass=Q();trace_tests=0
    blocks=[]
    for ell in range(depth+1):
        if index==2 and ell<depth: continue
        count=comb(depth,ell); dim=2**ell
        gamma=(1/index)**ell*(1-2/index)**(depth-ell)
        mass=count*gamma; sum_min+=mass;sum_unit+=dim*mass
        large=dim>=cutoff
        if not large: small_mass+=dim*mass
        if large:
            us=[[floor(dim*a[b]) for b in range(s)] for a in aa]
            ks=[nearest(dim*t) for t in theta]
            ts=[dim*n[b]-sum(u[b] for u in us)+sum(k*v[b] for k,v in zip(ks,kappas)) for b in range(s)]
        else:
            us=[[0]*s for _ in aa];ks=[0]*len(kappas);ts=[dim*x for x in n]
        assert all(0<=ts[b]<=dim*n[b] for b in range(s))
        assert all(0<=us[i][b]<=dim*hs[i][b] for i in range(r) for b in range(s))
        for b in range(s):
            # Every normalized finite trace is a convex combination of these
            # block traces. Positivity/unit bounds are checked at every vertex.
            value=Q(ts[b],dim*n[b]); assert 0<=value<=1;trace_tests+=1
        for ix,w in enumerate(weights):
            ret=sum((dot(w,u) for u in us),Q())
            lost=sum((dot(w,[dim*hs[i][b]-us[i][b] for b in range(s)]) for i in range(r)),Q())
            resid=dot(w,ts)
            corr=sum((k*dot(w,v) for k,v in zip(ks,kappas)),Q())
            assert resid-(dim-ret)==corr
            for key,val in [('retained',ret),('loss',lost),('residual',resid),('correction',corr)]:
                totals[ix][key]+=mass*val
        blocks.append({'dimension':dim,'count':count,'large':large,'retained_ranks':us,'residual_ranks':ts,'integer_exchange':ks,'minimal_weight':str(gamma)})
    assert sum_min==(1-1/index)**depth and sum_unit==1
    assert totals[0]['residual']==1-totals[0]['retained']
    for ix,w in enumerate(weights):
        c=sum((dot(w,[Q(hs[i][b])-aa[i][b] for b in range(s)]) for i in range(r)),Q())
        a=sum((dot(w,x) for x in aa),Q());W=sum(w,Q())
        bound=c+r*W*sum_min+a*small_mass
        assert totals[ix]['loss']<=bound
        assert bound<=c+(r*W+(cutoff-1)*a)*sum_min
        assert totals[ix]['residual']-(1-totals[ix]['retained'])==totals[ix]['correction']
        totals[ix]['bound']=bound
    return {'eta':eta,'K':K,'cutoff':cutoff,'totals':totals,'blocks':blocks,'trace_vertices':trace_tests,'small_block_mass':small_mass}

weights=[[Q(1,8),Q(1,4)],[Q(1,5),Q(1,5)]]
n=[2,3];hs=[[2,0],[2,0]];kk=[[2,-1]];th=[Q(7,5)]
first=construction(n,weights,hs,[[Q(2),Q(0)]]*2,kk,th,Q(3),2)
assert first['cutoff']==4
assert first['totals'][0]['retained']==Q(2,9)
assert first['totals'][0]['loss']==Q(5,18)
assert first['totals'][0]['residual']==Q(7,9)
assert first['totals'][1]['retained']==Q(16,45)
assert first['totals'][1]['loss']==Q(4,9)
assert first['totals'][1]['correction']==Q(2,15)
second=construction(n,weights,hs,[[Q(19,10),Q(0)]]*2,kk,th,Q(3),15)
assert second['cutoff']==3 and second['totals'][0]['loss']<Q(3,100)
assert Q(17,10)*Q(2,3)**15<Q(1,200)

fixtures=0;trace_vertices=0
for depth in range(0,31):
    for index in [Q(2),Q(5,2),Q(3),Q(5)]:
        for first_rank in [Q(2),Q(19,10),Q(7,4),Q(3,2)]:
            out=construction(n,weights,hs,[[first_rank,Q(0)]]*2,kk,th,index,depth)
            fixtures+=1;trace_vertices+=out['trace_vertices']

# Multiple independent kernel vectors; one physical kernel move has zero
# dual value, the other does not. This tests the full sum, not one vector.
n3=[2,3,4];w3=[[Q(1,12),Q(1,6),Q(1,12)],[Q(1,9)]*3]
h3=[[2,0,0],[2,0,0]];a3=[[Q(7,4),Q(0),Q(0)]]*2
k3=[[2,-1,0],[1,0,-1]];t3=[Q(7,5),Q(2,5)]
for depth in range(31):
    for index in [Q(2),Q(3),Q(7,2)]:
        out=construction(n3,w3,h3,a3,k3,t3,index,depth)
        fixtures+=1;trace_vertices+=out['trace_vertices']

# Empty integral-kernel list and one zero old cell are legitimate inputs.
# Their source residual is strictly interior; no exchange is manufactured.
for depth in range(16):
    out=construction([2,3],weights,[[1,1],[0,0]],[[Q(1,2),Q(1,2)],[Q(0),Q(0)]],[],[],Q(3),depth)
    fixtures+=1;trace_vertices+=out['trace_vertices']

report={'checked_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),
        'status':'pass','exact_rational_constructions':fixtures,
        'finite_trace_simplex_vertices':trace_vertices,
        'canonical_dual_nonzero_correction':'2/15',
        'second_check_actual_physical_loss':str(second['totals'][0]['loss']),
        'second_check_upper_bound':str(second['totals'][0]['bound']),
        'scope':'Exact arithmetic supports the complete finite proof; no numerical fixture is asserted to be a subfactor realization or a general amenability-derived allocation.'}
(D/'checks.json').write_text(json.dumps(report,indent=2)+'\n',encoding='utf-8')

import matplotlib
matplotlib.use('Agg')
matplotlib.rcParams['svg.hashsalt']='oa-subfactors-SFQ-v23'
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch
fig,ax=plt.subplots(figsize=(14,9));ax.set_xlim(0,14);ax.set_ylim(0,9);ax.axis('off')
fig.patch.set_facecolor('#f7f9fc');ax.set_facecolor('#f7f9fc')
def box(x,y,w,h,title,body,color='#dceaf4'):
    ax.add_patch(FancyBboxPatch((x,y),w,h,boxstyle='round,pad=0.08',facecolor=color,edgecolor='#364b63',linewidth=1.2))
    ax.text(x+.16,y+h-.22,title,fontsize=12,fontweight='bold',va='top',color='#18324c')
    ax.text(x+.16,y+h-.57,body,fontsize=10.4,va='top',linespacing=1.5,color='#18324c')
def arrow(x,y,xx,yy):ax.annotate('',xy=(xx,yy),xytext=(x,y),arrowprops={'arrowstyle':'->','lw':1.7,'color':'#364b63'})
ax.text(.35,8.65,'Scalar trace exchanges become integral inside actual Jones cup blocks',fontsize=17,fontweight='bold',color='#18324c')
box(.35,6.25,4.05,1.82,'Actual finite row F = Nₘ′ ∩ Nₖ',
    'Old ranks hᵢ; retained real ranks aᵢ ≤ hᵢ\nInteger relations κᵗ satisfy τ(κᵗ) = 0\nResidual b = n − Σaᵢ + Σθₜκᵗ\nStrict interior: 0 < b < n  (SFQ.1–5)')
box(4.95,6.25,4.1,1.82,'Actual separated cup inclusion',
    'F ⊗ Cʰ ⊂ Nₘ₊₃ₕ′ ∩ Nₖ\nCup block size D = 2ˡ; minimal weight γ\nΣ Dγ = 1;  Σγ = (1 − 1/d)ʰ\nBoth original traces factor  (CTR.5–13)')
box(9.6,6.25,4.02,1.82,'One finite level for every row',
    'Large block: uᵢ = floor(Daᵢ)\nkₜ = floor(Dθₜ + 1/2)\nt = Dn − Σuᵢ + Σkₜκᵗ\nSmall block: uᵢ = 0,  t = Dn')
arrow(4.45,7.15,4.85,7.15);arrow(9.1,7.15,9.5,7.15)
box(.35,3.66,6.1,1.98,'Exact physical scalar certificate  (SFQ.7–17)',
    'All ranks: 0 ≤ uᵢ ≤ Dhᵢ and 0 ≤ t ≤ Dn\nActual gᵢ′ ≤ gᵢ; actual q₀ has rank t\nτ(q₀) = 1 − Στ(gᵢ′), exactly\nDual correction = Σ γkₜρ(κᵗ); it can be nonzero',color='#e2f0e8')
box(7.0,3.66,6.62,1.98,'Whole residual and marked return  (SFQ.18–19)',
    'rᵢ′ = Uᵢgᵢ′Uᵢ* ≤ rᵢ;  f* = f + Σ(rᵢ − rᵢ′)\nPlace q₀ onto f* by an Nₖ unitary\nAll three square rows; both actual trace systems; prefix cups\nSame targets: added error ≤ √[2(‖y‖² + γᵧ²)Δ]',color='#e2f0e8')
ax.plot([11.6,11.6,3.4],[6.16,5.96,5.96],color='#364b63',lw=1.7)
arrow(3.4,5.96,3.4,5.78);arrow(6.52,4.63,6.91,4.63)
box(.35,1.04,6.1,2.08,'Exact finite check 1: d = 3, h = 2',
    'n = (2,3); τ weights = (1/8,1/4); ρ = (1/5,1/5)\nκ = (2,−1):  τ(κ) = 0,  ρ(κ) = 1/5\nCup sizes 4,2,2,1; every minimal cup weight = 1/9\nLarge block: u₁ = u₂ = (8,0); residual t = (4,6)\nτ(q₀) = 7/9; exact dual correction = 2/15',color='#fff0d8')
box(7.0,1.04,6.62,2.08,'Implementation bound and remaining selection',
    'Lossσₕ ≤ Cσ + rWσ(1−1/d)ʰ + Aσ Bₕ(D₀)\nBₕ is the exact lower binomial tail of small cup blocks\nCσ is the original fractional removal, kept separate\nEvery other finite trace uses its actual rank weights\nNo general small-loss real allocation is supplied',color='#fff0d8')
ax.text(.35,.52,'All box sizes are schematic. Proof: SFQ.1. Checks 1–2 are finite arithmetic fixtures, not asserted Jones invariants.',fontsize=10.2,color='#364b63')
ax.text(.35,.23,'Human context: Sorin Popa (1994), Theorem 4.4.1(1), p.222. Independent proof and figure: CC0-1.0.',fontsize=10.2,color='#364b63')
fig.savefig(D/'scalar-fiber-quantization-v23.svg',bbox_inches='tight',metadata={'Date':None})
fig.savefig(D/'scalar-fiber-quantization-v23.png',dpi=145,bbox_inches='tight')
plt.close(fig)
print(json.dumps(report))
