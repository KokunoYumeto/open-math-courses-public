"""Exact SU(2) action family from F7.51–F7.53; sampled curves, CC0."""
from pathlib import Path
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

def build():
    root = Path(__file__).resolve().parents[1] / "figures"
    root.mkdir(exist_ok=True)
    with plt.rc_context({
        "font.family": "DejaVu Sans", "font.size": 12,
        "svg.fonttype": "path", "svg.hashsalt": "YM-F07-action-v1",
        "axes.spines.top": False, "axes.spines.right": False,
    }):
        fig = plt.figure(figsize=(12, 8.6), facecolor="#fffef9")
        grid = fig.add_gridspec(1, 2, left=.07, right=.96, top=.73, bottom=.26, wspace=.30)
        ax = fig.add_subplot(grid[0, 0], projection="3d", computed_zorder=False)
        a = np.linspace(-1.5, 1.5, 81)
        aa, bb = np.meshgrid(a, a)
        zz = aa**2 * bb**2 / 2
        ax.plot_surface(aa, bb, zz, cmap="viridis", linewidth=0, alpha=.88, zorder=0)
        ax.plot(a, np.zeros_like(a), np.zeros_like(a), color="#c24b21", lw=3, zorder=10)
        ax.plot(np.zeros_like(a), a, np.zeros_like(a), color="#c24b21", lw=3, zorder=10)
        ax.set_xlabel(r"$aL$", labelpad=8)
        ax.set_ylabel(r"$bL$", labelpad=8)
        ax.set_zlabel(r"$(aL)^2(bL)^2/2$", labelpad=10)
        ax.view_init(elev=27, azim=-53)
        ax.set_zlim(0, 2.6)
        bx = fig.add_subplot(grid[0, 1])
        s = np.linspace(-.5, 1, 401)
        terms = [.5*np.ones_like(s), 2*s, 3*s**2, 2*s**3, .5*s**4]
        labels = [r"$1/2$", r"$2s$", r"$3s^2$", r"$2s^3$", r"$s^4/2$"]
        colors = ["#777777", "#d66a20", "#247697", "#813c91", "#527635"]
        for values, label, color in zip(terms, labels, colors):
            bx.plot(s, values, "--", label=label, color=color, lw=1.8)
        bx.plot(s, (1+s)**4/2, color="#123e4b", lw=3.2, label=r"Sum: $(1+s)^4/2$")
        bx.axhline(0, color="#adb7b5", lw=.7)
        bx.set(xlabel=r"Variation parameter $s$", ylabel="Displayed action density",
               xlim=(-.5, 1), ylim=(-1.2, 8.5))
        bx.grid(alpha=.2)
        bx.legend(loc="upper left", fontsize=10, frameon=False)
        fig.text(.06, .94, "The complete Yang–Mills action and every term of its variation",
                 size=18, weight="bold", color="#123e4b")
        fig.text(.06, .88, r"$\Gamma_1=aT_1,\quad\Gamma_2=bT_2,\quad"
                 r"\Gamma_0=\Gamma_3=0,\quad T_j=-i\sigma_j/2$", size=17)
        fig.text(.06, .82, r"Full density: $S_{\rm YM,Q}/{\rm vol}(Q)"
                 r"=\hbar a^2b^2/(2g_{\rm YM}^2)$", size=15)
        fig.text(.12, .765, "The complete action density", size=14)
        fig.text(.58, .765, "All five polynomial terms", size=14)
        fig.text(.06, .18, "Display map, with reference length L > 0:", size=13, weight="bold")
        fig.text(.06, .13, r"$g_{\rm YM}^2L^4S_{\rm YM,Q}/"
                 r"[\hbar\,{\rm vol}(Q)]=(aL)^2(bL)^2/2.$", size=15)
        fig.text(.06, .078, "Orange axes: a = 0 or b = 0, where curvature and action vanish. "
                 "Right panel: aL = bL = 1 + s.", size=11)
        fig.text(.06, .035, "Exact formulas and proofs: YM-F07, F7.51–F7.53. "
                 "The surface and curves are numerical samples of those functions.", size=11)
        fig.savefig(root/"f07-action-variation.svg", metadata={"Date":None}, facecolor=fig.get_facecolor())
        fig.savefig(root/"f07-action-variation.png", dpi=140, metadata={"Software":"YM-F07 figure"}, facecolor=fig.get_facecolor())
        plt.close(fig)
    p=root/"f07-action-variation.svg"
    s=p.read_text(encoding="utf-8")
    pos=s.index(">",s.index("<svg"))+1
    s=s[:pos]+'<title>Full quartic SU(2) Yang–Mills action and its variation</title><desc>The exact displayed density is (a L) squared times (b L) squared divided by two. Both coordinate axes have zero curvature and action. The slice a L equals b L equals one plus s retains its constant, linear, quadratic, cubic and quartic terms. Original action factors hbar and g Yang–Mills are shown in the display map. See F7.51 through F7.53.</desc>'+s[pos:]
    p.write_text(s,encoding="utf-8")

if __name__ == "__main__":
    build()
