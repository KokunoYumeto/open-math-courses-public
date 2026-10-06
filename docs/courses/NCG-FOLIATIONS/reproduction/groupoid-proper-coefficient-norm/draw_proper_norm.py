"""Original CC0 typed cutoff-intertwiner diagram for PN.1--PN.20."""
from pathlib import Path
import argparse
import json
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties
from matplotlib.patches import FancyBboxPatch
HERE=Path(__file__).resolve().parent
REG=FontProperties(fname=str(HERE/"fonts"/"DejaVuSans.ttf"))
BOLD=FontProperties(fname=str(HERE/"fonts"/"DejaVuSans-Bold.ttf"))
INK="#19334a";BLUE="#155e94";GREEN="#087858";ORANGE="#b65d16"
def label(ax,x,y,s,size=14,bold=False,**kw):
    ax.text(x,y,s,fontsize=size,fontproperties=BOLD if bold else REG,color=INK,**kw)
def arrow(ax,p,q,color=BLUE):
    ax.annotate("",xy=q,xytext=p,arrowprops={"arrowstyle":"->","lw":2.4,"color":color})
def box(ax,x,y,w,h):
    ax.add_patch(FancyBboxPatch((x,y),w,h,boxstyle="round,pad=.01",facecolor="#edf4f9",edgecolor=BLUE))
def render(out):
    out.mkdir(parents=True,exist_ok=True)
    matplotlib.rcParams.update({"svg.hashsalt":"proper-groupoid-norm-PN-v1","svg.fonttype":"path"})
    fig=plt.figure(figsize=(14,8),facecolor="white")
    fig.text(.05,.948,"Proper coefficients: a completed-module proof of full = reduced",fontsize=22,fontproperties=BOLD,color=INK)
    a=fig.add_axes([.055,.32,.46,.54]);a.axis("off");a.set_xlim(0,1);a.set_ylim(0,1)
    label(a,0,.96,"11U.2  The actual isometric intertwiner",17,True)
    for x,y,s in [(.13,.73,"Bₘ"),(.77,.73,"E ⊗P Bₘ"),(.13,.23,"Bₘ"),(.77,.23,"E ⊗P Bₘ")]:
        box(a,x-.11,y-.06,.22,.12);label(a,x,y,s,18,True,ha="center",va="center")
    arrow(a,(.26,.73),(.64,.73),GREEN);arrow(a,(.26,.23),(.64,.23),GREEN)
    label(a,.46,.82,"W",16,True,ha="center");label(a,.46,.30,"W",16,True,ha="center")
    arrow(a,(.13,.65),(.13,.31));arrow(a,(.77,.65),(.77,.31))
    label(a,.18,.49,"left f",12);label(a,.81,.49,"Λ(f) ⊗ 1",12)
    label(a,.44,.08,"⟨Wa, Wb⟩ = a* ∗ b in Bₘ",14,True,ha="center")
    b=fig.add_axes([.565,.32,.39,.54]);b.axis("off");b.set_xlim(0,1);b.set_ylim(0,1)
    label(b,0,.96,"PN.13  Every pair has one middle unit",16,True)
    x=(.13,.42);y=(.52,.42);z=(.89,.42)
    b.scatter([x[0],y[0],z[0]],[x[1],y[1],z[1]],s=80,color=INK)
    arrow(b,(.18,.42),(.46,.42));arrow(b,(.58,.42),(.83,.42),GREEN)
    label(b,.31,.50,"k",16,True,ha="center");label(b,.71,.50,"g",16,True,ha="center")
    label(b,.13,.30,"x = s(k)",11,ha="center");label(b,.52,.29,"y = r(k) = s(g)",11,True,ha="center");label(b,.89,.30,"z = r(g)",11,ha="center")
    arrow(b,(.15,.62),(.88,.62),ORANGE);label(b,.52,.69,"l = gk : x → z",14,True,ha="center")
    label(b,.52,.14,"Wa(g,k) = cy αg⁻¹(a(gk)) ∈ Py",14,True,ha="center")
    label(b,.52,.035,"h⁻¹g has the same source y; central cy stays fixed.",11,ha="center")
    c=fig.add_axes([.055,.075,.90,.18]);c.axis("off");c.set_xlim(0,1);c.set_ylim(0,1)
    box(c,.005,.035,.985,.93)
    label(c,.025,.77,"PN.8–PN.9: Σrg=y αg(cs(g)²) = 1 strictly; 11S.3 makes the localized double-arrow support compact.",12,True)
    label(c,.025,.48,"11U.3:  ‖f‖ₘ = ‖left f‖ ≤ ‖Λ(f)‖ = ‖f‖ᵣ.  The universal norm gives the reverse inequality.",13)
    label(c,.025,.19,"Thus qP : P ⋊ₘ G → P ⋊ᵣ G is an actual graded isomorphism. Original-unit Dirac factors remain separate.",12)
    notice=(HERE/"FONT-NOTICE.txt").read_text(encoding="utf-8")
    fig.savefig(out/"groupoid-proper-coefficient-norm.png",dpi=200,metadata={"Software":"Matplotlib; original diagram CC0 1.0","Description":notice})
    fig.savefig(out/"groupoid-proper-coefficient-norm.svg",metadata={"Date":None,"Creator":"Original CC0 proper-coefficient norm diagram","Description":notice})
    svg=out/"groupoid-proper-coefficient-norm.svg"
    svg.write_text(svg.read_text(encoding="utf-8"),encoding="utf-8",newline="\n")
    plt.close(fig)
    data={"proof_locators":["PN.10","PN.13","PN.14","PN.15","PN.19","PN.20"],"typed_pair":{"k":"x->y","g":"y->z","gk":"x->z","middle":"s(g)=r(k)=y","coefficient":"P_y"},"commuting_square":{"top_and_bottom":"W:B_m->E tensor_P B_m","left":"left multiplication by f","right":"Lambda(f) tensor 1"},"proper_coefficient_quotient":"actual graded isomorphism","not_claimed":["coefficient-free quotient invertibility","original-unit Dirac factors","the general original-unit graph-Dirac construction"]}
    (out/"groupoid-proper-coefficient-norm-data.json").write_text(json.dumps(data,indent=2)+"\n",encoding="utf-8",newline="\n")
if __name__=="__main__":
    p=argparse.ArgumentParser();p.add_argument("--output-dir",type=Path,default=HERE/"figures");render(p.parse_args().output_dir.resolve())
