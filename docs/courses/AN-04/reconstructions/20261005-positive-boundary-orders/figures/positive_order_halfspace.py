# Original AN03-U032 figure, Codex, September 2026, CC0.
# AN04 correction, 5 October 2026: distinguish the output vector from its scalar pairing.
from pathlib import Path
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch
OUT=Path(__file__).resolve().parent
fig=plt.figure(figsize=(15,10),facecolor="#fbfbf8")
fig.text(.5,.95,"Positive-order mapping with the original half-space support",
         ha="center",fontsize=21,color="#152b3c",weight="bold")
fig.text(.5,.905,
 r"$A_z=(a(1+|\xi|^2)^{(z-m)/2})_\rho+(a-a_\rho),\qquad A_m=a,\qquad 0<m<M$",
 ha="center",fontsize=17,color="#152b3c")
ax=fig.add_axes([.075,.49,.37,.35])
ax.set_facecolor("#eef4f7")
ax.axvline(0,color="#24738b",lw=3)
ax.axvline(3,color="#24738b",lw=3)
ax.axvline(1.3,color="#c59121",ls="--",lw=1.5)
ax.scatter([1.3],[0],s=120,c="#c59121",zorder=3)
ax.set(xlim=(-.25,3.25),ylim=(-2.7,2.7))
ax.set_xticks([0,1.3,3],["0","m","M"])
ax.set_yticks([-2,0,2],["","",""])
ax.set_xlabel(r"$\mathrm{Re}\,z$",fontsize=14)
ax.set_ylabel(r"$\mathrm{Im}\,z=\tau$",fontsize=14)
ax.text(.14,2.13,"Order 0 bound",fontsize=12,color="#195365")
ax.text(2.86,2.13,"Order M bound",ha="right",fontsize=12,color="#195365")
ax.text(1.5,1.28,r"$|F(i\tau)|,\ |F(M+i\tau)|$",ha="center",fontsize=13)
ax.text(1.5,.79,r"$\leq C(1+|\tau|)^L e^{\pi|\tau|/2}p(a)\|f\|_2\|g\|_2$",
        ha="center",fontsize=12)
ax.text(1.5,-.9,r"$e^{\varepsilon(z-m)^2},\ \varepsilon>0$",ha="center",fontsize=16,color="#855f13")
ax.text(1.5,-1.45,"Gaussian damping + maximum principle",ha="center",fontsize=11)
ax.text(1.5,-2.08,"Test-space pairing throughout the strip",ha="center",fontsize=10)
fig.text(.26,.433,"PS12–PS15: integer M > m; strip sketch with illustrative m.",
         ha="center",fontsize=10,color="#456")
right=fig.add_axes([.50,.47,.46,.36]);right.axis("off")
right.text(.02,.95,"Support and exact norm change",fontsize=17,weight="bold",color="#152b3c")
right.text(.02,.76,r"$\ell(\xi)=\sqrt{1+|\xi'|^2}+i\xi_n$",fontsize=17)
right.text(.02,.57,r"$|\ell(\xi)|^2=1+|\xi|^2$",fontsize=17)
right.text(.02,.38,r"$K_{-q}=\frac{1}{\Gamma(q)}\int_0^\infty t^{q-1}E_t(x')\delta(x_n-t)\,dt$",
           fontsize=14)
right.text(.02,.23,r"$E_t(x')=(2\pi)^{-(n-1)}\int e^{ix'\cdot\xi'}e^{-t\sqrt{1+|\xi'|^2}}\,d\xi'$",
           fontsize=13)
right.text(.02,.06,"PS6–PS11: Re q > 0 in the kernel formula; x_n >= 0.",fontsize=11,color="#456")
dia=fig.add_axes([.035,.13,.93,.22]);dia.axis("off")
dia.set(xlim=(0,1),ylim=(0,1))
centers=[.095,.36,.64,.905]
labels=[
 "$f$\n"+r"$\dot{H}_{(0)}(\mathbb{C}^p)$",
 "$u$\n"+r"$\dot{H}_{(s)}(\mathbb{C}^p)$",
 "$T_a u$\n"+r"$\dot{H}_{(s-m)}(\mathbb{C}^q)$",
 "$v$\n"+r"$\dot{H}_{(0)}(\mathbb{C}^q)$"]
for x,label in zip(centers,labels):
 dia.add_patch(FancyBboxPatch((x-.084,.18),.168,.56,
             boxstyle="round,pad=.008",facecolor="#edf3f5",edgecolor="#24738b",lw=1.6))
 dia.text(x,.47,label,ha="center",va="center",fontsize=15,color="#152b3c")
for x,y,label in zip(centers[:-1],centers[1:],
                    [r"$\Lambda_+^{-s}$",r"$T_a$",r"$\Lambda_+^{s-m}$"]):
 dia.annotate("",xy=(y-.1,.46),xytext=(x+.1,.46),
              arrowprops=dict(arrowstyle="->",color="#195365",lw=2))
 dia.text((x+y)/2,.83,label,ha="center",fontsize=15)
dia.text(.5,.0,"PS11, PS15: real multiplier arrows are inverse isometries; the middle arrow has the proved norm bound.",
         ha="center",fontsize=11,color="#456")
fig.text(.5,.071,
 r"$v=\Lambda_+^{s-m}T_a\Lambda_+^{-s}f,\quad F_{f,g}(m)=(v,g)$.  PS16–PS17: full quotient by adjoint duality.",
 ha="center",fontsize=12,color="#152b3c")
fig.text(.5,.035,
 "Original Fourier factor (2pi)^(-n), full residual, all real s, m >= 0, and both vector dimensions are retained.",
 ha="center",fontsize=10,color="#456")
fig.savefig(OUT/"positive_order_halfspace.png",dpi=160,facecolor=fig.get_facecolor())
fig.savefig(OUT/"positive_order_halfspace.svg",facecolor=fig.get_facecolor())
plt.close(fig)
print("Saved positive_order_halfspace.png and .svg")

