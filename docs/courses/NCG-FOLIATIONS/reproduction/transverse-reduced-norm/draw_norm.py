"""Original CC0 diagram for RN.7--RN.13. Bundled fonts retain their notice."""
from pathlib import Path
import argparse
import json
import math
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties, fontManager
import numpy as np
from PIL import PngImagePlugin

HERE = Path(__file__).resolve().parent
font_paths = [HERE/"fonts"/"DejaVuSans.ttf", HERE/"fonts"/"DejaVuSans-Bold.ttf"]
for path in font_paths:
    fontManager.addfont(str(path))
regular = FontProperties(fname=str(font_paths[0]))
bold = FontProperties(fname=str(font_paths[1]))
plt.rcParams.update({"font.family":"DejaVu Sans", "font.size":11,
                     "svg.fonttype":"path","svg.hashsalt":"transverse-reduced-norm-v1",
                     "axes.spines.top":False,"axes.spines.right":False})

def label(ax, x, y, value, size=11, weight=False, **kw):
    return ax.text(x,y,value,fontproperties=bold if weight else regular,
                   fontsize=size,**kw)

def main():
    parser=argparse.ArgumentParser()
    parser.add_argument("--output-dir",default=str(HERE/"figures"))
    args=parser.parse_args()
    output=Path(args.output_dir); output.mkdir(parents=True,exist_ok=True)
    fig, axes=plt.subplots(2,2,figsize=(14,9.4))
    fig.subplots_adjust(left=.075,right=.975,bottom=.075,top=.85,hspace=.42,wspace=.32)
    fig.suptitle("A geometric transverse representation can miss the reduced norm",
                 fontproperties=bold,fontsize=18,y=.975)
    fig.text(.5,.927,"Exact norm gap: 1 versus √3/2.  A scalar index +1 also need not identify an equivariant unit.",
             ha="center",fontproperties=regular,fontsize=12)
    a,b,c,d=axes.flatten()
    a.set_xlim(0,1);a.set_ylim(0,1);a.axis("off")
    label(a,0,1.04,"A.  Actual metric-bundle action",13,True)
    for x,col,txt in [(.23,"#146477","n ∈ SU(2) × S¹"),(.77,"#b45c18","Q ∈ Sym⁺₄")]:
        a.add_patch(plt.Circle((x,.63),.15,facecolor=col,alpha=.12,edgecolor=col,lw=2))
        label(a,x,.63,txt,11,ha="center",va="center")
    a.annotate("",xy=(.40,.84),xytext=(.12,.84),arrowprops={"arrowstyle":"->","lw":2,"color":"#146477"})
    label(a,.26,.90,"n ↦ ρ(g)n",12,ha="center")
    label(a,.77,.86,"Q is fixed",12,ha="center")
    label(a,.5,.31,"P = N × Sym⁺₄;  g(n,Q) = (gn,Q)",12,ha="center")
    label(a,.5,.19,"q(Q) has compact support and equals 1 on a ball.",11,ha="center")
    label(a,.5,.07,"Inverse central coefficient: χ(g)⁻¹.  Determinant: χ(g)².",11,ha="center")
    b.set_ylim(0,1.17);b.set_xlim(-.6,1.6)
    label(b,-.6,1.22,"B.  Proved norms of z = q vχ",13,True)
    b.bar([0,1],[1,math.sqrt(3)/2],width=.58,color=["#146477","#b45c18"])
    b.set_xticks([0,1],["geometric π","reduced regular"])
    b.set_ylabel("operator norm")
    label(b,0,1.045,"1",12,True,ha="center")
    label(b,1,math.sqrt(3)/2+.045,"√3/2 ≈ 0.866025",12,True,ha="center")
    b.grid(axis="y",alpha=.18);b.set_axisbelow(True)
    R=np.arange(1,41,dtype=int)
    quotients=(2*R/math.sqrt(3))/(1+4*R/3)
    c.plot(R,quotients,"o-",ms=3,color="#146477",label="exact finite-vector quotient")
    c.axhline(math.sqrt(3)/2,color="#b45c18",linestyle="--",label="proved norm √3/2")
    c.set_xlim(0,41);c.set_ylim(.45,.91);c.set_xlabel("integer truncation radius R")
    c.set_ylabel("Rayleigh quotient for A/4")
    label(c,0,.95,"C.  Infinite norm proved by exact finite tests",13,True)
    c.legend(loc="lower right",prop=regular,fontsize=10);c.grid(alpha=.18)
    label(c,3,.58,"(2R/√3) / (1 + 4R/3)",12)
    d.set_xlim(0,1);d.set_ylim(0,1);d.axis("off")
    label(d,0,1.04,"D.  Ordinary index and equivariant index",13,True)
    entries=[(.75,"trivial line",(1,0),"+1"),(.39,"sign line",(0,1),"−1")]
    for y,name,pair,char in entries:
        d.add_patch(plt.Rectangle((.015,y-.10),.97,.20,facecolor="#eef3f7",edgecolor="#637b8e",lw=1))
        label(d,.07,y,name,12,True,va="center")
        label(d,.52,y,str(pair),12,va="center")
        label(d,.88,y,char,12,va="center",ha="center")
    label(d,.52,.97,"(ind₊, ind₋)",11,ha="center")
    label(d,.88,.97,"character at c",10,ha="center")
    label(d,.5,.16,"Forgetting the C₂ action sums the pair:  +1 in both cases.",11,ha="center")
    label(d,.5,.035,"An equivariant action homotopy supplies an additional identity.",10,ha="center")
    for ax in [b,c]:
        for tick in ax.get_xticklabels()+ax.get_yticklabels():tick.set_fontproperties(regular)
        ax.xaxis.label.set_fontproperties(regular);ax.yaxis.label.set_fontproperties(regular)
    notice=(HERE/"FONT-NOTICE.txt").read_text(encoding="utf-8")
    credit="Original diagram and code: CC0 1.0. DejaVu glyphs retain their complete font terms.\n"+notice
    fig.savefig(output/"transverse-reduced-norm.png",dpi=160,
                metadata={"Software":"draw_norm.py","Description":credit})
    fig.savefig(output/"transverse-reduced-norm.svg",
                metadata={"Date":None,"Title":"Transverse geometric and reduced norm comparison","Description":credit})
    plt.close(fig)
    (output/"data.json").write_text(json.dumps({
        "R":R.tolist(),"rayleigh":quotients.tolist(),"reduced_norm":math.sqrt(3)/2,
        "geometric_norm":1,"exact_formula":"(2R/sqrt(3))/(1+4R/3)",
        "figure_scope":"Metric-bundle panel is a coordinate schematic; norm and integer-index comparisons are exact."
        },indent=2)+"\n",encoding="utf-8",newline="\n")

if __name__=="__main__":
    main()
