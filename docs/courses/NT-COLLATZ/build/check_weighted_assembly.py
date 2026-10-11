"""Exact finite checks for weighted first-passage assembly.
These checks test identities and finite examples, not an infinite asymptotic theorem.
The independent geometric offset is computed exactly by summing periodic classes,
not by truncating the infinite geometric distribution.
"""
from fractions import Fraction as F
from itertools import product
from collections import Counter
from math import comb
from pathlib import Path
import hashlib, json
import mpmath as mp

ROOT=Path(__file__).resolve().parents[1]
mp.mp.dps=150
counts=Counter()

def check(value, name):
    assert value, name
    counts[name]+=1

def words(n,s):
    if n==1:
        if s>=1: yield (s,)
        return
    for a in range(1,s-n+2):
        for b in words(n-1,s-a): yield (a,)+b

def prob(n,s):
    return F(comb(s-1,n-1),2**s) if s>=n>=1 else F(0)

def offset(a):
    return sum((F(3**(len(a)-j-1),2**sum(a[j:])) for j in range(len(a))),F(0))

def forward_offset(a):
    return sum((F(3**j,2**sum(a[:j+1])) for j in range(len(a))),F(0))

def residue(x,q):
    return x.numerator*pow(x.denominator,-1,q)%q

def independent(m):
    q=3**m
    period=2*3**(m-1)
    letter={a:F(2**(period-a),2**period-1) for a in range(1,period+1)}
    law=Counter()
    for a in product(letter,repeat=m):
        mass=F(1)
        for t in a: mass*=letter[t]
        law[residue(forward_offset(a),q)]+=mass
    check(sum(law.values())==1,"periodic_geometric_mass")
    return law

rhos={m:independent(m) for m in [1,2]}
for nu in range(2,5):
    Q=3**nu
    for s in range(nu,3*nu+1):
        ws=list(words(nu,s))
        check(len(ws)==comb(s-1,nu-1),"composition_count")
        mu=Counter()
        for a in ws:
            check(offset(a)==forward_offset(a[::-1]),"exact_reversal")
            mu[residue(offset(a),Q)]+=F(1,len(ws))
        for m in range(1,min(2,nu-1)+1):
            q=3**m;k=Q//q
            projected=[sum((mass for v,mass in mu.items() if v%q==x),F(0)) for x in range(q)]
            # Projection after reversal uses the first m coordinates of the reversed word.
            direct=Counter()
            for a in ws:
                direct[residue(forward_offset(a[::-1][:m]),q)]+=F(1,len(ws))
            check(all(direct[x]==projected[x] for x in range(q)),"conditioned_projection")
            for prefix in {a[::-1][:m] for a in ws}:
                t=sum(prefix)
                conditional=F(sum(a[::-1][:m]==prefix for a in ws),len(ws))
                check(conditional==F(1,2**t)*prob(nu-m,s-t)/prob(nu,s),"prefix_likelihood")
            b=2*m
            central=range(max(m,2*m-b),2*m+b+1)
            gamma=max(abs(prob(nu-m,s-t)/prob(nu,s)-1) for t in central)
            ptail=1-sum((prob(m,t) for t in central),F(0))
            qtail=1-sum((prob(m,t)*prob(nu-m,s-t)/prob(nu,s) for t in central),F(0))
            delta=sum((abs(mu[v]-projected[v%q]/k) for v in range(Q)),F(0))
            for z,U in [(7,33),(9,97)]:
                band=list(range(z,U,2));D=len(band);H=sum((F(1,x) for x in band),F(0))
                endpoints=[M for M in range(1,402,2) if M%5!=0 and z<F(2**s*M,Q)<U]
                fineH=[sum((F(Q,M)/H for M in endpoints if M%Q==v),F(0)) for v in range(Q)]
                fineF=[sum((F(2**s,D) for M in endpoints if M%Q==v),F(0)) for v in range(Q)]
                for kind,fine in [("harmonic",fineH),("flat",fineF)]:
                    coarse=[sum((fine[v] for v in range(x,Q,q)),F(0))/k for x in range(q)]
                    explicit=[sum((F(q,M)/H if kind=="harmonic" else F(q*2**s,Q*D)
                                   for M in endpoints if M%q==x),F(0)) for x in range(q)]
                    check(coarse==explicit,"exact_endpoint_fibre_average")
                    lift_expect=sum((projected[x]*coarse[x] for x in range(q)),F(0))
                    check(lift_expect==sum((projected[v%q]/k*fine[v] for v in range(Q)),F(0)),"uniform_lift_identity")
                    target=sum((mu[v]*fine[v] for v in range(Q)),F(0))
                    ref=sum((rhos[m][x]*coarse[x] for x in range(q)),F(0))
                    A=max(fine)
                    check(abs(target-ref)<=gamma*ref+A*(delta/2+ptail+qtail),"relative_comparison_lemma")
                    nominal=F(0)
                    for a in ws:
                        Fa=offset(a)
                        for M in endpoints:
                            if residue(Fa,Q)!=M%Q: continue
                            X=F(2**s,Q)*(M-Fa)
                            check(X.denominator==1 and X>0 and X.numerator%2==1,"positive_integer_inverse")
                            x=int(X)
                            for exponent in a:
                                numerator=3*x+1
                                check(numerator%(2**exponent)==0 and (numerator//2**exponent)%2==1,"exact_valuation_word")
                                x=numerator//2**exponent
                            check(x==M,"inverse_endpoint")
                            nominal+=F(Q,2**s*M)/H if kind=="harmonic" else F(1,D)
                    check(nominal==prob(nu,s)*target,"nominal_cell_identity")
                    if endpoints:
                        cap=(mp.log(mp.mpf(U)/z)/(2*(mp.mpf(H.numerator)/H.denominator))
                             +mp.mpf(Q)*H.denominator/(H.numerator*min(endpoints))) if kind=="harmonic" else F(U-z,2*D)+F(2**s,D)
                        observed=max(mp.mpf(v.numerator)/v.denominator for v in fine)
                        check(observed<=cap+mp.mpf("1e-130"),"finite_arithmetic_cap_diagnostic")

masses=[F(1,5),F(3,10),F(1,2)]
expected=[F(1,30),F(2,45),F(1,15)]
gamma=F(1,10);e=F(1,100)
for pieces in [1,100]:
    ds=[]
    for Y in masses:
        cells=[(Y*q/pieces,q/pieces) for q in [F(1,4),F(3,4)] for _ in range(pieces)]
        refs=[(y+q*e)/(1-gamma) for y,q in cells]
        ds.append(sum((r-y for (y,q),r in zip(cells,refs)),F(0)))
    check(ds==expected and sum(ds)==F(13,90),"absorption_equality_and_refinement")
check(sum(masses)+sum(expected)==F(103,90),"reference_total_not_renormalized")
check((F(9,11)+F(9,29))/3*F(2,3)==F(80,319),"endpoint_collision_exercise")

points=[5,7,9,11,13,15]
for kind in ["flat","harmonic"]:
    raw=[F(1) if kind=="flat" else F(1,x) for x in points]
    law=[x/sum(raw) for x in raw]
    weights=[sum(law[:2]),sum(law[2:5]),law[5]]
    check(sum(weights)==1,"closed_block_weights")
    for bits in product([0,1],repeat=6):
        band_values=[sum(law[i]*bits[i] for i in range(2))/weights[0],
                     sum(law[i]*bits[i] for i in range(2,5))/weights[1]]
        whole=sum(law[i]*bits[i] for i in range(6))
        for Z in [F(0),F(2,3),F(6,5)]:
            rhs=sum(weights[j]*abs(band_values[j]-Z) for j in range(2))+weights[2]*max(Z,abs(1-Z))
            check(abs(whole-Z)<=rhs,"closed_block_discrepancy")
for a,b in [([F(1,3),F(1,2),F(1,6)],[F(1,4),F(2,3),F(1,12)]),
            ([F(1),F(0),F(0)],[F(0),F(0),F(1)])]:
    full=max(abs(sum((a[i]-b[i])*bits[i] for i in range(3))) for bits in product([0,1],repeat=3))
    finite=max(abs(sum((a[i]-b[i])*bits[i] for i in range(2))) for bits in product([0,1],repeat=2))
    check(full==finite==sum(abs(x-y) for x,y in zip(a,b))/2,"completed_total_variation")

diagnostics=[]
for power in [60,80,100]:
    L=mp.mpf(10)**power;ell=mp.log(2);d=mp.log(mp.mpf(4)/3)
    h=int(mp.floor(L/100000));N=int(mp.floor(L/(10*ell)));m=int(mp.ceil(h*L**(-mp.mpf(2)/5)))
    for C in [mp.mpf(".5"),mp.mpf(1),mp.mpf(2)]:
        W=C*mp.sqrt(N*mp.log(N));b0=(10*C)**2+12
        check(W<=mp.mpf(".000022")*L and 6*W+mp.mpf(4)/3/d<=h,"large_scale_window_diagnostic")
        check(2*ell*W+mp.log(mp.mpf(8)/3)<=L**mp.mpf(".7") and L**mp.mpf(".7")+2*ell*W+ell<h*d,"large_scale_endpoint_diagnostic")
        maxgamma=0
        for nu in [int(mp.ceil(mp.mpf(".0034")*L)),int(mp.floor(mp.mpf(".0105")*L))]:
            b=mp.sqrt(12*b0*m*mp.log(nu))+2*b0*mp.log(nu)/d
            check(mp.sqrt(nu)<=m<=nu/2 and m<=h and W+b<=(nu-m)/2,"large_scale_likelihood_domain_diagnostic")
            v=mp.mpf(nu)
            lam=m/v+4*m*W**2/v**2+4*W*b/v+2*b*b/v+4*b/v+4*W*m/v**2+8/v
            maxgamma=max(maxgamma,mp.expm1(lam))
        check(maxgamma<1,"large_scale_absorption_diagnostic")
        diagnostics.append({"log_B":f"1e{power}","C":str(C),"endpoint_gamma_max":mp.nstr(maxgamma,18)})
eta=F(5097587,77645938)
check(F(1,16)<eta<F(1,5)<F(1,4),"exact_exponent_comparison")
result={"passed":True,"scope":"Exact rational finite identities; separately labelled high-precision diagnostics. No infinite theorem or Lean certification from tests.",
        "counts":dict(counts),"diagnostics_precision":150,"schedule_diagnostics":diagnostics,
        "source_sha256":hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}
(ROOT/"checks/weighted_assembly.json").write_text(json.dumps(result,indent=2)+"\n",encoding="utf-8")
print(json.dumps(result,indent=2))
