"""Exact matrix illustration for Exercise22.112; no sampled elliptic values."""
from pathlib import Path
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle

fig, ax = plt.subplots(figsize=(13.0, 8.5), dpi=180)
fig.patch.set_facecolor("white")
ax.set_xlim(0, 13)
ax.set_ylim(0, 8.5)
ax.axis("off")
ink, muted = "#152136", "#52627a"
ax.text(6.5, 8.12, "An elliptic curve, two punctures and one endpoint path",
        ha="center", va="center", fontsize=20, fontweight="bold", color=ink)
ax.text(6.5, 7.55, r"$U=E\setminus\{O,Q\},\quad D=\{P_0,P_1\}$",
        ha="center", fontsize=20, color=ink)
ax.text(6.5, 7.02, "de Rham dimension 4    •    Betti rank 4",
        ha="center", fontsize=16, color=muted)

xs = [3.0, 5.7, 8.4, 11.1]
ys = [5.35, 4.35, 3.35, 2.35]
headers = [r"$\lambda_1$", r"$\lambda_2$", r"$\delta_Q$", r"$\gamma:P_0\to P_1$"]
subheaders = ["complete cycle", "complete cycle", "positive puncture loop", "endpoint path"]
rows = [r"$\alpha=dx/y$", r"$\beta=x\,dx/y$", r"$\rho$", r"$dF$"]
values = [[r"$\omega_1$",r"$\omega_2$","0",r"$u$"],
          [r"$-\eta_1$",r"$-\eta_2$","0",r"$v$"],
          [r"$r_1$",r"$r_2$",r"$2\pi i$",r"$w$"],
          ["0","0","0","1"]]
for x, h, sh in zip(xs, headers, subheaders):
    ax.text(x, 6.33, h, ha="center", fontsize=18, color=ink)
    ax.text(x, 5.98, sh, ha="center", fontsize=11, color=muted)
for i, y in enumerate(ys):
    ax.text(0.95, y, rows[i], ha="center", va="center", fontsize=18, color=ink)
    for j, x in enumerate(xs):
        zero = values[i][j] == "0"
        color = "#f7f9fc" if zero else "#eef5ff"
        if (i,j)==(2,2): color="#fff3df"
        if (i,j)==(3,3): color="#eaf8f0"
        ax.add_patch(Rectangle((x-1.12,y-0.39),2.24,0.78,facecolor=color,edgecolor="#d1dbe8"))
        ax.text(x,y,values[i][j],ha="center",va="center",fontsize=24,
                color="#718198" if zero else ink)
ax.text(6.5,1.40,r"$\rho=\dfrac{y+b_Q}{2(x-a)y}\,dx,\qquad"
        r"\operatorname{res}_{Q}\rho=1,\quad\operatorname{res}_{O}\rho=-1$",
        ha="center",va="center",fontsize=19,color=ink)
ax.text(6.5,0.78,r"$F=(x-x_0)/(x_1-x_0),\qquad F(P_1)-F(P_0)=1$",
        ha="center",va="center",fontsize=17,color=ink)
ax.text(6.5,0.24,"Exact symbolic entries • Exercise 22.112 and (22.283) • No dimension claim for their scalar span",
        ha="center",fontsize=11,color=muted)
fig.subplots_adjust(left=0.02,right=0.99,bottom=0.02,top=0.99)
out=Path(__file__).with_suffix(".png")
fig.savefig(out,facecolor="white")
plt.close(fig)
print(out)
