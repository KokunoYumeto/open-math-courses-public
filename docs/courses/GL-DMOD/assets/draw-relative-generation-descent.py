from pathlib import Path
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch

base=Path(__file__).resolve().parent
fig, ax=plt.subplots(figsize=(12.8,8.0))
fig.patch.set_facecolor("#f5f7fb")
ax.set(xlim=(0,1),ylim=(0,1));ax.axis("off")
navy="#18324c"; blue="#dfeeff"; green="#e1f2e9"
def box(x,y,w,h,label,size=17,face="white"):
    ax.add_patch(FancyBboxPatch((x-w/2,y-h/2),w,h,boxstyle="round,pad=0.015,rounding_size=0.015",lw=1.5,ec=navy,fc=face))
    ax.text(x,y,label,ha="center",va="center",fontsize=size,color=navy,linespacing=1.6)
def arr(a,b,label=None,shift=0.024,size=13):
    ax.add_patch(FancyArrowPatch(a,b,arrowstyle="-|>",mutation_scale=17,lw=1.8,color=navy))
    if label:ax.text((a[0]+b[0])/2+shift,(a[1]+b[1])/2,label,ha="left",va="center",fontsize=size,color=navy)
ax.text(.5,.965,"Relative analytic generation: product induction and finite descent",ha="center",va="top",fontsize=20,color=navy,fontweight="bold")
box(.24,.83,.34,.12,r"$Q_n\times D'$"+"\n"+r"$\rho_D^*\mathcal{O}(h)=L_n(h,\ldots,h)$",size=16,face=blue)
box(.78,.83,.32,.12,r"$\mathbf{P}^n\times D'$"+"\n"+r"$F\ \mathrm{arbitrary\ coherent}$",size=16,face=blue)
arr((.425,.83),(.602,.83))
ax.text(.515,.866,r"$\rho_D$",ha="center",va="bottom",fontsize=19,color=navy)
ax.text(.515,.788,r"finite $\mathfrak{S}_n$ quotient",ha="center",va="top",fontsize=13,color=navy)
box(.5,.63,.80,.10,r"$\mathcal{O}_{Q_n\times D'}^{\,N}\ \twoheadrightarrow\ \rho_D^*F(h)$",size=23)
ax.text(.5,.711,"Product induction from the proved projective-line gluing theorem",ha="center",va="center",fontsize=14,color=navy)
arr((.14,.562),(.14,.532))
ax.text(.17,.547,"Exact finite pushforward and projection formula for every module",ha="left",va="center",fontsize=11.5,color=navy)
box(.5,.465,.85,.105,r"$B_{D'}^{\,N}\ \twoheadrightarrow\ B_{D'}\otimes F(h)"
    r"\ \overset{\tau_{D'}\otimes1}{\twoheadrightarrow}\ F(h)$",size=22,face=green)
ax.text(.5,.325,r"$B_{D'}=\rho_{D*}\mathcal{O},\qquad"
    r"\tau=\frac{1}{n!}\sum_{\sigma\in\mathfrak{S}_n}\sigma,\qquad\tau(1)=1$",
    ha="center",va="center",fontsize=18,color=navy)
arr((.14,.267),(.14,.212))
ax.text(.17,.244,"Twist by e; fixed algebraic global generators of B(e)",ha="left",va="center",fontsize=11.5,color=navy)
box(.5,.142,.85,.105,r"$\mathcal{O}_{\mathbf{P}^n\times D'}^{\,KN}"
    r"\ \twoheadrightarrow\ B_{D'}(e)^{\,N}"
    r"\ \twoheadrightarrow\ F(h+e)$",size=22)
ax.text(.5,.026,"Every arrow is defined on the entire product; the split trace is defined at branching points.\n"
    "Proof: (5.8m)–(5.8y).  Original CC0 diagram; drawing source retained.",
    ha="center",va="center",fontsize=13,color=navy,linespacing=1.5)
fig.savefig(base/"relative-generation-descent-mechanism.png",dpi=160,bbox_inches="tight",facecolor=fig.get_facecolor())
fig.savefig(base/"relative-generation-descent-mechanism.svg",bbox_inches="tight",facecolor=fig.get_facecolor())

