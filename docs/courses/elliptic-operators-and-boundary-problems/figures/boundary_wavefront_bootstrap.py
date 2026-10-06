"""Render the boundary wave-front bootstrap and local elliptic completion."""

from __future__ import annotations

from pathlib import Path

import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrowPatch, FancyBboxPatch, Polygon, Wedge


HERE = Path(__file__).resolve().parent
SVG = HERE / "boundary_wavefront_bootstrap.svg"
PNG = HERE / "boundary_wavefront_bootstrap.png"

BG = "#fffdf8"
INK = "#173750"
MUTED = "#53616c"
BLUE = "#e9f3f8"
BLUE_EDGE = "#4d7891"
GREEN = "#edf6ec"
GREEN_EDGE = "#608358"
ORANGE = "#fff1e4"
ORANGE_EDGE = "#a66c3f"
PURPLE = "#f3edf8"
PURPLE_EDGE = "#80669a"
RED = "#fff0ee"
RED_EDGE = "#a85d51"

fig, axes = plt.subplots(1, 3, figsize=(17.2, 7.5))
fig.patch.set_facecolor(BG)
for ax in axes:
    ax.set_facecolor(BG)
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 10)
    ax.axis("off")


def box(ax, x, y, w, h, text, face=BLUE, edge=BLUE_EDGE, size=11.2, weight=None):
    patch = FancyBboxPatch(
        (x, y), w, h,
        boxstyle="round,pad=0.12,rounding_size=0.13",
        facecolor=face, edgecolor=edge, linewidth=1.7,
    )
    ax.add_patch(patch)
    ax.text(
        x + w / 2, y + h / 2, text,
        ha="center", va="center", fontsize=size, color=INK,
        weight=weight, linespacing=1.25,
    )
    return patch


def arrow(ax, x0, y0, x1, y1, label=None, color=MUTED, curve=0.0, offset=0.18):
    patch = FancyArrowPatch(
        (x0, y0), (x1, y1), arrowstyle="-|>", mutation_scale=15,
        linewidth=1.65, color=color, connectionstyle=f"arc3,rad={curve}",
    )
    ax.add_patch(patch)
    if label:
        ax.text(
            (x0 + x1) / 2, (y0 + y1) / 2 + offset,
            label, ha="center", va="bottom", fontsize=10.2, color=color,
        )
    return patch


fig.suptitle(
    "Boundary wave-front equality: localize, bootstrap, and complete",
    fontsize=20, weight="bold", color=INK, y=0.975,
)
fig.text(
    0.5, 0.925,
    r"A tangential cone slice and the proved steps: BW12--BW31 and BW39a--BW43a.",
    ha="center", va="center", fontsize=11.6, color=MUTED,
)

# Panel I: nested tangential cones.
ax = axes[0]
ax.text(0.35, 9.35, "1  Exclude the data wave fronts", fontsize=14, weight="bold", color=INK)
origin = (1.35, 4.75)
ax.plot([origin[0], 9.2], [origin[1], origin[1]], color="#b8c2c8", linewidth=1.1)
ax.plot([origin[0], origin[0]], [1.25, 8.25], color="#b8c2c8", linewidth=1.1)
ax.add_patch(Wedge(origin, 7.0, -24, 24, facecolor=BLUE, edgecolor=BLUE_EDGE, linewidth=1.6, alpha=0.80))
ax.add_patch(Wedge(origin, 5.7, -12, 12, facecolor=GREEN, edgecolor=GREEN_EDGE, linewidth=1.7, alpha=0.92))
ax.plot([origin[0], 8.0], [origin[1], origin[1]], color=RED_EDGE, linewidth=2.2)
ax.scatter([5.75], [4.75], s=62, color=RED_EDGE, zorder=5)
ax.text(5.75, 5.12, r"$q_0=(y_0,\eta_0)$", ha="center", fontsize=11.5, color=INK)
ax.text(6.55, 6.35, r"$\Gamma_1$", fontsize=12, color=BLUE_EDGE, weight="bold")
ax.text(6.30, 5.42, r"$\Gamma_0\Subset\Gamma_1$", fontsize=12, color=GREEN_EDGE, weight="bold")
ax.scatter([7.35, 8.15], [7.75, 7.40], marker="x", s=70, linewidths=2.0, color=RED_EDGE, zorder=5)
ax.text(6.80, 8.40, r"$\operatorname{WF}_b(f)\cup\bigcup_j\operatorname{WF}(g_j)$", fontsize=10.6, color=RED_EDGE, ha="center")
ax.text(6.80, 8.00, r"is disjoint from $\overline{\Gamma_1}$", fontsize=10.6, color=RED_EDGE, ha="center")
box(
    ax, 1.2, 0.45, 7.8, 1.30,
    r"$A_r=C_rA_{r+1}+R_r,$  $R_r\in\Psi^{-\infty}$"
    + "\n" + r"$A_r^F=P_mA_r^EP_m^{-1}$;  $A_r^FP_m=P_mA_r^E$",
    PURPLE, PURPLE_EDGE, 10.4,
)

# Panel II: the two-stage regularity ladder.
ax = axes[1]
ax.text(0.35, 9.35, "2  Climb the exact mixed scale", fontsize=14, weight="bold", color=INK)
stage1 = [(1.0, 7.55), (2.65, 6.77), (4.30, 5.99), (5.95, 5.21)]
for idx, (x, y) in enumerate(stage1):
    box(ax, x, y, 2.20, 0.78, rf"$\bar H_{{(s+{idx},\,t-{idx})}}$", BLUE, BLUE_EDGE, 10.9)
    if idx:
        px, py = stage1[idx - 1]
        arrow(ax, px + 2.2, py + 0.37, x, y + 0.37, color=BLUE_EDGE)
ax.text(4.8, 8.88, r"$(s,t)\mapsto(s+1,t-1)$", ha="center", fontsize=12.2, color=BLUE_EDGE, weight="bold")
ax.text(4.8, 8.54, r"until $s\geq m$;  $s+t$ stays fixed", ha="center", fontsize=10.8, color=MUTED)
ax.text(5.0, 4.50, r"$D_t^mv=P_m^{-1}(Pv-\sum_{k=0}^{m-1}P_kD_t^kv)$",
        ha="center", fontsize=10.0, color=INK)
ax.text(5.0, 3.94, "Half-space recovery: MSB50--MSB56", ha="center", fontsize=9.7, color=MUTED)
box(ax, 1.05, 2.55, 2.25, 0.88, r"$\bar H_{(s,t_1)}$", GREEN, GREEN_EDGE, 11.4)
box(ax, 4.05, 2.55, 2.25, 0.88, r"$\bar H_{(s+1,t_1)}$", GREEN, GREEN_EDGE, 11.4)
box(ax, 7.05, 2.55, 2.25, 0.88, r"$\bar H_{(s+2,t_1)}$", GREEN, GREEN_EDGE, 11.4)
arrow(ax, 3.33, 2.99, 4.02, 2.99, r"parametrix", GREEN_EDGE, offset=0.30)
arrow(ax, 6.33, 2.99, 7.02, 2.99, r"parametrix", GREEN_EDGE, offset=0.30)
ax.text(5.15, 3.62, r"$(s,t_1)\mapsto(s+1,t_1)$ for $s\geq m$", ha="center", fontsize=11.8, color=GREEN_EDGE, weight="bold")
box(
    ax, 1.05, 0.55, 8.25, 1.18,
    r"$\bar H_{(s,t_1)}\hookrightarrow H^{s+\min(t_1,0)}$"
    + "\n" + r"arbitrarily large $s$  $\Longrightarrow$  $A_0u\in C^\infty$",
    PURPLE, PURPLE_EDGE, 11.2, "bold",
)

# Panel III: local completion and return to the original system.
ax = axes[2]
ax.text(0.35, 9.35, "3  Complete outside the selected cone", fontsize=14, weight="bold", color=INK)
box(ax, 0.55, 7.35, 3.55, 1.25, r"complete symbols" + "\n" + r"$a_k(y,t,\eta),\ c_{jk}(y,\eta)$", BLUE, BLUE_EDGE, 11.1)
box(ax, 5.90, 7.35, 3.55, 1.25, r"frozen-ray completions" + "\n" + r"$a_k^\circ(\eta),\ c_{jk}^\circ(\eta)$", ORANGE, ORANGE_EDGE, 10.8)
box(
    ax, 1.05, 5.20, 7.90, 1.30,
    r"$\widetilde a_k=\psi a_k+(1-\psi)a_k^\circ$  $(k<m)$"
    + "\n" + r"$\widetilde c_{jk}=\psi c_{jk}+(1-\psi)c_{jk}^\circ$;  $\widetilde a_m=a_m$",
    PURPLE, PURPLE_EDGE, 10.4, "bold",
)
arrow(ax, 2.35, 7.33, 3.65, 6.53, r"$\psi=1$ on $\Gamma_0$", BLUE_EDGE, 0.0, 0.05)
arrow(ax, 7.65, 7.33, 6.35, 6.53, r"$\psi=0$ off $\Gamma_1$", ORANGE_EDGE, 0.0, 0.05)
box(
    ax, 1.15, 3.15, 7.70, 1.10,
    r"global modified elliptic system"
    + "\n" + r"$\widetilde\beta:\operatorname{ran}q^+\longrightarrow G^0$ is an isomorphism",
    GREEN, GREEN_EDGE, 11.3,
)
arrow(ax, 5.0, 5.17, 5.0, 4.28, r"stable projection", GREEN_EDGE, offset=0.06)
box(
    ax, 0.75, 0.62, 8.50, 1.35,
    r"apply the wave-front equality to $(\widetilde P,\widetilde B)$"
    + "\n" + r"then use $A(\widetilde P-P)u,\ A(\widetilde B-B)u\in C^\infty$ on $\Gamma_0$",
    RED, RED_EDGE, 10.8, "bold",
)
arrow(ax, 5.0, 3.12, 5.0, 2.00, r"return at $q_0$", RED_EDGE, offset=0.06)

fig.text(
    0.5, 0.034,
    r"Conclusion: $\operatorname{WF}_b(u)|_{\partial X}=\operatorname{WF}_b(f)|_{\partial X}\cup\bigcup_j\operatorname{WF}(g_j)$.",
    ha="center", va="center", fontsize=12.5, color=INK, weight="bold",
)

fig.subplots_adjust(left=0.025, right=0.985, top=0.89, bottom=0.085, wspace=0.055)
fig.savefig(SVG, facecolor=fig.get_facecolor())
fig.savefig(PNG, dpi=180, facecolor=fig.get_facecolor())
plt.close(fig)
print(f"{SVG}\n{PNG}")
