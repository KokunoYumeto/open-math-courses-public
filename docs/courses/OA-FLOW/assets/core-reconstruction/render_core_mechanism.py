"""Reproducible exact-coordinate illustration for C9-C11 and C16-C17/C32.

CC0-1.0 to the extent of rights in this new figure source.
No simulation of a von Neumann algebra is asserted.
"""
from pathlib import Path
import re
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Polygon

HERE = Path(__file__).resolve().parent
OUT = HERE / "assets"
OUT.mkdir(exist_ok=True)
plt.rcParams.update({"font.family": "DejaVu Sans", "font.size": 12, "svg.hashsalt": "OA-FLOW-core-reconstruction-v1"})
fig, (left, right) = plt.subplots(1, 2, figsize=(13.2, 6.0))
fig.subplots_adjust(left=.07, right=.97, top=.83, bottom=.28, wspace=.34)
fig.suptitle("Spectral bands make the trace finite; translation fixes its scaling", fontsize=17, y=.96)

left.add_patch(Polygon([(0,-1),(0,0),(1,1),(1,0)], closed=True,
                      facecolor="#d4e9ed", edgecolor="#146477", linewidth=2))
left.plot([0,1],[0,1], color="#146477", lw=2)
left.plot([0,1],[-1,0], color="#146477", lw=2)
left.axhline(0,color=".78",lw=.8,zorder=0)
left.set(xlim=(-.15,1.2),ylim=(-1.2,1.2),xticks=[0,.5,1],yticks=[-1,0,1],
         xlabel=r"Fourier variable $r$",ylabel=r"Modular spectral variable $u$")
left.set_title(r"$I=[0,1]$: $r\in I$ and $r-u\in I$",fontsize=13,pad=16)
left.text(.5,-.03,r"$-1\leq u\leq1$",ha="center",va="center",fontsize=15)
left.text(.52,.80,r"$r-u=0$",rotation=34,ha="center",color="#146477")
left.text(.5,-.77,r"$r-u=1$",rotation=34,ha="center",color="#146477")
left.text(.5,-.24,r"$b_I(r)e^{u/2}=b_I(r-u)$",ha="center",transform=left.transAxes,fontsize=13)

r = np.linspace(0,2.15,500)
right.plot(r,np.exp(-r)/(2*np.pi),color="#273b65",lw=2.2,label=r"$e^{-r}/(2\pi)$")
for low,high,col in [(0,1,"#76b9c8"),(1,2,"#e9b467")]:
    x = np.linspace(low,high,200)
    right.fill_between(x,0,np.exp(-x)/(2*np.pi),color=col,alpha=.75)
right.annotate("",xy=(1.55,.145),xytext=(.55,.145),
               arrowprops=dict(arrowstyle="->",lw=1.8,color="#69441d"))
right.text(1.05,.152,r"$\theta_1(e_{[0,1]})=e_{[1,2]}$",ha="center",fontsize=12)
right.text(.46,.045,r"$m$",ha="center",fontsize=18,color="#173e47")
right.text(1.49,.018,r"$e^{-1}m$",ha="center",fontsize=16,color="#68441b")
right.set(xlim=(-.06,2.16),ylim=(0,.19),xticks=[0,1,2],
          xlabel=r"Spectral variable $r$",ylabel="Trace density")
right.set_title(r"Exact scalar distribution of $P$ (C17)",fontsize=13,pad=16)
right.legend(frameon=False,loc="upper right",fontsize=11)
right.text(.5,-.24,r"$m=(1-e^{-1})/(2\pi),\qquad \tau\circ\theta_s=e^{-s}\tau$",
           transform=right.transAxes,ha="center",fontsize=12)
for ax in (left,right):
    ax.spines[["top","right"]].set_visible(False)
fig.text(.07,.048,"Left: actual joint support used in the bounded antiunitary calculation (C9–C11).\n"
        "Right: interval trace masses and their shift (C16–C17, C32). These are spectral coordinates, not a model of M.",
        fontsize=10.6,color="#333333")
fig.savefig(OUT/"core-spectral-mechanism.png",dpi=170)
svg_path = OUT/"core-spectral-mechanism.svg"
fig.savefig(svg_path, metadata={"Date": None})
# Canonical serialization changes only separators, never path tokens.
svg_text = svg_path.read_text(encoding="utf-8")
svg_text = re.sub(r'(\bd=")([^"]*)(")',
                  lambda match: match.group(1) + " ".join(match.group(2).split()) + match.group(3), svg_text)
svg_path.write_text(svg_text, encoding="utf-8", newline="\n")
plt.close(fig)
