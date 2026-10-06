"""Original exact-set diagram; finite plotting windows are explicitly marked."""
from pathlib import Path
import json
import math
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch

D = Path(__file__).resolve().parent
A = D/"assets"
A.mkdir(exist_ok=True)
plt.rcParams.update({
    "font.family":"DejaVu Sans", "font.size":12,
    "svg.hashsalt":"type-iii-modular-trichotomy-20261004",
    "mathtext.fontset":"dejavusans", "axes.unicode_minus":True
})
navy="#143347"; blue="#007f9e"; red="#b83b41"; pale="#edf5f7"; grey="#5b6973"
fig=plt.figure(figsize=(16,11),dpi=180,facecolor="white")
canvas=fig.add_axes([0,0,1,1]);canvas.set(xlim=(0,1),ylim=(0,1));canvas.axis("off")
canvas.text(.055,.952,"The positive part comes from a subgroup; zero needs its own proof",
            fontsize=22,weight="bold",color=navy)
canvas.text(.055,.915,"For a given type III factor with separable predual  •  MT1–MT6",
            fontsize=14,color=grey)
canvas.text(.17,.865,r"Additive group $G\subseteq\mathbb{R}$",fontsize=17,color=navy)
canvas.text(.54,.865,r"Positive part $\exp G$  (horizontal coordinate: $\log x$)",
            fontsize=15,color=navy)
canvas.text(.932,.865,"Zero",fontsize=15,color=red,ha="center")
rows=[(.745,r"$G=\{0\}$","single point", "single"),
      (.555,r"$G=a\mathbb{Z}$","sample: a = log 2", "lattice"),
      (.365,r"$G=\mathbb{R}$","whole real line", "line")]
for y,title,subtitle,kind in rows:
    canvas.text(.055,y+.045,title,fontsize=19,color=navy)
    canvas.text(.055,y+.016,subtitle,fontsize=10.5,color=grey)
    left=fig.add_axes([.225,y-.025,.24,.072])
    right=fig.add_axes([.575,y-.025,.285,.072])
    for ax in [left,right]:
        ax.set(xlim=(-3.1,3.1),ylim=(-.75,.75))
        ax.spines[["top","right","left"]].set_visible(False)
        ax.spines["bottom"].set_position(("data",0));ax.spines["bottom"].set_color("#9eabb1")
        ax.set_yticks([]);ax.tick_params(axis="x",labelsize=10,pad=6,length=3)
    left.set_xticks([-2,0,2],["−2","0","2"])
    right.set_xticks([-math.log(4),-math.log(2),0,math.log(2),math.log(4)],
                      ["1/4","1/2","1","2","4"])
    vals=[0] if kind=="single" else [n*math.log(2) for n in range(-4,5)]
    if kind=="line":
        for ax in [left,right]:
            ax.plot([-3.02,3.02],[0,0],color=blue,lw=5,solid_capstyle="round")
            ax.scatter([-3.02,3.02],[0,0],marker="|",s=110,color=blue,zorder=4)
    else:
        for ax in [left,right]:ax.scatter(vals,[0]*len(vals),s=62,color=blue,zorder=4)
    if kind!="single":
        for ax in [left,right]:
            ax.text(-3.03,.32,"…",ha="center",color=blue,fontsize=16)
            ax.text(3.03,.32,"…",ha="center",color=blue,fontsize=16)
    canvas.annotate("",xy=(.565,y+.011),xytext=(.49,y+.011),
                    arrowprops={"arrowstyle":"->","lw":1.5,"color":grey})
    canvas.text(.527,y+.041,r"$x=e^r$",ha="center",color=navy,fontsize=12)
    canvas.text(.894,y+.011,r"$\cup$",ha="center",va="center",fontsize=22,color=grey)
    canvas.scatter([.936],[y+.011],s=125,facecolors=red,edgecolors=red,linewidth=2)
    canvas.text(.936,y-.04,"{0}",ha="center",color=red,fontsize=14)
    label={"single":r"$S(M)=\{0,1\}$",
           "lattice":r"$S(M)=\{0\}\cup\{2^n:n\in\mathbb{Z}\}$",
           "line":r"$S(M)=[0,\infty)$"}[kind]
    canvas.text(.575,y-.09,label,color=navy,fontsize=14)
canvas.text(.225,.242,"Dots/lines are exact sets inside finite windows; ellipses continue beyond them.",
            color=grey,fontsize=11)
box=FancyBboxPatch((.045,.045),.91,.154,boxstyle="round,pad=0.012,rounding_size=0.008",
                   linewidth=0,facecolor=pale)
canvas.add_patch(box)
canvas.text(.066,.167,"WHY ZERO CANNOT BE REMOVED  •  every faithful n.s.f. weight",color=red,
            fontsize=12,weight="bold")
canvas.text(.067,.125,r"$0\notin\mathrm{Sp}\Delta\ \Rightarrow\ \log\Delta$ bounded"
            r"$\ \Rightarrow\ \sigma_t=\mathrm{Ad}(e^{itb})$"
            r"$\ \Rightarrow\ \tau=\psi_{e^{-b}}$ is a faithful n.s.f. trace",
            fontsize=15,color=navy)
canvas.text(.067,.079,r"$0<\tau(a)<\infty\ \Rightarrow\ 0\ne p=1_{[\varepsilon,\infty)}(a),"
            r"\ \tau(p)<\infty\ \Rightarrow\ p$ finite  —  impossible in type III.",
            fontsize=14,color=navy)
canvas.text(.055,.014,"MT1–MT4 prove the zero part separately. No factor-existence or spectrum-realization claim is depicted.",
            fontsize=10.5,color=grey)
fig.savefig(A/"modular-trichotomy.png",dpi=180,metadata={"Software":"Original MT proof diagram"})
fig.savefig(A/"modular-trichotomy.svg",metadata={"Date":None,"Creator":"Original MT proof diagram"})
plt.close(fig)
svg=A/"modular-trichotomy.svg"
svg.write_text(svg.read_text(encoding="utf-8"),encoding="utf-8",newline="\n")
data={
 "coordinate":"r on left; log(x) on right; zero displayed in a separate box",
 "plot_window_r":[-3.1,3.1],
 "singleton":{"G":[0],"positive_S":[1],"separate_zero":True},
 "lattice":{"a":"log(2)","lambda":"1/2","displayed_integer_indices":list(range(-4,5)),
            "G":"{n log(2): n in Z}","positive_S":"{2^n: n in Z}",
            "displayed_positive_values":["1/16","1/8","1/4","1/2","1","2","4","8","16"],
            "finite_window_not_full_set":True,"separate_zero":True},
 "continuous":{"G":"R","positive_S":"(0,infinity)","separate_zero":True},
 "native_pixels":[2880,1980],
 "proof":"TYPE_III_MODULAR_TRICHOTOMY_PROOF.md MT1-MT6",
 "no_factor_existence_or_realization_claim":True
}
(D/"FIGURE_DATA.json").write_text(json.dumps(data,indent=2,ensure_ascii=False)+"\n",
                                  encoding="utf-8",newline="\n")
