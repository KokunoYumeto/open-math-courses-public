"""Exact finite path/clock checks, with separately labelled logarithmic diagnostics."""
from fractions import Fraction as F
from collections import Counter
from decimal import Decimal as D,localcontext
from math import isqrt
import json
counts=Counter();paths=[]
def T(n):return (3*n+1)//2 if n%2 else n//2
for n in range(1,385):
    xs=[n]
    while xs[-1]>1 and len(xs)<1001:xs.append(T(xs[-1]))
    assert xs[-1]==1
    raw=[n];ss=[0];Ps=[F(1)];ratios=[F(1)]
    for j,x in enumerate(xs[:-1]):
        p=x%2
        if p:raw.append(3*x+1)
        raw.append(T(x))
        ss.append(ss[-1]+p)
        Ps.append(Ps[-1]*(F(3*x,3*x+1) if p else 1))
        z=xs[j+1];k=j+1
        assert raw[k+ss[k]]==z
        assert F(n)==F(2**k*z,3**ss[k])*Ps[k]
        q=F(4**k*z*z,3**k*n*n)
        assert q==F(3)**(2*ss[k]-k)/Ps[k]**2
        ratios.append(q);counts['exact_prefix_products']+=1
    assert all(Ps[i]>=Ps[i+1]>0 for i in range(len(Ps)-1))
    levels={F(1),F(n)}
    for x in xs:
        if x<=n:levels.add(F(x))
        if 1<=F(2*x-1,2)<=n:levels.add(F(2*x-1,2))
    crossings=[]
    for z in sorted(levels):
        t=next(i for i,x in enumerate(xs) if x<=z)
        u=next(i for i,x in enumerate(raw) if x<=z)
        assert u==t+ss[t] and raw[u]==xs[t]
        if z<n:assert z/2<xs[t]<=z and xs[t-1]%2==0
        assert max(xs[:t+1])<=max(xs) and max(raw[:u+1])<=max(raw)
        crossings.append((z,t,u));counts['exact_real_level_crossings']+=1
    top=max(ratios+[1/q for q in ratios]);K=max(1,isqrt(top.numerator//top.denominator))
    while F(K*K)<top:K+=1
    assert all(F(1,K*K)<=q<=K*K for q in ratios)
    paths.append((n,xs,raw,ss,Ps,K,crossings));counts['actual_finite_paths']+=1
with localcontext() as ctx:
    ctx.prec=90
    ln2=D(2).ln();ln3=D(3).ln();d=ln2-ln3/2;tol=D('1e-75');diag=Counter()
    for n,xs,raw,ss,Ps,K,crossings in paths:
        E=D(K).ln();a=D(Ps[-1].denominator).ln()-D(Ps[-1].numerator).ln()
        B=(E+a)/ln3;radius=E+2*d*B/3+ln2-2*d/3
        for j,x in enumerate(xs):
            e=D(x).ln()-D(n).ln()+d*j
            aj=D(Ps[j].denominator).ln()-D(Ps[j].numerator).ln()
            assert abs(e)<=E+tol
            assert abs(e-(D(ss[j])-D(j)/2)*ln3-aj)<=tol
            assert -(E+a)/ln3-tol<=D(ss[j])-D(j)/2<=E/ln3+tol
            diag['logarithmic_prefix_identities']+=1
        for i,x in enumerate(raw):
            assert abs(D(x).ln()-D(n).ln()+2*d*i/3)<=radius+tol
            diag['ordinary_path_bounds']+=1
        for z,t,u in crossings:
            lz=D(z.numerator).ln()-D(z.denominator).ln()
            q=(D(n).ln()-lz)/d
            assert abs(D(t)-q)<=(E+ln2)/d+tol
            assert abs(D(u)-3*q/2)<=3*(E+ln2)/(2*d)+B+tol
            diag['first_passage_bounds']+=1
    p=ln2/ln3;kappa=1+(p*p.ln()+(1-p)*(1-p).ln())/ln2
    Astar=1/(2*kappa)
    for M in [10**3,10**6,10**12,10**24]:
        logM=D(M+2).ln()/ln2
        for A in [Astar+D(1),Astar+1/D(M+2).ln().sqrt(),2*Astar]:
            L=int(A*logM)+1;Lp=int(A*(D(M)*ln2).ln()/ln2)
            delta=kappa*L-logM/2;deltap=kappa*Lp-logM/2
            bound=2+abs(A)*(D(3)/ln2).ln()/ln2
            assert abs(L-Lp)<=bound
            assert abs(delta-deltap)<=kappa*bound
            diag['moving_rank_comparisons']+=1
# The illustration uses E=log9, proved by exact integer inequalities.
n=1048587;xs=[n];P=F(1);s=0
while xs[-1]>1024:
    x=xs[-1]
    if x%2:P*=F(3*x,3*x+1);s+=1
    xs.append(T(x));j=len(xs)-1
    assert 3**j*n*n<=81*4**j*xs[-1]**2
    assert 4**j*xs[-1]**2<=81*3**j*n*n
assert P>=F(999,1000)
assert len(xs)-1==37 and xs[-1]==986 and s==17
print(json.dumps(dict(passed=True,counts=dict(counts),
 exact_scope="Actual finite trajectories; exact prefix products and exponentiated logarithmic identities; rational-level first crossings and clock maps. Finite tests do not establish natural density.",
 illustration=dict(n=n,shortcut_time=37,ordinary_time=37+s,landing=986,E="log9",a="log(1000/999)",integer_bounds_verified=True),
 diagnostics=dict(precision_digits=90,counts=dict(diag),scope="Logarithmic path and passage inequalities and moving-rank comparisons are numerical diagnostics, not formal certificates."),
 formal_status="General results are written proofs, self-checked by the writing AI; no independent review or Lean replay."),indent=2))

