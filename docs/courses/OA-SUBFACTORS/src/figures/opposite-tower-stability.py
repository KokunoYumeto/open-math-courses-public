"""CC0: reproducible opposite-tower diagram and exact finite tensor checks."""
from pathlib import Path
from html import escape
import argparse,json

def exact_checks():
 import numpy as np
 import sympy as s
 tests=[]
 for m in [1,2]:
  size=2**m; n=size*size
  def merge(a,b):
   aa=f'{a:0{m}b}';bb=f'{b:0{m}b}'
   return int(''.join(x+y for x,y in zip(aa,bb)),2)
  units={}
  for a in range(size):
   for b in range(size):
    x=np.zeros((n,n),dtype=np.int64)
    for t in range(size):x[merge(a,t),merge(b,t)]=1
    units[a,b]=x
    assert np.trace(x)==(size if a==b else 0)
  assert np.array_equal(sum(units[a,a] for a in range(size)),np.eye(n,dtype=np.int64))
  for a in range(size):
   for b in range(size):
    assert np.array_equal(units[a,b].T,units[b,a])
    for c in range(size):
     for d in range(size):
      assert np.array_equal(units[a,b]@units[c,d],units[a,d] if b==c else np.zeros((n,n),dtype=np.int64))
  tests.append(dict(binary_input_sites=m,matrix_unit_products=size**4,unital_star_map=True,normalized_trace_preserved=True))
 # Both physical cup conventions commute with the two common tensor legs.
 I=s.eye(2);E={(i,j):I[:,i]*I[:,j].T for i in range(2) for j in range(2)}
 first=s.Matrix([0,s.sqrt(3)/2,s.Rational(1,2),0]); second=s.Matrix([0,s.Rational(1,2),s.sqrt(3)/2,0])
 cups=[first*first.H,second*second.H]
 commutations=0
 for cup in cups:
  assert cup*cup==cup and s.trace(cup)==1
  x=s.kronecker_product(cup,I,I)
  for leg in [0,1]:
   for i in range(2):
    for j in range(2):
     y=s.kronecker_product(s.eye(4),E[i,j] if leg==0 else I,I if leg==0 else E[i,j])
     assert x*y==y*x;commutations+=1
 # The prescribed-matrix conjugacy formula, also in unequal central fibers.
 conjugacies=[]
 for n in [2,3]:
  size=2*n; ds={}
  for i in range(n):
   for j in range(n):
    x=np.zeros((n,n),dtype=np.int64);x[i,j]=1;ds[i,j]=np.kron(x,np.eye(2,dtype=np.int64))
  for shift in [1,2]:
   U=np.roll(np.eye(size,dtype=np.int64),shift,axis=0)
   cs={key:U@x@U.T for key,x in ds.items()};w=U@ds[0,0]
   V=sum(cs[i,0]@w@ds[0,i] for i in range(n))
   assert np.array_equal(V.T@V,np.eye(size,dtype=np.int64))
   assert all(np.array_equal(V@x@V.T,cs[key]) for key,x in ds.items())
  conjugacies.append(dict(matrix_size=n,independent_central_fibers=2,formula_unitary=True,all_matrix_units_conjugated=True))
 return dict(binary_maps=tests,original_and_corrected_cup_commutations=commutations,prescribed_matrix_conjugacies=conjugacies,all_tests_exact=True,infinite_normal_tower_and_nonfactor_trace_claims_use_written_proof=True)

def draw(path):
 out=['<svg xmlns="http://www.w3.org/2000/svg" width="1120" height="900" viewBox="0 0 1120 900">','<rect width="1120" height="900" fill="#fafbfc"/>','<defs><marker id="arrow" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="#315b76"/></marker></defs>']
 def text(x,y,t,size=22,color='#172d3d',weight='normal'):
  out.append(f'<text x="{x}" y="{y}" font-family="DejaVu Sans,Arial,sans-serif" font-size="{size}" fill="{color}" font-weight="{weight}">{escape(t)}</text>')
 def box(x,y,w,h,title,lines,color='#eaf3f8'):
  out.append(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="10" fill="{color}" stroke="#91aabb" stroke-width="2"/>');text(x+16,y+33,title,23,weight='bold')
  for k,l in enumerate(lines):text(x+16,y+65+29*k,l,20)
 def arrow(x1,y1,x2,y2):out.append(f'<path d="M{x1} {y1} L{x2} {y2}" fill="none" stroke="#315b76" stroke-width="2.5" marker-end="url(#arrow)"/>')
 text(30,42,'One common tensor factor in the actual upper opposite tower',28,weight='bold')
 text(30,79,'d = [M:N] > 1;  B_j = M_j′ ∩ T;  all traces are the inherited physical trace τ.',20)
 for x,label in [(30,'B₁'),(390,'B₀'),(750,'B₋₁')]:box(x,125,300,100,label,['= A_j ⊗ R₀ at stage j'])
 arrow(337,175,382,175);arrow(697,175,742,175)
 text(150,260,'E₀ : B₀ → B₁',20);text(640,260,'q₀ ∈ B₋₁;  Tr₀ = dτ',20)
 box(30,300,1020,125,'Split the binary sites, retaining a full copy in the complement',[
  'R₀ = R_even ⊗ R_odd;    H = R_odd ⊂ B₁;    θ : R₀ → R_even reindexes the sites.',
  'B_j⁰ = H′ ∩ B_j = A_j ⊗ R_even;     Ψ_j = id_{A_j} ⊗ θ, for every j ≤ 1.'])
 for x,label in [(30,'B₁⁰'),(390,'B₀⁰'),(750,'B₋₁⁰')]:box(x,480,300,100,label,['= A_j ⊗ R_even'])
 arrow(337,530,382,530);arrow(697,530,742,530)
 box(30,620,1020,119,'Both cup conventions and both expectations are retained',[
  'Ψ_{j−1}(e_j) = e_j;   Ψ_{j−1}(q_j) = q_j;   Ψ_j(h_j) = h_j, for j ≤ 0.',
  'q_j = h_j^(−1/2) e_j h_j^(−1/2);    F_j(x) = E_j(h_j^(1/2) x h_j^(1/2)).'])
 box(30,770,1020,98,'Any prescribed unital D ≅ Mat_n in B₁',[
  'One unitary in B₁ conjugates D into R₀; compatible maps give B_j ≅ D′ ∩ B_j.'], '#fff0e9')
 text(31,893,'Theorem 50.7 and (50.24)–(50.28). Subscripts decrease along the upper tower. Box widths encode no trace masses.',16)
 out.append('</svg>');path.write_text('\n'.join(out)+'\n',encoding='utf-8')
if __name__=='__main__':
 parser=argparse.ArgumentParser();parser.add_argument('--check',action='store_true');a=parser.parse_args()
 if a.check:print(json.dumps(exact_checks()))
 draw(Path(__file__).with_name('opposite-tower-stability.svg'))
