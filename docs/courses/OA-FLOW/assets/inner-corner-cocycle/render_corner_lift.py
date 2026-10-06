"""Exact Hilbert--Schmidt full-corner model; deterministic native illustration."""
from pathlib import Path
import argparse, json
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle, FancyBboxPatch, FancyArrowPatch

parser=argparse.ArgumentParser()
parser.add_argument('--output',type=Path,default=Path(__file__).resolve().parent/'assets')
args=parser.parse_args();out=args.output;out.mkdir(parents=True,exist_ok=True)
plt.rcParams.update({'font.family':'DejaVu Sans','font.size':16,'svg.hashsalt':'L117-exact-corner-lift-20261005','mathtext.fontset':'dejavusans'})
D=np.diag([1,-1]).astype(complex);e=np.diag([1,0]).astype(complex)
X=np.array([[1,1],[1,-1]],dtype=complex)
W=lambda x:1j*x@D
S=lambda x:D@x@D
U=lambda x:1j*D@x
basis=[]
for a in range(2):
 for b in range(2):
  v=np.zeros((2,2),dtype=complex);v[a,b]=1;basis.append(v)
pair_checks=[]
for a,A in enumerate(basis):
 for b,B in enumerate(basis):
  old=np.trace(B.conj().T@A);new=np.trace(W(B).conj().T@W(A))
  assert old==new
  pair_checks.append({'basis_pair':[a,b],'inner_product':int(old.real),'image_inner_product':int(new.real)})
assert np.array_equal(W(S(X)),U(X))
assert np.array_equal((1j*D)@e,1j*e)
assert np.array_equal(D@e,e)
assert np.trace(X.conj().T@X)==4
for image in [W(X),S(X),U(X)]:assert np.trace(image.conj().T@image)==4
eta1=e@X;eta2=np.array([[1,-1],[0,0]],dtype=complex)
E21=np.array([[0,0],[1,0]],dtype=complex)
assert np.array_equal(eta1+E21@eta2,X)
gram=[[e,np.zeros((2,2))],[np.zeros((2,2)),e]]
xx=[np.eye(2),E21]
for a in range(2):
 for b in range(2):assert np.array_equal(e@xx[a].conj().T@xx[b]@e,gram[a][b])

fig=plt.figure(figsize=(16,11.5),dpi=200,facecolor='#f6f8fb')
ax=fig.add_axes([0,0,1,1]);ax.set_xlim(0,16);ax.set_ylim(0,11.5);ax.axis('off')
ink='#183042';blue='#216b9a';teal='#177a76';purple='#734696'
def text(x,y,t,size=16,color=ink,**kw):ax.text(x,y,t,fontsize=size,color=color,va='center',**kw)
def panel(x,y,w,h,title):
 ax.add_patch(FancyBboxPatch((x,y),w,h,boxstyle='round,pad=.04,rounding_size=.12',facecolor='white',edgecolor='#bac8d5',lw=1.1))
 text(x+.2,y+h-.35,title,19,blue,weight='bold')
def cells(x,y,labels,active=None,size=1.0):
 for r in range(2):
  for c in range(2):
   color='#d6eeec' if active is None or (r,c) in active else '#edf1f5'
   ax.add_patch(Rectangle((x+c*size,y+(1-r)*size),size,size,facecolor=color,edgecolor='#708b9b',lw=1.2))
   text(x+(c+.5)*size,y+(1.5-r)*size,labels[r][c],20,teal,ha='center')
def arrow(x,y,x2,y2,label=None):
 ax.add_patch(FancyArrowPatch((x,y),(x2,y2),arrowstyle='-|>',mutation_scale=19,color=blue,lw=1.7))
 if label:text((x+x2)/2,(y+y2)/2+.23,label,16,blue,ha='center')

text(.55,10.95,'A full corner lifts a unitary and fixes its central phase',27,ink,weight='bold')
text(.55,10.45,r'$K=M_2(\mathbb{C})$, $N=L(M_2)$, $e=L(E_{11})$, $D=\mathrm{diag}(1,-1)$',20)
panel(.5,6.05,4.55,3.95,'1  Finite-sum domain')
cells(.8,7.5,[[r'$E_{11}$',r'$E_{12}$'],[r'$E_{21}$',r'$E_{22}$']],active={(0,0),(0,1)},size=.85)
text(2.75,8.8,r'$eK$: first row',16)
text(2.75,8.35,'complex dimension 2',15)
text(2.75,7.85,r'$K$: dimension 4',16)
text(.8,7.05,r'$X=\eta_1+E_{21}\eta_2$',18)
text(.8,6.6,r'$(ex_i^*x_je)_{ij}=\mathrm{diag}(e,e)$',17)
panel(5.35,6.05,4.55,3.95,'2  Gram lift')
cells(5.7,7.25,[[r'$i$',r'$-i$'],[r'$i$',r'$-i$']],size=.82)
text(7.75,8.5,r'$T(X)=iXD$ on $eK$',16)
text(7.75,7.95,r'$W_T(X)=iXD$ on $K$',15)
text(5.65,6.85,'16 mixed basis products are preserved',15)
text(5.65,6.45,r'$W_T\in N^\prime$, $W_Te=T$',17)
panel(10.2,6.05,5.3,3.95,'3  Implementer in N')
cells(10.55,7.25,[[r'$i$',r'$i$'],[r'$-i$',r'$-i$']],size=.82)
text(12.55,8.5,r'$S(X)=DXD$',17)
text(12.55,7.95,r'$u=W_TS=L(iD)$',17)
text(10.5,6.85,'Tables show phases on basis vectors,',15)
text(10.5,6.45,'not the entries of a density or projection.',15)

panel(.5,2.6,15,3.1,'4  An exact vector follows the composition order')
cells(1.0,3.05,[[r'$1$',r'$1$'],[r'$1$',r'$-1$']],size=.67)
text(1.67,5.05,r'$X$',18,ha='center')
arrow(2.65,3.72,5.15,3.72,r'$S$')
cells(5.55,3.05,[[r'$1$',r'$-1$'],[r'$-1$',r'$-1$']],size=.67)
text(6.22,5.05,r'$SX$',18,ha='center')
arrow(7.2,3.72,9.7,3.72,r'$W_T$')
cells(10.1,3.05,[[r'$i$',r'$i$'],[r'$-i$',r'$i$']],size=.67)
text(10.77,5.05,r'$W_T(SX)=uX$',18,ha='center')
text(12.05,4.15,r'$\|X\|_{\rm HS}^2=4$',17)
text(12.05,3.55,'every displayed image',15)
text(12.05,3.1,'has the same norm',15)

panel(.5,.4,15,1.8,'5  Prescribed corner removes the phase ambiguity')
text(.85,1.4,r'$D$ and $iD$ both implement $\operatorname{Ad}D$',18)
text(.85,.85,r'$De=e$, but $(iD)e=ie$: the value $v=ie$ selects $iD$.',17)
text(9.35,1.4,r'$u_t=\mathrm{diag}(e^{it/2},e^{3it/2})$',18,purple)
text(9.35,.85,r'$t=\pi$: $u_\pi=iD$.  Real-line example only.',16,purple)
fig.savefig(out/'corner-lift.png',dpi=200,metadata={'Software':'Exact L117 matrix illustration'})
fig.savefig(out/'corner-lift.svg',metadata={'Date':None,'Creator':'Exact L117 matrix illustration'})
svg=out/'corner-lift.svg';svg.write_text('\n'.join(x.rstrip() for x in svg.read_text(encoding='utf-8').splitlines())+'\n',encoding='utf-8',newline='\n')
plt.close(fig)
def matrix(z):
 return [[[int(w.real),int(w.imag)] for w in row] for row in z]
data={'native_width':3200,'native_height':2300,'scalar_coordinates':'pairs [real,imaginary]','space':'M2 Hilbert--Schmidt, linear-first inner product Tr(Y*X)','corner_rank_in_coefficient_algebra':1,'corner_rank_on_K':2,'whole_complex_dimension':4,'corner_complex_dimension':2,'D':matrix(D),'X':matrix(X),'WT_X':matrix(W(X)),'S_X':matrix(S(X)),'u_X':matrix(U(X)),'u':matrix(1j*D),'prescribed_corner':matrix(1j*e),'gram_operators':[[matrix(w) for w in row] for row in gram],'mixed_basis_checks':pair_checks,'norm_squared':4,'continuous_family':'u_t=diag(exp(it/2),exp(3it/2)); real-line illustrative model, theorem arbitrary nonabelian LCH','proof_links':['L117_RESTORED_PROOF.md#l117-gram','L117_RESTORED_PROOF.md#l117-inner','L117_RESTORED_PROOF.md#l117-model']}
(out/'corner-lift-data.json').write_text(json.dumps(data,indent=2)+'\n',encoding='utf-8',newline='\n')
print('All 16 mixed Gram checks, 4 corner Gram operators, exact matrices and norm checks pass.')
