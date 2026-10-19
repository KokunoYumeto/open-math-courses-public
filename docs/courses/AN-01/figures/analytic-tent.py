"""Exact one-dimensional tent contour and Gaussian phase for AN01-U095, Lemma 3.
Original figure: GPT-6 Astra (OpenAI), Ultra, October 2026. CC0.
Run in this directory with numpy and matplotlib; writes SVG and PNG.
"""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
matplotlib.rcParams.update({"font.size":12,"svg.hashsalt":"AN01-U095-analytic-tent","font.family":"DejaVu Sans"})
out=Path(__file__).resolve().parent
x=np.linspace(-2.05,2.05,1201);dist=np.maximum(abs(x)-1,0);height=np.maximum(1-dist,0)/2
x0=.3;a=.25
moving=np.linspace(x0-2*a,x0+2*a,501)
tent=a*(1-abs(moving-x0)/(2*a))
assert np.all(np.maximum(abs(moving)-1,0)+2*tent<=1+1e-12)
r=np.linspace(-.85,.85,851)
original=r*r-a*a
final=np.where(abs(r)<=2*a,.75*r*r,r*r-a*a)
assert np.all(final>=.75*r*r-1e-12)
fig,axs=plt.subplots(1,2,figsize=(12.8,4.9),layout="constrained")
ax=axs[0]
ax.fill_between(x,-height,height,color="#e2edf9",label=r"$K_1:\ d(x,[-1,1])+2|y|\leq1$")
ax.plot(x,height,color="#6a88aa",lw=1);ax.plot(x,-height,color="#6a88aa",lw=1)
ax.axhline(0,color="#7f8791",lw=1);ax.plot([-1,1],[0,0],color="#283c52",lw=4,label=r"$K=[-1,1]$")
ax.plot(moving,tent,color="#b54132",lw=2.8,label=r"$Z_1(x)=x+0.25i(1-|x-0.3|/0.5)_+$")
ax.scatter([x0],[a],color="#172334",s=32,zorder=5)
ax.annotate(r"$z_0=0.3+0.25i$",xy=(x0,a),xytext=(.6,.4),arrowprops={"arrowstyle":"->","color":"#172334"},fontsize=11)
ax.set(xlim=(-2.1,2.1),ylim=(-.64,.64),xlabel=r"Real coordinate $x$",ylabel=r"Imaginary coordinate $y$",title="The contour stays inside the neighborhood")
ax.legend(loc="lower center",fontsize=9,framealpha=.95);ax.grid(alpha=.15)
ax=axs[1]
ax.axhline(0,color="#7f8791",lw=1)
ax.plot(r,original,"--",color="#8d7199",lw=2,label=r"Real path: $r^2-a^2$")
ax.plot(r,final,color="#b54132",lw=2.8,label="Deformed path")
ax.plot(r,.75*r*r,":",color="#23567e",lw=2,label=r"Lower bound: $3r^2/4$")
ax.axvline(-.5,color="#9da5af",lw=1,ls=":");ax.axvline(.5,color="#9da5af",lw=1,ls=":")
ax.text(0,.39,r"$\operatorname{Re}(z_0-Z_1)^2=3r^2/4$"+"\n"+r"for $|r|\leq 0.5$",ha="center",fontsize=11)
ax.set(xlim=(-.85,.85),ylim=(-.1,.72),xlabel=r"Signed displacement $r=x-x_0$",ylabel="Real part of the Gaussian phase",title="Positive phase gives uniform Gaussian decay")
ax.legend(loc="upper center",fontsize=10);ax.grid(alpha=.15)
fig.savefig(out/"analytic-tent.png",dpi=160,metadata={"Software":"Matplotlib; original CC0 figure"})
fig.savefig(out/"analytic-tent.svg",metadata={"Date":None,"Creator":"GPT-6 Astra (OpenAI), Ultra; CC0"})
p=out/"analytic-tent.svg";p.write_text("\n".join(line.rstrip() for line in p.read_text().splitlines())+"\n")
plt.close(fig)
