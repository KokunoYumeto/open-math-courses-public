from pathlib import Path
from fractions import Fraction as Q
import json
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

D=Path(__file__).resolve().parent
out=D/"assets";out.mkdir(exist_ok=True)
plt.rcParams.update({"font.family":"DejaVu Sans","font.size":12,
                    "svg.hashsalt":"oa-flow-fourier-minorants-20261005",
                    "axes.titleweight":"bold","axes.spines.top":False,
                    "axes.spines.right":False})
k=[Q(1,4),Q(1,2),Q(3,4)]
x=[Q(2),Q(5),Q(9)]
C=[[k[(j-l)%3]/6 for l in range(3)] for j in range(3)]
y=[sum(C[j][l]*x[l] for l in range(3)) for j in range(3)]
t=sum(x)/6
assert y==[Q(35,24),Q(3,2),Q(25,24)] and t==Q(8,3)
assert all(sum(row)==Q(1,4) for row in C)
data={"group":"Z/3Z","original_singleton_haar_mass":"2",
      "dual_singleton_haar_mass":"1/6","theta_m_coordinate":"(theta_m x)_j=x_(j-m)",
      "k":[str(q) for q in k],"x":[str(q) for q in x],
      "weighted_orbit_matrix":[[str(q) for q in row] for row in C],
      "H_k_x":[str(q) for q in y],"T_x":[str(t)]*3,
      "T_identity":"1/2","H_k_identity":"1/4",
      "strict_majorant_c":"3/4",
      "p_coefficients":["1/4","-1/16+i sqrt(3)/48","-1/16-i sqrt(3)/48"],
      "general_proof":"FOURIER_MINORANT_BRIDGE.md AM1–3; DUAL_ACTION_AVERAGING_RESTORED.md A4/A40–42",
      "scope":"Exact finite illustration; the arbitrary-group/full-cone proof is separate."}
(out/"fourier-minorants-data.json").write_text(json.dumps(data,indent=2)+"\n",encoding="utf-8",newline="\n")

fig=plt.figure(figsize=(14,10),facecolor="#fbfcfe")
fig.suptitle("A bounded Fourier density and the whole positive average",fontsize=21,x=.06,ha="left",y=.966)
fig.text(.06,.924,r"Exact example: $G=\mathbb{Z}/3\mathbb{Z}$, $ds(\{s\})=2$, $d\chi(\{\chi_m\})=1/6$, $M=\mathbb{C}$",
         fontsize=13,color="#34495e")
grid=fig.add_gridspec(2,2,left=.075,right=.955,bottom=.085,top=.862,hspace=.43,wspace=.27,height_ratios=[1,1.03])
blue="#2466a6";orange="#d4742c";green="#187b69";ink="#19324a"

ax=fig.add_subplot(grid[0,0])
ax.set_title("1  Strict density on the three dual points",loc="left",pad=16,fontsize=14)
ax.bar(range(3),[float(q) for q in k],color=blue,width=.55)
ax.axhline(.75,color=orange,ls="--",lw=1.8)
ax.text(.05,.87,r"$c=3/4<1$",ha="left",color=orange,fontsize=13)
for j,q in enumerate(k):ax.text(j,float(q)+.025,"$"+str(q)+"$",ha="center",fontsize=14,color=ink)
ax.set_ylim(0,1.02);ax.set_xticks(range(3),[r"$\chi_0$",r"$\chi_1$",r"$\chi_2$"])
ax.set_yticks([0,.25,.5,.75,1],["0","1/4","1/2","3/4","1"])
ax.set_ylabel(r"$k(\chi_m)$");ax.grid(axis="y",alpha=.14);ax.set_axisbelow(True)
ax.text(.02,-.24,r"$p(s)=\frac{1}{6}\sum_{m=0}^2 k_m\,e^{-2\pi i ms/3}$",transform=ax.transAxes,fontsize=14)

ax=fig.add_subplot(grid[0,1])
ax.set_title("2  The bounded map need not have fixed values",loc="left",pad=16,fontsize=14)
ax.bar(range(3),[float(q) for q in y],color=blue,width=.52,label=r"$H_k(x)=E_p(x)$")
ax.axhline(float(t),color=green,lw=2.1,label=r"$T(x)=(8/3,8/3,8/3)$")
for j,q in enumerate(y):ax.text(j,float(q)+.07,"$"+str(q)+"$",ha="center",fontsize=14,color=ink)
ax.text(2.3,float(t)+.06,r"$8/3$",ha="right",color=green,fontsize=14)
ax.set_ylim(0,3.2);ax.set_xticks(range(3),[r"$j=0$",r"$j=1$",r"$j=2$"]);ax.set_ylabel("output coordinate")
ax.grid(axis="y",alpha=.14);ax.set_axisbelow(True);ax.legend(frameon=False,fontsize=11,loc="upper left")
ax.text(.02,-.24,r"$x=(2,5,9),\qquad(\theta_mx)_j=x_{j-m}$",transform=ax.transAxes,fontsize=14)

ax=fig.add_subplot(grid[1,0]);ax.axis("off")
ax.set_title("3  Every finite coefficient is explicit",loc="left",pad=16,fontsize=14)
labels=[["$j="+str(j)+"$"]+["$"+str(q)+"$" for q in row] for j,row in enumerate(C)]
table=ax.table(cellText=labels,colLabels=["output",r"$x_0$",r"$x_1$",r"$x_2$"],cellLoc="center",
               bbox=[.03,.39,.89,.52])
table.auto_set_font_size(False);table.set_fontsize(16)
for (i,j),cell in table.get_celld().items():
    cell.set_edgecolor("#ccd8e4")
    cell.set_facecolor("#eaf1f8" if i==0 or j==0 else "white")
ax.text(.05,.24,r"$(H_kx)_j=\sum_{\ell=0}^2\frac{k_{j-\ell}}{6}\,x_\ell$",fontsize=15,color=ink)
ax.text(.05,.11,r"$H_k(1)=1/4,\qquad T(1)=1/2$",fontsize=15,color=ink)
ax.text(.05,-.015,"The canonical weight is not the probability average.",fontsize=11.5,color="#526579")

ax=fig.add_subplot(grid[1,1]);ax.axis("off")
ax.set_title("4  The proof compares complete positive values",loc="left",pad=16,fontsize=14)
items=[
(.86,r"$\mathcal{D}=\{k\in L^1_+: k\leq c<1\}$",ink),
(.68,r"$E_p=H_k,\qquad T(X)=\sup_{k\in\mathcal{D}}H_k(X)$",blue),
(.48,r"$(1-\varepsilon)A_K(X)\ \leq\ T(X)\ \leq\ A(X)$",green),
(.29,r"$\varepsilon\downarrow0,\quad K\ \mathrm{compact}:\qquad T(X)=A(X)$",green),
]
for yy,text,col in items:ax.text(.01,yy,text,fontsize=14,color=col)
ax.text(.01,.08,"All comparisons use normal positive functionals.\nInfinite values and uncountable compact-set nets remain included.",
        fontsize=11.2,color="#526579",linespacing=1.6)
fig.text(.06,.026,"Finite data above are exact. General proof: AM1–3; full finite domains: A40–42. Original illustration, CC0.",fontsize=10.8,color="#526579")
fig.savefig(out/"fourier-minorants.png",dpi=200,metadata={"Software":"OA-FLOW original deterministic renderer"})
fig.savefig(out/"fourier-minorants.svg",metadata={"Date":None})
plt.close(fig)
print(json.dumps(data,indent=2))
