"""Reproducible exact-coordinate illustration for W.4--W.7; original CC0."""
from pathlib import Path
import json, hashlib
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle, FancyArrowPatch

root=Path(__file__).resolve().parent
plt.rcParams.update({"font.family":"DejaVu Sans","font.size":11})
fig,(ax,bx)=plt.subplots(1,2,figsize=(14.5,6),gridspec_kw={"width_ratios":[1.15,1]})
fig.subplots_adjust(top=.87,bottom=.16,wspace=.24,left=.06,right=.97)
fig.suptitle("The residual complement term survives the proper trace",fontsize=17)
ax.axvspan(-2.1,0,color="#e6f4ee")
ax.axvspan(0,.48,color="#eee9f5")
ax.axvline(0,color="#604389",linewidth=1.6)
ax.add_patch(Rectangle((-1.95,-.15),1.30,.30,fill=False,edgecolor="#227764",
                       linewidth=1.5,linestyle="--"))
ax.add_patch(Rectangle((-1.6,-.125),.60,.25,facecolor="#f2bd64",
                       edgecolor="none",alpha=.48))
ax.text(-1.8,.255,r"$\Omega=\{\mathrm{Re}\,s<0\}$",color="#246651")
ax.text(.23,.255,r"$Z$",color="#604389",ha="center")
ax.text(-1.30,-.26,r"$\mathrm{supp}\,\theta'\Subset\Omega$",ha="center",color="#9a5d15")
ax.text(-1.30,-.31,"Only this compact tube is used by E.",ha="center",fontsize=10)
L,a0,im,tout=-1.8,-.8,.10,-.20
ax.plot([L,tout],[im,im],color="#177a72",linewidth=3)
ax.add_patch(FancyArrowPatch((-.58,im),(-.30,im),arrowstyle="-|>",mutation_scale=14,
                            color="#177a72",linewidth=2))
ax.plot([a0,a0],[0,im],color="#d5632e",linewidth=2.5)
ax.add_patch(FancyArrowPatch((a0,.018),(a0,.082),arrowstyle="-|>",mutation_scale=13,
                            color="#d5632e",linewidth=1.6))
ax.scatter([L,a0,a0,tout],[im,0,im,im],c=["#177a72","#d5632e","#d5632e","#177a72"],s=34,zorder=5)
ax.annotate(r"$L+iy$", (L,im),xytext=(-1.99,.155),fontsize=10)
ax.annotate(r"$a_0$", (a0,0),xytext=(-.84,-.07),fontsize=11)
ax.annotate(r"$a_0+iy$", (a0,im),xytext=(-.93,.175),fontsize=10)
ax.annotate(r"$t=-0.20+0.10i$", (tout,im),xytext=(-.44,.21),fontsize=10,
            arrowprops={"arrowstyle":"-","color":"#444"})
ax.plot([0,.20],[-.08,-.08],color="#7548a3",linewidth=5)
ax.scatter([.20],[-.08],s=25,color="#7548a3")
ax.text(.46,-.145,r"$S_{t_+}=[0,0.20]-0.08i$",fontsize=9,color="#604389",ha="right")
ax.text(-1.65,.015,r"$G$: weighted horizontal ray",fontsize=10,color="#177a72")
ax.set_xlim(-2.1,.48);ax.set_ylim(-.34,.31)
ax.set_xlabel(r"$\mathrm{Re}\,s$");ax.set_ylabel(r"$\mathrm{Im}\,s$")
ax.set_title("Exact sample geometry, g = 0",fontsize=13)
ax.grid(alpha=.15)
bx.axis("off")
boxes=[
 (.81, "Arbitrary holomorphic input", r"$(0,-f)+d(F,0)=(\bar\partial F,F-f)$"),
 (.56, "Cup, then proper localization", r"$m_T,\quad L_\eta(a,b)=(\eta a+\bar\partial\eta\wedge b,\eta b)$"),
 (.31, "Shifted relative trace", r"$Q_N(a,b)=(\mathrm{Tr}_q a,(-1)^N\mathrm{Tr}_{q-1}b)$"),
 (.06, "Actual class and its full-neighbourhood primitive", r"$(0,-V_P)+d(E+J_\chi,0)$")]
for ypos,title,formula in boxes:
    bx.add_patch(Rectangle((0,ypos),1,.17,facecolor="#f2f5f8",edgecolor="#889cae",
                          transform=bx.transAxes))
    bx.text(.5,ypos+.115,title,ha="center",va="center",fontsize=10,
            transform=bx.transAxes)
    bx.text(.5,ypos+.055,formula,ha="center",va="center",fontsize=12,
            transform=bx.transAxes)
for start,end in [(.81,.73),(.56,.48),(.31,.23)]:
    bx.annotate("",xy=(.5,end),xytext=(.5,start),
                xycoords="axes fraction",arrowprops={"arrowstyle":"->","color":"#45596b"})
fig.text(.07,.06,"Proof locators: W.3 (cone-shift sign); W.5 (one-normal E); W.7 (ordered N-normal extension).",fontsize=11)
fig.text(.07,.025,"The left panel shows two different output fibres. Tube bounds: [-1.95,-0.65] × [-0.15,0.15]. No boundary extension of f.",fontsize=10)
fig.savefig(root/"collar-comparison.png",dpi=155)
fig.savefig(root/"collar-comparison.svg")
data={"g":0,"input_domain":"Re(s)<0","L":L,"a0":a0,
      "allowed_output":[tout,im],"support_output":[.20,-.08],
      "support_interval":[[0,-.08],[.20,-.08]],
      "tube":{"real":[-1.95,-.65],"imag":[-.15,.15]},
      "theta_transition":[-1.6,-1.0],
      "transition_imag_window":[-.125,.125],
      "interpretation":"Exact illustrative parameter choice; two fibres are drawn. No plotted numerical sample supplies a proof.",
      "proof_locators":["W.3","W.5","W.7"],
      "human_source_context":"Bound Microhyp §3.1 and HolIII III.1/IV.2/IV.5; figure is independently drawn."}
(root/"collar-comparison-figure-data.json").write_text(json.dumps(data,indent=2)+"\n",encoding="utf8")
print(json.dumps({"png_sha256":hashlib.sha256((root/"collar-comparison.png").read_bytes()).hexdigest(),
                  "svg_sha256":hashlib.sha256((root/"collar-comparison.svg").read_bytes()).hexdigest()}))
