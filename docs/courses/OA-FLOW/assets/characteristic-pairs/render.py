"""Original characteristic-pair diagrams and exact arithmetic checks (CC0-1.0).

Run: python render.py
Needs Python 3, numpy and matplotlib. Uses installed runtime fonts without copying
font files. All mathematical formulas are proved in ../../src/OA-FLOW-CPP.md. Diagnostic
finite arithmetic is a reproducibility check, not a substitute for those proofs.
"""
from pathlib import Path
from itertools import permutations, product
import json
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, Rectangle, Circle
from matplotlib.colors import ListedColormap

HERE = Path(__file__).resolve().parent
plt.rcParams.update({
    "font.family": "DejaVu Sans", "mathtext.fontset": "dejavusans",
    "font.size": 12, "svg.fonttype": "none", "svg.hashsalt": "characteristic-pairs-20261008",
    "axes.spines.top": False, "axes.spines.right": False,
    "savefig.facecolor": "#ffffff",
})
INK = "#172d40"
BLUE = "#126b8f"
GOLD = "#b76712"
PALE = "#eef5f8"
COLORS = ["#e7edf2", "#77bdd6", "#69b7a6", "#d5ad69", "#bc8ab5"]

def arrow(ax, a, b, label=None, offset=(0, .16), color=BLUE, fontsize=13):
    ax.annotate("", xy=b, xytext=a,
                arrowprops=dict(arrowstyle="->", color=color, lw=1.7,
                                shrinkA=2, shrinkB=2))
    if label:
        ax.text((a[0]+b[0])/2+offset[0], (a[1]+b[1])/2+offset[1],
                label, ha="center", va="center", color=color, fontsize=fontsize)

def txt(ax, x, y, s, size=15, **kw):
    ax.text(x, y, s, ha="center", va="center", fontsize=size, color=INK, **kw)

def save(fig, stem):
    fig.savefig(HERE/f"{stem}.png", dpi=180, bbox_inches="tight")
    fig.savefig(HERE/f"{stem}.svg", bbox_inches="tight",
                metadata={"Date": None, "Creator": "Original CC0 characteristic-pair diagram"})
    plt.close(fig)

def compatible_diagram():
    fig, axes = plt.subplots(1, 2, figsize=(15.6, 7.2),
                             gridspec_kw={"width_ratios":[1.12,1]})
    fig.subplots_adjust(left=.025, right=.98, top=.84, bottom=.11, wspace=.12)
    fig.suptitle("Compatible lifts: changing a phase preserves the extension",
                 fontsize=20, fontweight="bold", color=INK, y=.96)
    fig.text(.5,.905,"Exact maps from CP2, CP7 and CP10; no continuity of a Borel section is assumed.",
             ha="center", color=INK, fontsize=12)
    ax=axes[0]; ax.set(xlim=(-.15,8.15), ylim=(0,6)); ax.axis("off")
    txt(ax,4,5.75,"A gauge gives an isomorphism over the same kernel and quotient",12)
    xs=[.15,1.35,4,6.65,7.85]
    for y, middle in [(4.8,r"$E_{\mu^f}$"),(3.1,r"$E_\mu$")]:
        for x,s in zip(xs,[r"$1$",r"$\mathbb{T}$",middle,r"$N$",r"$1$"]):
            txt(ax,x,y,s,18)
        arrow(ax,(.4,y),(1.06,y))
        arrow(ax,(1.68,y),(3.4,y),r"$i$",offset=(0,.23))
        arrow(ax,(4.52,y),(6.33,y),r"$q$",offset=(0,.23))
        arrow(ax,(6.95,y),(7.58,y))
    arrow(ax,(1.35,4.45),(1.35,3.48),r"$\mathrm{id}$",offset=(-.32,0))
    arrow(ax,(4,4.42),(4,3.48),r"$T_f$",offset=(.34,0))
    arrow(ax,(6.65,4.45),(6.65,3.48),r"$\mathrm{id}$",offset=(.32,0))
    ax.add_patch(FancyBboxPatch((.35,.25),7.3,2.05,
                   boxstyle="round,pad=.15",fc=PALE,ec="#c5d7df"))
    txt(ax,4,1.88,r"$T_f(z,n)=(zf(n),n),\qquad f(e)=1$",15)
    txt(ax,4,1.21,r"$\mu^f(a,b)=\mu(a,b)\,\frac{f(a)f(b)}{f(ab)}$",16)
    txt(ax,4,.51,r"$\lambda^f(a,g)=\lambda(a,g)\,\frac{f(g^{-1}ag)}{f(a)}$",16)

    ax=axes[1]; ax.set(xlim=(-.4,7),ylim=(0,6)); ax.axis("off")
    txt(ax,3.3,5.75,"The section need not intertwine conjugation",13)
    txt(ax,.75,4.7,r"$g^{-1}ag$",17)
    txt(ax,5.45,4.7,r"$a$",17)
    arrow(ax,(1.55,4.7),(5.05,4.7),r"$c_g:n\mapsto gng^{-1}$",
          offset=(0,.29),fontsize=14)
    arrow(ax,(.75,4.35),(.75,3.0),r"$s$",offset=(-.3,0))
    arrow(ax,(5.45,4.35),(5.45,3.86),r"$s$",offset=(.3,0))
    txt(ax,.75,2.65,r"$s(g^{-1}ag)$",16)
    txt(ax,5.45,3.55,r"$s(a)$",16)
    arrow(ax,(5.45,3.3),(5.45,2.98),r"$\times\lambda(a,g)$",
          offset=(-1.0,0),color=GOLD,fontsize=13)
    txt(ax,5.45,2.65,r"$\lambda(a,g)s(a)$",16)
    arrow(ax,(1.8,2.65),(4.20,2.65),r"$\beta_g$",
          offset=(0,.23),fontsize=16)
    txt(ax,3.32,2.04,r"$\beta_g(s(g^{-1}ag))=\lambda(a,g)\,s(a)$",15)
    ax.add_patch(FancyBboxPatch((-.05,.24),6.62,1.22,
                   boxstyle="round,pad=.15",fc="#fff5e9",ec="#e1c7a1"))
    txt(ax,3.25,1.02,r"$n\in N:\quad\beta_n=\mathrm{Ad}\,s(n)$",16)
    txt(ax,3.25,.5,r"$\lambda(m,n)=\mu(n,n^{-1}mn)\,/\,\mu(m,n)$",14)
    fig.text(.5,.035,"The right diagram includes the scalar correction explicitly. "
             "Inner compatibility fixes the action of every n in N.",
             ha="center",fontsize=12,color=INK)
    save(fig,"compatible-lifts")

def cyclic_diagram():
    fig,axes=plt.subplots(1,2,figsize=(14.8,6.8),gridspec_kw={"width_ratios":[1,1.12]})
    fig.subplots_adjust(left=.05,right=.97,top=.77,bottom=.16,wspace=.21)
    fig.suptitle("One phase determines every cyclic coordinate",
                 fontsize=21,fontweight="bold",color=INK,y=.995)
    fig.text(.5,.88,r"$p=5,\quad\zeta=e^{4\pi i/5},\quad"
             r"\lambda(5k,r)=\zeta^{kr},\quad\mu=1$",ha="center",fontsize=18,color=INK)
    ax=axes[0];ax.set_aspect("equal")
    ax.set(xlim=(-1.5,1.75),ylim=(-1.45,1.45));ax.axis("off")
    ax.add_patch(Circle((0,0),1,fill=False,edgecolor="#b8c6cf",lw=1.3))
    roots=np.exp(2j*np.pi*np.arange(5)/5)
    path=[(2*r)%5 for r in range(6)]
    for r in range(5):
        z0,z1=roots[path[r]],roots[path[r+1]]
        arrow(ax,(.88*z0.real,.88*z0.imag),(.88*z1.real,.88*z1.imag),color=BLUE)
    for j,z in enumerate(roots):
        ax.scatter([z.real],[z.imag],s=180,c=[COLORS[j]],edgecolor=INK,zorder=5)
        r=(3*j)%5  # inverse of 2 modulo 5
        label=r"$r=0,5$" if j==0 else rf"$r={r}$"
        txt(ax,1.43 if j==0 else 1.26*z.real,
            .03 if j==0 else 1.26*z.imag,label,14)
    txt(ax,0,-1.38,r"Each arrow multiplies by $\zeta$; $\zeta^5=1$.",12)
    txt(ax,0,1.38,"The five successive phases",14)
    ax=axes[1]
    residues=np.array([[(2*k*r)%5 for r in range(6)] for k in range(5)])
    ax.imshow(residues,cmap=ListedColormap(COLORS),vmin=-.5,vmax=4.5,
              interpolation="nearest",aspect="equal")
    ax.set_xticks(range(6),[str(r) for r in range(6)])
    ax.set_yticks(range(5),[str(k) for k in range(5)])
    ax.set_xlabel(r"$r$ (power of the automorphism)",fontsize=13,labelpad=8)
    ax.set_ylabel(r"$k$ (implementer $v^k$ of $\theta^{5k}$)",fontsize=13,labelpad=8)
    ax.set_title(r"Exact exponent residue $2kr\ \mathrm{mod}\ 5$",fontsize=14,pad=15,color=INK)
    for k,r in product(range(5),range(6)):
        ax.text(r,k,str(residues[k,r]),ha="center",va="center",fontsize=17,color=INK)
    ax.set_xticks(np.arange(-.5,6,.5)[::2],minor=True)
    ax.set_yticks(np.arange(-.5,5,.5)[::2],minor=True)
    ax.grid(which="minor",color="white",linewidth=2)
    ax.tick_params(which="minor",bottom=False,left=False)
    ax.add_patch(Rectangle((4.5,-.5),1,5,fill=False,lw=3,edgecolor=GOLD,clip_on=False))
    ax.text(5,-1.0,r"$r=5:\ \lambda(5k,5)=1$",ha="right",fontsize=12,color=GOLD)
    fig.text(.5,.042,"A cell with residue j means exp(2πij/5). "
             "The highlighted column is the inner-action constraint, not a numerical approximation.",
             ha="center",fontsize=12,color=INK)
    save(fig,"cyclic-phase")

def exact_checks():
    group=list(permutations(range(3)));e=(0,1,2)
    def mul(a,b):return tuple(a[b[i]] for i in range(3))
    def inv(a):return tuple(a.index(i) for i in range(3))
    def conj(g,a):return mul(mul(inv(g),a),g)
    trans23=(0,2,1)
    def f(a):return int(a==trans23)
    def lam(a,g):return (f(conj(g,a))-f(a))%4
    def mu(a,b):return (f(a)+f(b)-f(mul(a,b)))%4
    checks=0
    for a,b,c in product(group,repeat=3):
        assert (mu(a,b)+mu(mul(a,b),c)-mu(a,mul(b,c))-mu(b,c))%4==0
        assert (lam(a,mul(b,c))-lam(a,b)-lam(conj(b,a),c))%4==0
        assert (lam(a,c)+lam(b,c)-lam(mul(a,b),c)
                -mu(conj(c,a),conj(c,b))+mu(a,b))%4==0
        checks+=3
    for m,n in product(group,repeat=2):
        assert (lam(m,n)-mu(n,conj(n,m))+mu(m,n))%4==0
        checks+=1
    for x in group:
        assert lam(e,x)==lam(x,e)==mu(e,x)==mu(x,e)==0
        checks+=4
    a=(1,0,2);g=(1,2,0);h=a
    lhs=lam(a,mul(g,h))
    correct=(lam(a,g)+lam(conj(g,a),h))%4
    wrong=(lam(a,g)+lam(mul(mul(g,a),inv(g)),h))%4
    assert (lhs,correct,wrong)==(1,1,3)
    cyclic=0
    for p in range(1,8):
        for j in range(p):
            for k,l,r,s in product(range(-3,4),repeat=4):
                # Residues for lambda(kp,r)=exp(2pi i*j*k*r/p).
                assert (j*k*(r+s)-j*k*r-j*k*s)%p==0
                assert (j*(k+l)*r-j*k*r-j*l*r)%p==0
                assert (j*k*l*p)%p==0
                cyclic+=3
    report={
        "meaning":"Exact finite regression checks; the manuscript supplies the proofs for arbitrary groups and all integers.",
        "s3":{"composition":"right to left","phase_encoding":"i to the integer residue modulo 4",
              "axiom_checks":checks,"counterexample":{"lhs":lhs,"correct_rhs":correct,"opposite_conjugation_rhs":wrong}},
        "cyclic":{"p_values":[1,2,3,4,5,6,7],"all_root_indices":True,"integer_sample":[-3,3],
                  "exact_residue_checks":cyclic,"p0":"Only normalized lambda(0,r)=1 and mu(0,0)=1; proof CP30.",
                  "figure_residues":[[(2*k*r)%5 for r in range(6)] for k in range(5)]},
    }
    (HERE/"diagnostics.json").write_text(json.dumps(report,indent=2)+"\n",encoding="utf-8")
    print(json.dumps(report,indent=2))

if __name__=="__main__":
    exact_checks()
    compatible_diagram()
    cyclic_diagram()

