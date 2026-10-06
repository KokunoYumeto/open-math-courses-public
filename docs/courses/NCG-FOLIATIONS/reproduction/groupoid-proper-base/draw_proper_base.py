"""CC0 exact GP.1--GP.13 schematic; fonts retain their bundled notices."""
from pathlib import Path
import argparse
import json
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties
from matplotlib.patches import Polygon, FancyBboxPatch
HERE=Path(__file__).resolve().parent
REG=FontProperties(fname=str(HERE/"fonts"/"DejaVuSans.ttf"))
BOLD=FontProperties(fname=str(HERE/"fonts"/"DejaVuSans-Bold.ttf"))
INK="#19334a"; BLUE="#155e94"; GREEN="#087858"; ORANGE="#b65d16"
def text(ax,x,y,s,size=14,bold=False,**kw):
    ax.text(x,y,s,fontsize=size,fontproperties=BOLD if bold else REG,color=INK,**kw)
def arrow(ax,p,q,color=BLUE,style="arc3,rad=0"):
    ax.annotate("",xy=q,xytext=p,arrowprops={"arrowstyle":"->","color":color,"lw":2.5,"connectionstyle":style})
def render(out):
    out.mkdir(parents=True,exist_ok=True)
    matplotlib.rcParams.update({"svg.hashsalt":"groupoid-half-mass-GP-v1","svg.fonttype":"path"})
    fig=plt.figure(figsize=(13,7),facecolor="white")
    fig.text(.05,.946,"A proper base built on the actual groupoid arrows",fontsize=21,fontproperties=BOLD,color=INK)
    a=fig.add_axes([.075,.29,.39,.53]); a.set_xlim(0,1.06); a.set_ylim(0,1.06)
    a.add_patch(Polygon([[0,0],[1,0],[0,1]],closed=True,facecolor="#eff8f3",edgecolor=GREEN,lw=2))
    a.add_patch(Polygon([[.5,.5],[1.06,.5],[1.06,1.06],[.5,1.06]],closed=True,facecolor="#fff0df",edgecolor="none"))
    a.axvline(.5,color=ORANGE,ls="--"); a.axhline(.5,color=ORANGE,ls="--")
    a.plot([0,1],[1,0],color=GREEN,lw=2)
    text(a,.075,.24,"a + b ≤ 1\nif the two sets are disjoint",12)
    text(a,.77,.88,"a > ½\nb > ½\nimpossible",13,True,ha="center")
    a.set_xlabel("a = μ(E)",fontproperties=REG,fontsize=13)
    a.set_ylabel("b = μ(Lg⁻¹E)",fontproperties=REG,fontsize=13)
    a.set_title("11S.2  The strict half-mass test",fontproperties=BOLD,fontsize=16,pad=15)
    for label in a.get_xticklabels()+a.get_yticklabels():label.set_fontproperties(REG)
    b=fig.add_axes([.55,.29,.40,.56]);b.axis("off");b.set_xlim(0,1);b.set_ylim(0,1)
    text(b,0,.96,"11S.2  Overlap retains every anchor",16,True)
    x=(.49,.24); y=(.13,.68); z=(.85,.68)
    b.scatter([x[0],y[0],z[0]],[x[1],y[1],z[1]],s=90,color=INK,zorder=5)
    arrow(b,(.46,.29),(.16,.64));arrow(b,(.19,.68),(.79,.68),GREEN);arrow(b,(.53,.29),(.83,.64),ORANGE)
    text(b,.49,.13,"x = s(h) = s(k)",12,ha="center")
    text(b,.13,.77,"y = s(g)",12,ha="center");text(b,.85,.77,"z = r(g)",12,ha="center")
    text(b,.19,.43,"h ∈ E",14,True);text(b,.69,.43,"k = gh ∈ E",14,True)
    text(b,.49,.71,"g : y → z",14,True,ha="center")
    text(b,.49,.04,"g = kh⁻¹ ∈ EE⁻¹, a compact arrow set",12,True,ha="center")
    c=fig.add_axes([.05,.055,.90,.16]);c.axis("off");c.set_xlim(0,1);c.set_ylim(0,1)
    c.add_patch(FancyBboxPatch((.005,.045),.99,.91,boxstyle="round,pad=.005",facecolor="#edf4f9",edgecolor=BLUE))
    text(c,.025,.74,"11S.1–11S.3: M consists of range-fibre subprobabilities with mass > ½, in the vague topology.",12,True)
    text(c,.025,.45,"Every proper G-space maps equivariantly to M by Φ(z) = Σrh=p(z) c(h⁻¹z)² δh; the cutoff sum is 1.",12)
    text(c,.025,.17,"The proper space and central coefficient are proved. Classes C₀(T) → P → C₀(T) still require their Dirac construction.",11)
    notice=(HERE/"FONT-NOTICE.txt").read_text(encoding="utf-8")
    fig.savefig(out/"groupoid-proper-base.png",dpi=200,metadata={"Software":"Matplotlib; original diagram CC0 1.0","Description":notice})
    fig.savefig(out/"groupoid-proper-base.svg",metadata={"Date":None,"Creator":"Original CC0 groupoid measure-base diagram","Description":notice})
    svg=out/"groupoid-proper-base.svg"
    svg.write_text(svg.read_text(encoding="utf-8"),encoding="utf-8",newline="\n")
    plt.close(fig)
    data={"proof_locators":["Theorem11S.1","Theorem11S.2","Theorem11S.3","GP.8","GP.12"],"mass_threshold":{"strict_lower":"1/2","upper":1},"left_scope":"coordinate projection of two set masses; disjointness implies a+b<=1","right_scope":"typed composable arrow triangle; h and k in E imply g in E E^-1","not_claimed":["kernel compactification for arbitrary eligible holonomy","Dirac factors","the general original-unit graph-Dirac construction"]}
    (out/"groupoid-proper-base-data.json").write_text(json.dumps(data,indent=2)+"\n",encoding="utf-8",newline="\n")
if __name__=="__main__":
    parser=argparse.ArgumentParser();parser.add_argument("--output-dir",type=Path,default=HERE/"figures");render(parser.parse_args().output_dir.resolve())
