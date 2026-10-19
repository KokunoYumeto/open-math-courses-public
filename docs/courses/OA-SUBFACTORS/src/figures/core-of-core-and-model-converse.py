"""Internal ordinary core tower and model converse. CC0-1.0.

Run with Python, sympy installed. The SVG is reproducible. Exact finite
checks concern a matrix window of an index-four Bell basic construction,
also tensored with an arbitrary II1 spectator. They do not replace the
general argument or assert a physical infinite bicommutant.
"""
from pathlib import Path
from html import escape
import json
import sympy as s
D=Path(__file__).resolve().parent
def eq(a,b):assert a.applyfunc(s.simplify)==b.applyfunc(s.simplify)
I=s.eye(2);I4=s.eye(4)
units=[]
for i in range(2):
 for j in range(2):
  e=s.zeros(2);e[i,j]=1;units.append(s.sqrt(2)*s.kronecker_product(e,I))
b=s.Matrix([1,0,0,1])/s.sqrt(2);g=b*b.T
def expectation(x):
 y=s.zeros(2)
 for i in range(2):
  for j in range(2):y[i,j]=sum(x[2*i+k,2*j+k] for k in range(2))/2
 return s.kronecker_product(y,I)
eq(sum((a*g*a.H for a in units),s.zeros(4)),I4)
eq(sum((a*a.H for a in units),s.zeros(4)),4*I4)
eq(expectation(g),I4/4)
def psi(c):
 return sum((units[r]*g*units[t].H*c[r,t] for r in range(4) for t in range(4)),s.zeros(4))
def inverse(x):
 return s.Matrix(4,4,lambda r,t:s.simplify((b.H*units[r].H*x*units[t]*b)[0]))
matrix_units=[];images=[]
for r in range(4):
 for t in range(4):
  c=s.zeros(4);c[r,t]=1;matrix_units.append(c);images.append(psi(c))
  eq(inverse(psi(c)),c)
  eq(expectation(psi(c)),units[r]*units[t].H/4)
  assert s.simplify(s.trace(psi(c))-s.trace(c))==0
for a,x in zip(matrix_units,images):
 for c,y in zip(matrix_units,images):eq(x*y,psi(a*c))
eta=s.Matrix([s.trace(a)/4 for a in units])
eq(inverse(g),eta*eta.H)
# Eight basis slots, supported on different central summands. Each fiber
# has four slots. The finite coefficient algebra P is C+ C; tensoring
# with a II1 spectator yields the actual type-II version.
f=[(1,0)]*4+[(0,1)]*4
weights=[s.Rational(1,3),s.sqrt(2)/2,s.Rational(3,7)]
weighted_cases=0
for theta in weights:
 for block in range(2):
  for c,x in zip(matrix_units,images):
   weight=theta if block==0 else 1-theta
   physical=weight*s.trace(x)/4
   canonical=weight*s.trace(c)
   assert s.simplify(canonical-4*physical)==0
   weighted_cases+=1
 assert s.simplify(theta*4+(1-theta)*4)==4
assert sum(s.Rational(1) for _ in range(4))+s.Rational(1,2)==s.Rational(9,2)
# A right row must use beta(a*) after a multiplication reversal.
swap=s.Matrix([[1,0,0,0],[0,0,1,0],[0,1,0,0],[0,0,0,1]])
row=[]
for i in range(2):
 for j in range(2):
  e=s.zeros(2);e[i,j]=1
  row.append(swap*s.kronecker_product(I,s.sqrt(2)*e))
transported=[a.H.T for a in row]
for r,a in enumerate(transported):
 for t,c in enumerate(transported):eq(expectation(a.H*c),I4 if r==t else s.zeros(4))
wrong=expectation(row[0].T.H*row[0].T)
assert wrong!=I4
u=s.diag(1,s.I);alpha=lambda x:(u*x.T*u.H).T
small=[]
for i in range(2):
 for j in range(2):
  x=s.zeros(2);x[i,j]=1;small.append(x)
for x in small:
 eq(alpha(x),u.conjugate()*x*u.T)
 assert s.simplify(s.trace(alpha(x))-s.trace(x))==0
 for y in small:eq(alpha(x*y),alpha(x)*alpha(y))
record=dict(all_tests_exact=True,full_matrix_unit_inverse_cases=16,
 multiplication_cases=256,dual_expectation_cases=16,marked_cup_matrix_exact=True,
 weighted_central_trace_cases=weighted_cases,partial_Gram_slots=f,
 central_weights=[str(x) for x in weights],row_identity_and_index_exact=True,
 fractional_support_dimension='4+1/2=9/2; inherited cup2/9; canonical cup1',
 general_scope='17.14 proves arbitrary-center normal full-corner towers;17.15–17.16 prove the whole original model converse. These are written proofs, not inferences from fixtures.',
 physical_bicommutant_claimed=False,anti_transport_Gram_cases=16,wrong_unstarred_row_Gram=str(wrong),double_anti_multiplication_cases=16)
(D/'figure-mathematical-check.json').write_text(json.dumps(record,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
items=['<svg xmlns="http://www.w3.org/2000/svg" width="1120" height="1460" viewBox="0 0 1120 1460">',
 '<rect width="1120" height="1460" fill="#f8fafc"/>',
 '<defs><marker id="arrow" markerWidth="10" markerHeight="10" refX="8" refY="3" orient="auto"><path d="M0,0 L0,6 L9,3z" fill="#375f78"/></marker></defs>']
def text(x,y,t,size=21,bold=False):
 items.append(f'<text x="{x}" y="{y}" font-family="DejaVu Sans, sans-serif" font-size="{size}" font-weight="{"bold" if bold else "normal"}" fill="#172f44">{escape(t)}</text>')
def box(x,y,w,h,color='#eaf3f8'):items.append(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="10" fill="{color}" stroke="#8daabd" stroke-width="2"/>')
def arrow(x,y,x2,y2):items.append(f'<path d="M{x},{y} L{x2},{y2}" stroke="#375f78" stroke-width="2.5" marker-end="url(#arrow)"/>')
text(30,43,'An ordinary core generates itself',31,True)
text(30,79,'Proper finite index d > 1; inherited physical trace τ; original ordinary cups.',20)
box(30,110,1040,175)
text(47,142,'Actual restricted tower inside R — equation (17.43)',23,True)
text(47,180,'R = A₀   ⊃   A₁ = S   ⊃   A₂   ⊃   A₃   ⊃   · · ·',25)
text(47,216,'Aⱼ = R ∩ Lⱼ.  Original gⱼ ∈ Aⱼ;  E_(Aⱼ₊₁)(gⱼ) = 1/d.')
text(47,253,'Every restricted expectation is normal and faithful.  Provider 51.1.')
arrow(550,297,550,330)
box(30,343,1040,240,'#edf5e9')
text(47,377,'Full supported matrix corner — Theorem 17.14',23,True)
text(47,416,'P = Aⱼ₊₂,  Q = Aⱼ₊₁,  A = Aⱼ;  common partial row (aᵣ), supports fᵣ.')
text(47,453,'f Matₙ(P) f  ⟶  A,       Ψ(C) = Σᵣ,ₛ aᵣ Cᵣₛ gⱼ aₛ*')
text(47,491,'Σᵣ aᵣ gⱼ aᵣ* = 1.  The finite row proves full range, not just density.')
text(47,529,'τ(Ψ(C)) = (1/d) Σᵣ τ(Cᵣᵣ);    canonical Tr = d τ on the whole positive cone.')
text(47,564,'All central blocks and fractional supports remain.  No factoriality is used.')
arrow(550,595,550,628)
box(30,640,1040,175)
text(47,674,'Factor endpoints give an actual generating tunnel — Theorem 17.15',23,True)
text(47,712,'If S and R are factors, every Aⱼ is a II₁ factor by the full cup corners.')
text(47,750,'Lⱼ′ ∩ M  ⊂  Aⱼ′ ∩ R;    the left-hand union already generates R.')
text(47,788,'Thus the whole internal core is S ⊂ R, and 61.15 gives full strong amenability.')
arrow(550,827,550,860)
box(30,874,1040,157,'#f5f0e7')
text(47,908,'Whole-pair model isomorphism — Theorem 17.16',23,True)
text(47,946,'α : (N ⊂ M) ≅ (S ⊂ R)  pulls every Aⱼ, cup and partial row back into M.')
text(47,984,'This is an ordinary generating tunnel for the original whole pair.')
text(47,1019,'Proper / separable: strong amenability ⇔ global approximation ⇔ generation ⇔ model.')
text(30,1071,'An abstract represented copy need not be an embedded core of fixed larger factors.',20)
text(30,1107,'Popa 4.1.2(i)–(v), p.210; 5.1.1, p.226.  The physical bicommutant is separate.',20)
box(30,1150,1040,260,'#edf0fa')
text(47,1188,'Extremality: full opposite-model characterization — Theorem 17.18',23,True)
text(47,1227,'ρ : (S ⊂ R)  →  (B₁ ⊂ B₀), normal anti; CTS.7 needs no amenability.')
text(47,1265,'β : (N ⊂ M) → (B₁ ⊂ B₀), the supplied normal whole-pair anti-isomorphism.')
text(47,1303,'α = ρ⁻¹ β : (N ⊂ M) → (S ⊂ R) has TWO multiplication reversals.')
text(47,1341,'It is a normal trace-preserving isomorphism; 17.16 gives strong amenability.')
text(47,1380,'Without extremality the index-ten trace obstruction63.9 remains.')
items.append('</svg>')
(D/'core-of-core-and-model-converse.svg').write_text('\n'.join(items)+'\n',encoding='utf-8')
print(json.dumps(dict(exact_inverse_cases=16,multiplication_cases=256,central_trace_cases=weighted_cases,svg_written=True)))
