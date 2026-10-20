"""Exact scale bounds and samples of the planar continuous-forcing example.

Original illustration by GPT-6 Astra (OpenAI), CC0 1.0.
The accompanying lesson proves M14, M46 and M54 analytically.
"""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

plt.rcParams.update({"font.size":11,"svg.hashsalt":"AN01-annular-endpoints-v1"})
out=Path(__file__).resolve().parent
fig,axes=plt.subplots(1,3,figsize=(13.5,4.5),layout="constrained")
z=np.geomspace(2**-8,2**8,1001)
for eps,color in [(.5,"#23618f"),(1.,"#a34d22")]:
    axes[0].loglog(z,np.minimum(z,z**(-eps)),color=color,lw=2,
                  label=rf"$\varepsilon={eps:g}$")
axes[0].axvline(1,color="#777777",lw=.8,ls=":")
axes[0].set(xlabel=r"Relative scale $z=2^j\ell$",
            ylabel=r"$\min(z,z^{-\varepsilon})$",
            title="Cancellation and tails")
axes[0].legend();axes[0].grid(alpha=.2,which="both")
j=np.arange(0,65)
harmonic=np.concatenate(([0.],np.cumsum(1/np.arange(1,65))))
amplitude=harmonic+.5/(j+1)
forcing=30/(j+1)
axes[1].plot(j,amplitude,color="#a34d22",lw=1.6)
axes[1].scatter(j[::4],amplitude[::4],color="#a34d22",s=15)
axes[1].set(xlabel=r"Annulus index $j$",
            ylabel=r"$u(x_j)/|x_j|^2$",
            title="Accumulating quadratic coefficient")
axes[1].text(.06,.9,r"$H_j+\frac{1}{2(j+1)}$",transform=axes[1].transAxes,fontsize=14)
axes[1].grid(alpha=.2)
axes[2].plot(j,forcing/30,color="#23618f",lw=1.6)
axes[2].scatter(j[::4],(forcing/30)[::4],color="#23618f",s=15)
axes[2].set(xlabel=r"Annulus index $j$",
            ylabel=r"$P(D)u(x_j)/30$",
            title="Forcing tends to zero")
axes[2].text(.46,.78,r"$\frac{1}{j+1}$",transform=axes[2].transAxes,fontsize=15)
axes[2].grid(alpha=.2)
fig.suptitle(r"Planar samples: $x_j=(3\,2^{-j}/4,0)$, $P(D)=-\Delta$, $U=x_1^2-x_2^2+x_1x_2$",
             fontsize=12)
fig.savefig(out/"annular-cancellation-and-continuous-endpoint.png",dpi=160)
svg=out/"annular-cancellation-and-continuous-endpoint.svg"
fig.savefig(svg,metadata={"Date":None})
svg.write_text("\n".join(line.rstrip() for line in svg.read_text(encoding="utf-8").splitlines())+"\n",encoding="utf-8")
plt.close(fig)
