from pathlib import Path
import pathlib,json,datetime,math,itertools
from fractions import Fraction as F
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
plt.rcParams["svg.hashsalt"]="sharp-cut-return-v22"
from matplotlib.patches import Rectangle,FancyArrowPatch

own=pathlib.Path(__file__).resolve().parent
checks=[]
def record(name,condition,detail):
 if not condition: raise AssertionError(name)
 checks.append({'name':name,'passed':bool(condition),'detail':detail})
weights={'tau':[F(1,7),F(5,21)],'rho':[F(3,10),F(2,15)]}
n=[2,3];h=[[2,0],[2,0]]
record('both exact trace unit normalizations',all(sum(n[b]*w[b] for b in range(2))==1 for w in weights.values()),weights.__str__())
minima={k:sum(w[b]*max(sum(v[b] for v in h)-n[b],0) for b in range(2)) for k,w in weights.items()}
record('simultaneous exact minima',minima=={'tau':F(2,7),'rho':F(3,5)},str(minima))
allocs=[a for a in itertools.product(range(3),repeat=2) if sum(a)<=2]
for k,w in weights.items():
 vals=[sum((2-a[i])*w[0] for i in range(2)) for a in allocs]
 record('integer enumeration '+k,min(vals)==minima[k],str(min(vals)))
cup=[(4,F(1,9)),(2,F(1,9)),(2,F(1,9)),(1,F(1,9))]
record('actual two cup unit mass',sum(m*v for m,v in cup)==1,str(cup))
for k,w in weights.items():
 beta=sum(w)*sum(v for m,v in cup)
 cut=sum(w[b]*v*m*max(sum(u[b] for u in h)-n[b],0) for b in range(2) for m,v in cup)
 record('tensor cost invariant '+k,cut==minima[k],str(cut))
 record('tensor beta '+k,beta==({'tau':F(32,189),'rho':F(26,135)}[k]),str(beta))
record('index25 h200 exact total integer bound',2*F(24,25)**200<F(1,1000),'2*(24/25)^200<1/1000')

def l2sq(x):return float(np.vdot(x,x).real/x.shape[0])
rng=np.random.default_rng(220109)
ratios=[]
for size in range(2,10):
 for rankd in range(size+1):
  for rep in range(12):
   ra=rng.normal(size=(size,size))+1j*rng.normal(size=(size,size))
   a=ra/max(1,np.linalg.norm(ra,2))
   d=np.diag([0]*(size-rankd)+[1]*rankd);e=np.eye(size)-d
   re=size-rankd
   rc=rng.normal(size=(size,size))+1j*rng.normal(size=(size,size))
   c=e@rc@e+d@rc@d;c=c/max(1,np.linalg.norm(c,2))
   diff=a-e@a@e-d@c
   delta=rankd/size;lhs=l2sq(diff)
   if delta: ratios.append(math.sqrt(lhs/delta))
   gamma=float(np.linalg.norm(c,2))
   bound=2*(1+gamma**2)*delta
   record(f'nonselfadjoint block inequality size{size} d{rankd} case{rep}',lhs<=bound+2e-12,{'lhs_squared':lhs,'bound_squared':bound,'gamma':gamma})
e=np.diag([1,0,0]);d=np.diag([0,1,0]);r=e+d;a=-r;c=np.eye(3)
diff=a-e@a@e-d@c
record('exact equality matrix fixture',abs(l2sq(diff)-4/3)<1e-14,{'lhs_squared':l2sq(diff),'expected':4/3})
record('smaller comparison constant rejected',l2sq(diff)>(F(199,100)**2)*F(1,3),'constant1.99 rejected by exact equality example')
for gamma in [0,F(3,5),F(4,5),1]:
 g=float(gamma);s=math.sqrt(1-g*g)
 a=np.array([[-g,s,0],[s,g,0],[0,0,0]])
 c=-g*np.eye(3);diff=a-e@a@e-d@c
 bound=2*(1+g*g)/3
 record('every gamma equality fixture '+str(gamma),abs(l2sq(diff)-bound)<1e-14,{'lhs_squared':l2sq(diff),'exact_bound':str(2*(1+gamma**2)*F(1,3))})

# Three row identities in a finite tensor diagnostic: physical M=Mat3 tensor Mat2 tensor Mat4.
# A type-I test of the finite algebra calculations, not a substitute II1 construction.
def trace_first(x,dims,count):
 arr=x.reshape(*dims,*dims)
 keep=dims[count:];discard=math.prod(dims[:count]);keepdim=math.prod(keep)
 arr=arr.reshape(discard,keepdim,discard,keepdim)
 small=np.einsum('abad->bd',arr)/discard
 return np.kron(np.eye(discard),small)
def pinch_last(x,groups):
 ans=np.zeros_like(x)
 for g in groups:
  p=np.zeros((4,4));p[g,g]=1;p=np.kron(np.eye(6),p)
  ans+=p@x@p
 return ans
z=rng.normal(size=(24,24))+1j*rng.normal(size=(24,24));groups=[[0,1],[2,3]]
pz=pinch_last(z,groups)
enz=trace_first(z,(3,2,4),1);ekz=trace_first(z,(3,2,4),2)
qz=pinch_last(enz,groups);dz=pinch_last(ekz,groups)
rows=[('EN EP = EQ',trace_first(pz,(3,2,4),1),qz),('EP EN = EQ',pinch_last(enz,groups),qz),('ENk EP = ED',trace_first(pz,(3,2,4),2),dz),('EP ENk = ED',pinch_last(ekz,groups),dz),('ENk EQ = ED',trace_first(qz,(3,2,4),2),dz),('EQ ENk = ED',pinch_last(trace_first(ekz,(3,2,4),1),groups),dz)]
for name,x,y in rows:record('three physical row '+name,np.max(abs(x-y))<1e-12,{'max_abs_error':float(np.max(abs(x-y)))})

summary={'created_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'checks_count':len(checks),'all_passed':all(x['passed'] for x in checks),'max_random_comparison_ratio':max(ratios),'analytic_proof_required':True,'claim':'2 is sharp for specified candidate; expectation bound upper constant2 proved, no sharpness claimed there','checks':checks}
(own/'selfcheck.json').write_text(json.dumps(summary,indent=2)+'\n',encoding='utf-8')

plt.rcParams.update({'font.size':13,'font.family':'DejaVu Sans'})
fig=plt.figure(figsize=(15.5,10),layout='constrained')
gs=fig.add_gridspec(2,2,height_ratios=[1,1.03])
ax=fig.add_subplot(gs[0,0]);ax.set_xlim(0,10);ax.set_ylim(0,6);ax.axis('off')
ax.set_title('The same physical candidate, bounded more sharply',loc='left',fontweight='bold',pad=14)
for x,y,wid,ht,col,txt in [(1,2.6,3.4,1.4,'#dbeafe','0'),(4.4,2.6,3.4,1.4,'#ffedd5','X = ead'),(1,1.2,3.4,1.4,'#ffedd5','Y = dae'),(4.4,1.2,3.4,1.4,'#fee2e2','Z − C = dad − dc')]:
 ax.add_patch(Rectangle((x,y),wid,ht,facecolor=col,edgecolor='#334155',linewidth=1.5));ax.text(x+wid/2,y+ht/2,txt,ha='center',va='center')
ax.text(2.7,4.2,'kept e',ha='center');ax.text(6.1,4.2,'cut d',ha='center')
ax.text(.3,.3,'a − eae − dc     (block areas are schematic)',fontsize=12)
ax.text(.3,5.1,'‖a‖ ≤ R; ‖c‖ ≤ γ ≤ R; [c,e] = [c,d] = 0',fontsize=14)
ax=fig.add_subplot(gs[0,1]);u=np.linspace(0,1,401);ax.plot(u,4-(u-1)**2,lw=3,color='#2563eb',label='Exact block bound 4 − (z/s − 1)²')
ax.axhline(4,color='#dc2626',lw=2,label='New squared comparison bound: 4')
ax.axhline((1+math.sqrt(2))**2,color='#64748b',ls='--',lw=2,label='Previous squared bound: (1 + √2)²')
ax.set_ylim(2.7,6.2);ax.set_xlim(0,1);ax.set_xlabel('z/s = ‖dad‖₂ / (R √τ(d)); panel has γ = R');ax.set_ylabel('Squared error / (R² τ(d))');ax.grid(alpha=.2);ax.legend(fontsize=10,loc='center left');ax.set_title('Orthogonal off-diagonal energy supplies the gain',loc='left',fontweight='bold',pad=14)
ax=fig.add_subplot(gs[1,:]);ax.set_xlim(0,15);ax.set_ylim(0,5.3);ax.axis('off')
ax.set_title('The full residual and all three marked rows remain physical',loc='left',fontweight='bold',pad=13)
for y,segments in [(3.45,[(.3,3.3,'#bfdbfe','old cell r₁'),(4,3.3,'#bfdbfe','old cell r₂'),(7.7,2.1,'#e2e8f0','old residual f')]),(2.35,[(.3,2.3,'#bfdbfe','kept e₁'),(2.6,1,'#fed7aa','d₁'),(4,2.3,'#bfdbfe','kept e₂'),(6.3,1,'#fed7aa','d₂'),(7.7,2.1,'#e2e8f0','f')])]:
 for x,wid,col,txt in segments:
  ax.add_patch(Rectangle((x,y),wid,.7,facecolor=col,edgecolor='#334155',linewidth=1.2));ax.text(x+wid/2,y+.35,txt,ha='center',va='center',fontsize=12)
ax.add_patch(FancyArrowPatch((10.1,2.68),(11,2.68),arrowstyle='->',mutation_scale=18,color='#475569'))
ax.text(11.1,2.95,'f* = f + d₁ + d₂',fontweight='bold');ax.text(11.1,2.35,'Actual residual certificate\nand its own whole origin',fontsize=11)
ax.text(.3,1.65,'Original targets y stay fixed.  Every prescribed prefix and cup is retained.',fontsize=14)
ax.text(.3,.85,'E_N P* = Q*;    E_Nk P* = D*;    E_Nk Q* = D*   (and both L² expectation orders)',fontsize=13)
ax.text(.3,.18,'Added error ≤ √[2(‖y‖² + γᵧ²)Δ] ≤ 2‖y‖√Δ; if f = 0: √2‖y‖√Δ.       FS.7–FS.15',fontsize=14,color='#1d4ed8')
fig.suptitle('Sharper cut-and-return comparison; the unrestricted selection problem is still open',fontsize=19,fontweight='bold')
fig.savefig(own/'sharp-cut-return-v22.png',dpi=130)
fig.savefig(own/'sharp-cut-return-v22.svg',metadata={"Date":None})
print(json.dumps({'all_passed':summary['all_passed'],'checks_count':len(checks),'max_random_ratio':summary['max_random_comparison_ratio'],'figure':str(own/'sharp-cut-return-v22.png')}))

svg_path=Path(__file__).resolve().parent/"sharp-cut-return-v22.svg"
svg_path.write_text("\n".join(x.rstrip() for x in svg_path.read_text(encoding="utf-8").splitlines()).rstrip()+"\n",encoding="utf-8")
