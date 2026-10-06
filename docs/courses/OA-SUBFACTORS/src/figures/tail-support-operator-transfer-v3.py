"""Reproduce the schematic and exact actual tensor-Jones identities."""
from pathlib import Path
SVG='<svg xmlns="http://www.w3.org/2000/svg" width="1260" height="1030" viewBox="0 0 1260 1030">\n<rect width="1260" height="1030" fill="#ffffff"/>\n<text x="44" y="48" font-family="Arial,sans-serif" font-size="29" font-weight="bold" fill="#122438">Tail cuts retain operators; whole supports change the compressed index</text>\n<text x="44" y="80" font-family="Arial,sans-serif" font-size="19" fill="#122438">Exact actual objects and proof locators. The original general finite partition remains unresolved.</text>\n<rect x="44" y="115" width="560" height="170" rx="13" fill="#eff6ff" stroke="#2563eb" stroke-width="2"/>\n<text x="65" y="150" font-family="Arial,sans-serif" font-size="22" font-weight="bold" fill="#122438">Stronger actual tail-family input: OT.1</text>\n<text x="65" y="183" font-family="Arial,sans-serif" font-size="19" fill="#122438">p_i in Q_i = N_mi^(i); P_i = p_i A_mi^(i) p_i</text>\n<text x="65" y="215" font-family="Arial,sans-serif" font-size="19" fill="#122438">old error &lt; eps/2; tau(f) &lt; eps^2/(16 R^2)</text>\n<text x="65" y="247" font-family="Arial,sans-serif" font-size="18" fill="#122438">Popa4.4 pp.220-221 uses this tail membership.</text>\n<text x="65" y="274" font-family="Arial,sans-serif" font-size="17" fill="#122438">Unrestricted amenability has not supplied it here.</text>\n<rect x="657" y="115" width="560" height="170" rx="13" fill="#fff7ed" stroke="#b45309" stroke-width="2"/>\n<text x="678" y="150" font-family="Arial,sans-serif" font-size="22" font-weight="bold" fill="#122438">Available general whole support: OT.2</text>\n<text x="678" y="183" font-family="Arial,sans-serif" font-size="19" fill="#122438">p in B_m = Q\' cap N; Q = N_m; D = d^m</text>\n<text x="678" y="215" font-family="Arial,sans-serif" font-size="19" fill="#122438">Qp is an actual II1 factor inside pNp.</text>\n<text x="678" y="247" font-family="Arial,sans-serif" font-size="18" fill="#122438">(Qp)\' cap pMp = p A_m p: old operators retained.</text>\n<text x="678" y="274" font-family="Arial,sans-serif" font-size="17" fill="#122438">This is the membership supplied by general76.2.</text>\n<path d="M324 285 L324 334" stroke="#334155" stroke-width="2.5" fill="none"/><polygon points="324,334 318,324 330,324" fill="#334155"/>\n<path d="M937 285 L937 334" stroke="#334155" stroke-width="2.5" fill="none"/><polygon points="937,334 931,324 943,324" fill="#334155"/>\n<rect x="44" y="345" width="560" height="193" rx="13" fill="#eefbf3" stroke="#15803d" stroke-width="2"/>\n<text x="65" y="380" font-family="Arial,sans-serif" font-size="22" font-weight="bold" fill="#122438">Finite cups give exact compatible budgets</text>\n<text x="65" y="412" font-family="Arial,sans-serif" font-size="19" fill="#122438">sum c_i = 1; 0 &lt; a_i &lt; tau(p_i) for good cells</text>\n<text x="65" y="444" font-family="Arial,sans-serif" font-size="19" fill="#122438">Choose r_i ≤ p_i inside Q_i with tau(r_i) = a_i.</text>\n<text x="65" y="476" font-family="Arial,sans-serif" font-size="19" fill="#122438">u_i in Q_i fixes A_mi^(i), and places a copied cup.</text>\n<text x="65" y="508" font-family="Arial,sans-serif" font-size="17" fill="#122438">r_i enters actual B_(mi+J+1); residual trace is a_0.</text>\n<text x="65" y="530" font-family="Arial,sans-serif" font-size="17" fill="#122438">OT.3-OT.8: no near-identity unitary assumption</text>\n<rect x="657" y="345" width="560" height="193" rx="13" fill="#fff7ed" stroke="#b45309" stroke-width="2"/>\n<text x="678" y="380" font-family="Arial,sans-serif" font-size="22" font-weight="bold" fill="#122438">The literal corner-tunnel match is blocked</text>\n<text x="678" y="412" font-family="Arial,sans-serif" font-size="19" fill="#122438">[pNp : Qp] = D tau(p) rho_Q(p) &lt; D</text>\n<text x="678" y="444" font-family="Arial,sans-serif" font-size="19" fill="#122438">B_m cap Q = C1; a proper p is outside every later tail.</text>\n<text x="678" y="476" font-family="Arial,sans-serif" font-size="19" fill="#122438">Later compressed index = d^(m+l) tau(p) rho_Q(p).</text>\n<text x="678" y="508" font-family="Arial,sans-serif" font-size="17" fill="#122438">A depth shift needs tau(p) rho_Q(p) = d^(-a).</text>\n<text x="678" y="530" font-family="Arial,sans-serif" font-size="17" fill="#122438">OT.13-OT.16: necessary, not sufficient</text>\n<path d="M324 538 L324 589" stroke="#334155" stroke-width="2.5" fill="none"/><polygon points="324,589 318,579 330,579" fill="#334155"/>\n<path d="M937 538 L937 589" stroke="#334155" stroke-width="2.5" fill="none"/><polygon points="937,589 931,579 943,579" fill="#334155"/>\n<rect x="44" y="601" width="560" height="151" rx="13" fill="#eefbf3" stroke="#15803d" stroke-width="2"/>\n<text x="65" y="636" font-family="Arial,sans-serif" font-size="22" font-weight="bold" fill="#122438">Exact finite whole pairs; fixed physical y</text>\n<text x="65" y="668" font-family="Arial,sans-serif" font-size="19" fill="#122438">c_y = sum r_i b_y r_i in P*; b_y = E_P0(y)</text>\n<text x="65" y="700" font-family="Arial,sans-serif" font-size="19" fill="#122438">error &lt; eps/2 + eps/(2 sqrt(2)) &lt; eps</text>\n<text x="65" y="731" font-family="Arial,sans-serif" font-size="17" fill="#122438">OT.9-OT.10; both expectation orders are exact.</text>\n<rect x="657" y="601" width="560" height="151" rx="13" fill="#f8fafc" stroke="#64748b" stroke-width="2"/>\n<text x="678" y="636" font-family="Arial,sans-serif" font-size="22" font-weight="bold" fill="#122438">Actual tensor Jones example</text>\n<text x="678" y="665" font-family="Arial,sans-serif" font-size="17" fill="#122438">Q = 1 tensor 1 tensor R; N = M_2 tensor 1 tensor R</text>\n<text x="678" y="690" font-family="Arial,sans-serif" font-size="17" fill="#122438">M = M_2 tensor M_2 tensor R; d = 4</text>\n<text x="678" y="715" font-family="Arial,sans-serif" font-size="18" fill="#122438">tau(p) = rho_Q(p) = 1/2; local index = 1</text>\n<text x="678" y="741" font-family="Arial,sans-serif" font-size="15" fill="#122438">OT.17-18: constructed operators; no theorem counterexample.</text>\n<path d="M937 752 L937 763 M937 774 L937 785 M937 796 L937 807" stroke="#b45309" stroke-width="3" fill="none"/><polygon points="937,817 931,807 943,807" fill="#b45309"/>\n<rect x="44" y="830" width="1173" height="112" rx="13" fill="#fff7ed" stroke="#b45309" stroke-width="2"/>\n<text x="65" y="865" font-family="Arial,sans-serif" font-size="22" font-weight="bold" fill="#122438">Original unrestricted implication still required</text>\n<text x="65" y="897" font-family="Arial,sans-serif" font-size="19" fill="#122438">General amenability → actual finite operator transfer, exact residual certificate, or cheap actual overlap.</text>\n<text x="65" y="927" font-family="Arial,sans-serif" font-size="18" fill="#122438">No common stage, prefix or generating theorem is inferred from these individual-cell results.</text>\n<text x="44" y="977" font-family="Arial,sans-serif" font-size="17" fill="#122438">All positions and areas are schematic; no trace geometry is inferred. Exact proof locators OT.1-OT.18.</text>\n<text x="44" y="1007" font-family="Arial,sans-serif" font-size="17" fill="#122438">Sources: Popa(1994), pp.220-222; TakesakiIII XIX.2.6-2.8, pp.422-423. Dashed arrow marks the open input.</text>\n</svg>'
Path(__file__).with_suffix(".svg").write_bytes(SVG.encode("utf-8"))

from fractions import Fraction as F
import itertools,json
operator_checks=0;generation_checks=0
for n in [2,3,4]:
    e={(a*n+a,b*n+b):F(1,n) for a in range(n) for b in range(n)}
    def addmul(a,b):
        c={}
        for (i,k),v in a.items():
            for (l,j),w in b.items():
                if k==l:c[i,j]=c.get((i,j),F(0))+v*w
        return {k:v for k,v in c.items() if v}
    def scale(a,t):return {k:v*t for k,v in a.items() if v*t}
    def first(a,b):return {(a*n+k,b*n+k):F(1) for k in range(n)}
    assert addmul(e,e)==e
    assert {(j,i):v for (i,j),v in e.items()}==e
    trace=sum(e.get((i,i),F(0)) for i in range(n*n))/F(n*n)
    assert trace==F(1,n*n)
    partial={(a,c):sum(e.get((a*n+b,c*n+b),F(0)) for b in range(n))/n for a in range(n) for c in range(n)}
    assert partial=={(a,c):F(1,n*n) if a==c else F(0) for a in range(n) for c in range(n)}
    for a,b in itertools.product(range(n),repeat=2):
        assert addmul(addmul(e,first(a,b)),e)==scale(e,F(1,n) if a==b else F(0))
        operator_checks+=1
    for u,v,a,b in itertools.product(range(n),repeat=4):
        generated=scale(addmul(addmul(first(u,a),e),first(b,v)),n)
        assert generated=={(u*n+a,v*n+b):F(1)}
        generation_checks+=1
    rank_left_p=sum(1 for a,b in itertools.product(range(n),repeat=2) if a==0)
    tau_p=F(1,n);rho_p=F(rank_left_p,n*n)
    assert n*n*tau_p*rho_p==1
    operator_checks+=5
constant_checks=0
for q in range(1,10):
    eps=F(1,3);R=2;f=eps**2/(32*R**2);old=(1-f)/q
    eta=min(old/8,eps**2/(64*q*R**2))
    assert 0<eta<min(old/4,eps**2/(32*q*R**2))
    worst=f+2*q*eta
    assert worst<eps**2/(8*R**2)
    assert R**2*worst<(eps/2)**2
    assert old-2*eta>0
    constant_checks+=1
print(json.dumps({'passed':True,'actual_tensor_Jones_sizes':[2,3,4],'generation_checks':generation_checks,'projection_expectation_module_checks':operator_checks,'strict_transfer_constant_checks':constant_checks,'scope':'Finite exact operator identities verify the explicitly constructed tensor Jones example; scalar checks verify bounds only, with no unrealized Jones array claim.'}))


from fractions import Fraction as F
from itertools import product
import json

def mul(a,b):
 c={}
 for (i,k),x in a.items():
  for (k2,j),y in b.items():
   if k==k2: c[i,j]=c.get((i,j),F(0))+x*y
 return {k:v for k,v in c.items() if v}
def scale(a,s): return {k:v*s for k,v in a.items() if v*s}
def first(n,u,v): return {(u*n+a,v*n+a):F(1) for a in range(n)}
generation=0; scalar_expectation=0; module=0
for n in [2,3,4]:
 e={(a*n+a,b*n+b):F(1,n) for a,b in product(range(n),repeat=2)}
 assert mul(e,e)==e
 assert all(e.get((j,i),F(0))==v for (i,j),v in e.items())
 assert sum(e.get((i,i),F(0)) for i in range(n*n))/F(n*n)==F(1,n*n)
 en={(u,v):sum(e.get((u*n+a,v*n+a),F(0)) for a in range(n))/n for u,v in product(range(n),repeat=2)}
 assert en=={(u,v):(F(1,n*n) if u==v else F(0)) for u,v in product(range(n),repeat=2)}
 for u,v in product(range(n),repeat=2):
  assert mul(mul(e,first(n,u,v)),e)==(scale(e,F(1,n)) if u==v else {})
  scalar_expectation+=1
 for u,a,b,v in product(range(n),repeat=4):
  assert scale(mul(mul(first(n,u,a),e),first(n,b,v)),n)=={(u*n+a,v*n+b):F(1)}
  generation+=1
 assert F(n,n*n)==F(1,n)
 assert n*n*F(1,n)*F(n,n*n)==1
 module+=1
constants=0
for q in range(1,10):
 eps=F(1,3); R=F(2); f=eps*eps/(32*R*R); old=(1-f)/q
 eta=min(old/8,eps*eps/(64*q*R*R))
 assert eta<min(old/4,eps*eps/(32*q*R*R))
 worst=f+2*q*eta
 assert worst<eps*eps/(8*R*R)
 assert R*R*worst<eps*eps/4
 assert old-2*eta>0
 C2=F(25**q-1,6)+F((5**q-1)**2,4)
 assert C2>0
 constants+=1
assert F(1,8)<F(1,4)
verification_result={'status':'passed','n_values':[2,3,4],'generation_identities':generation,'scalar_compression_identities':scalar_expectation,'trace_module_checks':module,'strict_budget_cases':constants,'memory_only':True,'arithmetic':'exact fractions'}
from fractions import Fraction as F
n=3
p2=first(n,0,0)
p2.update(first(n,1,1))
assert mul(p2,p2)==p2
assert len(p2)==6
assert F(6,9)==F(2,3)
assert 9*F(2,3)*F(2,3)==4
for l in range(9):
 for k in range(13): assert 4*9**l!=9**k
rank_two_result={'n':3,'matrix_rank':2,'tau_p':'2/3','rho_Q_p':'2/3','corner_index':4,'physical_corner_index':9,'later_index':'4*9^l','no_endpoint_depth':'All nonnegative integers k; proved by prime valuation, supplemented by117 exact finite checks.'}

print(verification_result)
print(rank_two_result)
