"""Exact two-dimensional support drawings; original scene data, CC0."""
from pathlib import Path
import json
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

ROOT = Path(__file__).resolve().parent
OUT = ROOT / "figures"
OUT.mkdir(exist_ok=True)
plt.rcParams.update({"font.family": "DejaVu Sans", "font.size": 15, "svg.fonttype": "none",
                     "svg.hashsalt": "support-cone-forward-exact-model"})
a = np.array([1, -1])
v1, v2 = np.array([1, 1]), np.array([1, -1])
kernel = [a, a+v1, a+v2, a+v1+v2]
coefficients = [1, -2, -3, 6]

def setup():
    fig, ax = plt.subplots(figsize=(7.6, 7.6), dpi=160)
    ax.set_aspect("equal")
    ax.axhline(0, color="#818e9f", lw=.9)
    ax.axvline(0, color="#818e9f", lw=.9)
    ax.set_xlabel("$x$", fontsize=21)
    ax.set_ylabel("$y$", fontsize=21, rotation=0, labelpad=12)
    ax.spines[["top","right"]].set_visible(False)
    ax.grid(alpha=.15)
    return fig, ax

fig, ax = setup()
xx = np.linspace(-1, 8, 200)
ax.fill_between(xx, 1-(xx+1), 1+(xx+1), color="#c7e2f8", alpha=.75)
pts = np.array([-a+j*v1+k*v2 for j in range(7) for k in range(7) if j+k<=7])
ax.scatter(pts[:,0], pts[:,1], color="#185a91", s=26, zorder=3)
ax.plot([-1,8],[1,10], color="#185a91", lw=2)
ax.plot([-1,8],[1,-8], color="#185a91", lw=2)
for direction in [v1, v2]:
    start = -a+4.8*direction
    end = -a+5.5*direction
    ax.annotate("", end, start, arrowprops=dict(arrowstyle="-|>", lw=2.2, color="#185a91"))
for point, coef in zip(kernel, coefficients):
    ax.scatter(*point, color="#b34d15", marker="s", s=78, zorder=5)
    dx, dy = ((-.75,-.6) if coef==1 else (.15,.3) if coef==-2 else (.2,-.65) if coef==-3 else (.2,-.7))
    ax.text(point[0]+dx,point[1]+dy, str(coef), fontsize=16, color="#863305",
            bbox=dict(facecolor="white",alpha=.9,edgecolor="none",pad=1))
ax.scatter(*(-a),s=85,facecolor="white",edgecolor="#185a91",lw=2,zorder=4)
ax.annotate("$-a=(-1,1)$",(-1,1),(-2.05,2.55),fontsize=16,
            arrowprops=dict(arrowstyle="-",color="#185a91"))
ax.text(4.4,2.5,"$K=C-a$",fontsize=21,color="#185a91")
ax.text(3.25,-3.3,"kernel coefficients",fontsize=15,color="#863305")
ax.set_title("Inverse lattice and its support hull",fontsize=17,pad=15)
ax.text(.04,.025,r"$C=\{(x,y):x\geq|y|\}$",transform=ax.transAxes,fontsize=17,
        bbox=dict(facecolor="white",alpha=.92,edgecolor="none"))
ax.set_xlim(-2.5,8)
ax.set_ylim(-6.5,7)
fig.tight_layout()
fig.savefig(OUT/"translated-cone-and-kernel.png")
fig.savefig(OUT/"translated-cone-and-kernel.svg",metadata={"Date":None})
plt.close(fig)

fig, ax = setup()
xx = np.linspace(0,7,200)
ax.fill_between(xx,-xx,xx,color="#d9eedf",alpha=.9)
ax.plot([0,7],[0,7],color="#246743",lw=2)
ax.plot([0,7],[0,-7],color="#246743",lw=2)
ax.axvline(3,color="#b34d15",ls="--",lw=1.8)
ax.scatter(0,0,s=75,facecolor="white",edgecolor="#246743",lw=2,zorder=4)
ax.text(-.75,.25,"$0$",fontsize=18)
error=[(3,3,-8),(3,-3,-27),(6,0,216)]
for x,y,c in error:
    ax.scatter(x,y,s=100,color="#b34d15",zorder=5)
    offset=(.23,.25) if c==-8 else (.23,-.65) if c==-27 else (-.55,.55)
    ax.text(x+offset[0],y+offset[1],"$"+str(c)+"$",fontsize=18,color="#863305",
            bbox=dict(facecolor="white",alpha=.95,edgecolor="none",pad=2))
ax.text(4.7,2,"$C$",fontsize=24,color="#246743")
ax.text(3.2,-4.6,"$x=3$",fontsize=18,color="#863305")
ax.arrow(1.8,-1.2,-1.5,0,width=.015,head_width=.16,head_length=.18,
         length_includes_head=True,color="#263747")
ax.text(1.85,-1.1,r"$\eta=(-1,0)$",fontsize=16,color="#263747")
ax.set_title("Exact support of the compact error",fontsize=17,pad=15)
ax.text(.04,.027,r"$H_{R_2}(-1,0)=-3$",transform=ax.transAxes,fontsize=19,
        bbox=dict(facecolor="white",alpha=.95,edgecolor="none"))
ax.set_xlim(-1.1,7.2)
ax.set_ylim(-5.4,5.4)
fig.tight_layout()
fig.savefig(OUT/"finite-truncation-error.png")
fig.savefig(OUT/"finite-truncation-error.svg",metadata={"Date":None})
plt.close(fig)

scene = {"schema":"exact-mathematical-scene/v1","license":"CC0-1.0","a":a.tolist(),
         "v1":v1.tolist(),"v2":v2.tolist(),"kernel_support":[p.tolist() for p in kernel],
         "kernel_coefficients":coefficients,"inverse_support":"-a+j*v1+k*v2, j,k nonnegative integers",
         "inverse_hull":"x+1 >= abs(y-1)","negative_dual_interior":"eta_x < -abs(eta_y)",
         "error_truncation":"0 <= j,k <= 2","error_atoms":error,
         "error_support_function_at_eta_minus_e1":-3,
         "proof_locators":["manuscript.md Theorem1.1","Example6.1 equations6.1-6.7","Section5 equations5.7-5.12"],
         "scene_scope":"Exact worked model; finite displayed inverse lattice is not the full support",
         "blender_decision":"Two-dimensional affine support geometry is clearer in exact Cartesian drawings."}
(OUT/"scene.json").write_text(json.dumps(scene,indent=2)+"\n",encoding="utf-8")
print("Created two exact editable figures and their scene data.")
