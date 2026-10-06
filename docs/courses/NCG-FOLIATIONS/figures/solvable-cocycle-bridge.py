"""Original reproducible exact-map schematic; no numerical curve or proof inference."""
from pathlib import Path
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch

HERE = Path(__file__).resolve().parent
plt.rcParams.update({"font.family": "DejaVu Sans", "font.size": 13,
                     "svg.fonttype": "none", "mathtext.fontset": "dejavusans"})
fig = plt.figure(figsize=(16, 10), facecolor="#f6f8fc")
fig.text(.04, .952, "The full solvable geometric cycle bridge", fontsize=25,
         weight="bold", color="#152b49")
fig.text(.04, .913, "Actual graph  G = V ⋊ H  •  simply connected solvable H  •  all compact native cycles",
         fontsize=14, color="#4b5870")

panels = []
def panel(rect, title, colour):
    ax = fig.add_axes(rect)
    ax.set_xlim(0, 1); ax.set_ylim(0, 1); ax.axis("off")
    ax.add_patch(FancyBboxPatch((0, 0), 1, 1, boxstyle="round,pad=0.00,rounding_size=.028",
                               linewidth=1.5, edgecolor=colour, facecolor="white"))
    ax.text(.04, .91, title, fontsize=17, weight="bold", color=colour, va="top")
    panels.append(ax)
    return ax

a = panel([.04, .505, .445, .355], "A  Countable cocycles → global lift", "#215e9a")
a.text(.05, .755, r"$H=N\rtimes\mathbb{R},\quad r(t)=\exp(tX)$", fontsize=17)
a.text(.05, .605, r"$t_\alpha=\sum_\gamma\rho_\gamma\,\chi(h_{\alpha\gamma})$", fontsize=18)
a.text(.05, .46, r"$r_{\beta\alpha}=r(-t_\beta)\,h_{\beta\alpha}\,r(t_\alpha)\in N$", fontsize=16)
a.text(.05, .315, r"$r_{\beta\alpha}=n_\beta n_\alpha^{-1},\quad k_\alpha=r(t_\alpha)n_\alpha$", fontsize=16)
a.text(.05, .17, r"$h_{\beta\alpha}=k_\beta k_\alpha^{-1},\quad a=k_\alpha^{-1}f_\alpha$", fontsize=17)
a.text(.05, .055, "Locally finite closed supports; zero-weight terms extend by zero.", fontsize=11)

b = panel([.515, .505, .445, .355], "B  The entire normal bundle glues", "#21765a")
b.text(.05, .755, r"$\Psi_\alpha=D^\perp k_\alpha:\ a^*\tau\longrightarrow f_\alpha^*\tau$", fontsize=17)
b.text(.05, .595, r"$D^\perp h_{\beta\alpha}\,\Psi_\alpha=\Psi_\beta$", fontsize=19)
b.text(.05, .435, "Transport the metric, then the full spin-c module.", fontsize=14)
b.text(.05, .31, "Retain every line phase, torsion twist and stable grading.", fontsize=13)
b.text(.05, .16, r"$u=(k'_\alpha)^{-1}k_\alpha,\quad a_s=u_s a,\quad u_0=e,\ u_1=u$", fontsize=15)
b.text(.05, .055, "One whole family also retains bordisms and sphere clutch bundles.", fontsize=11)

c = panel([.04, .102, .445, .355], "C  Right universal space: the exact coordinate", "#6c519c")
c.text(.05, .755, r"$E_H\cong B_H\times H,\quad E_H,\ B_H\ \mathrm{contractible}$", fontsize=16)
c.text(.05, .595, r"$B_G=(E_H\times V)/((eh,v)\sim(e,hv))$", fontsize=16)
c.text(.05, .435, r"$[\sigma(b)h,v]\longmapsto(b,hv)$", fontsize=20)
c.text(.05, .275, r"$[(\sigma(b)h,v),\xi]\longmapsto(b,hv,D^\perp h\,\xi)$", fontsize=16)
c.text(.05, .11, "Hence  BG ≃ V  with the whole normal bundle τ.", fontsize=14)
c.text(.05, .035, "This classifies cocycle concordance, with actual arrows retained.", fontsize=11)

d = panel([.515, .102, .445, .355], "D  Proved interfaces and remaining work", "#ac6327")
d.text(.05, .755, r"$\mathcal{C}_{*,\tau}(V)\ \cong\ K_{*,\tau}^{\rm geom}(B_G)$", fontsize=18)
d.text(.05, .615, r"$\mu[M,E,f]=[E]\,a_{\rm cocycle,!}$", fontsize=18)
d.text(.05, .475, r"Compact $V$:  $\ell_!^{\rm geom}=\ell_!^{\rm an}=s_d\Theta_H$", fontsize=17)
d.text(.05, .345, r"$d:\quad0\ \ 1\ \ 2\ \ 3\ \ 4\ \ 5\ \ 6\ \ 7$", fontsize=16)
d.text(.05, .24, r"$s_d:\ +\ +\ -\ -\ +\ +\ -\ -$", fontsize=16)
d.text(.05, .115, "Still required: integral manifold duality and the full", fontsize=13,
       color="#954717")
d.text(.05, .045, "noncompact geometric leaf-map / assembly composition.", fontsize=13,
       color="#954717")

fig.text(.04, .046, "Proof: Lemmas 8B.1–2, Theorems 8B.3–4, Corollaries 8B.5–6; displays (B.a)–(B.r).",
         fontsize=12, color="#4b5870")
fig.text(.04, .018, "Exact map and module schematic, not a geometric projection. Historical source: Connes, Sections 9–12.",
         fontsize=11, color="#4b5870")
fig.canvas.draw()
renderer = fig.canvas.get_renderer()
violations = []
for ax in panels:
    box = ax.get_window_extent(renderer)
    for label in ax.texts:
        b = label.get_window_extent(renderer)
        if b.x0 < box.x0 - 1 or b.x1 > box.x1 + 1 or b.y0 < box.y0 - 1 or b.y1 > box.y1 + 1:
            violations.append(label.get_text())
assert not violations, violations
fig.savefig(HERE / "solvable-cocycle-bridge.svg", facecolor=fig.get_facecolor())
fig.savefig(HERE / "solvable-cocycle-bridge.png", dpi=160, facecolor=fig.get_facecolor())
plt.close(fig)
print("Four panels rendered; every panel label is inside its declared bounding box.")
