"""Exact coordinate diagram for the Hilbert graded core models.

Run: python render.py
No external data or network access is used. Original drawing: CC0-1.0.
"""
from pathlib import Path
import json
import shutil
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
plt.rcParams["svg.hashsalt"] = "oa-flow-hilbert-graded-core-20261008-v1"
from matplotlib import font_manager
from matplotlib.patches import FancyArrowPatch, Rectangle, Ellipse

HERE = Path(__file__).resolve().parent
plt.rcParams.update({"font.family": "DejaVu Sans", "font.size": 13,
                     "mathtext.fontset": "dejavusans", "svg.fonttype": "none"})
BLUE = "#176495"
ORANGE = "#aa5426"
GREEN = "#267957"
INK = "#203141"
MUTED = "#536471"
fig, axes = plt.subplots(2, 2, figsize=(16, 12))
fig.patch.set_facecolor("#fbfcfe")
fig.subplots_adjust(left=.04, right=.97, bottom=.06, top=.89, hspace=.22, wspace=.13)
fig.suptitle("Hilbert fibers: Fourier phase, right action, and retained unitary phase",
             fontsize=22, fontweight="bold", x=.505, y=.965, color=INK)
fig.text(.5, .925, "Exact scalar and 2 × 2 models  •  HLB Section 9 and Diagnostics A–E",
         ha="center", color=MUTED, fontsize=14)

def panel(ax, title):
    ax.set(xlim=(0, 1), ylim=(0, 1))
    ax.axis("off")
    ax.add_patch(Rectangle((0, 0), 1, 1, fill=False, edgecolor="#cbd5df", linewidth=1.2))
    ax.text(.035, .945, title, ha="left", va="top", fontsize=17,
            fontweight="bold", color=INK)

def txt(ax, x, y, s, **kwargs):
    ax.text(x, y, s, color=kwargs.pop("color", INK), **kwargs)

def arrow(ax, p, q, color=INK, **kwargs):
    ax.add_patch(FancyArrowPatch(p, q, arrowstyle="-|>", mutation_scale=15,
                                linewidth=1.6, color=color, **kwargs))

def matrix(ax, x, y, cells, title=None, color=BLUE, scale=1):
    w, h = .15 * scale, .16 * scale
    for i in range(2):
        for j in range(2):
            xx, yy = x + j*w, y-i*h
            ax.add_patch(Rectangle((xx-w/2, yy-h/2), w, h,
                                  facecolor="#f0f6fa", edgecolor="#ccd8e1"))
            txt(ax, xx, yy, cells[i][j], ha="center", va="center", fontsize=16, color=color)
    if title:
        txt(ax, x+w/2, y+h*.95, title, ha="center", fontsize=16, color=color)

ax=axes[0,0]
panel(ax, "A  Scalar Fourier coordinates")
txt(ax, .5, .79, r"$\widehat F(q)=\int e^{-iqs}F(s)\,ds$", ha="center", fontsize=19)
txt(ax, .5, .68, r"$L^2(ds)\ \longrightarrow\ L^2(dq/(2\pi))$", ha="center", fontsize=17)
txt(ax, .5, .57, r"$\lambda_t\mapsto e^{-itq},\quad h_\varphi=e^{-q},\quad\theta_r f(q)=f(q+r)$",
    ha="center", fontsize=16)
r=np.log(2)
qmin,qmax=-1.1,1.4
qx=lambda q:.12+.76*(q-qmin)/(qmax-qmin)
arrow(ax,(.1,.215),(.92,.215),color=MUTED)
txt(ax,.94,.21,r"$q$",va="center")
for q,label in [(-r,r"$-r$"),(0,"0"),(1-r,r"$1-r$"),(1,"1")]:
    ax.plot([qx(q),qx(q)],[.20,.23],color=MUTED,lw=1)
    txt(ax,qx(q),.17,label,ha="center",fontsize=12)
ax.plot([qx(0),qx(1)],[.425,.425],color=BLUE,lw=9,solid_capstyle="butt")
ax.plot([qx(-r),qx(1-r)],[.31,.31],color=ORANGE,lw=9,solid_capstyle="butt")
txt(ax,.035,.425,r"$P$",color=BLUE,va="center",fontsize=16)
txt(ax,.035,.31,r"$\theta_rP$",color=ORANGE,va="center",fontsize=16)
txt(ax,.5,.07,r"$r=\log 2:\quad\tau(P)=\frac{e-1}{2\pi},\quad\tau(\theta_rP)=\frac{1}{2}\tau(P)$",
    ha="center",fontsize=15)

ax=axes[0,1]
panel(ax,"B  A sign-sensitive right action")
txt(ax,.5,.79,r"$h=\operatorname{diag}(3,1)$"+";   k has rows (2, 1), (1, 2)",
    ha="center",fontsize=16)
txt(ax,.5,.69,r"$t_*=\pi/(2\log3),\qquad D^{it}\xi=h^{it}\xi k^{-it}$",ha="center",fontsize=16)
matrix(ax,.22,.49,[["1",r"$-i$"],[r"$i$","1"]],r"$2p_+$",BLUE,scale=.95)
matrix(ax,.68,.49,[["1",r"$i$"],[r"$-i$","1"]],r"$2p_-$",ORANGE,scale=.95)
txt(ax,.5,.215,r"$z=D^{it_*}e_{11}=\frac{1}{2}((1+i)e_{11}+(1-i)e_{12})$",
    ha="center",fontsize=17)
txt(ax,.27,.09,r"$z p_+=z$",ha="center",color=BLUE,fontsize=20)
txt(ax,.74,.09,r"$z p_-=0$",ha="center",color=ORANGE,fontsize=20)

ax=axes[1,0]
panel(ax,"C  The two-fiber commutant square")
txt(ax,.5,.80,r"$s=0,\quad r=t_*,\quad b=e_{11}\psi^{it}$",ha="center",fontsize=16)
pts={(0,0):(.22,.60),(1,0):(.77,.60),(0,1):(.22,.27),(1,1):(.77,.27)}
for (i,j),(x,y) in pts.items():
    label=[[r"$H(0)$",r"$H(r)$"],[r"$H(t)$",r"$H(r+t)$"]][j][i]
    ax.add_patch(Rectangle((x-.115,y-.065),.23,.13,facecolor="#edf4f8",edgecolor="#b7c9d6"))
    txt(ax,x,y,label,ha="center",va="center",fontsize=18)
arrow(ax,(.345,.60),(.64,.60))
arrow(ax,(.345,.27),(.64,.27))
arrow(ax,(.22,.52),(.22,.35),color=BLUE)
arrow(ax,(.77,.52),(.77,.35),color=ORANGE)
txt(ax,.495,.655,r"$L_xD^{ir}$",ha="center",fontsize=16)
txt(ax,.495,.325,r"$L_xD^{ir}$",ha="center",fontsize=16)
txt(ax,.205,.435,r"$A_0=R_{e_{11}}$",ha="right",fontsize=14,color=BLUE)
txt(ax,.79,.435,r"$B_0=R_{p_+}$",ha="left",fontsize=14,color=ORANGE)
txt(ax,.5,.08,r"$B_0L_xD^{ir}=L_xD^{ir}A_0\quad\text{for every }x\in M_2$",ha="center",fontsize=15)

ax=axes[1,1]
panel(ax,"D  Vectors, not phase classes")
txt(ax,.5,.80,r"$U\xi=S\xi S,\quad S=e_{12}+e_{21}$",ha="center",fontsize=16)
txt(ax,.5,.70,r"$\operatorname{Ad}(U)=\operatorname{Ad}(iU)$",ha="center",fontsize=17)
# Coordinates of the actual image vectors in the one-dimensional complex line C e22.
cx,cy,ry=.44,.345,.215
# Equal physical axis units: compensate for the wide panel's aspect ratio.
box=ax.get_position()
rx=ry*(box.height*fig.get_figheight())/(box.width*fig.get_figwidth())
ax.add_patch(Ellipse((cx,cy),2*rx,2*ry,fill=False,edgecolor="#c9d3dc",lw=1.2))
arrow(ax,(cx-rx-.065,cy),(cx+rx+.10,cy),color=MUTED)
arrow(ax,(cx,cy-ry-.04),(cx,cy+ry+.065),color=MUTED)
txt(ax,cx+rx+.105,cy-.015,"Re",fontsize=11)
txt(ax,cx-.015,cy+ry+.075,"Im",fontsize=11)
ax.plot([cx+rx,cx],[cy,cy+ry],color=GREEN,lw=2)
ax.scatter([cx+rx,cx],[cy,cy+ry],c=[BLUE,ORANGE],s=75,zorder=4)
txt(ax,cx+rx+.025,cy-.085,r"$Ue_{11}=e_{22}$",fontsize=15,color=BLUE)
txt(ax,cx+.035,cy+ry+.025,r"$iUe_{11}=ie_{22}$",fontsize=15,color=ORANGE)
txt(ax,cx+rx*.7,cy+ry*.7,r"$\sqrt{2}$",color=GREEN,fontsize=17)
txt(ax,.5,.045,r"$U^2=I,\qquad(iU)^2=-I$",ha="center",fontsize=16)

fig.text(.5,.017,"All signs, degrees, matrices, and trace factors are exact. See the accompanying proofs and data.",
         ha="center",fontsize=12,color=MUTED)
for ext in ("png","svg"):
    fig.savefig(HERE/f"hilbert-graded-core.{ext}",dpi=160,facecolor=fig.get_facecolor(), **({"metadata": {"Date": None}} if ext == "svg" else {}))
plt.close(fig)

data={
 "title":"Hilbert graded core: exact coordinate models",
 "license":"CC0-1.0 to the extent of rights held; font terms separate",
 "scalar":{"transform":"Fhat(q)=integral exp(-i*q*s) F(s) ds","domain_measure":"ds","target_measure":"dq/(2*pi)",
           "translation":"lambda_t F(s)=F(s-t)","generator_image":"exp(-i*t*q)","density":"exp(-q)",
           "dual":"theta_r f(q)=f(q+r)","trace_density":"exp(q)/(2*pi)","projection_support":[0,1],
           "r":"log(2)","translated_support":["-log(2)","1-log(2)"],"trace":"(e-1)/(2*pi)","trace_ratio":"1/2"},
 "matrix":{"h":[[3,0],[0,1]],"k":[[2,1],[1,2]],"t_star":"pi/(2*log(3))", "spatial":"D^it xi=h^it xi k^-it",
           "2p_plus":[["1","-i"],["i","1"]],"2p_minus":[["1","i"],["-i","1"]],
           "2z":[["1+i","1-i"],["0","0"]],"identities":["z*p_plus=z","z*p_minus=0","norm_HS(z)=1"]},
 "square":{"source_degrees":["0","r"],"target_degrees":["t","r+t"],"r":"t_star", "A0":"R_e11","B0":"R_p_plus",
           "horizontal":"L_x D^ir","identity":"B0 L_x D^ir = L_x D^ir A0 for every x in M2"},
 "phase":{"S":[[0,1],[1,0]],"U":"xi -> S xi S","inputs":"e11","outputs":["e22","i e22"],
          "distance":"sqrt(2)","plane":"exact complex line C e22","second_iterates":["I","-I"]},
 "proof_locators":["HLB9.b-d","HLB9.j-k","HLB9.n","HLB10.b-e"],
 "sampling":"None. The displayed objects and labels are exact; only page positions are drawing coordinates."
}
(HERE/"data.json").write_text(json.dumps(data,indent=2)+"\n",encoding="utf-8")
font=Path(font_manager.findfont("DejaVu Sans"))
license_file=font.parent/"LICENSE_DEJAVU"
if not license_file.is_file():
    raise FileNotFoundError("The bundled DejaVu license must be preserved.")
shutil.copyfile(license_file,HERE/"FONT-LICENSE.txt")
(HERE/"TERMS.md").write_text("# Figure terms\n\nOriginal diagram, renderer, and exact mathematical data: CC0-1.0 to the extent of rights held. The figure contains no external image or book excerpt. DejaVu font terms are retained in FONT-LICENSE.txt. Run `python render.py` with NumPy and Matplotlib to regenerate the PNG, editable SVG, and data. Mathematical claims and proof locators are recorded in data.json and in Sections 9–10 of the lesson.\n",encoding="utf-8")
print("Rendered PNG and SVG; exact data, renderer, and font terms retained.")
