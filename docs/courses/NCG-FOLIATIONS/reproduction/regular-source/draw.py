"""Original CC0 diagrams of RTP.3--13 and MI.1--10; no external artwork."""
from pathlib import Path
import argparse
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch
import numpy as np

plt.rcParams.update({"font.family":"DejaVu Sans", "font.size":13,
                    "svg.hashsalt":"ncg-regular-source-20261011", "svg.fonttype":"path"})
BLUE="#245b84"; RED="#a43d42"; GREEN="#24755e"; GRAY="#4c5664"

def box(ax,x,y,w,h,label,color=BLUE):
    ax.add_patch(FancyBboxPatch((x,y),w,h,boxstyle="round,pad=0.015",linewidth=1.5,
                              edgecolor=color,facecolor="white"))
    ax.text(x+w/2,y+h/2,label,ha="center",va="center",color=color,linespacing=1.6)

def save(fig,out,name):
    fig.savefig(out/(name+".svg"),metadata={"Date":None,"Creator":"Original CC0 mathematical diagram"})
    svg=out/(name+".svg");svg.write_bytes(svg.read_bytes().replace(b"\r\n",b"\n"))
    fig.savefig(out/(name+".png"),dpi=150,metadata={"Software":"Original CC0 mathematical diagram"})
    plt.close(fig)

def regular(out):
    fig,ax=plt.subplots(figsize=(12,7.5));fig.patch.set_facecolor("#f5f7fa")
    ax.set_xlim(0,1);ax.set_ylim(0,1);ax.axis("off")
    ax.text(.5,.96,"One regular source, two compactness directions",ha="center",fontsize=20,color=BLUE)
    ax.text(.5,.895,r"$\mathscr{H}=\mathscr{H}_T\,\widehat{\otimes}\,\mathscr{H}_N$   (original right $\mathrm{Cl}_q$ retained)",ha="center")
    box(ax,.04,.64,.40,.18,"Normal errors\n"+r"$A_1=C_T\widehat{\otimes}K_N$"+"\ncompact only in the normal direction",BLUE)
    box(ax,.56,.64,.40,.18,"Tree errors\n"+r"$A_2=K_T\widehat{\otimes}C_N$"+"\ncompact only in the tree direction",RED)
    ax.annotate("",xy=(.43,.52),xytext=(.24,.63),arrowprops={"arrowstyle":"->","color":BLUE,"lw":2})
    ax.annotate("",xy=(.57,.52),xytext=(.76,.63),arrowprops={"arrowstyle":"->","color":RED,"lw":2})
    box(ax,.20,.35,.60,.18,r"$A_1 A_2\subset J=K_T\widehat{\otimes}K_N$"+"\n"+r"$MA_1\subset J,\quad NA_2\subset J,\quad M+N=1$",GREEN)
    box(ax,.04,.075,.44,.18,r"$F=\sqrt{M}\,P+\sqrt{N}\,Q$"+" (symmetrized)\n"+r"$P=\Gamma_T\otimes F_N,\quad Q=F_T\otimes1$"+"\nwhole reduced source: both defects in J",BLUE)
    box(ax,.54,.075,.42,.18,"Every finite tree creation column\n"+r"$FT_v-(-1)^{|v|}T_vF_N\in K$"+"\noriginal phase and disk +1 retained",GREEN)
    ax.text(.5,.012,"RTP.3–13: algebraic schematic of the proved separator and creation maps",ha="center",fontsize=11,color=GRAY)
    save(fig,out,"regular-tree-normal-separator")

def metric(out):
    fig=plt.figure(figsize=(12,8));fig.patch.set_facecolor("#f5f7fa")
    fig.suptitle("The same holonomy: nonamenable metric isotropy and a normalized graph",fontsize=17,color=BLUE,y=.97)
    ax=fig.add_axes([.045,.30,.45,.57],projection="3d")
    ax.set_box_aspect((1,1,1));ax.set_xlim(-1.12,1.12);ax.set_ylim(-1.12,1.12);ax.set_zlim(-1.12,1.12)
    ax.set_xlabel("x");ax.set_ylabel("y");ax.set_zlabel("z")
    ax.view_init(elev=20,azim=35)
    for v,label,color in [(np.array([0,1,0]),"e2",GRAY),(np.array([0,1/3,2*np.sqrt(2)/3]),"A e2",BLUE),
                          (np.array([0,0,1]),"e3",GRAY),(np.array([2*np.sqrt(2)/3,0,1/3]),"B e3",RED)]:
        ax.quiver(0,0,0,*v,color=color,linewidth=2,arrow_length_ratio=.13)
        ax.text(*(v*1.12),label,color=color,fontsize=12)
    ax.set_title("Exact tangent vectors at n = 1\ncos(theta) = 1/3; orthogonal A, B",fontsize=12)
    tree=fig.add_axes([.57,.40,.37,.41]);tree.set_xlim(-1.1,1.1);tree.set_ylim(-1.1,1.1);tree.set_aspect("equal");tree.axis("off")
    tree.scatter([0],[0],s=130,color=GREEN,zorder=4);tree.text(.07,.02,"e (+)",fontsize=11,color=GREEN)
    for k,label in enumerate(["a","b","a^-1","b^-1"]):
        angle=np.pi/4+k*np.pi/2;p=.43*np.array([np.cos(angle),np.sin(angle)])
        tree.plot([0,p[0]],[0,p[1]],color=BLUE,lw=2);tree.scatter(*p,s=45,color=BLUE)
        tree.text(*(p*.80),label,fontsize=10,ha="center",va="center",bbox={"facecolor":"white","edgecolor":"none","pad":1})
        for offset in [-.32,0,.32]:
            c=.96*np.array([np.cos(angle+offset),np.sin(angle+offset)])
            tree.plot([p[0],c[0]],[p[1],c[1]],color=BLUE,lw=1.3)
            tree.scatter(*c,s=20,color=BLUE)
    tree.set_title("Ball of radius 2 in the full degree-four tree\nall levels and edges retained",fontsize=12)
    text=fig.add_axes([.055,.035,.89,.22]);text.axis("off")
    box(text,.02,.10,.45,.76,"Actual metric unit (1, I)\nisotropy and range fibre = F2\n"+r"$\|\frac{1}{4}\sum_{s=a^{\pm1},b^{\pm1}}\lambda_s\|\leq\sqrt{3}/2<1$",RED)
    box(text,.53,.10,.45,.76,"Same original q = 3, full inverse lift\nregular tree + invariant normal Dirac\nwhole reduced graph; original disk +1",GREEN)
    fig.text(.75,.30,"Finite tree drawing; the proof uses the entire completion.\nMI.1–10 give the exact germs, lifts, norm and domain.",ha="center",fontsize=10,color=GRAY)
    save(fig,out,"nonamenable-metric-isotropy")

if __name__=="__main__":
    p=argparse.ArgumentParser();p.add_argument("--output",type=Path,default=Path(__file__).resolve().parents[2]/"figures")
    a=p.parse_args();a.output.mkdir(parents=True,exist_ok=True)
    regular(a.output);metric(a.output)
