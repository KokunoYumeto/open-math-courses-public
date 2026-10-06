"""Exact finite Weyl multiplicity and general onto-map mechanism; original CC0."""
from pathlib import Path
import json
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, Circle
D=Path(__file__).resolve().parent
OUT=D/"figures";OUT.mkdir(exist_ok=True)
plt.rcParams.update({"font.family":"DejaVu Sans","font.size":13,"svg.hashsalt":"OA-FLOW-WY-exact-multiplicity-v1"})
tau=lambda k:(3*k+1)%10
R=np.zeros((10,10),dtype=int)
for k in range(10):R[tau(k),k]=1
assert np.array_equal(R.T@R,np.eye(10,dtype=int))
S=[]
for s in range(5):
 a=np.zeros((5,5),dtype=int)
 for j in range(5):a[(j-s)%5,j]=1
 S.append(a)
U=[R@np.kron(s,np.eye(2,dtype=int))@R.T for s in S]
P=[];E={}
for i in range(5):
 p=np.zeros((10,10),dtype=int)
 for a in range(2):p[tau(2*i+a),tau(2*i+a)]=1
 P.append(p)
 for j in range(5):
  e=np.zeros((5,5),dtype=int);e[i,j]=1
  E[i,j]=R@np.kron(e,np.eye(2,dtype=int))@R.T
assert np.array_equal(sum(P),np.eye(10,dtype=int))
for i in range(5):
 for j in range(5):
  assert np.array_equal(E[i,j],P[i]@U[(j-i)%5])
  assert np.array_equal(E[i,j].T,E[j,i])
  for k in range(5):
   for l in range(5):assert np.array_equal(E[i,j]@E[k,l],E[i,l]if j==k else np.zeros((10,10),dtype=int))
# Verify every Weyl phase exponent on each basis vector in integer arithmetic.
for s in range(5):
 for n in range(5):
  for j in range(5):assert n*j%5==(n*s+n*((j-s)%5))%5
# The scalar root sum is delta_ij, as proved exactly in WY6; numerical crosscheck only.
omega=np.exp(2j*np.pi/5)
V=[R@np.kron(np.diag([omega**(n*j)for j in range(5)]),np.eye(2))@R.T for n in range(5)]
selector_error=max(np.linalg.norm(sum(omega**(-n*i)*V[n]for n in range(5))/5-P[i])for i in range(5))
assert selector_error<1e-13
for i in range(5):
 for a in range(2):
  v=np.eye(10,dtype=int)[:,tau(a)]
  assert np.array_equal(E[i,0]@v,np.eye(10,dtype=int)[:,tau(2*i+a)])
colors=["#1764a0","#d66d18"];dark="#16314a";gray="#e7edf2";green="#27854e"
fig=plt.figure(figsize=(15,12),dpi=200,facecolor="white")
fig.text(.05,.965,"Weyl multiplicity: extracting a fibre and rebuilding every vector",fontsize=23,weight="bold",color=dark)
fig.text(.05,.928,"An exact Z/5Z system on C¹⁰, followed by the arbitrary-Hilbert proof mechanism",fontsize=16,color=dark)
ax=fig.add_axes([.055,.69,.89,.18]);ax.set_xlim(-.6,9.6);ax.set_ylim(-.85,1.3);ax.axis("off")
ax.set_title("A. The physical coordinates are interlaced",loc="left",fontsize=17,color=dark,pad=12)
for k in range(10):
 original=next(j for j in range(10)if tau(j)==k);i,a=divmod(original,2)
 ax.add_patch(FancyBboxPatch((k-.37,.02),.74,.64,boxstyle="round,pad=.02",facecolor=colors[a],edgecolor=dark,lw=2 if i==0 else .5))
 ax.text(k,.34,f"h{k}",ha="center",va="center",color="white",fontsize=16,weight="bold")
 ax.text(k,-.21,f"i = {i}",ha="center",color=dark,fontsize=12)
 if i==0:ax.text(k,.84,"P₀",ha="center",color=green,weight="bold",fontsize=14)
ax.text(4.5,-.67,"Vₙ acts by ωⁿⁱ on fibre i;  P₀H = span{h₁, h₄}.  Colours record the two multiplicity coordinates.",ha="center",color=dark,fontsize=13)
ax=fig.add_axes([.055,.36,.89,.26]);ax.set_xlim(-1.45,4.55);ax.set_ylim(-.75,1.85);ax.axis("off")
ax.set_title("B. The onto map W recovers two copies with identical group actions",loc="left",fontsize=17,color=dark,pad=12)
for i in range(5):ax.text(i,1.68,f"i = {i}",ha="center",color=dark,fontsize=15)
for a,y in [(0,1.1),(1,.2)]:
 ax.text(-1.3,y,"η = h₁"if a==0 else"η = h₄",color=colors[a],va="center",fontsize=15)
 for i in range(5):
  ax.add_patch(Circle((i,y),.2,facecolor=colors[a],edgecolor="white",lw=1))
  ax.text(i,y,f"h{tau(2*i+a)}",ha="center",va="center",color="white",fontsize=13,weight="bold")
  if i>0:ax.annotate("",(i-1+.25,y),(i-.25,y),arrowprops={"arrowstyle":"->","color":colors[a],"lw":1.6})
 ax.annotate("",(4.08,y-.24),(-.07,y-.24),arrowprops={"arrowstyle":"->","connectionstyle":"arc3,rad=.05","color":colors[a],"lw":1.2,"linestyle":"dashed"})
ax.text(1.6,-.68,r"$W(\delta_i\otimes\eta)=\kappa(E_{i0})\eta=U_{-i}\eta$"+"     |     U₁ sends i to i−1 (mod 5)",ha="center",color=dark,fontsize=15)
ax=fig.add_axes([.055,.045,.89,.245]);ax.set_xlim(0,1);ax.set_ylim(0,1);ax.axis("off")
ax.set_title("C. Why the same construction is onto without a countable basis",loc="left",fontsize=17,color=dark,pad=12)
def box(x,y,w,h,text,color):
 ax.add_patch(FancyBboxPatch((x,y),w,h,boxstyle="round,pad=.012",facecolor="#f5f8fa",edgecolor=color,lw=1.5))
 ax.text(x+w/2,y+h/2,text,ha="center",va="center",fontsize=14,color=dark,linespacing=1.45)
box(.015,.46,.26,.42,r"$E=\theta_{e,e},\quad\|e\|=1$"+"\n"+r"$K=\kappa(E)H$"+"\n"+"One rank-one projection",colors[0])
box(.34,.46,.31,.42,r"$W(\xi\otimes\eta)=\kappa(\theta_{\xi,e})\eta$"+"\n"+r"$\langle W(\xi\otimes\eta),W(\zeta\otimes\nu)\rangle$"+"\n"+r"$=\langle\xi,\zeta\rangle\langle\eta,\nu\rangle$",green)
box(.715,.46,.27,.42,"Every rank-one image lies"+"\n"+r"in $\operatorname{Ran}W$."+"\n"+"Nondegeneracy ⇒ dense range;"+"\n"+"isometry ⇒ closed range.",colors[1])
for x0,x1 in [(.285,.325),(.66,.7)]:ax.annotate("",(x1,.67),(x0,.67),arrowprops={"arrowstyle":"->","color":dark,"lw":2})
ax.text(.5,.265,r"$\kappa(\theta_{\xi,\zeta})h=W\left(\xi\otimes\kappa(\theta_{e,\zeta})h\right)$",ha="center",color=dark,fontsize=17)
ax.text(.5,.10,"WY2–5: full L¹ integration → compact-operator representation → onto W → both Weyl actions",ha="center",color=dark,fontsize=13)
fig.savefig(OUT/"weyl-multiplicity.png",metadata={"Software":"OA-FLOW WY original CC0"})
fig.savefig(OUT/"weyl-multiplicity.svg",metadata={"Date":None,"Creator":"OA-FLOW WY original CC0"})
plt.close(fig)
data={"group":"Z/5Z","Haar":"counting","dual_point_mass":"1/5","multiplicity":2,"omega":"exp(2*pi*i/5)","tau":[tau(k)for k in range(10)],"fibres":[[tau(2*i+a)for a in range(2)]for i in range(5)],"right_translation":"S_s delta_j=delta_(j-s mod5)","positive_Weyl_relation":"U_s V_n=omega^(ns) V_n U_s","P0_coordinates":[1,4],"all_matrix_units":[{"i":i,"j":j,"matrix":E[i,j].tolist()}for i in range(5)for j in range(5)],"exact_matrix_products_checked":625,"exact_adjoints_checked":25,"exact_Weyl_phase_exponents_checked":125,"numerical_selector_error":float(selector_error),"general_panel":"arbitrary-Hilbert proof mechanism, not a finite-to-general inference"}
(OUT/"weyl-multiplicity-data.json").write_text(json.dumps(data,ensure_ascii=False,indent=2)+"\n",encoding="utf-8",newline="\n")
print(json.dumps({"dimensions":[3000,2400],"matrix_products":625,"Weyl_phase_exponents":125,"selector_numeric_error":float(selector_error)}))
