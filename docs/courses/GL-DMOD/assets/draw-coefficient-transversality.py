"""Reproduce the bar, signed comparison and dual-number diagrams."""
from pathlib import Path
import json
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch
r=Path(__file__).resolve().parent
plt.rcParams.update({"font.family":"DejaVu Sans","font.size":13,
 "mathtext.fontset":"dejavusans","svg.hashsalt":"coefficient-transversality-CT-20261020"})
fig,axes=plt.subplots(3,1,figsize=(4.8,8.8))
blue="#164d78";teal="#087d76";orange="#b96517";ink="#17283a"
for ax in axes:
 ax.set_xlim(0,1);ax.set_ylim(0,1);ax.axis("off")
 ax.add_patch(FancyBboxPatch((.02,.03),.96,.93,boxstyle="round,pad=0.01",
  facecolor="#f6f9fc",edgecolor="#c4d2df",linewidth=1.2))
def txt(ax,x,y,s,**kw):ax.text(x,y,s,ha="center",va="center",color=ink,**kw)
def arr(ax,a,b,col=blue):
 ax.annotate("",xy=b,xytext=a,arrowprops={"arrowstyle":"->","color":col,"lw":1.6})
a=axes[0]
txt(a,.5,.88,"Split bar resolution · CT.4",fontsize=14,weight="bold")
for x,y,label in [(.22,.59,r"$L_{q+1}$"),(.52,.59,r"$L_q$"),(.81,.59,r"$L_{q-1}$")]:
 txt(a,x,y,label,fontsize=19)
arr(a,(.31,.62),(.43,.62));arr(a,(.61,.62),(.72,.62))
arr(a,(.43,.50),(.31,.50),teal);arr(a,(.72,.50),(.61,.50),teal)
txt(a,.37,.72,r"$d_{q+1}$",fontsize=12)
txt(a,.67,.72,r"$d_q$",fontsize=12)
txt(a,.37,.43,r"$h_q$",fontsize=12)
txt(a,.67,.43,r"$h_{q-1}$",fontsize=12)
txt(a,.5,.27,r"$d_{q+1}h_q+h_{q-1}d_q=1$",fontsize=16)
txt(a,.5,.12,"continuous scalar homotopy",fontsize=12)
a=axes[1]
txt(a,.5,.88,"Signed comparison · CT.23",fontsize=14,weight="bold")
txt(a,.5,.66,r"$D(x,y)=(d_Kx,\;fx-d_Jy)$",fontsize=15)
txt(a,.5,.44,r"$f\,d_K-d_Jf=0$",fontsize=18)
txt(a,.5,.25,r"$H^q(f)$ isomorphism for $q\geq k$",fontsize=12)
txt(a,.5,.11,r"$H^{k-1}(f)$ surjective",fontsize=12)
a=axes[2]
txt(a,.5,.88,"Dual numbers · CT.35–36",fontsize=14,weight="bold")
txt(a,.5,.70,r"$A=\mathbf{C}[\epsilon]/(\epsilon^2)$",fontsize=17)
txt(a,.5,.55,r"$B=A/(\epsilon),\quad I=\epsilon A$",fontsize=15)
txt(a,.25,.35,r"$B\widehat\otimes_A I$",fontsize=17)
txt(a,.77,.35,r"$B\widehat\otimes_A A$",fontsize=17)
arr(a,(.43,.35),(.60,.35),orange)
txt(a,.52,.46,r"$0$",fontsize=14)
txt(a,.5,.13,r"$\widehat{\mathrm{Tor}}^A_q(B,B)=B\ne0$",fontsize=16)
fig.subplots_adjust(left=.035,right=.965,top=.99,bottom=.01,hspace=.12)
fig.savefig(r/"coefficient-transversality.png",dpi=180,metadata={"Software":"Matplotlib"})
fig.savefig(r/"coefficient-transversality.svg",metadata={"Date":None})
plt.close(fig)
(r/"coefficient-transversality-exact-data.json").write_text(json.dumps({
 "proof_locators":["CT.4","CT.23--CT.25","CT.35--CT.36"],
 "bar_identity":"d_(q+1) h_q + h_(q-1) d_q = identity",
 "comparison":{"terms":"K^q direct_sum J^(q-1)",
  "differential":"(d_K x, f x - d_J y)","mixed_square":"f d_K - d_J f = 0",
  "range":"isomorphism q>=k, surjection q=k-1"},
 "dual_numbers":{"algebra":"C[epsilon]/epsilon^2","B":"A/(epsilon)","I":"epsilon A",
  "target_map":"B tensor_A I -> B tensor_A A is zero",
  "both_spaces":"B","Tor_q":"B for every q>=0"},
 "geometric_scale":None},ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
