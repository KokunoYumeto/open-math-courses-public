"""Exact carrier neighborhoods for AN01-U097, (N1), (N7) and Lemma5.
Original figure: GPT-6 Astra (OpenAI), Ultra, October 2026. CC0.
Run with numpy and matplotlib; creates PNG and SVG beside this source.
"""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Polygon,Circle
out=Path(__file__).resolve().parent
matplotlib.rcParams.update({"font.size":11,"font.family":"DejaVu Sans","svg.hashsalt":"AN01-U097-carrier-neighborhoods"})
epsilon=.45;centers=[-1.,1.]
fig,axs=plt.subplots(1,2,figsize=(11.5,4.7),layout="constrained")
for ax in axs:
 ax.axhline(0,color="#a3adb8",lw=.8);ax.axvline(0,color="#a3adb8",lw=.8)
 ax.set(xlim=(-1.75,1.75),ylim=(-.8,.8));ax.set_aspect("equal")
 ax.grid(alpha=.15);ax.set_xticks([-1.5,-1,0,1,1.5])
ax=axs[0]
for c in centers:
 vertices=np.array([[c-epsilon,0],[c,epsilon/2],[c+epsilon,0],[c,-epsilon/2]])
 assert np.max(abs(abs(vertices[:,0]-c)+2*abs(vertices[:,1])-epsilon))<1e-14
 ax.add_patch(Polygon(vertices,facecolor="#d2e6f6",edgecolor="#235788",lw=1.6))
 ax.scatter([c],[0],s=24,c="#172334",zorder=4)
ax.annotate(r"$\varepsilon/2$",xy=(1,epsilon/2),xytext=(.8,.59),arrowprops={"arrowstyle":"->","color":"#235788"},ha="center")
ax.annotate(r"$\varepsilon$",xy=(-1-epsilon,0),xytext=(-1.3,-.57),arrowprops={"arrowstyle":"->","color":"#235788"},ha="center")
ax.set(xlabel=r"$\operatorname{Re}z$",ylabel=r"$\operatorname{Im}z$",title="Complex carrier neighborhood")
ax.text(0,-.74,r"$\min(|\operatorname{Re}z-1|,|\operatorname{Re}z+1|)+2|\operatorname{Im}z|\leq0.45$",ha="center",fontsize=9)
ax=axs[1]
for c in centers:
 ax.add_patch(Circle((c,0),epsilon,facecolor="#e6e1f1",edgecolor="#725b94",lw=1.6))
 ax.scatter([c],[0],s=42,facecolors="white",edgecolors="#172334",zorder=5,linewidths=1.3)
X=np.array([1.2,.25]);Y=np.array([1.,0])
assert np.linalg.norm(X-Y)<epsilon
s=np.linspace(0,1,301);segment=(1-s[:,None])*X+s[:,None]*Y
assert np.all(np.linalg.norm(segment-Y,axis=1)<=epsilon)
ax.plot(segment[:,0],segment[:,1],color="#ba512e",lw=2,zorder=4)
ax.scatter([X[0]],[X[1]],color="#ba512e",s=28,zorder=5)
ax.annotate(r"$X=(1.2,0.25)$",xy=X,xytext=(.59,.63),arrowprops={"arrowstyle":"->","color":"#ba512e"},ha="center",fontsize=10)
ax.annotate("Excluded endpoint",xy=Y,xytext=(.57,-.62),arrowprops={"arrowstyle":"->","color":"#172334"},ha="center",fontsize=10)
ax.annotate(r"$\varepsilon=0.45$",xy=(-1,.45),xytext=(-1.05,.66),ha="center",fontsize=10)
ax.set(xlabel=r"$x$",ylabel=r"$t$",title="Real tube and its nearest-center path")
fig.savefig(out/"carrier-neighborhoods.png",dpi=160,metadata={"Software":"Matplotlib; original CC0 figure"})
fig.savefig(out/"carrier-neighborhoods.svg",metadata={"Date":None,"Creator":"GPT-6 Astra (OpenAI), Ultra; CC0"})
p=out/"carrier-neighborhoods.svg";p.write_text("\n".join(l.rstrip() for l in p.read_text().splitlines())+"\n")
plt.close(fig)
