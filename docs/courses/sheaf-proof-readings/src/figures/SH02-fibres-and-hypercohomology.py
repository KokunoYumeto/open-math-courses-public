"""Proper fibres and hypercohomology: exact maps and hypotheses.

Original mathematical illustration: GPT-6 Astra (OpenAI), Ultra, 2026-10-06.
CC0-1.0. Uses only Python's standard library and Matplotlib.
Installed location: src/figures/SH02-fibres-and-hypercohomology.py.
Output: figures/SH02-fibres-and-hypercohomology.svg.
"""
from pathlib import Path
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle, FancyBboxPatch, FancyArrowPatch

plt.rcParams.update({
    "font.family": "DejaVu Sans",
    "font.size": 12,
    "svg.hashsalt": "SH02-fibres-and-hypercohomology-v1",
})
ROOT = Path(__file__).resolve().parents[2]
OUT = ROOT / "figures" / "SH02-fibres-and-hypercohomology.svg"
OUT.parent.mkdir(parents=True, exist_ok=True)
BLUE, PURPLE, TEAL = "#216394", "#703b88", "#087f74"
INK, MUTED = "#172434", "#4d5966"
fig = plt.figure(figsize=(17, 12), facecolor="#ffffff")
fig.suptitle("Restriction determines the comparison maps", x=.5, y=.977,
             fontsize=22, fontweight="bold", color=INK)
A = fig.add_axes([.035, .515, .93, .405])
B = fig.add_axes([.035, .04, .93, .43])
for ax in (A, B):
    ax.set(xlim=(0, 1), ylim=(0, 1))
    ax.axis("off")
    ax.add_patch(FancyBboxPatch((0, 0), 1, 1,
        boxstyle="round,pad=0.006,rounding_size=0.015",
        linewidth=1.2, edgecolor="#cbd4dc", facecolor="#f8fafc",
        transform=ax.transAxes, clip_on=False))
def text(ax, x, y, s, size=13, color=INK, **kw):
    return ax.text(x, y, s, fontsize=size, color=color, transform=ax.transAxes, **kw)
def arrow(ax, a, b, color=INK, style="-|>", lw=1.6, **kw):
    ax.add_patch(FancyArrowPatch(a, b, arrowstyle=style, mutation_scale=14,
                 linewidth=lw, color=color, transform=ax.transAxes, **kw))

text(A, .022, .935, "A  Proper fibres: the map is section restriction", 17, fontweight="bold")
text(A, .022, .856, "Exact model shown:  " + r"$X=[-1,1]\times\mathbb{R},\quad f(u,t)=t$", 13)
# Product model, drawn with t horizontal and u vertical; only a finite window is shown.
x0, x1, y0, y1 = .045, .355, .425, .775
cx = (x0+x1)/2
A.add_patch(Rectangle((x0, y0), x1-x0, y1-y0, facecolor="#edf1f5",
                     edgecolor="none", transform=A.transAxes))
for half, color, alpha in ((.11, BLUE, .15), (.055, TEAL, .24)):
    A.add_patch(Rectangle((cx-half, y0), 2*half, y1-y0,
                         facecolor=color, edgecolor="none", alpha=alpha,
                         transform=A.transAxes))
    for xx in (cx-half,cx+half):
        A.plot([xx,xx],[y0,y1],color=color,lw=1,ls="--",alpha=.6,transform=A.transAxes)
A.plot([x0,x1],[y0,y0],color=MUTED,lw=1.2,transform=A.transAxes)
A.plot([x0,x1],[y1,y1],color=MUTED,lw=1.2,transform=A.transAxes)
for yy in (y0,y1):
    arrow(A,(x0+.01,yy),(x0-.012,yy),color=MUTED,lw=1.1)
    arrow(A,(x1-.01,yy),(x1+.012,yy),color=MUTED,lw=1.1)
A.plot([cx,cx],[y0,y1],color=PURPLE,lw=4,transform=A.transAxes,zorder=5)
A.scatter([cx,cx],[y0,y1],s=22,color=PURPLE,transform=A.transAxes,zorder=6)
text(A,.057,.70,r"$f^{-1}V_1$",12,BLUE)
text(A,.24,.60,r"$f^{-1}V_2$",12,TEAL)
text(A,cx+.009,.735,r"$X_0$",12,PURPLE,fontweight="bold")
text(A,.022,.76,r"$u=1$",10,MUTED,ha="right")
text(A,.022,.418,r"$u=-1$",10,MUTED,ha="right")
arrow(A,(.32,.41),(.32,.30),BLUE,lw=1.8)
text(A,.337,.355,r"$f$",15,BLUE)
arrow(A,(x0-.01,.26),(x1+.02,.26),MUTED,lw=1.1)
A.plot([cx-.11,cx+.11],[.285,.285],color=BLUE,lw=4,transform=A.transAxes)
A.plot([cx-.055,cx+.055],[.26,.26],color=TEAL,lw=4,transform=A.transAxes)
for half, yy, color in ((.11,.285,BLUE),(.055,.26,TEAL)):
    A.scatter([cx-half,cx+half],[yy,yy],s=29,facecolor="#f8fafc",
              edgecolor=color,linewidth=1.5,transform=A.transAxes,zorder=4)
A.scatter([cx],[.26],color=PURPLE,s=28,transform=A.transAxes,zorder=5)
text(A,cx,.192,r"$y=0$",12,PURPLE,ha="center")
text(A,.035,.192,r"$Y=\mathbb{R}$",11,MUTED)
text(A,cx-.11,.327,r"$V_1=(-2,2)$",11,BLUE)
text(A,cx+.02,.327,r"$V_2=(-1,1)$",11,TEAL)
text(A,.354,.235,r"$t$",12,MUTED)
text(A,.035,.085,"Smaller base intervals give smaller inverse images.\n"
     "The vertical segment is the compact fibre; horizontal arrows\n"
     "indicate the unbounded product direction.",11,MUTED,va="center")

text(A,.41,.854,r"General theorem: $f:X\to Y$ proper; $X,Y$ locally compact Hausdorff.",13,fontweight="bold")
text(A,.41,.786,r"$k$ commutative, $F\in D^+(k_X)$; arbitrary $k$-modules.",13)
text(A,.41,.714,r"$X_y=f^{-1}(y)$ is compact.",14,PURPLE)
text(A,.41,.643,r"For every open $W\supseteq X_y$, some open $V\ni y$ has $f^{-1}V\subseteq W$.",13)
text(A,.41,.562,r"Take a bounded-below injective resolution $F\to I^\bullet$.",12,MUTED)
text(A,.445,.461,r"$\mathrm{colim}_{V\ni y}\,\Gamma(f^{-1}V;I^\bullet)$",15,ha="left")
text(A,.965,.461,r"$\Gamma(X_y;I^\bullet|_{X_y})$",15,ha="right")
arrow(A,(.713,.478),(.777,.478),BLUE)
text(A,.745,.532,"restriction",10,BLUE,ha="center")
text(A,.745,.427,r"$\cong$",15,BLUE,ha="center")
text(A,.70,.308,r"$(Rf_*F)_y\ \cong\ R\Gamma(X_y;F|_{X_y})$",20,BLUE,ha="center")
text(A,.41,.195,"Compact-germ gluing gives the restriction comparison.",12,MUTED)
text(A,.41,.137,r"The restricted terms $I^j|_{X_y}$ are acyclic and compute derived sections.",12,MUTED)
text(A,.41,.061,"The product picture illustrates neighborhoods only; the theorem needs no manifold structure.",11,MUTED)

text(B,.022,.93,"B  Hypercohomology: a natural edge, with an additional isomorphism criterion",17,fontweight="bold")
text(B,.025,.853,r"$X$ any topological space; $K\in D^+(k_X)$ and $\mathcal{H}^qK=0$ for $q<a$.",13)
text(B,.045,.762,r"$\tau_{\leq q-1}K\ \longrightarrow\ \tau_{\leq q}K\ \longrightarrow\ \mathcal{H}^qK[-q]\ \longrightarrow\ (\tau_{\leq q-1}K)[1]$",17)
text(B,.045,.673,r"$E_2^{p,q}=H^p(X;\mathcal{H}^qK)\ \Longrightarrow\ H^{p+q}R\Gamma(X;K)$",16)
text(B,.59,.673,r"$p\geq0,\quad q\geq a$",14,MUTED)
text(B,.045,.587,r"$0=F_{a-1}T^n\subseteq F_aT^n\subseteq\cdots\subseteq F_nT^n=T^n,\quad T^n=H^nR\Gamma(X;K)$",15)
text(B,.94,.587,r"$(n\geq a)$",12,MUTED,ha="right")
text(B,.045,.521,r"For $n<a$, $T^n=0$.  Each degree has a finite filtration.",11,MUTED)

# Commuting triangle: only the horizontal edge gains an isomorphism under acyclicity.
text(B,.215,.365,r"$H^nR\Gamma(X;K)$",21,ha="center")
text(B,.755,.365,r"$\Gamma(X;\mathcal{H}^nK)$",21,ha="center")
text(B,.755,.118,r"$H^n(K_x)$",21,ha="center")
arrow(B,(.345,.386),(.62,.386),BLUE,lw=2)
text(B,.483,.427,r"$\alpha_n$: natural edge (always defined)",12,BLUE,ha="center")
arrow(B,(.755,.33),(.755,.184),PURPLE,lw=2)
text(B,.777,.242,"section → germ",12,PURPLE,va="center")
arrow(B,(.30,.325),(.643,.15),TEAL,lw=2)
text(B,.43,.242,"restriction",12,TEAL,rotation=-13,ha="center",
     bbox={"facecolor":"#f8fafc","edgecolor":"none","pad":1.5})
text(B,.055,.174,r"$\alpha_n$ is induced by $K\to\tau_{\geq n}K$.",12,BLUE)
text(B,.055,.111,r"$H^nR\Gamma(X;\tau_{\geq n}K)\cong\Gamma(X;\mathcal{H}^nK)$",12,BLUE)
text(B,.055,.047,"The triangle commutes: both routes restrict the same class.",11,TEAL)

fig.text(.50,.012,
         r"Extra condition: if $H^p(X;\mathcal{H}^qK)=0$ for every $p>0,q$, then $\alpha_n$ is an isomorphism.  The germ map need not be.",
         ha="center",fontsize=13,color=PURPLE)

fig.savefig(OUT,bbox_inches="tight",metadata={
    "Date":None,
    "Title":"Proper fibre restriction and the natural hypercohomology edge",
    "Creator":"GPT-6 Astra (OpenAI), Ultra",
    "Description":"Panel A shows the exact proper product model [-1,1] x R and the canonical compact-fibre restriction comparison. Panel B shows good truncations, the finite bounded-below filtration, and the edge/restriction triangle; only the edge gains an isomorphism under cohomology-sheaf acyclicity.",
    "Rights":"CC0 1.0 Universal; original mathematical illustration."
})

