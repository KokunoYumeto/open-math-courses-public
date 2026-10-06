"""Original exact Gram-isometry illustration; CC0-1.0 to the extent of rights held."""
from pathlib import Path
import json
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch,FancyArrowPatch
P=Path(__file__).resolve().parent;out=P/'assets';out.mkdir(exist_ok=True)
plt.rcParams.update({'font.family':'DejaVu Sans','mathtext.fontset':'dejavusans','svg.hashsalt':'homogeneous-gram-20261005'})
def mul(a,b):return [[sum(a[i][k]*b[k][j] for k in range(4)) for j in range(4)] for i in range(4)]
def adj(a):return [list(x) for x in zip(*a)]
def neg(a):return [[-x for x in row] for row in a]
def sigma(a):return [[a[(i+2)%4][(j+2)%4] for j in range(4)] for i in range(4)]
basis=[]
for i in range(2):
    for j in range(2):
        a=[[0]*4 for _ in range(4)];a[i][j]=1;a[i+2][j+2]=-1;basis.append(a)
identity=[[int(i==j) for j in range(4)] for i in range(4)]
V=neg(identity)
for x in basis:
    assert sigma(x)==neg(x)==mul(V,x)
    for y in basis:assert mul(adj(sigma(x)),sigma(y))==mul(adj(x),y)
x1,x2=basis[0],basis[3]
supports=[[1,0,1,0],[0,1,0,1]]
assert [a+b for a,b in zip(*supports)]==[1]*4
fig=plt.figure(figsize=(14,10),dpi=200,facecolor='#f5f7fa')
ink='#18364c';teal='#007f89';muted='#4e6374'
fig.text(.05,.956,'Recover an automorphism from its action on a whole fiber',size=20,weight='bold',color=ink)
fig.text(.05,.925,'The range vectors determine a unitary; homogeneity determines its scalar.',size=13,color=muted)
def panel(y,h,title):
    ax=fig.add_axes([.045,y,.91,h]);ax.set(xlim=(0,1),ylim=(0,1));ax.axis('off')
    ax.add_patch(FancyBboxPatch((.005,.012),.99,.975,boxstyle='round,pad=.003',fc='white',ec='#c6d1da'))
    ax.text(.025,.89,title,size=14,weight='bold',color=ink);return ax
def box(ax,xy,w,h,label):
    ax.add_patch(FancyBboxPatch(xy,w,h,boxstyle='round,pad=.007',fc='#e8f3f4',ec=teal))
    ax.text(xy[0]+w/2,xy[1]+h/2,label,ha='center',va='center',size=13,color=ink,linespacing=1.7)
def arrow(ax,a,b):ax.add_patch(FancyArrowPatch(a,b,arrowstyle='-|>',mutation_scale=17,lw=1.5,color=teal))
a=panel(.645,.245,'1  The map is defined on sums, so every mixed Gram term matters (HC1)')
box(a,(.035,.36),.29,.35,r'$\sum_i x_i\xi_i$'+'\n'+r'dense span in $\mathcal{H}$')
box(a,(.675,.36),.29,.35,r'$\sum_i\sigma(x_i)\xi_i$'+'\n'+r'dense span in $\mathcal{H}$')
arrow(a,(.34,.54),(.66,.54))
a.text(.50,.65,r'$V_0$',ha='center',size=17,color=teal)
a.text(.50,.42,r'$\sigma(x_i)^*\sigma(x_j)=x_i^*x_j$',ha='center',size=14,color=ink)
a.text(.025,.12,'Equal Gram matrices  →  well defined isometry  →  onto unitary V on the same Hilbert space',size=12,color=muted)
b=panel(.375,.245,'2  The unitary is forced by the fiber, and then fixed by every commuting symmetry (HC1–3)')
box(b,(.025,.39),.27,.32,r'$Vx=\sigma(x)$'+'\n'+r'$V\in M\cap A^\prime$')
box(b,(.365,.39),.27,.32,r'$\beta(V)=V$'+'\n'+r'for every $\beta\in H_\alpha$')
box(b,(.705,.39),.27,.32,r'$V=\lambda(p)1$'+'\n'+r'$\sigma|_{M_p}=\lambda(p)\,\mathrm{id}$')
arrow(b,(.31,.55),(.35,.55));arrow(b,(.65,.55),(.69,.55))
b.text(.025,.15,r'Nonzero fiber products give $\lambda(p+q)=\lambda(p)\lambda(q)$; Fourier density and biduality give $\sigma=\alpha_{s_0}$.',size=12,color=muted)
c=panel(.075,.275,'3  Exact example: interchange on M₂ ⊕ M₂ has a four-dimensional nontrivial fiber (HC4)')
c.text(.025,.72,r'$A=\{(a,a)\}$,   $M_1=\{(a,-a)\}$,   $\sigma(a,b)=(b,a)$',size=15,color=ink)
c.text(.025,.53,r'$x_1=\operatorname{diag}(1,0,-1,0)$',size=14,color=teal)
c.text(.515,.53,r'$x_2=\operatorname{diag}(0,1,0,-1)$',size=14,color=teal)
c.text(.025,.35,r'$\ell(x_1)=\operatorname{diag}(1,0,1,0)$',size=13,color=ink)
c.text(.515,.35,r'$\ell(x_2)=\operatorname{diag}(0,1,0,1)$',size=13,color=ink)
c.text(.025,.16,r'$\ell(x_1)+\ell(x_2)=I_4$,    $\sigma(x_i)=-x_i$    ⇒    $V=-I_4$,    $\lambda(1)=-1$.',size=15,color=teal)
fig.text(.05,.040,'The boxes are proof objects, not finite-dimensional approximations. Only the last panel is a finite matrix model.',size=10.5,color=muted)
fig.text(.05,.018,'Proof: HC1–4. Target: Takesaki II, Exercise XI.1.5, pp.330–331. Original Gram-isometry route and exact illustration.',size=10,color=muted)
fig.savefig(out/'homogeneous-gram.png',metadata={'Software':'Original HC Gram renderer'})
fig.savefig(out/'homogeneous-gram.svg',metadata={'Date':None,'Creator':'Original HC Gram renderer'})
plt.close(fig)
data={'model':'M2 plus M2, interchange action of Z/2','hilbert_dimension':4,'fiber_complex_dimension':4,'fiber_basis':basis,'chosen_x1':x1,'chosen_x2':x2,'support_diagonals':supports,'unitary_V':V,'character_values':{'0':1,'1':-1},'exact_integer_Gram_pairs_checked':16,'native_dimensions':[2800,2000],'general_panels':'Algebraic proof objects, not dimension or geometry claims.'}
(out/'homogeneous-gram-data.json').write_text(json.dumps(data,indent=2)+'\n',encoding='utf-8')
print('Exact16Gram-pair checks and figure generation passed')
