"""Exact phase-cover, Čech signs and residue-circle illustration; no numerical proof."""
from pathlib import Path
from fractions import Fraction
from math import factorial, comb
import argparse, json
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Circle, Arc

parser = argparse.ArgumentParser()
parser.add_argument("--output", type=Path, default=Path(__file__).resolve().parent)
out = parser.parse_args().output
out.mkdir(parents=True, exist_ok=True)
matplotlib.rcParams.update({"font.family": "DejaVu Sans", "font.size": 11,
    "svg.hashsalt": "angular-residue-geometry-v1", "axes.titleweight": "bold"})
data = {
    "phase_centers_in_pi_units": ["0", "1/2", "1", "3/2"],
    "phase_interval_length_in_pi_units": "3/4",
    "consecutive_overlap_length_in_pi_units": "1/4",
    "normal_dimension": 3,
    "r_N": -1,
    "deletion_and_primitive_signs": [
        {"omitted_index": i, "deletion_sign": (-1)**i,
         "primitive_sign": -(-1)**i, "product": -1} for i in range(3)],
    "ordinary_residue_slice": {"u": "0", "v": "1", "intermediate_radius": "1/4",
        "outer_radius": "3/2", "min_distance_to_u": "1/4",
        "min_distance_to_v": "3/4"},
    "strict_example": {"F": "exp(1/w)/(w*zeta) + log(w)*w^2/zeta^3 + w/zeta + zeta^2/w",
        "H": "2*pi*i*w^2/zeta^3", "G": "-w^2/zeta^3", "normal_face": "w/zeta",
        "spatial_face": "zeta^2/w", "log_homogeneous_coefficient": "p_{-1}(z)=-z^2",
        "ordinary_positive_coefficient": "a_m=1/(m!)^2"},
    "nonlinear_phi_u_plus_u_squared_at_zero": [
        {"m": m, "a_prime_m": str(sum((Fraction(comb(m,k),factorial(m+k)*factorial(m))
            for k in range(m+1)), Fraction(0)))} for m in range(10)],
}
(out / "angular-residue-geometry-data.json").write_text(json.dumps(data, indent=2) + "\n", encoding="utf-8")
fig, axes = plt.subplots(1, 3, figsize=(16.8, 6.4))
fig.patch.set_facecolor("#f7fafc")
colors = ["#315b94", "#138477", "#bc6f20", "#a24676"]
ax = axes[0]
ax.set_title("A strict normal-angle datum")
ax.add_patch(Circle((0,0), .83, fill=False, color="#c9d1db", linewidth=1.2))
for i, c in enumerate([0,90,180,270]):
    rad = .94 + .085*i
    ax.add_patch(Arc((0,0), 2*rad, 2*rad, theta1=c-67.5, theta2=c+67.5,
        color=colors[i], linewidth=5))
    angle = np.deg2rad(c)
    ax.text(1.43*np.cos(angle), 1.43*np.sin(angle), rf"$I_{i}$", color=colors[i],
        ha="center", va="center", fontsize=13, fontweight="bold")
ax.text(0,.18, r"$F(L+2\pi i)-F(L)=H$", ha="center", fontsize=11)
ax.text(0,-.2, r"$G=-H/(2\pi i)$", ha="center", fontsize=12)
ax.text(0,-1.76, r"Each interval: $3\pi/4$; overlap: $\pi/4$", ha="center")
ax.text(0,-2.13, "The holomorphic defect is supplied.\nAN.1–AN.3 do not assert microlocal descent.",
    ha="center", va="top", fontsize=10, color="#3a4a5b")
ax.set_xlim(-1.8,1.8); ax.set_ylim(-2.55,1.7); ax.set_aspect("equal"); ax.axis("off")

ax = axes[1]
ax.set_title("Literal missing-face primitives")
ax.axis("off")
ax.text(.5,.91, r"$N=3,\quad r_3=(-1)^3=-1$", ha="center", transform=ax.transAxes, fontsize=13)
table = ax.table(cellText=[["0", "+1", "−1", "−1"], ["1", "−1", "+1", "−1"],
    ["2", "+1", "−1", "−1"]],
    colLabels=["Omit i", "Čech sign", "Primitive sign", "Product"],
    cellLoc="center", bbox=[.02,.43,.96,.37])
table.auto_set_font_size(False); table.set_fontsize(10.3)
for (row,col), cell in table.get_celld().items():
    cell.set_edgecolor("#cbd5df")
    cell.set_facecolor("#e8eff6" if row==0 else ("#ffffff" if row%2 else "#f0f5f8"))
    if row==0: cell.get_text().set_fontweight("bold")
ax.text(.5,.33, r"$c_{\widehat i}=r_N(-1)^iS_i$", ha="center", transform=ax.transAxes, fontsize=13)
ax.text(.5,.24, r"$d(0,c)=(0,-r_N\sum_i S_i)$", ha="center", transform=ax.transAxes, fontsize=12)
ax.text(.5,.1, "AN.11–AN.12: each coefficient extends\non its actual omitted-coordinate face.",
    ha="center", va="top", transform=ax.transAxes, fontsize=10, color="#3a4a5b")

ax = axes[2]
ax.set_title("Separated ordinary residue circles")
ax.add_patch(Circle((0,0),1.5,fill=False,color="#d0a76b",linewidth=1.7,linestyle="--"))
ax.add_patch(Circle((0,0),.25,fill=False,color="#315b94",linewidth=2.6))
ax.scatter([0,1],[0,0],color=["#315b94","#a24676"],s=45,zorder=5)
ax.text(-.1,-.19,r"$u=0$",ha="right"); ax.text(1.08,.1,r"$v=1$",ha="left")
ax.annotate("positive orientation",xy=(0,.25),xytext=(-1.65,.72),
    arrowprops={"arrowstyle":"->","color":"#315b94"},color="#315b94",fontsize=10)
ax.annotate(r"$|s-u|=1/4$",xy=(.25,0),xytext=(.62,-.7),
    arrowprops={"arrowstyle":"->","color":"#315b94"},fontsize=11)
ax.text(-1.31,1.5,r"outer radius $3/2$",color="#956128",fontsize=10)
ax.text(0,-1.95,r"$|s-u|=1/4,\quad |v-s|\geq3/4$",ha="center",fontsize=12)
ax.text(0,-2.27,"OR.6–OR.12: integrate on compact tori.\nNo current limit at either singularity.",
    ha="center",va="top",fontsize=10,color="#3a4a5b")
ax.axhline(0,color="#d6dce3",linewidth=.8); ax.axvline(0,color="#d6dce3",linewidth=.8)
ax.set_xlim(-1.95,1.95); ax.set_ylim(-2.65,1.8); ax.set_aspect("equal"); ax.set_xticks([]);ax.set_yticks([])
for spine in ax.spines.values():spine.set_visible(False)
fig.suptitle("Actual holomorphic data, deletion signs, and residue separation", fontsize=16, fontweight="bold", y=.98)
fig.text(.5,.025,"Proof locators: AN.1–AN.4 and OR.1–OR.4. Exact planar slices and finite cover data; the proofs retain every normal coordinate and infinite coefficient index.",
    ha="center",fontsize=9.5,color="#334557")
fig.subplots_adjust(left=.035,right=.975,top=.87,bottom=.12,wspace=.2)
fig.savefig(out/"angular-residue-geometry.png",dpi=150,facecolor=fig.get_facecolor(),metadata={"Software":"Matplotlib"})
fig.savefig(out/"angular-residue-geometry.svg",facecolor=fig.get_facecolor(),metadata={"Date":None,"Creator":"Matplotlib"})
plt.close(fig)
print(json.dumps({"outputs": ["angular-residue-geometry.png", "angular-residue-geometry.svg", "angular-residue-geometry-data.json"]}))
