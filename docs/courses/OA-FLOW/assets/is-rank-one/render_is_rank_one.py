"""Original CC0-1.0 figure for the full rank-one transformation proof."""
from pathlib import Path
from fractions import Fraction as Q
import json
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
HERE=Path(__file__).resolve().parent
plt.rcParams.update({"font.family":"DejaVu Sans","font.size":13,"svg.hashsalt":"oa-flow-is-rank-one-v1"})
u=[Q(1),Q(0),Q(0)];v=[Q(3,5),Q(4,5),Q(0)]
w=[Q(4,5),Q(0),Q(3,5)];z=[Q(0),Q(1),Q(0)]
def outer(a,b):return [[x*y for y in b] for x in a]
def mm(a,b):return [[sum(a[i][k]*b[k][j] for k in range(3)) for j in range(3)] for i in range(3)]
def trans(a):return list(map(list,zip(*a)))
E=outer(u,v);F=outer(w,z);c=sum(x*y for x,y in zip(w,v))
P=mm(E,F);assert c==Q(12,25) and P==[[c*x for x in row] for row in outer(u,z)]
R=[[Q(int(j==(i+1)%3)) for j in range(3)] for i in range(3)]
Ru=u[1:]+u[:1];Rv=v[1:]+v[:1]
T=mm(mm(R,E),trans(R));assert T==outer(Ru,Rv)
INK="#17354e";TEAL="#087f8c";ORANGE="#bd6524"
fig=plt.figure(figsize=(15,10.2),dpi=180,facecolor="white")
fig.suptitle("Rank-one kernels determine the whole operator factor",fontsize=23,color=INK,y=.985)
fig.text(.5,.94,r"Exact images under $\Phi$: $G=\mathbb{Z}/3\mathbb{Z}$ with counting Haar measure; general construction below.",ha="center",color=INK,fontsize=14)
grid=fig.add_gridspec(2,3,left=.06,right=.96,top=.85,bottom=.39,hspace=1.05,wspace=.58)
def heat(ax,a,title):
 arr=np.array([[float(x) for x in row] for row in a])
 ax.imshow(arr,vmin=0,vmax=1,cmap="Blues")
 for i in range(3):
  for j in range(3):ax.text(j,i,str(a[i][j]),ha="center",va="center",color="white" if arr[i,j]>.55 else INK,fontsize=15)
 ax.set_xticks(range(3));ax.set_yticks(range(3));ax.set_xlabel("input index");ax.set_ylabel("output index")
 ax.set_title(title,pad=10,color=INK,fontsize=16)
heat(fig.add_subplot(grid[0,0]),E,r"$\Phi(E_{u,v})=|u\rangle\langle v|$")
heat(fig.add_subplot(grid[0,1]),F,r"$\Phi(E_{w,z})=|w\rangle\langle z|$")
heat(fig.add_subplot(grid[0,2]),P,r"$\Phi(E_{u,v}E_{w,z})=\frac{12}{25}|u\rangle\langle z|$")
fig.text(.5,.615,r"$u=(1,0,0),\quad v=(3/5,4/5,0),\quad w=(4/5,0,3/5),\quad z=(0,1,0)$",ha="center",fontsize=14,color=INK)
heat(fig.add_subplot(grid[1,0]),R,r"Right shift: $(R\xi)_j=\xi_{j+1}$")
heat(fig.add_subplot(grid[1,1]),T,r"$R\Phi(E_{u,v})R^*$")
heat(fig.add_subplot(grid[1,2]),outer(Ru,Rv),r"$\Phi(E_{Ru,Rv})$")
fig.text(.5,.29,r"Kernel composition contracts the middle vectors: $\langle w,v\rangle=12/25$.  IS41–43",ha="center",color=INK,fontsize=15)
fig.text(.5,.25,r"Right translation transports both vectors; in general each carries $\Delta_G(h)^{1/2}$.  IS47",ha="center",color=INK,fontsize=14)
fig.text(.5,.19,r"General Hilbert space: $U:L^2(G)\otimes\mathcal{H}_e\longrightarrow\mathcal{H},\qquad U(\eta\otimes\xi)=E_{\eta,e}\xi$",ha="center",color=INK,fontsize=17)
fig.text(.5,.14,r"$E_{u,v}\ \longleftrightarrow\ |u\rangle\langle v|\otimes I_{\mathcal{H}_e},\qquad P_F=\sum_{j=1}^{\dim F}E_{u_j,u_j}\ \overset{\mathrm{strong}}{\longrightarrow}\ I$",ha="center",color=TEAL,fontsize=18)
fig.text(.5,.085,r"Finite subspaces $F\subset C_c(G)$ exhaust a dense span.  The proof establishes full support and normality.  IS44–46",ha="center",color=INK,fontsize=13)
fig.text(.5,.035,"The matrices are exact scalar-factor examples. No finite dimension or separability is imposed on the coefficient algebra.",ha="center",color=INK,fontsize=12.5)
fig.savefig(HERE/"is-rank-one.png",dpi=180,metadata={"Software":"Original CC0 matplotlib proof figure"})
fig.savefig(HERE/"is-rank-one.svg",metadata={"Date":None,"Creator":"Original CC0 mathematical figure"})
plt.close(fig)
data={"group":"Z/3Z","measure":"counting Haar","inner_product":"linear in first variable","vectors":{k:[str(x) for x in a] for k,a in [("u",u),("v",v),("w",w),("z",z)]},"overlap":str(c),"matrix_interpretation":"Images under Phi in B(L2G); regular operators have the additional identity factor.","matrices":{k:[[str(x) for x in row] for row in a] for k,a in [("E_uv",E),("E_wz",F),("product",P),("right_shift_R",R),("conjugated_E",T)]},"identities_exact":True,"proof_locators":["IS41","IS43","IS44","IS45","IS46","IS47"],"limits":"Finite example checks the algebraic identities. Full-support and arbitrary-coefficient statements are proved in the lesson, not inferred numerically.","licence":"CC0-1.0 to the extent of rights held"}
(HERE/"rank-one-data.json").write_text(json.dumps(data,indent=2)+"\n",encoding="utf8")
