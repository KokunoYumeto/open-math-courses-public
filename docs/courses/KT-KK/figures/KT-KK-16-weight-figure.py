from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

root = Path(__file__).resolve().parent
t = np.linspace(0, 1, 301)
raw = np.column_stack((1-t, t/np.sqrt(2), t/np.sqrt(2)))
den = np.sqrt((1-t)**2 + t**2)
curve = raw / den[:, None]
fig = plt.figure(figsize=(12.8, 5.8), facecolor="white")
ax = fig.add_subplot(121)
# This exact plane has beta=gamma; q=sqrt(beta^2+gamma^2).
ax.plot(raw[:,0], np.sqrt(2)*raw[:,1], color="#94a3b8",
        linestyle="--", linewidth=1.5, label="unnormalized chord")
ax.plot(curve[:,0], np.sqrt(2)*curve[:,1], color="#075985", linewidth=3,
        label="unit-length symbol path")
ax.scatter(curve[[0,-1],0], np.sqrt(2)*curve[[0,-1],1],
           color=["#b45309", "#047857"], s=45, zorder=3)
ax.text(.59, .07, r"$A_0=(1,0,0)$", fontsize=10)
ax.text(.02, 1.07, r"$A_1=(0,1/\sqrt{2},1/\sqrt{2})$", fontsize=10)
ax.set(xlim=(-.04,1.12), ylim=(-.04,1.17), aspect="equal")
ax.set_xlabel(r"$\alpha$: kinetic", labelpad=8)
ax.set_ylabel(r"$q=\sqrt{\beta^2+\gamma^2}$: combined position", labelpad=8)
ax.grid(color="#cbd5e1", linewidth=.7)
ax.legend(loc="center", bbox_to_anchor=(.37,.43), frameon=False, fontsize=9)
ax.set_title("Unit Clifford weights: equation (5.23)", pad=15)
fig.text(.105, .10,
          r"$|(1-t)A_0+tA_1|=\sqrt{(1-t)^2+t^2}\geq1/\sqrt{2}$",
          fontsize=11)
ax.text(.04, .13, r"$\beta=\gamma=q/\sqrt{2}$", transform=ax.transAxes,
        fontsize=11)
right = fig.add_subplot(122)
right.axis("off")
right.set_title("Global operator comparison: equations (5.16)–(5.19)", pad=15)
boxes = [
    (.82, r"$P\longrightarrow J=\mathrm{sign}(D)$"+"\n"
     r"$g_W=a_n e^{-\sqrt{1+|u|^2}}\,1_{\Lambda^0}$"),
    (.53, r"$\ker D=\mathbb{C} g_W$: even, trivial $O(n)$ character"+"\n"
     r"$\mathbb{C} g_W\widehat{\otimes} S_N$ keeps the full normal spinor"),
    (.24, r"$G=(J+\Gamma_\Lambda C_N(\nu))/\sqrt{1+|\nu|^2}$"+"\n"
     "kernel: outward normal cycle\ncomplement: exact involution, degenerate")
]
for y, label in boxes:
    right.text(.5, y, label, ha="center", va="center", fontsize=11,
               bbox=dict(boxstyle="round,pad=.7", facecolor="#eff6ff",
                         edgecolor="#475569", linewidth=1))
for top, bottom in [(.72,.63),(.41,.35)]:
    right.annotate("", xy=(.5,bottom), xytext=(.5,top),
                   arrowprops=dict(arrowstyle="-|>", color="#475569", lw=1.5))
fig.text(.5, .047,
         r"Left: an admissible sample with $|u|=2$, $|\nu|=1$, "
         r"$m_0(\sqrt{5})=1$, $m(2)=0$. The dashed chord is normalized to the solid arc.",
         ha="center", fontsize=10)
fig.text(.5, .018,
         "Direct-symbol sources: Connes–Skandalis (1984), Section II; "
         "Blackadar, free author edition, Example 17.1.2(g). "
         "Comparison proved here in Lemmas 5.1–5.3.",
         ha="center", fontsize=8.5)
fig.subplots_adjust(left=.04, right=.96, bottom=.24, top=.88, wspace=.22)
fig.savefig(root/"KT-KK-16-weight-homotopy.svg")
fig.savefig(root/"KT-KK-16-weight-homotopy.png", dpi=160)
print("Rendered KT-KK-16-weight-homotopy.svg and .png")


