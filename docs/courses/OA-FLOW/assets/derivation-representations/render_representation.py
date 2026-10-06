"""Original CC0 exact matrix diagram for a nonfaithful, degenerate representation."""
from pathlib import Path
import json
import sympy as sp
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle,FancyBboxPatch,FancyArrowPatch

OUT=Path(__file__).resolve().parent
plt.rcParams.update({'font.family':'DejaVu Sans','font.size':16,'mathtext.fontset':'dejavusans','svg.fonttype':'path','svg.hashsalt':'oa-flow-l35-representation-v1'})
navy='#17334d';blue='#2563a6';teal='#147a70';orange='#b45118';gray='#718294';light='#f1f5f9'
I2=sp.eye(2);I3=sp.eye(3);I7=sp.eye(7);Z3=sp.zeros(3)
def unit(n,i,j):
 m=sp.zeros(n);m[i,j]=1;return m

def comm(x,y):return x*y-y*x
h1=sp.diag(0,2);h2=sp.diag(0,5)
a=sp.Matrix(2,2,sp.symbols('a11 a12 a21 a22'));b=sp.Matrix(2,2,sp.symbols('b11 b12 b21 b22'))
T=sp.Matrix(2,2,sp.symbols('t11 t12 t21 t22'));c=sp.Matrix(2,2,sp.symbols('c11 c12 c21 c22'));e=sp.Matrix(2,2,sp.symbols('e11 e12 e21 e22'))
assert comm(h1,a)==sp.Matrix([[0,-2*a[0,1]],[2*a[1,0],0]])
assert comm(h2,b)==sp.Matrix([[0,-5*b[0,1]],[5*b[1,0],0]])
assert sp.expand(sp.trace(T*e*a*c)-sp.trace(c*T*e*a))==0
assert sp.expand(sp.trace(T*sp.I*comm(h1,a))-sp.trace(sp.I*comm(T,h1)*a))==0
E21=unit(2,1,0)
assert comm(h1,E21)==2*E21 and comm(h2,E21)==5*E21
p=sp.diag(1,1,1,1,0,0,0);q=I7-p
S=sp.diag(-1,-1,1,1,0,0,0);B=sp.diag(0,0,2,2,0,0,0)
pi=sp.diag(sp.kronecker_product(a,I2),Z3)
lam=sp.symbols('lambda');full=pi+lam*q
assert comm(S,full)==sp.diag(sp.kronecker_product(comm(h1,a),I2),Z3)
assert comm(S+q,full)==comm(S,full) and comm(B+q,full)==comm(B,full)
pi_generators=[sp.diag(sp.kronecker_product(unit(2,i,j),I2),Z3) for i in range(2) for j in range(2)]
comm_generators=[sp.diag(sp.kronecker_product(I2,unit(2,i,j)),Z3) for i in range(2) for j in range(2)]
comm_generators += [sp.diag(sp.zeros(4),unit(3,i,j)) for i in range(3) for j in range(3)]
def commutant_dim(gs):
 equations=sp.Matrix.vstack(*[sp.kronecker_product(I7,g)-sp.kronecker_product(g.T,I7) for g in gs])
 return 49-equations.rank()
assert all(comm(x,y)==sp.zeros(7) for x in pi_generators for y in comm_generators)
dim_comm=commutant_dim(pi_generators);dim_bicom=commutant_dim(comm_generators)
assert dim_comm==13 and dim_bicom==5
checks={'source_algebra':'M2 direct_sum M2','source_complex_dimension':8,'hilbert_dimensions':{'essential':4,'silent':3,'total':7},'representation':'pi(a,b)=(a tensor I2) direct_sum zero3','surviving_central_projection':'z=(I2,0)','kernel':'0 direct_sum M2','pi_image_dimension':4,'commutant':'(I2 tensor M2) direct_sum M3','commutant_dimension_exact':dim_comm,'bicommutant':'(M2 tensor I2) direct_sum C I3','bicommutant_dimension_exact':dim_bicom,'h1_diagonal':[0,2],'h2_diagonal':[0,5],'source_derivation_norm':5,'represented_derivation_norm':2,'centered_implementer_diagonal':list(S.diagonal()),'centered_implementer_norm':1,'least_positive_implementer_diagonal':list(B.diagonal()),'least_positive_implementer_norm':2,'silent_projection_diagonal':list(q.diagonal()),'norm_witness':'e21 in each M2: [h1,e21]=2e21, [h2,e21]=5e21','dual_module_product':'c phi_T e = phi_(c1 T e1)','dual_derivation':'d* phi_T = phi_(i[T,h1])','zero_representation_on_C7':{'commutant':'M7','bicommutant':'C I7','normal_extension_image':'0','represented_derivation':'0'},'all_exact_assertions_pass':True}
OUT.joinpath('exact_checks.json').write_text(json.dumps(checks,indent=2,default=str)+'\n',encoding='utf-8')
fig=plt.figure(figsize=(18,11),facecolor='white')
fig.text(.045,.95,'A nonfaithful, degenerate representation',fontsize=28,weight='bold',color=navy)
fig.text(.045,.902,r'$A=M_2\oplus M_2,\qquad\mathcal{H}=(\mathbb{C}^2\otimes\mathbb{C}^2)\oplus\mathbb{C}^3$',fontsize=23,color=navy)
fig.text(.045,.858,'The surviving algebra corner acts with multiplicity two; three Hilbert coordinates are silent.',fontsize=17,color=gray)
# Input algebra has two independent 2x2 blocks.
ax=fig.add_axes([.04,.345,.20,.445]);ax.set_xlim(-.5,2.8);ax.set_ylim(-.6,6.3);ax.axis('off')
for top,symbol,col in [(5.3,'a',blue),(2.2,'b',gray)]:
 for i in range(2):
  for j in range(2):
   ax.add_patch(Rectangle((j,top-1-i),1,1,facecolor=col,alpha=.12,edgecolor='none'))
   ax.text(j+.5,top-.5-i,'$'+symbol+'_{'+str(i+1)+str(j+1)+'}$',fontsize=22,color=col,ha='center',va='center')
 ax.add_patch(Rectangle((0,top-2),2,2,fill=False,edgecolor=col,lw=2))
ax.text(1,5.6,r'$zA=M_2\oplus0$',fontsize=20,ha='center',color=blue)
ax.text(1,2.5,r'$(1-z)A=0\oplus M_2$',fontsize=18,ha='center',color=gray)
ax.text(1,2.94,r'$h_1=\operatorname{diag}(0,2)$',fontsize=15,ha='center',color=blue)
ax.text(1,-.12,r'$h_2=\operatorname{diag}(0,5)$',fontsize=15,ha='center',color=orange)
fig.text(.135,.305,r'kernel: $\pi(0,b)=0$',fontsize=17,color=gray,ha='center')
# Explicit 7x7 matrix arrays, using the ordered tensor basis.
def block_matrix(ax,silent):
 ax.set_xlim(0,7);ax.set_ylim(0,7);ax.set_aspect('equal');ax.axis('off')
 for i in range(7):
  for j in range(7):
   active=(i<4 and j<4);tail=(i>=4 and j>=4)
   col=blue if active else (teal if silent and tail else gray)
   alpha=.105 if active else (.115 if tail else .025)
   ax.add_patch(Rectangle((j,6-i),1,1,facecolor=col,alpha=alpha,edgecolor='none'))
   value='0';textcol=gray;font=14
   if active and i%2==j%2:
    value=r'$a_{'+str(i//2+1)+str(j//2+1)+'}$';textcol=blue;font=18
   elif silent and tail and i==j:
    value=r'$\lambda$';textcol=teal;font=20
   ax.text(j+.5,6.5-i,value,ha='center',va='center',color=textcol,fontsize=font)
 ax.add_patch(Rectangle((0,0),7,7,fill=False,edgecolor=navy,lw=1.8))
 ax.plot([4,4],[0,7],color=navy,lw=1.8);ax.plot([0,7],[3,3],color=navy,lw=1.8)
axp=fig.add_axes([.315,.35,.27,.442]);block_matrix(axp,False)
axm=fig.add_axes([.69,.35,.27,.442]);block_matrix(axm,True)
fig.text(.45,.813,r'$\pi(A)=\overline{\pi}(A^{**})$',fontsize=22,ha='center',color=navy)
fig.text(.825,.813,r'$M=\pi(A)^{\prime\prime}$',fontsize=22,ha='center',color=navy)
fig.text(.45,.312,'zero on the silent '+r'$\mathbb{C}^3$',fontsize=17,ha='center',color=gray)
fig.text(.825,.312,'independent scalar '+r'$\lambda I_3$',fontsize=17,ha='center',color=teal)
fig.patches.append(FancyArrowPatch((.227,.659),(.307,.659),transform=fig.transFigure,arrowstyle='-|>',mutation_scale=23,color=blue,lw=2.5))
fig.text(.267,.687,r'$\pi$',fontsize=24,ha='center',color=blue)
fig.patches.append(FancyArrowPatch((.598,.563),(.68,.563),transform=fig.transFigure,arrowstyle='-|>',mutation_scale=23,color=teal,lw=2.5))
fig.text(.639,.598,'bicommutant',fontsize=14,ha='center',color=teal)
fig.text(.639,.52,'adds '+r'$\mathbb{C}q$',fontsize=14,ha='center',color=teal)
# Exact norm and implementer data.
for x,wid in [(.045,.40),(.49,.47)]:
 fig.patches.append(FancyBboxPatch((x,.11),wid,.145,transform=fig.transFigure,boxstyle='round,pad=0.01',facecolor=light,edgecolor='#d9e2eb'))
fig.text(.245,.206,r'$\|d\|=5\quad\longrightarrow\quad\|D\|=2$',fontsize=26,ha='center',color=navy)
fig.text(.245,.15,'The discarded corner carried the larger norm.',fontsize=15,ha='center',color=gray)
fig.text(.725,.207,r'$S=\operatorname{diag}(-1,-1,1,1,0,0,0)$',fontsize=19,ha='center',color=navy)
fig.text(.725,.146,r'$D(x)=i[S,x],\qquad\|S\|=1=\frac{1}{2}\|D\|$',fontsize=23,ha='center',color=navy)
fig.text(.50,.062,r'$\pi(A)^{\prime}=(I_2\otimes M_2)\oplus M_3,\qquad M=(M_2\otimes I_2)\oplus\mathbb{C}I_3$',fontsize=20,ha='center',color=navy)
fig.text(.045,.025,'Exact algebra blocks in the ordered tensor basis. Proof: L35, represented-derivation example (E1)–(E11).',fontsize=13,color=gray)
fig.savefig(OUT/'surviving-corner-silent-summand.png',dpi=200,facecolor='white')
fig.savefig(OUT/'surviving-corner-silent-summand.svg',metadata={'Date':None},facecolor='white')
plt.close(fig)
print(json.dumps({'png':'surviving-corner-silent-summand.png','pixels':[3600,2200],'commutant_dimension':dim_comm,'bicommutant_dimension':dim_bicom,'exact_checks':True}))
