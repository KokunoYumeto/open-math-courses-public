"""Original exact geometry for AN01-U105, Lemma 1, Theorem 2 and Exercise 4.

GPT-6 Astra (OpenAI), Ultra, October 2026. CC0.
The finite normal arrows sample the proved full nonzero conormal lines.
"""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle, FancyArrowPatch

OUT = Path(__file__).resolve().parent
plt.rcParams.update({"font.size": 12, "svg.fonttype": "none",
                     "axes.spines.top": False, "axes.spines.right": False})
fig, axes = plt.subplots(1, 2, figsize=(12.8, 6.2))
fig.subplots_adjust(left=.085, right=.97, top=.80, bottom=.23, wspace=.32)
fig.suptitle("Analytic fiber detection and support normals", fontsize=20, y=.965)
fig.text(.5, .90, "Cauchy reconstruction controls the whole section; a support boundary forces both signs.",
         ha="center", fontsize=12)
ax = axes[0]
ax.set_title("Complex fiber variable", pad=17, fontweight="bold")
ax.axhline(0, color="#d4dbe2", lw=1)
ax.axvline(0, color="#d4dbe2", lw=1)
ax.add_patch(Rectangle((-23/20, -3/20), 23/10, 3/10,
                       facecolor="#dfedf8", edgecolor="#4284b5", ls="--", lw=1.6))
ax.add_patch(Rectangle((-13/10, -3/10), 13/5, 3/5,
                       fill=False, edgecolor="#176347", lw=2))
ax.plot([-1, 1], [0, 0], color="#172e45", lw=5, solid_capstyle="round")
ax.scatter([-1, 1], [0, 0], c="#172e45", s=23, zorder=4)
for xy1, xy2 in [((-.4,-.3),(.15,-.3)),((1.3,-.15),(1.3,.15)),
                 ((.4,.3),(-.15,.3)),((-1.3,.15),(-1.3,-.15))]:
    ax.add_patch(FancyArrowPatch(xy1, xy2, arrowstyle="-|>", mutation_scale=16,
                                lw=2, color="#176347"))
ax.text(0, .047, r"real carrier $L=[-1,1]$", ha="center", fontsize=12)
ax.text(0, -.105, r"$\Omega_{\rm in}$", ha="center", color="#286997")
ax.annotate(r"positive contour $\Gamma$", xy=(.8,.3), xytext=(.1,.47),
            arrowprops={"arrowstyle":"-", "color":"#176347"}, color="#176347")
ax.annotate("", xy=(1.15, -.1), xytext=(1.3,-.1),
            arrowprops={"arrowstyle":"|-|", "lw":1.1, "color":"#8e3f12"})
ax.annotate(r"gap $3/20$", xy=(1.225,-.1), xytext=(.65,-.52),
            arrowprops={"arrowstyle":"-", "color":"#8e3f12"}, color="#8e3f12")
ax.set(xlim=(-1.55,1.55), ylim=(-.62,.62), xlabel=r"$\operatorname{Re} z$",
       ylabel=r"$\operatorname{Im} z$")
ax.set_xticks([-1.3,-1,0,1,1.3], ["−1.3","−1","0","1","1.3"])
ax.set_yticks([-.3,-.15,0,.15,.3], ["−0.3","−0.15","0","0.15","0.3"])
ax.text(.5, -.27, r"$|(\zeta-y)^{-1}|\leq 20/3$ on $\Omega_{\rm in}$ for $\zeta\in\Gamma$",
        transform=ax.transAxes, ha="center", fontsize=12)

ax=axes[1]
ax.set_title("Real support and cotangent directions", pad=17, fontweight="bold")
y=np.linspace(-1.52,1.52,601)
ax.fill_between(y,-2.05,-y*y,color="#dfedf8")
ax.plot(y,-y*y,color="#246a97",lw=2.2)
ax.axhline(0,color="#d4dbe2",lw=1,zorder=0)
ax.axvline(0,color="#d4dbe2",lw=1,zorder=0)
for q in [-.8,0,.8]:
    base=np.array([q,-q*q])
    normal=np.array([2*q,1.0]);normal/=np.linalg.norm(normal)
    for sign in [-1,1]:
        tip=base+sign*.47*normal
        ax.add_patch(FancyArrowPatch(base,tip,arrowstyle="-|>",mutation_scale=16,
                                    lw=2,color="#8d3a22",zorder=5))
    ax.scatter(*base,s=20,c="#246a97",zorder=6)
ax.text(-1.12,-1.73,r"$F=\{t\leq-y^2\}$",color="#235f87",fontsize=13)
ax.text(.18,.50,r"$\pm\,dt$",color="#8d3a22",fontsize=13)
ax.annotate(r"$\lambda(2y,1),\ \lambda\ne0$",xy=(1.18,-.42),xytext=(.11,1.03),
            arrowprops={"arrowstyle":"-", "color":"#8d3a22"},color="#8d3a22",fontsize=12)
ax.set(xlim=(-1.52,1.52),ylim=(-2.05,1.3),xlabel=r"$y$",ylabel=r"$t$")
ax.set_aspect("equal",adjustable="box")
ax.text(.5,-.27,r"$u(y,t)=H(-t-y^2)$ has exactly these conormal lines.",
        transform=ax.transAxes,ha="center",fontsize=12)
for ext in ["svg","png"]:
    fig.savefig(OUT/("hyperfunction-support-normals."+ext),dpi=160,facecolor="white")
svg=OUT/"hyperfunction-support-normals.svg"
svg.write_bytes(("\n".join(line.rstrip() for line in svg.read_text(encoding="utf-8").splitlines())+"\n").encode())
plt.close(fig)
