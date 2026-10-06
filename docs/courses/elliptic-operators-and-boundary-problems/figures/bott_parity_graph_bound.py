from pathlib import Path
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

out = Path(__file__).resolve().parent
n = np.arange(1, 13)
qe = 2 * (n // 2)
qo = 2 * ((n + 1) // 2) - 1
full = np.sqrt(2 * n / (n + 1))
even = np.sqrt(np.maximum(1, 2 * qe / (n + 1)))
odd = np.sqrt(np.maximum(1, 2 * qo / (n + 1)))

fig, ax = plt.subplots(figsize=(10.5, 6), facecolor="#fbfbf8")
ax.set_facecolor("#fbfbf8")
ax.plot(n, full, "o-", color="#404d5e",
        label=r"Full forms: $\sqrt{2n/(n+1)}$")
ax.plot(n, even, "-", color="#147991",
        label=r"Even forms: $\sqrt{\max(1,2q_e/(n+1))}$")
ax.plot(n, odd, "-", color="#a64e36",
        label=r"Odd forms: $\sqrt{\max(1,2q_o/(n+1))}$")
ax.scatter(n[1:], even[1:], color="#147991", s=44, zorder=5)
odd_attained = n != 2
ax.scatter(n[odd_attained], odd[odd_attained],
           color="#a64e36", s=44, zorder=5)
ax.scatter([1], [even[0]], facecolors="#fbfbf8", edgecolors="#147991",
           linewidths=2, s=95, zorder=6)
ax.scatter([2], [odd[1]], facecolors="#fbfbf8", edgecolors="#a64e36",
           linewidths=2, s=95, zorder=6)
ax.annotate("Even n=1: supremum only", xy=(1, 1), xytext=(1.2, .86),
            arrowprops={"arrowstyle": "->", "color": "#147991"},
            fontsize=10, color="#147991")
ax.annotate("Odd n=2: supremum only", xy=(2, 1), xytext=(4.2, .9),
            arrowprops={"arrowstyle": "->", "color": "#a64e36"},
            fontsize=10, color="#a64e36")
ax.set(xlabel="Dimension n (positive integers)",
       ylabel="Norm from the original graph domain to L2",
       xlim=(.65, 12.3), ylim=(.82, 1.42))
ax.set_xticks(n)
ax.grid(alpha=.2)
ax.legend(loc="lower right", fontsize=10)
ax.set_title("Bott oscillator bounds with both parity domains retained",
             fontsize=15, pad=15)
fig.text(.5, .065,
         r"$q_e=2\lfloor n/2\rfloor$, $q_o=2\lceil n/2\rceil-1$; "
         r"BS5–BS8 keep $\|u\|_{\mathcal{B}}^2=\|u\|^2+"
         r"\sum_j(\|x_ju\|^2+\|D_ju\|^2)$.",
         ha="center", fontsize=10)
fig.text(.5, .025,
         "Filled parity points: attained by the original Gaussian in the "
         "highest permitted degree. Lines guide the eye.",
         ha="center", fontsize=10)
fig.subplots_adjust(bottom=.21)
fig.savefig(out / "bott_parity_graph_bound.png", dpi=160,
            facecolor=fig.get_facecolor())
fig.savefig(out / "bott_parity_graph_bound.svg",
            facecolor=fig.get_facecolor())
plt.close(fig)
print("Saved parity norm PNG and SVG.")
