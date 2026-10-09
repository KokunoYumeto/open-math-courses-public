"""Exact finite checks and Figure WBR/DNP.

Code and diagram: GPT-6.1 Sol (OpenAI), October 2026. CC0-1.0.
Requires Python, SymPy and Matplotlib. No external data or private files.
"""
from pathlib import Path
from fractions import Fraction as Q
from math import ceil, comb, lcm
import datetime, hashlib, json, random
import sympy as sp
import matplotlib
matplotlib.use('Agg')
matplotlib.rcParams['svg.hashsalt']='actual-trace-fiber-v24'
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle

D = Path(__file__).resolve().parent

def dot(x,y):
    return sum((a*b for a,b in zip(x,y)),Q())

def fl(x):
    return x.numerator//x.denominator

def integral_intersection(kappas,inactive,s):
    if not kappas:
        return []
    K=sp.Matrix(s,len(kappas),lambda b,t:kappas[t][b])
    KE=K[list(inactive),:] if inactive else sp.zeros(0,len(kappas))
    result=[]
    for c in KE.nullspace():
        v=K*c
        if not any(v):
            continue
        den=lcm(*(int(x.q) for x in v))
        result.append([int(den*x) for x in v])
    # Removing redundant columns is unnecessary for the theorem, but makes
    # the tested rounding coefficients unique in their span.
    if result:
        B=sp.Matrix(s,len(result),lambda b,t:result[t][b])
        result=[result[t] for t in B.rref()[1]]
    return result

def boundary(n,weights,hs,aa,kappas,zz,epsilon,index,depth):
    s=len(n); r=len(hs)
    H=[sum(h[b] for h in hs) for b in range(s)]
    assert all(dot(weights[0],k)==0 for k in kappas)
    assert dot(weights[0],zz)==0
    assert all(dot(w,n)==1 and min(w)>0 for w in weights)
    assert all(0<=aa[i][b]<=hs[i][b]<=n[b] for i in range(r) for b in range(s))
    bs=[Q(n[b])-sum(a[b] for a in aa)+zz[b] for b in range(s)]
    assert all(0<=x<=n[b] for b,x in enumerate(bs))
    if not any(H):
        assert not any(zz)
        return {'empty':True,'trace_vertices':s}
    E=[b for b in range(s) if H[b]==0 and zz[b]==0]
    A=[b for b in range(s) if b not in E]
    nu=min([Q(1)]+[Q(n[b],2*H[b]) for b in range(s) if H[b]])
    ax=[[(1-epsilon)*aa[i][b]+epsilon*nu*hs[i][b] for b in range(s)] for i in range(r)]
    zx=[(1-epsilon)*v for v in zz]
    bx=[Q(n[b])-sum(a[b] for a in ax)+zx[b] for b in range(s)]
    assert all(0<bx[b]<n[b] for b in A)
    assert all(bx[b]==n[b] and zx[b]==0 and all(a[b]==0 for a in ax) for b in E)
    kk=integral_intersection(kappas,E,s)
    assert all(dot(weights[0],v)==0 and all(v[b]==0 for b in E) for v in kk)
    if kk:
        B=sp.Matrix(s,len(kk),lambda b,t:kk[t][b])
        theta=B.gauss_jordan_solve(sp.Matrix([sp.Rational(z.numerator,z.denominator) for z in zx]))[0]
        th=[Q(int(x.p),int(x.q)) for x in theta]
    else:
        assert not any(zx)
        th=[]
    eta=min(min(bx[b],n[b]-bx[b]) for b in A)
    K=Q(max(sum(abs(v[b]) for v in kk) for b in A),2)
    cutoff=max(1,ceil((r+K)/eta))
    totals=[dict(retained=Q(),loss=Q(),residual=Q(),correction=Q()) for w in weights]
    unit=Q();minimum=Q();small=Q();vertices=0;blocks=[]
    for ell in range(depth+1):
        if index==2 and ell<depth:
            continue
        dim=2**ell; multiplicity=comb(depth,ell)
        gamma=(1/index)**ell*(1-2/index)**(depth-ell)
        mass=multiplicity*gamma
        unit+=dim*mass;minimum+=mass
        large=dim>=cutoff
        if large:
            us=[[fl(dim*a[b]) for b in range(s)] for a in ax]
            ks=[fl(dim*t+Q(1,2)) for t in th]
            ts=[dim*n[b]-sum(u[b] for u in us)+sum(k*v[b] for k,v in zip(ks,kk)) for b in range(s)]
            assert all(-K<=ts[b]-dim*bx[b]<r+K for b in A)
        else:
            small+=dim*mass
            us=[[0]*s for _ in hs];ks=[0]*len(kk);ts=[dim*x for x in n]
        assert all(ts[b]==dim*n[b] for b in E)
        assert all(0<=ts[b]<=dim*n[b] for b in range(s))
        assert all(0<=us[i][b]<=dim*hs[i][b] for i in range(r) for b in range(s))
        for b in range(s):
            # Every finite normalized trace on this actual cup subalgebra is
            # a convex combination of these block-trace vertices.
            assert 0<=Q(ts[b],dim*n[b])<=1
            assert all(0<=Q(u[b],dim*n[b])<=1 for u in us)
            vertices+=1
        for j,w in enumerate(weights):
            ret=sum((dot(w,u) for u in us),Q())
            loss=sum((dot(w,[dim*hs[i][b]-us[i][b] for b in range(s)]) for i in range(r)),Q())
            residual=dot(w,ts)
            correction=sum((k*dot(w,v) for k,v in zip(ks,kk)),Q())
            assert residual-(dim-ret)==correction
            for name,val in [('retained',ret),('loss',loss),('residual',residual),('correction',correction)]:
                totals[j][name]+=mass*val
        blocks.append(dict(dimension=dim,large=large,retained=us,residual=ts,exchange=ks))
    assert unit==1 and minimum==(1-1/index)**depth
    assert totals[0]['residual']==1-totals[0]['retained']
    for j,w in enumerate(weights):
        S=sum((dot(w,h) for h in hs),Q())
        C=sum((dot(w,[Q(hs[i][b])-aa[i][b] for b in range(s)]) for i in range(r)),Q())
        Cx=sum((dot(w,[Q(hs[i][b])-ax[i][b] for b in range(s)]) for i in range(r)),Q())
        Ax=sum((dot(w,a) for a in ax),Q());WA=sum((w[b] for b in A),Q())
        assert Cx==(1-epsilon)*C+epsilon*(1-nu)*S and Cx<=C+epsilon*S
        bound=Cx+r*WA*minimum+Ax*small
        coarse=C+epsilon*S+(r*WA+(cutoff-1)*Ax)*minimum
        assert totals[j]['loss']<=bound<=coarse
        assert totals[j]['residual']-(1-totals[j]['retained'])==totals[j]['correction']
        totals[j].update(S=S,C=C,C_repaired=Cx,bound=bound,coarse=coarse)
    R0=(cutoff-1).bit_length()
    tail=sum((Q(comb(depth,ell))*(2/index)**ell*(1-2/index)**(depth-ell) for ell in range(min(depth+1,R0))),Q())
    assert tail==small
    return dict(empty=False,inactive=E,active=A,nu=nu,residual_real=bx,cutoff=cutoff,kernel=kk,totals=totals,blocks=blocks,trace_vertices=vertices)

n=[2,3,1]
wt=[Q(1,10),Q(1,5),Q(1,5)]
wr=[Q(1,8),Q(1,8),Q(3,8)]
whigh=[Q(2,5),Q(1,50),Q(7,50)] # S_dual=8/5>1
weights=[wt,wr,whigh,[Q(1,6)]*3]
hs=[[2,0,0],[2,0,0]];aa=[[Q(x) for x in h] for h in hs]
kappas=[[2,-1,0],[2,0,-1],[0,1,-1]];zz=[Q(2),Q(-1),Q()]
fixture=boundary(n,weights,hs,aa,kappas,zz,Q(1,4),Q(2),4)
assert fixture['inactive']==[2] and fixture['cutoff']==12
assert fixture['residual_real']==[Q(1,4),Q(9,4),Q(1)]
assert fixture['totals'][0]['retained']==Q(13,40) and fixture['totals'][0]['residual']==Q(27,40)
assert fixture['totals'][1]['retained']==Q(13,32) and fixture['totals'][1]['residual']==Q(11,16)
assert fixture['totals'][1]['correction']==Q(3,32)
assert fixture['totals'][2]['S']==Q(8,5)
tested=0;vertices=0
for eps in [Q(1,50),Q(1,20),Q(1,10),Q(1,4),Q(1,2),Q(3,4)]:
    for index in [Q(2),Q(5,2),Q(3),Q(5)]:
        for depth in [0,1,2,4,8,16]:
            result=boundary(n,weights,hs,aa,kappas,zz,eps,index,depth)
            tested+=1;vertices+=result['trace_vertices']
# Exact no-kernel and zero-family conventions, including retained-zero cells.
for ranks in [[],[[0,0,0]],[[1,0,0]],[[2,0,1]]]:
    h0=ranks;a0=[[Q(x) for x in h] for h in h0]
    for index in [Q(2),Q(3)]:
        for depth in [0,3,12]:
            result=boundary(n,weights,h0,a0,[],[Q()]*3,Q(1,5),index,depth)
            tested+=1;vertices+=result['trace_vertices']

rng=random.Random(2409)
accepted=0
while accepted<160:
    h0=[[rng.randrange(n[b]+1) for b in range(3)] for i in range(rng.randrange(1,4))]
    a0=[[Q(h[b]*rng.randrange(5),4) for b in range(3)] for h in h0]
    th=[Q(rng.randrange(-4,5),4),Q(rng.randrange(-4,5),4)]
    z0=[sum((th[t]*kappas[t][b] for t in range(2)),Q()) for b in range(3)]
    b0=[Q(n[b])-sum(a[b] for a in a0)+z0[b] for b in range(3)]
    if not all(0<=b0[b]<=n[b] for b in range(3)):
        continue
    result=boundary(n,weights,h0,a0,kappas,z0,Q(1,rng.randrange(2,12)),rng.choice([Q(2),Q(5,2),Q(3)]),rng.randrange(0,13))
    accepted+=1;tested+=1;vertices+=result['trace_vertices']

# Actual five-label endpoint enumeration, with the full parity subgroup retained.
# An endpoint is (finite lamp set, translation triple, central integer grade).
zero=(frozenset(),(0,0,0),0)
az=(frozenset({(0,0,0)}),(0,0,0),1)
def mul(a,b):
    lamps,v,r=a;other,w,t=b
    shifted=frozenset(tuple(v[j]+x[j] for j in range(3)) for x in other)
    return (lamps.symmetric_difference(shifted),tuple(v[j]+w[j] for j in range(3)),r+t)
def labels(sign):
    return [zero,(az[0],az[1],sign)]+[(frozenset(),tuple(sign if j==axis else 0 for j in range(3)),0) for axis in range(3)]
def step(coeffs,sign):
    out={}
    for g,c in coeffs.items():
        for label in labels(sign):
            h=mul(g,label);out[h]=out.get(h,0)+c
    return out
X,T=sp.symbols('X T',nonzero=True)
def aggregate(coeffs):
    return sp.expand(sum(c*X**g[2] for g,c in coeffs.items()))
endpoint_checks=0;endpoint_counts=[]
for phase in [1,-1]:
    source=step(step({zero:1},phase),-phase)
    assert zero in source and az in source
    assert aggregate(source)==sp.expand((4+X)*(4+X**-1))
    assert all(g[2]%2==len(g[0])%2 for g in source)
    direction={zero:T,az:-1};expected=T-X
    counts=source;den=(4+T)*(4+T**-1)
    dualden=den
    for t in range(7):
        agg=aggregate(direction)
        assert sp.expand(agg-expected)==0 and agg!=0
        assert sp.simplify(agg.subs(X,T)/den)==0
        assert sp.simplify(agg.subs(X,T**-1)/dualden-(T-T**-1)/((4+T)*(4+T**-1)))==0
        assert all(g[2]%2==len(g[0])%2 for g in direction)
        assert sum(counts.values())==5**(2+t)
        endpoint_checks+=1
        endpoint_counts.append(dict(phase=phase,tail_depth=t,full_endpoint_blocks=len(counts),direction_endpoint_blocks=len(direction)))
        sign=phase*(-1)**t
        factor=4+X**sign
        expected=sp.expand(expected*factor)
        direction=step(direction,sign);counts=step(counts,sign)
        den*=4+T**sign;dualden*=4+T**(-sign)

# Reproducible research illustration, with exact labels rather than a false
# numerical transcendental approximation. Positions encode layout only.
fig=plt.figure(figsize=(15,10),dpi=140,facecolor='white')
ax=fig.add_axes([0,0,1,1]);ax.set_xlim(0,15);ax.set_ylim(0,10);ax.axis('off')
navy='#183b56';blue='#3685b5';green='#41916e';red='#c45a45';gray='#e6ebf0'
ax.text(.6,9.45,'Actual cup boundary repair and exact direction nonpromotion',fontsize=21,color=navy,weight='bold')
ax.text(.6,9.03,'WBR.1–20 and DNP.1–11  |  all depths are actual Jones stages',fontsize=12,color=navy)
ax.text(.6,8.45,'Weak residual → ε = 1/4 repair → dimension-16 cup rank check',fontsize=15,color=navy,weight='bold')
for j,(cap,old,new) in enumerate(zip(n,[Q(0),Q(2),Q(1)],[Q(1,4),Q(9,4),Q(1)])):
    y=7.65-j*.85
    ax.text(.65,y+.12,f'block {j+1}: n = {cap}',fontsize=12,color=navy)
    for x,val in [(3.2,old),(7.1,new)]:
        ax.add_patch(Rectangle((x,y),3,.35,color=gray))
        ax.add_patch(Rectangle((x,y),3*float(val)/cap,.35,color=green if j==2 else blue))
        ax.text(x+1.5,y+.49,f'b = {val}',ha='center',fontsize=12,color=navy)
    ax.text(10.65,y+.12,'inactive: full unit' if j==2 else 'active: strict interior',fontsize=12,color=green if j==2 else navy)
ax.text(3.2,8.02,'before',fontsize=11,color=navy)
ax.text(7.1,8.02,'after',fontsize=11,color=navy)
ax.text(.65,4.92,'Ranks: retained (26, 0, 0) in each old cell; residual (4, 36, 16)',fontsize=13,color=navy)
ax.text(.65,4.55,'Physical: 13/40 + 27/40 = 1     Dual: 13/32 + 11/16 = 1 + 3/32',fontsize=13,color=navy)
ax.plot([.6,14.4],[4.13,4.13],color=gray,lw=2)
ax.text(.65,3.62,'A different actual WM inclusion: transcendental λ ∈ (1, 2)',fontsize=15,color=navy,weight='bold')
ax.text(.65,3.08,'Source direction on reachable endpoint blocks 1 and az:  v = (λ, −1)',fontsize=13,color=navy)
ax.text(.65,2.55,'Grade aggregate:  λ − X',fontsize=14,color=red)
ax.text(6.2,2.55,'each + step × (4 + X); each − step × (4 + X⁻¹)',fontsize=13,color=navy)
ax.annotate('',xy=(5.65,2.62),xytext=(4.65,2.62),arrowprops=dict(arrowstyle='->',color=navy,lw=2))
ax.text(.65,1.98,'At every later depth:  (λ − X)(4 + X)ᵖ(4 + X⁻¹)ᑫ ≠ 0',fontsize=15,color=red)
ax.text(.65,1.42,'Every integer physical-null vector has zero aggregate in every grade.',fontsize=13,color=navy)
ax.text(.65,.92,'Physical evaluation = 0; original dual evaluation = (λ − λ⁻¹)/dᵘ > 0.',fontsize=13,color=navy)
ax.text(.65,.42,'Upper arithmetic fixture is not asserted to be a Jones invariant. Lower argument concerns exact promotion only.',fontsize=10,color=navy)
fig.savefig(D/'boundary-and-direction-v24.png',dpi=140)
fig.savefig(D/'boundary-and-direction-v24.svg',metadata={'Date':None})
plt.close(fig)

report={
    'checked_at_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),
    'boundary_constructions':tested,'finite_trace_simplex_vertices':vertices,
    'actual_full_endpoint_symbolic_checks':endpoint_checks,
    'actual_endpoint_counts':endpoint_counts,
    'fixture':fixture,
    'scope':'Exact rational arithmetic and formal actual five-label endpoint checks; not a proof of the unrestricted allocation.',
    'cc0':'CC0-1.0',
}
def serial(obj):
    if isinstance(obj,Q):return str(obj)
    raise TypeError(type(obj).__name__)
(D/'CHECKS.json').write_text(json.dumps(report,ensure_ascii=False,indent=2,default=serial)+'\n',encoding='utf-8')
print(json.dumps({k:report[k] for k in ['boundary_constructions','finite_trace_simplex_vertices','actual_full_endpoint_symbolic_checks']}))
