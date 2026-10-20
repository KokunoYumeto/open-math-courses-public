"""Reproducible original diagram of transverse directional solution fibres."""
from pathlib import Path
from fractions import Fraction as Q
import json
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Polygon

root = Path(__file__).resolve().parent
matplotlib.rcParams.update({"font.family": "DejaVu Sans", "font.size": 18,
                           "svg.hashsalt": "finite-directional-fibres"})
blue, red, grey = "#145da0", "#a12b3a", "#57657a"
fig, axes = plt.subplots(3, 1, figsize=(7.4, 15.8),
    gridspec_kw={"height_ratios": [1.15, 1.25, 1]})
fig.subplots_adjust(hspace=.64, left=.17, right=.95, top=.96, bottom=.025)
a = axes[0]
x = np.linspace(0, .48, 401)
a.plot(x, x**1.5, color=red, lw=2.8)
a.plot(x, -x**1.5, color=red, lw=2.8)
xw = np.linspace(-.48, .48, 401)
a.fill_between(xw, -.53, -np.abs(xw), color=blue, alpha=.15)
a.plot(xw, -np.abs(xw), "--", color=blue, lw=1.8)
a.scatter([0], [0], color=red, zorder=5, s=50)
a.text(.15, .35, r"$S:\ t^2=x^3$", color=red)
a.text(-.38, -.43, r"$W_1:\ t<-|x|$", color=blue)
a.set(xlim=(-.48,.48), ylim=(-.53,.52), xlabel=r"$x$ (real slice)",
      ylabel=r"$t=\operatorname{Re}t$")
a.set_xticks([-.4,0,.4]);a.set_yticks([-.4,0,.4])
a.set_title("A. Open inner cone at the cusp", fontsize=19, pad=17)
a.axhline(0, color=grey, lw=.7);a.axvline(0, color=grey, lw=.7)
a.grid(alpha=.15)

a = axes[1]
rho = 1/32
for sign, color in [(1,blue),(-1,red)]:
    h = sign/8
    xx = np.linspace(-.16,rho,600)
    yy = np.where(xx<=0, rho, np.sqrt(np.maximum(0,rho*rho-xx*xx)))
    a.fill_between(xx,h-yy,h+yy,color=color,alpha=.09)
    a.plot(xx,h-yy,color=color,lw=1.4)
    a.plot(xx,h+yy,color=color,lw=1.4)
    xc = np.linspace(-rho/2,rho,300)
    yc = np.where(xc<=0,rho,np.sqrt(np.maximum(0,rho*rho-xc*xc)))
    a.fill_between(xc,h-yc,h+yc,color=color,alpha=.30)
    a.plot([-rho/2,-rho/2],[h-rho,h+rho],color=color,lw=2)
    a.scatter([0],[h],color=color,s=45)
    a.annotate("",xy=(-.157,h),xytext=(-.12,h),
               arrowprops={"arrowstyle":"->","color":color,"lw":1.6})
    a.text(-.148,h+.048,r"$h_+=i/8$" if sign==1 else r"$h_-=-i/8$",
           color=color,fontsize=18)
a.set(xlim=(-.165,.047),ylim=(-.21,.21),xlabel=r"$\operatorname{Re}t$",
      ylabel=r"$\operatorname{Im}t$")
a.set_xticks([-.125,0]);a.set_xticklabels([r"$-1/8$","0"])
a.set_yticks([-.125,0,.125]);a.set_yticklabels([r"$-1/8$","0",r"$1/8$"])
a.set_title("B. Disjoint caps at $x_*=-1/4$\n$\\rho=1/32$",fontsize=19,pad=17)
a.grid(alpha=.15)

a = axes[2];a.axis("off")
a.set_title("C. The comparison after finite Hom",fontsize=19,pad=14)
lines = [
    r"$\operatorname{Ext}^{k}_{E}(M,\mathcal{C}_{p_0})$",
    r"$\downarrow\ \simeq$",
    r"$\mathcal{H}^{k+1}(\mathscr{L})_0$",
    r"$\downarrow\ \simeq$",
    r"$\oplus_j\operatorname{Ext}^{k}_{E}(M_{p_j},\mathcal{C}_{p_j})$",
    r"$=\ \oplus_j\mathbf{C}^{r_j}\quad(k=0)$",
    r"$=\ 0\quad(k>0)$"]
for yy,txt in zip(np.linspace(.94,.02,len(lines)),lines):
    a.text(.5,yy,txt,ha="center",va="center",fontsize=19,transform=a.transAxes)
for ax in axes[:2]:
    ax.spines[["top","right"]].set_visible(False)
fig.savefig(root/"finite-directional-fibres.png",dpi=160,metadata={"Software":"Matplotlib"})
fig.savefig(root/"finite-directional-fibres.svg",metadata={"Date":None,"Creator":"Open mathematics course figures"})
plt.close(fig)
data = {
  "curve":"t^2=x^3", "real_slice_only_in_panel_A":True,
  "x_star":"-1/4", "normal_roots":["i/8","-i/8"],
  "normalized_conormals":[["1","3i/4"],["1","-3i/4"]],
  "rho":str(Q(1,32)), "imaginary_separation":str(Q(1,4)),
  "four_rho":str(4*Q(1,32)), "cap_real_interval":["-1/64","1/32"],
  "cap_shape":"|Im T|<=rho for Re T<=0; |T|<=rho for Re T>=0",
  "opens_extend_to_negative_real_infinity":True,
  "proof_locators":["FD.11","FD.22","FD.29","FD.32","FD.34"],
  "source_context":"https://www.kurims.kyoto-u.ac.jp/~kenkyubu/kashiwara/HolIII.pdf"
}
(root/"finite-directional-fibres-exact-data.json").write_text(
    json.dumps(data,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
