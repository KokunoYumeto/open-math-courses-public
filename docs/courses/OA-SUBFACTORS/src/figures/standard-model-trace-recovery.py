"""CC0. Finite trace recovery, exact PG cup checks, and reproducible SVG.

The tests use the existing actual PG1–PG14 index-ten balanced-word model.
They do not construct a new counterexample or supply the general proof.
"""
from fractions import Fraction as F
from pathlib import Path
from itertools import product
from math import isqrt
from html import escape
import json

# Exact Q(sqrt(2)): (a,b) means a+b sqrt(2).
ZERO=(F(0),F(0));ONE=(F(1),F(0))
def qa(x,y):return (x[0]+y[0],x[1]+y[1])
def qm(x,y):return (x[0]*y[0]+2*x[1]*y[1],x[0]*y[1]+x[1]*y[0])
def qs(c,x):return (c*x[0],c*x[1])
def root(x):
 for s in [1,2]:
  v=x/s;a,b=isqrt(v.numerator),isqrt(v.denominator)
  if a*a==v.numerator and b*b==v.denominator:return (F(a,b),F(0)) if s==1 else (F(0),F(a,b))
 raise AssertionError(x)
odd=(F(1,4),F(1,2),F(1,4));even=(F(2,5),F(1,5),F(2,5));d=10
weight=lambda j:odd if j%2 else even
def word_weight(w,start=1):
 a=F(1)
 for j,i in enumerate(w,start):a*=weight(j)[i]
 return a
def cup_word(r,i):
 if not r:return F(1),[i]
 scalar=F(d**(2**(r-1)));out=[]
 for k in [2*i,2*i-1,2*i+1,2*i]:
  a,b=cup_word(r-1,k);scalar*=a;out+=b
 return scalar,out
def apply_cup(v,j):
 out={};wts=weight(j)
 for w,c in v.items():
  old=w[j-1]
  if old!=w[j]:continue
  for a in range(3):
   z=w[:j-1]+(a,a)+w[j+1:];term=qm(c,root(wts[a]*wts[old]));out[z]=qa(out.get(z,ZERO),term)
 return {w:c for w,c in out.items() if c!=ZERO}
def apply_block(r,w):
 scalar,ops=cup_word(r,1);v={w:ONE}
 for j in reversed(ops):v=apply_cup(v,j)
 return {w:qs(scalar,c) for w,c in v.items() if c!=ZERO}
def expected_column(k,w):
 first=w[:k]
 if w[k:]!=first[::-1]:return {}
 a=word_weight(first)
 return {v+v[::-1]:root(word_weight(v)*a) for v in product(range(3),repeat=k)}
identity=(0,1,2)
def pmul(a,b):return tuple(a[b[i]] for i in range(3))
def charge(w):
 p=identity;n=0
 for j,i in enumerate(w,1):
  if i==1:p=pmul(p,(1,0,2));n+=-1 if j%2 else 1
  elif i==2:p=pmul(p,(0,2,1))
 return p,n
reports=[]
for r in [0,1,2]:
 k=2**r;words=list(product(range(3),repeat=k))
 inputs=list(product(range(3),repeat=2*k)) if k<=2 else [w+w[::-1] for w in words]
 if k==4:
  inputs+=list(w for w in product(range(3),repeat=8) if w[4:]!=w[:4][::-1])[:32]
 for w in inputs:assert apply_block(r,w)==expected_column(k,w),(k,w)
 assert sum(word_weight(w) for w in words)==1
 recovered={w:word_weight(w[::-1],k+1) for w in words}
 assert sum(recovered.values())==1
 assert all(word_weight(w)*recovered[w]==F(1,d**k) for w in words)
 units=0
 for a in words:
  for b in words:
   if charge(a)==charge(b):
    # For E_ab, the equation between first and reversed second half is
    # exactly equality of these rank-one coefficients on every input.
    assert word_weight(a)==word_weight(b)
    for c in words[:9]:assert root(word_weight(a)*word_weight(c))==root(word_weight(b)*word_weight(c))
    units+=1
 reports.append(dict(K=k,original_cup_word_length=len(cup_word(r,1)[1]),original_cup_word_scalar=str(cup_word(r,1)[0]),cup_columns_checked=len(inputs),all_cup_columns_checked=(k<=2),balanced_matrix_units_checked=units,physical_cup_trace=str(F(1,d**k)),recovered_trace_normalization='1'))
assert reports[0]['original_cup_word_scalar']=='1' and reports[1]['original_cup_word_scalar']=='10' and reports[2]['original_cup_word_scalar']=='1000000'
assert sum(odd)==sum(even)==1
assert all(a*b==F(1,10) for a,b in zip(odd,even))

out=[]
def put(s):out.append(s)
def rect(x,y,w,h,fill,stroke='#9aafbd',r=12):put(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{r}" fill="{fill}" stroke="{stroke}"/>')
def text(x,y,s,size=22,bold=False,anchor='start',fill='#142c42'):put(f'<text x="{x}" y="{y}" font-size="{size}" font-weight="{"bold" if bold else "normal"}" text-anchor="{anchor}" fill="{fill}">{escape(s)}</text>')
def arrow(x1,y1,x2,y2):put(f'<path d="M{x1},{y1} L{x2},{y2}" stroke="#3a607b" stroke-width="2.5" fill="none" marker-end="url(#arrow)"/>')
put('<svg xmlns="http://www.w3.org/2000/svg" width="1000" height="1120" viewBox="0 0 1000 1120" role="img" aria-labelledby="title desc"><title id="title">Finite trace recovery reconstructs the ordinary standard model</title><desc id="desc">A finite skipped-cup equation recovers the downward trace from the marked upward ladder. The recovered trace and the physical opposite trace give different completions. The index-ten PG example displays their exact first-level weights.</desc><defs><marker id="arrow" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse"><path d="M0,0 L10,5 L0,10z" fill="#3a607b"/></marker></defs><rect width="1000" height="1120" fill="white"/><g font-family="Arial, DejaVu Sans, sans-serif">')
text(38,43,'The marked invariant recovers the downward trace',29,True)
text(38,78,'Finite index; every finite stage; no extremality or finite-depth assumption.',21)
rect(28,104,944,235,'#eef5fc')
text(52,144,'Finite data in A₂K, with dyadic K ≥ k (17.20)–(17.23)',24,True)
text(52,188,'b ∈ Bₖ ⊂ B_K;    G_K = B₂K ∩ {e₀,…,e_K₋₁}′',24)
text(52,231,'Unique η_K(b) ∈ G_K:     η_K(b) F_K = b F_K',25,True)
text(52,274,'Recovered trace:     tₖ(b) = σ₂K(η_K(b))',25,True)
text(52,314,'F₁ = e₁;    F₂ = d e₂ e₁ e₃ e₂;    τ(F_K) = d⁻ᴷ.',22)
rect(28,362,944,234,'#edf7f3')
text(52,402,'Whole ordinary-core reconstruction (17.25)–(17.27)',24,True)
text(64,450,'(B_algᵒᵖ, t)',25,True);arrow(270,442,375,442);text(397,450,'Rʳᵉᶜ',26,True);arrow(525,442,630,442);text(650,450,'ordinary core R',25,True)
text(52,491,'The smaller row is Cₖ = Bₖ ∩ {e₀}′; the same maps carry S.',22)
text(52,532,'SA.7: strong amenability + separable predual give the core-pair isomorphism to N ⊂ M.',19)
text(52,573,'Compare two recovered models to classify the original proper pairs.',22)
rect(28,619,944,406,'#fff5e9')
text(52,659,'Both traces stay explicit: the existing actual PG model',24,True)
text(80,704,'Given upward σ₁ on B₁',23,True)
text(557,704,'Recovered downward t₁',23,True)
baseline=918
for origin,vals,color in [(80,odd,'#287db1'),(557,even,'#248773')]:
 for i,t in enumerate(vals):
  x=origin+100*i;h=float(300*t);rect(x,baseline-h,65,h,color,color,0);text(x+32.5,baseline-h-10,str(t),20,True,'middle');text(x+32.5,949,'b'+str(i),19,anchor='middle')
 put(f'<path d="M{origin-10},{baseline} H{origin+285}" stroke="#98a8b5" stroke-width="1.5"/>')
text(52,991,'Bar heights = 300 px per trace unit. Both triples sum to 1.',21)
text(38,1060,'Completing B_alg with σ gives the physical opposite model; (17.26) uses t.',21)
text(38,1095,'Proofs17.8–17.10. Popa (1994), §1.3.5 and Theorem5.1.1, printed226.',20)
put('</g></svg>')
rootdir=Path(__file__).resolve().parent
(rootdir/'standard-model-trace-recovery.svg').write_text('\n'.join(out)+'\n',encoding='utf-8')
if rootdir.name!='figures':
 (rootdir/'figure-mathematical-check.json').write_text(json.dumps(dict(actual_model='Existing PG1–PG14; no new model construction',original_first_B_trace=[str(x) for x in odd],recovered_first_trace=[str(x) for x in even],tests=reports,cofinality_is_proved_not_inferred_from_finite_samples=True),indent=2)+'\n',encoding='utf-8')
print(json.dumps(dict(tested_K=[x['K'] for x in reports],cup_columns_checked=sum(x['cup_columns_checked'] for x in reports),balanced_matrix_units_checked=sum(x['balanced_matrix_units_checked'] for x in reports),svg='standard-model-trace-recovery.svg')))
