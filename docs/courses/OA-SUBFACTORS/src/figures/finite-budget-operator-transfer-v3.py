"""Reproduce the exact budget-transfer schematic and finite operator checks."""
from pathlib import Path
SVG='<svg xmlns="http://www.w3.org/2000/svg" width="1260" height="990" viewBox="0 0 1260 990">\n<defs><marker id="arrow" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse"><path d="M0 0 L10 5 L0 10 Z" fill="#334155"/></marker><style>text{font-family:Arial,sans-serif;fill:#122438}.title{font-size:30px;font-weight:700}.head{font-size:22px;font-weight:700}.label{font-size:19px}.small{font-size:17px}.line{stroke:#334155;stroke-width:2.5;fill:none;marker-end:url(#arrow)}.dash{stroke:#b45309;stroke-width:3;stroke-dasharray:9 7;fill:none;marker-end:url(#arrow)}</style></defs>\n<rect width="1260" height="990" fill="#ffffff"/>\n<text x="50" y="48" font-family="Arial,sans-serif" font-size="30" font-weight="bold" fill="#122438">Exact support budgets leave an operator-transfer input</text>\n<text x="50" y="79" font-family="Arial,sans-serif" font-size="19" fill="#122438">Actual Jones stages; different continuations are allowed on different cells.</text>\n<rect x="50" y="112" width="550" height="130" rx="14" fill="#eff6ff" stroke="#2563eb" stroke-width="2"/>\n<text x="72" y="145" font-family="Arial,sans-serif" font-size="22" font-weight="bold" fill="#122438">Old physical partition p and finite square P0</text>\n<text x="72" y="175" font-family="Arial,sans-serif" font-size="19" fill="#122438">sum p_i = 1; lambda_i = tau(p_i)</text>\n<text x="72" y="205" font-family="Arial,sans-serif" font-size="19" fill="#122438">b_y = E_P0(y); old error &lt; eps/2</text>\n<text x="72" y="228" font-family="Arial,sans-serif" font-size="17" fill="#122438">Available near-cover and residual: 76.4</text>\n<rect x="660" y="112" width="550" height="130" rx="14" fill="#eefbf3" stroke="#15803d" stroke-width="2"/>\n<text x="682" y="145" font-family="Arial,sans-serif" font-size="22" font-weight="bold" fill="#122438">Finite canonical partition g in B_j</text>\n<text x="682" y="175" font-family="Arial,sans-serif" font-size="19" fill="#122438">sum g_i = 1; a_i = tau(g_i)</text>\n<text x="682" y="205" font-family="Arial,sans-serif" font-size="19" fill="#122438">D = sum |a_i - lambda_i| ≤ C_q^2 delta_j^2</text>\n<text x="682" y="228" font-family="Arial,sans-serif" font-size="17" fill="#122438">UFP.2; centers may vary with j</text>\n<path d="M600 177 L652 177" stroke="#334155" stroke-width="2.5" fill="none"/>\n<rect x="165" y="305" width="930" height="145" rx="14" fill="#eefbf3" stroke="#15803d" stroke-width="2"/>\n<text x="188" y="339" font-family="Arial,sans-serif" font-size="22" font-weight="bold" fill="#122438">Optimal physical redistribution, then separate actual tunnel placement</text>\n<text x="188" y="370" font-family="Arial,sans-serif" font-size="19" fill="#122438">tau(r_i) = a_i; sum r_i = 1; sum ||r_i - p_i||_2^2 = D</text>\n<text x="188" y="401" font-family="Arial,sans-serif" font-size="19" fill="#122438">u_i g_i u_i* = r_i; P* = direct sum of full supported A_j^(i) pairs</text>\n<text x="188" y="430" font-family="Arial,sans-serif" font-size="17" fill="#122438">UFP.3; E_N E_P* = E_P* E_N = E_Q*; A0 is retained</text>\n<path d="M326 242 L326 297" stroke="#334155" stroke-width="2.5" fill="none"/><path d="M936 242 L936 297" stroke="#334155" stroke-width="2.5" fill="none"/>\n<rect x="50" y="515" width="550" height="135" rx="14" fill="#eff6ff" stroke="#2563eb" stroke-width="2"/>\n<text x="72" y="549" font-family="Arial,sans-serif" font-size="22" font-weight="bold" fill="#122438">Support movement has a proved bound</text>\n<text x="72" y="580" font-family="Arial,sans-serif" font-size="19" fill="#122438">||D_r(x) - D_p(x)||_2 &lt;= 2 ||x|| sqrt(D)</text>\n<text x="72" y="610" font-family="Arial,sans-serif" font-size="19" fill="#122438">D can be made arbitrarily small.</text>\n<text x="72" y="637" font-family="Arial,sans-serif" font-size="17" fill="#122438">UFP.4 / (UFP.8); no number-of-cells factor</text>\n<rect x="660" y="515" width="550" height="135" rx="14" fill="#fff7ed" stroke="#b45309" stroke-width="2.5"/>\n<text x="682" y="549" font-family="Arial,sans-serif" font-size="22" font-weight="bold" fill="#122438">Actual operator-transfer input is still needed</text>\n<text x="682" y="580" font-family="Arial,sans-serif" font-size="19" fill="#122438">K^2 = sum_l ||(1 - E_P*) D_r(a_l)||_2^2</text>\n<text x="682" y="610" font-family="Arial,sans-serif" font-size="19" fill="#122438">Small D alone does not bound K.</text>\n<text x="682" y="637" font-family="Arial,sans-serif" font-size="17" fill="#122438">a_l: trace-orthonormal basis of P0; UFP.4</text>\n<path d="M326 450 L326 507" stroke="#334155" stroke-width="2.5" fill="none"/><path d="M936 450 L936 507" stroke="#334155" stroke-width="2.5" fill="none"/>\n<rect x="165" y="720" width="930" height="105" rx="14" fill="#eff6ff" stroke="#2563eb" stroke-width="2"/>\n<text x="188" y="754" font-family="Arial,sans-serif" font-size="22" font-weight="bold" fill="#122438">Exact target-error certificate</text>\n<text x="188" y="784" font-family="Arial,sans-serif" font-size="19" fill="#122438">D &lt; eps^2/(64 R^2), K &lt; eps/(4 R) imply final error &lt; eps</text>\n<text x="188" y="812" font-family="Arial,sans-serif" font-size="17" fill="#122438">UFP.4 / (UFP.10)-(UFP.13); R = max(1, max_y ||y||)</text>\n<path d="M326 650 L326 712" stroke="#334155" stroke-width="2.5" fill="none"/><path d="M936 650 L936 660 M936 669 L936 679 M936 688 L936 698 M936 707 L936 712" stroke="#b45309" stroke-width="3" fill="none"/>\n<rect x="50" y="867" width="1160" height="60" rx="10" fill="#f8fafc" stroke="#64748b"/>\n<text x="72" y="894" font-family="Arial,sans-serif" font-size="17" fill="#122438">Other established sufficient inputs: residual tau(f) in Gamma_plus (FP.2), or cheap actual overlap (FP.5).</text>\n<text x="72" y="918" font-family="Arial,sans-serif" font-size="17" fill="#122438">Amenability has not supplied these inputs here. Routine core changes preserve Z(S): UFP.5.</text>\n<text x="50" y="956" font-family="Arial,sans-serif" font-size="17" fill="#122438">Schematic only: no shape or area denotes a trace. Popa (1994), pp.209-210,220-222.</text>\n<text x="50" y="979" font-family="Arial,sans-serif" font-size="17" fill="#122438">Proof locators UFP.2-UFP.5 are exact; the dashed arrow marks the residual unproved implication.</text>\n<polygon points="652,177 643,171 643,183" fill="#334155"/>\n<polygon points="326,297 320,288 332,288" fill="#334155"/>\n<polygon points="936,297 930,288 942,288" fill="#334155"/>\n<polygon points="326,507 320,498 332,498" fill="#334155"/>\n<polygon points="936,507 930,498 942,498" fill="#334155"/>\n<polygon points="326,712 320,703 332,703" fill="#334155"/>\n<polygon points="936,712 930,703 942,703" fill="#b45309"/>\n</svg>'
Path(__file__).with_suffix(".svg").write_bytes(SVG.encode("utf-8"))

from fractions import Fraction
import cmath,math,itertools,json
constant_checks=0
for q in range(2,13):
    prefix=[2*5**i for i in range(q-1)]
    recurrence=sum(x*x for x in prefix)+sum(prefix)**2
    printed=Fraction(25**(q-1)-1,6)+Fraction(5**(q-1)-1,2)**2
    assert printed==recurrence
    constant_checks+=1
n=12
cases=[([10,1,1],[4,4,4]),([6,4,2],[2,4,6]),([3,3,3,3],[1,5,2,4]),([5,4,3],[5,4,3])]
def owners(counts):
    return [i for i,c in enumerate(counts) for _ in range(c)]
def redistribute(old_counts,new_counts):
    old=owners(old_counts);new=old[:];supply=[]
    for i,(p,a) in enumerate(zip(old_counts,new_counts)):
        if p>a:
            candidates=[k for k,o in enumerate(old) if o==i]
            supply.extend(candidates[:p-a])
    pos=0
    for i,(p,a) in enumerate(zip(old_counts,new_counts)):
        if a>p:
            for k in supply[pos:pos+a-p]:new[k]=i
            pos+=a-p
    assert pos==len(supply)
    assert [new.count(i) for i in range(len(new_counts))]==new_counts
    diffs=[Fraction(sum((o==i)!=(r==i) for o,r in zip(old,new)),n) for i in range(len(new_counts))]
    assert diffs==[Fraction(abs(p-a),n) for p,a in zip(old_counts,new_counts)]
    return old,new,sum(diffs)
def l2sq(x):return sum(abs(v)**2 for row in x for v in row)/n
def diff(x,y):return [[x[a][b]-y[a][b] for b in range(n)] for a in range(n)]
def pinch(x,o):return [[x[a][b] if o[a]==o[b] else 0 for b in range(n)] for a in range(n)]
def diagonal(x):return [[x[a][b] if a==b else 0 for b in range(n)] for a in range(n)]
operator_checks=0
for oc,nc in cases:
    old,new,D=redistribute(oc,nc)
    targets=[[[cmath.exp(2j*math.pi*a*b/n)/math.sqrt(n) for b in range(n)] for a in range(n)]]
    for a in range(n):
        for b in range(n):
            m=[[0j]*n for _ in range(n)];m[a][b]=1;targets.append(m)
    K2=sum(1 for a in range(n) for b in range(n) if a!=b and old[a]==old[b] and new[a]==new[b])
    for x in targets:
        # These targets have operator norm1. Their old pinching is a contraction.
        px=pinch(x,old);rx=pinch(x,new)
        assert l2sq(diff(rx,px))<=4*float(D)+1e-10
        b=px;c=pinch(b,new);expect=diagonal(c)
        eta2=l2sq(diff(c,expect));off2=l2sq(diff(b,c))
        assert abs(l2sq(diff(b,expect))-(off2+eta2))<1e-10
        assert off2<=4*float(D)+1e-10
        assert eta2<=l2sq(b)*K2+1e-10
        total=math.sqrt(l2sq(diff(x,diagonal(x))))
        old_error=math.sqrt(l2sq(diff(x,b)))
        assert total<=old_error+math.sqrt(4*float(D)+eta2)+1e-10
        operator_checks+=1
eps=Fraction(1,7);R=5
D_threshold=eps**2/(64*R**2);K2_threshold=eps**2/(16*R**2)
assert 4*R**2*D_threshold+R**2*K2_threshold==eps**2/8<eps**2/4
print(json.dumps({'passed':True,'constant_checks':constant_checks,'physical_partition_cases':len(cases),'operator_checks':operator_checks,'finite_matrix_dimension':n,'scope':'finite algebra identities only; no Jones counterexample or realization claim'}))
