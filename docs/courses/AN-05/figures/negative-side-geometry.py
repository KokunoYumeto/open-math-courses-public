"""Exact Lorentzian example and polarized-flow direction for G12--G36."""
from pathlib import Path
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

A = 2.0
plt.rcParams.update({"font.family": "DejaVu Sans", "font.size": 12})
fig, (left, right) = plt.subplots(1, 2, figsize=(13.5, 6.8))
fig.subplots_adjust(left=0.075, right=0.975, bottom=0.25, top=0.77, wspace=0.26)
x2 = np.linspace(-0.3, 0.3, 601)
w = 1 - A*x2**2
left.axhspan(-0.15, 0, color="#fce9ce")
left.axhspan(0, 0.03, color="#dcecf5")
left.axhline(0, color="#294c63", lw=2)
for h,color in zip([0.03,0.06,0.09],["#bd8336","#a25d1b","#794717"]):
    left.plot(x2,-h/w, color=color, lw=2.2, label=rf"$y_1=\Phi=-{h:g}$")
grid_x2,grid_x1 = np.meshgrid(np.linspace(-0.27,0.27,7),np.linspace(-0.13,-0.012,5))
grid_w = 1-A*grid_x2**2
c = grid_w**2-4*A*A*grid_x1**2*grid_x2**2
assert np.min(c)>0.6
vx1 = grid_w/c
vx2 = 2*A*grid_x1*grid_x2/c
vnorm = np.hypot(vx1,vx2)
left.quiver(grid_x2,grid_x1,vx2/vnorm,vx1/vnorm,color="#3d715f",alpha=0.7,
            angles="xy",scale_units="xy",scale=50,width=0.003)
left.text(0.0,0.011,r"$S=\{x_1=0\}$; positive side above",ha="center",fontsize=11)
left.text(-0.27,-0.144,r"Arrows: direction of exact $V$; $V\Phi=1$",fontsize=10)
left.set(xlabel=r"$x_2$ with $x_3=0$",ylabel=r"$x_1$",
         xlim=(-0.31,0.31),ylim=(-0.15,0.03),title="Same oriented zero surface, adapted negative levels")
left.legend(frameon=False,loc="upper center",bbox_to_anchor=(0.5,1.075),
            ncol=3,fontsize=10)
left.set_title("Same oriented zero surface, adapted negative levels",pad=50)

t = np.linspace(-0.2,0.2,501)
for h,color in zip([0,0.05,0.1],["#294c63","#be822f","#9e581b"]):
    phi = -h+8*A*h*t**2
    right.plot(t,phi,color=color,lw=2.5,label=rf"$x_1=-h,\ h={h:g}$")
right.axvline(0,color="#687781",ls=":",lw=1)
right.text(0.0,-0.025,r"$(H_p\Phi)(x(0),\xi)=0$",ha="center",fontsize=11)
right.text(0.0,-0.073,r"$(H_p^2\Phi)(x(0),\xi)=16Ah\geq0$",ha="center",fontsize=12)
right.set(xlabel=r"Hamilton parameter $t$",ylabel=r"$\Phi(x(t))$",
          title="Exact tangent characteristic curves")
right.legend(frameon=False,loc="upper center",bbox_to_anchor=(0.5,1.075),
             ncol=3,fontsize=10)
right.set_title("Exact tangent characteristic curves",pad=50)
for ax in (left,right): ax.grid(alpha=0.15)
fig.suptitle(r"$p=\xi_1^2-\xi_2^2+\xi_3^2,\quad"
             r"\Phi=x_1(1-A(x_2^2+x_3^2)),\quad A=2$",
             fontsize=16,y=0.98)
fig.text(0.5,0.14,r"Right: $\xi=(0,1,1)$, $x(t)=(-h,-2t,2t)$, "
         r"$p=0$, $\Phi(x(t))=-h+8Ah t^2$; the surface curve ($h=0$) remains flat.",
         ha="center",fontsize=11)
fig.text(0.5,0.087,r"Left: $V=(w,2Ax_1x_2,-2Ax_1x_3)/p(d\Phi)$; "
         "level graphs and arrow directions are exact formulas.",ha="center",fontsize=11)
fig.text(0.5,0.025,"An explicit proved example, not the general symbol's characteristic geometry.\n"
         "Source: Hörmander IV, Lemma 28.4.2 and adapted-coordinate paragraph, printed pp.246--247; G12--G36.",
         ha="center",fontsize=10)
path=Path(__file__).with_name("negative-side-geometry.png")
fig.savefig(path,dpi=180,bbox_inches="tight",metadata={
    "Title":"Exact negative-side Hamilton geometry and polarized flow",
    "Description":"Private receiving geometry, G12--G36",
    "Software":"Matplotlib"})
plt.close(fig)
print(path.resolve())
