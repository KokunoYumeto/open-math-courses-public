"""Exact nodal-curve illustration. GPT-6 Astra (OpenAI), Ultra, 2026. CC0-1.0.
Run with Python, NumPy and Matplotlib; outputs are written beside this script.
"""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Circle

OUT = Path(__file__).resolve().parent
plt.rcParams.update({"font.family": "DejaVu Sans", "font.size": 12,
                     "svg.fonttype": "none", "svg.hashsalt": "SH03-global-branches"})
fig, axes = plt.subplots(1, 2, figsize=(12, 4.7), constrained_layout=True)
left, right = axes
blue, orange = "#1769aa", "#c45a13"

left.axhline(0, color="#b9bec5", lw=.8)
left.axvline(0, color="#b9bec5", lw=.8)
for t0, color in [(-1, orange), (1, blue)]:
    left.add_patch(Circle((t0, 0), .24, fill=False, linestyle="--",
                          edgecolor=color, lw=1.7))
    left.plot(t0, 0, "o", ms=8, mfc="white", mec=color, mew=2, zorder=4)
    left.annotate(f"t = {t0}", (t0, 0), xytext=(t0, -.4),
                  ha="center", color=color)
theta = np.linspace(0, np.pi, 401)
left.plot(.86*np.cos(theta), .64*np.sin(theta), color="#333333", lw=2)
left.annotate("", xy=(0.0,.64), xytext=(.18,.625),
              arrowprops={"arrowstyle":"->", "color":"#333333", "lw":2})
left.text(0, 1.0, "A path in the connected regular domain", ha="center")
left.text(0, -.83, "The two punctured neighborhoods have disconnected union;\n"
          "the full regular domain is connected.", ha="center", fontsize=10.5)
left.set(xlim=(-1.6,1.6), ylim=(-1.1,1.3), xlabel="Re t", ylabel="Im t",
         title=r"Full complex parameter domain: $\mathbb{C}\setminus\{-1,1\}$")
left.set_aspect("equal", adjustable="box")
left.set_xticks([-1,0,1]); left.set_yticks([-1,0,1])

t = np.linspace(-1.62,1.62,1500)
right.plot(t*t-1,t*(t*t-1),color="#747c86",lw=2)
for t0, color in [(-1, orange), (1, blue)]:
    tt=np.linspace(t0-.19,t0+.19,250)
    right.plot(tt*tt-1,tt*(tt*tt-1),color=color,lw=3)
right.axhline(0,color="#b9bec5",lw=.8,zorder=0)
right.axvline(0,color="#b9bec5",lw=.8,zorder=0)
right.plot(0,0,"o",ms=8,mfc="white",mec="#222222",mew=2,zorder=5)
right.annotate("node: both omitted parameters map here",
               (0,0),xytext=(-1.05,1.9),
               arrowprops={"arrowstyle":"->","color":"#333333"},
               fontsize=10.5)
right.text(.64,.6,r"$y=+x\sqrt{1+x}$",color=blue,fontsize=11)
right.text(.64,-.85,r"$y=-x\sqrt{1+x}$",color=orange,fontsize=11)
right.text(-.95,-2.2,"Right panel shows only the real trace;\n"
           "the complex curve lies in "+r"$\mathbb{C}^2$"+".",fontsize=10.5)
right.set(xlim=(-1.15,1.9),ylim=(-2.7,2.7),xlabel="real x",ylabel="real y",
          title=r"Real trace of $y^2=x^2(x+1)$")
fig.suptitle(r"$\nu(t)=(t^2-1,\ t(t^2-1))$: one global component, two local branches",
             fontsize=15)
fig.savefig(OUT/"global-branches.png",dpi=180)
fig.savefig(OUT/"global-branches.svg", metadata={"Title": "One global component and two local branches", "Creator": "GPT-6 Astra (OpenAI), Ultra", "Description": "Complex punctured parameter plane and explicitly labelled real trace of the nodal curve y^2=x^2(x+1).", "Rights": "CC0-1.0", "Date": None})
