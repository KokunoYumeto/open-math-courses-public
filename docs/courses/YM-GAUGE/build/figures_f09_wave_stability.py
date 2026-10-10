from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch,FancyArrowPatch
ROOT=Path(__file__).resolve().parent.parent/'figures'
ROOT.mkdir(parents=True,exist_ok=True)
plt.rcParams['svg.hashsalt']='YM-F09-wave_stability'
fig, ax = plt.subplots(figsize=(15, 9.6))
fig.patch.set_facecolor("#f7f8fb")
ax.set_facecolor("#f7f8fb")
ax.set_xlim(0, 15)
ax.set_ylim(0, 9.6)
ax.axis("off")
ax.text(.5, 9.15, "Signed electric data from the original physical equations", fontsize=21,
        weight="bold", color="#14263f")
ax.text(.5, 8.72, r"$I=[t_-,t_+]$, common anchor $t_*$, physical speed $c>0$, heat interval $[0,S]$",
        fontsize=13, color="#45566c")


def box(x, y, w, h, title, body, color="#e7eef8", title_size=14, body_size=12):
    patch = FancyBboxPatch((x,y), w,h, boxstyle="round,pad=0.16,rounding_size=0.13",
                           linewidth=1.4, edgecolor="#93a6bf", facecolor=color)
    ax.add_patch(patch)
    ax.text(x+.12, y+h-.28, title, va="top", fontsize=title_size, weight="bold", color="#14263f")
    ax.text(x+.12, y+h-.79, body, va="top", fontsize=body_size, linespacing=1.5, color="#20344e")


def arrow(x1,y1,x2,y2,label=""):
    ax.add_patch(FancyArrowPatch((x1,y1),(x2,y2),arrowstyle="-|>", mutation_scale=15,
                                linewidth=1.6, color="#45566c"))
    if label:
        ax.text((x1+x2)/2+.05,(y1+y2)/2+.07,label,fontsize=10,color="#45566c")


box(.55, 6.45, 4.2, 1.65, "Initial energy difference", 
    r"$y_0^2=\|\partial_x z(t_*)\|_2^2+c^{-2}\|e(t_*)\|_2^2$"+"\n"+
    r"$y(t)\leq\Theta(t)y_0$  (WS.13)", color="#e2f2eb", body_size=12)
box(5.4, 6.45, 4.15, 1.65, "Transverse physical wave",
    "□"+r"$_cP_{\rm df}z=-P_{\rm df}N_\delta$"+"\n"+
    r"Exact finite-$S$ spectral integral"+"\n(WS.16–18)", body_size=11.7)
box(10.2, 6.45, 4.2, 1.65, "Longitudinal Gauss field",
    r"$P_{\rm cf}e=\nabla\Delta^{-1}Q_\delta$"+"\n"+
    r"$8J_{12/7}s^{-1/8}$ kernel bound (WS.22)", body_size=11.7)
arrow(4.93,7.23,5.2,7.23)
box(3.9, 3.95, 7.2, 1.58, "Signed electric datum in physical temporal gauge",
    r"$\mathcal{D}_p(e)\leq C_p^{\rm phys}y_0$,  $p=2,\infty$  (WS.24)"+"\n"+
    "Both electric projections are retained.",
    color="#e2f2eb", body_size=12)
arrow(7.5,6.28,7.5,5.72)
arrow(12.3,6.28,10.0,5.72)
box(.55, 1.42, 6.65, 1.74, "Anchored gauge transfer and heat equation",
    r"$f=U^{-1}eU+(\operatorname{Ad}_{U^{-1}}-\operatorname{Ad}_{(U')^{-1}})E'$"+"\n"+
    r"Ordered heat commutators (WS.26–32) $\longrightarrow$ ED.25b", body_size=11.5)
box(7.85, 1.42, 6.55, 1.74, "Caloric electric receiver (WS.34)",
    r"$\delta e_p\leq C_p^{\rm cal}y_0+D_p^{\rm gauge}d$"+"\n"+
    r"$\qquad +Z_p^{\rm gauge}Z_6+\alpha_p\delta A_0+\beta_p\delta C_F$",
    color="#e2f2eb", body_size=12.5)
arrow(6.2,3.76,4.3,3.35)
arrow(7.36,2.3,7.67,2.3)
ax.text(.55,.75,"Proved scope: a regular-pair coefficient. Uniform control by the energy radius still needs the paired nonlinear forcing estimate.",
        fontsize=12,color="#7d422d",weight="bold")
ax.text(.55,.29,"Proof locators: WS.4–WS.40. Human-source context: Sung-Jin Oh, arXiv:1210.1558v2. Diagram of exact maps; no simulated solution.",
        fontsize=10,color="#45566c")
fig.savefig(ROOT/"f09-wave-stability.png",dpi=170,bbox_inches="tight",facecolor=fig.get_facecolor())
fig.savefig(ROOT/"f09-wave-stability.svg",bbox_inches="tight",facecolor=fig.get_facecolor(),metadata={'Date':None})
plt.close(fig)

def build():
    return None
