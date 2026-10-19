"""CC0: exact corner fixtures and a reproducible two-trace model diagram."""
from pathlib import Path
from html import escape
from fractions import Fraction
import argparse,json

def exact_checks():
 import sympy as s
 I2=s.eye(2);I3=s.eye(3);E={(i,j):I2[:,i]*I2[:,j].T for i in range(2) for j in range(2)}
 F={(i,j):I3[:,i]*I3[:,j].T for i in range(3) for j in range(3)}
 cup=sum((s.kronecker_product(E[i,j],E[i,j]) for i in range(2) for j in range(2)),s.zeros(4))/2
 assert cup*cup==cup
 tests=[]
 for rank in [1,2,3]:
  p=sum((F[i,i] for i in range(rank)),s.zeros(3));P=s.kronecker_product(I2,p);t=s.Rational(rank,3)
  if rank==1:vs=[F[i,0] for i in range(3)]
  elif rank==2:vs=[F[0,0]+F[1,1],F[2,0]]
  else:vs=[I3]
  assert len(vs)<=s.ceiling(1/t)
  assert sum((v*v.H for v in vs),s.zeros(3))==I3
  assert all(v*p==v for v in vs)
  for i in range(2):
   for j in range(2):
    b=s.kronecker_product(E[i,j],I3);pb=P*b
    inverse=sum((s.kronecker_product(I2,v)*pb*s.kronecker_product(I2,v.H) for v in vs),s.zeros(6))
    assert inverse==b and s.trace(pb)/6/t==s.trace(b)/6
  upperP=s.kronecker_product(s.eye(4),p);upperCup=s.kronecker_product(cup,I3)
  cp=upperP*upperCup
  assert cp*cp==cp and s.trace(cp)/12/t==s.Rational(1,4)
  tests.append(dict(projection_rank=rank,projection_normalized_trace=str(t),frame_length=len(vs),all_four_commutant_matrix_units_recovered=True,normalized_traces_preserved=True,corner_cup_normalized_trace='1/4',canonical_cup_trace=1))
 lists=[[Fraction(2,5),Fraction(1,5),Fraction(2,5)],[Fraction(1,4),Fraction(1,2),Fraction(1,4)]]
 for values in lists:
  for t in [Fraction(1,3),Fraction(2,3),Fraction(7,9)]:assert [(t*x)/t for x in values]==values
 assert Fraction(7,3)/3==Fraction(7,9)
 return dict(finite_corner_tests=tests,distinct_existing_PG_trace_lists_preserved=True,real_amplification_normalization_checked='alpha=7/3, n=3, normalized projection trace7/9',all_tests_exact=True,irrational_projection_and_infinite_normal_claims_use_written_proof=True)

def draw(path):
 out=['<svg xmlns="http://www.w3.org/2000/svg" width="1120" height="990" viewBox="0 0 1120 990">','<rect width="1120" height="990" fill="#fafbfc"/>','<defs><marker id="arrow" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="#315b76"/></marker></defs>']
 def text(x,y,t,size=22,weight='normal'):
  out.append(f'<text x="{x}" y="{y}" font-family="DejaVu Sans,Arial,sans-serif" font-size="{size}" fill="#172d3d" font-weight="{weight}">{escape(t)}</text>')
 def box(x,y,w,h,title,lines,color='#eaf3f8'):
  out.append(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="10" fill="{color}" stroke="#91aabb" stroke-width="2"/>');text(x+16,y+34,title,23,'bold')
  for k,l in enumerate(lines):text(x+16,y+68+29*k,l,20)
 def arrow(x1,y1,x2,y2):out.append(f'<path d="M{x1} {y1} L{x2} {y2}" fill="none" stroke="#315b76" stroke-width="2.5" marker-end="url(#arrow)"/>')
 text(30,43,'Physical amplification preserves both separately traced models',28,'bold')
 text(30,81,'0 ≠ p ∈ N;   t = τ(p);   τᵖ = τ/t on pTp.   No ambient separability is assumed.',20)
 box(30,120,1020,132,'The actual corner tower and its marked finite rows',[
  'pNp ⊂ pMp ⊂ pM₁p ⊂ ⋯;     e_jᵖ = pe_j;     each index is d = [M:N].',
  'φ(b) = pb;   φ⁻¹(c) = Σ v_r c v_r*;   v_r ∈ N,   v_r = v_rp,   Σ v_rv_r* = 1.',
  'τᵖ(pb) = τ(b) for every b in the relevant relative commutant.'])
 box(30,315,480,209,'Ordinary standard model',[
  'Both finite rows and every marked cup',
  'determine the recovered downward trace ρ.',
  'ρ_kᵖ(pc) = ρ_k(c), by the finite mirror.',
  'Theorem 17.9 extends the comparison',
  'normally to both ordinary-core endpoints.'])
 box(570,315,480,209,'Actual physical opposite model',[
  'B_i = M_i′ ∩ T,  for every i ≥ −1.',
  'B_iᵖ = (pM_i p)′ ∩ pTp = pB_i.',
  'The map φ_i(b) = pb preserves σ.',
  'e_jᵖ = pe_j;  h_jᵖ = ph_j;  q_jᵖ = pq_j.',
  'Canonical trace: dτ maps to dτᵖ.'])
 arrow(250,260,250,303);arrow(810,260,810,303)
 box(30,578,1020,130,'Every positive real amplification α',[
  'Choose integer n ≥ α and p ∈ N ⊗ Mat_n with (τ ⊗ Tr_n)(p) = α.',
  'The normalized projection trace is (τ ⊗ tr_n)(p) = α/n.',
  'First amplify the physical tower by Mat_n, then apply the exact corner maps.'])
 box(30,758,1020,151,'Physical bicommutant equality transfers in both directions',[
  'D = (M′ ∩ T)′ ∩ T contains M;     (B₀ᵖ)′ ∩ pTp = pDp.',
  'If pDp = pMp, then x = Σ v_r(v_r* x v_s)v_s* ∈ M for every x ∈ D.',
  'This is amplification invariance of the equality, not a proof that D = M.'], '#fff0e9')
 text(32,951,'Theorems 17.11–17.12; Corollary 17.13. The two trace systems are not identified.',19)
 text(32,980,'No old negative tunnel is silently compressed. Boxes and arrows are schematic; widths encode no trace masses.',16)
 out.append('</svg>');path.write_text('\n'.join(out)+'\n',encoding='utf-8')
if __name__=='__main__':
 parser=argparse.ArgumentParser();parser.add_argument('--check',action='store_true');a=parser.parse_args()
 if a.check:print(json.dumps(exact_checks()))
 draw(Path(__file__).with_name('amplification-and-model-traces.svg'))
