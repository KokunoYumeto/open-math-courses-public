"""Reproduce the original continuous-model diagram and exact smoothing plot.

Original code and visual expression: CC0-1.0 to the extent of rights held.
Matplotlib and its DejaVu fonts retain their respective licences.
"""
from pathlib import Path
from fractions import Fraction
import json
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
plt.rcParams["svg.hashsalt"] = "oa-flow-measure-models-continuous-20261009-v1"
from matplotlib.patches import FancyBboxPatch
import numpy as np

OUT = Path(__file__).resolve().parent
plt.rcParams.update({
    "font.family": "DejaVu Sans", "mathtext.fontset": "dejavusans",
    "font.size": 13, "svg.fonttype": "none",
    "axes.spines.top": False, "axes.spines.right": False,
})
fig = plt.figure(figsize=(14, 10), facecolor="#fbfcfe")
gs = fig.add_gridspec(2, 1, height_ratios=[1.45, 1], hspace=.24,
                      left=.085, right=.95, top=.93, bottom=.1)
ax = fig.add_subplot(gs[0]); ax.axis("off"); ax.set_xlim(0, 1); ax.set_ylim(0, 1)
blue, green, ink = "#275c95", "#207866", "#17283e"

def box(x, y, title, subtitle, color):
    p = FancyBboxPatch((x-.17, y-.10), .34, .20,
        boxstyle="round,pad=0.012,rounding_size=0.018",
        linewidth=1.4, edgecolor=color, facecolor="white")
    ax.add_patch(p)
    ax.text(x, y+.025, title, ha="center", va="center", color=color, fontsize=21)
    ax.text(x, y-.053, subtitle, ha="center", va="center", color=ink, fontsize=11)

def arrow(a, b, color=ink):
    ax.annotate("", xy=b, xytext=a,
                arrowprops={"arrowstyle":"->", "lw":1.7, "color":color})

box(.21, .77, r"$A$", "countable smoothed generators", blue)
box(.79, .77, r"$C_0(X)$", "continuous functions on the spectrum", blue)
box(.21, .36, r"$M$", "original abelian von Neumann algebra", green)
box(.79, .36, r"$L^\infty(X,\lambda)$", "all bounded measurable classes", green)
arrow((.397,.77),(.602,.77),blue)
ax.text(.50,.835,"Gelfand isomorphism",ha="center",fontsize=11,color=blue)
ax.text(.50,.70,r"$a\longmapsto\widehat a$  (C12)",ha="center",fontsize=12,color=blue)
arrow((.397,.36),(.602,.36),green)
ax.text(.50,.425,r"$\Theta$  (C18)",ha="center",fontsize=14,color=green)
ax.text(.50,.285,"normal, with normal inverse",ha="center",fontsize=10.5,color=green)
for x in [.21,.79]:
    arrow((x,.65),(x,.48))
    ax.text(x+.022,.565,"ultraweakly\ndense inclusion",ha="left",va="center",fontsize=10.5,color=ink)
ax.text(.5,.125,r"$U:H_\varphi\ \longrightarrow\ L^2(X,\lambda),\qquad"
                      r"U\pi_\varphi(a)\xi_\varphi=\widehat a$",
        ha="center",va="center",fontsize=16,color=ink)
ax.text(.5,.025,r"$\|\pi_\varphi(a)\xi_\varphi\|^2"
                      r"=\varphi(a^*a)=\int_X|\widehat a|^2\,d\lambda$  (C16)",
        ha="center",va="center",fontsize=15,color=ink)

ax2=fig.add_subplot(gs[1]); ax2.set_facecolor("white")
eps=.25
def H(u):
    return np.select([u<=-eps,u<=0,u<eps],
                     [0,(u+eps)**2/(2*eps**2),1-(eps-u)**2/(2*eps**2)],default=1)
x=np.linspace(-.45,1.45,1601); p=H(x)-H(x-1)
ax2.plot([-.45,0,0,1,1,1.45],[0,0,1,1,0,0],ls="--",lw=2,color="#929ca6",label=r"$p=1_{[0,1]}$")
ax2.fill_between(x,0,p,color="#d7e7f6",alpha=.65)
ax2.plot(x,p,lw=3,color=blue,label=r"$p_\varepsilon=\phi_\varepsilon*p,\quad\varepsilon=1/4$")
ax2.scatter([-.25,.25,.75,1.25],[0,1,1,0],s=35,color=blue,zorder=5)
ax2.set_xticks([-.25,0,.25,.75,1,1.25],
              [r"$-\varepsilon$","0",r"$\varepsilon$",r"$1-\varepsilon$","1",r"$1+\varepsilon$"])
ax2.set_yticks([0,.5,1]); ax2.set_ylim(-.07,1.32);ax2.set_xlim(-.45,1.45)
ax2.set_xlabel(r"$x$",labelpad=6)
ax2.grid(axis="y",alpha=.18)
ax2.legend(loc="upper right",frameon=False,fontsize=11)
ax2.set_title("Smoothing preserves the orbit integral and makes the orbit norm continuous",
              loc="left",pad=14,fontsize=13,color=ink)
ax2.text(.02,.16,r"$\int p(x-t)\,dt=\int p_\varepsilon(x-t)\,dt=1$",
         transform=ax2.transAxes,fontsize=13,color=ink)
fig.suptitle("From continuous generators to the full measurable action",fontsize=20,x=.085,ha="left",color=ink)
fig.text(.085,.029,"Top: the actual maps in (C12)–(C18).  Bottom: the exact translation sample (EX1)–(EX3).",
         fontsize=11,color=ink)
fig.savefig(OUT/'continuous-model.png',dpi=220,facecolor=fig.get_facecolor())
fig.savefig(OUT/'continuous-model.svg',facecolor=fig.get_facecolor(),metadata={'Date': None})
plt.close(fig)

def exact_H(u):
    e=Fraction(1,4)
    if u<=-e:return Fraction(0)
    if u<=0:return (u+e)**2/(2*e**2)
    if u<e:return 1-(e-u)**2/(2*e**2)
    return Fraction(1)
pts=[Fraction(n,8) for n in range(-2,11)]
data={"epsilon":"1/4", "formula":"H_epsilon(x)-H_epsilon(x-1)",
      "support":["-1/4","5/4"],"plateau":["1/4","3/4"],
      "orbit_integrals":{"p":"1","p_epsilon":"1"},
      "exact_samples":[{"x":str(t),"p_epsilon":str(exact_H(t)-exact_H(t-1))} for t in pts]}
(OUT/'exact-data.json').write_text(json.dumps(data,indent=2)+'\n',encoding='utf-8')
print('Created continuous-model.png, continuous-model.svg, exact-data.json')
