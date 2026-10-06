"""Render exact lift profiles and samples of the proved dual-norm ratio."""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

root=Path(__file__).resolve().parent
plt.rcParams.update({"font.size":11,"axes.titlesize":12,"svg.fonttype":"none"})
x=np.linspace(-1,1,801)
n=np.arange(1,13)
fig,axes=plt.subplots(1,3,figsize=(14,4.2),constrained_layout=True)
axes[0].plot(x,2-x*x,label=r"$\Phi=2-x^2$",color="#7755aa",linewidth=2)
axes[0].plot(x,1-x*x,label=r"$w_+=1-x^2$",color="#bb4422",linewidth=2)
axes[0].plot(x,x*x-1,label=r"$w_-=x^2-1$",color="#007f8b",linewidth=2)
axes[0].set(title="Actual lift and zero-boundary corrections",xlabel=r"$x\in[-1,1]$",ylabel="Function value",ylim=(-1.2,3.6))
axes[0].legend(loc="upper right",framealpha=.9)
axes[1].plot(x,3-2*x*x,label=r"$u_+=3-2x^2;\ -u_+''=4$",color="#bb4422",linewidth=2)
axes[1].plot(x,np.ones_like(x),label=r"$u_-=1;\ -u_-''=0$",color="#007f8b",linewidth=2)
axes[1].scatter([-1,1],[1,1],color="black",s=25,zorder=5)
axes[1].set(title="Same boundary values, different equations",xlabel=r"$x\in[-1,1]$",ylabel="Function value",ylim=(.6,4.6))
axes[1].legend(loc="upper center",framealpha=.9)
axes[2].plot(n,np.sqrt((n+1)/n),"o",color="#7755aa",label=r"$\sqrt{(n+1)/n}$")
axes[2].axhline(1,color="#444444",linestyle="--",label="Printed bound would require ratio ≤ 1")
axes[2].set(title=r"$\Omega=(0,\pi)^n,\ A=I,\ \lambda_{\rm V}=1$",xlabel=r"Dimension $n$",ylabel=r"$\|\nabla u\|_2/(\lambda_{\rm V}\|F\|_{1,*})$",ylim=(.98,1.46),xticks=[1,2,4,6,8,10,12])
axes[2].legend(loc="upper right",fontsize=9)
for ax in axes:
    ax.grid(alpha=.2)
fig.savefig(root/"vessella-dirichlet-comparison.svg",metadata={"Date":None})
fig.savefig(root/"vessella-dirichlet-comparison.png",dpi=180)
plt.close(fig)
