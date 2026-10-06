"""Original exact Banach proof diagrams and finite rational model; CC0-1.0."""
from pathlib import Path
from fractions import Fraction
import hashlib, json
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Polygon, Rectangle, FancyBboxPatch

def render(directory):
    directory = Path(directory)
    directory.mkdir(parents=True, exist_ok=True)
    ink, blue, green, red = "#172438", "#185aa0", "#087c68", "#a32d33"
    plt.rcParams.update({"font.family":"DejaVu Sans","font.size":15,
                         "mathtext.fontset":"dejavusans","text.color":ink})
    fig = plt.figure(figsize=(6,12), facecolor="white")
    fig.suptitle("Compactness of dual balls\nand the finite-test mechanism",
                 fontsize=18, fontweight="bold", y=.985, color=ink)
    ax = fig.add_axes((.15,.68,.7,.25))
    ax.set_aspect("equal")
    ax.add_patch(Rectangle((-1,-1),2,2,fill=False,edgecolor=green,ls="--",lw=2))
    ax.add_patch(Polygon([(1,0),(0,1),(-1,0),(0,-1)],facecolor="#dbeafb",edgecolor=blue,lw=2))
    ax.plot(1,1,"o",color=red,ms=7)
    ax.annotate("(1, 1)\nnorm = 2",xy=(1,1),xytext=(.35,1.42),
                fontsize=14,color=red,arrowprops={"arrowstyle":"->","color":red})
    ax.set(xlim=(-1.55,1.55),ylim=(-1.4,2.1),xticks=(-1,0,1),yticks=(-1,0,1),
           xlabel="a",ylabel="b")
    ax.grid(alpha=.15)
    fig.text(.5,.603,r"$X=(\mathbb{R}^2,\|\cdot\|_\infty)$",ha="center",fontsize=17)
    fig.text(.5,.570,r"Blue: $\|f_{a,b}\|=|a|+|b|\leq1$",ha="center",fontsize=15)
    fig.text(.5,.537,"Dashed: two coordinate bounds only",ha="center",fontsize=14,color=green)
    fig.text(.5,.502,"Finite tests for one alleged external point",
             ha="center",fontsize=16,fontweight="bold")
    flow = fig.add_axes((.06,.025,.88,.465))
    flow.set(xlim=(0,1),ylim=(0,1));flow.axis("off")
    boxes=[
        (.76, r"$\zeta\in\overline{J(K)}^{\,w^*}\setminus J(X)$"+"\n"+
              r"$E_n=\operatorname{span}\{\zeta,Jx_1,\ldots,Jx_n\}$"),
        (.51, r"$F_n\subset B_{X^*}\quad\mathrm{finite}$"+"\n"+
              r"$\max_{f\in F_n}|y(f)|\geq\frac{1}{2}\|y\|\quad(y\in E_n)$"),
        (.26, r"$x_{n+1}\in K$"+"\n"+
              r"$|f(x_{n+1})-\zeta(f)|<1/(n+1)$"+"\n"+
              r"$f\in F_1\cup\cdots\cup F_n$"),
        (.015, r"$x\in X\quad\mathrm{weak\ accumulation\ point}$"+"\n"+
              r"$f(x)=\zeta(f)\ (f\in\bigcup_nF_n)$"+"\n"+
              r"$Jx=\zeta\quad\mathrm{contradiction}$")
    ]
    for y, label in boxes:
        flow.add_patch(FancyBboxPatch((.025,y),.95,.21,boxstyle="round,pad=.01",
                       facecolor="#f5f8fc",edgecolor=blue,lw=1.4))
        flow.text(.5,y+.105,label,ha="center",va="center",fontsize=14)
    for y in (.74,.49,.24):
        flow.annotate("",xy=(.5,y-.015),xytext=(.5,y+.015),
                      arrowprops={"arrowstyle":"->","color":green,"lw":1.8})
    out=directory/"banach-compactness-mechanism.png"
    fig.savefig(out,dpi=200,metadata={"Software":"OA-MOD course project; original CC0 diagram"})
    plt.close(fig)
    # The independent finite corner optimization checks the model norm without
    # invoking the formula as its implementation.
    count=0
    for a in [Fraction(k,5) for k in range(-10,11)]:
        for b in [Fraction(k,5) for k in range(-10,11)]:
            corner_sup=max(abs(a*x+b*y) for x,y in [(1,1),(1,-1),(-1,1),(-1,-1)])
            assert corner_sup==abs(a)+abs(b)
            count+=1
    assert max(abs(x+y) for x,y in [(1,1),(1,-1),(-1,1),(-1,-1)])==2
    receipt={"schema":"oa-mod-Banach-figure-model/v1",
             "finite_rational_pairs_checked":count,"corner_optimization":"PASS",
             "outside_coordinate_only_point":[1,1],"outside_point_functional_norm":2,
             "diagram":"Typed schematic; no planar embedding of an infinite-dimensional dual is claimed.",
             "proof_locators":["AB.11–13","AB.14"],"width":1200,"height":2400,
             "png_sha256":hashlib.sha256(out.read_bytes()).hexdigest().upper()}
    return receipt

if __name__=="__main__":
    import argparse
    parser=argparse.ArgumentParser()
    parser.add_argument("--out",type=Path,default=Path(__file__).resolve().parent)
    args=parser.parse_args()
    print(json.dumps(render(args.out),indent=2))
