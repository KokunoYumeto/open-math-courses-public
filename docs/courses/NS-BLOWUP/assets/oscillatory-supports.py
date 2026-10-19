"""Draw the exact support and covering maps proved in OS1–OS7."""
from pathlib import Path
import re
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch

out = Path(__file__).resolve().parent
fig = plt.figure(figsize=(14, 12), dpi=100, facecolor="#f7f9fc")
ax = fig.add_axes([0, 0, 1, 1])
ax.set(xlim=(0, 14), ylim=(0, 12))
ax.axis("off")
ink, blue, orange = "#172a42", "#1b638f", "#a24c16"
def text(x, y, value, size=18, color=ink):
    ax.text(x, y, value, va="top", fontsize=size, color=color, linespacing=1.5)
def panel(y, h, title):
    ax.add_patch(FancyBboxPatch((.45, y), 13.1, h, boxstyle="round,pad=.12",
                              linewidth=1, edgecolor="#b9cadb", facecolor="white"))
    text(.75, y+h-.2, title, 20, blue)
text(.65, 11.7, "One family of separated oscillatory supports", 25)
text(.65, 11.18, "Exact maps from the physical field to the auxiliary tori · OS1–OS7", 16)
panel(8.2, 2.45, "1  Physical evaluation and the common-torus map")
text(.85, 9.95, r"$Y=v_r r^{d_r}+v_t t\quad(\mathrm{mod}\ \mathbb{Z}^2)$", 22)
text(.85, 9.35, r"$Y\ \longmapsto\ H=J_g^{\,i_0}Y\ \longmapsto\ Y_i=J_g^\Delta H$", 23)
text(.85, 8.72, r"$0\leq\Delta\leq\Delta_{\max},\qquad \det J_g=14,\qquad 14^\Delta\ {\rm sheets}$", 21)
panel(5.3, 2.55, "2  Overlap in physical space forces separation on the torus")
text(.85, 7.12, r"$K_\gamma\cap K_{\gamma'}\neq\varnothing,\quad\gamma\neq\gamma'$", 22)
text(.85, 6.52, r"$\overline{\mathcal{R}_\gamma^{\rm abs,+}}\cap"
                  r"\overline{\mathcal{R}_{\gamma'}^{\rm abs,+}}=\varnothing$", 23)
text(.85, 5.91, r"$(\partial^I w_\gamma)(\partial^J w_{\gamma'})=0\qquad\mathrm{for\ every\ }I,J$", 22)
panel(2.8, 2.15, "3  Each pulse follows its own sheet")
text(.85, 4.24, r"$H_w=H+T_g^{-\Delta}c_i(w-v(H))v_t$", 23)
text(.85, 3.62, r"$D_rv=D_zv=0,\quad\mathfrak{t}_*v=1,\quad "
                  r"D_HH_w=I-v_t\lambda_t$", 21)
panel(.65, 1.8, "4  The covariance retains every physical factor")
text(.85, 1.75, r"$\left\langle u_\nu\otimes u_\nu\right\rangle_\theta"
                  r"=\sum_\gamma 2\nu Q_\gamma^{-2A}"
                  r"\operatorname{Re}(a_\gamma\otimes\overline{a_\gamma})$", 22)
text(.85, 1.08, "Only opposite harmonics of the same label survive.  Source: section 6; OS7.13.", 14, orange)
text(.65, .35, "Map diagram; no sampled flow or chosen numerical rectangle locations.", 13)
for ext in ["svg", "png"]:
    fig.savefig(out / ("oscillatory-supports." + ext), dpi=100)
p = out / "oscillatory-supports.svg"
p.write_text(re.sub(r'width="1008pt" height="864pt"', 'width="1400" height="1200"',
                    p.read_text(encoding="utf8")), encoding="utf8")
plt.close(fig)
