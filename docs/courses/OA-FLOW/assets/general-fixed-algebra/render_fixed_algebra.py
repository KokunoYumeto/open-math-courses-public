"""Exact original fixed-algebra example. CC0-1.0 to the extent of rights held."""
from pathlib import Path
import json
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch

ROOT = Path(__file__).resolve().parent
ASSETS = ROOT / "assets"
ASSETS.mkdir(exist_ok=True)
plt.rcParams.update({"font.family":"DejaVu Sans","font.size":16,
                     "svg.hashsalt":"NCF-20261005","svg.fonttype":"none"})
fig = plt.figure(figsize=(14,9),dpi=200,facecolor="#f4f7fb")
fig.suptitle("A fixed algebra contains more than its coefficients",
             fontsize=24,fontweight="bold",y=.963,color="#17344b")
fig.text(.5,.904,r"Exact example: $G=\mathbb{Z}/2$, $M=M_2(\mathbb{C})$, $\alpha_1=\mathrm{Ad}\,v$",
         ha="center",fontsize=18,color="#405b70")
ax = fig.add_axes([.045,.16,.49,.65]); ax.axis("off")
ax.set_xlim(0,1);ax.set_ylim(0,1)
def box(y,title,formula,color):
    ax.add_patch(FancyBboxPatch((.015,y),.94,.21,boxstyle="round,pad=.013",
                 facecolor=color,edgecolor="#9bb2c7",linewidth=1.5))
    ax.text(.485,y+.145,title,ha="center",fontsize=17,fontweight="bold",color="#17344b")
    ax.text(.485,y+.066,formula,ha="center",fontsize=17,color="#17344b")
box(.765,r"Ambient algebra: 16 complex dimensions",r"$P=M_4(\mathbb{C})$","#e7eef8")
box(.385,r"Full fixed algebra: 8 complex dimensions",r"$R=P^{\mathrm{Ad}\,D}$","#e4f3f1")
box(.025,r"Coefficient intersection: 4 complex dimensions",r"$R\cap Q=\pi(M_2(\mathbb{C}))$","#fff0d5")
for y,label in [(.75,r"Impose $DXD=X$"),(.37,r"Also impose $[X,E_0]=0$")]:
    ax.annotate("",xy=(.10,y-.12),xytext=(.10,y),
                arrowprops={"arrowstyle":"-|>","lw":2,"color":"#486f8e"})
    ax.text(.17,y-.077,label,fontsize=17,color="#405b70")

bx = fig.add_axes([.60,.26,.34,.51]);bx.set_title(r"A witness: $\lambda_1\in R$, $\lambda_1\notin Q$",
                                                fontsize=19,pad=24,color="#17344b")
v=np.array([[0,1],[1,0]],dtype=int);I=np.eye(2,dtype=int);Z=np.zeros((2,2),dtype=int)
D=np.block([[Z,v],[v,Z]]);lam=np.block([[Z,I],[I,Z]]);E0=np.diag([1,1,0,0])
comm=lam@E0-E0@lam
assert np.array_equal(D@lam@D,lam)
assert np.array_equal(comm,np.block([[Z,-I],[I,Z]]))
bx.imshow(lam,cmap="Blues",vmin=0,vmax=1,interpolation="nearest")
for (i,j),val in np.ndenumerate(lam):
    bx.text(j,i,str(int(val)),ha="center",va="center",fontsize=30,
            fontweight="bold",color="white" if val else "#17344b")
labels=[r"$(0,e_1)$",r"$(0,e_2)$",r"$(1,e_1)$",r"$(1,e_2)$"]
bx.set_xticks(range(4),labels,fontsize=13);bx.set_yticks(range(4),labels,fontsize=13)
bx.tick_params(length=0,pad=10)
bx.axhline(1.5,color="#7897af",lw=2);bx.axvline(1.5,color="#7897af",lw=2)
for s in bx.spines.values():s.set_color("#9bb2c7")
fig.text(.765,.155,r"$D\lambda_1D=\lambda_1$     but     $[\lambda_1,E_0]\ne0$",
         ha="center",fontsize=18,color="#405b70")
fig.text(.5,.065,"NCF2–3 recover the whole crossed product; GDA5 extracts its coefficient algebra.",
         ha="center",fontsize=16,color="#405b70")
data={"group":"Z/2 with counting Haar","coefficient_algebra":"M2(C)",
      "ordered_coordinates":["(0,e1)","(0,e2)","(1,e1)","(1,e2)"],
      "v":v.tolist(),"D":D.tolist(),"lambda1":lam.tolist(),"E0":E0.tolist(),
      "commutator_lambda1_E0":comm.tolist(),
      "complex_dimensions":{"ambient":16,"fixed_algebra":8,"coefficient_intersection":4},
      "fixed_block_relations":{"E":"v A v","C":"v B v"},
      "coefficient_additional_condition":"B=0",
      "dimensions":[2800,1800],"proof":"GENERAL_FIXED_ALGEBRA_PROOF.md NCF6",
      "license":"CC0-1.0 to the extent of rights held"}
(ROOT/"figure-data.json").write_text(json.dumps(data,indent=2)+"\n",encoding="utf-8",newline="\n")
fig.savefig(ASSETS/"fixed-algebra-distinction.png",dpi=200,
            metadata={"Software":"Original NCF finite example"})
fig.savefig(ASSETS/"fixed-algebra-distinction.svg",metadata={"Date":None,"Creator":"Original NCF finite example"})
svg=ASSETS/"fixed-algebra-distinction.svg"
svg.write_text(svg.read_text(encoding="utf-8"),encoding="utf-8",newline="\n")
plt.close(fig)
