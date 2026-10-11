"""Original CC0 diagram of MGP.1--13 and MRP.1--13; no external artwork."""
from pathlib import Path
import argparse
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch
import numpy as np

plt.rcParams.update({"font.family": "DejaVu Sans", "font.size": 11,
                    "svg.hashsalt": "ncg-global-metric-phase-20261011", "svg.fonttype": "path"})
BLUE = "#245b84"
GREEN = "#24755e"
GRAY = "#4c5664"

def box(ax, x, y, w, h, label, color=BLUE):
    ax.add_patch(FancyBboxPatch((x, y), w, h, boxstyle="round,pad=0.014",
                              linewidth=1.5, edgecolor=color, facecolor="white"))
    ax.text(x+w/2, y+h/2, label, ha="center", va="center", color=color, linespacing=1.5)

def arrow(ax, x1, y1, x2, y2):
    ax.annotate("", xy=(x2, y2), xytext=(x1, y1),
                arrowprops={"arrowstyle": "->", "color": BLUE, "lw": 1.7})

def save(fig, out, name):
    fig.savefig(out/(name+".svg"), metadata={"Date": None, "Creator": "Original CC0 mathematical diagram"})
    svg = out/(name+".svg")
    svg.write_bytes(svg.read_bytes().replace(b"\r\n", b"\n"))
    fig.savefig(out/(name+".png"), dpi=150, metadata={"Software": "Original CC0 mathematical diagram"})
    plt.close(fig)

def draw(out):
    fig = plt.figure(figsize=(13.2, 8.8))
    fig.patch.set_facecolor("#f5f7fa")
    fig.suptitle("The global metric phase and two proved reduced receiving routes",
                 fontsize=19, color=BLUE, y=.966)
    ax = fig.add_axes([.065, .44, .30, .39])
    t = np.linspace(0, 4, 201)
    magnitude = 10**t-1
    xi, eta = np.meshgrid(magnitude, magnitude)
    radius = np.sqrt(1+xi*xi+eta*eta)
    defect = 1/(1+radius**(-.5)*xi*xi+eta*eta)
    im = ax.pcolormesh(t, t, np.log10(defect), cmap="viridis", shading="auto", vmin=-8, vmax=0)
    ax.set_xlabel(r"original quotient magnitude $|\xi|$")
    ax.set_ylabel(r"vertical magnitude $|\eta|$")
    ax.set_xticks([0, 1, 2, 3, 4], ["0", "9", "99", "999", "9999"])
    ax.set_yticks([0, 1, 2, 3, 4], ["0", "9", "99", "999", "9999"])
    ax.set_title("Exact square defect: radial sample", fontsize=12, pad=12)
    cax = fig.add_axes([.38, .44, .012, .39])
    cb = fig.colorbar(im, cax=cax, ticks=[-8, -6, -4, -2, 0])
    cb.set_label(r"$\log_{10}(1-f^2)$", fontsize=11)
    fig.text(.225, .30, r"$R=(1+|\xi|^2+|\eta|^2)^{1/2}$"+"\n"+
             r"$1-f^2=(1+R^{-1/2}|\xi|^2+|\eta|^2)^{-1}$"+"\n"+
             r"$1-f^2\leq 2R^{-3/2}$ (all rays)", ha="center", va="center", linespacing=1.9, fontsize=12)
    fig.text(.225, .17, "The plot samples two magnitudes.\nMB.14 proves the bound on all rays.\nMGP.1–10 prove operator bounds, scalar\ncompactness and actual nonlinear covariance.",
             ha="center", va="center", color=GRAY, linespacing=1.6)
    flow = fig.add_axes([.46, .12, .49, .73])
    flow.set_xlim(0, 1); flow.set_ylim(0, 1); flow.axis("off")
    box(flow, .025, .78, .95, .20,
        r"$W=\mathrm{Met}(\tau),\quad d=q(q+1)/2,\quad n=q+d$"+"\n"+
        "Full coherent inverse coefficient; invariant volume\n"+
        r"$F_W$: maximal scalar cycle (MGP.11–13)")
    arrow(flow, .27, .76, .24, .66); arrow(flow, .73, .76, .76, .66)
    box(flow, .015, .46, .45, .19, "Actual range-fibre certificate\n"+
        r"$\|\alpha\xi_s-\xi_r\|\to0$"+"\nfull regular-source isometry\nMRP.1–5", GREEN)
    box(flow, .535, .46, .45, .19, "Actual free-group germs\nwhole vertex–edge tree\ntwo compact ideals and separator\nRTP.1–13; MRP.6", GREEN)
    arrow(flow, .24, .44, .39, .34); arrow(flow, .76, .44, .61, .34)
    box(flow, .025, .135, .95, .19, "Reduced vertical Bott product; full graph correspondence\n"+
        r"$q+2d\longrightarrow q,\quad z^qz^{-(q+1)}=z^{-1}$"+"\n"+
        "Mixed graded signs and final right Clifford action retained\noriginal normal phase and positive q-disk +1 (MRP.7–13)")
    flow.text(.5, .035, "These are sufficient receiving scopes.\nArbitrary original holonomy remains unfinished.",
              ha="center", va="center", color=GRAY, fontsize=11, linespacing=1.5)
    fig.text(.5, .04, "Exact symbol sample at left; algebraic schematic of the proved maps at right. All metric and tree fibres remain.",
             ha="center", fontsize=11, color=GRAY)
    save(fig, out, "global-metric-reduced-routes")

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path, default=Path(__file__).resolve().parents[2]/"figures")
    args = parser.parse_args()
    args.output.mkdir(parents=True, exist_ok=True)
    draw(args.output)
