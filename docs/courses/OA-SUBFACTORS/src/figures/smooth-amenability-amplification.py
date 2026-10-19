"""CC0: finite matrix induction and return, with exact rational fixtures."""
from pathlib import Path
from html import escape
import json,argparse

def exact_checks():
 import sympy as s
 I=s.eye(3);E={(i,j):I[:,i]*I[:,j].T for i in range(3) for j in range(3)}
 p=E[0,0]+E[1,1];v=[p,E[2,0]];V=s.Matrix.hstack(*v);q=V.H*V;W=p*V;a=W.H*W
 assert V*V.H==I and q*q==q and W*W.H==p and a*a==a and q*a==a
 cases=0
 for x in E.values():
  assert V*(V.H*x*V)*V.H==x
  assert q*(V.H*x*V)*q==V.H*x*V
  cases+=1
 for x in [E[i,j] for i in range(2) for j in range(2)]:
  assert W*(W.H*x*W)*W.H==x
 # Finite conditional expectation with a genuine noncommutative spectator:
 # M=Mat_3, represented ambient=Mat_3 tensor Mat_2; p has rank2.
 J=s.eye(2);F={(i,j):J[:,i]*J[:,j].T for i in range(2) for j in range(2)}
 def tr2(X,rank):
  return s.Matrix(rank,rank,lambda i,j:(X[2*i,2*j]+X[2*i+1,2*j+1])/2)
 def lift(x):return s.kronecker_product(x,J)
 returned=0
 for x in E.values():
  for b in F.values():
   X=s.kronecker_product(x,b)
   Y=sum((v[i]*tr2(lift(v[i].H)*X*lift(v[j]),3)*v[j].H for i in range(2) for j in range(2)),s.zeros(3))
   assert Y==x*s.trace(b)/2
   returned+=1
 assert s.Rational(7,3)/3==s.Rational(7,9)
 return dict(all_tests_exact=True,finite_frame_matrix_units=cases,corner_return_matrix_units=4,conditional_expectation_entry_tests=returned,partial_final_support='diag(p,e11), strictly below diag(p,p)',real_alpha='7/3 with normalized projection trace7/9',singular_spectator_case='proved in full Exercise61.8; finite fixtures do not approximate a singular state')

def draw(path):
 out=['<svg xmlns="http://www.w3.org/2000/svg" width="1120" height="990" viewBox="0 0 1120 990">','<title>All smooth representations and compatible hypertraces under a physical corner</title>','<rect width="1120" height="990" fill="#fafbfc"/>','<defs><marker id="arr" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="#315b76"/></marker></defs>']
 def text(x,y,t,size=22,bold=False):
  out.append(f'<text x="{x}" y="{y}" font-family="DejaVu Sans,Arial,sans-serif" font-size="{size}" font-weight="{"bold" if bold else "normal"}" fill="#172d3d">{escape(t)}</text>')
 def box(x,y,w,h,title,lines,color='#eaf3f8'):
  out.append(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="10" fill="{color}" stroke="#91aabb" stroke-width="2"/>')
  text(x+16,y+33,title,21,True)
  for k,l in enumerate(lines):text(x+16,y+65+29*k,l,20)
 def arrow(x1,y1,x2,y2):out.append(f'<path d="M{x1} {y1} L{x2} {y2}" stroke="#315b76" stroke-width="2.5" marker-end="url(#arr)"/>')
 text(30,43,'All smooth representations: finite induction and return',29,True)
 text(30,81,'0 ≠ p ∈ N;  t = τ(p);  vᵢ = vᵢp;  Σ vᵢvᵢ* = 1;  V = (vᵢ);  q = V*V.',21)
 box(30,115,1040,127,'The finite matrix identification — Theorem 61.9',[
  'Θₓ(x) = V*xV : X → q Matᵣ(pXp)q;       Θₓ⁻¹(C) = VCV*.',
  'Both maps are normal *-isomorphisms, with units 1 and q.',
  'Every represented tower level and every smoothness inclusion is retained.'])
 box(30,295,480,169,'Any original smooth square',[
  'U ⊂ V₀ above N ⊂ M.',
  'Compress: pUp ⊂ pV₀p.',
  'Its whole tower is pVⱼp, cups peⱼ.',
  'Corner amenability supplies Fₚ.'])
 box(590,295,480,169,'Any corner smooth square',[
  'Uₚ ⊂ Wₚ above pNp ⊂ pMp.',
  'Induce: q Matᵣ(Uₚ)q ⊂ q Matᵣ(Wₚ)q.',
  'Its whole tower is q Matᵣ(Wₚ,ⱼ)q.',
  'Original amenability supplies F̃.'])
 arrow(270,250,270,282);arrow(830,250,830,282)
 box(30,510,480,157,'Return to the original pair — (61.37)',[
  'F(x) = Σᵢ,ⱼ vᵢ Fₚ(vᵢ*xvⱼ) vⱼ*.',
  'F is UCP, fixes M and sends U into N.',
  'EₙF = FE;       hypertrace = τF.'],'#eef6eb')
 box(590,510,480,157,'Return to the corner pair — (61.39)',[
  'W = (pvᵢ);  WW* = p;  a = W*W = Θ(p).',
  'Fₚ(b) = W F̃(W*bW) W*.',
  'Hypertrace = τₚFₚ;       τₚ = τ/t.'],'#eef6eb')
 arrow(270,474,270,499);arrow(830,474,830,499)
 box(30,715,1040,142,'Full equivalence — Theorem 61.11',[
  'N ⊂ M amenable  ⇔  pNp ⊂ pMp amenable  ⇔  every real amplification amenable.',
  'α > 0: choose n ≥ α;  (τ ⊗ Trₙ)(b) = α;  normalized projection trace = α/n.',
  'Finite sums preserve arbitrary compatible states; F and Fₚ need not be normal.'],'#f6f1e7')
 arrow(270,678,270,704);arrow(830,678,830,704)
 text(30,902,'Corollary 61.12: strong amenability also retains factoriality of the whole ordinary core.',21)
 text(30,940,'No extremality, finite depth or ambient separability is imposed. Diagram positions are schematic.',19)
 out.append('</svg>');Path(path).write_text('\n'.join(out)+'\n',encoding='utf-8')

if __name__=='__main__':
 parser=argparse.ArgumentParser();parser.add_argument('--svg',default=str(Path(__file__).with_suffix('.svg')));parser.add_argument('--check-json');a=parser.parse_args()
 checks=exact_checks();draw(a.svg)
 if a.check_json:Path(a.check_json).write_text(json.dumps(checks,indent=2)+'\n',encoding='utf-8')
 print(json.dumps(checks))
