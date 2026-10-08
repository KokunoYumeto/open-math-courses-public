"""Exact coordinate projections for GP10, GP12 and GP32. CC0-1.0."""
from pathlib import Path
import hashlib,json
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
ROOT=Path(__file__).resolve().parents[1]
plt.rcParams.update({"svg.fonttype":"none","font.size":10,"svg.hashsalt":"AN04-GHP-20261008"})
fig,ax=plt.subplots(1,3,figsize=(13,4.5),layout="constrained")
u=np.linspace(-.75,.75,301)
ax[0].axhspan(0,.65,color="#e4f4ef")
ax[0].plot(-u,u*u,color="#007f97",lw=2)
ax[0].scatter([0],[0],color="#172b44",s=28,zorder=3)
ax[0].set(title="Tangent orbit: physical side (GP32)",xlabel=r"$z_1=-u$",ylabel=r"$r=u^2$",ylim=(-.08,.65))
ax[0].text(-.7,.58,r"$r\geq0$",color="#276a53")
tt=np.linspace(-1,0,301);s=.5
ax[1].axhspan(0,.08,color="#e4f4ef")
ax[1].plot(-tt,tt*tt+tt,color="#b34f0d",lw=2)
ax[1].scatter([0,1],[0,0],color="#172b44",s=28,zorder=3)
ax[1].set(title="Ambient chord: exterior (GP12)",xlabel=r"$z_1=-t$; start $s=1/2$",ylabel=r"$r=t^2+t$",ylim=(-.3,.08))
ax[1].text(.14,-.24,r"$r<0$ between endpoints",fontsize=9)
ss=np.linspace(-.7,.7,301)
ax[2].plot(2*ss,-2*ss**3/3,color="#007f97",lw=2)
ax[2].scatter([0],[0],color="#172b44",s=28,zorder=3)
ax[2].set(title="Two boundary shifts (GP10)",xlabel=r"$\Delta z_1=2s$",ylabel=r"$\Delta z_d=-2s^3/3$")
for a in ax:
 a.axhline(0,color="#718096",lw=.8);a.grid(True,alpha=.2);a.set_axisbelow(True)
fig.suptitle("Homogeneous glancing geometry: exact projections at lambda = 1",fontsize=14)
out=ROOT/"figures/glancing-pair-orbits-and-signs.svg"
fig.savefig(out,metadata={"Date":None,"Creator":"Independent AN-04 mathematical illustration"});plt.close(fig)
record=dict(svg=out.relative_to(ROOT).as_posix(),svg_sha256=hashlib.sha256(out.read_bytes()).hexdigest(),
 generator_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
 exact_formula_locators=["GP10","GP12","GP32"],original_illustration=True,
 numerical_scope="Plots of exact polynomial coordinate projections, not a numerical PDE solution.",
 actually_inspected=False)
(ROOT/"figure-check.json").write_text(json.dumps(record,indent=2)+"\n",encoding="utf-8")
print(json.dumps({"generated":True,"figure":out.name}))
