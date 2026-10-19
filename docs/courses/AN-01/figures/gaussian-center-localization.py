from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Circle

plt.rcParams.update({"font.size":12,"axes.spines.top":False,"axes.spines.right":False})
fig,axes=plt.subplots(1,2,figsize=(12,4.7),layout="constrained")
ax=axes[0]
for radius,color,label,style in [(2.4,"#e9edf3","O","-"),(1.7,"#cce5e4","Y","-"),(.65,"#a7c5ec","B","--")]:
    ax.add_patch(Circle((0,0),radius,facecolor=color,edgecolor="#34516c",linestyle=style,lw=1.5))
    ax.text(-radius+.16,.15,label,fontsize=14)
ax.plot(0,0,"o",color="#18334a");ax.text(.1,-.3,r"$x_0$")
ax.annotate("",xy=(1.7,0),xytext=(.65,0),arrowprops={"arrowstyle":"<->","color":"#a23d29","lw":2})
ax.text(.95,.15,r"$d$",color="#a23d29")
ax.plot([1.92,2.1,-2.05],[-.65,1.1,-1.1],"x",color="#a23d29",ms=9)
ax.text(-2.65,-2.65,"Centers outside Y form the analytic remainder",fontsize=10)
ax.set(xlim=(-2.85,2.85),ylim=(-2.9,2.9),aspect="equal",title="Separate the retained and omitted centers")
ax.set_xticks([]);ax.set_yticks([])
ax=axes[1];x=np.linspace(-2.4,2.4,701)
for rho,color in [(1,"#4b7a9e"),(4,"#288579"),(16,"#ad542e")]:
    ax.plot(x,np.exp(-rho*x*x),label=rf"$\rho={rho}$",color=color,lw=2)
ax.set(xlabel=r"$x-y$ (here $y=0$)",ylabel=r"$e^{-\rho(x-y)^2}$",title="Exact real Gaussian decay",ylim=(-.02,1.06))
ax.grid(alpha=.2);ax.legend(frameon=False)
root=Path(__file__).parent
fig.savefig(root/"gaussian-center-localization.png",dpi=180)
fig.savefig(root/"gaussian-center-localization.svg")
svg=root/"gaussian-center-localization.svg"
svg.write_text("\n".join(line.rstrip() for line in svg.read_text(encoding="utf-8").splitlines())+"\n",encoding="utf-8")
plt.close(fig)
