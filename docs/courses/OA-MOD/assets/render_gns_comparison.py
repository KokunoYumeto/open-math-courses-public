"""Render three original, reproducible GNS proof illustrations.

Usage: python render_gns_comparison.py --output-directory assets
Images illustrate the cited proofs; finite plotted samples are not proofs.
Original OA-MOD course project plotting code, CC0-1.0.
"""
from pathlib import Path
import argparse
import hashlib
import json
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch
import numpy as np

plt.rcParams.update({"font.family":"DejaVu Sans","font.size":14,
                     "mathtext.fontset":"dejavusans","axes.titleweight":"bold"})
INK="#172438";BLUE="#185aa0";GREEN="#087c68";ORANGE="#b44c12"

def panel(ax,y,title,lines,color=BLUE,height=.17):
    ax.add_patch(FancyBboxPatch((.05,y),.9,height,
        boxstyle="round,pad=0.012,rounding_size=.012",facecolor="#f4f8fc",
        edgecolor=color,linewidth=1.6))
    ax.text(.5,y+height-.026,title,ha="center",va="top",color=color,
            fontsize=14,fontweight="bold")
    ax.text(.5,y+height-.066,lines,ha="center",va="top",color=INK,
            fontsize=13,linespacing=1.55)

def arrow(ax,y,caption):
    ax.annotate("",xy=(.5,y-.040),xytext=(.5,y+.016),
                arrowprops={"arrowstyle":"->","color":INK,"lw":1.8})
    ax.text(.5,y-.042,caption,ha="center",va="center",fontsize=11,color=INK)

def save(fig,path):
    assert not path.exists(),path
    fig.savefig(path,dpi=220,facecolor="white",
                metadata={"Software":"OA-MOD original plotting code",
                          "Copyright":"CC0-1.0"})
    plt.close(fig)

def render(out):
    out.mkdir(parents=True,exist_ok=True)
    f=plt.figure(figsize=(4.4,8.9));ax=f.add_axes((.02,.01,.96,.98));ax.set(xlim=(0,1),ylim=(0,1));ax.axis("off")
    ax.text(.5,.987,"Recovering the GNS graph",ha="center",va="top",fontsize=16,color=INK,fontweight="bold")
    panel(ax,.755,"Supplied concrete fields",
          "$x_j\\in M_y\\subseteq B(K_y)$\nBoth Gram orders are measurable.\nThe set is sharp-norm dense.",height=.175)
    arrow(ax,.739,"Gram construction (GFR-02)")
    panel(ax,.493,"Actual intrinsic graph field",
          "$g_j=(\\Lambda x_j,\\overline{\\Lambda x_j^*})$\n$E_y=G(\\overline{S_y})\\subseteq H_y\\oplus\\overline{H_y}$\nFirst projection $P_y$ is measurable.",height=.17)
    arrow(ax,.478,"Cauchy code + both concrete resolvents")
    panel(ax,.224,"Unique selected graph limit",
          "$g_{s_n}\\longrightarrow(\\Lambda c,\\overline{\\Lambda c^*})$\n$c\\in\\mathfrak{a}_y$ exactly when the code exists.\nBounded right multipliers identify it.",color=GREEN,height=.175)
    arrow(ax,.208,"Completed analytic selection (GFR-04–05)")
    ax.text(.5,.128,"Apply $P_y$: measurable $\\Lambda c$.\nUse $c=x_j^*$ and $c=x_jx_k$:\nsharp and product fields follow.",ha="center",va="top",fontsize=12,color=INK,linespacing=1.1)
    ax.text(.5,.015,"Proof: GFR-02, 04, 05; equations GFR.5–17.\nAntecedent: Takesaki II, VIII.4.4–4.5.",ha="center",va="bottom",fontsize=10,color=INK)
    save(f,out/"gns-code-and-graph.png")

    f=plt.figure(figsize=(4.4,8.4));ax=f.add_axes((.02,.01,.96,.98));ax.set(xlim=(0,1),ylim=(0,1));ax.axis("off")
    ax.text(.5,.987,"Two typed transports",ha="center",va="top",fontsize=16,color=INK,fontweight="bold")
    panel(ax,.750,"One countable contraction family",
          "$q_m\\in M_y$, $\\|q_m\\|\\leq1$\n$q_m$ and $\\pi_y(q_m)$ are measurable.\nStrong-star dense in both unit balls.",height=.175)
    ax.text(.5,.718,"Two strong-star metrics",ha="center",va="top",fontsize=13,fontweight="bold",color=INK)
    panel(ax,.488,"Forward: concrete to actual GNS",
          "$a_y\\in M_y\\subseteq B(K_y)$\n$d_K(q_{m_n},a_y/r_y)<1/n$\n$\\pi_y(a_y)=r_y\\lim_n\\pi_y(q_{m_n})$",height=.18)
    ax.text(.5,.470,"$r_y=1+\\|a_y\\|$; choose the least index.",ha="center",va="top",fontsize=12,color=INK)
    panel(ax,.222,"Inverse: actual GNS to concrete",
          "$B_y\\in\\pi_y(M_y)\\subseteq B(H_y)$\n$d_H(\\pi_y(q_{m_n}),B_y/r_y)<1/n$\n$\\pi_y^{-1}(B_y)=r_y\\lim_n q_{m_n}$",color=GREEN,height=.18)
    ax.text(.5,.202,"$r_y=1+\\|B_y\\|$; choose the least index.",ha="center",va="top",fontsize=12,color=INK)
    ax.text(.5,.128,"Bounds may vary with the fibre.\nThese are operator-algebra maps.\nExample: $\\dim K_y=2$, $\\dim H_y=4$.",ha="center",va="top",fontsize=12,color=INK,linespacing=1.1)
    ax.text(.5,.015,"Proof: GFR-07–08, equations GFR.21–25.\nMatrix example: GFR-11; source: VIII.4.5.",ha="center",va="bottom",fontsize=10,color=INK)
    save(f,out/"gns-two-transports.png")

    f,ax=plt.subplots(figsize=(4.4,8.0))
    f.subplots_adjust(left=.20,right=.96,bottom=.40,top=.80)
    n=np.arange(1,21)
    ax.plot(n,n,"o-",ms=3,color=ORANGE,label="operator norm")
    ax.plot(n,2/n,"s-",ms=3,color=BLUE,label="sharp norm squared")
    ax.plot(n,1/(n*(n*n+1)),"^-",ms=3,color=GREEN,label="resolvent error squared")
    ax.set_yscale("log");ax.set_xlim(1,20);ax.set_xticks([1,5,10,15,20]);ax.set_xlabel("integer n")
    ax.set_ylabel("exact sample value");ax.grid(True,which="both",alpha=.22)
    ax.legend(loc="upper center",bbox_to_anchor=(.5,1.28),frameon=False,fontsize=11)
    f.suptitle("Sharp convergence with\nunbounded operator norms",y=.975,fontsize=15,color=INK,fontweight="bold")
    f.text(.52,.290,"$x_n=n\\,1_{(0,n^{-3})}$,  $z=(1,0)$",ha="center",fontsize=14,color=INK)
    f.text(.52,.220,"$\\|x_n\\|=n$,  $\\|x_n\\|_\\varphi^{\\sharp\\,2}=2/n$",ha="center",fontsize=14,color=INK)
    f.text(.52,.145,"$\\|(R_-(x_n)-R_-(0))z\\|^2$\n$=1/[n(n^2+1)]$",ha="center",fontsize=14,color=INK)
    f.text(.52,.015,"Logarithmic vertical axis; samples are not a proof.\nExact calculation: GFR-11, equation GFR.31.\nClassical spike antecedent: SCF-03.",ha="center",fontsize=10,color=INK)
    save(f,out/"gns-spike-and-resolvent.png")
    rows=[]
    for name in ("gns-code-and-graph.png","gns-two-transports.png","gns-spike-and-resolvent.png"):
        p=out/name;raw=p.read_bytes()
        from PIL import Image
        with Image.open(p) as im:width,height=im.size
        rows.append({"path":name,"bytes":len(raw),"sha256":hashlib.sha256(raw).hexdigest().upper(),"width":width,"height":height})
    return rows

if __name__=="__main__":
    parser=argparse.ArgumentParser();parser.add_argument("--output-directory",type=Path,required=True)
    args=parser.parse_args();print(json.dumps({"figures":render(args.output_directory),"license":"CC0-1.0"},indent=2))

