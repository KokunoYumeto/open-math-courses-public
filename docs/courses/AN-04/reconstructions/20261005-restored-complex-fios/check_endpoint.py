"""Finite controls for the new complete endpoint proof; not a theorem certificate."""
from pathlib import Path
import hashlib,json
import numpy as np
import sympy as s
ROOT=Path(__file__).resolve().parent
checks=[]
x,e,R=s.symbols('x e R',real=True,positive=True)
q=s.exp(s.I*s.sqrt(R)*x-x*x/2-(e-R)**2/(2*R))
balanced=q.subs({x:x/s.sqrt(R),e:s.sqrt(R)*e},simultaneous=True)
expected=s.exp(s.I*x-x*x/(2*R)-(e-s.sqrt(R))**2/2)
assert s.simplify(balanced-expected)==0
for al in range(4):
 for be in range(4):
  lhs=s.diff(balanced,x,al,e,be)
  rhs=R**s.Rational(be-al,2)*s.diff(q,x,al,e,be).subs({x:x/s.sqrt(R),e:s.sqrt(R)*e},simultaneous=True)
  assert s.simplify(lhs-rhs)==0
wrong=q.subs({x:s.sqrt(R)*x,e:s.sqrt(R)*e},simultaneous=True)
assert s.simplify(s.diff(wrong,x).subs({x:0,e:s.sqrt(R)})-s.diff(expected,x).subs({x:0,e:s.sqrt(R)}))!=0
checks.append({'name':'Exact balanced Gaussian/modulation dilation and sixteen mixed derivatives','passed':True,
 'scope':'Actual substituted family, both scaling factors, full chain identities and a wrong-spatial-dilation negative control; the Schwartz model supplements the compact-support proof.'})
trials=0
for n in range(1,7):
 N=n+2
 for j in range(25):
  for k in range(25):
   if abs(k-j)<4:continue
   exponent=(N+n/2)*j+n*k/2-2*N*max(j,k)
   assert exponent<=-j-k
   # Geometric separation, including the low-frequency balls.
   imin=0 if j==0 else 2**(j-1);imax=2**(j+1)
   omin=0 if k==0 else 2**k;omax=2**(k+1)
   gap=max(imin-omax,omin-imax)
   assert gap>=.375*2**max(j,k)
   trials+=1
checks.append({'name':'Both off-diagonal Schur exponents and low-frequency separation','passed':True,
 'trials':trials,'scope':'Dimensions 1–6 and shells 0–24; exact exponent arithmetic, both triangular regions and separation constant 3/8. The written proof treats all shells.'})
norms=[]
for count in [12,32,64]:
 j,k=np.meshgrid(np.arange(count),np.arange(count))
 near=(abs(k-j)<=3).astype(float)
 far=np.where(abs(k-j)>=4,2.**(-j-k),0.)
 assert np.max(near.sum(axis=0))<=7 and np.max(near.sum(axis=1))<=7
 assert np.linalg.norm(near,2)<=7+1e-12
 assert far.sum()<4
 norms.append({'shell_count':count,'near_norm':float(np.linalg.norm(near,2)),'far_entry_sum':float(far.sum())})
# Uniform norms by themselves do not justify summation.
assert np.linalg.norm(sum(np.eye(3) for _ in range(12)),2)==12
checks.append({'name':'Actual finite shell operator matrices and failure without overlap control','passed':True,
 'models':norms,'scope':'Banded matrix norm and summable far matrix; twelve coincident identity pieces have norm twelve despite each having norm one.'})
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
report={'passed':True,'checks':checks,'source_sha256':sha(ROOT/'endpoint-half-order-bound.md'),
 'script_sha256':sha(Path(__file__)),'general_proof_certified_by_finite_checks':False}
(ROOT/'endpoint-checks.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n','utf-8')
print(json.dumps({'passed':True,'finite_controls':len(checks),'geometric_trials':trials}))
