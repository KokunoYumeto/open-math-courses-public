from pathlib import Path
import json
from datetime import datetime, timezone
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import sympy as sp

root = Path(__file__).resolve().parent

plt.rcParams.update({"font.size": 12, "svg.fonttype": "none"})
t = np.linspace(-1, 1, 501)
v = np.sqrt(3) / 2
fig, axes = plt.subplots(1, 2, figsize=(13, 4.9), constrained_layout=True)
axes[0].plot(t[t <= 0], v * np.abs(t[t <= 0]), color="#2166ac", lw=3, label=r"incoming $\xi=\sqrt{3}/2$")
axes[0].plot(t[t >= 0], v * np.abs(t[t >= 0]), color="#b2182b", lw=3, label=r"outgoing $\xi=-\sqrt{3}/2$")
axes[0].scatter([-1, 0, 1], [v, 0, v], s=55, c=["#2166ac", "#333333", "#b2182b"], zorder=3)
axes[0].annotate("boundary: both roots compress to σ=0", (0, 0), xytext=(0, .27), ha="center", arrowprops={"arrowstyle": "->"})
axes[0].set(xlabel=r"physical time $t$", ylabel=r"normal coordinate $x$", title=r"$x=(\sqrt{3}/2)|t|$")
axes[0].legend(loc="upper center", fontsize=10)
axes[0].set_ylim(-.08, 1.16)
axes[1].plot(t, .75*t, color="#4d9221", lw=3)
axes[1].scatter([-1,0,1],[-.75,0,.75], c=["#2166ac","#333333","#b2182b"], s=55, zorder=3)
axes[1].annotate("incoming half: e<0", (-.65,-.4875), xytext=(-.55,.24), ha="center", arrowprops={"arrowstyle":"->"})
axes[1].annotate("outgoing half: e>0", (.65,.4875), xytext=(.40,-.37), ha="center", arrowprops={"arrowstyle":"->"})
axes[1].set(xlabel=r"physical time $t$", ylabel=r"compressed clock $e=-\sigma/|\tau|$", title=r"$e=3t/4$ is continuous and increasing")
for ax in axes:
    ax.axhline(0,color="#777777",lw=.8)
    ax.axvline(0,color="#777777",lw=.8)
    ax.grid(alpha=.2)
    ax.set_xlim(-1.08,1.08)
fig.suptitle(r"Flat wave: $\tau=1,\ \zeta=1/2,\ y=-t/2$; two coordinate projections", fontsize=15)
svg = root/"reflection-clock.svg"
png = root/"reflection-clock.png"
fig.savefig(svg)
fig.savefig(png, dpi=150)
plt.close(fig)
s=sp.symbols("s",real=True)
vs=sp.sqrt(3)/2
for sign in [1,-1]:
    xi=sign*vs
    x=-2*xi*s
    tt=2*s
    y=-s
    assert sp.simplify(1-xi**2-sp.Rational(1,4))==0
    assert sp.diff(x,s)==-2*xi
    assert sp.diff(tt,s)==2
    assert sp.diff(y,s)==-1
    assert sp.simplify(-x*xi-sp.Rational(3,4)*tt)==0
