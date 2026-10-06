"""CC0. Exact Z12 Fourier data and a reproducible explanatory figure."""
from pathlib import Path
from fractions import Fraction
import json, hashlib, math
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch
D=Path(__file__).resolve().parent; OUT=D/"figures"; OUT.mkdir(exist_ok=True)
plt.rcParams.update({"font.family":"DejaVu Sans","font.size":11,
    "svg.hashsalt":"oa-flow-general-lca-local-fourier-lf8","axes.titlesize":14,
    "axes.labelsize":11,"savefig.facecolor":"#f7f9fc"})
N=12; V={0,1,2}; O={11,0,1,2,3}
qfrac=[Fraction(sum((n+v)%N in O for v in V),len(V)) for n in range(N)]
q=np.array([float(v) for v in qfrac])
s=np.arange(N); n=np.arange(N)
inverse=np.exp(2j*np.pi*np.outer(s,n)/N)/N
k=inverse@q
assert np.max(np.abs(k.imag))<2e-15
k=k.real
expected=np.array([5/12,(5+3*math.sqrt(3))/36,1/18,-1/36,0,
    (5-3*math.sqrt(3))/36,-1/36,(5-3*math.sqrt(3))/36,0,-1/36,
    1/18,(5+3*math.sqrt(3))/36])
assert np.max(np.abs(k-expected))<2e-15
forward=np.exp(-2j*np.pi*np.outer(n,s)/N)
assert np.max(np.abs(forward@k-q))<8e-15
norm_exact=(11+6*math.sqrt(3))/18
assert abs(np.abs(k).sum()-norm_exact)<2e-15
assert abs(k.sum()-1)<2e-15
a=np.zeros(N); a[0]=1; a[1]=.25
ahat=forward@a; c=1.25
b=.25*(np.roll(k,1)-k)
Dhat=c+(ahat-c)*q
assert np.max(np.abs(forward@b-(ahat-c)*q))<2e-15
assert np.abs(b).sum()/c <= (2/5)*math.sqrt(5/3)
plateau=[11,0,1]
assert np.max(np.abs(Dhat[plateau]-ahat[plateau]))<2e-15
assert np.min(np.abs(Dhat))>0
data={
 "license":"CC0","group":"Z/12Z","physical_Haar":"counting","dual_Haar_mass":"1/12",
 "forward_sign":"negative","inverse_sign":"positive","V":[0,1,2],"O":[-1,0,1,2,3],
 "q_exact":[str(v) for v in qfrac],
 "k_exact":["5/12","(5+3*sqrt(3))/36","1/18","-1/36","0",
            "(5-3*sqrt(3))/36","-1/36","(5-3*sqrt(3))/36","0","-1/36",
            "1/18","(5+3*sqrt(3))/36"],
 "k_numerical":k.tolist(),"k_norm_exact":"(11+6*sqrt(3))/18",
 "k_norm_numerical":float(np.abs(k).sum()),"proved_k_norm_bound":"sqrt(5/3)",
 "a_exact":{"0":"1","1":"1/4"},"c_exact":"5/4",
 "b_norm_over_c_numerical":float(np.abs(b).sum()/c),
 "proved_Neumann_ratio_bound":"(2/5)*sqrt(5/3) < 1",
 "Dhat_formula":"5/4 + (1 + exp(-2*pi*i*n/12)/4 - 5/4)*q(n)",
 "Dhat_numerical":[[float(z.real),float(z.imag)] for z in Dhat],
 "numerical_verification_tolerance":8e-15,
 "schematic_scope":"arbitrary LCH abelian G; neighbourhood nets and finite Radon tails; no arbitrary closed-set synthesis"}
(OUT/"local-fourier-data.json").write_text(json.dumps(data,indent=2)+"\n",encoding="utf-8")
fig=plt.figure(figsize=(15,11),dpi=200,facecolor="#f7f9fc")
gs=fig.add_gridspec(2,2,left=.07,right=.95,bottom=.14,top=.88,hspace=.39,wspace=.28)
fig.suptitle("Local Fourier division: compact dual plateaus control a physical convolution error",
             fontsize=19,fontweight="bold",x=.5,y=.965)
fig.text(.5,.918,"Exact finite model: counting Haar on Z/12Z, dual mass 1/12; general proof: LF0–LF7",
         ha="center",fontsize=12,color="#42556c")
blue="#2765ab"; green="#168471"; orange="#bd662c"; gray="#c8d1dc"; purple="#7851a9"
ax=fig.add_subplot(gs[0,0]); labels=np.arange(-5,7); vals=q[labels%N]
colors=[green if v==1 else orange if v else gray for v in vals]
ax.bar(labels,vals,color=colors,width=.66,zorder=3)
ax.scatter([-1,0,1,2,3],[1.38]*5,s=32,color=blue,zorder=4)
ax.scatter([0,1,2],[1.20]*3,s=32,color=purple,zorder=4)
ax.text(-4.8,1.38,r"$O=\{-1,0,1,2,3\}$",va="center",color=blue,fontsize=11)
ax.text(-4.8,1.20,r"$V=\{0,1,2\}$",va="center",color=purple,fontsize=11)
ax.set(xlim=(-5.7,6.7),ylim=(0,1.54),xticks=labels,yticks=[0,1/3,2/3,1],
       yticklabels=["0","1/3","2/3","1"],xlabel=r"Dual index $n$ (modulo twelve)",ylabel=r"$q(n)$")
ax.set_title("A. A plateau from overlap counts",loc="left",pad=13,fontweight="bold")
ax.grid(axis="y",alpha=.2,zorder=0)
ax.text(.5,-.22,r"$q(n)=\#\{v\in V:n+v\in O\}/3$; plateau at $-1,0,1$",
        transform=ax.transAxes,ha="center",fontsize=11)
ax=fig.add_subplot(gs[0,1])
ax.bar(s,k,width=.66,color=[blue if v>=-1e-15 else orange for v in k],zorder=3)
ax.axhline(0,color="#6f8192",linewidth=.8)
ax.set(xticks=s,xlabel=r"Physical index $s$",ylabel=r"$k(s)$",ylim=(-.065,.46))
ax.set_title("B. Its signed physical kernel",loc="left",pad=13,fontweight="bold")
ax.grid(axis="y",alpha=.2,zorder=0)
ax.text(.5,-.22,r"$\sum_s k(s)=1,\qquad\|k\|_1=(11+6\sqrt{3})/18\leq\sqrt{5/3}$",
        transform=ax.transAxes,ha="center",fontsize=11)
ax=fig.add_subplot(gs[1,0]); theta=np.linspace(0,2*np.pi,400)
ax.plot(1+.25*np.cos(theta),-.25*np.sin(theta),color=gray,linewidth=1.5)
ax.scatter(ahat.real,ahat.imag,color=purple,s=36,label=r"$\widehat a(n)$",zorder=3)
ax.plot(Dhat.real,Dhat.imag,linestyle=":",linewidth=1,color=blue)
ax.scatter(Dhat.real,Dhat.imag,color=blue,s=28,label=r"$\widehat D(n)$",zorder=4)
ax.scatter(ahat[plateau].real,ahat[plateau].imag,facecolors="none",edgecolors=green,
           s=125,linewidths=2,zorder=5,label=r"$q(n)=1$: equality")
for nn in [-3,-2,-1,1,2,3]:
    z=Dhat[nn%N]; ax.annotate(str(nn),(z.real,z.imag),xytext=(7,5 if nn<0 else -12),
                            textcoords="offset points",fontsize=9,color=blue)
ax.annotate(r"$c=5/4$",(c,0),xytext=(c-.09,.25),
            arrowprops={"arrowstyle":"->","color":"#42556c"},ha="center")
ax.set(xlim=(.70,1.37),ylim=(-.30,.35),xlabel="Real part",ylabel="Imaginary part")
ax.set_aspect("equal",adjustable="box")
ax.set_title("C. A genuine Neumann denominator",loc="left",pad=13,fontweight="bold")
ax.legend(loc="upper left",fontsize=9,frameon=False)
ax.grid(alpha=.17)
ax.text(.5,-.24,r"$\widehat D=c+(\widehat a-c)q,\quad\|b/c\|_1\leq(2/5)\sqrt{5/3}<1$",
        transform=ax.transAxes,ha="center",fontsize=10.8)
ax=fig.add_subplot(gs[1,1]); ax.axis("off")
ax.set_title("D. General-LCA mechanism (schematic)",loc="left",pad=13,fontweight="bold")
def box(x,y,w,h,text,color):
    patch=FancyBboxPatch((x,y),w,h,boxstyle="round,pad=.013,rounding_size=.025",
                        linewidth=1.1,edgecolor=color,facecolor="white",transform=ax.transAxes)
    ax.add_patch(patch); ax.text(x+w/2,y+h/2,text,ha="center",va="center",
                              transform=ax.transAxes,fontsize=10.7,color="#23384d")
def arrow(x1,y1,x2,y2):
    ax.annotate("",xy=(x2,y2),xytext=(x1,y1),xycoords="axes fraction",
                arrowprops={"arrowstyle":"->","color":"#566d85","lw":1.4})
box(.06,.78,.88,.16,"LF1–2: small dual support, uniform A-norm\ncompact-uniform translation error + finite Radon tails",blue)
box(.06,.53,.88,.16,"LF3:  b = a*k − c k,  ||b||₁ < |c|\nNeumann inverse gives division on the plateau",blue)
box(.02,.27,.45,.16,"LF4: finite A-partitions\nlocal ideal membership",green)
box(.53,.27,.45,.16,"LF5: compact-frequency density\npreserves closed support",green)
box(.06,.02,.88,.15,"LF6: neighbourhood vanishing implies membership\nempty hull forces I = A(Γ)",purple)
arrow(.5,.78,.5,.69); arrow(.5,.53,.245,.43); arrow(.5,.53,.755,.43)
arrow(.245,.27,.39,.17); arrow(.755,.27,.61,.17)
fig.text(.5,.019,"Closed-set pointwise vanishing alone is not the hypothesis of LF6.  Full objects, constants and domains: complete caption + proof.",
         ha="center",fontsize=10.5,color="#42556c")
fig.savefig(OUT/"local-fourier.png",metadata={"Software":"OA-FLOW CC0 local Fourier reproduction"})
fig.savefig(OUT/"local-fourier.svg",metadata={"Date":None,"Creator":"OA-FLOW CC0 local Fourier reproduction"})
plt.close(fig)
print(json.dumps({p.name:hashlib.sha256(p.read_bytes()).hexdigest()
                  for p in sorted(OUT.iterdir()) if p.is_file()},indent=2))
