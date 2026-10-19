"""Exact example illustrating Lemma15.4. Original exposition, CC0."""
from pathlib import Path
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

HERE = Path(__file__).resolve().parent
fig = plt.figure(figsize=(10, 4.4), facecolor="white")
ax = fig.add_axes([0.065, 0.35, 0.50, 0.52])
ax.set_xlim(0.5, 5.5)
ax.set_ylim(-1.5, 1.0)
ax.axis("off")
ink, blue, orange = "#172b4d", "#176b9b", "#b85319"
ax.plot([0.7, 5.3], [0, 0], color="#a9b5c4", lw=1.2)
for x, label in [(1, r"$u_3=1$"), (3, r"$u_2=3$"), (5, r"$u_1=5$")]:
    ax.plot(x, 0, "o", color=ink, ms=7)
    ax.text(x, 0.26, label, ha="center", fontsize=13, color=ink)
for left, right, label in [(1, 3, r"$q=2$"), (3, 5, r"$p=2$")]:
    ax.annotate("", (right, -0.32), (left, -0.32),
                arrowprops=dict(arrowstyle="<->", color=blue, lw=1.8))
    ax.text((left+right)/2, -0.62, label, ha="center", fontsize=12, color=blue)
ax.annotate("", (5, -1.0), (1, -1.0),
            arrowprops=dict(arrowstyle="<->", color=orange, lw=1.8))
ax.text(3, -1.3, r"$r=p+q=4$", ha="center", fontsize=12, color=orange)
fig.text(0.065, 0.94, "From a bounded ratio to the original square roots",
         fontsize=16, weight="bold", color=ink)
fig.text(0.62, 0.80, r"$A=5^2-3^2=16$", fontsize=13, color=ink)
fig.text(0.62, 0.69, r"$B=5^2-1^2=24$", fontsize=13, color=ink)
fig.text(0.62, 0.58, r"$t=p/r=1/2,\quad D=24$", fontsize=13, color=blue)
fig.text(0.62, 0.46, r"$P=Dt=12,\quad Q=D(1-t)=12$", fontsize=12, color=blue)
fig.text(0.065, 0.23,
         r"Recover the scale:  $r^2=\frac{A-Bt}{t(1-t)}=\frac{16-24/2}{1/4}=16$",
         fontsize=14, color=orange)
fig.text(0.065, 0.10,
         r"Then $u_1=(r+B/r)/2=5$,  $u_3=(B/r-r)/2=1$,  $u_2=u_1-tr=3$.",
         fontsize=12, color=ink)
out = HERE.parent/"figures"/"three-square-recovery.png"
fig.savefig(out, dpi=160, facecolor="white")
plt.close(fig)
print(out)
