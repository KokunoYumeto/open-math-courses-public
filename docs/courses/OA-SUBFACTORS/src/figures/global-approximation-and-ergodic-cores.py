"""CC0: exact weighted projection matching, Jones pull-down and prefix bounds."""
from pathlib import Path
from html import escape
from fractions import Fraction
from math import isqrt
import json,argparse

def exact_checks():
 import sympy as s
 p2=s.diag(1,0);r2=s.eye(2);p3=s.diag(0,1,1);r3=s.diag(1,0,0);w3=s.Matrix([[0,1,0],[1,0,0],[0,0,1]])
 weights=[s.Rational(1,3),s.sqrt(2)/2,(s.sqrt(5)-1)/2];weighted=[]
 for theta in weights:
  distance=s.simplify(theta*s.trace((p2-r2)**2)/2+(1-theta)*s.trace((w3*p3*w3.H-r3)**2)/3)
  assert s.simplify(distance-(theta/2+(1-theta)/3))==0
  weighted.append(dict(theta=str(theta),squared_distance=str(distance)))
 I=s.eye(2);E={(i,j):I[:,i]*I[:,j].T for i in range(2) for j in range(2)}
 p=sum((s.kronecker_product(E[i,j],E[i,j]) for i in range(2) for j in range(2)),s.zeros(4))/2
 def EP(X):return s.kronecker_product(s.Matrix(2,2,lambda i,j:sum(X[2*i+k,2*j+k] for k in range(2))/2),I)
 def norm2(X):return s.simplify(s.trace(X.H*X)/4)
 large=[]
 for u in [s.Matrix([[0,1],[1,0]]),s.Matrix([[1,1],[1,-1]])/s.sqrt(2),s.diag(1,s.I)]:
  w=s.kronecker_product(u,I);q=w*p*w.H;x=4*EP(w*p)
  assert x==w and x*p==w*p and EP(q)==s.eye(4)/4
  assert x*p*x.H==q
  large.append(dict(unitary_squared_distance=str(norm2(x-s.eye(4))),finite_algebra_preserved=True,small_final_correction='identity'))
 c=s.Rational(99,101);t=s.Rational(20,101)
 # A unitary in Q whose pull-down is genuinely nonunitary, with positive polar part.
 w=s.eye(4);w[0,0]=c;w[0,3]=-t;w[3,0]=t;w[3,3]=c
 assert w*w.H==s.eye(4)
 x=4*EP(w*p);assert x==s.diag(c-t,c-t,c+t,c+t) and x*p==w*p
 a2=norm2(w*p*w.H-p);polar2=norm2(x-s.eye(4))
 assert s.simplify(a2-s.Rational(200,10201))==0
 assert s.simplify(polar2-s.Rational(4,101))==0 and polar2<=2*c*t
 # An exact small P-unitary return between distinct ordinary cups.
 v=s.kronecker_product(s.Matrix([[c,-t],[t,c]]),I);q=v*p*v.H
 z=v*p;u=4*EP(z)
 assert u==v and u*p*u.H==q and EP(q)==s.eye(4)/4
 assert norm2(u-s.eye(4))<=16*norm2(q-p)
 # Certified rational upper bounds for a finite error recursion; no floating point.
 def sqrt_upper(a,digits=1200):
  scale=10**digits;n=a.numerator*scale*scale;den=a.denominator;k=isqrt(n//den)
  if k*k*den<n:k+=1
  result=Fraction(k,scale);assert result*result>=a;return result
 initial=Fraction(1,10**1024);delta=initial
 for _ in range(3):
  a=2*delta+sqrt_upper(6*delta+2*initial);bound=4*(a+2*sqrt_upper(4*a));delta+=2*bound
 assert delta<Fraction(1,10**12)
 return dict(all_tests_exact=True,weighted_block_matching_cases=weighted,large_set_preserving_Jones_returns=large,nonunitary_pull_down_squared_error=str(a2),nonunitary_polar_squared_error=str(polar2),exact_small_unitary_return=True,finite_recursion=dict(index=4,prefix_length=3,initial_tolerance='10^(-1024)',final_certified_upper_bound='<10^(-12)',square_roots='rational upper enclosures, denominator10^1200'),general_nonseparable_cores_and_directed_states='proved in61.19–61.20; not inferred from matrix fixtures')

def draw(path):
 out=['<svg xmlns="http://www.w3.org/2000/svg" width="1120" height="1190" viewBox="0 0 1120 1190">','<title>Global finite approximation, exact ordinary prefixes and ergodic actual cores</title>','<rect width="1120" height="1190" fill="#fafbfc"/>','<defs><marker id="arr" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="#315b76"/></marker></defs>']
 def text(x,y,t,size=20,bold=False):
  out.append(f'<text x="{x}" y="{y}" font-family="DejaVu Sans,Arial,sans-serif" font-size="{size}" font-weight="{"bold" if bold else "normal"}" fill="#172d3d">{escape(t)}</text>')
 def box(x,y,w,h,title,lines,color='#eaf3f8'):
  out.append(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="10" fill="{color}" stroke="#91aabb" stroke-width="2"/>');text(x+16,y+32,title,21,True)
  for k,l in enumerate(lines):text(x+16,y+65+28*k,l,19)
 def arrow(x1,y1,x2,y2):out.append(f'<path d="M{x1} {y1} L{x2} {y2}" stroke="#315b76" stroke-width="2.5" marker-end="url(#arr)"/>')
 text(30,42,'Global approximation, exact prefixes and ergodic cores',29,True)
 text(30,80,'N ⊂ M proper finite index d; original physical trace τ; no ambient separability.',21)
 box(30,112,1040,120,'Original global finite-set condition (G) — equation (61.56)',[
  'For every finite Y ⊂ M and ε > 0, some actual ordinary finite tunnel has',
  'maxᵧ ‖y − E_(Nₘ′∩M)(y)‖₂,τ < ε.  The tunnel may depend on Y and ε.'])
 arrow(550,243,550,272)
 box(30,286,1040,199,'Two different unitary corrections — Lemma 61.17',[
  'Inside C = Nₘ′ ∩ Qᵢ:  match finite cup central traces, keeping every block weight.',
  'Pull down to v ∈ C ∩ Nᵢ:  v fixes Nₘ and preserves C and A = Nₘ′ ∩ M.',
  'Then u ∈ Nᵢ is small and makes the current ordinary cup exact.',
  '‖u − 1‖₂ ≤ B_d(Δᵢ,t);   Δ₀ = t;   Δᵢ₊₁ = Δᵢ + 2B_d(Δᵢ,t).',
  'Every fixed finite prefix is exact; its target error tends to zero as t → 0.'],'#eef6eb')
 text(46,513,'Q₀ = M; Qᵢ = Nᵢ₋₁ for i ≥ 1.  Physical targets stay fixed throughout.',19)
 arrow(300,528,300,557);arrow(820,528,820,557)
 box(30,571,500,234,'Countable actual-core construction',[
  'Aⱼ = Nₘⱼ′ ∩ M; retain all old matrix units.',
  'Approximate finite M-unitary averages',
  'inside the next Aⱼ₊₁, after the old prefix.',
  '‖E_Z(R)(x) − τ(x)1‖₂ ≤ 5 · 2⁻ʲ.',
  'R = (⋃ Aⱼ)″ has scalar center.',
  'It is an actual II₁ core: Theorem 61.19.'])
 box(570,571,500,234,'Directed all-smooth state construction',[
  'For every finite F ⊂ M and η > 0:',
  'φ_F,η|M = τ;     φ_F,η E = φ_F,η.',
  '|φ_F,η(mx − xm)| ≤ 2η ‖x‖ for m ∈ F.',
  'Use all finite F, with η decreasing.',
  'A cofinal state cluster may be singular.',
  'The original full M is retained: 61.20.'])
 arrow(300,817,300,846);arrow(820,817,820,846)
 box(30,860,1040,158,'Full original equivalence — Theorem 61.20',[
  'Original strong amenability  ⇔  relative amenability to one ergodic actual core',
  '⇔  global finite approximation (G)  ⇔  (G) after every prescribed ordinary prefix.',
  'Popa Theorem 4.1.2(i)–(iii), without separability; forward proofs SA.6 / 60.4 retained.'],'#f6f1e7')
 text(30,1060,'The countable core can be proper in nonseparable M; its construction does not generate all M.',20)
 text(30,1100,'Only finite cup-generated algebras are matched, with their exact inherited trace weights.',20)
 text(30,1140,'The separate physical infinite bicommutant remains unproved here. Positions are schematic.',19)
 out.append('</svg>');Path(path).write_text('\n'.join(out)+'\n',encoding='utf-8')

if __name__=='__main__':
 p=argparse.ArgumentParser();p.add_argument('--svg',default=str(Path(__file__).with_suffix('.svg')));p.add_argument('--check-json');a=p.parse_args()
 checks=exact_checks();draw(a.svg)
 if a.check_json:Path(a.check_json).write_text(json.dumps(checks,indent=2)+'\n',encoding='utf-8')
 print(json.dumps(checks))
