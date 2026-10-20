"""Reproduce the exact bimodule, cokernel and finite tensor diagram."""
from pathlib import Path
import argparse,json
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch

parser=argparse.ArgumentParser()
parser.add_argument("--output-dir",type=Path,default=Path(__file__).parent)
out=parser.parse_args().output_dir
out.mkdir(parents=True,exist_ok=True)
plt.rcParams.update({"font.family":"DejaVu Sans","font.size":16,
                     "svg.hashsalt":"special-tensor-transfer-ST-v1"})
fig=plt.figure(figsize=(16,11),dpi=150,facecolor="#f5f8fc")
ax=fig.add_axes([0,0,1,1])
ax.set_xlim(0,1);ax.set_ylim(0,1);ax.axis("off")
ink="#19334c";blue="#205d99";green="#16715c";muted="#52677f"
ax.text(.5,.954,"Special kernels and finite algebraic tensors",
        ha="center",color=ink,fontsize=25)
ax.text(.5,.912,r"Independent normal variables $u,s$; shared spatial variables $x$",
        ha="center",color=muted,fontsize=17)
def arrow(x1,y1,x2,y2,color=blue):
    ax.annotate("",xy=(x2,y2),xytext=(x1,y1),
                arrowprops={"arrowstyle":"->","lw":2,"color":color})
def row(y,labels):
    positions=[.06,.23,.49,.77,.95]
    for x,label in zip(positions,labels):
        ax.text(x,y,label,ha="center",va="center",color=ink,fontsize=20)
    for a,b in zip(positions[:-1],positions[1:]):
        arrow(a+.045,y,b-.055,y)
row(.816,["0",r"$R$",r"$T$",r"$\mathcal{J}$","0"])
ax.text(.5,.76,"Exact sequence of R–R bimodules; ST.11",
        ha="center",color=muted)
row(.673,["",r"$N_1$",r"$T\otimes_R N_1$",r"$\mathcal{J}\otimes_R N_1$","0"])
row(.497,["",r"$N_2$",r"$T\otimes_R N_2$",r"$\mathcal{J}\otimes_R N_2$","0"])
# Only the last three arrows belong to the two right-exact tensor rows.
# Blank first entries have no mathematical role; cover those drawn arrows.
for y in [.673,.497]:
    ax.add_patch(FancyBboxPatch((.102,y-.018),.077,.036,boxstyle="square,pad=0",
                              fc="#f5f8fc",ec="#f5f8fc",zorder=8))
for x,label in [(.23,r"$\varphi$"),(.49,r"$T\otimes\varphi$"),
                (.77,r"$\mathcal{J}\otimes\varphi$")]:
    arrow(x,.634,x,.537,green)
    ax.text(x+.018,.586,label,ha="left",va="center",color=green,fontsize=15)
ax.text(.5,.431,"Both tensor rows are right exact; the first arrows need not be injective.",
        ha="center",color=muted,fontsize=15)
ax.add_patch(FancyBboxPatch((.055,.23),.89,.152,boxstyle="round,pad=.015",
                          fc="white",ec="#b5cbdc",lw=1.4))
ax.text(.5,.34,r"$C=A/AD_u,\qquad \mathcal{J}=A/(AD_u+D_sA)$",
        ha="center",color=ink,fontsize=20)
ax.text(.5,.276,r"$\mathcal{J}\otimes_R N \ \simeq\ (C\otimes_R N)/D_s(C\otimes_R N)$",
        ha="center",color=blue,fontsize=20)
ax.text(.5,.177,r"$\mathcal{J}\otimes\varphi=0"
        r"\quad\Longleftrightarrow\quad"
        r"\mathrm{im}(T\otimes\varphi)\subseteq\mathrm{im}(1\otimes N_2)$",
        ha="center",color=green,fontsize=19)
ax.text(.5,.111,r"$\sigma(P)_\beta=\sum_{l\geq0}(-\partial_s)^l a_{0,l,\beta}$",
        ha="center",color=ink,fontsize=20)
ax.text(.5,.056,"ST.2, ST.12–ST.19. Exact algebraic diagram; no geometric scale.",
        ha="center",color=muted,fontsize=15)
fig.savefig(out/"special-tensor-transfer.png",metadata={"Software":"Matplotlib"})
fig.savefig(out/"special-tensor-transfer.svg",metadata={"Date":None})
plt.close(fig)
data={"normal_coordinates":["u","s"],"spatial_coordinates":"x_1,...,x_d",
      "rings":{"R":"D_X^infinity","A":"D_Y^infinity","T":"chosen-fibration decorated E^infinity"},
      "first_row":["0","R","T","J","0"],"first_row_exact":True,
      "tensor_rows":[["N_1","T tensor_R N_1","J tensor_R N_1","0"],
                     ["N_2","T tensor_R N_2","J tensor_R N_2","0"]],
      "tensor_rows_right_exact":True,"first_tensor_arrows_injective_required":False,
      "cokernel":"J tensor_R N = (C tensor_R N)/D_s(C tensor_R N)",
      "coefficient_projection":"sum_l (-partial_s)^l a_0,l,beta",
      "image_criterion":"ST.16","finite_witnesses":["ST.18","ST.19"],
      "geometric_scale":None,"human_source":"Kashiwara–Kawai HolIII III.4.9 pp.898–899"}
(out/"special-tensor-transfer-data.json").write_text(
    json.dumps(data,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
