"""Independent finite exact checks of the parameter-chain and sign contracts."""
from collections import defaultdict
from itertools import combinations
from fractions import Fraction as F
import json,sys
sys.dont_write_bytecode=True
def add(*chains):
 d=defaultdict(int)
 for chain,k in chains:
  for s,v in chain.items():d[s]+=k*v
 return {s:v for s,v in d.items() if v}
def singleton(s):return {tuple(s):1}
def boundary(c):
 out=defaultdict(int)
 for s,a in c.items():
  if len(s)==1:continue
  for i in range(len(s)):out[s[:i]+s[i+1:]]+=a*(-1)**i
 return {s:a for s,a in out.items() if a}
def cross(a,b):
 r=len(a)-1;s=len(b)-1;out=defaultdict(int)
 for horiz in combinations(range(r+s),r):
  horiz=set(horiz);i=j=0;vertices=[(a[0],b[0])];inv=0
  for k in range(r+s):
   if k in horiz:i+=1;inv+=j
   else:j+=1
   vertices.append((a[i],b[j]))
  out[tuple(vertices)]+=(-1)**inv
 return {s:a for s,a in out.items() if a}
def tensor_boundary_product(a,b):
 r=len(a)-1;out={}
 if r:
  for i in range(len(a)):out=add((out,1),(cross(a[:i]+a[i+1:],b),(-1)**i))
 if len(b)>1:
  for j in range(len(b)):out=add((out,1),(cross(a,b[:j]+b[j+1:]),(-1)**(r+j)))
 return out
def W(m):
 out={}
 for r in range(m+1):out=add((out,1),(cross(tuple(range(r+1)),tuple(range(r,m+1))),1))
 return out
def L(m):return singleton((i,i) for i in range(m+1))
def embed_face(c,m,i):
 idx=[j for j in range(m+1) if j!=i]
 return {tuple((idx[a],idx[b]) for a,b in s):v for s,v in c.items()}
def face_sum(c,m):
 out={}
 for i in range(m+1):out=add((out,1),(embed_face(c,m,i),(-1)**i))
 return out
def Hs(n):
 hs=[{}]
 for m in range(1,n+1):
  z=add((L(m),1),(W(m),-1),(face_sum(hs[m-1],m),-1))
  if boundary(z):raise RuntimeError('Residual is not a cycle at '+str(m))
  h={((0,0),)+s:v for s,v in z.items()}
  if boundary(h)!=z:raise RuntimeError('Cone identity failed at '+str(m))
  hs.append(h)
 return hs
def edge_B(P,Q,h):
 # Integrate pr1*dx wedge pr2*dy on the actual pushed affine H1.
 def x(v):return F(P[0])+F(v[0])*(F(Q[0])-F(P[0]))
 def y(v):return F(P[1])+F(v[1])*(F(Q[1])-F(P[1]))
 total=F(0)
 for s,a in h.items():
  p0,p1,p2=s
  det=(x(p1)-x(p0))*(y(p2)-y(p0))-(x(p2)-x(p0))*(y(p1)-y(p0))
  total+=a*det/2
 return total
def checks():
 product=[]
 for r in range(6):
  for s in range(6-r):
   a=tuple(range(r+1));b=tuple(range(s+1))
   if boundary(cross(a,b))!=tensor_boundary_product(a,b):raise RuntimeError('Product boundary defect')
   product.append({'r':r,'s':s,'shuffle_terms':len(cross(a,b))})
 hs=Hs(5);homotopy=[]
 for m in range(6):
  if m and boundary(W(m))!=face_sum(W(m-1),m):raise RuntimeError('AW-cross chain map defect')
  lhs=add((boundary(hs[m]),1),(face_sum(hs[m-1],m),1))if m else{}
  if lhs!=add((L(m),1),(W(m),-1)):raise RuntimeError('Homotopy defect')
  for simplex in hs[m]:
   if not all(0<=a<=m and 0<=b<=m for a,b in simplex):raise RuntimeError('Carrier vertex escapes parameter product')
  homotopy.append({'m':m,'H_affine_terms':len(hs[m]),'identity':'exact','parameter_carrier_vertices':'inside'})
 triangles=[]
 for A,B,C in [((0,0),(1,0),(1,1)),((-2,1),(3,-1),(0,4)),((1,2),(1,2),(4,5))]:
  wedge=F((B[0]-A[0])*(C[1]-A[1])-(C[0]-A[0])*(B[1]-A[1]),2)
  cup=F((B[0]-A[0])*(C[1]-B[1]))
  delta=edge_B(B,C,hs[1])-edge_B(A,C,hs[1])+edge_B(A,B,hs[1])
  if wedge-cup!=delta:raise RuntimeError('Actual integral homotopy sign defect')
  triangles.append({'vertices':[A,B,C],'wedge':str(wedge),'cup':str(cup),'delta_B':str(delta)})
 # Relative-to-ambient ordering in learner Example3:
 permutation=(3,1,0,2);inversions=sum(permutation[i]>permutation[j] for i in range(4)for j in range(i+1,4))
 if inversions!=4:raise RuntimeError('Normal/base permutation defect')
 # g=-dphi, beta=-f ds => g wedge beta=-f ds wedge dphi.
 base=-1;annular=1
 if annular!=(-1)**1*base:raise RuntimeError('Annular parity defect')
 # Cubical normalization: two oriented triangles each have area 1/2.
 unit_square=F(1,2)+F(1,2)
 if unit_square!=1:raise RuntimeError('Oriented box normalization defect')
 return {'schema':'AN02-form-right-cap046-exact-chain-checks/v1','status':'pass',
 'product_boundary_checks':product,'universal_homotopy_checks':homotopy,
 'actual_affine_form_integral_checks':triangles,'unit_square_top_integral':str(unit_square),
 'normal_circle_example':{'permutation':permutation,'inversions':inversions,'base_integral':base,'annular_integral':annular,'p':1},
 'limits':'Finite algebraic checks support, but do not replace, the complete all-degree proof; no numerical test proves the general support or orientation theorem.'}
if __name__=='__main__':print(json.dumps(checks(),indent=2))
