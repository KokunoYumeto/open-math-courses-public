"""CC0: exact downward expected-square fixtures and generating hypertrace diagram."""
from pathlib import Path
from html import escape
import argparse,json

def exact_checks():
 import sympy as s
 I=s.eye(2);E={(i,j):I[:,i]*I[:,j].T for i in range(2) for j in range(2)}
 bell=sum((s.kronecker_product(E[i,j],E[i,j]) for i in range(2) for j in range(2)),s.zeros(4))/2
 g=s.kronecker_product(bell,s.eye(4));e=s.kronecker_product(I,bell,I);f=s.kronecker_product(s.eye(4),bell);lam=s.Rational(1,4)
 for a,b in [(g,e),(e,g),(e,f),(f,e)]:assert a*b*a==lam*a
 assert g*f==f*g
 for a in E.values():
  u=s.kronecker_product(a,s.eye(8));T=f*e*g*u*g*e*f
  assert g*T==T*g==lam**2*g*u*g*f
 # An independent matrix spectator, retained by every downward expectation.
 G=s.kronecker_product(bell,I)
 def embed(a,b):return s.kronecker_product(a,I,b)
 def expected(X):
  return s.Matrix(4,4,lambda r,c:sum(X[(r//2*2+k)*2+r%2,(c//2*2+k)*2+c%2] for k in range(2))/2)
 def down(U):
  # Re-embed U (first leg and spectator) into the three-leg ambient.
  X=s.zeros(8)
  for i in range(2):
   for j in range(2):
    block=U[2*i:2*i+2,2*j:2*j+2];X+=embed(E[i,j],block)
  return 4*expected(G*X*G)
 basis=[s.sqrt(2)*s.kronecker_product(a,I) for a in E.values()]
 rows=0
 for a in E.values():
  for b in E.values():
   U=s.kronecker_product(a,b);want=s.trace(a)/2*s.kronecker_product(I,b)
   assert down(U)==want
   assert sum((x*down(x.H*U) for x in basis),s.zeros(4))==U
   assert G*embed(a,b)*G==s.kronecker_product(I,I,s.trace(a)/2*b)*G
   rows+=1
 for i,a in enumerate(basis):
  for j,b in enumerate(basis):assert down(a.H*b)==(s.eye(4) if i==j else s.zeros(4))
 assert sum((a*a.H for a in basis),s.zeros(4))==4*s.eye(4)
 # All matrix coefficients of the centrality identity, with noncommutative outputs.
 J=s.eye(4);F=[J[:,i]*J[:,j].T for i in range(4) for j in range(4)]
 central=0
 for p in F:
  for a in F:
   for b in E.values():
    left=s.trace(p*a)/4*b;right=s.trace(a*p)/4*b
    assert left==right;central+=1
 return dict(all_tests_exact=True,ordinary_Jones_relations=5,three_cup_commutation_cases=4,downward_expectation_and_full_row_cases=rows,partial_basis_gram_entries=16,noncommutative_coefficient_centrality_cases=central,scalar_index=4,singular_limit_and_general_smoothness='established by the full written proof, not inferred from finite matrix fixtures')

def draw(path):
 out=['<svg xmlns="http://www.w3.org/2000/svg" width="1120" height="1080" viewBox="0 0 1120 1080">','<title>From an actual generating tunnel to the full compatible hypertrace</title>','<rect width="1120" height="1080" fill="#fafbfc"/>','<defs><marker id="arr" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="#315b76"/></marker></defs>']
 def text(x,y,t,size=21,bold=False):
  out.append(f'<text x="{x}" y="{y}" font-family="DejaVu Sans,Arial,sans-serif" font-size="{size}" font-weight="{"bold" if bold else "normal"}" fill="#172d3d">{escape(t)}</text>')
 def box(x,y,w,h,title,lines,color='#eaf3f8'):
  out.append(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="10" fill="{color}" stroke="#91aabb" stroke-width="2"/>');text(x+16,y+33,title,22,True)
  for k,l in enumerate(lines):text(x+16,y+67+29*k,l,20)
 def arrow(x1,y1,x2,y2):out.append(f'<path d="M{x1} {y1} L{x2} {y2}" stroke="#315b76" stroke-width="2.5" marker-end="url(#arr)"/>')
 text(30,43,'A generating tunnel gives a compatible hypertrace',27,True)
 text(30,81,'N ⊂ M proper finite index;  U ⊂ᴱ V₀ arbitrary smooth expected representation.',21)
 box(30,112,1040,150,'Exact downward extension — Theorems 61.13–61.14',[
  'Uⱼ₊₁ = Uⱼ ∩ {gⱼ}′;      each step is normal, faithful, nondegenerate and smooth.',
  'One step:  E₋₁(u) = d E(gug);      gug = E₋₁(u)g;      every partial support is retained.',
  'Smoothness follows through the actual finite corner and w = λ⁻¹ᐟ²eg, not an infinite map.'])
 arrow(550,274,550,306)
 box(30,320,1040,158,'The original physical relative commutants',[
  'Pⱼ = Nⱼ′ ∩ M;      Φⱼ : V₀ → Uⱼ;      Φⱼ|M = E_Nⱼ;      [Pⱼ,Uⱼ] = 0.',
  'For p ∈ Pⱼ:  E_Nⱼ(pa) = E_Nⱼ(ap), by the original trace pairing.',
  'Finite common rows give Φⱼ(px) = Φⱼ(xp) for every x ∈ V₀.'],'#eef6eb')
 arrow(550,490,550,522)
 box(30,536,1040,137,'Normal compatible states at each depth — Theorem 61.15',[
  'ψⱼ is a normal state on Uⱼ extending τ_Nⱼ;      φⱼ = ψⱼ Φⱼ.',
  'φⱼ|M = τ;      φⱼE = φⱼ;      φⱼ centralizes the whole Pⱼ.'])
 arrow(550,685,550,717)
 box(30,731,1040,153,'The uniform physical return — equation (61.55)',[
  '|φⱼ(mx − xm)| ≤ 2 ‖x‖ ‖m − E_Pⱼ(m)‖₂,τ  → 0, for every fixed m ∈ M.',
  'Generation:  (⋃ Pⱼ)″ = M.      Take a cofinal cluster in σ(V₀*, V₀).',
  'The limit is M-central, restricts to τ and preserves E; it may be singular.'],'#f6f1e7')
 text(30,933,'Theorem 61.16: strong amenability ⇔ a generating ordinary tunnel',25,True)
 text(30,973,'Proper finite index and separable predual; no extremality or finite depth.',21)
 text(30,1011,'Forward implication: existing SA.7.  Converse: the full state construction above.',20)
 text(30,1048,'The separate physical bicommutant identity remains unproved here. Positions are schematic.',19)
 out.append('</svg>');Path(path).write_text('\n'.join(out)+'\n',encoding='utf-8')

if __name__=='__main__':
 p=argparse.ArgumentParser();p.add_argument('--svg',default=str(Path(__file__).with_suffix('.svg')));p.add_argument('--check-json');a=p.parse_args()
 checks=exact_checks();draw(a.svg)
 if a.check_json:Path(a.check_json).write_text(json.dumps(checks,indent=2)+'\n',encoding='utf-8')
 print(json.dumps(checks))
